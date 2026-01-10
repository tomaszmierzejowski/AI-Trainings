## Builder Tools (MagicUI.ai / Lovable)

### Slides
- Slide 1 — Purpose (Polish: Cel)  
  - Rapid UI/app scaffolding for drafts; production still in Pega/App Studio.  
  - Speaker notes: Set expectation—this is a first-draft accelerator.

- Slide 2 — Inputs that Matter (Polish: Wejścia)  
  - Fields, types, validation rules, layout hints, sample fictional values.  
  - Keep it short; include role/persona if relevant.  
  - Speaker notes: Show a concise prompt example for an intake form.

- Slide 3 — Demo Flow (Polish: Przebieg demo)  
  - Paste spec → generate UI → export screenshot/spec → review → harden in Pega.  
  - Speaker notes: Emphasize review before reuse.

- Slide 4 — Safety & Quality (Polish: Bezpieczeństwo)  
  - No real data; check accessibility; align to design system.  
  - Validate required fields, masks, and error states.  
  - Speaker notes: Mention security review for any generated code.

- Slide 5 — Pega Mapping (Polish: Mapowanie do Pega)  
  - Map mock to views/sections; note what to rebuild; keep governance.  
  - Reusable prompts: intake, review, approval screens.  
  - Speaker notes: Keep mapping notes in the repo for traceability.

### Audiobook Script (5–6 min + Q&A)
"Builder tools like MagicUI and Lovable turn a short spec into a UI mock fast. Provide clear inputs: fields, types, validation rules, layout hints, and fictional sample values. Generate, export, and review for accessibility and security. Then map the mock to Pega views or sections in App Studio—Pega remains the governed system of record.  
Keep a small library of prompts for common screens like intake, review, and approvals so teams can reuse them. Always inspect generated code or specs for alignment with your design system and for any hidden data. These tools shorten iteration loops without replacing governed delivery."  

Likely Q&A:
- Q: Can we ship the generated UI directly?  
  A: No—treat it as a draft; rebuild or verify in Pega/App Studio under governance.  
- Q: How detailed should the prompt be?  
  A: Include fields, types, validation, layout hints, and sample fictional data—keep it concise.  
- Q: What about accessibility?  
  A: Check labels, focus order, contrast, and error messaging during review before mapping to Pega.  
