---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/graph-based-reasoning"
topic: "Graph-Based Reasoning"
level: advanced
built_from: ["graph-neural-networks", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/compositional-reasoning", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/knowledge-grounded-agents"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Graph-Based Reasoning"
minutes: 16
category: structured-reasoning
---

# Graph-Based Reasoning
> Put the entities and relations of a problem into a **graph**, and reasoning becomes movement
> along edges: one hop for a fact, several hops for a conclusion no single edge contains. A neural
> network can do that movement as **message passing**, or a language model can do it by walking a
> knowledge graph in the prompt. The one sentence: **structure the problem as a graph, and multi-hop
> inference becomes a computation you can name, trace, and check.**

**Why it matters:** the two live production uses are **graph-structured retrieval** (Graph RAG and
its descendants, where provenance and multi-hop questions beat flat vector similarity) and
**knowledge-graph question answering (KGQA)**, where the graph supplies the facts a model would
otherwise invent. The research edge is **neural algorithmic reasoning** — training networks to
imitate classical algorithms so they generalize to larger inputs than they were trained on.
Interviewers probe the failure mode: **over-smoothing and the receptive-field limit**, where a
k-layer message-passing network simply cannot see a k+1-hop dependency.

**Start here — suggested path:**

1. **See message passing before the equations** — read [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) — **Sanchez-Lengeling, Reif, Pearce & Wiltschko (Distill)**. *Interactive figures for nodes, edges, and the aggregate-then-update step that every graph reasoner repeats.*
2. **Get the argument for structure** — read [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261) — **Battaglia et al., DeepMind (2018)**. *Entities and relations as an architectural prior, and why combinatorial generalization needs one.*
3. **Watch the course opening** — watch [Stanford CS224W: Machine Learning with Graphs, Lecture 1.1 — Why Graphs](https://www.youtube.com/watch?v=JAB_plj2rbA) — **Jure Leskovec (Stanford Online)**. *The problem framing: which questions are naturally graph questions, and what a node embedding is for.*
4. **See reasoning as algorithm imitation** — read [Neural Algorithmic Reasoning](https://arxiv.org/abs/2105.02761) — **Petar Veličković & Charles Blundell (2021)**. *Train the network to execute a classical algorithm, then reuse that executor on messy real inputs.*
5. **Take it to language models** — read [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687) — **Besta et al. (2023)**. *Thoughts as vertices and dependencies as edges, so a reasoning trace can merge and revisit branches instead of only branching.*

## Courses (free)
- [CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Jure Leskovec (Stanford)** — the canonical free syllabus, slides, and colabs for graph representation learning and reasoning tasks.
- [Geometric Deep Learning — lecture series](https://geometricdeeplearning.com/lectures/) — **Bronstein, Bruna, Cohen & Veličković** — the "grids, groups, graphs, geodesics, gauges" course; why message passing is the right primitive on a graph.
- [CS520: Knowledge Graphs](https://web.stanford.edu/class/cs520/) — **Stanford** — free seminar with recorded sessions on building, querying, and reasoning over knowledge graphs.

## Videos
- [Stanford CS224W, Lecture 1.1 — Why Graphs](https://www.youtube.com/watch?v=JAB_plj2rbA) — **Jure Leskovec (Stanford Online)** — the clearest half hour on which problems are graph problems and what representation buys you.
- [Reasoning on Natural Inputs](https://www.youtube.com/watch?v=U2vybDdoDAQ) — **Petar Veličković (IPAM, UCLA)** — the algorithmic-reasoning programme explained by the person who defined it: run the algorithm in latent space, not on hand-clean inputs.

## Key Papers
- [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261) — **Battaglia et al. (2018)** — the graph-network formalism that unifies most architectures on this page.
- [Graph Attention Networks](https://arxiv.org/abs/1710.10903) — **Veličković et al. (2018)** — attention as the aggregation rule; the workhorse layer for reasoning over heterogeneous edges.
- [Neural Algorithmic Reasoning](https://arxiv.org/abs/2105.02761) — **Veličković & Blundell (2021)** — the position paper: learn an algorithm's steps, then transfer the executor.
- [The CLRS Algorithmic Reasoning Benchmark](https://arxiv.org/abs/2205.15659) — **Veličković et al. (2022)** — thirty classical algorithms turned into a generalization test with held-out larger inputs.
- [The CLRS-Text Algorithmic Reasoning Language Benchmark](https://arxiv.org/abs/2406.04229) — **Markeeva et al. (2024)** — the same tasks as text, so language models and graph networks are measured on one scale.
- [Graph of Thoughts](https://arxiv.org/abs/2308.09687) — **Besta et al. (2023)** — reasoning traces as arbitrary graphs rather than chains or trees, with aggregation and refinement operators.
- [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://arxiv.org/abs/2307.07697) — **Sun et al. (2023)** — the model walks the graph itself, beam-searching relation paths instead of reading a retrieved blob.
- [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://arxiv.org/abs/2310.01061) — **Luo et al. (2023)** — plan a relation path first, ground it in the graph second; the trace is the explanation.
- [Can Language Models Solve Graph Problems in Natural Language?](https://arxiv.org/abs/2305.10037) — **Wang et al. (2023)** — the NLGraph benchmark, and the honest result that prompting gains fade as graph problems get harder.
- [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — **Pan, Luo, Wang et al. (2023)** — the three integration patterns (graph-enhanced model, model-enhanced graph, and the two combined).

## Articles / Blogs (free, no paywall)
- [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) — **Distill** — still the best interactive explanation of the aggregation step everything here depends on.
- [GraphRAG: unlocking LLM discovery on narrative private data](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/) — **Microsoft Research** — why global, corpus-level questions need a graph and community summaries rather than top-k chunks.
- [CLRS: the algorithmic reasoning benchmark](https://github.com/google-deepmind/clrs) — **Google DeepMind** — the code and data; you can reproduce the size-generalization results yourself.

## Books (free, with chapters)
- [*Graph Representation Learning* — the graph-neural-network chapters](https://www.cs.mcgill.ca/~wlh/grl_book/) — **William L. Hamilton (McGill)** — free PDF; the compact formal treatment of message passing and its limits.
- [*Knowledge Graphs*](https://kgbook.org/) — **Hogan, Blomqvist, Cochez et al.** — free; the standard reference for the graph half, including query languages and inductive reasoning over graphs.

## In this platform
- The mechanism owner (canonical home): [Graph Neural Networks](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks) · [Equivariant and Geometric Deep Learning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning/equivariant-and-geometric-deep-learning)
- Prerequisite in this sub-area: [Knowledge Graphs](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs/knowledge-graphs)
- Next in this section: [Causal and Relational Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/causal-and-relational-reasoning/causal-and-relational-reasoning) · [Compositional Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/compositional-reasoning/compositional-reasoning)
- Where it ships: [Graph RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/graph-rag/graph-rag) · [Knowledge-Grounded Agents](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/knowledge-grounded-agents/knowledge-grounded-agents)
- The mathematics: [Spectral Graph Theory](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/spectral-graph-theory/spectral-graph-theory)
