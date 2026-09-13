---
id: "frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks/references"
topic: "Graph Neural Networks — References"
parent: "frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks"
type: references
updated: 2026-09-14
---

# Graph Neural Networks — references

> Companion link library for **[Graph Neural Networks](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Build the intuition interactively** — read [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) — **Sanchez-Lengeling, Reif, Pearce & Wiltschko (Distill)**. *Interactive figures that make "a graph is nodes, edges, and global attributes" concrete before any layer appears.*
2. **See where the convolution comes from** — read [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/) — **Daigavane, Ravindran & Aggarwal (Distill)**. *Connects spectral graph theory to the message-passing layer you actually implement.*
3. **Read the layer that started the modern wave** — [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) — **Kipf & Welling (2016)**, with [the author's own blog post](https://tkipf.github.io/graph-convolutional-networks/). *One renormalised adjacency matmul per layer; everything else is a variation.*
4. **Take the course** — [Stanford CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Stanford (Jure Leskovec)**. *The canonical course: node embeddings, GNN design space, expressivity, scaling.*
5. **Build something** — follow the [PyTorch Geometric documentation](https://pytorch-geometric.readthedocs.io/en/latest/) — **PyG maintainers**. *The introduction-by-example tutorial gets a GCN training on Cora in about thirty lines.*

**In this platform**:
- Applied downstream: [Graph RAG](/ai-ml/practitioner-workflows/llm-applications/graph-rag/graph-rag) · [Spectral Graph Theory](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/spectral-graph-theory/spectral-graph-theory)
- Next in this sub-area: [Neural Operators](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/neural-operators/neural-operators) · [Equivariant and Geometric Deep Learning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning/equivariant-and-geometric-deep-learning)
- Prerequisites: [Perceptron & MLP](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/perceptron-and-mlp/perceptron-and-mlp) · [CNNs & Convolution](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/cnns-and-convolution/cnns-and-convolution)

**Videos**:
- [AMMI Geometric Deep Learning Course (2022)](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **Michael Bronstein** — the symmetry-first derivation, from the author of the book.
- [Stanford CS224W Lecture 1.1 — Why Graphs](https://www.youtube.com/watch?v=JAB_plj2rbA) — **Stanford Online (Jure Leskovec)** — the opening lecture of the full free video course.

**Courses**:
- [AMMI Geometric Deep Learning Course (2022)](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **Michael Bronstein, Joan Bruna, Taco Cohen & Petar Veličković** — twelve lectures deriving GNNs from symmetry rather than from analogy.
- [Geometric Deep Learning](https://geometricdeeplearning.com/) — **Bronstein, Bruna, Cohen & Veličković** — the course hub with the proto-book, slides, and problem sets.
- [Stanford CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Stanford (Jure Leskovec)** — free slides, notes and lecture videos; the reference course for the whole field.

**Articles**:
- [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) — **Distill** — interactive and peer-reviewed; the best first read in the field.
- [Deep Graph Library](https://www.dgl.ai/) — **DGL team** — framework-agnostic implementations and tutorials for every layer named above.
- [Graph Convolutional Networks](https://tkipf.github.io/graph-convolutional-networks/) — **Thomas Kipf** — the GCN author's own explanation, still the clearest short introduction.
- [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/) — **Distill** — the spectral-to-spatial bridge, with playable figures.

**Papers**:
- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) — **Bronstein, Bruna, Cohen & Veličković (2021)** — the "5G" proto-book placing GNNs inside a single symmetry framework.
- [Graph Attention Networks](https://arxiv.org/abs/1710.10903) — **Veličković et al. (2017)** — learned, anisotropic neighbour weights.
- [GraphCast: Learning Skillful Medium-Range Global Weather Forecasting](https://arxiv.org/abs/2212.12794) — **Lam et al. (DeepMind, 2022)** — the flagship applied GNN; a mesh graph over the globe.
- [How Powerful are Graph Neural Networks?](https://arxiv.org/abs/1810.00826) — **Xu, Hu, Leskovec & Jegelka (2018)** — the Weisfeiler-Leman expressivity bound and the GIN layer that attains it.
- [Inductive Representation Learning on Large Graphs](https://arxiv.org/abs/1706.02216) — **Hamilton, Ying & Leskovec (2017)** — GraphSAGE: neighbourhood sampling, the reason GNNs scale to billions of edges.
- [Neural Message Passing for Quantum Chemistry](https://arxiv.org/abs/1704.01212) — **Gilmer et al. (2017)** — unifies prior graph models into the message-passing framework everyone now uses.
- [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) — **Kipf & Welling (2016)** — the GCN layer; the most-implemented graph layer in existence.
