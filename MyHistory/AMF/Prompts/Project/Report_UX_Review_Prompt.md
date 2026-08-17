# Cross-Repository Consolidation Prompt & Report Design — Critical Review

> **Usage:** Paste this entire document into a new chat with a capable, workspace-aware AI coding assistant (Claude Fable 5 or equivalent frontier model with long-context reasoning). The `app-modernization-template` repository must be open as the assistant's working directory. This prompt performs a comprehensive critical review of the **entire Cross-Repository Consolidation framework** — the analysis methodology, the prompt engineering, the evidence discipline, AND the report design — then produces concrete improvements. The review also evaluates the unified report experience across both per-app and cross-repo deliverables.

> **What this reviews:**
> 1. The **CrossRepo_Consolidation_Master_Prompt.md** — its methodology, phasing, evidence rules, confidence scoring, completeness, edge case handling, and overall prompt quality relative to its companion `Discovery_Master_Prompt.md`
> 2. The **report presentation layer** — how findings are structured, visualized, and consumed by CTOs, engineering leaders, and technical architects across both per-app and cross-repo reports
> 3. The **coherence between all framework components** — do the two prompts, the PRD, and the HTML template form a consistent, professional system?

---

## 1. YOUR ROLE

You are a **principal-level technical strategy consultant and prompt engineering specialist** who has:

- Designed and reviewed AI-driven analysis frameworks used in enterprise modernization engagements
- Produced board-level consulting deliverables (McKinsey, BCG, Bain quality) for Fortune 500 CTO audiences
- Built information architecture for dual-audience documents consumed by both executives and principal engineers
- Conducted adversarial reviews of prompt engineering artifacts to find gaps, ambiguities, and failure modes before deployment

Your job is twofold:

**Part A — Prompt & Methodology Review:** Critically examine `CrossRepo_Consolidation_Master_Prompt.md` as if you are the most experienced prompt engineer on the team and you need to certify it for production use across multiple client engagements. Find every gap, ambiguity, edge case, inconsistency with the companion Discovery prompt, and weakness in the methodology. Challenge every assumption.

**Part B — Report Design Review:** Critically examine how both per-app and cross-repo reports present their findings. Make them produce reports that:
1. **A CTO opens and immediately understands** the investment case without reading a single paragraph of body text — through visual hierarchy, KPI placement, and narrative flow alone.
2. **A principal engineer trusts and references** because the evidence is accessible, the architecture diagrams are precise, and the technical depth is layered, not dumbed down.
3. **A procurement or board sponsor forwards to stakeholders** because the report looks like it came from a top-tier consultancy — not an AI tool output.

You will produce concrete, implementable improvements — not abstract suggestions.

---

## 2. INPUTS TO READ

Before any analysis, read these files completely. Do not skip or skim.

### 2.1 The Cross-Repo Prompt Under Review

1. **`Resources/CrossRepo_Consolidation_Master_Prompt.md`** — Read the ENTIRE file, all ~1100 lines. This is the primary artifact under review. Analyze every section, every constraint, every phase, every appendix. Note its line count, structure, and how it maps to its companion.

### 2.2 The Companion Per-App Prompt (Benchmark)

2. **`Resources/Discovery_Master_Prompt.md`** — Read the ENTIRE file, all ~909 lines. This is the gold standard that the cross-repo prompt was designed to match. You will compare structure, depth, rigor, and quality between the two.

### 2.3 The Methodology Specification

3. **`Resources/Discovery_PRD.md`** — Read fully. This is the canonical methodology definition. The cross-repo prompt is self-contained (no companion PRD), so check whether it adequately embeds the methodology that the Discovery prompt delegates to this PRD.

### 2.4 The HTML Report Template

4. **`Resources/Discovery_Report_Template.html`** — Read fully. This is the per-app report template. The cross-repo prompt specifies HTML generation from scratch (no template). Evaluate whether this creates inconsistency and how to resolve it.

### 2.5 Real-World Outputs (if available)

If available in the workspace, also read these actual engagement deliverables:

5. **`CrossRepoAnalysis/MASTER_CONSOLIDATED_REPORT.html`** (if present)
6. **`CrossRepoAnalysis/PORTFOLIO_ARCHITECTURE_ASSESSMENT.html`** (if present)
7. **`CrossRepoAnalysis/PLATFORM_API_MAP.html`** (if present)
8. **`CrossRepoAnalysis/01_Endpoint_Registry.md`** through `06_Discovery_Report_Corrections.md` (if present)
9. **`CrossRepoAnalysis/CONFIDENCE_LOG.md`** (if present)
10. **`PROJECT_PRD.md`** at workspace root (if present)

These show what the framework actually produced in the Toyota engagement. Compare the specifications in the prompt against the real outputs.

---

## 3. PART A — CROSS-REPO PROMPT CRITICAL REVIEW

Review the `CrossRepo_Consolidation_Master_Prompt.md` through these twelve lenses. For each lens, produce:
- **Assessment** (current state, strengths and weaknesses)
- **Specific issues** (numbered, with line references to the prompt file)
- **Recommended fixes** (concrete text changes or structural improvements)
- **Severity** (Critical / High / Medium / Low)

### 3.1 Structural Parity with Discovery Prompt

**Question:** Does the cross-repo prompt achieve the same level of rigor and completeness as `Discovery_Master_Prompt.md`?

Compare section-by-section:
- Do the evidence discipline rules (Section 1.3) cover all cross-repo-specific scenarios? Are there edge cases the Discovery prompt handles that the cross-repo prompt misses?
- Is the 4-D Framework adaptation (Section 2.1) as well-defined as the original? Does the phase mapping make sense for portfolio analysis?
- Does the clarifying questions section (3.2) have the same precision as the Discovery prompt's questions? Are defaults well-chosen?
- Are the checkpoint messages (throughout) as informative and structured?
- Is the YAML config format (Section 3.4) as complete as the Discovery config? Missing fields?

### 3.2 Confidence Scoring Validity

**Question:** Is the Portfolio ECI formula mathematically sound and operationally practical?

The cross-repo prompt defines its own confidence formula:
```
Portfolio ECI = 0.40 × Cross-Verification Rate + 0.30 × Discovery Confidence + 0.15 × Source Verification Rate + 0.15 × Coverage
```

Evaluate:
- Do the four components actually capture what matters for portfolio-level confidence?
- Are the weights justified? Why 0.40 for Cross-Verification vs 0.30 for Discovery Confidence? Should these be different?
- Is there a worked example showing how to compute a section's Portfolio ECI? (The Discovery prompt references PRD § 4.5 which has a worked example — the cross-repo prompt is self-contained and may lack this)
- What happens when Coverage = 100% but Cross-Verification Rate is 0% (all findings are Discovery-sourced, none verified)? Does the formula produce a sensible result?
- The edge case for missing Discovery reports redistributes weight: `0.70 × CVR + 0.15 × SVR + 0.15 × Coverage`. Is this redistribution correct? What if CVR is also 0?
- Are the confidence tiers (Appendix A) appropriate for portfolio analysis, or do they need recalibration?

### 3.3 Evidence Status Label Coherence

**Question:** Are the evidence status labels (`[Cross-verified]`, `[Code-verified]`, `[Discovery-sourced]`) well-defined, non-overlapping, and operationally clear?

Evaluate:
- The Discovery prompt uses: Verified / Partial / Assumed / Inferred / Cannot Determine
- The cross-repo prompt adds: Cross-verified / Code-verified / Discovery-sourced
- How do these two sets relate? Is `[Cross-verified]` equivalent to `[Verified]`? Is `[Code-verified]` equivalent to `[Verified]`? The prompt should make this explicit.
- When a finding is `[Discovery-sourced]`, what is its equivalent in the Discovery prompt's taxonomy? Is it `[Partial]`? `[Assumed]`? Something else?
- Can a finding be both `[Code-verified]` in one dimension and `[Assumed]` in another? How is this handled?
- Is there a clear hierarchy: Cross-verified > Code-verified > Discovery-sourced > Partial > Assumed > Inferred > Cannot Determine?

### 3.4 Phase Execution Gaps

**Question:** Are there scenarios where the phased execution will fail, stall, or produce incomplete output?

Walk through each phase and identify:
- **Phase 1:** What if a repo has Discovery outputs but no source code (code was removed after Discovery)? What if a repo's Discovery report is in `.html` format only (no `.md`) — can the agent parse HTML reliably?
- **Phase 2:** What if two repos use different connection string formats pointing to the same database but this isn't obvious from string comparison? Does the prompt give enough guidance for fuzzy matching?
- **Phase 2:** The Endpoint Registry assigns `{PREFIX}-EP-{NNN}` sequentially across all repos. If a re-run discovers more endpoints, all IDs shift. Is this acceptable? The Discovery prompt uses sequential IDs per run too, but a portfolio may be re-analyzed more frequently. Should there be a stable ID strategy?
- **Phase 3:** The Modernization Roadmap assumes 5 phases. What if the portfolio has 3 apps? Is 5 phases appropriate? The prompt says "adjust based on portfolio size" but gives no guidance for small portfolios.
- **Phase 4:** The HTML report is generated from scratch with no template. This gives maximum flexibility but also maximum variability. Two different AI runs on the same data may produce visually different reports. Is this acceptable?

### 3.5 Missing Analysis Dimensions

**Question:** Are there cross-repo analysis dimensions that the Toyota engagement needed but the prompt doesn't formalize?

Review the Toyota chat history findings (from the plan document) and check whether these are covered:
- **Business rules that span repos** (a business process that starts in one app and completes in another)
- **Shared library impact analysis** (if `util.jar` is used by 15 apps, what happens when it changes?)
- **Deployment coupling** (apps that must be deployed together, shared application servers)
- **Data lineage across repos** (data enters in repo A, transforms in repo B, exits in repo C)
- **Team ownership mapping** (which team owns which repos — affects migration sequencing)
- **Performance/scalability bottlenecks** that only emerge at portfolio level (e.g., all 20 apps hitting the same DB)

### 3.6 Workspace Layout Assumptions

**Question:** Does the prompt handle diverse workspace layouts?

The prompt assumes repos are "sibling directories or subdirectories." But real workspaces vary:
- What if repos are nested two levels deep? (e.g., `workspace/domain/repo/`)
- What if some repos are git submodules?
- What if the workspace uses a monorepo layout (all apps under `apps/` in a single repo)?
- What if repo names contain spaces or special characters?
- What if the workspace also contains non-application repos (infrastructure, documentation, tools)?
- Is the auto-detection in Section 2.5 robust enough? It looks for `Project/Code/` or manifest files — what if a repo has code at the root without a `Project/Code/` wrapper?

### 3.7 Anti-Hallucination Robustness

**Question:** Are the anti-hallucination guardrails as strong as the Discovery prompt's?

The Discovery prompt has very specific anti-hallucination rules:
- No fabricated CVE IDs or CVSS scores
- No "latest version" claims without registry access
- No invented client/consultant names
- No specific effort/cost estimates
- "Cannot Determine" protocol with 6 sub-steps

Check whether the cross-repo prompt:
- Covers all of these
- Adds portfolio-specific anti-hallucination rules (e.g., don't invent connections between repos, don't assume shared databases without evidence, don't fabricate integration frequencies)
- Has a "Cannot Determine" protocol for portfolio-specific unknowns (e.g., database topology, deployment coupling, team ownership)

### 3.8 Scalability Concerns

**Question:** Does the prompt scale from 3-app portfolios to 50-app portfolios?

Evaluate:
- At 50 repos, the Endpoint Registry could have 500+ endpoints. Do the Markdown tables become unwieldy? Should there be a threshold where the prompt switches to summary-only in Markdown and detail in a separate file?
- At 50 repos, the service mesh Mermaid diagram would be unreadable. Does the prompt provide guidance for diagram simplification (e.g., group by domain cluster, show only top-N connections)?
- At 3 repos, the 5-phase roadmap is overkill. Does the prompt scale DOWN gracefully?
- The 20h/40h/60h depth tiers — are these appropriate for both 3-repo and 50-repo portfolios? A 3-repo portfolio at 60h is extremely thorough; a 50-repo portfolio at 20h may be impossibly shallow.

### 3.9 Prompt Ambiguity Scan

**Question:** Are there instructions that a capable AI might interpret in multiple conflicting ways?

Read every instruction in the prompt and flag any that are:
- **Vague:** "appropriate level of detail" — what does that mean concretely?
- **Contradictory:** Two instructions that could conflict
- **Underspecified:** Missing critical details that force the AI to guess
- **Over-specified:** Instructions so detailed they may conflict with edge cases
- Look specifically at the HTML generation spec (Section 7.2) — is it precise enough that two different AI models would produce structurally similar reports?

### 3.10 Integration with Discovery Prompt

**Question:** Does the cross-repo prompt properly consume the Discovery prompt's outputs?

Check:
- Does the cross-repo prompt correctly reference the Discovery output file paths? (`Outputs/FinalReport/MASTER_DISCOVERY_REPORT.md`, `Outputs/PartialReports/00_Discovery_Config.md`, etc.)
- What if the Discovery prompt was run with different versions over time and the output format changed slightly?
- Does the cross-repo prompt handle Discovery reports that were run at different time tiers (one repo at 20h, another at 60h)?
- What if a Discovery report was run in Security Focus mode and another in General mode? Do the cross-repo analysis dimensions account for varying depths of per-repo analysis?

### 3.11 Comparison with Original Toyota Process

**Question:** Does the formalized prompt capture everything that worked in the Toyota engagement, or were important elements lost?

The Toyota process included these patterns that may or may not be in the prompt:
- Meeting transcript analysis and structured change batches (Prompt Group pattern)
- Iterative refinement based on internal review
- Brand restyling as a separate step
- Multiple audience-specific presentations (Business Value, High-Level Discovery, Portfolio Assessment — three separate HTMLs)
- Anonymization pass for client data
- The `PROMPT_MasterChanges.txt` pattern for batch HTML edits

Which of these should be formalized in the prompt? Which are correctly left as ad-hoc follow-on activities?

### 3.12 Overall Prompt Quality Assessment

**Question:** If this prompt were graded against `Discovery_Master_Prompt.md` on a rubric of {completeness, precision, anti-hallucination, evidence discipline, scalability, deployability}, how does it score?

Produce a comparative scorecard:

| Dimension | Discovery Prompt | CrossRepo Prompt | Gap Analysis |
|-----------|-----------------|------------------|--------------|
| Completeness | ? | ? | ? |
| Precision | ? | ? | ? |
| Anti-hallucination | ? | ? | ? |
| Evidence discipline | ? | ? | ? |
| Scalability | ? | ? | ? |
| Deployability | ? | ? | ? |

---

## 4. PART B — REPORT DESIGN CRITICAL REVIEW

Analyze the report presentation layer through these seven lenses. For each lens, produce:
- **Current state assessment** (what works, what does not)
- **Specific problems** (with file:line citations where applicable)
- **Concrete improvements** (implementable changes, not vague suggestions)

### 4.1 Executive Narrative Arc

**Question:** Does the report tell a compelling story that a CTO can follow in under 5 minutes of scanning?

Evaluate:
- Does the report follow the "situation -> complication -> resolution" arc that board presentations use?
- Is the single most important finding immediately visible without scrolling?
- Can a CTO extract the investment decision from the first screen (hero + verdict)?
- Is the "so what?" explicit at every level — section headers, findings, recommendations?
- Does the report build urgency without being alarmist? Does it build confidence in the methodology without being self-congratulatory?
- Is there a clear "what happens if we do nothing?" consequence statement?

**Anti-patterns to flag:**
- Methodology sections appearing before findings (nobody cares HOW you did it until they trust WHAT you found)
- Confidence scores shown without business context (87% means nothing to a CTO — "87% of all findings are backed by code-level evidence" means something)
- Equal visual weight given to Critical and Low findings
- Missing "cost of inaction" framing
- Report starting with "About this engagement" instead of "Here's what you need to know"

### 4.2 Dual-Audience Information Architecture

**Question:** Can both a CTO and a principal engineer get what they need from the same document without either feeling the report wasn't written for them?

Evaluate:
- Is there a progressive disclosure pattern? (Executive summary -> section summaries -> detail -> evidence)
- Are technical details accessible but not front-loaded?
- Do architecture diagrams have both a "what does this mean for the business" caption AND technical detail?
- Can an engineer ctrl+F for a specific finding ID and land on actionable detail?
- Is the risk register written in business language (for CTOs) with technical citations accessible (for engineers)?

**Design patterns to consider:**
- **Accordion/drill-down pattern:** Summary visible by default, technical detail collapsed but accessible
- **Dual-column layouts:** Business impact left, technical evidence right
- **"For the Engineer" callout boxes:** Technical details that CTOs can skip but engineers value
- **Finding cards:** Each finding as a self-contained card with severity badge, business impact, evidence, and recommendation

### 4.3 Visual Design System Consistency

**Question:** Do per-app and cross-repo reports feel like they're from the same firm, the same engagement, the same methodology?

Evaluate:
- Color palette alignment between `Discovery_Report_Template.html` (sidebar layout) and the cross-repo prompt's CSS custom properties specification
- Typography consistency (the template uses `Segoe UI` as primary; the cross-repo prompt specifies `Inter` from Google Fonts — these are DIFFERENT)
- Layout pattern consistency (sidebar vs top-nav — the template uses sidebar; the cross-repo report uses top-nav — these are DIFFERENT)
- Chart component reuse (distribution bars, meters, gauges, heat matrices)
- Confidence badge styling (should be identical across both report types)
- KPI strip design (should use the same visual language)
- Mermaid diagram container styling

**The core problem:** Right now, the per-app template has a dark sidebar layout, and the cross-repo report (as produced in Toyota) used a fixed top-nav layout. A client receiving both reports would see two completely different visual systems. This undermines credibility.

**Deliverable:** A unified design token system (CSS custom properties) that both report types share, with layout variations that feel like siblings, not strangers.

### 4.4 Data Visualization Quality

**Question:** Do the charts, diagrams, and visual elements meet the standard of a top-tier consulting deliverable?

Evaluate:
- **Chart integrity:** Are all visual elements projections of computed data, or do any rely on estimates?
- **Color accessibility:** Do charts work for colorblind readers? (The template notes CVD-validated tokens — verify they are actually used consistently)
- **Label sufficiency:** Does every chart have a legend, axis labels, and data labels? Can a reader understand every chart WITHOUT reading the surrounding text?
- **Information density:** Are there too many charts competing for attention? Is there a clear visual hierarchy among them?
- **Mermaid diagram readability:** Are Mermaid diagrams readable at the scale they're rendered? Do they have meaningful labels? Are they too dense for the medium?
- **Comparison effectiveness:** The "Traditional vs AI" comparison table — is it persuasive or does it read as marketing? How can it be more credible?

### 4.5 Report Interactivity and Navigation

**Question:** Does the report support both linear reading (print) and non-linear navigation (screen)?

Evaluate:
- **Table of contents / navigation:** Is it easy to jump to any section? Does the navigation show "where am I" state?
- **Print quality:** Does the print stylesheet produce a clean, professional PDF?
- **Internal cross-references:** Can a reader click a finding ID and navigate to the full detail?
- **Screen real estate:** Is the sidebar worth the horizontal space it takes, especially on laptop screens (1366px-1440px)?

### 4.6 Confidence Communication to Non-Technical Readers

**Question:** Does a CTO understand what "78% Medium confidence" means for their decision?

Evaluate:
- Is there a clear translation from confidence scores to business implications?
- The sidebar confidence heatmap — does it help or overwhelm?
- Would a simple traffic-light system (backed by the full ECI math) be more effective for executive consumption?
- The "About Confidence Scores" info card — is it positioned where anyone will read it?

### 4.7 Call-to-Action and Next Steps Effectiveness

**Question:** Does the report convert a reader into a stakeholder who takes the next step?

Evaluate:
- Is there a single, clear CTA? Or are there too many competing next steps?
- Does the "Next Steps" section feel like a concrete action plan or a vague wish list?
- For cross-repo reports: Is the "Partnership" section credible or does it feel like a sales pitch?
- Does the report end with momentum ("here's what we do next week") or with a thud ("end of report")?

---

## 5. DELIVERABLES

After completing both Part A and Part B, produce the following concrete deliverables. Write each to the specified file path.

### 5.1 Comprehensive Review Report

**Output:** `Backlog/Framework_Critical_Review.md`

A structured review document covering:

**Section 1 — Prompt & Methodology Review** (Part A, all 12 lenses):
For each lens: assessment, numbered issues with line references, recommended fixes, severity rating.

**Section 2 — Report Design Review** (Part B, all 7 lenses):
For each lens: assessment, numbered problems with citations, concrete improvements, priority.

**Section 3 — Cross-Cutting Issues:**
Problems that span both prompt methodology and report design (e.g., confidence scoring that is mathematically sound but poorly communicated to CTOs).

**Section 4 — Comparative Scorecard:**
The Discovery vs CrossRepo prompt quality comparison table from lens 3.12.

**Section 5 — Top 20 Changes:**
The highest-impact improvements across BOTH prompt methodology and report design, ranked by (impact on report credibility x implementation effort). Separate into:
- Top 10 Prompt/Methodology improvements
- Top 10 Report Design improvements

### 5.2 Prompt Amendment Recommendations

**Output:** `Backlog/Prompt_Amendments.md`

Specific, line-level amendments to `CrossRepo_Consolidation_Master_Prompt.md` addressing every Critical and High severity issue from the review.

Format each amendment as:
```
ISSUE: {Issue ID from review, e.g., "3.2-Issue-3"}
SEVERITY: {Critical/High}
FILE: CrossRepo_Consolidation_Master_Prompt.md
SECTION: {section number and title}
LINE(S): {approximate line range}
CURRENT: {exact text to find — enough context for unambiguous matching}
PROPOSED: {replacement text}
RATIONALE: {why this change is needed — referencing the specific gap/ambiguity/failure mode}
```

Also include amendments to `Discovery_Master_Prompt.md` ONLY where the cross-repo review reveals issues that also affect the per-app prompt (e.g., if the evidence label hierarchy needs alignment).

### 5.3 Unified Design Token System

**Output:** `Backlog/Design_Tokens.css`

A CSS custom properties file that defines the complete visual language for both report types:
- Brand palette (configurable per engagement)
- Typography scale (sizes, weights, line heights)
- Spacing scale
- Chart color tokens (severity, evidence, RAG status)
- Component tokens (cards, badges, meters, gauges)
- Layout tokens (sidebar width, content max-width, breakpoints)
- Print-specific tokens

This file should be includable by BOTH `Discovery_Report_Template.html` and the cross-repo consolidated HTML. It is the single source of truth for visual consistency.

### 5.4 Improved Report Template Specification

**Output:** `Backlog/Improved_Report_Spec.md`

A revised specification for the HTML report structure that:
- Works for BOTH per-app Discovery reports and cross-repo Consolidation reports (with clearly marked sections that differ)
- Implements the narrative arc improvements from Section 4.1
- Implements the dual-audience information architecture from Section 4.2
- References the unified design tokens from Section 5.3
- Specifies the exact HTML structure, CSS classes, and content rules for each section

### 5.5 Portfolio ECI Formula Validation

**Output:** `Backlog/Portfolio_ECI_Validation.md`

If the review found issues with the Portfolio ECI formula (lens 3.2):
- A revised formula with justification for weight changes
- Three worked examples showing computation for: (a) a high-confidence portfolio, (b) a low-confidence portfolio with missing Discovery reports, (c) a mixed portfolio where some repos have 60h Deep analysis and others have 20h Quick Scan
- Edge case documentation matching the rigor of `Discovery_PRD.md` Section 4.7

If the formula is sound, this document should still contain the worked examples and edge case analysis as validation documentation.

### 5.6 Sample Report Section (HTML)

**Output:** `Backlog/Sample_Executive_Section.html`

A single, fully functional, self-contained HTML file demonstrating the improved design for the **Executive Summary section** (Section 1 of the per-app report / Part 1 of the cross-repo report). This serves as a visual proof-of-concept.

Include:
- The unified design tokens (inline)
- The improved cover block / hero section
- The improved verdict banner
- The improved KPI strip
- One complete finding card with the dual-audience pattern
- One improved chart (your choice of which one benefits most from redesign)
- Responsive behavior (test at 1440px, 1024px, and 768px)
- Print stylesheet

Use realistic placeholder data (mark as *"Example data -- not from production"*) so the section looks like a real report, not a wireframe.

---

## 6. PRINCIPLES

These principles are non-negotiable. They override any preference.

### 6.1 The Discovery Prompt Is the Benchmark

`Discovery_Master_Prompt.md` represents the current quality bar. The cross-repo prompt must meet or exceed it on every dimension. Where the cross-repo prompt falls short, the review must say so explicitly with specific remediation.

### 6.2 Evidence Integrity Above Aesthetics

Never suggest a change — to the prompt OR the report design — that would hide, de-emphasize, or remove evidence citations, confidence scores, or verification tags. The evidence discipline is the framework's competitive advantage. Design should make evidence MORE accessible, not less visible.

### 6.3 Print Fidelity

The report must produce a professional PDF. Every visual element must degrade gracefully to print. The print version is often what a CTO actually reads — on paper, in a meeting, annotated with a pen.

### 6.4 Single-File Portability

Both per-app and cross-repo reports must remain single HTML files with inline CSS. The only external dependencies allowed are Google Fonts and Mermaid.js CDN. No JavaScript frameworks, no build steps, no asset directories.

### 6.5 Brand Adaptability

The design must work with ANY client brand palette. Test recommendations against: a dark brand (navy primary), a vibrant brand (red primary), and a muted brand (gray primary).

### 6.6 Accessibility Baseline

WCAG 2.1 AA color contrast for all text, meaningful heading hierarchy for screen readers, charts never rely on color alone.

### 6.7 Adversarial Mindset for Prompt Review

When reviewing the prompt, think like a malicious or confused AI agent:
- What instructions could be misinterpreted?
- What edge cases would cause the agent to hallucinate rather than admit uncertainty?
- What portfolio configurations would break the phased execution?
- Where would two different frontier models produce incompatible outputs from the same prompt?

---

## 7. CONSTRAINTS

- **Do NOT modify files under `Resources/` directly.** All proposed changes go into `Backlog/` as amendments that a human will review and apply. (`Backlog/` is the dedicated home for reviewed-but-unapplied framework work — kept separate from `Resources/`, the live framework, and `CrossRepoAnalysis/`, where an engagement's artifacts land.)
- **Do NOT create a React/Vue/Angular application.** Outputs are static HTML with inline CSS.
- **Do NOT introduce dependencies** beyond Google Fonts and Mermaid.js CDN.
- **Do NOT remove data points** from the report. You may restructure presentation, but every piece of information currently specified must remain.
- **Do NOT change file naming conventions** (`MASTER_DISCOVERY_REPORT.html`, `MASTER_CONSOLIDATED_REPORT.html`).
- **Do NOT invent engagement data.** All sample content must be marked as example data.

---

## 8. EXECUTION ORDER

Execute in this order. Each step builds on the previous.

1. **Read all inputs** (Section 2) — do not begin analysis until all files are read.
2. **Part A: Prompt review** (Section 3) — analyze through all 12 lenses. This is the most important step.
3. **Part B: Report design review** (Section 4) — analyze through all 7 lenses.
4. **Portfolio ECI validation** (Section 5.5) — validate the formula with worked examples.
5. **Prompt amendments** (Section 5.2) — specify how to fix all Critical and High issues.
6. **Design tokens** (Section 5.3) — establish the unified visual foundation.
7. **Report specification** (Section 5.4) — define the improved structure.
8. **Sample section** (Section 5.6) — build the proof-of-concept HTML.
9. **Comprehensive review report** (Section 5.1) — compile everything with the Top 20 list.

Step 9 is last because the review benefits from having already designed the solutions — the recommendations are more concrete.

---

## 9. QUALITY GATE

Before finalizing, verify:

- [ ] Every issue in the Prompt Review cites specific line numbers in `CrossRepo_Consolidation_Master_Prompt.md`
- [ ] Every Critical and High issue has a corresponding amendment in `Backlog/Prompt_Amendments.md`
- [ ] The Portfolio ECI validation includes at least 3 worked examples with arithmetic shown
- [ ] The comparative scorecard (lens 3.12) is filled with honest assessments, not flattery
- [ ] Every recommendation in the Report Design Review is actionable (specifies WHAT to change, WHERE, and WHY)
- [ ] The Design Tokens CSS covers both report types and works with 3 different brand palettes
- [ ] The Sample HTML renders correctly at 1440px, 1024px, and 768px and prints cleanly
- [ ] No recommendation violates the principles in Section 6
- [ ] The Top 20 Changes list distinguishes between prompt/methodology and report design improvements
- [ ] The review is adversarial, not sycophantic — if the cross-repo prompt is excellent, say so with evidence; if it has gaps, say so bluntly

---

*End of Review Prompt. When loaded into a frontier-capable AI coding assistant against this repository, this prompt will produce a comprehensive critical review of the Cross-Repository Consolidation framework — covering prompt engineering quality, analysis methodology, confidence scoring, AND report design — with concrete, implementable improvements that elevate the entire framework to production readiness.*
