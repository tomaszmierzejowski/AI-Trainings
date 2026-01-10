## Shared Folder Structure (Reusable)

Use this as the base for all clients. Keep English-first; add Polish examples where it boosts adoption.

```
training/
  shared/                         # Reusable templates and base assets
    survey.md                     # Pre-training survey (questions only)
    agendas.md                    # 1/2/3-day reusable agendas
    labs.md                       # Reusable hands-on labs
    adaptation-guide.md           # How to tailor using survey answers
    modules/                      # Per-module outlines/notes/scripts (reusable)
      ai-fundamentals.md
      prompting-power.md
      cursor-chatgpt-perplexity.md
      governance-safety.md
      pega-workflow-ai.md         # Generic pattern; clone per client
      productivity-recipes.md
      builder-tools.md
    assets/                       # Logos, placeholder data, screenshots
      readme.md
    templates/                    # Slide + doc templates
      slide-outline-template.pptx (placeholder)
      audiobook-script-template.md
      lab-template.md
  pega-poland/                    # Client-specific copy
    survey.md                     # Same questions + optional localized notes
    agendas.md                    # Pega-Poland tuned timing/examples
    labs.md                       # Labs tuned to Pega workflows
    adaptation-notes.md           # What changed vs shared
    modules/                      # Pega-Poland specific scripts/notes
      pega-workflow-ai.md
      pega-productivity.md
      pega-builder-demos.md
    assets/                       # Safe sample data/screens
      fictional-datasets.md
    delivery-notes.md             # Room/remote setup, links, accounts
```

Usage:
- Copy `training/shared` as a baseline for new clients; rename subfolder (e.g., `training/pega-<client>/`).
- Keep `shared` untouched to preserve templates; only extend/override in client folders.
- Store any real data outside this tree; use fictional or scrubbed samples only.
