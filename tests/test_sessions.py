import os
import tempfile
import unittest
import app as grc

class SessionPermissions(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.old=grc.DB_PATH
        grc.DB_PATH=os.path.join(self.tmp.name,'test.db')
        grc.init_db()
        self.c=grc.app.test_client()
        self.c.get('/')
    def tearDown(self):
        grc.DB_PATH=self.old
        self.tmp.cleanup()
    def post(self,path,data=None):
        with self.c.session_transaction() as s: token=s['csrf']
        return self.c.post(path,data={**(data or {}),'csrf':token})
    def switch(self,user): return self.post('/demo/identity',{'user_id':user})
    def test_requested_workflow(self):
        asset=dict(name='Fictional asset',owner='Demo team',description='Demo',information='Metadata',importance='High',concerns='Availability')
        self.switch(4)
        self.assertEqual(self.post('/assets?as_user=1',asset).status_code,403)
        self.c.get('/risks'); self.c.get('/')
        with self.c.session_transaction() as s: self.assertEqual(s['user_id'],4)
        self.switch(1)
        self.assertEqual(self.post('/assets',asset).status_code,302)
        risk=dict(title='Demo outage',asset_id=1,threat='Outage',vulnerability='Single region',impact_text='Service interruption',owner='Demo team',likelihood=3,impact=5,treatment='Treat',actions='Recovery exercise',approval_authority='Senior Management',review_date='2030-01-01')
        self.assertEqual(self.post('/risks',risk).status_code,302)
        self.assertEqual(self.post('/risks/1/treatment',{'option':'Treat','actions':'Recovery and restore exercise','status':'In Progress'}).status_code,302)
        self.assertEqual(self.post('/risks/1/control',{'control_ref':'A.8.13'}).status_code,302)
        self.assertEqual(self.post('/risks/1/soa',{'control_ref':'A.8.13','applicable':'1','justification':'Backups address the fictional outage','owner':'Demo team'}).status_code,302)
        self.assertEqual(self.post('/soa/1/submit').status_code,400)
        self.assertEqual(self.post('/soa/1/evidence',{'name':'Fictional restoration log','period':'Q1 2030','owner':'Ikigai IT Operations','reference':'FICTIONAL-BACKUP-001'}).status_code,302)
        self.assertEqual(self.post('/soa/1/submit').status_code,302)
        self.assertEqual(self.post('/risks/1/residual',{'likelihood':'2','impact':'4','decision':'Treat','reason':'Recovery exercise planned','approver':'Senior Management','review_date':'2030-02-01'}).status_code,302)
        self.assertEqual(self.post('/risks/1/review',{'decision':'Submitted for Review'}).status_code,302)
        self.assertEqual(self.post('/risks/1/review',{'decision':'Approved'}).status_code,403)
        self.switch(2)
        self.assertEqual(self.post('/risks/1/review',{'decision':'Rejected'}).status_code,400)
        self.assertEqual(self.post('/risks/1/review',{'decision':'Rejected','comment':'Revise treatment'}).status_code,302)
        self.switch(1)
        self.post('/risks/1/review',{'decision':'Submitted for Review'})
        self.switch(2)
        self.assertEqual(self.post('/risks/1/review',{'decision':'Approved'}).status_code,302)
        with grc.app.app_context():
            actions=[r[0] for r in grc.db().execute('SELECT action FROM audit')]
            for action in ['Demo identity changed','Access denied','Created','Submitted for Review','Rejected','Approved','Treatment updated','Linked control','Residual risk reviewed','Submitted']: self.assertIn(action,actions)
            self.assertEqual(grc.db().execute('SELECT COUNT(*) FROM controls').fetchone()[0],7)
            self.assertEqual(grc.db().execute('SELECT COUNT(*) FROM evidence').fetchone()[0],1)
            self.assertEqual(self.post('/soa/1/decision',{'decision':'Approved'}).status_code,302)
            self.assertEqual(grc.db().execute("SELECT decision FROM decisions WHERE entity_type='SoA'").fetchone()[0],'Approved')
        self.switch(5)
        self.assertEqual(self.c.get('/risks').status_code,403)
        self.assertEqual(self.c.get('/modules/users').status_code,200)
        self.switch(4)
        for name in grc.MODULES:
            self.assertEqual(self.c.get('/modules/'+name).status_code,403 if name=='users' else 200)
