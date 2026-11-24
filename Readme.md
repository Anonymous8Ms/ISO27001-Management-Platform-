# Ikigai GRC Management Platform

An educational Governance, Risk, and Compliance (GRC) management platform inspired by ISO/IEC 27001:2022 concepts.

The project models a fictional EdTech organization named **Ikigai** and demonstrates how information-security assets, risks, treatments, reviews, approvals, and audit history can be managed in one application.

> **Important:** This is an educational prototype. It is not an ISO 27001-certified product, does not prove compliance, and must not be used to store real personal, financial, credential, or confidential information.

## Live Demo

[Open the Ikigai GRC platform](https://iso-27001-management-platform.vercel.app/)

The live demo uses fictional data only.

## Project Purpose

Small organizations may manage security risks, ownership, approvals, and audit records across separate spreadsheets and documents. This project demonstrates how those activities can be organized through a simple GRC workflow.

The application was created as a learning project while studying:

- Governance, Risk, and Compliance

- Information Security Management Systems

- ISO/IEC 27001:2022 concepts

- Information-asset management

- Risk assessment and treatment

- Role-based access principles

- Review and approval workflows

- Audit trails

## Fictional Organization

**Organization:** Ikigai
**Industry:** Education Technology (EdTech)

Ikigai provides online courses, live classes, mock tests, and career-preparation programs. Its fictional information-security scope includes student information, application services, cloud infrastructure, employee information, finance-related information, vendors, and security records.

No real organization, student, employee, customer, payment, credential, or confidential information is used in this project.

## Implemented Features

### Dashboard

- Security-posture summary

- Registered asset count

- Open-risk count

- Critical-risk count

- Awaiting-review count

- Recent audit activity

### Asset Register

- Create fictional information assets

- Assign an owner or responsible team

- Record asset description and information type

- Record importance and security concerns

- View registered assets

### Risk Register

- Create information-security risks

- Link a risk to an information asset

- Record threat, vulnerability, and potential impact

- Assess likelihood and impact on a 1–5 scale

- Calculate the risk rating

- Select a treatment option

- Record treatment actions and review date

- View risk details and status

### Reviews and Approvals

- View risks submitted for review

- Add a review comment

- Approve a submission

- Reject a submission

- Request changes

- Apply reviewer permissions through the demonstration role model

### Audit History

- Append-only record of important actions

- Records asset and risk creation

- Records review submissions

- Records approval-related actions

- Records role changes and denied actions

- Displays actor, action, entity, timestamp, and change details

### Demonstration Roles

The application includes a role selector for demonstrating basic access behavior:

- **Administrator**

- **GRC Analyst**

- **Control Owner**

- **Reviewer/Approver**

- **Read-only Auditor**

The role selector is a demonstration feature and is not production authentication.

## Demonstrated Workflow

The current prototype demonstrates:

> **Asset → Risk Assessment → Treatment → Review → Approval Decision → Audit History**

The application focuses on the implemented risk-management and review workflow. It does not claim to be a complete ISO 27001 compliance-management system.

## Technology

The application is a lightweight web prototype with server-rendered pages, form-based interactions, session-based demonstration roles, and fictional sample records. It is deployed on Vercel.

## Data and Privacy Boundary

The platform is intended for fictional GRC records only. Do not enter:

- Real student or customer information

- Real employee information

- Payment or financial records

- Passwords, API keys, or credentials

- Confidential evidence or business documents

- Personal information belonging to real individuals

## Project Scope

The project scope and fictional Ikigai organization are documented in [`docs/project-scope.md`](docs/project-scope.md).

## Portfolio Disclaimer

This project demonstrates GRC thinking and workflow design for learning and portfolio purposes. It is not legal, audit, certification, privacy, or compliance advice. ISO/IEC 27001 requirements should be interpreted using the official standard and qualified professional guidance.
