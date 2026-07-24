# Three-Repo Delivery Pipeline — AI Modernization Discovery

> **Source:** Tomasz Mierzejowski's personal IP repositories
> **Last updated:** 2026-07-24

---

## Architecture Overview

The AI Modernization discovery methodology is implemented across three repositories, each handling a distinct stage of the delivery pipeline. The methodology IP (prompts, scoring formulas, report templates) is strictly separated from the automation mechanics.

```
Stage 1 (per-app)          Stage 2 (portfolio)         Automation
┌─────────────────┐       ┌─────────────────────┐     ┌────────────────────┐
│ app-modernization│       │ discovery-report-    │     │ discovery-         │
│ -template        │──────>│ template             │<────│ orchestrator       │
│                  │       │                      │     │                    │
│ 60h per repo     │       │ Consolidation        │     │ Runs Stage 1+2    │
│ Master Prompt    │       │ Master Report        │     │ unattended         │
│ Discovery PRD    │       │ Portfolio analysis   │     │ 20-60 repos        │
│ Report Template  │       │                      │     │ Quality gates      │
└─────────────────┘       └─────────────────────┘     └────────────────────┘
```

---

## Stage 1: `app-modernization-template`
<!-- [Source: Discovery_PRD.md v2.4] -->

**Purpose:** Per-application 60-hour discovery. One clone per application.

**Contents:**
- `Resources/Discovery_PRD.md` — The methodology specification (v2.4): Five Promises, 60-hour model, ECI scoring, coverage ledger, evidence labels
- `Resources/Discovery_Master_Prompt.md` — The execution prompt loaded into an AI coding assistant
- `Resources/Discovery_Report_Template.html` — Self-contained HTML report template
- `Project/Code/` — Where the customer's source code is placed (after secret removal)
- `Project/Documentation/` — Customer-provided docs (auto-detected by the prompt)
- `Project/SonarQubeReport/` — Optional tool scan results
- `Outputs/` — Generated report, evidence, confidence log, coverage ledger

**Workflow:**
1. Clone the template repository
2. Place sanitized source code in `Project/Code/`
3. Load the master prompt into an AI coding assistant (Cursor, Claude, etc.)
4. The prompt asks 3 clarifying questions (package, known context, engagement metadata)
5. AI runs the 40-hour analysis phase
6. Human consultant reviews and delivers

**Output:** A complete, customer-ready HTML report with quantified confidence scores, evidence citations, coverage ledger, risk register, architecture diagrams, and (for FULL package) an exhaustive business-rule catalog.

---

## Stage 2: `discovery-report-template`
<!-- [Source: Master_Report_PRD.md v1.1] -->

**Purpose:** Portfolio consolidation. Takes all Stage 1 per-app reports and produces a unified master report.

**When used:** Engagements covering multiple applications (e.g., 20 repositories in a single platform). Stage 2 starts only after all Stage 1 discoveries pass their quality gates.

**What it adds beyond Stage 1:**
- Cross-application dependency mapping (service mesh visualization)
- Portfolio-wide risk aggregation
- Domain consolidation maps
- Shared-library blast radius analysis
- Deployment coupling assessment
- Data lineage across the portfolio
- Phased modernization roadmap with business value cards

**Design constraint:** The consolidated report uses the same design system, confidence model, and evidence discipline as per-app reports. A customer receiving both sees one firm, not two.
<!-- [Source: Master_Report_PRD.md v1.1, §1] -->

---

## Automation: `discovery-orchestrator`
<!-- [Source: Orchestrator_PRD.md v1.0] -->

**Purpose:** Turns the two-stage methodology into a one-command, unattended, resumable pipeline.

**Problem it solves:** Running 20-60 individual discoveries by pasting prompts into AI sessions doesn't scale. The orchestrator automates the mechanical supervision while keeping the methodology IP separated from the automation.

### Key capabilities

| Capability | How it works |
|------------|-------------|
| **Declarative configuration** | One `engagement.yaml` file defines the entire run: repos, budgets, pre-answered questions, quality gates |
| **Auto-discovery** | Repositories auto-discovered from a parent folder; explicit entries only for overrides |
| **Parallel execution** | Stage 1 discoveries run in parallel (configurable concurrency), each in an isolated workspace |
| **Unattended operation** | Clarifying questions pre-answered via a runtime preamble; no human interaction during the run |
| **Programmatic quality gates** | Coverage ledger completeness, ECI sanity, artifact completeness, report integrity — all enforced by code, not model self-assessment |
| **Resume safety** | Every unit of work is independently resumable; re-running is always safe |
| **Cost controls** | Hard per-session budget caps, turn caps, wall-clock timeouts, per-engagement cost report |
| **Stage coordination** | Stage 2 starts only when every repo passes its Stage 1 gate |

### IP Separation
<!-- [Source: Orchestrator_PRD.md v1.0, §4] -->

The orchestrator contains **zero methodology IP**:
- No prompt text, scoring formulas, clarifying-question wording, or report templates
- Template repos are consumed read-only through a `KnowledgePack` interface
- The runner can be distributed to external teams without exposing the methodology know-how
- Replacing the local knowledge pack with a gateway-backed implementation requires zero pipeline changes

### Multi-Engine Support
<!-- [Source: Orchestrator_PRD.md v1.0, §5 FR-12/FR-13] -->

The execution engine is pluggable:

| Engine | Status | Notes |
|--------|--------|-------|
| Cursor | Default (Tomasz's primary) | Headless CLI wrapper |
| Claude (Agent SDK) | Supported | Full cost reporting and budget caps |
| Gemini | Supported | Headless CLI wrapper |
| Copilot | Supported | Headless CLI wrapper |
| Command | Supported | Arbitrary executable (future orchestrator seam) |

Engine failover: if the primary engine fails at session level, the orchestrator escalates to a fallback engine. A circuit breaker (3 primary session errors) routes all remaining sessions to the fallback automatically. Resume is engine-agnostic.

### Pipeline Flow

```
INTAKE --> STAGE-1 FAN-OUT --> PER-REPO GATE --> STAGE-2 CONSOLIDATION --> MASTER GATE --> BUNDLE
```

Unit state machine: `pending -> running -> gating -> done | failed`

Deliverables bundle: per-repo reports, master consolidated report, cost & status report.

---

## Evidence Labels Across the Pipeline

Every finding in every report (Stage 1 and Stage 2) carries an evidence label:

| Label | Meaning |
|-------|---------|
| **[Discovery-sourced]** | Found during AI-assisted codebase analysis |
| **[Code-verified]** | Confirmed by specific file:line citation in the source code |
| **[Cross-verified]** | Validated by multiple analysis passes or different AI models |
| **[Assumed]** | Inferred from patterns; flagged for human review |

The confidence scoring (ECI) uses these labels as inputs. Verified and Partial findings count toward the Verification Rate; only Verified findings count toward the Critical Verification Rate. This ensures that the most important findings (Critical/High severity) have the highest evidence bar.
