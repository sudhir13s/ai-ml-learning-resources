---
id: "llms-applications-and-agents/agentic-ai/context-engineering"
topic: "Context Engineering"
level: advanced
built_from: ["prompting-and-in-context-learning", "memory", "tool-use"]
leads_to: ["multi-agent-systems", "agent-evaluation"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Context Engineering"
minutes: 16
category: agentic-ai
---

# Context Engineering

> Prompt engineering asks what to *write*. Context engineering asks what to *load*: the discipline of
> deciding, every turn, which system instructions, tool schemas, retrieved documents, memories and
> prior steps occupy a finite attention budget — and what gets summarised, offloaded or dropped.
> For an agent that runs for hundreds of steps, this is the main engineering surface.

**Why it matters:** it became the dominant framing for agent work in 2025, and it is where most
production agent failures actually originate.

- **What is probed:** the four operations — **write** (scratchpads, memories outside the window), **select** (retrieve only what this step needs), **compress** (summarise, compact), **isolate** (sub-agents with their own clean windows); why token count is a poor proxy for context quality.
- **The failure taxonomy to name:** context **poisoning** (a hallucination re-read as fact), **distraction** (the model over-attends to a bloated history), **confusion** (irrelevant tools or documents pulled into a decision) and **clash** (later information contradicting earlier).
- **The counter-intuitive rule:** a 1M-token window is a budget, not a target. Attention degrades with length (lost-in-the-middle), and every extra token is paid for in latency and cost — so the smallest sufficient context wins.
- **The cache constraint:** a stable prefix is what makes prefix caching work. Putting a timestamp or a shuffled tool list at the top of a system prompt silently destroys the cache hit rate.

**Start here — suggested path:**

1. **Read the definition from a frontier lab** — read [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — **Anthropic**. *Context as a finite budget, compaction, note-taking and sub-agent isolation, with the reasoning behind each.*
2. **Get the four-operation framework** — read [Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/) — **Lance Martin (LangChain)**. *Write, select, compress, isolate — the vocabulary the field settled on.*
3. **Learn the failure modes by name** — read [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) — **Drew Breunig**. *Poisoning, distraction, confusion and clash, each with a concrete fix.*
4. **Read a production post-mortem** — read [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) — **Yichao Ji (Manus)**. *Key-value-cache stability, masking tools instead of removing them, keeping failures in context — hard-won and specific.*
5. **See where the term came from** — read [Context engineering](https://simonwillison.net/2025/Jun/27/context-engineering/) — **Simon Willison**. *The naming discussion (including Karpathy's framing) and why "prompt engineering" stopped describing the job.*

## Courses (free)

- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/introduction) — **Hugging Face** — free, end-to-end; building the loop is what makes context growth tangible.
- [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) — **Rohit G (community, MIT-licensed)** — a large open curriculum that builds agents, skills and Model Context Protocol servers from first principles; useful as a hands-on build track rather than a primary source.

## Videos

- [Context Engineering for Agents](https://www.youtube.com/watch?v=_IlTcWciEC4) — **Lance Martin (Latent Space)** — the write/select/compress/isolate framework presented by its author, with real agent traces.
- [Context Engineering for AI Agents with LangChain and Manus](https://www.youtube.com/watch?v=6_BcCthVvb8) — **LangChain** — the LangChain and Manus practitioners comparing what actually held up in production.
- [How We Build Effective Agents](https://www.youtube.com/watch?v=D7_ipDqhtwk) — **Barry Zhang, Anthropic (AI Engineer)** — the simplicity-first argument that context engineering is a consequence of.
- [How Long Contexts Fail (and How to Fix Them)](https://www.youtube.com/watch?v=-iRQxHxYqak) — **Drew Breunig (O'Reilly)** — the failure taxonomy walked through live.

## Key Papers

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — **Liu et al. (2023)** — the empirical result underneath every ordering and budgeting decision: middle-of-context information is used least.
- [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334) — **Mei et al. (2025)** — the first systematic taxonomy: retrieval, processing, management, and the systems built on them.

## Articles / Blogs (free, no paywall)

- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — **Anthropic** — the reference statement of the discipline: budget, compaction, note-taking, sub-agents.
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — **Anthropic** — tool schemas and returned payloads *are* context; this is the half most teams neglect.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — **Anthropic** — context isolation across sub-agents, with the token-cost accounting made explicit.
- [Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/) — **Lance Martin** — the four-operation framework with LangGraph examples.
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) — **Yichao Ji** — production lessons: design around the key-value cache, keep the wrong turns visible, mask rather than remove.
- [The rise of context engineering](https://blog.langchain.com/context-engineering-for-agents/) — **LangChain** — the same framework from the framework authors, with the agent-trajectory view.
- [Context Engineering](https://www.philschmid.de/context-engineering) — **Philipp Schmid** — a compact, well-structured definition and worked example, good for a first pass.

## Books (free, with chapters)

- [*Speech and Language Processing* (3rd ed.) — Ch. 12 "Model Alignment, Prompting and In-Context Learning"](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky & Martin** — free PDF; the academic grounding for why in-context conditioning works at all.

## In this platform

- Canonical home of the prompt itself: [Prompting and In-Context Learning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning)
- What context engineering assembles: [Memory for Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/memory/memory) · [Tool Use and Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use) · [RAG Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-foundations/rag-foundations) · [Reranking](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/reranking/reranking)
- The loop it runs inside: [Agent Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-foundations/agent-foundations) · [Planning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/planning/planning) · [Multi-Agent Systems](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/multi-agent-systems/multi-agent-systems)
- Why a bigger window is not a free fix: [Long Context vs RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/long-context-vs-rag/long-context-vs-rag) · [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures)
- What a stable prefix is worth: [Caching and Cost Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/caching-and-cost-optimization/caching-and-cost-optimization)
- Untrusted content entering context is an attack surface: [Prompt Injection and Agent Guardrails](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails)
- Intuition track: [Context Engineering](/ai-ml/ai-ml-intuitions/memory-retrieval-and-context/context-engineering/context-engineering-intuition) · [Agent Memory](/ai-ml/ai-ml-intuitions/memory-retrieval-and-context/agent-memory/agent-memory-intuition)
- Build it as a workflow: [Context Engineering](/ai-ml/practitioner-workflows/llm-application-workflows/context-engineering) · [Agent Building](/ai-ml/practitioner-workflows/llm-application-workflows/agent-building)
