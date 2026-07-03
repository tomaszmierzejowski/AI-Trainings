# Lab 2: Building Systems (RAG & Agents)

## Part 1: "Paper RAG" (Analog Simulation)
*Goal: Understand the mechanics of Vector Search without a computer.*

**Activity**:
1. **The Corpus**: Take the provided 1-page "Pega Poland Employee Handbook" (Fictional).
2. **Chunking**: Physically cut the paper into paragraphs (Chunks).
3. **Embedding**: On the back of each chunk, write 3 keywords that represent its "meaning" (e.g., "Holidays", "Sick Leave", "Remote Work"). This is a simplified "Vector".
4. **The Query**: "Can I work from Spain?"
5. **Retrieval**: Scan the keywords (Vectors). Find the top 2 chunks that match "Remote Work" or "Location".
6. **Generation**: Read ONLY those 2 chunks. Answer the question.

**Discussion**:
- What if the keywords didn't match? (Semantic gap).
- What if the chunk was too small to have context? (Chunking strategy).

---

## Part 2: The Digital Pod Build (Agentic Workflow)
**Objective**: Build a "Research Agent" that can critique its own work.

**Tools**: Perplexity (Researcher) + ChatGPT (Synthesizer).

**The Workflow**:
1. **Step 1: Research**: 
   - Prompt Perplexity: "Find the latest EU AI Act requirements for 'High Risk' AI systems. Cite 3 specific articles."
   - *Output*: A list of requirements.

2. **Step 2: Critique (The ReAct Loop)**:
   - Prompt ChatGPT: "You are a Compliance Officer. specific articles? If yes, summarize. If no, output 'MISSING_DATA'."
   - *Logic*: If MISSING_DATA, you must refine the Perplexity prompt and try again.

3. **Step 3: Synthesis**:
   - Prompt ChatGPT: "Draft a memo to the CTO summarizing the compliance gaps based on these findings."

**Deliverable**:
- A flow diagram of your Agent.
- The 3 Prompts used.
- One example of the "Critique" step catching a bad result (Hallucination or laziness).
