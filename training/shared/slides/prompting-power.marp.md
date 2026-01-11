---
marp: true
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
---

# Prompt Mastery Quickstart
## The Engineering Approach

---

# The Foundation: RTF Framework

- **Role**: Who is the AI? (e.g., Senior Architect)
- **Task**: What must it do? (e.g., Draft Code)
- **Format**: How should it look? (e.g., JSON)

> "If you only learn one thing, learn RTF."

---

# Technique 1: Few-Shot Prompting

- Don't just tell; **show**.
- Provide 2-3 examples of Input -> Output.
- Critical for JSON, SQL, or Pega Rule formats.

---

# Technique 2: Chain-of-Thought

- Ask the model to **"Think step-by-step"**.
- Forces reasoning before the answer.
- Reduces logic errors by 40%+.

---

# Technique 3: Iterative Refinement

- Never accept the first draft.
- **The "Refusal" Check**: "If you lack info, state it."
- Ask AI to critique its own output.

---

# Advanced: Ladders & Decomposition

- **Laddering**: Start simple -> Verify -> Add Constraints.
- **Decomposition**: Break big tasks (Build App) into small steps (Define Data -> Define Stages).

---

# Safety & Governance

- **No PII**: Use placeholders like `[Client_ID]`.
- **Approved Endpoints**: Don't paste secrets into public web UIs.
- Treat the prompt window like a billboard.
