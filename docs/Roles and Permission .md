The file structure :
# Roles and Permissions

## Purpose

## Role Definitions

## Permission Rules

## Approval and Separation of Duties


# Roles and Permissions

## Purpose

This document defines the responsibilities and access rights of users in the Ikigai GRC Management Platform. Permissions follow least privilege and separation-of-duties principles.

## Role Definitions

### Administrator

Manages users, roles, system settings, and platform configuration. The Administrator should normally see only account metadata, such as username, role, status, and last-login information. The Administrator should not view student personal details, employee records, financial records, passwords, evidence files, or sensitive risk details unless explicitly authorized for a documented support or security purpose.


### GRC Analyst

Creates and maintains assets, risks, risk treatments, controls, SoA records, and evidence metadata. The GRC Analyst can submit records for review but should not be the sole approver of their own work.

### Control Owner

Updates controls assigned to them and submits supporting evidence. A Control Owner should not approve their own evidence.

### Reviewer/Approver

Reviews submitted risks, treatments, SoA decisions, controls, and evidence. The Reviewer/Approver can approve, reject, or request changes.

### Read-only Auditor

Views relevant assets, risks, controls, SoA records, evidence, approvals, and audit history. The Read-only Auditor cannot create, edit, approve, or delete GRC records.

## Permission Matrix

| Activity | Administrator | GRC Analyst | Control Owner | Reviewer/Approver | Read-only Auditor |
|---|---|---|---|---|---|
| Manage users and roles | Yes, but not sensitive user data | No | No | No | No |
| View assets | Metadata and authorized records | Yes | Assigned assets | Yes | Yes |
| Create or edit assets | Yes | Yes | Assigned assets | No | No |
| Create or edit risks | Yes | Yes | Assigned risks | No | No |
| Assess risks | Yes | Yes | Assigned risks | Review | View |
| Create risk treatments | Yes | Yes | Assigned risks | Review | View |
| Create or edit controls | Yes | Yes | Assigned controls | Review | View |
| Create or edit SoA records | Yes | Yes | Provide information | Approve or reject | View |
| Upload or submit evidence | Yes | Yes | Assigned controls | No | No |
| Review evidence | Yes | No for own submissions | No for own submissions | Yes | View |
| Approve or reject submissions | No for own work | No for own work | No for own work | Yes | View |
| View audit history | Yes, subject to sensitive-data restrictions | Yes | Relevant records | Yes | Yes |
| Edit or delete audit history | No | No | No | No | No |
| Export reports | Yes | Yes | Assigned records | Yes | Yes |

## Permission Rules

- Administrator access must be limited to platform administration and user-account metadata.
- Sensitive personal, employee, financial, and security information must not be visible to an Administrator by default.
- Any exceptional access must have a documented business reason, time limit, approval, and audit-history record.
- Passwords, authentication secrets, payment-card data, and encryption keys must never be displayed to administrators.
- The platform should display only the minimum information needed for each role.
- Ikigai should review administrator access regularly as part of its privacy and access-control processes.


## Approval and Separation of Duties

The normal approval workflow is:

1. A GRC Analyst or Control Owner creates or updates a record.
2. The record is submitted for review.
3. A Reviewer/Approver checks the record and evidence.
4. The Reviewer/Approver approves, rejects, or requests changes.
5. The system records the decision, user, date, comments, and status in audit history.
