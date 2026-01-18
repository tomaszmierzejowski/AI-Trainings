## Hands-On Labs (Practical)

Use fictional data only. Tools: Cursor, ChatGPT, Perplexity.

### Lab 1: Intelligent Intake & Routing (45-60 min)
*Goal: Convert unstructured email into structured JSON decisioning data.*
- **Role**: Senior BA / Pega Architect.
- **Data**: `fictional-datasets/service.csv` (10 emails).
- **Steps**:
  1. **Research**: Use Perplexity to find "Best practices for email classification taxonomy".
  2. **Draft Prompt (ChatGPT)**:
     - Role: Triage Bot.
     - Task: Extract Sentiment, Intent, Product, Urgency.
     - Format: JSON.
     - Constraint: If intent is unclear, set Urgency=High.
  3. **Test**: Run 3 examples. Check JSON validity.
  4. **Refine**: Add "Few-Shot" examples for edge cases (e.g., angry customer).
- **Success Criteria**: 90% accurate classification on the test set. Valid JSON output.

### Lab 2: The Decision Strategy (60 min)
*Goal: Build a logic table and a "reasoning" prompt.*
- **Role**: Decisioning Architect.
- **Data**: `fictional-datasets/claims.csv`.
- **Steps**:
  1. **Define Rules**: Use ChatGPT to brainstorm "Fraud indicators for auto claims".
  2. **Build Table**: Create a decision matrix (Markdown or Excel).
  3. **Prompting**: Create a Chain-of-Thought prompt:
     - "Analyze this claim."
     - "Check against these 3 fraud rules."
     - "Think step-by-step."
     - "Recommendation: Approve/Reject/Refer."
- **Success Criteria**: Clear reasoning logic for each decision.

### Lab 3: Rapid Prototyping (Low-Code + AI) (90 min)
*Goal: Go from idea to UI mock to User Story.*
- **Role**: Product Owner / System Architect.
- **Tools**: MagicUI (optional) or ChatGPT + Cursor.
- **Steps**:
  1. **Concept**: "Mobile-first onboarding app for banking."
  2. **UI Mock**: Use MagicUI or ChatGPT to describe the screen layout.
  3. **Specs**: Use Cursor to write the Pega Case Type definition (Stages, Steps).
  4. **Data Model**: Ask AI to generate the Data Class structure (JSON/Java).
- **Success Criteria**: A visual mock + a technical spec ready for App Studio.
