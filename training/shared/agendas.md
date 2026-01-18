## Agendas (Practical AI Training)

Focus: 80% hands-on, 20% theory. Outcome-driven (reduce cycle time, improve quality).
Resources: slide decks in `training/shared/slides/`, TTS in `training/shared/tts/`, prompt packs in `training/shared/labs/packs/`, datasets in `training/shared/assets/fictional-datasets/`.

### 1-Day: Fast-Start & Quick Wins
*Goal: Leave with working prompts, a configured tool stack, and an ROI model.*

- **09:00–09:30 — Kickoff: The AI Opportunity.**
  - **Show**: Market trends, "Why Now?" slide.
  - **Discuss**: Friction in current workflows (typing, reading).
  - **KPIs**: Cycle time reduction, AHT (Average Handle Time).
- **09:30–10:45 — Module: Prompt Mastery (RTF & CoT).**
  - **Teach**: The RTF Formula (Role-Task-Format).
  - **Demo**: Bad prompt vs. RTF prompt (Live in ChatGPT).
  - **Exercise**: "Laddering" — iterate a prompt 3 times (Base -> +Context -> +Constraints).
- **11:00–12:00 — Module: Tool Selection Matrix.**
  - **Matrix**: Perplexity (Research) vs ChatGPT (Drafting) vs Cursor (Building).
  - **Demo**: Find a specific Pega regulation using Perplexity (verify citation).
  - **Setup**: Ensure everyone has accounts logged in.
- **12:00–13:00 — Lunch.**
- **13:00–14:30 — Lab 1: Intelligent Intake & Triage.**
  - **Asset**: `service.csv` (10 emails).
  - **Task**: Write a prompt to extract JSON entities (Intent, Sentiment) from row 1.
  - **Challenge**: Handle a "confused" customer email correctly.
  - **Validation**: Does the JSON parse?
- **14:45–16:00 — Module: Pega Workflow Acceleration.**
  - **Concepts**: Intake -> Triage -> Generative Action.
  - **Activity**: Calculate ROI for a hypothetical process (Time saved * Volume).
  - **Demo**: Show a "Generative Reply" workflow concept.
- **16:00–17:00 — Governance & Action Plan.**
  - **Safety**: The "Billboard Rule" (No PII).
  - **Plan**: What will you build on Monday?

### 3-Day: Deep Dive & Builder Pods
*Goal: Build a deployable prototype, a prompt library, and trained champions.*

- **Day 1**: Fast-Start (Same as above).
- **Day 2**: Builder Mode.
  - 09:00–10:30 — **Module: Advanced Prompting**.
    - Techniques: Few-shot, Iterative Refinement, Decomposition.
  - 10:45–12:00 — **Module: Productivity Recipes**.
    - Role-based prompts: BAs (User Stories), SEs (Demos), SAs (Refactoring).
  - 13:00–16:00 — **Lab 2: Pod Build (Domain Specific)**.
    - Teams pick a domain: Claims (Fraud check) or Onboarding (KYC).
    - Build chain: Intake Prompt -> Decision Matrix -> Rejection/Approval Email.
  - 16:00–17:00 — Review & Refine (Peer critique of prompts).
- **Day 3**: Scale & Governance.
  - 09:00–10:30 — **Module: Evaluation & Testing**.
    - Concepts: Golden sets (test cases), Regression testing (did the prompt break?).
  - 10:45–12:30 — **Lab 3: Final Polish & Audit**.
    - Stress-testing: "Adversarial" prompts (try to break the bot).
  - 13:30–15:30 — **Demo Day**.
    - Teams present their Pod Build.
    - Must show: The Prompt, The Output, The Business Value (ROI).
  - 15:30–17:00 — **Governance Deep Dive & Roadmap**.
    - Audit logs, Pega "Human in the loop" patterns.
