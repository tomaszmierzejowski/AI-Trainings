> **⚠️ DEPRECATED (2026-07-19):** This file uses the retired Alpha–Epsilon codename scheme and contains unverified ROI figures, marine/vessel framing, and other AI-generated content that has not been fact-checked. Do NOT use for any published content. See `SOURCE_OF_TRUTH.md` for the current 4 approved case studies: Proof of Scale, Invisible Risk, Proof of Speed, The Rescue.

# AI App Modernization Factory — Security Intelligence Report

## Overview: Security as Discovery Core

The Factory's security assessment capability is not a separate service line — it is integrated into every discovery engagement. This means every client receives a security report alongside the technical analysis, with no additional engagement or cost.

This integration was a deliberate design decision: security findings are consistently the highest-value discovery output, and separating them would underserve clients who most need them.

---

## Findings Catalogue: What the Factory Discovers

### Category 1: Authentication & Authorization Gaps

**Finding type: Unauthenticated API endpoints**

The most dramatic single finding in the Factory's portfolio: Project Beta documented **529 REST API endpoints** accessible without authentication in a production billing and CRM system.

What this means practically:
- Any actor with network access could query customer transaction histories
- Financial records, personal data, and business logic were exposed
- The system was processing live financial transactions while this exposure existed
- The client had no knowledge of the endpoint count or authentication coverage before discovery

The 47 unauthenticated endpoints found in Project Beta's billing system are significant because they were in a financial transaction processing context — PCI-DSS scope.

**Finding type: Authentication bypass patterns**
Automated analysis identifies code patterns where authentication is implemented inconsistently — where some endpoints correctly validate sessions and nearby endpoints do not, creating exploitable gaps.

---

### Category 2: Known Vulnerability Exploitation (CVE Matches)

**Finding type: End-of-life framework vulnerabilities**

Project Delta: **200+ CVEs** on a production maritime research platform
- Framework: Meteor 1.8 (end-of-life)
- Runtime: Node.js 8 (end-of-life, no longer receiving security patches)
- CVE distribution: Critical, High, and Medium severity
- Production context: vessel-deployed platform — physical operational systems

**Finding type: Critical historical CVEs still in production**

Project Alpha: **Apache Struts 1.1** (CVE-2014-0114)
- CVSS Score: 7.5 (High)
- Vulnerability class: Remote Code Execution via ClassLoader manipulation
- First disclosed: 2014 (10 years before discovery)
- Status in client systems: Active in production workloads at time of discovery
- Industry context: Same software family as CVE-2017-5638 used in Equifax breach

The Struts finding illustrates a systemic industry problem: organizations running production workloads on decade-old technology stacks with publicly documented critical vulnerabilities. These are not theoretical exposures — they are exploitable by any threat actor with basic knowledge and network access.

---

### Category 3: Hardcoded Credentials

**Finding pattern:** Production-accessible credentials embedded in source code

Findings across multiple engagements:
- Database passwords hardcoded in configuration files checked into version control
- API keys in source code (potentially historical exposure if repositories were ever external)
- Service account credentials embedded in application logic

**Business risk:** Source code repositories are common exfiltration targets in supply-chain attacks. Any historical exposure of these repositories — to contractors, external auditors, or through git misconfiguration — would have exposed production credentials.

---

### Category 4: Compliance Gaps

**GDPR Article 17 — Right to Erasure (Project Beta)**

The billing system discovery found that GDPR Article 17 was not technically implemented. This means:
- The organization was legally required to delete personal data on request (since May 2018)
- The system had no technical mechanism to do so
- Every user data deletion request received in the preceding 6+ years could not have been honored
- Regulatory exposure: up to €20M fine (4% of global annual turnover, whichever is higher)

**PCI-DSS Compliance Gap (Project Beta)**

The billing system's 47 unauthenticated endpoints in financial transaction processing created PCI-DSS scope violations:
- Cardholder data environment (CDE) control requirements not met
- Exposure category: ongoing non-compliance
- Penalty range: €100,000+ per month until remediation

**SOX Relevance (Project Beta)**

Mid-migration risk assessment identified SOX-relevant exposure:
- Financial reporting system modifications without adequate controls documentation
- Estimated exposure: 200,000–500,000 NOK

---

### Category 5: Infrastructure & Code Quality

**Finding type: 8,800+ SonarQube violations (Project Alpha)**

Project Alpha's 20-repository portfolio had 8,800+ documented code quality violations catalogued automatically. These are not style issues — they include:
- Null pointer dereference patterns
- SQL construction vulnerabilities (injection potential)
- Insecure random number generation
- Deprecated cryptographic algorithms

**Finding type: Code complexity indicators**
- Files with cyclomatic complexity exceeding maintainability thresholds
- Dead code branches (executed on every request, doing nothing — performance waste + confusion)
- Missing error handling (exception swallowing patterns)

---

## Security Discovery ROI Calculation

| Project | Primary Finding | Potential Cost of Incident | Discovery Cost | Multiplier |
|---------|----------------|--------------------------|----------------|-----------|
| Alpha | RCE vulnerability (Equifax class) | €5M–€50M (breach + regulatory) | ~€100K | 50–500x |
| Beta | 529 exposed endpoints + GDPR gap | €20M GDPR + €1.2M/year PCI | ~€100K | 200x+ |
| Delta | 200+ CVEs on vessel platform | Operational + safety risk: unquantified | ~€100K | High |
| Gamma | Framework end-of-life (research data) | Research program failure + years of work | ~€30K | Catastrophic avoidance |

The security findings alone — independent of any modernization work — justify the discovery investment in every engagement completed to date.

---

## The "Already Exposed" Reality

A key insight from the Factory's security discoveries: in most cases, the vulnerabilities found were not new risks. They were pre-existing exposures that the organization did not know about.

The question is not "did this discovery create a new risk?" — it is "did this discovery reveal an existing risk that was already being carried?"

**Apache Struts 1.1 in Project Alpha**: This vulnerability was documented in 2014. The client had been running it for approximately 10 years. Every day without discovery was a day of unknown exposure.

**529 unauthenticated endpoints in Project Beta**: These endpoints were live in production, accessible to anyone who knew the API patterns. They had been live for years. Discovery didn't create the risk — it ended the period of carrying unknown risk.

**200+ CVEs in Project Delta**: Every CVE was publicly documented. The vulnerability information was available to any threat actor. The client organization was the last party to learn about their own exposure.

Discovery does not introduce risk. Discovery ends the window of asymmetric information where threat actors know more about your systems than you do.

---

## The Local Security Architecture

A critical technical detail: the Factory's AI analysis pipeline is designed to run on the client's own infrastructure or on dedicated isolated environments. Code is not uploaded to shared cloud services.

This matters for:
- **IP protection**: Source code represents organizational IP. Sending it to external AI services creates exposure.
- **Regulatory compliance**: For organizations in regulated industries (financial services, healthcare, public sector), source code cannot leave controlled environments.
- **Client confidence**: Organizations with security-conscious cultures require contractual assurance about code handling.

The Factory's local obfuscation pipeline strips sensitive information before any cloud processing steps, creating a technical architecture where the most sensitive elements of the codebase never leave the client's controlled perimeter.
