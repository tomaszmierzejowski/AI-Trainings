## Adaptation Guide (Reuse for New Clients)

Goal: clone this training to new clients quickly while staying safe and relevant.

### Tailoring Map
- Roles: highlight role-relevant recipes; adjust labs to their primary channels (email/chat/forms/mobile).  
- KPIs: map examples to their top 2–3 KPIs (cycle time, CSAT/NPS, AHT, conversion, compliance).  
- Domain: swap demo domain (claims/onboarding/sales ops/service/HR/finance) with fictional data.  
- Tooling: replace ChatGPT with approved LLM; note VPN/SSO; remove tools they cannot use.  
- Data sensitivity: strip examples near restricted entities; add redaction reminders.  
- Governance: embed their approvals, logging/audit needs, retention rules.  
- Language: keep instruction English-first; add localized examples only for user-facing text.  

### Quick Procedure
1) Duplicate `training/shared` to `training/<client-name>/`.  
2) Update `survey.md` with any client-specific wording and send.  
3) Adjust `agendas.md` time zones, modules, and labs per survey answers.  
4) In modules, swap examples for the client domain; keep slide structure.  
5) In labs, change channels/data and success criteria to match their KPIs; keep fictional datasets.  
6) Update governance slides/notes with their security/legal constraints and approved endpoints.  
7) Remove or replace any blocked tools; add offline alternatives if needed.  
8) Add localized (Polish or other) examples only where end-users read the text.  
9) Re-run a quick check: no real data, endpoints approved, logs enabled, prompts stored.  
