## Pega Workflow AI (Generic Pattern)

### Slides
- Slide 1 — Workflow Map (Polish: Mapa przepływu)  
  - Intake → triage → decision → action → feedback.  
  - Identify friction: slow routing, missing data, unclear notes.  
  - Speaker notes: Anchor every AI idea to a workflow step.

- Slide 2 — AI Touchpoints (Polish: Punkty AI)  
  - Classify, extract, summarize, route, recommend, draft.  
  - Keep outputs structured (JSON/table).  
  - Speaker notes: Stress bounded outputs; avoid free-form for routing/eligibility.

- Slide 3 — Process AI & Decisioning (Polish: Process AI i decyzje)  
  - Process AI: signals/predictions from history.  
  - Decisioning: NBA with constraints and arbitration.  
  - Speaker notes: Prediction = “how risky/valuable”; Decisioning = “what to do.”

- Slide 4 — Low-Code Accelerators (Polish: Low-code)  
  - App Studio case templates, data objects, personas.  
  - Quick stages; wire AI later.  
  - Speaker notes: Start with template, then attach Prediction/Decision strategies.

- Slide 5 — GenAI Connectors (Polish: GenAI)  
  - Draft emails, summarize interactions, suggest rules.  
  - Keep fictional data; enforce short formats.  
  - Speaker notes: Show example prompt for case summary with JSON output.

- Slide 6 — Example Flow (Polish: Przykład)  
  - Email intake → case type + routing → NBA offer → summary note.  
  - Feedback: log outcome to improve prompts/models.  
  - Speaker notes: Walk through end-to-end with 2 sample cases.

### Audiobook Script (7–8 min + Q&A)
"Think in steps: intake, triage, decision, action, feedback. Intake uses an LLM to classify and extract key fields. Triage applies a prediction to score urgency or value. Decisioning chooses the next best action with constraints. Action uses a GenAI connector to draft the email or case note. Feedback logs outcomes to improve prompts and models.  
Process AI is your prediction engine—great when you have historical signals. Real-time decisioning arbitrates what to do given constraints. GenAI handles the language tasks but stays bounded with structured outputs.  
Start fast with App Studio templates for stages and data objects, then plug in Prediction or Decision strategies. Keep everything fictional for demos, and log prompts and results. This pattern repeats across claims, onboarding, sales ops, and service—swap the data, keep the structure."  

Likely Q&A:
- Q: How do we pick where to start?  
  A: Find the slowest/highest-friction step tied to a KPI (cycle time/SLA); start with a bounded LLM task there.  
- Q: Can LLMs make routing decisions?  
  A: They can propose, but keep final routing in rules/decision tables; use LLM for classification and justification.  
- Q: How do we improve over time?  
  A: Capture feedback, expand golden sets, refine prompts, and retrain predictions when data shifts.  
