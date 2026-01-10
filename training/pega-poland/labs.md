## Hands-On Labs (Pega Poland)

Use fictional Polish/English data; no client data. Tools: Cursor, ChatGPT/approved LLM, Perplexity; optional MagicUI.ai/Lovable. English-first; add Polish examples for user-facing text.

### Lab 1 — Email Intake to Case & Routing
- Duration: 60–75 min. Roles: BA/consultant/SE/SA.  
- Goal: classify inbound email to case type (claims/onboarding/service) and propose routing with rationale.  
- Steps:  
  1) Research: Use Perplexity to pull 3–5 public policy snippets (citations).  
  2) Prompt: In ChatGPT, draft classification + routing prompt (JSON output).  
  3) Test set: In Cursor, store prompt pack + 10 fictional test cases with expected case type.  
  4) Iterate: Tighten constraints (word limits, queues list).  
  5) Review failures; adjust few-shot examples if needed.  
- Sample prompt:  
  ```
  You are a Pega consultant. Classify this email into case_type (claims/onboarding/service) and propose routing_queue. Extract customer_type, product, urgency, channel. Return JSON with confidence 0–1 and one-sentence rationale in English; add Polish queue label if user-facing.
  ```
- Checkpoints: valid JSON; rationale <40 words; queues match list provided.  
- Success: ≥80% correct type; routing with confidence + rationale; prompts logged in repo.  
- Troubleshooting: If misrouting, provide queue definitions; if verbose, add word caps; if missing fields, force schema.

### Lab 2 — NBA Strategy Mock
- Duration: 60–75 min. Roles: consultant/SE/SA.  
- Goal: design a next-best-action table for retention/upsell/service recovery.  
- Steps:  
  1) Define context slots: intent, value_tier, risk_flag, channel, sentiment.  
  2) Ask ChatGPT for eligibility/prioritization rules and rationales.  
  3) Convert to structured table/JSON in Cursor with constraints and tie-breakers.  
  4) Dry-run 5 fictional scenarios; record outcomes.  
  5) Add guardrails: block upsell if risk_flag=true; prioritize retain for high value.  
- Sample prompt:  
  ```
  Create a next-best-action table for retain, upsell, service_recover. Inputs: intent, value_tier, risk_flag, channel, sentiment. Provide eligibility (boolean), priority (1=highest), and rationale <=20 words. Output JSON array.
  ```
- Success: table with clear rules; 5 scenario outcomes recorded; rationales concise.  
- Troubleshooting: If priorities tie, add tie-breakers (value_tier, sentiment); if rules vague, force boolean expressions; if too wordy, cap words.

### Lab 3 — Low-Code Prototype + UI Mock
- Duration: 75–90 min. Roles: mixed.  
- Goal: clickable prototype outline with AI-assisted drafts and UI mock.  
- Steps:  
  1) Define stages, steps, data objects, personas.  
  2) Generate intake/review mock in MagicUI/Lovable (fictional values); export screenshot/spec.  
  3) In Cursor, map to App Studio view spec, assignment routing, and validation rules.  
  4) Draft stakeholder summary (English; include Polish example for user-facing text).  
- Sample prompt (UI):  
  ```
  Build an intake form for onboarding with fields: applicant_id, product, kyc_flag, risk_score, region, channel, notes. Add validation and helper text. Use fictional data; labels in English, add Polish in parentheses where user-facing.
  ```
- Success: stage outline + UI mock + routing notes + 150–200 word summary; no real data.  
- Troubleshooting: If mock misses validation, list them explicitly; if summary long, cap words; if routing vague, add queue names and SLAs.  
