---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/symbolic-knowledge-as-neural-input/references"
topic: "Symbolic Knowledge as Neural Input — References"
parent: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/symbolic-knowledge-as-neural-input"
type: references
updated: 2026-09-14
---

# Symbolic Knowledge as Neural Input — references

> Companion link library for **[Symbolic Knowledge as Neural Input](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/symbolic-knowledge-as-neural-input/symbolic-knowledge-as-neural-input)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Start from the graph itself** — skim the inductive-knowledge chapter of [*Knowledge Graphs*](https://kgbook.org/) — **Hogan, Blomqvist, Cochez et al.** *Embeddings, graph neural networks, and rule mining introduced in one vocabulary, on top of the symbolic model.*
2. **Read the founding model** — read [Translating Embeddings for Modeling Multi-relational Data](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) — **Bordes, Usunier, García-Durán, Weston & Yakhnenko (2013)**. *TransE: a relation is a translation, `h + r ≈ t`; simple enough to derive on a whiteboard.*
3. **See why the geometry matters** — read [RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space](https://arxiv.org/abs/1902.10197) — **Sun, Deng, Nie & Tang (2019)**. *Rotations model symmetry, antisymmetry, inversion, and composition — the patterns TransE cannot.*
4. **Read the modern map** — skim [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — **Pan, Luo, Wang, Chen, Wang & Wu (2023)**. *Every way the two are combined, sorted; the vocabulary interviewers use.*
5. **Run the production version** — work through [GraphRAG](https://github.com/microsoft/graphrag) — **Microsoft Research**. *Build a knowledge graph from a corpus, summarise its communities, and answer global questions the chunk-and-embed pipeline cannot.*

**In this platform**:
- The mechanism this page assumes: [Graph Neural Networks](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks)
- Where it ships: [Graph RAG](/ai-ml/practitioner-workflows/llm-applications/graph-rag/graph-rag) · [Agent Memory](/ai-ml/practitioner-workflows/agentic-systems/memory/memory) · [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/evaluation/hallucination-and-grounding/hallucination-and-grounding)
- Prerequisites: [Knowledge Graphs](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs/knowledge-graphs) · [Rules, Constraints and Ontologies](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/rules-constraints-and-ontologies/rules-constraints-and-ontologies) · [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai)
- Next in this sub-area: [Neural Models with Symbolic Constraints](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints/neural-models-with-symbolic-constraints)

**Videos**:
- [GraphRAG: LLM-Derived Knowledge Graphs for RAG](https://www.youtube.com/watch?v=r09tJfON6kE) — **Alex Chao (Microsoft Research, GraphRAG co-author)** — the indexing and community-summarisation pipeline walked through by one of its authors.
- [Knowledge Graphs (lecture)](https://www.youtube.com/playlist?list=PLar5iR7mhb4dJHDSjmeo6W7HomHBSZf9t) — **Knowledge-Based Systems, TU Dresden (Markus Krötzsch)** — a full university course on graph data models, query languages, and ontologies — the symbolic side that embeddings compress.
- [Neuro-Symbolic AI Summer School 2025 — Day 2](https://www.youtube.com/live/-uEx0IICBxg) — **Centaur AI Institute** — current systems that feed structured knowledge into learned models, presented by the people building them.

**Courses**:
- [Stanford CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Stanford (Jure Leskovec)** — free slides and readings; the knowledge-graph block covers TransE through RotatE and query answering over embeddings.
- [Stanford CS520: Knowledge Graphs](https://web.stanford.edu/class/cs520/) — **Stanford (Vinay Chaudhri et al.)** — free seminar materials: how graphs are built, queried, and used by learned models, with practitioner sessions.

**Articles**:
- [GraphRAG](https://github.com/microsoft/graphrag) — **Microsoft Research** — the reference implementation, with the indexing and query pipelines documented end to end.
- [PyKEEN](https://github.com/pykeen/pykeen) — **PyKEEN developers (Ali, Berrendorf, Hoyt et al.)** — dozens of knowledge-graph embedding models with a reproducible benchmarking harness; the fastest way to compare scoring functions yourself.
- [Scallop: a language for neurosymbolic programming](https://www.scallop-lang.org/) — **University of Pennsylvania** — what it looks like when the symbolic input is a relational database the network reads and writes.

**Papers**:
- [A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models](https://arxiv.org/abs/2501.13958) — **Zhang, Chen, Bei et al. (2025)** — the 2025 state of graph-conditioned retrieval, with the design axes named.
- [Complex Embeddings for Simple Link Prediction](https://arxiv.org/abs/1606.06357) — **Trouillon, Welbl, Riedel, Gaussier & Bouchard (2016)** — complex-valued embeddings that handle asymmetric relations with a bilinear score.
- [ERNIE: Enhanced Language Representation with Informative Entities](https://arxiv.org/abs/1905.07129) — **Zhang, Han, Liu, Jiang, Sun & Liu (2019)** — entity embeddings fused into a language model's hidden states rather than its prompt.
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — **Edge, Trinh, Cheng, Bradley, Chao, Mody, Truitt & Larson (2024)** — extract a graph, summarise communities, answer questions no single chunk contains.
- [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831) — **Gutiérrez, Shu, Gu, Yasunaga & Su (2024)** — a graph plus personalised PageRank as the retrieval index; multi-hop retrieval in a single step.
- [KEPLER: A Unified Model for Knowledge Embedding and Pre-trained Language Representation](https://arxiv.org/abs/1911.06136) — **Wang, Gao, Zhang et al. (2021)** — one encoder trained on both masked language modelling and a knowledge-embedding objective.
- [Modeling Relational Data with Graph Convolutional Networks](https://arxiv.org/abs/1703.06103) — **Schlichtkrull, Kipf, Bloem, van den Berg, Titov & Welling (2017)** — R-GCN: the graph itself becomes the computation, one message-passing channel per relation type.
- [RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space](https://arxiv.org/abs/1902.10197) — **Sun et al. (2019)** — the clearest statement of which relation patterns an embedding family can and cannot represent.
- [Translating Embeddings for Modeling Multi-relational Data](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) — **Bordes et al. (2013)** — TransE; the reference point every later embedding model is compared against.

**Books**:
- [*Graph Representation Learning*](https://www.cs.mcgill.ca/~wlh/grl_book/) — **William L. Hamilton (McGill)** — free book; shallow embeddings, message passing, and knowledge-graph models derived in one notation.
- [*Knowledge Graphs*](https://kgbook.org/) — **Hogan, Blomqvist, Cochez et al.** — free; the embeddings chapter sits directly beside the schema and ontology chapters, which is the right way to read it.
