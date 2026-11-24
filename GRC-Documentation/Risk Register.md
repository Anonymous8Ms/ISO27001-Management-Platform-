### Risk 1: Unauthorized access to student information

**Asset:** Student Information Database

**Threat:** An attacker gains unauthorized access to the database.

**Vulnerability:** A vulnerability or insecure configuration may remain after a system update, or users may have more access than required.

**Potential impact:** Student personal information and identification details could be exposed, misused, or sold. Ikigai could face harm to students, legal or regulatory consequences, financial loss, and loss of trust.

**Initial treatment:** Apply least-privilege access, perform regular access reviews, scan for vulnerabilities, test changes before release, and monitor security logs.

**Risk owner:** Head of IT Operations

**Status:** Open

**Likelihood:** 4 — Likely

**Impact:** 5 — Severe

**Risk rating:** 4 × 5 = 20

**Risk level:** Critical

**Risk acceptance decision:** Treat

**Approval authority:** Senior Management

**Review frequency:** Monthly



### Risk 2: Student account takeover

**Asset:** Student Accounts and Authentication System

**Threat:** An attacker obtains a student’s credentials through phishing, password reuse, credential stuffing, or a weak password-reset process.

**Vulnerability:** Weak authentication controls, lack of MFA, stolen sessions, or insufficient monitoring of unusual login activity.

**Potential impact:** The attacker may access personal information, change account details, misuse paid courses, or access examination-related information. This could harm students and damage Ikigai’s reputation.

**Initial treatment:** Enforce strong passwords, implement MFA where appropriate, secure password recovery, limit failed login attempts, monitor unusual logins, and provide security-awareness guidance.

**Risk owner:** Head of IT Operations

**Status:** Open

**Likelihood:** 4 — Likely

**Impact:** 4 — Major

**Risk rating:** 4 × 4 = 16

**Risk level:** High

**Risk acceptance decision:** Treat

**Approval authority:** Head of IT Operations

**Review frequency:** Monthly



### Risk 3: Unauthorized access to employee and financial information

**Asset:** Employee Information and Financial Information

**Threat:** An attacker obtains an employee’s credentials through phishing, malware, password reuse, or another credential-theft method.

**Vulnerability:** Weak authentication, excessive employee access, lack of multi-factor authentication, poor access reviews, or delayed account deactivation.

**Potential impact:** The attacker may access employee personal information, salary records, invoices, budgets, or financial reports. They may modify financial records, commit fraud, or disclose confidential information. This could cause privacy harm, financial loss, legal consequences, and reputational damage to Ikigai.

**Initial treatment:** Apply least-privilege access, use role-based permissions, implement multi-factor authentication for sensitive systems, review access regularly, monitor unusual activity, protect credentials, and immediately disable accounts when employees leave.

**Risk owner:** Head of IT Operations, with Finance and Human Resources responsible for their respective information.

**Status:** Open

**Likelihood:** 3 — Possible

**Impact:** 5 — Severe

**Risk rating:** 3 × 5 = 15

**Risk level:** High

**Risk acceptance decision:** Treat

**Approval authority:** Senior Management

**Review frequency:** Monthly


### Risk 4: Learning platform unavailability

**Asset:** Ikigai web and mobile learning platform, student database, and critical third-party services

**Threat:** A cloud provider, database, sign-in provider, payment gateway, external API, or other critical vendor becomes unavailable or experiences a major outage.

**Vulnerability:** Ikigai may depend on a single provider or service without sufficient redundancy, monitoring, recovery procedures, or alternative arrangements.

**Potential impact:** Students may be unable to sign in, purchase courses, access lectures, attend classes, or view their learning records. Ikigai may lose revenue, fail to deliver services, and damage customer trust.

**Initial treatment:** Maintain regular backups, monitor critical services, define recovery procedures, test restoration, use redundancy where practical, and create business-continuity and disaster-recovery plans.

**Risk owner:** Head of IT Operations

**Status:** Open

**Likelihood:** 3 — Possible

**Impact:** 5 — Severe

**Risk rating:** 3 × 5 = 15

**Risk level:** High

**Risk acceptance decision:** Treat

**Approval authority:** Senior Management

**Review frequency:** Monthly


**Likelihood:** `[score and description]`

**Impact:** `[score and description]`

**Risk rating:** `[likelihood × impact]`

**Risk level:** `[Low, Medium, High, or Critical]`

**Risk acceptance decision:** `[Accept, Treat, Transfer, or Avoid]`

**Approval authority:** `[role]`

**Review date:** `[date or review frequency]`


