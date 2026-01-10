## Hands-On Labs (Reusable)

Principles: fictional data only; log prompts; keep changes small; review outputs; English-first with optional Polish examples for user-facing text. Tools: Cursor, ChatGPT (or approved LLM), Perplexity; optional MagicUI.ai/Lovable.

### Lab 1 — Case Intake & Triage Draft
- Duration: 60–75 min. Roles: BA/consultant/SE/SA mixed.  
- Goal: classify inbound email/form into a case type and propose routing with rationale.  
- Tools: Perplexity for public policy cites; ChatGPT for prompts; Cursor to store prompt pack/test cases.  
- Data: fictional emails/forms (10 cases).  
- Steps:  
  1) Research: Use Perplexity to pull 3–5 public routing/policy snippets with citations.  
  2) Prompt draft: In ChatGPT, craft a prompt to extract entities (customer type, product, urgency, channel) and classify into case type with routing.  
  3) Test set: In Cursor, create a prompt pack (YAML/MD) with 10 fictional test cases; include expected case type.  
  4) Iterate: Run tests, tighten format (JSON with type, routing, confidence, rationale). Add guardrails (no PII, word limits).  
  5) Review: Capture failures and refine once more.  
- Sample prompt:  
  ```
  You are a Pega consultant. Classify the inbound message into a case type (claims, onboarding, service). Extract customer_type, product, urgency, channel. Propose routing_queue and confidence 0–1 with a one-sentence rationale. Output JSON.
  ```
- Checkpoints: format is valid JSON; confidence present; rationale <40 words.  
- Success criteria: ≥80% correct case type on test set; routing with confidence + rationale; prompt pack saved; no real data.  
- Troubleshooting: If model is verbose, add word limits; if misclassifying, add 2–3 few-shot examples with fictional data; if routing is weak, add routing queues list and definitions.

### Lab 2 — Real-Time Decisioning Mock
- Duration: 60–75 min. Roles: consultant/SE/SA.  
- Goal: design a next-best-action (NBA) matrix using LLM context plus deterministic rules.  
- Tools: ChatGPT for drafts; Cursor for table/JSON; Perplexity for public policy citations if needed.  
- Steps:  
  1) Define context slots: intent, value_tier, risk_flag, channel, sentiment.  
  2) Prompt ChatGPT to propose eligibility/prioritization rules for 3 action types (retain, upsell, service_recover).  
  3) In Cursor, convert to a structured decision table/JSON with constraints and tie-breakers.  
  4) Dry-run 5 fictional scenarios; log outcomes and rationales.  
  5) Add guardrails: max one offer per channel; block upsell if risk_flag=true.  
- Sample prompt:  
  ```
  Draft a next-best-action table for retain, upsell, service_recover. Inputs: intent, value_tier, risk_flag, channel, sentiment. For each action, give eligibility rule and priority (1=highest). Add rationale. Output as a JSON array.
  ```
- Checkpoints: table is machine-readable; constraints explicit; rationale ≤25 words.  
- Success criteria: clear eligibility + priorities; 5 test runs recorded with expected outcomes; rationale per scenario.  
- Troubleshooting: If priorities tie, add tie-breaker on value_tier; if rules are vague, force boolean conditions; if outputs ramble, tighten word limits.

### Lab 3 — Low-Code Case Prototype + UI Scaffold
- Duration: 75–90 min. Roles: BA/consultant/SE/SA.  
- Goal: build a clickable prototype outline with AI-assisted drafts and a UI mock.  
- Tools: MagicUI.ai or Lovable (UI mock), ChatGPT (text), Cursor (spec + routing notes).  
- Data: fictional dataset (10–30 rows).  
- Steps:  
  1) Define case: stages, steps, data objects (fields + types), personas.  
  2) Generate UI mock (MagicUI/Lovable) for intake + review; export screenshot/spec.  
  3) In Cursor, write a Pega-style view description, assignment routing notes, and validation rules.  
  4) Ask ChatGPT for a stakeholder summary (English; add a Polish example for user-facing text).  
- Sample prompt (UI):  
  ```
  Create an intake form for a claims case with fields: policy_id (text), claim_type (dropdown), amount (currency), severity (low/med/high), channel (email/chat/web), description (textarea). Include validation rules and helper text. Use fictional data only.
  ```
- Checkpoints: stages and data objects listed; UI mock exported; routing notes include queues and SLAs; summary ≤200 words.  
- Success criteria: stage diagram outline + UI mock + routing notes + stakeholder summary; no real data.  
- Troubleshooting: If mock misses validation, add explicit rule list; if routing vague, provide queue names and SLAs; if summary long, cap words.  
