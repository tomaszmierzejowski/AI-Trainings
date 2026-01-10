## Cursor / ChatGPT / Perplexity Power Use

### Slides
- Slide 1 — Right Tool, Right Task (Polish: Właściwe narzędzie)  
  - Cursor: code/rule edits, diffs, explanations.  
  - ChatGPT: drafts, prompts, meeting/email notes.  
  - Perplexity: cited research, public policy lookup.  
  - Speaker notes: Position them as a stack—research → draft → implement/review.

- Slide 2 — Safe Setup (Polish: Bezpieczne środowisko)  
  - No real customer data; use fictional sets.  
  - Keep repos clean; review diffs; small batches.  
  - Respect VPN/SSO/approved LLM endpoints.  
  - Speaker notes: Remind to log prompts and responses.

- Slide 3 — Cursor Workflows (Polish: Cursor)  
  - Explain-this-rule; propose refactor; generate tests.  
  - Inline edits with review; TODO traces.  
  - Speaker notes: Demo reading a Pega-like rule and adding validation.

- Slide 4 — ChatGPT Workflows (Polish: ChatGPT)  
  - Draft emails, decision rationales, meeting notes.  
  - Test prompts and formatting; add acceptance criteria.  
  - Speaker notes: Use clear roles and formats; ask for short rationale + final answer.

- Slide 5 — Perplexity Workflows (Polish: Perplexity)  
  - Retrieve public policy text with citations.  
  - Summaries of docs; compare options with sources.  
  - Speaker notes: Emphasize cited outputs; keep scope to public info.

- Slide 6 — Pega Tie-ins (Polish: Pega kontekst)  
  - Rule explanations, stage suggestions, routing drafts, persona scripts.  
  - Integration stubs and test data generation (fictional).  
  - Speaker notes: Map tasks to case lifecycle; stress governance.

### Audiobook Script (6–7 min + Q&A)
"Use each tool for its strength. Perplexity is your research front-end: pull public, cited guidance you can ground into prompts. ChatGPT is your drafting engine: emails, meeting notes, rationales, and prompt experiments. Cursor is your implementation partner: reading rules, proposing edits, and generating tests—with diffs you can review.  
Keep it safe: no real customer data, work in small batches, and review diffs. Log prompts and responses for reuse and audit.  
In practice: start with Perplexity to gather cited public policy on PII handling. Feed that into ChatGPT to draft a client email or a prompt. Then use Cursor to explain an existing rule and propose a safer refactor, generating a small test set. This stack lets you research, draft, and implement quickly while staying governed."  

Likely Q&A:
- Q: When should I not use Perplexity?  
  A: When data is confidential or not public—keep to approved internal sources only.  
- Q: How do I keep Cursor changes safe?  
  A: Small diffs, review every change, avoid committing secrets, and use fictional data in examples/tests.  
- Q: What if ChatGPT output is verbose?  
  A: Add format constraints, word limits, and ask for a short rationale plus a clean final answer.  
