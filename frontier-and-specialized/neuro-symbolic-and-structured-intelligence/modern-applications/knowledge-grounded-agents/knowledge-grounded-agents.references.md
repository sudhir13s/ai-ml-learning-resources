---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/knowledge-grounded-agents/references"
topic: "Knowledge-Grounded Agents — References"
parent: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/knowledge-grounded-agents"
type: references
updated: 2026-09-14
---

# Knowledge-Grounded Agents — references

> Companion link library for **[Knowledge-Grounded Agents](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/knowledge-grounded-agents/knowledge-grounded-agents)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Start with the loop** — read [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — **Yao, Zhao, Yu et al. (2023)**. *Thought, action, observation; the interleaving that lets an external store correct the model mid-task.*
2. **Watch the framing from the author** — watch [Language Agents (PhD defense)](https://www.youtube.com/watch?v=zwfE6J2BIR4) — **Shunyu Yao (Princeton)**. *Where memory, actions, and reasoning sit in an agent architecture, rather than as separate prompt tricks.*
3. **Make the memory a graph** — read [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — **Edge, Trinh, Cheng et al., Microsoft Research (2024)**. *Entity graph plus community summaries; the answer to "what are the themes in this whole corpus?"*
4. **Make the memory grow** — read [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — **Wang, Xie, Jiang et al., NVIDIA (2023)**. *A skill library of executable code, indexed and reused: knowledge stored as verified programs.*
5. **See the 2025 state** — read [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) — **Rasmussen, Paliychuk, Beauvais et al. (2025)**. *Facts with validity intervals, so the agent can represent that something used to be true.*

**In this platform**:
- Related: [Agent Planning](/ai-ml/practitioner-workflows/agentic-systems/planning/planning) · [Citations and Attribution](/ai-ml/practitioner-workflows/llm-applications/citations-and-attribution/citations-and-attribution) · [Graph-Based Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/graph-based-reasoning/graph-based-reasoning)
- Canonical homes elsewhere: [Graph RAG](/ai-ml/practitioner-workflows/llm-applications/graph-rag/graph-rag) · [Agent Memory](/ai-ml/practitioner-workflows/agentic-systems/memory/memory) · [Reason and Act](/ai-ml/practitioner-workflows/agentic-systems/reason-and-act/reason-and-act)

**Videos**:
- [Generally Capable Agents in Open-Ended Worlds](https://www.youtube.com/watch?v=ZSPEyFqAGDc) — **Jim Fan (NVIDIA, GTC 2024)** — the Voyager line of work: skills as code, curriculum, and self-verification.
- [GraphRAG methods to create optimized context windows for retrieval](https://www.youtube.com/watch?v=c5qJHr3DnT4) — **Jonathan Larson (Microsoft Research)** — a GraphRAG author on indexing cost, community detection, and when a graph is not worth it.
- [Language Agents (PhD defense)](https://www.youtube.com/watch?v=zwfE6J2BIR4) — **Shunyu Yao (Princeton)** — ReAct, Tree of Thoughts, and the cognitive-architecture framing, from their author.

**Courses**:
- [CS520: Knowledge Graphs](https://web.stanford.edu/class/cs520/) — **Stanford** — the academic companion: construction, identity, and reasoning, with recorded seminar sessions.
- [Knowledge Graphs for RAG](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/) — **DeepLearning.AI with Neo4j** — free short course; build the graph, write the queries, wire it to a model, in about an hour.

**Articles**:
- [GraphRAG](https://github.com/microsoft/graphrag) — **Microsoft Research** — the open implementation; the indexing pipeline is the part worth reading before you adopt it.
- [GraphRAG documentation](https://microsoft.github.io/graphrag/) — **Microsoft Research** — prompt tuning, indexing cost, and the query modes explained by the maintainers.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — **Lilian Weng** — the standard map of planning, memory, and tool use, with the memory taxonomy this page assumes.
- [ReAct: Synergizing Reasoning and Acting in Language Models — project page](https://react-lm.github.io/) — **Yao et al. (Princeton)** — demos and prompts; the fastest way to see the trace format.
- [Voyager — project page](https://voyager.minedojo.org/) — **NVIDIA and collaborators** — videos of the skill library growing, plus the code.

**Papers**:
- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) — **Zhang, Bo, Ma et al. (2024)** — the design space: what to store, how to write it, how to read it, how to evaluate it.
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — **Edge et al., Microsoft Research (2024)** — the reference architecture for graph-structured retrieval, with the local/global distinction that matters most.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — **Park, O'Brien, Cai et al. (2023)** — memory stream, retrieval by relevance-recency-importance, and reflection into higher-level facts.
- [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831) — **Gutiérrez, Shu, Gu, Yasunaga & Su (2024)** — a knowledge graph plus personalized PageRank for single-step multi-hop retrieval.
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — **Packer, Wooders, Lin et al., Berkeley (2023)** — paging between a small context and a large store, managed by the model itself.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — **Yao et al. (2023)** — the base loop every knowledge-grounded agent still runs.
- [Think-on-Graph](https://arxiv.org/abs/2307.07697) — **Sun et al. (2023)** — the agent traverses the knowledge graph itself, so the reasoning path is an auditable artefact.
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — **Wang et al., NVIDIA (2023)** — the skill library: knowledge as executable, tested code rather than as remembered text.
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) — **Rasmussen et al. (2025)** — bitemporal facts; the current answer to memory that must expire.

**Books**:
- [*Knowledge Graphs* — Ch. 3 "Schema, Identity, Context", Ch. 5 "Inductive Knowledge"](https://kgbook.org/) — **Hogan, Blomqvist, Cochez et al.** — free; identity and provenance are exactly what an agent's graph store gets wrong first.
