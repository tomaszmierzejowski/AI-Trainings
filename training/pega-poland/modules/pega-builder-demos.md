## Builder Demos (MagicUI/Lovable with Pega)

### Slides
- Slide 1 — Use Case (Polish: Przypadek)  
  - Intake + review screens for claims/onboarding/service (fictional).  
  - Speaker notes: Explain demo scope and constraints.

- Slide 2 — Prompt Template (Polish: Szablon promptu)  
  - Fields, validation, sample fictional values, layout hints.  
  - Optional Polish labels for user-facing text.  
  - Speaker notes: Show a concise example prompt.

- Slide 3 — Flow (Polish: Przebieg)  
  - Generate UI mock → review → map to Pega views/sections.  
  - Speaker notes: Stress that mapping is manual/verified in App Studio.

- Slide 4 — Safety & Quality (Polish: Bezpieczeństwo)  
  - No real data; check accessibility; align to Pega UX and branding.  
  - Validate required fields, masks, error states.  
  - Speaker notes: Note any client design system constraints.

- Slide 5 — Handoff to Pega (Polish: Przekazanie)  
  - Document mapping notes; rebuild in App Studio; log prompts.  
  - Reusable prompts: intake, review, approvals.  
  - Speaker notes: Keep artifacts in repo for traceability.

### Audiobook Script (4–5 min + Q&A)
"For builder demos we keep it fast and safe. Use MagicUI or Lovable to generate intake and review screens from a concise prompt: fields, validation rules, layout hints, and fictional sample values. Add Polish labels only where users see text; keep system text in English.  
Generate the mock, review it for accessibility and security, and then map it to Pega views or sections in App Studio—Pega remains the governed build. Capture mapping notes and prompts so others can reuse them. This keeps demos quick while respecting design and compliance."  

Likely Q&A:
- Q: Can we reuse the generated code?  
  A: Treat it as a reference; rebuild or verify in Pega/App Studio under governance.  
- Q: How much Polish localization?  
  A: Add Polish where user-facing; keep specs/logic English to stay consistent.  
- Q: What checks before showing to a client?  
  A: Verify no real data, accessibility basics (labels, contrast), and alignment with client branding; log prompts.  
