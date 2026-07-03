---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  strong { color: #e74c3c; }
  code { background-color: #f0f0f0; padding: 2px 5px; border-radius: 4px; }
---

# Business AI Masterclass
## Day 1: The Engineering of Intelligence

<!-- Speaker Note:
- Welcome the group.
- State the goal: "We are moving from Magic to Math."
- Set expectations: This is a technical deep dive.
-->

---

# Agenda: Day 1

1. **Module 1.1**: The Physics of LLMs (Transformers & Tokens)
2. **Module 1.2**: Controlling Randomness (Temperature & Top-P)
3. **Module 1.3**: Advanced Prompting (CoT & ToT)
4. **Lab 1**: The Prompt Engineering Workbench
5. **Module 1.4**: Hallucinations & Grounding

---

# Module 1.1: The Physics of LLMs

## The Transformer Architecture (2017)
* "Attention is All You Need" (Vaswani et al.)
* **Self-Attention**: The model weighs the importance of every word against every other word in the sequence.
* **Analogy**: The "Cocktail Party Effect". You focus on one voice while processing the background noise.

<!-- Speaker Note:
- Draw a simple diagram: Input -> [Attention Mechanism] -> Output.
- Explain "Self-Attention": It allows the model to handle long-range dependencies. In the sentence "The animal didn't cross the street because it was too tired", what does "it" refer to? Self-attention links "it" to "animal".
-->

## It's Not Magic, It's Math
* An LLM is a **Next Token Prediction Engine**.
* $P(w_t | w_{1}, ..., w_{t-1})$
* It calculates the probability of the next word given the context.

---

# What is a "Token"?

* LLMs do not see "words". They see integers (Tokens).
* **BPE (Byte Pair Encoding)**:
  * Common words = 1 token (`Apple`)
  * Rare words = Multiple tokens (`Un-friend-li-ness`)
  * Code/Numbers = Often split (`12345` -> `12`, `345`)
* **Cost**: You pay per 1k tokens (Input vs Output costs differ).

<!-- Speaker Note:
- Open the OpenAI Tokenizer page (platform.openai.com/tokenizer) if you have internet.
- Show "Hamburger" (1 token) vs "Lollipop" (often 2-3 tokens).
- Explain why LLMs fail at math: They see numbers as separate tokens, not numerical values.
-->

---

# The Probability Distribution

* The model outputs a vector of **Logits** (raw scores).
* **Softmax Function**: Converts logits to percentages (0-100%).
* **Result**: A list of all possible next words and their likelihood.
  * `The`: 40%
  * `A`: 30%
  * `Apple`: 0.001%

<!-- Speaker Note:
- Emphasize that the model essentially rolls a dice.
- Even if "The" is 40%, there is a chance it picks "A". This is the source of creativity AND hallucination.
-->

---

# Module 1.2: Controlling Randomness

## Temperature
* **Math**: Divides the logits before Softmax.
* **Low (0.1)**: Exaggerates differences. The "Best" word wins. (Deterministic).
* **High (1.5)**: Flattens the curve. "Bad" words get a chance. (Creative/Chaotic).

## Top-P (Nucleus Sampling)
* Instead of "Top 5 words" (Top-K), we take the "Top 90% cumulative mass".
* **Dynamic**: 
  * If unsure, the pool is big.
  * If sure, the pool is small.

<!-- Speaker Note:
- Use the "Slot Machine" analogy.
- Low Temp = The machine is rigged to always give the jackpot.
- High Temp = The machine is fair (or chaotic).
-->

---

# Module 1.3: Advanced Prompting

## Chain of Thought (CoT)
* **Prompt**: "Think step-by-step."
* **Mechanism**: Forces the model to generate intermediate tokens.
* **Why**: LLMs have no "working memory" outside of the tokens they generate. Writing *is* thinking.

<!-- Speaker Note:
- This is the single most important technique.
- Explain: If you ask a human to multiply 342 * 912 in their head, they fail. If you give them paper, they succeed.
- CoT is the "paper" for the LLM.
-->

## Tree of Thoughts (ToT)
* **Concept**: Generate multiple paths. Evaluate. Backtrack.
* **Use Case**: Complex coding, strategic planning.
* **Flow**:
  1. Generate 3 ideas.
  2. Critique each.
  3. Pick the winner.
  4. Expand.

---

# Lab 1: Prompt Engineering Workbench

* **Goal**: Build a Mortgage Approval Prompt.
* **Constraints**:
  * Accuracy > 95%.
  * Must handle missing data gracefully.
  * Must output JSON.

*(Switch to Lab Instructions)*

<!-- Speaker Note:
- Walk around.
- Look for people struggling with JSON format. Suggest "Few-Shot" examples.
- Look for people struggling with math. Suggest "Chain of Thought".
-->

---

# Module 1.4: Hallucinations & Grounding

## Types of Failure
1. **Fabrication**: Inventing facts (The "Stochastic Parrot").
2. **Instruction Drift**: Forgetting the rules in a long conversation.
3. **Sycuphancy**: Agreeing with the user even when they are wrong.

## The Fix: Grounding (RAG)
* Never ask the model to "know" things.
* Ask it to "process" things you give it.
* **Formula**: `Answer based ONLY on the provided context.`

---

# Day 1 Wrap Up

* **Summary**: We moved from "Chat" to "Engineering".
* **Key Takeaway**: Randomness is a feature, not a bug. You must control it.
* **Tomorrow**: We build systems (RAG & Agents).
