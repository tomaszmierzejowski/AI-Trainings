# Discovery Resources

Core system files that drive the AI-assisted **single-repository** discovery framework. These are read-only — the AI agent reads from here but never writes here.

## Per-Application Discovery

- **Discovery_Master_Prompt.md** — The prompt pasted into a capable, workspace-aware AI coding assistant to execute the legacy application discovery against `Project/Code/`
- **Discovery_PRD.md** — Product Requirements Document detailing the methodology, confidence scoring, and design decisions
- **Discovery_Report_Template.html** — HTML template for the customer-facing discovery report, filled by the AI during Phase 4 and written to `Outputs/FinalReport/MASTER_DISCOVERY_REPORT.html`

## Multi-repository (portfolio) discovery

Cross-repository consolidation — combining N completed single-repo discoveries into one master report — lives in its own repository: **`app-modernization-master-template`** (contains `CrossRepo_Consolidation_Master_Prompt.md`, `Master_Report_Template.html` + its PRD, and `Report_UX_Review_Prompt.md`). Completed clones of *this* repository are its inputs. See the "Master (Multi-Repo) Discovery" section of [`Team_Discovery_Process_Guide.html`](../Team_Discovery_Process_Guide.html) for the team process.
