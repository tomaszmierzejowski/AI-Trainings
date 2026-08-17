# Anonymized Case Studies — AI Modernization Discovery

> **Source:** All facts from Verified Facts Registry (VFR), July 2026, stripped of customer names.
> **Last updated:** 2026-07-24
> Codenames only. See AMF/README.md for the anonymization policy.

---

## Project Proof of Scale — Enterprise Automotive Dealer Platform
<!-- [Source: VFR §3.1] -->

**Engagement type:** AI-powered cross-repository discovery
**Duration:** 3 weeks (calendar time)
**Team:** 1.5 consultants (one full-time, two part-time including Tomasz)

### The challenge

A 20-repository Java/J2EE legacy platform running a national automotive dealer network. The stack had accumulated over years: EJB 1.1/2.0, Struts 1.1, Spring 4.3, Java 8, Oracle WebLogic. Nobody had a verified picture of what the platform actually contained. A traditional discovery (interview-based, partial code sampling) was estimated at 8-14 weeks.

### What we found

- **187 API endpoints** mapped across all repositories
- **98 inter-service connections** identified, showing how the 20 applications talked to each other
- **Apache Struts 1.1 / CVE-2014-0114** discovered — a critical vulnerability in a framework that had been in production for years
- Complete architecture mapping across all 20 repositories, visualized in a unified mockup

### What we delivered

A **460-page consolidated report** covering all 20 repositories, delivered in **3 weeks** by 1.5 consultants. The report used the full Stage 1 + Stage 2 pipeline: individual per-app discoveries feeding into a portfolio consolidation master report.

### Speed comparison

Approximately **13x faster** than the traditional approach estimate. The aspirational target is 20x post-methodology improvements, but this engagement measured ~13x.
<!-- [Source: VFR §5, "20x faster discovery" — approved with disclaimer: aspirational post-improvements, actual was ~13x] -->

### Discovery cost savings

**87%** reduction in discovery and analysis costs compared to traditional approach. This applies to the discovery/analysis phase only, not full modernization costs.
<!-- [Source: VFR §5, "87% discovery cost savings" — approved with disclaimer: discovery phase only] -->

---

## Project Invisible Risk — Nordic Tolling & Billing Platform
<!-- [Source: VFR §3.3] -->

**Engagement type:** Discovery and modernization planning
**Platform:** .NET/C# enterprise billing system

### The challenge

A large-scale billing and tolling platform with unknown security exposure and undocumented business logic. The platform had been growing for years, and no one had a full picture of what was in it.

### What we found

- **529 anonymous HTTP endpoints** out of ~1,000 total discovered — over half the platform's API surface was running without proper identification or authentication patterns
- **143 business rules** extracted at **94% confidence** (custom AMF scoring methodology)
<!-- [Source: VFR §3.3 — "143 at 94% confidence" confirmed as precise verified count; AI-Trainings uses "100+" for marketing, but 143 is the verified figure] -->
- **~3,500 C# files**, **828 Azure Functions**, **97 projects** (74 non-test)
- **Test coverage: ~24%**
- **Modernization Readiness Score: 45/100**

### The currency mismatch mystery

Different values between the invoicing module and the finance module had gone unexplained for approximately 2 years. Nobody could figure out why the numbers didn't match.

AI-assisted analysis identified the cause: a third-party system had a **hardcoded Danish krone-to-USD conversion rate** embedded in its code. The rate was static, not pulled from any exchange rate service. This finding was subsequently **confirmed by the customer** — who had been looking for this answer for years.
<!-- [Source: VFR §3.3, "The currency mismatch story (verified)"] -->

### Recommendation

Proposal B: Azure Container Apps + Dapr for the modernization path.
<!-- [Source: VFR §3.3] -->

---

## Project Proof of Speed — Pediatric Mobile Health App
<!-- [Source: VFR §3.2] -->

**Engagement type:** Emergency technology migration
**Duration:** 4 days
**Context:** A children's mental health research non-profit needed their mobile app operational before Christmas

### The challenge

Google Play was deprecating Xamarin.Forms support. The app — used for a national pediatric research project — needed to migrate to .NET 8 MAUI or stop working. The research project launch was scheduled for January. Traditional migration estimate: 4-8 weeks.

### What we did

Emergency Xamarin.Forms to .NET 8 MAUI migration completed in **4 days**.

- **92% code preservation** (measured by line count)
- **1,200+ repetitive code changes** handled by AI — the kind of mechanical find-and-replace-with-context work that would take humans days
- **Google Play first-submission approval** — the migrated app passed review on the first attempt
- Only the Android version was deployed and modernized (both platforms existed, but Android was the active one)
<!-- [Source: VFR §3.2 — "both Android and iOS exist; only Android was deployed and modernized"] -->

### The outcome

The app was **operational on Christmas Eve**, enabling the national research project launch in January as planned. Without the 4-day migration, the research project timeline would have been at risk.

### What we're honest about

App startup felt faster after migration, but this was **not benchmarked** — it was perceived improvement, not measured.
<!-- [Source: VFR §3.2 — "Felt faster, NOT benchmarked"] -->

---

## Project The Rescue — Ocean Research Data Collection System
<!-- [Source: VFR §3.4] -->

**Engagement type:** Discovery-phase documentation (October 2025)

### The challenge

A data collection system deployed across **20+ research and reference fleet vessels**. The system ran on embedded hardware: Intel NUC devices (CentOS 7), iPad/Cordova mobile clients, and Raspberry Pi relay stations.

The legacy stack:
- **Meteor 1.8**, **Node.js 8.17**, **React 15.4**, **MongoDB 3.6**
- Every component deeply outdated and carrying known vulnerabilities

### What we found

- **200+ CVEs identified** through SonarQube scanning + AI analysis
- The application had been **undeployable for 2 years** — the team could not deploy software to their hardware
- Root cause: **10 active-looking git branches**, but only **3 were actually in production use**, each tied to different custom hardware configurations. The branch-to-hardware mapping was undocumented.

### What we did

Matched the 3 real production branches to their respective hardware configurations and automated the deployment process with **dockerization**, ending the 2-year deployment block. AI was instrumental in analyzing the branch/hardware relationships and containerizing the deployment.

---

## Banned Metrics — Not Used in Any Case Study

The following claims appeared in earlier versions of these case studies and have been confirmed as AI-generated fabrications or unverified estimates. They are permanently banned:
<!-- [Source: VFR §4] -->

- All ROI multipliers (16x, 10x+, 8-10x, 3-5x) except where specifically approved with disclaimers
- "100% success rate" / "0% regression rate"
- "€80,000+ avoided costs"
- "$500K+ catastrophic failure"
- "100,000+ lines of code" for The Rescue
- "23 critical decision points" for Proof of Speed
- "15% faster startup" for Proof of Speed (not benchmarked)
- "€800K remediation program" for Invisible Risk
- All fabricated customer quotes
- Any customer-identifying information
