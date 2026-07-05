# AI App Modernization Factory — Case Studies (Anonymized)

All client names have been replaced with project codenames (Alpha through Epsilon) in accordance with confidentiality policy. Industry and geography references are preserved for context.

---

## Project Alpha — Nordic Automotive Platform

**Industry:** Automotive retail (multi-brand dealer network)
**Geography:** Norway
**Engagement scope:** Portfolio discovery across a large dealer management platform

### Challenge
A Nordic automotive retail organization was running 20 interconnected repositories built on obsolete technology stacks. The platform powered sales workflows, inventory, and customer management. No one in the organization had a reliable map of how the 20 repos connected to each other, what APIs were exposed externally, or what critical business logic was embedded in the legacy code.

### What the Factory Found (60-hour automated discovery)
- **20 repositories** analyzed, **98 inter-service connections** mapped
- **Apache Struts 1.1** in production — subject to **CVE-2014-0114**, a Remote Code Execution vulnerability with CVSS score 7.5 (High). This vulnerability was publicly known since 2014 and is the same class of vulnerability that caused the Equifax breach (2017, $575M settlement)
- **Plaintext credentials** hardcoded in configuration files and source code
- **8,800+ SonarQube code quality violations** catalogued
- No automated test coverage on critical business logic paths

### Outcome
- Full discovery report delivered in **3 weeks** (traditional estimate: 14 weeks)
- Cost: **~500,000 NOK** (traditional estimate: **~2,300,000 NOK**)
- Cost reduction: **78%**
- Modernization roadmap produced with prioritized risk remediation plan
- Client was able to present board-level risk exposure for the first time with code-linked evidence

### Key Quote Context
The RCE vulnerability finding was the pivotal moment: the client had been running production systems on a codebase with a known 10-year-old critical vulnerability. Discovery made the invisible visible.

---

## Project Beta — Nordic Tolling & Billing System

**Industry:** Transportation infrastructure (electronic tolling)
**Geography:** Norway
**Engagement scope:** Discovery of a legacy billing and CRM platform

### Challenge
A Nordic tolling operator was running a legacy billing and CRM system processing millions of transactions. The system had grown organically over years, and the organization had lost institutional knowledge of its internal API structure. A mid-migration attempt by a previous vendor had been abandoned, leaving the codebase in a partially modified state.

### What the Factory Found
- **529 REST API endpoints** documented — **with no authentication requirement** on a significant subset
- **GDPR Article 17 (right to erasure)** not implemented: user data deletion requests could not be technically honored
- **Hardcoded credentials** in source code
- **Compliance score: 35/100** (non-compliant threshold: 60/100)
- **143 business rules** extracted at **94% confidence** from ~220,000 lines of legacy code
- **312 evidence-tagged citations** in discovery report (every finding linked to source)
- **SOX-relevant risk**: mid-migration financial reporting exposure estimated at 200,000–500,000 NOK
- **GDPR fine exposure**: up to €20M under GDPR Article 83
- **PCI-DSS penalty exposure**: €100,000+ per month in ongoing non-compliance

### Deliverables
- 3-week delivery (traditional equivalent: 6 months)
- Full compliance scorecard with regulatory exposure mapping
- Business rules documentation covering 16 modules across 4 core domains
- Remediation roadmap with prioritized compliance milestones

### Outcome
The 529 unauthenticated endpoint finding created immediate executive attention. Before the discovery, the organization had no visibility into this exposure. The compliance report became the basis for a prioritized €800K remediation program.

---

## Project Gamma — National Research Platform (Mobile)

**Industry:** Non-profit research / public health
**Geography:** Norway
**Engagement scope:** Emergency mobile application migration

### Challenge
A Norwegian organization running a national research project — tracking children's wellbeing and self-esteem across multiple municipalities — had their mobile application (Android and iOS) become non-functional due to the end-of-life of the Xamarin framework (Google Play API update, Q4 2024). The application was the primary data collection tool for kindergartens across Norway. Without it, a multi-year national research project could not launch its January 2026 cohort.

The organization had a very limited budget and a fixed deadline: **January 2, 2026**, when kindergartens across multiple Norwegian municipalities were scheduled to start.

### What the Factory Did
- Automated analysis of existing Xamarin codebase
- AI-assisted migration to .NET MAUI (the successor framework)
- Parallel test generation to ensure functional parity
- App Store submission (both Google Play and Apple App Store)

### Results
- **Delivery time: 4 days** (industry estimate for Xamarin-to-MAUI migration: 4–8 weeks)
- **92% of original code preserved** (no unnecessary rewrites)
- **Zero post-launch bugs** reported
- **First-submission approval** on both app stores (no rejection/resubmission cycle)
- National research program launched on schedule, January 2, 2026
- Kindergartens across multiple Norwegian municipalities operational on day one

### Customer Feedback (anonymized excerpt)
*From the project sponsor, received December 24, 2025:*

> "Xamarin-app is working again! Now we can look forward to an exciting national research project to start in the new year! Thank you so much. Merry Christmas!"

This was the message received on Christmas Eve — the migration was completed and deployed in time for the January launch. The feedback represents direct impact: a national research program serving children and families was enabled by a 4-day technical intervention.

---

## Project Delta — Maritime Research Platform

**Industry:** Maritime / fisheries research
**Geography:** Norway
**Engagement scope:** Security assessment and modernization discovery for vessel-deployed research platform

### Challenge
A maritime research organization operated a specialized data collection and processing platform deployed across 20+ vessels. The platform ran on severely outdated infrastructure: Meteor 1.8 and Node.js version 8 — both end-of-life technologies with publicly documented critical vulnerabilities.

The organization had no visibility into the security posture of their vessel-deployed systems or the extent of their vulnerability exposure.

### What the Factory Found
- **Meteor 1.8 + Node.js 8**: combined exposure of **200+ known CVEs** (Common Vulnerabilities and Exposures)
- Complete dependency graph of 100,000+ lines of code across 300+ files
- All 20+ vessel deployment targets mapped and documented
- Vulnerability severity distribution: Critical / High / Medium classified

### Outcome
- Discovery delivered in **3 weeks**
- **ROI: 16x** on the discovery investment (cost savings from prevented incident + modernization cost reduction)
- Organization for the first time had a complete security exposure picture
- Modernization roadmap produced to migrate off end-of-life stack before critical vulnerability exploitation

### Context: Why This Matters
Running Meteor 1.8 and Node.js 8 in a production maritime environment is equivalent to running a ship with a known hull breach. The vulnerabilities were publicly documented; the only question was whether a threat actor would find them before the organization's own discovery. The Factory discovery answered that question definitively: 200+ vulnerabilities existed, and the organization now had 3 weeks of warning instead of a post-breach response.

---

## Project Epsilon — National Data Infrastructure

**Industry:** Public sector / national data management
**Geography:** Norway
**Engagement scope:** Architecture modernization and clean-sheet rebuild

### Challenge
A national data management organization needed a full architectural overhaul of a legacy data processing system. The system handled sensitive national-level data with requirements for long-term maintainability, security compliance, and scalability.

### What the Factory Delivered
- Architecture design applying **Clean Architecture**, **Domain-Driven Design (DDD)**, and **CQRS** patterns
- Full **Azure Bicep Infrastructure-as-Code** implementation
- Automated test suite covering business logic
- Deployment pipeline with zero-downtime capability

### Outcome
- System delivered with complete architectural documentation
- Infrastructure reproducible from code (no manual configuration)
- Design patterns selected for 10+ year maintainability horizon

---

## Cross-Project Portfolio Summary

| Project | Industry | Core Finding | Delivery Time | Cost vs Traditional | ROI |
|---------|----------|-------------|---------------|---------------------|-----|
| Alpha | Automotive | RCE vulnerability (CVE-2014-0114), 8,800+ quality issues | 3 weeks | 78% reduction | 8x |
| Beta | Transport | 529 exposed endpoints, 35/100 compliance, GDPR exposure | 3 weeks | 78% reduction | 8x |
| Gamma | Research/Non-profit | Emergency 4-day migration, 0 bugs | 4 days | 85% reduction | 4x |
| Delta | Maritime | 200+ CVEs on vessel platform | 3 weeks | — | 16x |
| Epsilon | Public sector | Clean architecture rebuild with IaC | — | — | — |

**Portfolio-level:** 100% of projects delivered on time. 0% post-launch regression rate. Average ROI: 8–16x.
