# Initial Statement of Applicability

> This is an educational, limited-scope Statement of Applicability for the Ikigai GRC Management Platform. It is not a complete ISO/IEC 27001 certification SoA.

## Purpose

This document records which selected ISO/IEC 27001:2022 Annex A controls apply to Ikigai, why they apply, who owns them, their implementation status, and the evidence required to demonstrate operation.

## SoA Record Fields

Each SoA record contains:

- Control reference
- Control name
- Applicability decision
- Justification
- Related risks
- Control owner
- Implementation status
- Required evidence
- Review status

## SoA Records

### 1. Access Control and Least Privilege

**ISO/IEC 27001 reference:** Annex A 5.15 Access control, with related identity and access-rights controls

**Applicable:** Yes

**Justification:** Ikigai processes student, employee, financial, authentication, academic, and GRC information. Access must be limited to authorized users based on their responsibilities.

**Related risks:** Risk 1, Risk 2, Risk 3, and partially Risk 4

**Control owner:** Head of IT Operations

**Implementation status:** Planned

**Required evidence:**

- Access-control policy
- Role-permission matrix
- Approved access requests
- Weekly privileged-access reviews
- Monthly employee-access reviews
- Offboarding records
- Privileged-account list
- Authentication and access logs
- MFA configuration evidence

**Review status:** Not yet reviewed

---

### 2. Secure Development and Change Management

**ISO/IEC 27001 reference:** Annex A 8.25, A.8.26, A.8.28, and A.8.32

**Applicable:** Yes

**Justification:** Ikigai operates web and mobile applications that process student information, authentication data, learning records, payment-related information, and external integrations. Changes must be assessed and tested before release.

**Related risks:** Risk 1, Risk 2, and Risk 4

**Control owner:** Head of Engineering

**Implementation status:** Planned

**Required evidence:**

- Change-management policy
- Change request or ticket
- Risk classification
- Security and privacy impact review
- Code-review record
- Test results
- Security-test results
- Approval record
- Deployment record
- Rollback plan
- Post-release monitoring record

**Review status:** Not yet reviewed

---

### 3. Vulnerability and Patch Management

**ISO/IEC 27001 reference:** Annex A 8.8 Management of technical vulnerabilities

**Applicable:** Yes

**Justification:** Ikigai uses web and mobile applications, cloud infrastructure, databases, employee devices, and third-party integrations. Unpatched or misconfigured systems could lead to unauthorized access, data exposure, account compromise, or service disruption.

**Related risks:** Risk 1, Risk 2, Risk 3, and Risk 4

**Control owner:** Head of IT Operations

**Implementation status:** Planned

**Required evidence:**

- Vulnerability-management policy
- Vulnerability-scan reports
- Patch-management records
- Vendor security advisories
- Penetration-test findings
- Remediation tickets
- Patch-verification results
- Exception and risk-acceptance records
- Vulnerability-status reports

**Review status:** Not yet reviewed

---

### 4. Backup and Recovery

**ISO/IEC 27001 reference:** Annex A 8.13 Information backup, with related ICT continuity controls

**Applicable:** Yes

**Justification:** Ikigai depends on online learning services and stores student, employee, financial, academic, and GRC information. Backups and tested recovery procedures are needed to recover from data loss, corruption, ransomware, infrastructure failure, or service disruption.

**Related risks:** Risk 1, Risk 3, and Risk 4

**Control owner:** Head of IT Operations

**Implementation status:** Planned

**Required evidence:**

- Backup and recovery policy
- Backup schedule
- Backup-success reports
- Backup-failure alerts
- Backup-retention configuration
- Encryption and access-control evidence
- Restoration-test records
- Disaster-recovery exercise report
- RTO and RPO approval
- Recovery-plan version history

**Review status:** Not yet reviewed

---

### 5. Supplier Security and Third-Party Risk Management

**ISO/IEC 27001 reference:** Annex A 5.19, A.5.20, A.5.21, and A.5.22

**Applicable:** Yes

**Justification:** Ikigai depends on cloud, payment, authentication, video, email, analytics, and other external providers. Supplier risks may affect student information, financial information, platform availability, and regulatory obligations.

**Related risks:** Risk 1, Risk 3, and Risk 4

**Control owner:** Head of IT Operations

**Implementation status:** Planned

**Required evidence:**

- Vendor register
- Vendor risk assessment
- Security questionnaire
- Relevant assurance reports
- Vendor contract
- Data-processing agreement where applicable
- Sub-processor list
- Incident-notification records
- Periodic vendor-review records
- Service-level reports
- Vendor-remediation tracker
- Secure data-deletion or return evidence

**Review status:** Not yet reviewed

---

### 6. Information-Security Awareness, Education and Training

**ISO/IEC 27001 reference:** Annex A 6.3 Information security awareness, education, and training

**Applicable:** Yes

**Justification:** Employees and contractors may access student, employee, financial, academic, and system information. Security and privacy training is necessary to reduce phishing, credential theft, accidental disclosure, and inappropriate handling of information.

**Related risks:** Risk 1, Risk 2, and Risk 3

**Control owner:** HR Manager or Head of People

**Implementation status:** Planned

**Required evidence:**

- Security-awareness policy
- Annual training material
- Quarterly refresher material
- New-joiner training records
- Training-completion reports
- Quiz or assessment results
- Phishing-simulation results
- Role-based training records
- Training exception records
- Follow-up records

**Review status:** Not yet reviewed

---

### 7. Information-Security Incident Management

**ISO/IEC 27001 reference:** Annex A 5.24, A.5.25, A.5.26, A.5.27, and A.5.28

**Applicable:** Yes

**Justification:** Ikigai processes student, employee, financial, academic, and authentication information and depends on critical online services. A formal incident-management process is needed to support detection, containment, investigation, recovery, evidence preservation, and applicable notifications.

**Related risks:** Risk 1, Risk 2, Risk 3, and Risk 4

**Control owner:** Incident Manager

**Implementation status:** Planned

**Required evidence:**

- Incident-management policy
- Incident register
- Severity assessment
- Response timeline
- Investigation evidence
- Containment records
- Communication and notification decisions
- Recovery records
- Root-cause analysis
- Corrective-action tracker
- Lessons-learned review
- Closure approval

**Review status:** Not yet reviewed

## SoA Summary

| Control | Applicable | Owner | Status |
|---|---|---|---|
| Access control and least privilege | Yes | Head of IT Operations | Planned |
| Secure development and change management | Yes | Head of Engineering | Planned |
| Vulnerability and patch management | Yes | Head of IT Operations | Planned |
| Backup and recovery | Yes | Head of IT Operations | Planned |
| Supplier security | Yes | Head of IT Operations | Planned |
| Security awareness and training | Yes | HR Manager / Head of People | Planned |
| Incident management | Yes | Incident Manager | Planned |
