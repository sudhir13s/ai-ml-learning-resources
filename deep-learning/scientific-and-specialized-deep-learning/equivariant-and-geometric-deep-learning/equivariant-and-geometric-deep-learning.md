---
id: "deep-learning/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning"
topic: "Equivariant and Geometric Deep Learning"
level: advanced
built_from: ["graph-neural-networks", "cnns-and-convolution"]
leads_to: ["deep-learning/scientific-and-specialized-deep-learning/neural-operators"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Equivariant and Geometric Deep Learning"
minutes: 15
category: scientific-and-specialized-deep-learning
---

# Equivariant and Geometric Deep Learning

> Geometric deep learning is the claim that almost every successful architecture is a **symmetry
> assumption made into a layer**: convolution encodes translation equivariance, a graph network
> encodes permutation equivariance, a recurrent network encodes time-translation. Build the
> symmetry group of your data into the layer — $f(g \cdot x) = g \cdot f(x)$ — and the model stops
> having to learn it from examples.

**Why it matters:** for molecules, proteins, and point clouds the relevant group is $E(3)$
(rotations, translations, reflections in 3D), and an $E(3)$-equivariant network is dramatically
more sample-efficient than an unconstrained one because it never wastes capacity learning that a
rotated molecule is the same molecule. This is the machinery inside AlphaFold's structure module
and inside the machine-learned interatomic potentials (MACE, NequIP) that now do practical
materials simulation. The trade-off interviewers probe: strict equivariance costs throughput, and
at very large data scale an unconstrained model with heavy augmentation can catch up.

**Start here — suggested path:**

1. **Get the unifying frame** — read [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) — **Bronstein, Bruna, Cohen & Veličković (2021)**. *The "5G" proto-book; read the introduction and the blueprint chapter first.*
2. **Watch it taught** — [AMMI Geometric Deep Learning Course (2022)](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **Bronstein, Bruna, Cohen & Veličković**. *Twelve lectures by the book's authors; lecture 2 defines invariance versus equivariance precisely.*
3. **See the first equivariant CNN** — read [Group Equivariant Convolutional Networks](https://arxiv.org/abs/1602.07576) — **Cohen & Welling (2016)**. *Generalises the convolution to arbitrary discrete groups; the paper the field grew from.*
4. **See the practical 3D layer** — read [E(n) Equivariant Graph Neural Networks](https://arxiv.org/abs/2102.09844) — **Satorras, Hoogeboom & Welling (2021)**. *Equivariance without spherical harmonics — simple enough to implement in an afternoon.*
5. **Build with the standard library** — explore [e3nn](https://e3nn.org/) — **e3nn maintainers**. *The Euclidean neural network library that MACE, NequIP and many AlphaFold-adjacent models are built on.*

## Invariance versus equivariance

- **Invariant** — the output does not change when the input is transformed (an energy prediction under rotation).
- **Equivariant** — the output transforms *the same way* as the input (a force vector under rotation).
- **Getting it wrong** is the classic bug: predicting forces with an invariant head silently discards direction.
- **How it is built** — either restrict the filters (group convolution, spherical harmonics / tensor products) or restrict the message function to act only on invariant quantities such as distances.

## Courses (free)

- [Geometric Deep Learning](https://geometricdeeplearning.com/) — **Bronstein, Bruna, Cohen & Veličković** — the course hub: proto-book, slides, lecture links, all free.
- [AMMI Geometric Deep Learning Course (2022)](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **the same four authors** — the full lecture series.
- [Stanford CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Stanford (Jure Leskovec)** — the graph background this material assumes.

## Videos

- [AMMI Geometric Deep Learning Course (2022)](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) — **Michael Bronstein et al.** — the canonical lecture series on symmetry-first architecture design.
- [Stanford CS224W Lecture 1.1 — Why Graphs](https://www.youtube.com/watch?v=JAB_plj2rbA) — **Stanford Online (Jure Leskovec)** — the entry point to the graph half of the story.

## Key Papers

- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) — **Bronstein et al. (2021)** — the unifying blueprint.
- [Group Equivariant Convolutional Networks](https://arxiv.org/abs/1602.07576) — **Cohen & Welling (2016)** — the founding construction.
- [Tensor field networks](https://arxiv.org/abs/1802.08219) — **Thomas et al. (2018)** — rotation- and translation-equivariant networks for 3D point clouds via spherical harmonics.
- [SE(3)-Transformers](https://arxiv.org/abs/2006.10503) — **Fuchs, Worrall, Fischer & Welling (2020)** — equivariant attention; the layer type used in structure prediction.
- [E(n) Equivariant Graph Neural Networks](https://arxiv.org/abs/2102.09844) — **Satorras, Hoogeboom & Welling (2021)** — the cheap, widely used alternative.
- [MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields](https://arxiv.org/abs/2206.07697) — **Batatia et al. (2022)** — the current default machine-learned interatomic potential.
- [Highly accurate protein structure prediction with AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) — **Jumper et al. (DeepMind, 2021)** — the invariant point attention structure module; the field's landmark application.
- [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w) — **Abramson et al. (DeepMind, 2024)** — the diffusion-based successor, and the shift away from strict equivariance.

## Articles / Blogs (free, no paywall)

- [e3nn](https://e3nn.org/) — **e3nn maintainers** — documentation that doubles as a tutorial on irreducible representations and tensor products.
- [Geometric Deep Learning](https://geometricdeeplearning.com/) — **Bronstein et al.** — blog, book and course in one place.
- [Deep Graph Library](https://www.dgl.ai/) — **DGL team** — implementations of several equivariant layers with runnable examples.

## In this platform

- Prerequisites: [Graph Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks) · [CNNs & Convolution](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/cnns-and-convolution/cnns-and-convolution)
- Related in this sub-area: [Neural Operators](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/neural-operators/neural-operators) · [Physics-Informed Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/physics-informed-neural-networks/physics-informed-neural-networks)
- The attention layer these architectures adapt: [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism)
