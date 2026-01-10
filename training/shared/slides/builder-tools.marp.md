---
marp: true
theme: default
paginate: true
---

# Builder Tools (MagicUI / Lovable)
- Draft fast; harden in Pega
- Fictional data only
Notes: Set expectation: reference, not production.

---
# Agenda
- Purpose
- Inputs that matter
- Demo flow
- Safety & quality
- Pega mapping
Notes: 20–30 minutes.

---
# Purpose
- Rapid UI mock generation
- Shorten iteration; not final build
Notes: Pega/App Studio stays source of truth.

---
# Inputs (Wejścia)
- Fields, types, validation, layout hints
- Sample fictional values; optional persona
Notes: Keep prompt concise; include helper text.

---
# Demo Flow
- Paste spec → generate → export → review → harden in Pega
- Capture prompts for reuse
Notes: Review before reuse; check accessibility.

---
# Safety & Quality
- No real data; check a11y and security
- Align to design system; validate errors/masks
Notes: Mention client branding constraints.

---
# Pega Mapping
- Map mock to views/sections; rebuild/verify
- Reusable prompts: intake, review, approvals
Notes: Store mapping notes in repo.

---
# Wrap
- Use as accelerator only
- Keep prompts logged and reusable
- Verify in Pega before demos
Notes: Point to lab 3 and prompt packs.
