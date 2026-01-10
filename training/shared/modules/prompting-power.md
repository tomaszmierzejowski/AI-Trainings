## Prompting Power Skills

### Slides
- Slide 1 — Prompt Formula (Polish: Formuła promptu)  
  - Instruction → context → format → constraints → examples (optional).  
  - Example: “You are a Pega consultant. Classify the email into a case type and routing. Output JSON.”  
  - Speaker notes: Show the template and stress brevity plus clarity.

- Slide 2 — Patterns that Work (Polish: Wzorce)  
  - Chain-of-thought (short), critique-and-revise, delimitation with ``` fences, retries with changes.  
  - Few-shot when you need strict structure; keep examples fictional.  
  - Speaker notes: Demonstrate a short reasoning step then a clean final answer.

- Slide 3 — Prompt Ladders (Polish: Drabinka promptów)  
  - Start coarse → test on 5–10 cases → tighten constraints.  
  - Log each version in a prompt cookbook.  
  - Speaker notes: Encourage small iterations; keep failures to learn.

- Slide 4 — Safety & Data Handling (Polish: Bezpieczeństwo)  
  - No real customer data; use placeholders/masking.  
  - Redact PII; avoid copying secrets; log prompts/responses.  
  - Speaker notes: Mention audit trails and approved endpoints.

- Slide 5 — Pega Use Cases (Polish: Przykłady Pega)  
  - Intake clarification, email triage, stage summaries, routing suggestions.  
  - Decision table drafts, meeting-note generation.  
  - Speaker notes: Tie each to case lifecycle; emphasize format outputs (JSON/table).

### Audiobook Script (6–7 min + Q&A)
"Prompting becomes reliable when it is systematic. Use a simple formula: clear instruction, the minimal context, the output format, constraints, and examples when structure matters. Example: ‘You are a Pega consultant. Classify the email into a case type and suggest routing. Output JSON with type, confidence, and reason.’  
Patterns: add a short chain-of-thought so the model reasons, then ask for a clean final answer. Use critique-and-revise when the first draft is weak. Delimit inputs with fences to avoid confusion.  
Build prompt ladders: start broad, test on a handful of real cases, note failure modes, and tighten constraints. Capture every version in a prompt cookbook so teams reuse the good ones.  
Safety: never paste real customer data. Use placeholders, redact PII, and log prompts/responses for audit. Stick to approved endpoints.  
Pega workflows benefit directly: classify intake, extract entities, generate stage summaries, draft decision table candidates, and produce concise meeting notes. Consistency and safety make prompting a reusable capability."  

Likely Q&A:
- Q: How many examples should I include?  
  A: Only when you need deterministic formatting—start with 2–3 fictional, concise examples.  
- Q: How to reduce hallucinations?  
  A: Provide grounding facts, constrain output format, and keep the task narrow; add validation checks.  
- Q: Should I always use chain-of-thought?  
  A: Use brief reasoning for complex tasks; avoid long reasoning that bloats tokens—ask for a short rationale plus a clean final answer.  
