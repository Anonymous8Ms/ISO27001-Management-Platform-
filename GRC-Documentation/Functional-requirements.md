# Functional Requirements

## Purpose

This document defines what the Ikigai GRC Management Platform must allow authorized users to do.

## 1. User and Access Management
m
- The system must allow authorized administrators to create, update, deactivate, and assign roles to users.
- The system must enforce role-based access control.
- The system must restrict sensitive personal, employee, financial, and security information according to user permissions.
- The system must prevent users from approving their own submissions.
- The system must record important user and permission changes in audit history.
- The system must support immediate deactivation of users who leave Ikigai.

## 2. Asset Management

- The system must allow authorized users to create, view, update, and archive information assets.
- Each asset must record its name, owner, information stored, importance, and security concerns.
- Users must be able to link assets to related risks.
- Changes to important asset records must be recorded in audit history.

## 3. Risk Management

- The system must allow authorized users to create and update risks.
- Each risk must record its asset, threat, vulnerability, potential impact, owner, status, and treatment.
- The system must support likelihood and impact scores from 1 to 5.
- The system must calculate the risk rating as likelihood multiplied by impact.
- The system must classify the result as Low, Medium, High, or Critical.
- Users must be able to assign a risk owner and approval authority.
- Users must be able to record inherent and residual risk.
- The system must track risk-treatment actions, owners, target dates, and status.

## 4. Control Management

- The system must allow authorized users to create and maintain control records.
- Each control must record its reference, name, purpose, description, owner, related risks, status, and required evidence.
- Users must be able to link controls to one or more risks.
- The system must track control implementation status.
- Control Owners must be able to update their assigned controls.
- Important control changes must be recorded in audit history.

## 5. Statement of Applicability

- The system must allow authorized users to create SoA records.
- Each SoA record must include the control reference, applicability decision, justification, related risks, owner, implementation status, required evidence, and review status.
- Users must be able to mark a control as applicable or not applicable.
- A justification must be required for every applicability decision.
- SoA records must be submitted for review before approval.
- Approved SoA decisions must not be changed without a new review or recorded change history.

## 6. Evidence Management

- The system must allow authorized users to add evidence metadata.
- Evidence must be linked to a control, risk, SoA record, or treatment action.
- Evidence must record its name, description, owner, date, review period, and status.
- The system must support evidence statuses such as Draft, Submitted, Accepted, Rejected, and Expired.
- Evidence submitted by a Control Owner must be reviewed by an authorized Reviewer/Approver.
- The system must record evidence-review comments and decisions.
- Evidence files and links must be protected according to their sensitivity.

## 7. Review and Approval

- Users must be able to submit records for review.
- Reviewers must be able to approve, reject, or request changes.
- Rejected records must include a review comment.
- Approved records must record the approver, decision date, and comments.
- The system must prevent unauthorized users from approving records.
- The system must maintain a history of review and approval decisions.

## 8. Incident Management

- Authorized users must be able to create incident records.
- Incidents must include severity, affected asset, description, owner, status, and response actions.
- The system must support Critical, High, Medium, and Low severity levels.
- Users must be able to record containment, investigation, recovery, communication, and corrective actions.
- Incident records must support lessons-learned information.
- Access to sensitive incident details must be restricted.

## 9. Audit History

- The system must record important create, update, submit, approve, reject, archive, and permission-change actions.
- Each audit-history record must include the user, action, date and time, affected record, previous value where applicable, and new value where applicable.
- Users must not be able to edit or delete audit-history records.
- Audit history must be viewable according to role permissions.

## 10. Dashboard and Reporting

- The system must display open risks by severity.
- The system must display controls by implementation status.
- The system must show evidence awaiting review.
- The system must show overdue treatment actions.
- The system must show incidents by severity and status.
- The system must provide filters by owner, status, severity, asset, control, and date.
- Reports must respect the user’s access permissions.
- Administrators must not automatically see sensitive personal or confidential information in reports.

## 11. Privacy and Data Protection Requirements

- The system must collect only information needed for GRC activities.
- Sensitive personal information must be visible only to authorized users.
- Passwords, authentication secrets, payment-card data, and encryption keys must never be displayed.
- Exceptional access to sensitive information must require a reason, approval, time limit, and audit record.
- The system must support archiving instead of permanent deletion where records are needed for audit history.
- Privacy-related records must identify the purpose, owner, access restrictions, and retention expectations where applicable.

## 12. Initial Workflow

The first complete workflow must support:

1. Create an asset.
2. Create a risk linked to the asset.
3. Assess likelihood and impact.
4. Calculate the risk rating.
5. Create a treatment plan.
6. Link the risk to a control.
7. Create an SoA decision.
8. Add supporting evidence.
9. Submit the record for review.
10. Approve, reject, or request changes.
11. Record the decision in audit history.

User referes to who manages GRC Management platform
