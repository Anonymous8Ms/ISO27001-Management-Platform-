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


### Control 2: Secure Development and Change Management

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


### Control 3: Vulnerability and Patch Management

**ISO/IEC 27001 reference:** Annex A 8.8 Management of technical vulnerabilities

**Purpose:** Identify, assess, prioritize, and remediate technical vulnerabilities in Ikigai’s applications, infrastructure, devices, and third-party components.

**Control description:** Ikigai should regularly identify vulnerabilities, assess their severity and business impact, assign remediation owners, apply patches or compensating controls within defined timeframes, and retain evidence of the work performed.

**Related risks:** Risk 1, Risk 2, Risk 3, and Risk 4

**Control owner:** Head of IT Operations

**Supporting owners:**

- Engineering identifies and fixes vulnerabilities in applications and dependencies.
- IT Operations patches infrastructure, operating systems, and devices.
- System owners assess the effect of vulnerabilities on their systems.
- Vendor managers coordinate vulnerability information received from third parties.
- GRC Analyst tracks overdue remediation and reports significant exceptions.

**Vulnerability remediation targets:**

| Severity | Target |
|---|---|
| Critical | Remediate within 7 calendar days |
| High | Remediate within 14 calendar days |
| Medium | Remediate within 30 calendar days |
| Low | Remediate within 90 calendar days |

**Emergency condition:** A critical vulnerability that is actively exploited, internet-facing, or likely to expose student or financial information should be contained or mitigated within 24 to 72 hours.

**Required process:**

1. Identify vulnerabilities through scanning, vendor notices, penetration tests, code reviews, and security monitoring.
2. Record the affected asset, source, severity, and discovery date.
3. Assess exploitability, exposure, affected information, and business impact.
4. Assign a remediation owner and target date.
5. Apply a patch, upgrade, configuration change, or compensating control.
6. Test the change before production deployment where practical.
7. Verify that the vulnerability has been resolved.
8. Record evidence and close the item.
9. Escalate overdue or high-impact vulnerabilities to management.
10. Record and approve exceptions when remediation cannot meet the target.

**Required evidence:**

- Vulnerability-management policy
- Vulnerability-scan reports
- Patch-management records
- Vendor security advisories
- Penetration-test findings
- Remediation tickets
- Patch verification results
- Exception and risk-acceptance records
- Monthly vulnerability-status report

**Statement of Applicability decision:** Applicable

**Justification:** Ikigai operates web and mobile applications, cloud infrastructure, databases, employee devices, and third-party integrations. Unpatched or misconfigured systems could allow unauthorized access, account compromise, data exposure, or service disruption.

**Implementation status:** Planned


### Control 4: Backup and Recovery

**ISO/IEC 27001 reference:** Annex A 8.13 Information backup and related ICT continuity controls

**Purpose:** Ensure that Ikigai can recover important information and services after accidental deletion, corruption, ransomware, infrastructure failure, or a major service disruption.

**Control description:** Ikigai performs scheduled backups of important information and systems, protects backups from unauthorized access or deletion, monitors backup success, and periodically tests restoration.

**Related risks:** Risk 1, Risk 3, and Risk 4

**Control owner:** Head of IT Operations

**Supporting owners:**

- Engineering identifies application and database recovery requirements.
- Finance and Human Resources identify critical records that require recovery.
- System owners confirm backup scope and retention needs.
- GRC Analyst tracks backup and recovery evidence.
- Cloud or service providers perform agreed backup activities under the shared-responsibility model.

**Backup scope:**

- Student information database
- Student account and authentication data
- Employee information
- Financial information
- Course and examination content
- GRC records
- Source code and system configuration

**Backup requirements:**

- Student, employee, and financial information should be backed up daily.
- Course and examination content should be backed up whenever new content is uploaded or existing content is changed.
- Each approved version of course and examination content should be retained so that an earlier version can be restored.
- Examination content and answer keys should have restricted access and protected backup copies.
- A periodic backup verification should confirm that uploaded content can be successfully restored.

- Backups should be encrypted and access-controlled.
- Backups should be stored separately from production where practical.
- Backup failures should generate alerts and be investigated.
- Backup retention periods should be defined for each information type.
- Backup deletion should require authorized approval.

**Recovery targets:**

- **RTO:** Restore critical learning services within 4 hours after a major outage.
- **RPO:** Restore critical data with no more than 1 hour of data loss, where technically practical.

**Recovery testing:**

- Test critical database restoration quarterly.
- Perform a broader disaster-recovery exercise annually.
- Retest recovery procedures after major infrastructure changes.
- Record the test result, issues found, corrective action, and approval.

**Required evidence:**

- Backup and recovery policy
- Backup schedule
- Backup-success reports
- Backup-failure alerts and corrective actions
- Backup-retention configuration
- Encryption and access-control evidence
- Restoration-test records
- Disaster-recovery exercise report
- RTO and RPO approval
- Recovery-plan version history

**Statement of Applicability decision:** Applicable

**Justification:** Ikigai depends on online learning services and stores student, employee, financial, academic, and GRC information. Backup and recovery capabilities are necessary to preserve information and restore services after data loss or disruption.

**Implementation status:** Planned


### Control 5: Supplier Security and Third-Party Risk Management

**ISO/IEC 27001 reference:** Annex A 5.19 Information security in supplier relationships, A.5.20 Addressing information security within supplier agreements, A.5.21 Managing information security in the ICT supply chain, and A.5.22 Monitoring, review, and change management of supplier services

**Purpose:** Ensure that third-party vendors do not introduce unacceptable confidentiality, integrity, availability, privacy, or compliance risks to Ikigai.

**Control description:** Ikigai identifies, assesses, approves, contracts with, monitors, and periodically reviews suppliers that process Ikigai information or support important business services.

**Related risks:** Risk 1, Risk 3, and Risk 4

**Control owner:** Head of IT Operations

**Supporting owners:**

- Legal or Privacy function reviews contracts and data-processing requirements.
- Finance reviews commercial and payment-related requirements.
- System owners identify the information and services involved.
- Procurement or Vendor Manager coordinates onboarding and reviews.
- GRC Analyst maintains the vendor register and tracks evidence.
- Department owners confirm the business need for the vendor.

**Vendor risk categories:**

- **Critical vendor:** Processes highly sensitive information or supports a service whose failure could seriously affect students, security, finances, or platform availability.
- **High-risk vendor:** Processes important information or supports an important business function but has a more limited effect than a critical vendor.
- **Low-risk vendor:** Has limited access to information and does not support a critical business service.

**Examples:**

- Cloud hosting provider: Critical
- Payment service provider: Critical
- Authentication provider: Critical or High
- Video-conferencing provider: High
- Email service provider: High
- Analytics provider: High or Low, depending on the data collected
- Office-supply vendor with no system or data access: Low

**Pre-onboarding requirements:**

Before approving a vendor, Ikigai should assess:

- What information the vendor will process, store, or transmit
- The purpose and extent of the vendor’s access
- Data-storage locations and transfer arrangements
- Security controls and available assurance reports
- Encryption and access-management practices
- Incident-reporting arrangements
- Use of sub-processors or sub-vendors
- Business-continuity and recovery capabilities
- Data-retention, deletion, and return procedures
- Relevant legal, regulatory, and contractual requirements

**Contract requirements:**

Where applicable, supplier agreements should define:

- Information-security responsibilities
- Privacy and data-processing obligations
- Access-control requirements
- Confidentiality obligations
- Incident-notification timelines
- Cooperation during investigations
- Audit or evidence rights
- Sub-processor approval or notification requirements
- Data location and transfer requirements
- Data return and secure deletion at contract termination
- Service availability and recovery commitments

**Review frequency:**

- Critical vendors: Monthly formal review
- High-risk vendors: Monthly formal review
- Low-risk vendors: Review every three months
- Major incident or significant service change: Immediate review
- New sub-vendor, policy change, legal change, data-processing change, or security-assurance change: Review when identified

**Ongoing monitoring:**

Ikigai should monitor:

- Vendor security incidents and breaches
- Service outages and availability
- Security-policy changes
- New sub-processors or sub-vendors
- Changes in data-processing activities
- Security certification or audit-report status
- Open vendor remediation actions
- Contract and regulatory compliance

**Required evidence:**

- Vendor register
- Vendor risk assessment
- Security questionnaire
- ISO 27001, SOC 2, PCI DSS, or other assurance evidence where relevant
- Vendor contract
- Data-processing agreement where applicable
- Sub-processor list
- Incident-notification records
- Monthly or periodic review records
- Service-level reports
- Vendor-remediation tracker
- Secure data-deletion or return evidence

**Statement of Applicability decision:** Applicable

**Justification:** Ikigai depends on cloud, payment, authentication, video, email, analytics, and other external providers. A supplier-security process is necessary to manage risks that Ikigai cannot control directly.

**Implementation status:** Planned

### Control 6: Information Security Awareness, Education and Training

**ISO/IEC 27001 reference:** Annex A 6.3 Information security awareness, education, and training

**Purpose:** Ensure that employees and contractors understand their information-security responsibilities and can identify, prevent, and report security and privacy problems.

**Control description:** Ikigai provides security-awareness training before granting system access, comprehensive training annually, and quarterly awareness refreshers covering new threats, incidents, policy changes, and lessons learned.

**Related risks:** Risk 1, Risk 2, and Risk 3

**Control owner:** HR Manager or Head of People

**Supporting owners:**

- IT Operations provides technical-security guidance.
- Legal or Privacy function provides privacy and data-protection guidance.
- GRC Analyst tracks training completion and evidence.
- Department managers ensure their teams complete required training.

**Training requirements:**

- New joiners and contractors must complete core security and privacy training before receiving system access.
- New-joiner training must cover the main annual topics and the latest relevant quarterly threat information.
- All employees and contractors must complete comprehensive security-awareness training annually.
- Quarterly refreshers must cover new threats, phishing patterns, recent incidents, policy changes, and lessons learned.
- Additional role-based training must be provided to developers, IT administrators, HR, Finance, and Customer Support staff.
- Additional training must be provided after a major incident, significant policy change, or identified knowledge gap.

**Training topics:**

- Passwords and multi-factor authentication
- Phishing and social engineering
- Handling student, employee, and financial information
- Incident reporting
- Device and workspace security
- Acceptable use of company systems
- Confidentiality obligations
- Secure use of artificial-intelligence tools
- Privacy responsibilities
- Consequences of unauthorized disclosure
- Role-specific security responsibilities

**Effectiveness checks:**

- Training-completion tracking
- Short quizzes
- Simulated phishing exercises
- Scenario-based exercises
- Incident-reporting drills
- Secure-coding training for developers
- Privacy-handling exercises for relevant teams

**Required evidence:**

- Security-awareness policy
- Annual training material
- Quarterly refresher material
- New-joiner training records
- Attendance and completion reports
- Quiz or assessment results
- Phishing-simulation results
- Role-based training records
- Training exception and follow-up records

**Statement of Applicability decision:** Applicable

**Justification:** Employees and contractors may access student, employee, financial, academic, and system information. Awareness and role-specific training are necessary to reduce phishing, accidental disclosure, credential theft, and inappropriate handling of information.

**Implementation status:** Planned


### Control 7: Information-Security Incident Management

**ISO/IEC 27001 reference:** Annex A 5.24–5.28

**Purpose:** Ensure that Ikigai can identify, report, assess, contain, investigate, recover from, and learn from information-security incidents.

**Control description:** Ikigai maintains an incident-management process with defined severity levels, response time targets, responsibilities, escalation rules, evidence requirements, and lessons-learned activities.

**Related risks:** Risk 1, Risk 2, Risk 3, and Risk 4

**Control owner:** Incident Manager

**Supporting owners:**

- IT Operations handles technical containment and recovery.
- Engineering handles application and code-related incidents.
- Legal or Privacy handles privacy and notification assessments.
- HR supports employee-related incidents.
- Vendor Manager coordinates third-party incidents.
- Senior Management approves major business and communication decisions.
- GRC Analyst maintains records, evidence, and corrective actions.

**Severity levels:**

| Severity | Description | Initial response target |
|---|---|---|
| Critical | Major or ongoing impact to sensitive data, critical systems, or many users | Acknowledge within 15 minutes; assess within 1 hour |
| High | Significant impact to an important system, group, or process | Acknowledge within 1 hour; assess within 4 hours |
| Medium | Limited impact manageable through normal response | Acknowledge within 1 business day; assess within 2 business days |
| Low | Minor event with no confirmed material impact | Acknowledge within 2 business days; assess within 5 business days |

**Incident-response procedure:**

1. Report the suspected incident.
2. Record the initial facts and evidence.
3. Determine whether it is an event or incident.
4. Assign an initial severity.
5. Contain the incident.
6. Investigate the affected systems, information, and users.
7. Remove the cause or exploited weakness.
8. Recover and validate normal service.
9. Communicate with authorized stakeholders.
10. Record root cause, corrective actions, and lessons learned.
11. Close the incident with authorized approval.

**Required evidence:**

- Incident-management policy
- Incident register
- Incident reports
- Severity assessment
- Response timeline
- Evidence and investigation records
- Communication and notification decisions
- Recovery records
- Root-cause analysis
- Corrective-action tracker
- Lessons-learned review

**Statement of Applicability decision:** Applicable

**Justification:** Ikigai processes student, employee, financial, academic, and authentication information and depends on critical online services. A formal incident-management process is necessary to reduce harm, support recovery, preserve evidence, and meet applicable notification obligations.

**Implementation status:** Planned

