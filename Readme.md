# ISO 27001 GRC Management Platform

> Educational prototype — fictional data only — not an ISO 27001 compliance or certification system.

## Current demo

The Flask and SQLite MVP implements a fictional asset and risk register, 1–5 likelihood and impact assessment, risk treatment, seven selected Ikigai controls, risk-to-control links, limited Statement of Applicability decisions, evidence metadata references, submission, independent review decisions, and audit history. It does not accept evidence files or real personal, financial, credential, or production information.

Run `python3 -m pip install -r requirements.txt` and `python3 app/app.py`, then open `http://127.0.0.1:8000`. Select a fictional demo identity in the header. This selector is a demonstration context and is not production authentication. Run the workflow check with `python3 -m unittest discover -s app/tests -v`.

The five sidebar destinations are Dashboard, Asset Register, Risk Register, Reviews and Approvals, and Audit History. Other modules described below remain future plans.

## Deploy to Vercel

Vercel automatically detects `app/app.py` as a Flask application. Import this GitHub repository in Vercel, leave the framework preset and build/output settings on their detected defaults, and add a secret environment variable named `GRC_SESSION_KEY` for Production, Preview, and Development. Generate its value locally with `python3 -c "import secrets; print(secrets.token_hex(32))"`; do not commit the value.

This repository uses SQLite. On Vercel it is placed in `/tmp`, because a Function's deployed filesystem is read-only. The resulting database is suitable only for a portfolio demonstration: records can reset on a cold start, redeployment, or a request served by a different Function instance. A durable multi-user deployment must migrate the database to a persistent service such as a Vercel Marketplace Postgres provider before it is treated as production.

After the first deployment, open the Vercel URL and exercise the demo workflow. Future pushes to `main` create new production deployments when Git integration is enabled; pushes to other branches create previews.

## Repository structure

- `GRC-Documentation/` — project documentation and GRC source-of-truth records
- `UI-UX/` — Jinja page templates and the shared stylesheet
- `app/` — Flask application code and automated workflow tests

The root contains only the README and the small configuration files required by Python, Git, and Vercel.

A learning project for understanding and applying Governance, Risk, and Compliance (GRC) concepts through a small ISO/IEC 27001:2022-inspired web application.

> **Important:** This is an educational project. It is not a certified ISO 27001 compliance product and does not claim that an organization is compliant with ISO/IEC 27001.

## Project purpose

The goal of this project is to build a simple system that helps a fictional organization manage information-security risks, controls, Statement of Applicability (SoA) decisions, evidence, reviews, approvals, and audit history.

This project is being developed while learning about:

- Governance, Risk, and Compliance (GRC)
- Information Security Management Systems (ISMS)
- ISO/IEC 27001:2022 concepts
- Risk assessment and treatment
- Security controls
- Evidence management
- Internal review and approval workflows
- Audit trails

## Problem being addressed

Small organizations often track risks, controls, evidence, and approvals in separate spreadsheets, documents, and email conversations. This project explores how those activities could be organized in one application.

The intended workflow is:

> **Risk → Control → SoA decision → Evidence → Review → Approval → Audit history**

## Planned capabilities

The first version is expected to include:

- Organization and ISMS-scope details
- User roles and permissions
- Risk register
- Risk-to-control mapping
- ISO 27001 control library
- Statement of Applicability records
- Control owners and implementation status
- Evidence records
- Review and approval workflow
- Audit-history records
- Basic dashboard metrics and filters

The scope may change as the project develops. Changes will be recorded in the project documentation.

## Intended users

The initial design considers these user roles:

- **Administrator:** Manages users and basic system settings.
- **GRC Analyst:** Creates and maintains risks, controls, and SoA records.
- **Control Owner:** Updates assigned controls and submits evidence.
- **Reviewer/Approver:** Reviews submissions and approves or rejects them.
- **Read-only Auditor:** Views relevant records and audit history.

These roles are design assumptions for the learning project and may be revised after further analysis.

## Technology stack

- Frontend: server-rendered Jinja templates and CSS
- Backend: Python 3.12 and Flask
- Database: SQLite locally; temporary SQLite under `/tmp` in the Vercel portfolio demo
- Authentication: fictional role-selector session for demonstration only
- File storage: no evidence-file upload; fictional metadata references only

## Documentation

- [Project scope](GRC-Documentation/project-scope.md)
- [Functional requirements](GRC-Documentation/Functional-requirements.md)
- [User roles and permissions](GRC-Documentation/Roles-and-Permission%20.md)
- [Workflows and statuses](GRC-Documentation/Workflows-and-status.md)
- Tests: `app/tests/test_sessions.py`

## Current status

**Status:** Educational first vertical-slice MVP, with further modules planned

### Completed

- Selected ISO 27001 Statement of Applicability and control tracking as the initial project direction.
- Started learning ISO/IEC 27001:2022 and ISMS fundamentals.
- Defined the initial GRC workflow.

### In progress

- Finalizing the fictional organization and ISMS scope.
- Identifying initial information assets and risks.
- Designing the requirements and data model.

### Planned next steps

1. Finalize the organization profile and ISMS scope.
2. Define the first five risks.
3. Define the first set of controls in my own words.
4. Document the SoA fields and workflow.
5. Design the database entities and relationships.
6. Select the technology stack.
7. Build the first vertical slice of the application.
8. Test the risk-to-control-to-evidence workflow.

## Disclaimer

This repository is for learning and portfolio purposes. It does not provide legal, audit, certification, or compliance advice. ISO/IEC 27001 requirements should be interpreted using the official standard and qualified professional guidance where necessary.
