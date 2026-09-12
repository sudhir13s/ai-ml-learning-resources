---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/knowledge-grounded-agents"
topic: "Knowledge-Grounded Agents"
level: advanced
built_from: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-language-models", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-robotics", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Knowledge-Grounded Agents"
minutes: 17
category: modern-applications
---

# Knowledge-Grounded Agents
> Most agents keep their state in the transcript: everything the agent knows is text in a context
> window. A knowledge-grounded agent keeps its state in a **structured store** instead — a graph of
> entities and relations, a library of verified skills, a set of typed facts with provenance and
> timestamps. The one sentence: **give the agent a database instead of a diary, and its memory
> becomes queryable, updatable, and checkable.**

**Why it matters:** the transcript approach fails in exactly three predictable ways — it forgets
past the context window, it cannot answer questions that require joining facts stated far apart,
and it has no way to retract something that stopped being true. Graph-structured memory answers
all three, which is why **Graph RAG**, temporal knowledge graphs, and skill libraries dominated
2024–26 agent design. The failure mode interviewers probe: **extraction error compounding** — every
fact in the graph was written by the same fallible model, so a bad entity resolution poisons every
query that touches it.

**Start here — suggested path:**

1. **Start with the loop** — read [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — **Yao, Zhao, Yu et al. (2023)**. *Thought, action, observation; the interleaving that lets an external store correct the model mid-task.*
2. **Watch the framing from the author** — watch [Language Agents (PhD defense)](https://www.youtube.com/watch?v=zwfE6J2BIR4) — **Shunyu Yao (Princeton)**. *Where memory, actions, and reasoning sit in an agent architecture, rather than as separate prompt tricks.*
3. **Make the memory a graph** — read [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — **Edge, Trinh, Cheng et al., Microsoft Research (2024)**. *Entity graph plus community summaries; the answer to "what are the themes in this whole corpus?"*
4. **Make the memory grow** — read [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — **Wang, Xie, Jiang et al., NVIDIA (2023)**. *A skill library of executable code, indexed and reused: knowledge stored as verified programs.*
5. **See the 2025 state** — read [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) — **Rasmussen, Paliychuk, Beauvais et al. (2025)**. *Facts with validity intervals, so the agent can represent that something used to be true.*

## Courses (free)
- [Knowledge Graphs for RAG](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/) — **DeepLearning.AI with Neo4j** — free short course; build the graph, write the queries, wire it to a model, in about an hour.
- [CS520: Knowledge Graphs](https://web.stanford.edu/class/cs520/) — **Stanford** — the academic companion: construction, identity, and reasoning, with recorded seminar sessions.

## Videos
- [Language Agents (PhD defense)](https://www.youtube.com/watch?v=zwfE6J2BIR4) — **Shunyu Yao (Princeton)** — ReAct, Tree of Thoughts, and the cognitive-architecture framing, from their author.
- [Generally Capable Agents in Open-Ended Worlds](https://www.youtube.com/watch?v=ZSPEyFqAGDc) — **Jim Fan (NVIDIA, GTC 2024)** — the Voyager line of work: skills as code, curriculum, and self-verification.
- [GraphRAG methods to create optimized context windows for retrieval](https://www.youtube.com/watch?v=c5qJHr3DnT4) — **Jonathan Larson (Microsoft Research)** — a GraphRAG author on indexing cost, community detection, and when a graph is not worth it.

## Key Papers
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — **Yao et al. (2023)** — the base loop every knowledge-grounded agent still runs.
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — **Edge et al., Microsoft Research (2024)** — the reference architecture for graph-structured retrieval, with the local/global distinction that matters most.
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — **Wang et al., NVIDIA (2023)** — the skill library: knowledge as executable, tested code rather than as remembered text.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — **Park, O'Brien, Cai et al. (2023)** — memory stream, retrieval by relevance-recency-importance, and reflection into higher-level facts.
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — **Packer, Wooders, Lin et al., Berkeley (2023)** — paging between a small context and a large store, managed by the model itself.
- [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831) — **Gutiérrez, Shu, Gu, Yasunaga & Su (2024)** — a knowledge graph plus personalized PageRank for single-step multi-hop retrieval.
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) — **Rasmussen et al. (2025)** — bitemporal facts; the current answer to memory that must expire.
- [Think-on-Graph](https://arxiv.org/abs/2307.07697) — **Sun et al. (2023)** — the agent traverses the knowledge graph itself, so the reasoning path is an auditable artefact.
- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) — **Zhang, Bo, Ma et al. (2024)** — the design space: what to store, how to write it, how to read it, how to evaluate it.

## Articles / Blogs (free, no paywall)
- [GraphRAG](https://github.com/microsoft/graphrag) — **Microsoft Research** — the open implementation; the indexing pipeline is the part worth reading before you adopt it.
- [GraphRAG documentation](https://microsoft.github.io/graphrag/) — **Microsoft Research** — prompt tuning, indexing cost, and the query modes explained by the maintainers.
- [ReAct: Synergizing Reasoning and Acting in Language Models — project page](https://react-lm.github.io/) — **Yao et al. (Princeton)** — demos and prompts; the fastest way to see the trace format.
- [Voyager — project page](https://voyager.minedojo.org/) — **NVIDIA and collaborators** — videos of the skill library growing, plus the code.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — **Lilian Weng** — the standard map of planning, memory, and tool use, with the memory taxonomy this page assumes.

## Books (free, with chapters)
- [*Knowledge Graphs* — Ch. 3 "Schema, Identity, Context", Ch. 5 "Inductive Knowledge"](https://kgbook.org/) — **Hogan, Blomqvist, Cochez et al.** — free; identity and provenance are exactly what an agent's graph store gets wrong first.

## In this platform
- Previous in this section: [Neuro-Symbolic Language Models](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-language-models/neuro-symbolic-language-models)
- Next in this section: [Neuro-Symbolic Robotics](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-robotics/neuro-symbolic-robotics)
- Canonical homes elsewhere: [Graph RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/graph-rag/graph-rag) · [Agent Memory](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/memory/memory) · [Reason and Act](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/reason-and-act/reason-and-act)
- Related: [Agent Planning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/planning/planning) · [Citations and Attribution](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/citations-and-attribution/citations-and-attribution) · [Graph-Based Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/graph-based-reasoning/graph-based-reasoning)
