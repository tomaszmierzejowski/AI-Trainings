# Unified Final Report — Product Requirements Document

**Version:** 1.1 (promoted to `Resources/` 2026-07-10)
**Status:** Live for the **portfolio scope** — `Resources/Master_Report_Template.html` is the template the Cross-Repo prompt fills (§ 7.2). The single-app scope remains served by `Discovery_Report_Template.html` in `app-modernization-template` until a future promotion.
**Companion assets:** `Master_Report_Template.html` (the implementation, design tokens inlined), `Backlog/Portfolio_ECI_Validation.md` (portfolio confidence formula, pending application).

---

## 1. Vision

One report system for **every** modernization discovery engagement — whether the subject is a **single application** or a **multi-repository portfolio**. Today the framework produces two visually unrelated deliverables from two different mechanisms (a per-app template vs. cross-repo HTML generated from scratch). A client receiving both sees two firms. This PRD defines a single, scope-adaptive report so that:

- The **same shell, components, confidence model, and design tokens** are used in both cases.
- Only the **section set** changes with scope. Everything else is identical.
- A CTO understands the investment case from the first screen; a principal engineer trusts and can reference the evidence; a board sponsor forwards it because it reads like a top-tier consultancy, not an AI tool.

**This PRD always applies.** Both the Discovery master prompt (single app) and the Cross-Repo Consolidation master prompt (portfolio) fill *this one template* per *this one spec*.

### 1.1 Non-negotiable principles (inherited)

1. **Evidence integrity above aesthetics.** No layout choice hides or de-emphasizes a citation, confidence score, or verification tag.
2. **Single-file portability.** One self-contained `.html` with inline CSS. Only external dependency: Mermaid.js via CDN. No web fonts, no JS frameworks, no build step, no asset directory.
3. **Print fidelity.** The report must export to a clean, professional PDF. The printed version is often what the CTO actually reads.
4. **Brand adaptability.** Works with any client palette by changing only the brand tokens (the `:root` token block inlined at the top of `Master_Report_Template.html`; live palette rules: `Discovery_PRD.md` § 7.8 in `app-modernization-template` — red/orange-dominant, purple as gradient start only, white navigation).
5. **Accessibility baseline.** WCAG 2.1 AA contrast; meaningful heading hierarchy; charts never rely on color alone (legend + labels always present).

---

## 2. Scope model

The report has exactly one variable input that changes structure: **`report_scope`**.

| `report_scope` | Subject | Filled by | Section set |
|----------------|---------|-----------|-------------|
| `application` | One application (`Project/Code/`) | `Discovery_Master_Prompt.md` | § 4.1 (11 sections) |
| `portfolio` | N repositories | `CrossRepo_Consolidation_Master_Prompt.md` | § 4.2 (4 parts) |

Everything in §§ 3, 5, 6, 7, 8 is **identical for both scopes**. The template carries both section sets; the filling prompt keeps the block matching its scope and deletes the other (each block is delimited by `<!-- SCOPE:application ... -->` / `<!-- SCOPE:portfolio ... -->` comment markers).

Set `report_scope` in the report's metadata header (YAML in the `.md` twin, `data-scope` attribute on `<body>` in the HTML).

---

## 3. Narrative arc (identical for both scopes)

The reader meets **what we found and what to do** before **how we did it**. Fixed order:

1. **Hero + KPI strip** — the situation at a glance.
2. **Verdict banner** — the decision, on screen one, with a decision gauge.
3. **"The one thing"** — the single most important finding, spotlighted.
4. **"Cost of inaction"** — an explicit "if we do nothing" consequence (never invents cost/effort figures; speaks to risk exposure).
5. **Body sections** (scope-dependent) — complication → resolution, each opening with a one-line summary + confidence badge.
6. **Methodology & framework value** — *moved to the end.* How we did it, the AI-vs-traditional comparison, the evidence discipline.
7. **Next steps / single CTA** — momentum out.

Anti-patterns this ordering exists to prevent: methodology before findings; bare confidence scores with no business translation; equal visual weight for Critical and Low findings; a report that opens with "About this engagement"; a report that ends with a thud.

---

## 4. Section sets

### 4.1 `report_scope: application` (11 sections)

Preserves the current per-app section set and every data point in it — only ordering/framing/disclosure change.

| # | Section | Confidence badge | Notes |
|---|---------|:---:|-------|
| — | Hero + Verdict + "one thing" + "cost of inaction" | overall (in hero) | front matter |
| 1 | Executive Summary | overall weighted | severity bar, risk-landscape matrix, evidence & coverage panel, "About Confidence" card |
| 2 | Engagement Overview | none | ledger-backed coverage statement lives here |
| 3 | Current State Assessment | yes | |
| 4 | Risk Register | yes | full table + Critical/High as finding cards |
| 5 | Technical Debt | yes | debt bars |
| 6 | Architecture (+ Flow Index) | yes | Mermaid diagram cards |
| 7 | Security & Compliance | yes | CVE list, auth, compliance |
| 8 | Data & Integrations | yes | integration table + map |
| 9 | Recommended Path | yes | decision framework + gauge + pros/cons |
| 10 | Next Steps | none | timeline + walkthrough guide |
| 11 | Business Rules | yes | conditional (PRD § A.1 inclusion rule) |
| — | Methodology & framework value | — | moved to end |

### 4.2 `report_scope: portfolio` (4 parts)

| Part | Title | Content |
|------|-------|---------|
| — | Hero + Verdict + "one thing" + "cost of inaction" | KPI strip: # apps, endpoints, connections, domains, depth |
| 1 | Executive Overview | portfolio summary (per-app cards/table), overall confidence. *AI-framework-value + Traditional-vs-AI table move to Part 4.* |
| 2 | As-Is Analysis — What We Found | Platform Health Scorecard, Case for Change, Endpoint Summary, Application Map (service mesh — clustered above ~25 nodes), Database Connectivity, **Portfolio Coupling** (cross-repo processes, shared-lib blast radius, deployment coupling, data lineage, ownership) |
| 3 | Target Architecture — Where To Go | mandatory recommendation divider (verbatim), Domain Consolidation Map, Target Architecture, phase-by-phase (deep tier), Modernization Roadmap, Business Value cards, Risk Register summary |
| 4 | Partnership, Methodology & Next Steps | framework methodology + AI-framework-value + Traditional-vs-AI table (each row labelled engagement-actual vs framework-reference), optional track record, single CTA |

Part 3 must open with this exact text:
> *"The following sections present our recommended modernization approach. This architecture and roadmap is our professional recommendation based on the code-level discovery findings. Final architecture decisions should be made collaboratively with the client development team in a follow-on Architecture & Scoping engagement."*

---

## 5. Dual-audience information architecture

Business framing is the default surface; technical depth is one interaction away.

- **Finding card** — the headline unit for Critical/High findings. Layers: severity badge + ID + evidence/confidence badge → business-language title → **Business impact** (CTO layer) → collapsible **"For the engineer"** `<details>` block containing Rule-7 claim isolation ("what the code shows" / "what this implies"), `file:line` (or `{repo}/file:line`) citations, and `[MUST VERIFY]`/`[SHOULD VERIFY]` tags. Prints expanded.
- **Full registers stay complete and Ctrl+F-able.** The Risk Register / Endpoint Registry / Connection Map / Duplicate & Domain tables remain full tables below the cards. Every row keeps its stable ID and an evidence-status badge (per Discovery PRD § 6.4). Low/Informational findings live only in the tables, never as cards (severity gets visual weight).
- **Diagrams carry two captions:** a business caption ("what this means") and a technical note ("node/edge counts, protocols, source file").

---

## 6. Design system

The complete visual language is the design-token block inlined at the top of `Master_Report_Template.html`. Highlights that are **mandatory** for both scopes:

- **No magic numbers:** every numeric code visible to the customer carries its meaning at the point of use — scale scores render with their word (Healthy / Needs Attention / Critical; "2 · Moderate concern"), never a bare digit; a legend accompanies any dotted/coded visual.

- **Shell:** 248px sticky left sidebar + fluid `.main` (max-width 980px). Sidebar collapses to a top strip below 768px.
- **Fonts:** system stack `'Segoe UI', system-ui, -apple-system, sans-serif` (mono `'Cascadia Code','Consolas',monospace`). **No Google Fonts** — guarantees identical offline/print rendering.
- **One severity palette, one evidence palette, one confidence-tier palette, one RAG palette** — all CVD-validated (replaces the current template's three parallel tier palettes and three severity palettes).
- **One base table** (`.data-table` + `.compact` modifier) — replaces the four near-duplicate table styles.
- **Canonical accent orange `#E8640A`** (resolves the `#E8640A` vs `#EF7D00` vs `#F5883F` divergence across the framework).
- **Mermaid:** `theme: 'neutral', securityLevel: 'strict'`, `startOnLoad: true`, loaded in a try/catch so source stays visible if the CDN is blocked.

### 6.1 Navigation
- Sidebar TOC with grouped links and a per-section confidence heatmap.
- **Active-section highlight** via a single dependency-free `IntersectionObserver` scroll-spy (the only JS beyond Mermaid; guarded in try/catch).
- CSS smooth-scroll + `scroll-margin-top`.

### 6.2 Print
Shared `@media print`: hide sidebar, full-width main, force chart colors (`print-color-adjust: exact`), `page-break-inside: avoid` on cards/rows/diagrams, `<details>` render expanded.

### 6.3 Responsive
Tested at 1440px, 1024px (padding tightens, two-col grids relax), and 768px (sidebar → top strip, callouts and verdict stack, KPI/scorecard grids reflow via `auto-fit minmax()`).

---

## 7. Confidence model (unified)

### 7.1 Two formulas, one presentation
- **`report_scope: application`** uses the per-app ECI (canonical `Discovery_PRD.md` § 4.5): `ECI = 0.50 × Verification Rate + 0.35 × Critical Verification Rate + 0.15 × Coverage`.
- **`report_scope: portfolio`** uses the **revised** Portfolio ECI (see `Portfolio_ECI_Validation.md`): `Portfolio ECI = 0.30 × Cross-Verification Rate + 0.30 × Critical Cross-Verification Rate + 0.25 × Discovery Confidence + 0.15 × Coverage`.

Both share the tier bands (Very High 90-100 / High 70-89 / Medium 50-69 / Low 30-49 / Very Low 0-29), ±10-point precision, and the "< 5 scoreable findings → tier label only" rule. Both keep a **Critical-verification term** so a single unverified Critical/High finding pulls the section down ~2 tiers — the guarantee the whole ECI system exists to provide.

### 7.2 Evidence labels
The report renders the per-app labels (Verified / Partial / Assumed / Inferred / Cannot Determine) and, for portfolio scope, the cross-repo labels (`[Cross-verified]` > `[Code-verified]` > `[Discovery-sourced, orig. <status>]`). `[Discovery-sourced]` **always carries its inherited status** so evidence quality is never lost.

### 7.3 Translation (mandatory)
Every confidence score keeps its ECI percentage + tier **and** gains a one-line plain-language consequence beside it (e.g. *"High — 78%. Most critical findings are code-verified; the shared-database topology still needs DBA confirmation."*). A reader must never see a bare "78% Medium". The hero front-loads the single overall-confidence number so the reader is not dependent on scrolling to the "About Confidence" card. That card stays (static methodology text), unmodified.

### 7.4 Confidence floor
If overall confidence < 40%, show the preliminary-assessment banner and neutral verdict styling (unchanged behavior from both prompts).

---

## 8. Chart integrity

Every visual (KPI strip, severity bar, risk matrix, meters, evidence distribution, gauges, scorecards, debt bars) is a **projection of a number that exists elsewhere** in the report or logs — never a standalone estimate. If the underlying number does not exist, the visual is removed, not invented. The self-verification check (VC-02 in both prompts) cross-checks every chart figure against its source. The "Traditional vs AI" table labels every row as **engagement-actual** or **framework-reference range** so it reads as evidence, not marketing.

---

## 9. Metadata header

Both `.md` and `.html` twins carry:

```yaml
report_scope: "{application|portfolio}"
report_id: "{PREFIX}-DISC-{YYYY}-{MM}"        # or {PREFIX}-PORT-{YYYY}-{MM}
subject_name: "{application or portfolio name}"
client_name: "{client or 'TO FILL — consultant'}"
consultant_name: "{consultant/firm or 'TO FILL — consultant'}"
organization_label: "{sidebar brand label}"
report_date: "{YYYY-MM-DD}"
ai_hours: "{N} hrs (configured)"
overall_confidence: "{NN}% - {Tier}"
recommendation: "{Remediate|Hybrid|Full Modernization}   # application
                 |Targeted Remediation|API Platform Modernization|Full API Platform Rebuild}"  # portfolio
decision_score: "{N}/21"
report_version: "1.0"
```

---

## 10. Fill rules (what the master prompts must honour)

1. Set `data-scope` on `<body>`; keep the matching scope block, delete the other.
2. Fill every KPI/scorecard/meter/gauge from a computed count; **remove any tile you cannot back** — never estimate (chart integrity, § 8).
3. Position the decision gauge marker: `left = (score − 7) / 14 × 100%`, clamped 2%–98%.
4. Render Critical/High findings as finding cards; keep all findings (incl. Low/Informational) in the full register table.
5. Fill each section's confidence badge with ECI % + tier + the plain-language consequence line (§ 7.3). Sections without independent scores (Engagement Overview, Next Steps) carry no badge.
6. Put Mermaid source in `<pre class="mermaid">` inside a `.diagram-card`; add both captions (§ 5).
7. No placeholder text may remain except intentional `[TO FILL — consultant]` markers.
8. Never invent client/consultant names, CVE IDs, CVSS scores, "latest version" claims, or cost/effort/timeline figures.

---

## 11. Relationship to existing documents

- **Supersedes:** `Discovery_Master_Prompt.md` § 7.3 (template-fill instructions), `CrossRepo_Consolidation_Master_Prompt.md` § 7.2 (HTML-from-scratch), and `Resources/Discovery_Report_Template.html` (replaced by `Unified_Report_Template.html`).
- **Inherits from:** `Discovery_PRD.md` § 4 (per-app ECI) and § 7.8 (CVD palette, chart integrity, value-first visuals).
- **Depends on:** `Backlog/Portfolio_ECI_Validation.md` (portfolio formula — pending application to the Cross-Repo prompt) and the token block inlined in `Master_Report_Template.html` (visual language).
- **Does not change:** file-naming conventions (`MASTER_DISCOVERY_REPORT.html`, `MASTER_CONSOLIDATED_REPORT.html`), evidence discipline rules, or the phased execution of either master prompt.
