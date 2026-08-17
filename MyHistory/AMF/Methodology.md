# AI Modernization Discovery — Methodology

> **Source:** Tomasz Mierzejowski's personal IP repositories
> **Last updated:** 2026-07-24
> All claims source-tagged. See AMF/README.md for the tagging convention.

---

## The 60-Hour Discovery Model
<!-- [Source: Discovery_PRD.md v2.4, §2] -->

A standardized, repeatable, AI-semi-automated discovery process for legacy applications. One engagement per repository; each application gets its own clone of the template.

| Phase | Hours | Owner | Description |
|-------|-------|-------|-------------|
| Manual Prep & Sensitive Data Removal | 10h | Human consultant | Static code analysis, remove secrets/credentials/PII before AI access |
| AI-Assisted Discovery | 40h | AI agent | Automated codebase analysis, report generation, iterative refinement |
| Report Review & Customer Delivery | 10h | Human consultant | QA the AI output, prepare customer readout, deliver presentation |
| **Total** | **60h** | | |

The AI discovery time is configurable by package:
<!-- [Source: Discovery_PRD.md v2.4, §3] -->

| Package | Time Tier | What it covers |
|---------|-----------|----------------|
| FULL (recommended) | 60h Deep | All sections, exhaustive business-rule extraction, full self-verification |
| FULL without rules | 60h Deep | Same as FULL, but skips the per-file business-rule extraction sweep |
| QUICK TRIAGE | 20h Quick | High-level assessment, top risks only, abbreviated sections |
| CUSTOM | Configurable | 20h/40h/60h, selectable discovery mode and audience |

### Problem it solves

Manual legacy discovery: 200-400 hours per application, inconsistent across consultants, varying quality. AI-assisted discovery compresses this to 60 hours while scanning 100% of files (not the traditional 5-15% sample).
<!-- [Source: Discovery_PRD.md v2.4, §1.1] -->

### Pricing philosophy

Discovery engagements are priced at **€15K-€40K** depending on scope and complexity.
<!-- [Source: VFR §2] -->

### Discovery timeline

**15-30 days** calendar time per engagement.
<!-- [Source: VFR §2] -->

---

## The Five Promises
<!-- [Source: Discovery_PRD.md v2.4, §1.3] -->

The engagement is sold on five specific promises. Each maps to enforcing mechanisms; each has an honestly stated boundary.

### Promise 1: We scan all the code

**Enforcement:** Coverage ledger (every file, live status), coverage term in ECI, ledger-backed coverage statement.

**Honest boundary:** "Scanned" is ledger-proven. Obfuscated/generated files are excluded with stated reasons, never silently skipped. The Analyzed-vs-Skimmed mix is disclosed.

### Promise 2: We extract all business rules from the code

**Enforcement:** Exhaustive ledger-driven sweep over every domain-logic file at every tier. Greedy-extraction rule. Yield audit with forced re-run if extraction count seems low.

**Honest boundary:** Every domain-logic file is swept; recognition of implicit rules is bounded by static analysis. The "without rules" package skips extraction with a mandatory customer-facing caveat.

### Promise 3: The specification suffices to rebuild with close to zero regression

**Enforcement:** Rebuild specification (flows, testable rules, interfaces, data model, integrations, non-functional behavior). ID-anchored completeness check.

**Honest boundary:** Static analysis cannot capture undocumented runtime behavior. "Close to zero regression" requires this spec + recommended characterization tests + the Specification Gaps list as residual risk.

### Promise 4: We map out all risks of the current state

**Enforcement:** Risk register from all analysis dimensions + mandatory 10-category taxonomy sweep. Explicit "no findings" notes per category. Risk heat matrix.

**Honest boundary:** "All risks identifiable from code, configuration, docs, and provided inputs." Runtime-only and organizational risks are flagged as verification items.

### Promise 5: A defensible, formalized recommendation

**Enforcement:** 7-dimension scored framework + formal 7-path Recommendation Catalog (R0-R6) with deterministic selection. Mandatory Options Considered table (every path accepted/rejected with cited evidence).

**Honest boundary:** The recommendation is code-evidence-based. Business strategy inputs (budget, roadmap, sourcing) can shift the choice.

---

## Evidence Confidence Index (ECI)
<!-- [Source: Discovery_PRD.md v2.4, §4] -->

Every finding, section summary, and overall report carries a numeric percentage (0-100%) and a tier label.

### Tiers

| Tier | Range | Meaning |
|------|-------|---------|
| Very High | 90-100% | Most findings verified; no unresolved Critical/High gaps |
| High | 70-89% | Strong evidence breadth; Critical/High largely verified |
| Medium | 50-69% | Some Critical/High findings unverified or assumed |
| Low | 30-49% | Significant Critical/High gaps; human review required |
| Very Low | 0-29% | Mostly speculative; flagged for re-investigation |

### Evidence Status Labels

| Status | Meaning |
|--------|---------|
| **Verified** | Confirmed by code/config with file:line citation |
| **Partial** | Some evidence, incomplete verification |
| **Assumed** | Inferred from patterns or indirect signals |
| **Inferred** | Derived from absence of evidence |
| **Cannot Determine** | Unresolvable from codebase alone |

### ECI Formula

```
ECI = 0.50 × Verification Rate + 0.35 × Critical Verification Rate + 0.15 × Coverage
```

- **Verification Rate** (weight 0.50): (Verified + Partial) / total scoreable findings
- **Critical Verification Rate** (weight 0.35): Verified among Critical+High / total Critical+High
- **Coverage** (weight 0.15): Analyzed artifacts / total relevant artifacts (from the coverage ledger, not self-graded)

All scores rounded to nearest 10 percentage points. Verbal communication uses tier labels only. The formula is deterministic: improvement deltas in reports are computed, not estimated.

### Design properties

- A single unverified Critical finding visibly pulls the section score down, even when many lower-severity findings are well-evidenced.
- Coverage is anchored to auditable ground truth (the ledger), not model self-assessment.
- Informational findings are excluded from all ratios to prevent score inflation.
- Adding verified Informational findings cannot change a section's score (gaming regression).

---

## Coverage Ledger
<!-- [Source: Discovery_PRD.md v2.4, §4.5] -->

The coverage ledger (`coverage_ledger.md`) records the analysis status of every file in the codebase:

- **Analyzed:** Full analysis completed
- **Skimmed:** Quick review, no deep analysis
- **Excluded:** Justified exclusion (generated, vendored, binary, minified)
- **Not covered:** Not yet examined (counts against Coverage score)

This makes "100% of files scanned" a verifiable artifact, not an assertion. The ledger feeds the Coverage term in the ECI formula.

---

## Cross-Model Verification
<!-- [Source: Discovery_PRD.md v2.4, §4; VFR §2] -->

Marketed as the "Anti-Hallucination Documentation Framework," this is the real mechanism: findings from one AI model are cross-checked against other models and against code evidence. Combined with confidence scoring per finding and file:line citations, this creates a layered verification system:

1. **AI generates findings** with evidence citations
2. **Self-verification pass** catches internal contradictions
3. **Cross-model check** validates against a different AI engine
4. **Human architect review** before any finding reaches the customer
5. **Computed confidence scores** make remaining uncertainty explicit

The label "Anti-Hallucination Framework" is a marketing term. The reality is multi-pass verification with quantified confidence.
<!-- [Source: VFR §2, "Methodology Labels"] -->

---

## Stage 1 to Stage 2 Pipeline
<!-- [Source: Discovery_PRD.md v2.4, §1; Master_Report_PRD.md v1.1; Orchestrator_PRD.md v1.0] -->

### Stage 1: Per-Application Discovery

One repository, one 60-hour engagement, one HTML report. The `app-modernization-template` repository contains the master prompt, PRD, and report template. Output: a self-contained HTML report with confidence scores, evidence citations, risk register, architecture diagrams, and (if FULL package) an exhaustive business-rule catalog.

### Stage 2: Portfolio Consolidation

When an engagement covers multiple applications (e.g., 20 repositories), Stage 2 consolidates all per-app reports into a master portfolio report. The `discovery-report-template` repository handles this. Output: a unified report covering cross-application dependencies, portfolio-wide risks, domain consolidation maps, and a phased modernization roadmap.

The consolidated report uses the same design system, confidence model, and evidence discipline as per-app reports. A CTO receiving both sees one firm, not two.

### The handoff

Stage 1 workspaces (per-app) feed directly into Stage 2 as inputs. The orchestrator automates this: Stage 2 starts only when every Stage 1 repository passes its quality gate.

---

## Evidence Labels
<!-- [Source: Discovery_PRD.md v2.4, §4.2] -->

Every finding in a discovery report carries one of these labels:

| Label | Meaning | Trust level |
|-------|---------|-------------|
| [Discovery-sourced] | Found during AI-assisted codebase analysis | Standard |
| [Code-verified] | Confirmed by specific file:line citation | High |
| [Cross-verified] | Validated by multiple analysis passes or models | Highest |
| [Assumed] | Inferred from patterns, not directly confirmed | Low (flagged for human review) |

---

## Report Structure
<!-- [Source: Master_Report_PRD.md v1.1, §3] -->

The narrative arc puts findings before methodology:

1. **Hero + KPI strip** — the situation at a glance
2. **Verdict banner** — the decision, on screen one
3. **"The one thing"** — the single most important finding
4. **"Cost of inaction"** — explicit "if we do nothing" consequence (never invented cost figures; speaks to risk exposure)
5. **Body sections** — complication to resolution, each with a one-line summary + confidence badge
6. **Methodology & framework value** — moved to the end; how we did it, AI-vs-traditional comparison
7. **Next steps / single CTA** — momentum out

Reports are self-contained HTML: one file, inline CSS, no external dependencies except Mermaid.js via CDN. They export cleanly to PDF.
