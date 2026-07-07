# Discovery: Product Requirements Document

**Version:** 2.1

---

## 1. Vision

A standardized, repeatable, AI-semi-automated discovery process for legacy applications that produces customer-ready HTML reports with quantified confidence scoring. This discovery is the mandatory first step before the **App Modernization Accelerate** phase.

The framework is intentionally scoped to **one engagement per repository**: one input project under `Project/`, one output set under `Outputs/`. Each application that needs to be discovered gets its own clone of this repository.

### 1.1 Problem Statement

Manual legacy application discovery is expensive (200-400h per app), inconsistent across consultants, and produces reports of varying quality. AI-assisted discovery can compress this to 60 hours total while producing more thorough, evidence-backed reports — but only if the AI agent is given a precise, structured prompt that enforces rigor, confidence tracking, and verifiable claims.

### 1.2 Success Criteria

- A single prompt file (`Resources/Discovery_Master_Prompt.md`) that can be loaded into any capable, workspace-aware AI coding assistant (driven by a modern large language model with long-context reasoning and multi-file read/write access) against the codebase in `Project/Code/`
- The prompt produces a complete, customer-ready HTML report under `Outputs/FinalReport/` filling every section of the report template
- Every finding includes an evidence status with evidence citations; every section carries a confidence score
- Coverage is auditable — a coverage ledger (`Outputs/Evidence/coverage_ledger.md`) records the analysis status of every file, so "100% of files scanned" is backed by an artifact, never asserted
- The output is tech-stack agnostic — the prompt auto-detects languages, frameworks, databases, and infrastructure
- Quality matches or exceeds gold-standard discovery reports from prior engagements

---

## 2. The 60-Hour Model

### 2.1 Time Allocation (Default)

| Phase | Hours | Owner | Description |
|-------|-------|-------|-------------|
| Manual Prep & Sensitive Data Removal | 10h | Human consultant | Static code analysis, remove secrets/credentials/PII from code and docs before AI access |
| AI-Assisted Discovery | 40h | AI agent | Automated codebase analysis, report generation, iterative refinement |
| Report Review & Customer Delivery | 10h | Human consultant | QA the AI output, prepare customer readout, conduct presentation |
| **Total** | **60h** | | |

### 2.2 Configurability

The AI discovery time (default 40h) is configurable via the Time Budget clarifying question (see § 3.1). The prompt adapts its thoroughness per tier:
- **20h Quick Scan:** High-level assessment, top risks only, partial sections
- **40h Standard:** Full report coverage, all sections filled, moderate depth
- **60h Deep Discovery:** Exhaustive analysis, business rules extraction, full flow mapping

---

## 3. Clarifying Questions (Canonical Definition)

Before starting analysis, the prompt presents these clarifying questions to scope the discovery. **This section is the single source of truth for all clarifying questions** — the Master Prompt references this section rather than duplicating the question text. Each question uses a multiple-choice format with a default answer. There is no project-selection question — the repository contains exactly one project (under `Project/`).

### 3.1 Question 1: Time Budget

> What is your time budget for AI-assisted discovery?
>
> - **A) 20h — Quick Scan.** High-level assessment, top risks only, partial sections. Best for initial triage.
> - **B) 40h — Standard (recommended).** Full report coverage, all sections filled, moderate depth. Best for most engagements.
> - **C) 60h — Deep Discovery.** Exhaustive analysis, business rules extraction, full flow mapping. Best for complex or high-value applications.
>
> *Default: B (40h Standard)*

This affects the depth of analysis per section — see § 2.2 for the tier definitions.

### 3.2 Question 2: Discovery Mode

> What is the main goal of this discovery?
>
> - **A) General Discovery (default).** Balanced assessment across all dimensions.
> - **B) System Mapping.** Focus on architecture, integrations, and data flows for system planning.
> - **C) Business Rules Mapping.** Deep extraction of business logic, rules, and domain knowledge.
> - **D) Security & Compliance Focus.** Prioritize CVEs, access control, data protection, compliance gaps.
> - **E) Data & Integration Focus.** Deep dive into data models, flows, integration surface.
> - **F) Custom.** You specify focus areas.
>
> *Default: A (General Discovery)*

### 3.3 Question 3: Application Context

> Is this application part of a larger customer system, or is it standalone?
>
> - **A) Standalone.** Independent application.
> - **B) Part of a system.** Provide the system name (used as a label in the report header, e.g., "Financial Platform").
>
> *Default: A (Standalone)*

### 3.4 Question 4: Available Inputs

> What inputs are available beyond the codebase?
>
> - **A) Code only.** Just the source code repository.
> - **B) Code + existing documentation.** Architecture docs, runbooks, READMEs, etc. are present in `Project/Documentation/`.
> - **C) Code + docs + interview notes.** Stakeholder interview transcripts or notes are available in `Project/AdditionalResources/`.
> - **D) Code + docs + interviews + operational data.** Incident logs, monitoring data, deployment history are available.
>
> *Default: A (Code only)*

### 3.5 Question 5: Customer Audience

> Who is the primary audience for this report?
>
> - **A) C-level / business leadership.** Focus on business impact, strategic recommendations, and executive summaries.
> - **B) Technical architects.** Emphasize architecture assessment, integration complexity, and modernization patterns.
> - **C) Development team.** Highlight code quality, technical debt specifics, and actionable remediation steps.
> - **D) Mixed audience (default).** Balanced content addressing all stakeholder levels.
>
> *Default: D (Mixed audience)*

### 3.6 Question 6: Known Context

> Is there anything specific you already know about this application? (Free text — e.g., "This is a Java ERP system, approximately 15 years old, handles order management and invoicing.")
>
> *Default: None — the discovery will detect everything from the codebase.*

### 3.7 Question 7: Engagement Metadata

> Who is this report prepared for and by? (Used to fill the report cover, sidebar, and footer.)
>
> - **Client name** — the organization receiving the report
> - **Consultant name / firm** — shown under "Prepared by"
> - **Organization label** — shown in the sidebar logo (defaults to the consultant firm name)
>
> *Default: None — if not provided, the agent fills these fields with `[TO FILL — consultant]` markers. The agent must never invent client or consultant names.*

---

## 4. Confidence Scoring System

### 4.1 Dual Scale
Every finding, section summary, and overall report carries a numeric percentage (0-100%) and a tier label:

| Tier | Range | Meaning |
|------|-------|---------|
| Very High | 90-100% | Most findings verified; no unresolved Critical/High gaps |
| High | 70-89% | Strong evidence breadth; Critical/High largely verified |
| Medium | 50-69% | Some Critical/High findings unverified or assumed |
| Low | 30-49% | Significant Critical/High gaps; human review required |
| Very Low | 0-29% | Mostly speculative; flagged for re-investigation |

### 4.2 Evidence Status Labels
Each finding's status drives ECI (§ 4.5). Only Critical/High findings enter Critical Verification Rate; Partial is insufficient to close a high-severity gap. All findings require a severity label (Critical, High, Medium, Low, Informational).

**Scoreable findings:** all findings except Informational. Informational findings provide context, not risk — they are excluded from every ECI ratio so a volume of easy verified observations cannot inflate a section's score.

**Per-finding confidence is the evidence status label only.** There are no per-finding numeric scores (removed in the v2.0 ECI migration, § A.4). Customer-facing tables show the status badge.

| Status | Meaning | Verification Rate | Critical Verification Rate |
|--------|---------|:---:|:---:|
| **Verified** | Confirmed by code/config with file:line citation | Yes | Yes |
| **Partial** | Some evidence, incomplete verification | Yes | No |
| **Assumed** | Inferred from patterns or indirect signals | No | No |
| **Inferred** | Derived from absence of evidence | No | No |
| **Cannot Determine** | Unresolvable from codebase (Rule 6) | No | No |

Cannot Determine findings count in the Verification Rate denominator (so they pull the score down) and must each add an item to the section's "What would raise confidence" callout.

### 4.3 Confidence Tracking
`CONFIDENCE_LOG.md` records per section: ECI score/tier, Verification Rate, Critical Verification Rate (or "N/A"), Coverage (with a reference to the coverage ledger rows it was computed from), evidence distribution, evidence used, what would raise ECI (as computed deltas, § 4.8), blocking gaps, and a small-sample flag when the section has fewer than 5 scoreable findings.

The log ends with a **Next-Phase Focus Map** — one row per section: Coverage, Critical Verification Rate, and the indicated action. Low Coverage → analyze more in a follow-on phase; low Critical Verification Rate → external verification needed (interviews, tool scans, ops data); both high → findings can be relied on. This table is the primary input for planning further discovery phases.

### 4.4 Weighted Overall Confidence
| Tier | Weight | Sections |
|------|--------|----------|
| **Primary** | 20% | Risk Register, Security & Compliance |
| **Standard** | 15% | Current State Assessment, Data & Integrations |
| **Supporting** | 10% | Technical Debt, Architecture (Partial), Recommended Path |

Weights sum to exactly 100% (2×20 + 2×15 + 3×10). Skipped/empty sections: exclude and redistribute weight proportionally. Business Rules (Section 11) if present: add at 10%, redistribute so total = 100%. Formula: `overall_confidence = sum(section_ECI × section_weight)` rounded to nearest 10%.

Sections 1 (Executive Summary), 2 (Engagement Overview), and 10 (Next Steps) are not independently scored: Section 1 displays the overall weighted confidence; Sections 2 and 10 carry no confidence badge.

### 4.5 Calculation Formula — Evidence Coverage Index (ECI)
```
ECI = 0.50 × Verification Rate + 0.35 × Critical Verification Rate + 0.15 × Coverage
```

| Term | Formula | Measures |
|------|---------|----------|
| **Verification Rate** | (Verified + Partial) / total scoreable findings | Evidence breadth |
| **Critical Verification Rate** | Verified among Critical+High / total Critical+High | High-severity evidence strength |
| **Coverage** | Analyzed relevant artifacts / total relevant artifacts | How much of the input was actually examined |

**Coverage is objective, not self-graded.** It is computed from `Outputs/Evidence/coverage_ledger.md` — the per-file analysis status inventory — not from the findings list. Each section defines its relevant artifact set:

| Section | Relevant artifacts (ledger subset) |
|---------|-------------------------------------|
| Security & Compliance | Dependency manifests, configuration files, auth/entry-point code |
| Technical Debt | All source files |
| Architecture | Module/source files plus infrastructure and deployment files |
| Data & Integrations | DDL/migrations/ORM models plus integration code |
| Risk Register, Current State | The full ledger |
| Recommended Path | Mean Coverage of the contributing sections above |

Files with ledger status `Analyzed` or `Skimmed` count as analyzed; files marked `Excluded` with a justified reason (generated, vendored, binary, minified) are removed from the denominator; `Not covered` files count against Coverage.

**Weight rationale:**
- **0.50 — Verification Rate** is the primary signal. Broad evidence coverage across all findings is the strongest predictor of whether a section's conclusions can be trusted.
- **0.35 — Critical Verification Rate** ensures that a single unverified Critical or High finding visibly pulls the score down, even when many lower-severity findings are well-evidenced. This prevents a volume of "easy" verifications from hiding the most important gaps.
- **0.15 — Coverage** is the lightest weight because it measures how much input was examined, not whether conclusions are correct — but unlike the two ratios above it cannot be influenced by which findings the agent chooses to report, so it anchors the score to auditable ground truth.
- These weights are structured estimates. After 10+ engagements, they should be validated against reviewer accuracy data and adjusted if needed (see § A.5 #5).

**Critical Verification Rate special case:** If no Critical/High findings, set `Critical Verification Rate = Verification Rate`. Compute ratios → apply formula → ×100 → round to nearest 10% → tier (§ 4.1). Deterministic.

**CVE note:** CVE claims are Assumed unless confirmed by a tool report in `Project/SonarQubeReport/`; they do not count toward Verification Rate or Critical Verification Rate. Log count in CONFIDENCE_LOG.

**CVSS prohibition:** Do not assign CVSS scores — state severity and direct reader to NVD, unless a tool report provides the score.

**Worked example (Risk Register, 6 findings):**

| Finding | Status | Severity | Verification Rate | Critical Verification Rate |
|---------|--------|----------|:---:|:---:|
| RISK-01 (EOL runtime) | Verified | Critical | Yes | Yes |
| RISK-02 (CVE claim) | Assumed | Critical | No | No |
| RISK-03 (no tests) | Inferred | High | No | No |
| RISK-04 (credential exposure) | Verified | High | Yes | Yes |
| RISK-05 (single developer) | Partial | Medium | Yes | N/A |
| RISK-06 (no CI/CD) | Inferred | Medium | No | N/A |

Verification Rate=3/6=0.50, Critical Verification Rate=2/4=0.50, Coverage=1.00 (ledger: 100% of relevant artifacts analyzed) → ECI=0.575 → **60% Medium**

### 4.6 Severity Classification for ECI
Critical and High enter Critical Verification Rate denominator; Medium/Low/Informational do not. See § 4.2 table.

### 4.7 Edge Cases
| Scenario | Rule |
|----------|------|
| **0 scoreable findings** | Exclude from overall average; redistribute weight. Do not interpolate. |
| **Skipped section** | Same as 0 findings. |
| **Only Informational findings** | Treat as 0 scoreable findings (exclude section). |
| **Only Cannot Determine** | Verification Rate = 0 and Critical Verification Rate = 0, so ECI = 0.15 × Coverage (≤ 15 points before rounding). Callout: "Cannot be meaningfully assessed from codebase alone." |
| **Only Medium/Low findings** | Critical Verification Rate = Verification Rate. Note in CONFIDENCE_LOG. |
| **< 5 scoreable findings** | Compute normally, but customer-facing badges show the **tier label only** (no percentage) — with so few findings the ±10-point precision claim would be false. CONFIDENCE_LOG records the raw components with a small-sample flag. |

### 4.8 Presentation Rules
| Context | Format | Example |
|---------|--------|---------|
| CONFIDENCE_LOG.md | % + tier + components + distribution | `60% (Medium) — Verification Rate 50%, Critical Verification Rate 50%, Coverage 100% — 2 Verified, 1 Partial, 1 Assumed, 2 Inferred` |
| HTML section badges | Tier + % | `Medium — 60%` |
| HTML executive scorecard | Tier + % + footnote | `60% Medium` with footnote |
| Customer verbal | Tier labels only | "moderate confidence" |
| HTML "About" card | Methodology + precision | Static card: ECI, tiers, ±10-point precision (not modified per-report) |

**Precision rule:** All ECI scores rounded to nearest 10 percentage points (±10-point precision). Verbal communication uses tier labels only. Sections with fewer than 5 scoreable findings display tier labels only (§ 4.7).

**Computed improvement deltas:** Every item in a "What would raise confidence" callout must state its impact as a **computed** delta: re-run the section's ECI assuming the named evidence upgrades the affected findings to Verified (or raises Coverage), and state the result as *"+N points (computed)"*. The formula is deterministic, so these deltas are exact — never guess improvement percentages.

**Section score vs finding trust:** the section ECI answers *"where should further discovery focus?"*; the per-finding evidence status answers *"can this finding be believed?"*. Never use the section score to justify trust in an individual finding.

### 4.9 Calibration Validation
Permanent regression test — any formula change must pass all six. Coverage inputs are stated explicitly (they come from the ledger, not from the findings):

| Scenario | Findings | Coverage input | Verification Rate | Critical Verification Rate | ECI | Rounded | Tier |
|----------|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **A** — Mostly verified | 8 Verified, 1 Partial, 1 Assumed (all Medium) | 1.00 | 0.90 | =Verification Rate=0.90 | 0.915 | **90%** | Very High |
| **B** — Mixed evidence | 3 Verified, 4 Partial, 2 Assumed, 1 Inferred (all Medium) | 1.00 | 0.70 | =Verification Rate=0.70 | 0.745 | **70%** | High |
| **C** — Mostly unknown | 2 Assumed, 3 Cannot Determine (all Medium); only 40% of relevant artifacts analyzable | 0.40 | 0 | =Verification Rate=0 | 0.060 | **10%** | Very Low |
| **D** — Empty | 0 scoreable findings | — | — | — | N/A | Excluded | N/A |
| **E** — Skipped | Not executed | — | — | — | N/A | Redistributed | N/A |
| **F** — CVE-heavy | 12 Assumed (High) + 3 Verified (High) | 1.00 | 0.20 | 0.20 | 0.320 | **30%** | Low |

**Critical Gap regression:** 10× Medium Verified + 1× Critical Cannot Determine, Coverage 1.00 → Verification Rate=10/11=0.91, Critical Verification Rate=0/1=0 → ECI=0.605 → **60% Medium**. (The Critical gap alone pulls a fully-covered, mostly-verified section down two tiers — this is the behavior the formula exists to guarantee.)

**Gaming regression:** adding 5 Verified **Informational** findings to scenario F must not change its score (Informational findings are excluded from all ratios).

---

## 5. Stable ID Scheme

The discovery uses an app-name-derived prefix for traceable, searchable IDs across all artifacts.

### 5.1 ID Format

The prefix is derived from the application name (e.g., `PORTAL`, `CRM`, `INVOICING`). The prompt auto-generates this from the detected application name or asks the user.

| Entity | Format | Example |
|--------|--------|---------|
| Risk | `{PREFIX}-RISK-{NN}` | `PORTAL-RISK-01` |
| Flow | `{PREFIX}-FLOW-{NN}` | `PORTAL-FLOW-01` |
| Rule | `{PREFIX}-RULE-{CAT}-{NN}` | `PORTAL-RULE-VAL-01` |
| Integration | `{PREFIX}-INT-{NN}` | `PORTAL-INT-01` |
| Finding | `{PREFIX}-FIND-{NN}` | `PORTAL-FIND-01` |
| Gap | `{PREFIX}-GAP-{NN}` | `PORTAL-GAP-01` |
| CVE Reference | `{PREFIX}-CVE-{NN}` | `PORTAL-CVE-01` |

### 5.2 Discovery Metadata

The report includes a metadata header for unambiguous identification:

```yaml
discovery_id: "{PREFIX}-DISC-{YYYY}-{MM}"
application_name: "{application name}"
system_group: "{system group or 'Standalone'}"
discovery_mode: "general"
time_budget_hours: 40
discovery_date: "{YYYY}-{MM}-{DD}"
tech_stack_detected:
  languages: ["C#", "SQL"]
  frameworks: [".NET Framework 4.8"]
  databases: ["SQL Server 2019"]
  infrastructure: ["Windows Server", "IIS"]
overall_confidence: "70% - High"
report_version: "1.0"
```

---

## 6. Output Structure

### 6.0 Workspace Structure

The canonical directory tree is in [`Code_Structure.md`](../../Code_Structure.md). The key principles are:

- The AI reads from `Project/` and writes to `Outputs/` subfolders — never the reverse.
- `Project/SonarQubeReport/` is an optional input. If a SonarQube or other static analysis scan was run, the report is placed here for the AI to cross-reference during Phase 2 (see Master Prompt Section 2.5). The discovery proceeds without it.
- `Resources/` contains the master prompt, this PRD, and the HTML report template — system files that the AI reads but never modifies.
- For another application, clone this repository again. Each clone is one engagement.

### 6.1 Output File Layout

All AI outputs are created under `Outputs/`:

```
Outputs/
  PartialReports/
    00_Discovery_Config.md            # Mode, time budget, tech stack, clarifying answers
    01_Executive_Summary.md           # Detailed executive summary
    02_Engagement_Overview.md         # Scope, methods, coverage, confidence overview
    03_Current_State_Assessment.md    # App profile, tech stack, strengths, constraints
    04_Risk_Register.md               # Full risk register with evidence
    04_Other_Findings.md              # Operational, knowledge, data, integration findings
    05_Technical_Debt.md              # Debt scoring with evidence per dimension
    06_Architecture_Partial.md        # Components, topology, constraints, integration points
    07_Security_Compliance.md         # CVEs, auth, data protection, compliance matrix
    08_Data_Integrations.md           # Data health, integration map, migration risks
    09_Recommended_Path.md            # Decision framework, scoring, recommendation
    10_Next_Steps.md                  # Timeline, owners, decision gates
  FinalReport/
    MASTER_DISCOVERY_REPORT.md        # Consolidated report (key points + links to detail files)
    MASTER_DISCOVERY_REPORT.html      # Customer-ready HTML (filled report template)
  NewDocumentation/
    Discovery_Plan.md                 # Auto-generated analysis plan for this specific discovery
    CONFIDENCE_LOG.md                 # Per-section confidence tracking
    VERIFICATION_LOG.md               # Claim verification audit trail
    README.md                         # Index of all discovery artifacts
    diagrams/                         # Mermaid diagram source files
      architecture_overview.mmd
      integration_map.mmd
      data_flow.mmd
      deployment_topology.mmd
  Evidence/                           # Supporting evidence snapshots
    coverage_ledger.md                # Per-file analysis status — backs all coverage claims
    dependency_scan.md
    code_metrics.md
    security_findings.md
```

> **Naming note:** the auto-generated plan is deliberately *not* named `Discovery_PRD.md` — that would collide with `Resources/Discovery_PRD.md` (this document), which the Master Prompt references as authoritative for § 3 and § 4.

### 6.2 Dual Format Requirement

Every section file exists as `.md`. The master report exists as both `.md` and `.html`. The HTML version uses the report template (see Section 7) and is the customer-facing deliverable.

### 6.3 Master Report Structure

The `Outputs/FinalReport/MASTER_DISCOVERY_REPORT.md` contains:
- Key metrics and scores for each section (not full detail)
- Confidence score per section
- Link to the detailed section file (in `Outputs/PartialReports/`)
- Mermaid diagrams inline
- Discovery metadata header

### 6.4 Evidence Status in Finding Tables

All customer-facing finding tables include an **Evidence Status / Confidence** column so that per-finding confidence is visible without requiring the reader to consult Markdown detail files:

| Table | Column Name | Cell Format |
|-------|-------------|-------------|
| Risk Register (Section 4) | Confidence | Evidence status badge (e.g., "Verified") |
| Flow Index (Section 6) | Confidence | Evidence status badge |
| Business Rules Catalog (Section 11) | Confidence | Evidence status badge |
| Integration Points (Section 8) | Confidence | Evidence status badge |

This ensures that a customer asking "how confident are you about RISK-03?" can answer the question directly from the risk register table.

---

## 7. HTML Template Enhancements

The report template is stored at `Resources/Discovery_Report_Template.html`.

### 7.1 Confidence Score Badges

Add a confidence badge to every section header:

```html
<div class="confidence-badge high">
  <span class="confidence-score">80%</span>
  <span class="confidence-tier">High Confidence</span>
</div>
```

CSS classes: `very-high` (green), `high` (blue), `medium` (yellow), `low` (orange), `very-low` (red).

### 7.2 Overall Confidence Scorecard

Add to the Executive Summary scorecard grid:

```html
<div class="scorecard blue">
  <div class="score-value">70%</div>
  <div class="score-label">Overall Confidence<br/>(weighted)</div>
</div>
```

### 7.3 Evidence Citations

Findings should include source citations:

```html
<div class="evidence-citation">
  <span class="evidence-icon">📄</span>
  <code>src/services/OrderProcessor.cs:142-168</code>
  <span class="evidence-status verified">Verified</span>
</div>
```

### 7.4 "What Would Raise Confidence" Callouts

Each section should include:

```html
<div class="callout confidence-improvement">
  <strong>What would raise confidence:</strong>
  <ul>
    <li>Access to production deployment configuration (high impact — would verify deployment topology findings)</li>
    <li>Interview with the original developer (high impact — would verify business logic and knowledge concentration findings)</li>
    <li>Review of incident/support ticket history (moderate impact — would verify operational risk findings)</li>
  </ul>
</div>
```

### 7.5 Discovery Metadata

Add a metadata section to the cover:

```html
<div class="meta-item">
  <div class="meta-label">Discovery ID</div>
  <div class="meta-value">{PREFIX}-DISC-{YYYY}-{MM}</div>
</div>
<div class="meta-item">
  <div class="meta-label">System Group</div>
  <div class="meta-value">Financial Platform</div>
</div>
```

### 7.6 Engagement Hours

The default is configurable, showing both AI hours and total:

```html
<div class="meta-item">
  <div class="meta-label">AI Discovery Hours</div>
  <div class="meta-value">38 / 40 hrs</div>
</div>
```

### 7.7 Sidebar Enhancement

Add a "Confidence" section to the sidebar showing per-section confidence as a mini heatmap or list.

### 7.8 Value-First Visual Components

The template leads with visuals that make the engagement's value and rigor legible to a customer at a glance. All of them are **projections of computed numbers** (ledger, CONFIDENCE_LOG, Risk Register) — the Master Prompt's chart integrity rule forbids filling any of them with estimates, and VC-02 cross-checks every chart figure.

| Component | Where | Shows | Fill mechanism |
|-----------|-------|-------|----------------|
| "By the numbers" KPI strip | Cover | Files analyzed, coverage %, LOC, rules, flows, integrations | Ledger-backed values; remove unbackable tiles |
| Decision gauge | Verdict banner + Section 9 | Score position across Remediate / Hybrid / Modernize bands | Marker `left = (score − 7) / 14 × 100%` |
| Findings-by-severity bar | Section 1 | Stacked severity mix with legend counts | `flex-grow: {count}` per segment |
| Risk Landscape matrix | Section 1 | Impact × likelihood grid with one chip per risk | Chips placed per register columns |
| Evidence & Coverage panel | Section 1 | Coverage meter, verification meter, evidence-status distribution | Ledger + CONFIDENCE_LOG values |
| Diagram cards (Mermaid) | Sections 6, 8 | Architecture, data flow, integration map (+ deployment/sequence at 60h) | `<pre class="mermaid">` + CDN loader; offline shows readable source |
| Score dots | Section 9 | 1–3 dot scale per decision dimension | Class `s1`/`s2`/`s3` |

**Color system:** report chrome uses the brand palette — Purple Dark `#4D1D82`, Orange `#E8640A` (accents/marks; darker `#C55208` for small text on light, lighter `#F5883F` on dark), Dark BG `#1A0A2E`, Light BG `#F8F6FC`. Data marks keep the CVD-validated semantic palettes and never restate brand colors: severity `#d03b3b / #ec835a / #eda100 / #2a78d6` (Critical→Low), evidence `#0ca30c / #2a78d6 / #eda100 / #7568c9 / #d03b3b` (Verified / Partial / Assumed / Inferred / Cannot Determine). Every chart ships with a legend and labels so color never carries meaning alone; the print stylesheet preserves chart colors and hides the sidebar.

---

## 8. Discovery Execution Flow

### 8.1 Phase 0: Configuration (Prompt Start)

1. Present clarifying questions (Section 3 of this PRD)
2. Collect answers and store in `Outputs/PartialReports/00_Discovery_Config.md`
3. Derive the ID prefix from the application name
4. Set time budget and depth parameters

### 8.2 Phase 1: Codebase Reconnaissance (Hours 0-8)

1. **Directory structure analysis** — Map the full project tree of `Project/Code/`, identify modules, layers, entry points
2. **Tech stack detection** — Languages, frameworks, build tools, dependency manifests, database types
3. **Size and complexity metrics** — File counts, line counts per language, directory depth, module boundaries
4. **Dependency inventory** — Parse all manifest files, identify versions, flag EOL/deprecated
5. **Initial risk signals** — Flag obvious issues (no tests, no CI, hardcoded credentials patterns)
6. **Coverage Ledger creation** — Enumerate every file under `Project/Code/` into `Outputs/Evidence/coverage_ledger.md` with per-file analysis status (see § 9.4)
7. Output: `Outputs/NewDocumentation/Discovery_Plan.md` + `Outputs/PartialReports/00_Discovery_Config.md` + `Outputs/PartialReports/03_Current_State_Assessment.md` (draft) + `Outputs/Evidence/coverage_ledger.md`

### 8.3 Phase 2: Deep Analysis (Hours 8-28)

Execute in this order, updating documentation after each step:

1. **Security scan** (→ `Outputs/PartialReports/07_Security_Compliance.md`)
   - Dependency CVE check
   - Secrets/credentials in code
   - Authentication patterns
   - Data protection practices
   - Compliance signals

2. **Code quality & debt assessment** (→ `Outputs/PartialReports/05_Technical_Debt.md`)
   - Complexity analysis
   - Test coverage detection
   - Code duplication patterns
   - Dead code identification
   - Documentation quality

3. **Architecture mapping** (→ `Outputs/PartialReports/06_Architecture_Partial.md`)
   - Component identification
   - Layer separation analysis
   - Deployment topology inference
   - Mermaid diagram generation

4. **Data & integration analysis** (→ `Outputs/PartialReports/08_Data_Integrations.md`)
   - Database schema analysis
   - Stored procedure inventory
   - Integration point mapping
   - Data flow tracing
   - Mermaid integration map

5. **Business rules extraction** (→ `Outputs/PartialReports/04_Risk_Register.md`, `Outputs/PartialReports/04_Other_Findings.md`)
   - Domain logic identification
   - Validation rules
   - Business flow mapping
   - Knowledge concentration assessment

### 8.4 Phase 3: Synthesis & Scoring (Hours 28-36)

1. Cross-reference all findings
2. Apply the 7-dimension decision framework (score 1-3 per dimension)
3. Calculate overall risk score (/21)
4. Apply override rules (EOL, critical CVEs)
5. Determine recommended path (Remediate / Hybrid / Full Modernization)
6. Generate `Outputs/PartialReports/09_Recommended_Path.md` and `Outputs/PartialReports/10_Next_Steps.md`
7. Update confidence scores across all sections

**Effort/cost estimate guard:** The AI must NOT provide specific effort estimates (e.g., "6-8 weeks"), cost figures (e.g., "$200K"), or team size recommendations. These require scoping information not available from code analysis alone. Instead, state: *"Effort and cost estimation requires a follow-on Architecture & Scoping engagement."* Mark any rough magnitude estimates (e.g., "multi-month effort") as `[SHOULD VERIFY]`.

### 8.5 Phase 4: Report Assembly (Hours 36-40)

1. Generate `Outputs/PartialReports/01_Executive_Summary.md` (synthesizes all sections)
2. Generate `Outputs/PartialReports/02_Engagement_Overview.md`
3. Compile `Outputs/FinalReport/MASTER_DISCOVERY_REPORT.md` with links to all detail files
4. Generate `Outputs/FinalReport/MASTER_DISCOVERY_REPORT.html` using the template at `Resources/Discovery_Report_Template.html`
5. Final `Outputs/NewDocumentation/CONFIDENCE_LOG.md` and `Outputs/NewDocumentation/VERIFICATION_LOG.md`
6. Self-QA pass: verify all claims have evidence citations, all IDs are consistent, all scores are justified
7. Coverage verification (VC-11): confirm the coverage ledger is complete, compute the final coverage percentage, and report it in the Engagement Overview with any `Not covered` files listed by name

---

## 9. Quality Standards

### 9.1 Expert-Level Analysis

The prompt must instruct the AI to perform at the level of the **top 0.1% of software discovery and reverse-engineering experts**. This means:

- Never accept surface-level observations — always dig into the code for evidence
- Trace data flows end-to-end, not just identify entry points
- Identify implicit business rules hidden in code patterns, not just explicit ones
- Recognize architectural anti-patterns and their specific business impact
- Quantify findings wherever possible (counts, percentages, severity scores)
- Distinguish between "this is bad practice" and "this is an active risk to the business"

### 9.2 Evidence Discipline

Every claim in the report must follow this evidence standard. The master prompt enforces 8 non-negotiable rules:

1. **File + line citation** for code-based findings (e.g., `src/services/OrderProcessor.cs:142`)
2. **Full metric provenance** — every quantitative claim must include: search method, scope, exact-vs-estimated, and known limitations
3. **Label synthetic examples** — any data example the AI creates must be marked: *"Example data — not from production."*
4. **Separate code-proven from externally-dependent** — findings that depend on external system behavior must be labeled: *"Externally dependent — cannot verify from codebase alone."*
5. **Log metric discrepancies** — maintain `Outputs/NewDocumentation/VERIFICATION_LOG.md` tracking what was checked and what was found
6. **"Cannot Determine" protocol** — when the AI cannot determine a value from the codebase (e.g., EOL status, CVE details, latest library version, production topology, compliance applicability), it must: state what CAN be determined, state what external verification is needed, mark the finding as `[Assumed]` or `[Inferred]` (never `[Verified]`), and tag with `[MUST VERIFY]` or `[SHOULD VERIFY]` per Rule 8.
7. **"Claim Isolation" for security findings** — every security finding must separate: **"What the code shows"** (observable facts with citation, Verified evidence) from **"What this may mean"** (security implication, Assumed/Inferred evidence). This allows human reviewers to validate facts independently of interpretation.
8. **Human verification tags (two tiers):**
   - `[MUST VERIFY]` — specific CVE IDs/CVSS scores, Critical findings with only Assumed/Inferred evidence, compliance obligation applicability
   - `[SHOULD VERIFY]` — business criticality, user base size, cost estimates, incident history, deployment topology (when no IaC present)
   - **Interpreting untagged claims:** Findings without a tag are backed by Verified or Partial evidence. They have the highest evidence quality and should be prioritized last during human review.

### 9.3 Multi-Pass QA

The prompt must include a self-verification step:

1. After generating each section, re-read the code to verify claims
2. Cross-check metrics between sections (e.g., "14 CVEs" in Executive Summary matches the count in Security section)
3. Ensure all IDs are sequential and referenced correctly
4. Verify Mermaid diagrams render correctly
5. Check that confidence scores are justified by evidence

### 9.4 Coverage Accounting

The engagement promises that 100% of files are scanned and that business-rule extraction is exhaustive. These claims are backed by an auditable artifact — never by assertion:

- **Phase 1** enumerates every file under `Project/Code/` into `Outputs/Evidence/coverage_ledger.md`.
- Every file carries a status the agent updates continuously: `Analyzed` (read and assessed), `Skimmed` (opened; structure and purpose identified), `Excluded` (generated / vendored / binary / minified — always with a stated reason), or `Not covered`.
- **Business-rule sweep:** during Phase 2 every `Analyzed`/`Skimmed` file is classified as domain-logic or non-domain (plumbing, UI scaffolding, configuration, tests, generated). Every domain-logic file receives a rule-extraction pass and records either its extracted rule IDs or an explicit "no extractable business rules" note in the ledger. The sweep runs in full at **every** time tier — tiers vary only in how deeply rules are documented, never in whether extraction happens.
- **Phase 4** computes `Coverage = (Analyzed + Skimmed) / (total − Excluded)`, verifies the ledger (VC-11), reports the coverage statement in the Engagement Overview, and lists any `Not covered` files by name.
- **Honest claim boundary:** the report may state "100% of files scanned" only when the ledger shows 100%. It must never claim every *implicit* rule was necessarily recognized — the coverage statement is evidence-based, e.g.: *"100% of 214 domain-logic files swept; 87 business rules extracted."*

---

## 10. Prompt Engineering Techniques (from Lyra)

The final master prompt must incorporate these techniques from the Lyra system:

### 10.1 Role Assignment
Assign the AI a specific expert role with clear authority and constraints.

### 10.2 4-D Methodology
- **Deconstruct:** Analyze the codebase systematically before drawing conclusions
- **Diagnose:** Identify gaps, risks, and patterns before prescribing solutions
- **Develop:** Build findings with evidence, scoring, and cross-references
- **Deliver:** Produce structured, formatted, customer-ready outputs

### 10.3 Chain-of-Thought
For complex analysis (architecture inference, risk scoring, path recommendation), require explicit reasoning steps before conclusions.

### 10.4 Constraint Optimization
- Time box awareness (adapt depth to available hours)
- Confidence thresholds (flag when below 50%, block report delivery below 30%)
- Scope boundaries (explicitly state what is and isn't covered)

### 10.5 Context Layering
Build understanding in layers: codebase structure → dependency analysis → code quality → architecture → integrations → synthesis.

---

## 11. Constraints & Assumptions

1. **One engagement per repository** — A repository hosts exactly one input project (`Project/`) and produces exactly one output set (`Outputs/`). Discovering another application requires a separate clone of this repository.
2. **Read-only on application code** — The AI agent never modifies anything under `Project/`; it reads from `Project/Code/` and creates files in `Outputs/` subfolders.
3. **No runtime access** — No database connections, no API calls, no production environment access.
4. **Sensitive data removed** — The human consultant has already sanitized secrets/credentials before AI access (Phase 0 of the 60h model).
5. **Workspace-aware AI coding assistant** — The prompt is designed for any modern large language model operating inside a coding assistant that has read access to the repository's files and write access for creating output files. It does not assume any vendor-specific mode, tool-calling schema, or proprietary feature; any planning/reasoning mode the environment provides should be enabled when available.
6. **Single application scope** — Each discovery targets one application (or tightly coupled cluster treated as one unit).
7. **English only** — All outputs are in English.
8. **Mermaid diagrams only** — No PlantUML; Mermaid renders natively in HTML without external dependencies.

---

## 12. Reference Materials

| Document | Location | Purpose |
|----------|----------|---------|
| Discovery Master Prompt | `Resources/Discovery_Master_Prompt.md` | The prompt the consultant pastes into their AI coding assistant |
| Discovery Report Template | `Resources/Discovery_Report_Template.html` | HTML template with confidence badges, evidence citations, sidebar heatmap |
| Lyra System | `Tools/Lyra.md` | Prompt engineering techniques (4-D Methodology) |

---

## Appendix A: Design Decisions

This appendix documents key design decisions and their rationale for reference by anyone maintaining or extending the discovery system.

---

### A.1 Feature Decisions

#### Single-Project Repository Model

**Decision:** Each repository represents **exactly one engagement** — one input project under `Project/`, one output set under `Outputs/`. To discover another application, clone the repository again.

**Rationale:** Earlier iterations of the framework supported multiple projects per repository with templates and per-project subfolders. In practice this added meaningful operational complexity (path resolution, project selection, cross-project aggregation) for marginal benefit. Folding the model down to one-project-per-repository removes an entire class of confusion: there are no `{PROJECT}` placeholders to resolve, no template folders to copy, no project-selection step, and no risk of an output landing under the wrong subfolder. Cloning the repository is cheap; the cost of multi-project ambiguity is not.

**Implementation:** All paths in the master prompt and PRD are fixed (`Project/Code/`, `Outputs/PartialReports/`, etc.). Phase 0 has no project-selection step. There is no Templates/ folder.

#### Business Rules Catalog

**Decision:** Include as **optional Section 11** in the HTML template.

**Rationale:** A structured business rules catalog with stable IDs, per-rule evidence status, and cross-references to flows adds significant value — particularly for engagements where business logic extraction is a primary goal. Extraction itself always runs in full (the ledger-driven sweep, § 9.4) — what varies by tier and mode is only how deeply the extracted rules are *documented* in the customer-facing report.

**Implementation:** One unified inclusion rule (used by the Master Prompt and the template): include Section 11 when the discovery mode is Business Rules Mapping (Mode C), **or** when more than 10 rules were extracted (summary rows: one line per rule); use full per-rule detail when more than 20 rules were extracted or in Deep Discovery (60h). When neither applies the HTML section is removed — the complete extracted rule list always remains in the Markdown partial reports and the coverage ledger.

#### Flow Index

**Decision:** Include as a **subsection of Architecture (Section 6)**, always present.

**Rationale:** A flow index providing a single reference table for all identified data and business flows is one of the most valuable artifacts in a discovery report. It makes it easy for stakeholders to understand the application's behavior at a glance. Placing it within Architecture (rather than as a standalone section) keeps the report structure clean while ensuring it's always produced.

**Implementation:** Even Quick Scan gets a lightweight flow list (top 5 flows). Standard gets all detected flows. Deep Discovery gets all flows with step-by-step flow cards.

#### Presentation Walkthrough Guide

**Decision:** Include as **Section 10.5 "Report Walkthrough Guide"** within Next Steps.

**Rationale:** A standalone presentation plan file adds operational complexity. A lightweight walkthrough guide embedded in the Next Steps section serves the same purpose — giving the consultant a suggested presentation order, time allocation per section, and key talking points — without requiring a separate artifact.

**Implementation:** A table with columns: Order, Section, Time, Key Talking Points. Default is a 45-minute readout. Included in both the Markdown and HTML outputs.

#### Verification — Embedded vs. Separate

**Decision:** **Embedded as Phase 4** within the master prompt.

**Rationale:** Adversarial QA is most effective when the same agent that performed the analysis can re-read the code to verify its own claims. A separate companion prompt would lose the analysis context, require re-reading large portions of the codebase, and add operational complexity. Embedding the verification as Phase 4 ensures it always runs as part of the discovery flow.

**Implementation:** Phase 4 includes a 10-item self-verification checklist. For 60h Deep Discovery, an additional adversarial re-check is performed on the top 3 highest-severity findings: re-read cited code, verify claims, check for alternative interpretations, downgrade if weakened.

#### Analysis Phase Ordering

**Decision:** Optimized order for maximum context building:

1. Structure & Size (builds mental map)
2. Dependencies & EOL (identifies immediate risks)
3. Security (uses dependency data)
4. Code Quality & Debt (uses structure data)
5. Architecture & Flows (uses all above)
6. Data & Integrations (uses architecture)
7. Business Rules (uses flows + data)
8. Synthesis & Scoring (uses everything)

**Rationale:** Security is placed before Code Quality because security findings (especially CVEs) directly inform debt scoring and the risk register. Business Rules extraction is placed last because it requires maximum context — understanding the architecture, data model, and integration surface before reliably identifying where business rules live and what they do.

#### Incremental Runs / Resume

**Decision:** Support via `Outputs/PartialReports/00_Discovery_Config.md` with a `last_completed_phase` field.

**Rationale:** Large codebases may require multiple sessions. The discovery agent should be able to detect a partially-completed discovery and offer to resume. Each phase writes its completion status to the config file, and on startup the agent checks for this file.

**Implementation:** If `Outputs/PartialReports/00_Discovery_Config.md` exists and contains a `last_completed_phase` field, the agent displays completed phases and asks: "Resume from next phase, or start fresh?"

### A.2 Prompt Design Rationale

**Why 9 sections, not more:** The master prompt is structured as 9 top-level sections (Identity, Methodology, Phase 0-4, Output Specs, Appendices) because this maps cleanly to the 4-D framework and keeps the prompt navigable. Each phase is self-contained with its own checkpoint, so the executing agent can track progress without losing context.

**Why phases have explicit checkpoints:** Large language models handle long prompts well but can lose track of position in a multi-hour analysis. Each phase ends with a checkpoint that summarizes what was produced and what comes next. This serves as both a progress indicator for the user and a context anchor for the agent.

**Why context layering is enforced:** The analysis order (Structure → Dependencies → Security → Code Quality → Architecture → Data → Business Rules → Synthesis) is not arbitrary. Each layer builds on the previous. Attempting to write the Architecture section before understanding dependencies leads to missed integration points. Attempting to extract business rules before understanding the data model leads to incomplete rule catalogs.

**Why the HTML template is referenced but not embedded:** Embedding the full HTML template in the prompt would add ~15K tokens of HTML/CSS that the agent needs to parse but rarely references during analysis. Instead, the prompt provides filling instructions (Section 7.3 of the master prompt) that reference the template's structure. The template file lives at `Resources/Discovery_Report_Template.html` and is used during Phase 4 only.

**Why evidence discipline is non-negotiable:** Prior discoveries demonstrate that evidence-backed findings are dramatically more credible than unsupported claims. The eight evidence discipline rules are placed in Section 1 (before methodology) to establish them as foundational constraints, not optional guidelines.

---

### A.3 Known Limitations

1. **External system behavior.** The discovery cannot verify how external systems behave. Integration findings are limited to what the codebase reveals about connection methods, data formats, and error handling. The actual behavior of connected systems requires separate investigation.

2. **Runtime-only patterns.** Performance characteristics, memory usage, concurrency issues, and race conditions are generally not detectable from static code analysis. The prompt acknowledges this limitation and flags runtime-dependent findings as lower confidence.

3. **Data volume analysis.** Without database access, the discovery cannot assess actual data volumes, query performance, or storage utilization. Schema analysis is limited to what DDL files, migration scripts, or ORM models reveal.

4. **Interview-dependent findings.** Business context, organizational knowledge, incident history, and operational practices are only available if interview notes or documentation are provided. Code-only discoveries will have lower confidence in the Knowledge Concentration and Operational Cost dimensions.

5. **Obfuscated or generated code.** Minified JavaScript, compiled binaries, generated code (e.g., from code generators or scaffolding tools), and obfuscated code cannot be meaningfully analyzed. The prompt instructs the agent to note these as coverage gaps.

6. **Multi-repository applications.** The prompt assumes the contents of `Project/Code/` represent the full application. If the application spans multiple repositories, the discovery will only cover what's in `Project/Code/`. Cross-repo dependencies will be flagged as external integrations.

7. **AI model limitations.** The executing model may hallucinate file paths, invent CVE numbers, or miscount entities. The self-verification checklist (Phase 4) is designed to catch these errors, but human review of the final report remains essential.

---

### A.4 Confidence Scoring: Migration from Severity-Weighted Average to ECI

**Decision:** Replace the severity-weighted average formula with the Evidence Coverage Index (ECI) as of PRD v2.0. As of v2.1, the Completeness term is replaced by ledger-based Coverage (see the v2.1 addendum at the end of this section).

**Problem with the prior model:**
The prior formula (`section_confidence = Σ(evidence_score × severity_weight) / Σ(severity_weight)`) had one dominant failure mode: a section with a large number of well-evidenced low-severity findings could score as "High confidence" even when a single Critical finding was Cannot Determine. In the most extreme case — 10 Verified Medium findings plus 1 Critical Cannot Determine — the prior formula returned 79% (High), concealing the unresolved Critical gap from the report reader. This is the precise scenario that matters most: discovering that the single most important finding cannot be confirmed from the codebase alone.

Secondary issues: the evidence score constants (1.00/0.65/0.40/0.25/0.10) and severity weights (3.0/2.0/1.0/0.5) were arbitrary and not calibrated; the CVE hard-cap mechanism was nearly always a no-op because CVE claims are typically marked Assumed (0.40), which is already below the 0.60 cap; and rounding to nearest 5% while claiming ±10% actual precision produced false precision.

**Why ECI:**
The Evidence Coverage Index replaces one opaque severity-weighted average with three named, interpretable ratios:
- **Verification Rate** answers: how broadly did we verify findings?
- **Critical Verification Rate** answers: are the highest-severity findings actually confirmed?
- **Completeness** answers: how many findings are structurally unresolvable?

Critical Verification Rate is the key structural addition. When a Critical or High finding is Cannot Determine, Critical Verification Rate moves toward zero, pulling the entire section score down regardless of how many low-severity findings are verified. This directly fixes the dominant failure mode.

**Tradeoffs accepted:**
- Scenario B (3 Verified, 4 Partial, 2 Assumed, 1 Inferred — all Medium) now scores 70% (High) rather than the prior 65% (Medium). This is considered more accurate: a section where 70% of findings carry real evidence, with no unresolved Critical or High gaps, is legitimately High confidence. The prior model's Medium result was an artifact of the Assumed/Inferred score constants dragging down the average.
- Scenario F (CVE-heavy) now scores 30% (Low) rather than 55% (Medium). This is considered more accurate: 12 of 15 findings are unverified assumptions.
- The CVE hard-cap mechanism is removed. It is replaced by the natural behavior of the formula: Assumed CVE claims do not count toward Verification Rate or Critical Verification Rate, which produces the appropriate downward pressure without a separate cap constant.
- Backward compatibility with prior reports is broken. Reports generated under the old formula will show different percentages and, in some cases, different tiers. All new engagements use ECI from this version forward.

**Calibration note:** The ECI term weights (0.50/0.35/0.15) are structured estimates, not empirically calibrated. After 10+ engagements, reviewer accuracy data should be used to validate or adjust these weights per § A.5 future improvement #5.

**Implementation:** The Master Prompt scoring section, CONFIDENCE_LOG.md template, and HTML badge logic must all be updated to match the new formula. The CONFIDENCE_LOG must explicitly record Verification Rate, Critical Verification Rate, and Coverage as separate computed fields so the score is fully auditable.

**v2.1 addendum — Completeness → Coverage:** The Completeness term (`1 − CannotDetermine/total`) was replaced by ledger-based Coverage in v2.1 because it was self-graded: it only counted findings the agent itself chose to label "Cannot Determine," so an agent that simply never wrote such findings scored Completeness = 1.00 while potentially knowing nothing. Coverage is computed from the per-file inventory in `Outputs/Evidence/coverage_ledger.md` and cannot be improved by omission — the only way to raise it is to analyze more files. Cannot-Determine findings still exert downward pressure through the Verification Rate denominator. Two further v2.1 hardening changes: Informational findings are excluded from all ratios (anti-inflation), and sections with fewer than 5 scoreable findings present tier labels only (honest precision). The § 4.9 calibration scenarios were restated with explicit Coverage inputs; all scenario tiers are unchanged (the Critical Gap regression moves from 0.591 to 0.605, still 60% Medium).

---

### A.5 Future Improvements

1. **Multi-agent verification.** Use a second AI agent (different model or different prompt) to independently verify the primary agent's findings. Compare results and flag disagreements. This would significantly increase confidence in the output.

2. **Automated Mermaid rendering check.** Integrate a Mermaid syntax validator that checks all generated diagrams before including them in the HTML report. Currently, syntax errors are caught by the self-verification checklist but not automatically fixed.

3. **Integration with SCA tools.** If the workspace has access to tools like `npm audit`, `pip-audit`, `dotnet list package --vulnerable`, or OWASP Dependency Check, the prompt could invoke these for more accurate CVE detection rather than relying on version-based inference.

4. **Interactive mode.** Instead of running the full discovery end-to-end, allow the user to run individual phases or sections on demand. This would support iterative refinement and allow the consultant to guide the analysis based on emerging findings.

5. **Confidence calibration.** After running the prompt against 10+ real codebases, analyze the correlation between stated confidence and actual accuracy (as judged by human reviewers). Use this data to calibrate the confidence scoring thresholds.

6. **Template customization.** Allow the HTML template to be branded per consulting firm (logo, colors, footer text) via a simple configuration block, without requiring the consultant to edit HTML.
