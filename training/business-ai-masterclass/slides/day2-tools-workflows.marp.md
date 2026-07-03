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
## Day 2: Building Systems (RAG & Agents)

<!-- Speaker Note:
- Recap Day 1: We mastered the single prompt.
- Goal for Day 2: We link prompts together into Systems.
-->

---

# Agenda: Day 2

1. **Module 2.1**: The Memory of AI (Embeddings & Vectors)
2. **Module 2.2**: RAG Architecture
3. **Lab 2**: The Pod Build (Agentic Workflow)
4. **Module 2.3**: Agents & The ReAct Pattern

---

# Module 2.1: The Memory of AI

## What is an Embedding?
* Converting text into a list of numbers (Vector).
* **OpenAI text-embedding-3-small**: 1,536 dimensions.
* **Concept**:
  * `King` - `Man` + `Woman` ≈ `Queen`
  * Meaning is preserved in the math.

<!-- Speaker Note:
- Use the "Grocery Store" analogy.
- Aisle 1: Fruits. Aisle 10: Cleaning.
- Embeddings place similar items in similar "aisles" (dimensions).
-->

## Cosine Similarity
* Measuring the angle between two vectors.
* **0 degrees**: Identical.
* **90 degrees**: Unrelated.
* **180 degrees**: Opposite.
* *This is how "Search" works in the AI era.*

---

# Module 2.2: RAG Architecture
*(Retrieval Augmented Generation)*

## The Problem
* LLMs have a "Knowledge Cutoff".
* LLMs hallucinate on obscure facts.
* LLMs cannot see your private data.

## The Architecture
1. **Ingest**: PDF -> Text -> Chunks -> Embeddings -> Vector DB.
2. **Retrieve**: User Query -> Embedding -> Vector Search -> Top 3 Chunks.
3. **Generate**: `System Prompt` + `Top 3 Chunks` + `User Query` -> Answer.

<!-- Speaker Note:
- Draw the pipeline on a whiteboard.
- Highlight "Chunking" as a critical failure point. If you cut a sentence in half, meaning is lost.
-->

---

# Module 2.3: Agents & Tools

## The ReAct Pattern
* **Re**ason + **Act**.
* **The Loop**:
  1. **Thought**: The model plans what to do.
  2. **Action**: The model outputs a special token (e.g., JSON for API call).
  3. **Observation**: The system executes the code and gives the result back.
  4. **Repeat**.

<!-- Speaker Note:
- Explain that the LLM is the "Brain", but the Code is the "Hands".
- The Loop is what makes it autonomous.
-->

## Tool Use (Function Calling)
* LLMs can't "browse the web" natively.
* They output specific JSON that *we* execute.
* **Example**:
  ```json
  { "function": "get_weather", "args": { "city": "London" } }
  ```

---

# Lab 2: The Pod Build

* **Goal**: Build a Research Agent.
* **Workflow**:
  1. **Planner**: Breaks down the user question.
  2. **Researcher**: Uses Perplexity/Search to find facts.
  3. **Critique**: Checks if the facts are sufficient.
  4. **Writer**: Synthesizes the answer.

*(Switch to Lab Instructions)*

<!-- Speaker Note:
- This is the hardest lab.
- Ensure teams are using the output of step 1 as input for step 2.
- The "Critique" step is often skipped—force them to include it.
-->

---

# Day 2 Wrap Up

* **Summary**: We moved from "One Prompt" to "Systems of Prompts".
* **Key Takeaway**: Context is King. RAG gives context. Agents give action.
* **Tomorrow**: Governance & Security.
