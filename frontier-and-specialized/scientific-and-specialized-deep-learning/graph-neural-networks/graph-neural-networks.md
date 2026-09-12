---
id: "frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks"
topic: "Graph Neural Networks"
level: intermediate
built_from: ["perceptron-and-mlp", "cnns-and-convolution"]
leads_to: ["frontier-and-specialized/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning", "frontier-and-specialized/scientific-and-specialized-deep-learning/neural-operators"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Graph Neural Networks"
minutes: 16
category: scientific-and-specialized-deep-learning
---

# Graph Neural Networks

> A graph neural network (GNN) generalises convolution from a grid to an arbitrary graph: each
> node repeatedly **aggregates messages from its neighbours** and updates its own vector. After
> $k$ rounds every node's representation summarises its $k$-hop neighbourhood, and the whole
> thing is permutation-equivariant by construction because the aggregator is a sum, mean, or max.

**Why it matters:** GNNs are the workhorse behind molecular property prediction, recommendation
graphs, traffic forecasting, and — most visibly in 2026 — DeepMind's GraphCast weather model.
The interview question is almost always **expressivity**: standard message passing is at most as
powerful as the 1-dimensional Weisfeiler-Leman graph isomorphism test, so it cannot distinguish
some structurally different graphs; and **over-smoothing**, where stacking too many rounds makes
every node vector converge to the same value.

**Start here — suggested path:**

1. **Build the intuition interactively** — read [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) — **Sanchez-Lengeling, Reif, Pearce & Wiltschko (Distill)**. *Interactive figures that make "a graph is nodes, edges, and global attributes" concrete before any layer appears.*
2. **See where the convolution comes from** — read [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/) — **Daigavane, Ravindran & Aggarwal (Distill)**. *Connects spectral graph theory to the message-passing layer you actually implement.*
3. **Read the layer that started the modern wave** — [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) — **Kipf & Welling (2016)**, with [the author's own blog post](https://tkipf.github.io/graph-convolutional-networks/). *One renormalised adjacency matmul per layer; everything else is a variation.*
4. **Take the course** — [Stanford CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Stanford (Jure Leskovec)**. *The canonical course: node embeddings, GNN design space, expressivity, scaling.*
5. **Build something** — follow the [PyTorch Geometric documentation](https://pytorch-geometric.readthedocs.io/en/latest/) — **PyG maintainers**. *The introduction-by-example tutorial gets a GCN training on Cora in about thirty lines.*

## The design space in one screen

- **Message** — what a neighbour sends (its vector, optionally edge features).
- **Aggregate** — sum (most expressive), mean (degree-invariant), max (structure-selective), or attention-weighted (GAT).
- **Update** — how the node combines its own state with the aggregate; a multilayer perceptron (MLP) here is what makes GIN maximally expressive.
- **Readout** — node-level, edge-level, or graph-level pooling, chosen by the task.

## Courses (free)

- [Stanford CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Stanford (Jure Leskovec)** — free slides, notes and lecture videos; the reference course for the whole field.
- [AMMI Geometric Deep Learning Course (2022)](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **Michael Bronstein, Joan Bruna, Taco Cohen & Petar Veličković** — twelve lectures deriving GNNs from symmetry rather than from analogy.
- [Geometric Deep Learning](https://geometricdeeplearning.com/) — **Bronstein, Bruna, Cohen & Veličković** — the course hub with the proto-book, slides, and problem sets.

## Videos

- [Stanford CS224W Lecture 1.1 — Why Graphs](https://www.youtube.com/watch?v=JAB_plj2rbA) — **Stanford Online (Jure Leskovec)** — the opening lecture of the full free video course.
- [AMMI Geometric Deep Learning Course (2022)](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **Michael Bronstein** — the symmetry-first derivation, from the author of the book.

## Key Papers

- [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) — **Kipf & Welling (2016)** — the GCN layer; the most-implemented graph layer in existence.
- [Neural Message Passing for Quantum Chemistry](https://arxiv.org/abs/1704.01212) — **Gilmer et al. (2017)** — unifies prior graph models into the message-passing framework everyone now uses.
- [Inductive Representation Learning on Large Graphs](https://arxiv.org/abs/1706.02216) — **Hamilton, Ying & Leskovec (2017)** — GraphSAGE: neighbourhood sampling, the reason GNNs scale to billions of edges.
- [Graph Attention Networks](https://arxiv.org/abs/1710.10903) — **Veličković et al. (2017)** — learned, anisotropic neighbour weights.
- [How Powerful are Graph Neural Networks?](https://arxiv.org/abs/1810.00826) — **Xu, Hu, Leskovec & Jegelka (2018)** — the Weisfeiler-Leman expressivity bound and the GIN layer that attains it.
- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) — **Bronstein, Bruna, Cohen & Veličković (2021)** — the "5G" proto-book placing GNNs inside a single symmetry framework.
- [GraphCast: Learning Skillful Medium-Range Global Weather Forecasting](https://arxiv.org/abs/2212.12794) — **Lam et al. (DeepMind, 2022)** — the flagship applied GNN; a mesh graph over the globe.

## Articles / Blogs (free, no paywall)

- [Graph Convolutional Networks](https://tkipf.github.io/graph-convolutional-networks/) — **Thomas Kipf** — the GCN author's own explanation, still the clearest short introduction.
- [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) — **Distill** — interactive and peer-reviewed; the best first read in the field.
- [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/) — **Distill** — the spectral-to-spatial bridge, with playable figures.
- [Deep Graph Library](https://www.dgl.ai/) — **DGL team** — framework-agnostic implementations and tutorials for every layer named above.

## In this platform

- Prerequisites: [Perceptron & MLP](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/perceptron-and-mlp/perceptron-and-mlp) · [CNNs & Convolution](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/cnns-and-convolution/cnns-and-convolution)
- Next in this sub-area: [Neural Operators](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/neural-operators/neural-operators) · [Equivariant and Geometric Deep Learning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning/equivariant-and-geometric-deep-learning)
- Applied downstream: [Graph RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/graph-rag/graph-rag) · [Spectral Graph Theory](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/spectral-graph-theory/spectral-graph-theory)
