## Business AI Masterclass Curriculum (3-Day Expanded)

**Focus**: Deep technical understanding, advanced engineering patterns, and rigorous governance.
**Target Audience**: Business users who want to master the *engineering* behind the magic, and Technical leads who need a structured approach to AI adoption.

**Resources**: 
- Slide decks: `slides/*.pptx`
- Audio scripts: `audio-scripts/*.md` (Audiobook style)
- Labs: `labs/*.md` (Step-by-step engineering exercises)
- Trainer Guide: `TRAINER_GUIDE.md` (Deep technical notes)

---

### Curriculum Overview

| Day | Theme | Technical Focus | Business Outcome |
|---|---|---|---|
| **1** | **The Engineering of Intelligence** | Transformers, Tokens, Probability, Advanced Prompting (CoT, ToT). | Ability to write deterministic, reliable prompts for complex tasks. |
| **2** | **Building Systems: RAG & Agents** | Embeddings, Vector Search, ReAct Pattern, Tool Use. | Understanding how to build "Chat with my PDF" and "Agentic" workflows. |
| **3** | **Governance, Security & Production** | OWASP Top 10 for LLMs, Prompt Injection, Evaluation Metrics. | Safe, compliant, and measured AI deployment. |

---

### Detailed Agenda

#### Day 1: The Engineering of Intelligence
*Goal: Demystify the "Black Box" and master the physics of LLMs.*

- **09:00–10:00 — Module 1.1: The Physics of LLMs**
  - **The Transformer**: Attention mechanisms explained simply ("The cocktail party effect").
  - **Tokens vs. Words**: Tokenization (BPE), vocabulary size, and cost implications.
  - **The Probability Distribution**: Logits, Softmax, and how the model predicts the next token.
  - *Technical Dive*: Why `Temperature=0` isn't always 100% deterministic.

- **10:15–11:30 — Module 1.2: Controlling Randomness**
  - **Hyperparameters**: Deep dive into `Temperature`, `Top-P` (Nucleus Sampling), and `Top-K`.
  - **Frequency/Presence Penalties**: Forcing creativity vs. repetition.
  - **Lab 1.1**: "The Slot Machine" — Testing different temperatures on the same prompt.

- **11:30–12:30 — Module 1.3: Advanced Prompting Architectures**
  - **Zero-shot vs. Few-shot**: The mathematical impact of examples in the context window.
  - **Chain of Thought (CoT)**: Forcing intermediate computation.
  - **Tree of Thoughts (ToT)**: Exploring multiple reasoning paths (DFS/BFS conceptualization).

- **13:30–15:00 — Lab 1.2: The Prompt Engineering Workbench**
  - **Task**: Build a complex "Reasoning Engine" for a business case (e.g., Mortgage Approval).
  - **Requirement**: Use CoT to reduce hallucination rates.
  - **Output**: A reliable prompt template that passes 10/10 test cases.

- **15:15–16:30 — Module 1.4: Hallucinations & Grounding**
  - **Why they happen**: The "stochastic parrot" problem.
  - **Types**: Fact fabrication vs. Instruction deviations.
  - **Countermeasures**: "Refusal-aware" training and System Prompts.

- **16:30–17:00 — Day 1 Retro & Q&A**

#### Day 2: Building Systems (RAG & Agents)
*Goal: Move beyond "Chat" to "Systems" that can see, search, and act.*

- **09:00–10:30 — Module 2.1: The Memory of AI (Embeddings)**
  - **Vector Space**: Representing meaning as numbers (High-dimensional space).
  - **Cosine Similarity**: How we measure "closeness" of ideas mathematically.
  - **Vector Databases**: The long-term memory for LLMs.

- **10:45–12:00 — Module 2.2: RAG Architecture (Retrieval Augmented Generation)**
  - **The Workflow**: User Query -> Embed -> Search Vector DB -> Retrieve Chunks -> Inject into Context -> Generate Answer.
  - **Chunking Strategies**: Fixed size vs. Semantic chunking.
  - **Lab 2.1**: "Paper RAG" — Simulating a vector search manually to understand the mechanics.

- **13:00–14:30 — Module 2.3: Agents & The ReAct Pattern**
  - **ReAct**: **Re**asoning + **Act**ing. The loop of "Thought -> Action -> Observation".
  - **Tool Use**: How an LLM "calls" an API (JSON formatting).
  - **The "Brain" vs. The "Hands"**: Separating reasoning from execution.

- **14:45–16:30 — Lab 2.2: The Pod Build (Agentic Workflow)**
  - **Scenario**: Build a "Research Agent" using Perplexity (Search) + ChatGPT (Synthesis).
  - **Challenge**: The agent must "critique" its own search results and search again if needed.
  - **Outcome**: A multi-step workflow that self-corrects.

- **16:30–17:00 — Day 2 Retro**

#### Day 3: Governance, Security & Production
*Goal: Deploying safely in a hostile world.*

- **09:00–10:30 — Module 3.1: The Dark Side (Security)**
  - **OWASP Top 10 for LLMs**: The standard industry framework.
  - **Prompt Injection**: "Ignore previous instructions". Direct vs. Indirect injection.
  - **Jailbreaking**: DAN (Do Anything Now) and role-play attacks.
  - **Data Leakage**: Training data extraction attacks.

- **10:45–12:00 — Module 3.2: Evaluation & Metrics**
  - **The Evaluation Gap**: Why accuracy is hard to measure.
  - **Deterministic Metrics**: ROUGE, BLEU (and why they fail for reasoning).
  - **LLM-as-a-Judge**: Using GPT-4 to grade GPT-3.5.
  - **Golden Datasets**: Building a regression suite.

- **13:00–15:00 — Lab 3: Red Teaming Capstone**
  - **Role**: You are the Attacker.
  - **Target**: Your neighbor's "Pod Build" from Day 2.
  - **Goal**: Trick their agent into revealing the "System Prompt" or performing a banned action.
  - **Defense**: Patching the holes with "Guardrail" prompts.

- **15:15–16:30 — Module 3.3: Production & ROI**
  - **Cost Modeling**: Tokens per query * Volume.
  - **Latency**: The "Time to First Token" (TTFT) metric.
  - **ROI**: Calculating hours saved vs. API costs.

- **16:30–17:00 — Graduation & Next Steps**
