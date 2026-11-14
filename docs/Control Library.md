### Control 1: Access Control and Least Privilege

**ISO/IEC 27001 reference:** Annex A 5.15 Access control, with related identity and access-rights controls

**Purpose:** Ensure that users receive only the access required for their responsibilities and that unnecessary or risky access is identified and removed.

**Control description:** Access to Ikigai systems and information is granted according to job responsibilities, approved by an authorized person, reviewed regularly, and removed or changed when access is no longer required.

**Related risks:** Risk 1, Risk 2, Risk 3, and partially Risk 4

**Control owner:** Head of IT Operations

**Supporting owners:**

- Human Resources informs IT about joining, role changes, leave, and termination.
- Department managers approve employee access.
- System owners approve access to specific systems or information.
- IT Operations grants, changes, reviews, monitors, and removes access.
- GRC Analyst tracks evidence and reviews whether the process is operating.

**Review frequency:**

- Privileged and critical access: Weekly
- Normal employee access: Monthly
- Termination or role-change access removal: Immediately
- Extended leave: Access reviewed before or at the start of the leave period

**Additional safeguards:**

- Multi-factor authentication for privileged and sensitive access
- Monitoring of unusual login and access activity
- Disabled dormant accounts
- Time-limited or just-in-time privileged access where practical
- Separate administrator accounts for administrative activities

**Required evidence:**

- Access-control policy
- Role-permission matrix
- Approved access requests
- Weekly privileged-access review records
- Monthly employee-access review records
- Offboarding and access-removal records
- Privileged-account list
- Access and authentication logs
- Evidence of MFA configuration

**Statement of Applicability decision:** Applicable

**Justification:** Ikigai processes student, employee, financial, authentication, and business information. Limiting and reviewing access is necessary to reduce unauthorized access, account compromise, insider misuse, and unauthorized system changes.

**Implementation status:** Planned

x### Control 2: Secure Development and Change Management

**ISO/IEC 27001 reference:** Annex A 8.25 Secure development life cycle, A.8.26 Application security requirements, A.8.28 Secure coding, and A.8.32 Change management

**Purpose:** Ensure that changes to Ikigai’s applications, infrastructure, integrations, and configurations do not introduce unacceptable security, privacy, or availability risks.

**Control description:** Ikigai classifies proposed changes according to risk. Low-risk changes receive a lightweight review. Changes that may affect student information, authentication, payments, artificial-intelligence features, or production infrastructure receive a full security and privacy review before release.

**Related risks:** Risk 1, Risk 2, and Risk 4

**Control owner:** Head of Engineering

**Supporting owners:**

- Product Manager documents the purpose and business impact of the change.
- Engineering Team develops, performs code review, and tests the change.
- IT Operations manages deployment, monitoring, and rollback.
- Legal or Privacy function reviews personal-data implications.
- GRC Analyst tracks review, approval, and evidence.
- System owner approves changes affecting a specific system or dataset.

**Change-review categories:**

**Low-risk change:**

- Does not process or expose sensitive information.
- Does not affect authentication or authorization.
- Does not change payment processing.
- Does not affect production infrastructure.
- Does not introduce an external integration or AI functionality.

A low-risk change requires a change record, basic testing, code review where applicable, and approval from the responsible team.

**High-risk change:**

- Processes, stores, displays, or transfers student or employee information.
- Affects authentication, authorization, account recovery, or privileged access.
- Changes payment-related functionality or payment-provider integration.
- Introduces or changes an AI feature.
- Changes production infrastructure, databases, network settings, or security configurations.
- Introduces a new external service or third-party integration.
- Could significantly affect platform availability.

A high-risk change requires security and privacy impact review, testing in a non-production environment, appropriate security testing, documented approval, deployment planning, monitoring, and a rollback plan.

**Required change process:**

1. Record the proposed change.
2. Identify the systems and information affected.
3. Classify the change as low-risk or high-risk.
4. Assess security, privacy, and availability impacts.
5. Review access and data-flow effects.
6. Develop and test the change in a non-production environment.
7. Perform security testing appropriate to the risk.
8. Obtain the required approval.
9. Deploy the change according to an approved plan.
10. Monitor the system after deployment.
11. Record the result and close the change.
12. Review and document any unexpected issue.

**Emergency changes:** Emergency changes may be implemented quickly to respond to an active incident or serious vulnerability. The change must still be recorded, approved by an authorized person where possible, and reviewed retrospectively after implementation.

**Required evidence:**

- Change-management policy
- Change request or ticket
- Risk classification
- Security and privacy impact checklist
- Code-review record
- Test results
- Security-test results
- Approval record
- Deployment record
- Rollback plan
- Post-release monitoring record
- Emergency-change review, where applicable

**Statement of Applicability decision:** Applicable

**Justification:** Ikigai operates web and mobile applications that process student information, authentication data, learning records, payment-related information, and external integrations. A risk-based change-management process is necessary to reduce the possibility of data exposure, account compromise, insecure integrations, and service disruption.

**Implementation status:** Planned
