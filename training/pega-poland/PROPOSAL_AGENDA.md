# Pega Business AI Masterclass — Training Proposal

---

## Executive Summary

**The Imperative: From AI Chat to Deterministic Engineering**

The era of treating AI as a magical conversationalist is over. Enterprise organizations are stalling their generative AI initiatives because they are building brittle, unpredictable chatbots rather than robust, measurable systems. This training proposal is designed to fundamentally shift how Pega technical leads and business decision-makers approach artificial intelligence: moving from prompt-guessing to deterministic software engineering.

**Why This Training, Why Now?**

Frontier models in 2026 (Claude 3.7, Gemini 2.0, GPT-4o) are capable of autonomous reasoning and multi-step execution. However, without a deep understanding of the underlying "physics" of these models — tokenization, probability distributions, vector embeddings, and agentic orchestration — enterprise deployments are doomed to fail due to hallucinations, astronomical token costs, and catastrophic security vulnerabilities like prompt injection. Pega's architecture is uniquely positioned to act as the governed "brain" and "muscle" for these systems, but your teams need the technical rigor to integrate them properly.

**What Pega Teams Will Gain**

This masterclass fuses the bleeding edge of LLM engineering (Tree of Thoughts, Semantic Chunking, Re-ranking, LLM-as-a-Judge) with Pega-specific workflow acceleration patterns (Intelligent Intake, Confidence-Based Triage, and Generative Action). We will stop generating superficial UI mocks and start engineering autonomous ReAct agents that can search private corporate data and trigger Pega APIs securely.

**The ROI Profile**

This is a high-impact technical curriculum directly tied to business outcomes. By mastering advanced prompting and model routing economics, participants will target 30%+ AHT reduction, eliminate manual data entry through zero-touch JSON intake, and architect systems that cost pennies rather than dollars per query.

---

## Critique of Existing Agendas (Internal Reference)

### 1. The "1-Day: Fast-Start & Quick Wins" Agenda

- **Strong**: The RTF (Role-Task-Format) framework is an excellent, practical starting point. The focus on extracting JSON from unstructured text (Intelligent Intake) proves immediate Pega ROI.
- **Weak**: Incredibly superficial. It teaches people how to drive without explaining the engine. You cannot talk about "AI Governance" for 60 minutes without explaining why models hallucinate or leak data at a mathematical level.
- **Missing**: Any mention of RAG, Vector Spaces, or Agentic workflows.
- **Cut**: Too short to deliver lasting architectural change. Scrap as a standalone offering.
- **Ratings**: Technical Depth: 3/10 | Pega Relevance: 8/10 | Engagement: 7/10 | Readiness: 4/10

### 2. The "3-Day: Deep Dive & Builder Pods" Agenda

- **Strong**: The arc from basic prompting to building a domain-specific pod (Claims/Onboarding) is a good pedagogical concept.
- **Weak**: The pacing is a disaster. It jumps abruptly from basic prompt engineering straight into complex system building, completely skipping the intermediate steps of tool orchestration.
- **Missing**: The underlying physics of LLMs. How can a System Architect build an AI pod without understanding context windows, embeddings, or sampling math like Temperature and Min-P?
- **Cut**: The "Builder Tools" (MagicUI/Lovable) modules are complete filler. "Productivity Recipes" is also generic filler.
- **Ratings**: Technical Depth: 4/10 | Pega Relevance: 7/10 | Engagement: 6/10 | Readiness: 4/10

### 3. The "Business AI Masterclass (Expanded)" Agenda

- **Strong**: Real engineering. The inclusion of Transformers, Logits, RAG Architectures, OWASP Security, and LLM-as-a-Judge is excellent. The "Red Teaming" capstone is a phenomenal engagement tool.
- **Weak**: It swings too far into generic tech and forgets the client is Pega. The business value statements are generic rather than tied to Case Management, Intelligent Intake, and Workflow Acceleration.
- **Missing**: Modern 2026 context. Still references older sampling techniques and misses critical components like model routing economics.
- **Cut**: Vague role-play scenarios. Every lab must use Pega-specific fictional datasets (claims.csv, onboarding.csv).
- **Ratings**: Technical Depth: 9/10 | Pega Relevance: 4/10 | Engagement: 8/10 | Readiness: 7/10

---

## The New 3-Day Agenda

### DAY 1: The Physics of Intelligence & Pega Intelligent Intake

*We do not touch an LLM until we understand what a token is. Day 1 moves participants from "chatting" to deterministic engineering.*

| Time | Module | Objectives | Format | Business Value |
|---|---|---|---|---|
| 09:00–10:30 | **1.1 The Physics of LLMs & Controlling Randomness** | Understand Transformers, Tokenization (BPE), Context Windows, and how to manipulate Logits via Temperature, Top-P, and Min-P. | Lecture & Demo | Developers and VPs must understand that AI is a probabilistic math engine; controlling its randomness is the only way to guarantee enterprise reliability. |
| 10:30–10:45 | *Coffee Break & Micro-Exercise* | Each participant opens the OpenAI Tokenizer and tokenizes a sentence from their own Pega workflow. Share the most surprising token count. | Exercise | Grounds the abstract "token" concept in participants' daily reality. |
| 10:45–12:00 | **1.2 The 2026 Multi-Model Landscape & Economics** | Evaluate the cost, latency, and context limits of Claude 3.7, Gemini 2.0, GPT-4o, Perplexity, and Cursor. | Discussion & Demo | Selecting the wrong model destroys ROI; teams will learn to route simple tasks to cheap, fast models and complex logic to heavy reasoning engines. |
| 12:00–13:00 | *Lunch* | | | |
| 13:00–14:30 | **Lab 1: Pega Intelligent Intake (Prompt Engineering Workbench)** | Master the RTF framework, Zero-shot, and Few-shot prompting to force LLMs to output strict, deterministic JSON. | Hands-on Lab (service.csv) | Teaches participants how to eliminate manual data entry and accelerate Pega Case Creation from minutes to milliseconds. |
| 14:45–16:30 | **1.3 Advanced Orchestration (CoT, ToT & Refinement)** | Architect complex reasoning prompts using Chain-of-Thought, Tree of Thoughts, and Iterative Refinement. | Lecture & Lab | Solves the "hallucination" problem in complex Pega routing/triage logic by giving the AI a mathematical scratchpad to serialize its computation. |
| 16:30–17:00 | **Day 1 Retro & Architecture Mapping** | Map today's concepts to participants' actual Pega workflows. Identify which workflows benefit most from RAG vs Agents. | Discussion | Cements technical concepts into tangible Pega business value and sets the stage for Day 2. |

### DAY 2: Architecting AI Systems (RAG, Agents, and Pega Actions)

*A prompt is just a brain in a jar. Day 2 connects the brain to memory (RAG) and hands (APIs).*

| Time | Module | Objectives | Format | Business Value |
|---|---|---|---|---|
| 09:00–10:30 | **2.1 The Mathematics of Memory (Embeddings & Vector Spaces)** | Understand high-dimensional Vector Spaces, Embeddings, and Cosine Similarity. | Lecture | The absolute foundation of Enterprise Semantic Search, enabling Pega to find exact needle-in-a-haystack knowledge without fine-tuning. |
| 10:45–12:30 | **2.2 Advanced RAG Pipelines & Grounding** | Build Retrieval Augmented Generation pipelines incorporating Semantic Chunking, Hybrid Search, and Re-ranking models. | Lecture & Demo | Solves the LLM "knowledge cutoff" and hallucination risks by securely grounding answers strictly in live, approved corporate documents. |
| 12:30–13:30 | *Lunch* | | | |
| 13:30–15:00 | **2.3 Tool Calling & The ReAct Pattern** | Teach the LLM to output deterministic JSON schemas to trigger external functions via the Thought -> Action -> Observation loop. | Lecture & Demo | Shifts AI from a passive chatbot into an active "Digital Worker" that can execute secure Pega API calls and accelerate case resolution. |
| 15:00–16:45 | **Lab 2: Pega Generative Action Pod Build** | Build a multi-step autonomous agent that reads a Pega claim (claims.csv), checks fraud indicators, and drafts a defensible rejection/approval logic chain. | Hands-on Lab | Proves that AI can handle complex, multi-step cognitive labor, drastically reducing Average Handle Time for senior staff. |
| 16:45–17:00 | **Day 2 Retro & Peer Code Review** | Swap agent architectures with neighboring teams. Find one infinite loop risk, one missing error handler, one security concern. | Discussion | Exposes participants to different architectural approaches and surfaces vulnerabilities for Day 3. |

### DAY 3: Hardening the Enterprise (Security, Evaluation & Production)

*Highly capable systems without governance are automated liabilities. Day 3 prepares them for production.*

| Time | Module | Objectives | Format | Business Value |
|---|---|---|---|---|
| 09:00–10:30 | **3.1 OWASP Top 10 & Defending the Pipeline** | Master the mechanics of direct/indirect Prompt Injection, Data Leakage, and RAG poisoning. | Lecture | Protects the enterprise's proprietary data and reputation from malicious actors hijacking automated workflows. |
| 10:45–12:30 | **Lab 3: Red Teaming Capstone** | Attack neighboring teams' agents (built on Day 2) to force PII leaks and hallucinations, then rewrite system prompts with strict Guardrails to patch them. | Hands-on Gamified Lab | The only way to securely deploy AI is to understand exactly how it breaks; this builds an internal security playbook. |
| 12:30–13:30 | *Lunch* | | | |
| 13:30–15:00 | **3.2 LLM-as-a-Judge & Regression Testing** | Build automated regression testing suites using Golden Datasets to mathematically score AI outputs (Faithfulness, Relevance). | Lecture & Lab | Replaces "vibes-based" testing with engineering rigor, guaranteeing that updates to prompts or models do not break production Pega workflows. |
| 15:15–16:30 | **3.3 Production Economics & Demo Day** | Calculate Token Costs, Time-to-First-Token latency, and present final, secured AI architectures with an attached ROI model. | Discussion & Presentations | Ensures technical leads can justify their AI architecture choices to the CFO using cold, hard math. |
| 16:30–17:00 | **Graduation & Next Steps** | Summary of 3-day arc, certificate distribution, and 90-day action plan. | Ceremony | Sends participants home with momentum and a concrete roadmap. |

---

## What Participants Will Leave With

1. **A Production-Ready Prompt Cookbook**: A library of meticulously engineered RTF and Chain-of-Thought prompts, specifically tuned to force deterministic JSON outputs for Pega Intelligent Intake workflows.

2. **A Verified AI ROI Calculator**: A concrete mathematical model mapping API token costs (across Claude, Gemini, and GPT-4o) against labor hours saved, proving the exact break-even point for their specific use cases.

3. **A Functional ReAct Agent Architecture**: A mapped multi-step logic loop (Thought -> Action -> Observation) ready to be integrated with Pega GenAI Connectors to handle Generative Action and Case Routing.

4. **A Red Teaming Security Playbook**: A documented list of tested Guardrails and XML delimiter strategies that actively prevent OWASP Top 10 vulnerabilities like indirect prompt injection and data leakage.

5. **An Automated Evaluation Framework**: A curated "Golden Dataset" pipeline using LLM-as-a-Judge to execute mathematical regression testing on human language, ensuring future AI updates never break production.
