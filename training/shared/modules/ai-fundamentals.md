## AI Fundamentals (Enterprise)

### Slides
- Slide 1 — Why AI + Low-Code Now (Polish: Dlaczego teraz?)  
  - AI speeds discovery + build; low-code enforces guardrails.  
  - Use AI for text-heavy steps: intake, triage, summarize, decide.  
  - Value lens: cycle time, SLA hits, CSAT/NPS, conversion.  
  - Speaker notes: Frame this as “faster change with control.” Call out hybrid teams; AI keeps momentum while low-code keeps governance.

- Slide 2 — Model Types (Polish: Typy modeli)  
  - LLMs: language + reasoning; not a database.  
  - Predictive models: structured scoring (propensity, risk).  
  - Retrieval: fetch facts at request time.  
  - Speaker notes: Stress fusion: LLM for understanding, prediction for scoring, retrieval for truth.

- Slide 3 — Grounding vs. Fine-Tuning (Polish: Ugruntowanie vs. trenowanie)  
  - Default: grounding with retrieval + instructions.  
  - Fine-tune only for narrow, stable, high-volume tasks.  
  - Keep prompts/data fictional in training/demos.  
  - Speaker notes: Emphasize freshness and safety of grounding; fine-tune when data stable and approval exists.

- Slide 4 — Enterprise Patterns (Polish: Wzorce)  
  - Classify, extract, summarize, route, recommend, draft.  
  - Agentic flows = plan → act → check; keep humans on high-risk steps.  
  - Speaker notes: Map patterns to real flows: email intake → classify → extract → route; NBA → recommend; draft note.

- Slide 5 — Risks & Mitigations (Polish: Ryzyka i zabezpieczenia)  
  - Hallucination, prompt injection, leakage, bias.  
  - Mitigate: allow/deny lists, redaction, content filters, logging, HITL.  
  - Speaker notes: Give a short example of prompt injection and how to strip URLs/HTML.

- Slide 6 — Metrics & Evaluation (Polish: Metryki)  
  - Quality: precision/recall, factuality.  
  - Impact: cycle time, SLA adherence, CSAT.  
  - Offline tests + inline monitors; keep golden sets.  
  - Speaker notes: Tie tests to business KPIs; keep 10–20 golden cases per use case.

- Slide 7 — Pega Tie-ins (Polish: Pega kontekst)  
  - Process AI: signals/predictions; Decisioning: NBA arbitration.  
  - GenAI connectors: classify, summarize, draft.  
  - Guardrails: access groups, masked data pages, logging.  
  - Speaker notes: Show how LLM augments, not replaces, existing Pega decisioning.

### Audiobook Script (7–8 min + Q&A)
"Welcome. Let’s ground ourselves on what AI can safely do in enterprise workflows. Large language models understand and reason over text—they excel at reading an email, extracting entities, and proposing next steps. They are not databases, so we keep truth in systems of record and fetch facts at request time using retrieval. For structured scoring—who to prioritize, what to offer—we rely on predictive models. The winning pattern is fusion: LLM for understanding, prediction for scoring, decisioning to arbitrate, all wrapped in governance.  
We prefer grounding over fine-tuning. Grounding means you provide the facts and constraints in the prompt—this keeps data fresh and safer. Fine-tuning is for narrow, stable, high-volume cases and only with approvals.  
Risks: hallucinations, prompt injection, leakage, and bias. We counter with redaction, allow/deny lists, filters, logging, and human-in-the-loop for high-stakes moves.  
Evaluation is dual: quality metrics like precision and recall, and business impact like cycle time and SLA hits. Keep golden test sets and monitor inline.  
In Pega, Process AI captures signals, Decisioning selects the next best action, and GenAI connectors draft or summarize. AI is an accelerator when we keep it governed, measured, and tied to outcomes."  

Likely Q&A:
- Q: When do we fine-tune instead of retrieve?  
  A: Only when the task is narrow, data is stable, volume is high, and approvals exist; otherwise use retrieval.  
- Q: How do we prevent leakage?  
  A: Redact PII, constrain prompts, use approved endpoints, log everything, and avoid sending raw records.  
- Q: How do we measure success?  
  A: Track both accuracy (precision/recall, factuality) and business KPIs (cycle time, SLA hits, CSAT); test offline and monitor inline.  
