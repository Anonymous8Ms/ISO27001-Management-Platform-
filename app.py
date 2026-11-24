from datetime import datetime, timezone
from functools import wraps
import json
import os
import sqlite3
from flask import Flask, abort, g, redirect, render_template, request, url_for, session
import secrets

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IS_VERCEL = bool(os.environ.get("VERCEL"))


def session_key():
    configured_key = os.environ.get("GRC_SESSION_KEY")
    if configured_key:
        return configured_key
    if IS_VERCEL:
        # Vercel's deployment filesystem is read-only. Set GRC_SESSION_KEY in
        # project settings so demo sessions remain valid between instances.
        return secrets.token_hex(32)
    key_path = os.path.join(BASE_DIR, ".grc-session-key")
    if not os.path.exists(key_path):
        with open(key_path, "w", encoding="utf-8") as key_file:
            key_file.write(secrets.token_hex(32))
        os.chmod(key_path, 0o600)
    with open(key_path, encoding="utf-8") as key_file:
        return key_file.read().strip()


app.secret_key = session_key()
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Strict",
    SESSION_COOKIE_SECURE=IS_VERCEL,
)
default_db_path = "/tmp/ikigai-grc.sqlite3" if IS_VERCEL else os.path.join(BASE_DIR, "grc.sqlite3")
DB_PATH = os.environ.get("GRC_DB", default_db_path)
ROLES = ["Administrator", "GRC Analyst", "Control Owner", "Reviewer/Approver", "Read-only Auditor"]
CONTROLS = [
    ("A.5.15", "Access Control and Least Privilege"),
    ("A.8.25", "Secure Development and Change Management"),
    ("A.8.8", "Vulnerability and Patch Management"),
    ("A.8.13", "Backup and Recovery"),
    ("A.5.19", "Supplier Security and Third-Party Risk Management"),
    ("A.6.3", "Information-Security Awareness, Education and Training"),
    ("A.5.24", "Information-Security Incident Management"),
]

def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys=ON")
    return g.db

@app.teardown_appcontext
def close_db(_error):
    conn = g.pop("db", None)
    if conn:
        conn.close()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
    PRAGMA foreign_keys=ON;
    CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT NOT NULL, role TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS assets(id INTEGER PRIMARY KEY, name TEXT NOT NULL, owner TEXT NOT NULL, description TEXT NOT NULL, information TEXT NOT NULL, importance TEXT NOT NULL, concerns TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Active', created_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS risks(id INTEGER PRIMARY KEY, title TEXT NOT NULL, asset_id INTEGER NOT NULL REFERENCES assets(id), threat TEXT NOT NULL, vulnerability TEXT NOT NULL, impact_text TEXT NOT NULL, owner TEXT NOT NULL, likelihood INTEGER NOT NULL CHECK(likelihood BETWEEN 1 AND 5), impact INTEGER NOT NULL CHECK(impact BETWEEN 1 AND 5), rating INTEGER NOT NULL, level TEXT NOT NULL, treatment TEXT NOT NULL, actions TEXT NOT NULL, approval_authority TEXT NOT NULL, residual_risk TEXT NOT NULL DEFAULT '', review_date TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Draft', created_by INTEGER NOT NULL REFERENCES users(id), version INTEGER NOT NULL DEFAULT 1);
    CREATE TABLE IF NOT EXISTS treatments(id INTEGER PRIMARY KEY, risk_id INTEGER NOT NULL REFERENCES risks(id), option TEXT NOT NULL, actions TEXT NOT NULL, owner TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Planned');
    CREATE TABLE IF NOT EXISTS risk_controls(risk_id INTEGER NOT NULL REFERENCES risks(id), control_ref TEXT NOT NULL, control_name TEXT NOT NULL, PRIMARY KEY(risk_id, control_ref));
    CREATE TABLE IF NOT EXISTS soa(id INTEGER PRIMARY KEY, risk_id INTEGER NOT NULL REFERENCES risks(id), control_ref TEXT NOT NULL, control_name TEXT NOT NULL, applicable INTEGER NOT NULL, justification TEXT NOT NULL, owner TEXT NOT NULL, implementation_status TEXT NOT NULL DEFAULT 'Planned', status TEXT NOT NULL DEFAULT 'Draft', creator_id INTEGER NOT NULL REFERENCES users(id), approver_id INTEGER REFERENCES users(id), decision_comment TEXT DEFAULT '', version INTEGER NOT NULL DEFAULT 1);
    CREATE TABLE IF NOT EXISTS audit(id INTEGER PRIMARY KEY, actor_id INTEGER NOT NULL REFERENCES users(id), timestamp TEXT NOT NULL, action TEXT NOT NULL, entity_type TEXT NOT NULL, entity_id INTEGER NOT NULL, previous_value TEXT, new_value TEXT, comment TEXT DEFAULT '', transition TEXT DEFAULT '');
    CREATE TABLE IF NOT EXISTS revisions(id INTEGER PRIMARY KEY, entity_type TEXT NOT NULL, entity_id INTEGER NOT NULL, version INTEGER NOT NULL, snapshot TEXT NOT NULL, saved_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS residual_reviews(id INTEGER PRIMARY KEY, risk_id INTEGER NOT NULL REFERENCES risks(id), likelihood INTEGER NOT NULL CHECK(likelihood BETWEEN 1 AND 5), impact INTEGER NOT NULL CHECK(impact BETWEEN 1 AND 5), rating INTEGER NOT NULL, level TEXT NOT NULL, decision TEXT NOT NULL, reason TEXT NOT NULL, approver TEXT NOT NULL, review_date TEXT NOT NULL, actor_id INTEGER NOT NULL REFERENCES users(id), created_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS controls(ref TEXT PRIMARY KEY, name TEXT NOT NULL, owner TEXT NOT NULL, implementation_status TEXT NOT NULL DEFAULT 'Planned');
    CREATE TABLE IF NOT EXISTS evidence(id INTEGER PRIMARY KEY, soa_id INTEGER NOT NULL REFERENCES soa(id), control_ref TEXT NOT NULL REFERENCES controls(ref), name TEXT NOT NULL, period TEXT NOT NULL, owner TEXT NOT NULL, reference TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Draft', creator_id INTEGER NOT NULL REFERENCES users(id), created_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS decisions(id INTEGER PRIMARY KEY, entity_type TEXT NOT NULL, entity_id INTEGER NOT NULL, reviewer_id INTEGER NOT NULL REFERENCES users(id), decided_at TEXT NOT NULL, decision TEXT NOT NULL, comment TEXT NOT NULL DEFAULT '');
    """)
    if 'implementation_status' not in [column[1] for column in conn.execute('PRAGMA table_info(soa)')]:
        conn.execute("ALTER TABLE soa ADD COLUMN implementation_status TEXT NOT NULL DEFAULT 'Planned'")
    users = [(1,"Asha Analyst","GRC Analyst"),(2,"Ravi Reviewer","Reviewer/Approver"),(3,"Mira Owner","Control Owner"),(4,"Ira Auditor","Read-only Auditor"),(5,"Admin User","Administrator")]
    conn.executemany("INSERT OR IGNORE INTO users(id,name,role) VALUES(?,?,?)", users)
    conn.executemany("INSERT OR IGNORE INTO controls(ref,name,owner) VALUES(?,?,?)", [(ref,name,{'A.8.25':'Head of Engineering','A.6.3':'Head of People','A.5.24':'Incident Manager'}.get(ref,'Head of IT Operations')) for ref,name in CONTROLS])
    conn.commit(); conn.close()

def actor():
    user_id = session.get("user_id", 1)
    try: user_id = int(user_id)
    except ValueError: user_id = 1
    return db().execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone() or db().execute("SELECT * FROM users WHERE id=1").fetchone()

@app.before_request
def set_actor():
    g.user = actor()
    if request.method == 'POST' and request.form.get('csrf') != session.get('csrf'):
        abort(400, 'Session verification failed. Refresh the page and try again.')
    session.setdefault('csrf', secrets.token_hex(24))
    if g.user['role']=='Administrator' and request.endpoint not in ('static', 'switch_user', 'dashboard', 'module'):
        abort(403)
    if g.user['role']=='Control Owner' and request.endpoint not in ('static', 'switch_user', 'dashboard', 'module', 'risk_detail', 'create_evidence'):
        abort(403)

@app.post('/demo/identity')
def switch_user():
    user = db().execute('SELECT * FROM users WHERE id=?', (request.form.get('user_id'),)).fetchone()
    if not user: abort(400, 'Unknown demo identity')
    audit('Demo identity changed', 'User', user['id'], old=g.user['id'], new=user['id'])
    db().commit()
    session['user_id'] = user['id']
    return redirect(url_for('dashboard'))

def roles(*allowed):
    def deco(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            if g.user["role"] not in allowed: abort(403)
            return fn(*args, **kwargs)
        return wrapped
    return deco

def audit(action, typ, ident, old=None, new=None, comment="", transition=""):
    db().execute("INSERT INTO audit(actor_id,timestamp,action,entity_type,entity_id,previous_value,new_value,comment,transition) VALUES(?,?,?,?,?,?,?,?,?)",
        (g.user["id"], datetime.now(timezone.utc).isoformat(), action, typ, ident, json.dumps(old, default=str) if old is not None else None, json.dumps(new, default=str) if new is not None else None, comment, transition))

@app.context_processor
def inject(): return {"users": db().execute("SELECT * FROM users ORDER BY id").fetchall(), "controls": CONTROLS}

@app.get("/")
def dashboard():
    if g.user['role'] in ('Administrator', 'Control Owner'):
        return render_template('module.html', title='Demo workspace', message='Use the navigation to view your available modules. GRC details are restricted for this identity.', rows=[])
    conn=db()
    return render_template("dashboard.html", assets=conn.execute("SELECT COUNT(*) FROM assets").fetchone()[0], risks=conn.execute("SELECT COUNT(*) FROM risks").fetchone()[0], reviews=conn.execute("SELECT COUNT(*) FROM soa WHERE status IN ('Submitted for Review','Under Review')").fetchone()[0], critical=conn.execute("SELECT COUNT(*) FROM risks WHERE level='Critical' AND status!='Closed'").fetchone()[0], recent=conn.execute("SELECT a.*,u.name actor FROM audit a JOIN users u ON u.id=a.actor_id ORDER BY a.id DESC LIMIT 6").fetchall())

@app.get("/assets")
def assets(): return render_template("assets.html", rows=db().execute("SELECT * FROM assets ORDER BY id DESC").fetchall())

@app.post("/assets")
@roles("Administrator","GRC Analyst")
def create_asset():
    f=request.form
    cur=db().execute("INSERT INTO assets(name,owner,description,information,importance,concerns,created_at) VALUES(?,?,?,?,?,?,?)",(f["name"],f["owner"],f["description"],f["information"],f["importance"],f["concerns"],datetime.now(timezone.utc).isoformat()))
    audit("Created","Asset",cur.lastrowid,new=dict(f)); db().commit(); return redirect(url_for("assets",as_user=g.user["id"]))

def risk_level(score): return "Low" if score<=4 else "Medium" if score<=9 else "High" if score<=16 else "Critical"

@app.get("/risks")
def risks(): return render_template("risks.html", rows=db().execute("SELECT r.*,a.name asset FROM risks r JOIN assets a ON a.id=r.asset_id ORDER BY r.id DESC").fetchall(), assets=db().execute("SELECT * FROM assets ORDER BY name").fetchall())

@app.post("/risks")
@roles("Administrator","GRC Analyst")
def create_risk():
    f=request.form
    required=('title','asset_id','threat','vulnerability','impact_text','owner','likelihood','impact','treatment','actions','approval_authority','review_date')
    if any(not f.get(field,'').strip() for field in required): abort(400,'Complete every required risk field.')
    if f['treatment'] not in ('Treat','Avoid','Transfer','Accept'): abort(400,'Invalid treatment option.')
    try:
        likelihood=int(f["likelihood"]); impact=int(f["impact"])
        if not 1<=likelihood<=5 or not 1<=impact<=5: raise ValueError()
    except ValueError: abort(400,"Likelihood and impact must be 1–5")
    if not db().execute("SELECT 1 FROM assets WHERE id=?",(f["asset_id"],)).fetchone(): abort(400,"Select a valid asset")
    score=likelihood*impact
    cur=db().execute("INSERT INTO risks(title,asset_id,threat,vulnerability,impact_text,owner,likelihood,impact,rating,level,treatment,actions,approval_authority,review_date,created_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(f["title"],f["asset_id"],f["threat"],f["vulnerability"],f["impact_text"],f["owner"],likelihood,impact,score,risk_level(score),f["treatment"],f["actions"],f["approval_authority"],f["review_date"],g.user["id"]))
    risk_id=cur.lastrowid
    db().execute("INSERT INTO treatments(risk_id,option,actions,owner) VALUES(?,?,?,?)",(risk_id,f["treatment"],f["actions"],f["owner"]))
    audit("Created","Risk",risk_id,new={"title":f["title"],"asset_id":f["asset_id"],"rating":score,"level":risk_level(score)})
    db().commit(); return redirect(url_for("risk_detail",risk_id=risk_id,as_user=g.user["id"]))

@app.get("/risks/<int:risk_id>")
def risk_detail(risk_id):
    conn=db(); risk=conn.execute("SELECT r.*,a.name asset FROM risks r JOIN assets a ON a.id=r.asset_id WHERE r.id=?",(risk_id,)).fetchone()
    if not risk: abort(404)
    return render_template("risk_detail.html",risk=risk,mappings=conn.execute("SELECT * FROM risk_controls WHERE risk_id=?",(risk_id,)).fetchall(),soas=conn.execute("SELECT s.*,u.name creator,au.name approver FROM soa s JOIN users u ON u.id=s.creator_id LEFT JOIN users au ON au.id=s.approver_id WHERE risk_id=?",(risk_id,)).fetchall(),treatment=conn.execute("SELECT * FROM treatments WHERE risk_id=?",(risk_id,)).fetchone(),residual=conn.execute('SELECT * FROM residual_reviews WHERE risk_id=? ORDER BY id DESC LIMIT 1',(risk_id,)).fetchone(),evidence=conn.execute('SELECT * FROM evidence WHERE soa_id IN (SELECT id FROM soa WHERE risk_id=?) ORDER BY id DESC',(risk_id,)).fetchall())

@app.get('/risks/<int:risk_id>/workflow')
def risk_workflow(risk_id):
    conn=db()
    risk=conn.execute('SELECT * FROM risks WHERE id=?',(risk_id,)).fetchone()
    if not risk: abort(404)
    return render_template('workflow.html',risk=risk,treatment=conn.execute('SELECT * FROM treatments WHERE risk_id=?',(risk_id,)).fetchone(),residual=conn.execute('SELECT * FROM residual_reviews WHERE risk_id=? ORDER BY id DESC LIMIT 1',(risk_id,)).fetchone(),mappings=conn.execute('SELECT * FROM risk_controls WHERE risk_id=?',(risk_id,)).fetchall(),soas=conn.execute('SELECT * FROM soa WHERE risk_id=?',(risk_id,)).fetchall())

@app.post("/risks/<int:risk_id>/control")
@roles("Administrator","GRC Analyst")
def map_control(risk_id):
    ref=request.form["control_ref"]; control=next((x for x in CONTROLS if x[0]==ref),None)
    if not control: abort(400)
    db().execute("INSERT OR IGNORE INTO risk_controls VALUES(?,?,?)",(risk_id,*control)); audit("Linked control","Risk",risk_id,new={"control_ref":ref}); db().commit(); return redirect(url_for("risk_detail",risk_id=risk_id,as_user=g.user["id"]))

@app.post("/risks/<int:risk_id>/soa")
@roles("Administrator","GRC Analyst")
def create_soa(risk_id):
    f=request.form
    if not f.get("justification","").strip(): abort(400,"Justification is required")
    control=next((x for x in CONTROLS if x[0]==f.get("control_ref")),None)
    if not control: abort(400)
    if not db().execute('SELECT 1 FROM risk_controls WHERE risk_id=? AND control_ref=?',(risk_id,control[0])).fetchone(): abort(400,'Link the control to this risk first.')
    cur=db().execute("INSERT INTO soa(risk_id,control_ref,control_name,applicable,justification,owner,creator_id,implementation_status) VALUES(?,?,?,?,?,?,?,?)",(risk_id,*control,int(f["applicable"]),f["justification"],f["owner"],g.user["id"],db().execute('SELECT implementation_status FROM controls WHERE ref=?',(control[0],)).fetchone()[0]))
    audit("Created","SoA",cur.lastrowid,new={"risk_id":risk_id,"control_ref":control[0],"applicable":f["applicable"],"justification":f["justification"]}); db().commit(); return redirect(url_for("risk_detail",risk_id=risk_id,as_user=g.user["id"]))

@app.post("/soa/<int:soa_id>/submit")
@roles("Administrator","GRC Analyst","Control Owner")
def submit_soa(soa_id):
    row=db().execute("SELECT * FROM soa WHERE id=?",(soa_id,)).fetchone()
    if not row or row["creator_id"]!=g.user["id"]: abort(403)
    if row['status'] not in ('Draft', 'Rejected', 'Change Requested'): abort(400, 'This record cannot be submitted in its current state.')
    if not db().execute('SELECT 1 FROM evidence WHERE soa_id=?',(soa_id,)).fetchone(): abort(400,'Add fictional evidence metadata before submission.')
    db().execute("UPDATE soa SET status='Submitted for Review' WHERE id=?",(soa_id,))
    db().execute("UPDATE evidence SET status='Submitted' WHERE soa_id=?",(soa_id,))
    audit("Submitted","SoA",soa_id,old=row["status"],new="Submitted for Review",transition=f'{row["status"]} → Submitted for Review'); db().commit(); return redirect(url_for("risk_detail",risk_id=row["risk_id"],as_user=g.user["id"]))

@app.post("/soa/<int:soa_id>/decision")
@roles("Reviewer/Approver")
def decide_soa(soa_id):
    row=db().execute("SELECT * FROM soa WHERE id=?",(soa_id,)).fetchone()
    if not row or row["creator_id"]==g.user["id"]: abort(403)
    if row['status'] not in ('Submitted for Review', 'Under Review'): abort(400, 'Only submitted records can be reviewed.')
    decision=request.form.get("decision"); comment=request.form.get("comment","").strip()
    if decision not in ("Approved","Rejected","Change Requested"): abort(400)
    if decision in ("Rejected","Change Requested") and not comment: abort(400,"A comment is required")
    prev=dict(row); db().execute("INSERT INTO revisions(entity_type,entity_id,version,snapshot,saved_at) VALUES('SoA',?,?,?,?)",(soa_id,row["version"],json.dumps(prev,default=str),datetime.now(timezone.utc).isoformat()))
    db().execute("UPDATE soa SET status=?,approver_id=?,decision_comment=?,version=version+1 WHERE id=?",(decision,g.user["id"],comment,soa_id))
    db().execute('UPDATE evidence SET status=? WHERE soa_id=?',({'Approved':'Accepted','Rejected':'Rejected','Change Requested':'Rejected'}[decision],soa_id))
    db().execute('INSERT INTO decisions(entity_type,entity_id,reviewer_id,decided_at,decision,comment) VALUES(?,?,?,?,?,?)',('SoA',soa_id,g.user['id'],datetime.now(timezone.utc).isoformat(),decision,comment))
    audit(decision,"SoA",soa_id,old=prev,new={"status":decision,"approver":g.user["name"]},comment=comment,transition=f'{row["status"]} → {decision}'); db().commit(); return redirect(url_for("risk_detail",risk_id=row["risk_id"],as_user=g.user["id"]))

@app.post('/soa/<int:soa_id>/evidence')
@roles('GRC Analyst','Control Owner')
def create_evidence(soa_id):
    row=db().execute('SELECT * FROM soa WHERE id=?',(soa_id,)).fetchone()
    if not row: abort(404)
    if g.user['role']=='GRC Analyst' and row['creator_id']!=g.user['id']: abort(403)
    if g.user['role']=='Control Owner' and row['owner']!=g.user['name']: abort(403)
    if row['status'] not in ('Draft','Rejected','Change Requested'): abort(400,'Evidence can be added before submission or after changes are requested.')
    f=request.form
    if any(not f.get(k,'').strip() for k in ('name','period','owner','reference')): abort(400,'Complete all evidence metadata fields.')
    if not f['reference'].startswith('FICTIONAL-'): abort(400,'Use a fictional reference beginning FICTIONAL-.')
    cur=db().execute('INSERT INTO evidence(soa_id,control_ref,name,period,owner,reference,creator_id,created_at) VALUES(?,?,?,?,?,?,?,?)',(soa_id,row['control_ref'],f['name'],f['period'],f['owner'],f['reference'],g.user['id'],datetime.now(timezone.utc).isoformat()))
    audit('Created','Evidence',cur.lastrowid,new={'soa_id':soa_id,'control_ref':row['control_ref'],'name':f['name'],'reference':f['reference']})
    db().commit(); return redirect(url_for('risk_detail',risk_id=row['risk_id']))

@app.get("/audit")
def audit_history(): return render_template("audit.html",rows=db().execute("SELECT a.*,u.name actor FROM audit a JOIN users u ON u.id=a.actor_id ORDER BY a.id DESC").fetchall())

@app.errorhandler(403)
def forbidden(_):
    db().rollback()
    audit('Access denied', 'Permission', g.user['id'], new={'endpoint': request.endpoint, 'method': request.method})
    db().commit()
    return render_template("error.html",code=403,message="Access denied: your active role cannot access this page or perform this action."),403

MODULES = {'controls':'Control Library', 'soa':'Statement of Applicability', 'evidence':'Evidence Register', 'reviews':'Reviews and Approvals', 'incidents':'Incident Register', 'vendors':'Vendor Register', 'users':'Users and Roles', 'metrics':'GRC Metrics'}

@app.get('/modules/<name>')
def module(name):
    if name not in MODULES: abort(404)
    role = g.user['role']
    if role == 'Administrator' and name != 'users': abort(403)
    if role == 'Control Owner' and name not in ('controls','evidence'): abort(403)
    if name == 'users' and role != 'Administrator': abort(403)
    if name == 'reviews':
        return render_template('reviews.html', rows=db().execute('SELECT * FROM risks ORDER BY id DESC').fetchall())
    rows=[]
    message='Planned module — editing is not implemented in this MVP.'
    if name == 'controls':
        rows=[f'{ref}: {title}' for ref,title in CONTROLS]
        message='Selected educational controls. Assignment and control editing are planned; Control Owners cannot edit unassigned records.'
    elif name == 'soa':
        rows=[f"{r['control_ref']} · {r['control_name']} · {'Applicable' if r['applicable'] else 'Not applicable'} · {r['justification']} · {r['owner']} · Risk #{r['risk_id']} · {r['implementation_status']} · Review: {r['status']}" for r in db().execute('SELECT * FROM soa')]
        message='Create and submit SoA decisions from the associated risk detail page.'
    elif name == 'users':
        rows=[f"{r['name']} — {r['role']}" for r in db().execute('SELECT * FROM users')]
        message='Fictional platform identities. User and configuration editing are planned.'
    return render_template('module.html',title=MODULES[name],message=message,rows=rows)

@app.post('/risks/<int:risk_id>/review')
def review_risk(risk_id):
    row=db().execute('SELECT * FROM risks WHERE id=?',(risk_id,)).fetchone()
    if not row: abort(404)
    decision=request.form.get('decision')
    comment=request.form.get('comment','').strip()
    if decision == 'Submitted for Review':
        if g.user['role'] != 'GRC Analyst' or row['created_by'] != g.user['id']: abort(403)
        if row['status'] not in ('Draft','Rejected','Change Requested'): abort(400,'Risk is not ready for submission.')
    elif decision == 'Under Review':
        if g.user['role'] != 'Reviewer/Approver' or row['created_by'] == g.user['id']: abort(403)
        if row['status'] != 'Submitted for Review': abort(400,'Risk must be submitted first.')
    else:
        if g.user['role'] != 'Reviewer/Approver' or row['created_by'] == g.user['id']: abort(403)
        if row['status'] not in ('Submitted for Review','Under Review'): abort(400,'Submit the risk before review.')
        if decision not in ('Approved','Rejected','Change Requested'): abort(400,'Invalid decision')
        if decision != 'Approved' and not comment: abort(400,'Rejection and change requests require a comment.')
    db().execute('UPDATE risks SET status=? WHERE id=?',(decision,risk_id))
    if decision in ('Approved','Rejected','Change Requested'):
        db().execute('INSERT INTO decisions(entity_type,entity_id,reviewer_id,decided_at,decision,comment) VALUES(?,?,?,?,?,?)',('Risk',risk_id,g.user['id'],datetime.now(timezone.utc).isoformat(),decision,comment))
    audit(decision,'Risk',risk_id,old=row['status'],new=decision,comment=comment,transition=f"{row['status']} → {decision}")
    db().commit()
    return redirect(url_for('module',name='reviews'))

@app.post('/risks/<int:risk_id>/treatment')
@roles('GRC Analyst')
def update_treatment(risk_id):
    row=db().execute('SELECT * FROM risks WHERE id=?',(risk_id,)).fetchone()
    if not row: abort(404)
    if row['created_by'] != g.user['id'] or row['status'] not in ('Draft','Rejected','Change Requested'): abort(403)
    option=request.form.get('option'); actions=request.form.get('actions','').strip(); status=request.form.get('status')
    if option not in ('Treat','Avoid','Transfer','Accept') or status not in ('Planned','In Progress','Completed') or not actions: abort(400,'Complete treatment details.')
    old=db().execute('SELECT * FROM treatments WHERE risk_id=?',(risk_id,)).fetchone()
    db().execute('UPDATE treatments SET option=?,actions=?,status=? WHERE risk_id=?',(option,actions,status,risk_id))
    db().execute('UPDATE risks SET treatment=?,actions=? WHERE id=?',(option,actions,risk_id))
    audit('Treatment updated','Risk',risk_id,old=dict(old),new={'option':option,'actions':actions,'status':status})
    db().commit(); return redirect(url_for('risk_detail',risk_id=risk_id))

@app.post('/risks/<int:risk_id>/residual')
@roles('GRC Analyst')
def review_residual(risk_id):
    row=db().execute('SELECT * FROM risks WHERE id=?',(risk_id,)).fetchone()
    if not row: abort(404)
    if row['created_by'] != g.user['id']: abort(403)
    f=request.form
    try:
        likelihood=int(f.get('likelihood','')); impact=int(f.get('impact',''))
        if not 1<=likelihood<=5 or not 1<=impact<=5: raise ValueError()
    except ValueError: abort(400,'Residual scores must be 1–5.')
    if f.get('decision') not in ('Treat','Avoid','Transfer','Accept') or any(not f.get(k,'').strip() for k in ('reason','approver','review_date')): abort(400,'Complete residual review fields.')
    rating=likelihood*impact; level=risk_level(rating)
    db().execute('INSERT INTO residual_reviews(risk_id,likelihood,impact,rating,level,decision,reason,approver,review_date,actor_id,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(risk_id,likelihood,impact,rating,level,f['decision'],f['reason'],f['approver'],f['review_date'],g.user['id'],datetime.now(timezone.utc).isoformat()))
    db().execute('UPDATE risks SET residual_risk=? WHERE id=?',(f'{rating} · {level}',risk_id))
    audit('Residual risk reviewed','Risk',risk_id,old=row['residual_risk'],new={'rating':rating,'level':level,'decision':f['decision'],'approver':f['approver'],'review_date':f['review_date']},comment=f['reason'])
    db().commit(); return redirect(url_for('risk_detail',risk_id=risk_id))

@app.errorhandler(400)
def bad_request(error): return render_template("error.html",code=400,message=getattr(error,"description","Invalid request.")),400

init_db()
if __name__=="__main__": app.run(host='127.0.0.1', port=int(os.environ.get('PORT','8000')), debug=False)
