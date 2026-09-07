---
id: "deep-learning/scientific-and-specialized-deep-learning/neural-operators"
topic: "Neural Operators"
level: advanced
built_from: ["physics-informed-neural-networks", "graph-neural-networks"]
leads_to: ["equivariant-and-geometric-deep-learning"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Neural Operators"
minutes: 15
category: scientific-and-specialized-deep-learning
---

# Neural Operators

> A physics-informed neural network learns *one* solution; a **neural operator** learns the
> **solution map itself** — a function between infinite-dimensional function spaces, so one
> trained model answers a whole family of initial conditions in a single forward pass. The
> defining property is **discretisation invariance**: train on a coarse grid, evaluate on a fine
> one, because the learned object is an operator, not a grid-shaped array.

**Why it matters:** this is the architecture behind the 2023–26 machine-learning weather models.
GraphCast produces a 10-day global forecast in under a minute on one tensor processing unit
against hours on a supercomputer for the numerical system, and beats it on the large majority of
verification targets. The Fourier neural operator (FNO) is the key idea to be able to explain: a
global convolution done as a pointwise multiply in the frequency domain, which is what gives an
operator layer a *global* receptive field at $O(N \log N)$ cost.

**Start here — suggested path:**

1. **See the operator idea first** — read [Fourier Neural Operator for Parametric Partial Differential Equations](https://arxiv.org/abs/2010.08895) — **Li, Kovachki, Azizzadenesheli, Liu, Bhattacharya, Stuart & Anandkumar (2020)**. *The FNO layer: lift, Fourier transform, truncate modes, multiply, invert.*
2. **Read the authors' walkthrough** — [Fourier Neural Operator](https://zongyi-li.github.io/blog/2020/fourier-pde/) — **Zongyi Li (Caltech)**. *The first author's own blog post, with animations of Navier-Stokes rollouts.*
3. **See the other formulation** — read [DeepONet: Learning nonlinear operators](https://arxiv.org/abs/1910.03193) — **Lu, Jin & Karniadakis (2019)**. *Branch-and-trunk networks derived from the universal operator approximation theorem — a genuinely different route to the same goal.*
4. **See the 2026 payoff** — read [GraphCast: Learning Skillful Medium-Range Global Weather Forecasting](https://arxiv.org/abs/2212.12794) — **Lam et al. (DeepMind, 2022)**, with the [DeepMind blog post](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/). *An operator-style graph model that beat the operational numerical system.*
5. **Run one** — use the [neuraloperator library](https://neuraloperator.github.io/) — **Caltech / NVIDIA authors**. *The reference PyTorch implementation of FNO and its successors, with pretrained Darcy and Navier-Stokes models.*

## The three families

- **Fourier neural operator (FNO)** — kernel integration as a multiply in Fourier space; best on regular grids and periodic domains.
- **DeepONet** — branch network encodes the input function, trunk network encodes the query location; handles irregular sensors naturally.
- **Graph-based operators** — message passing on a mesh (GraphCast, MeshGraphNets); the right choice when the domain is a sphere or an unstructured mesh.

## Courses (free)

- [neuraloperator documentation and tutorials](https://neuraloperator.github.io/) — **neuraloperator maintainers** — runnable notebooks that take you from a Darcy-flow dataset to a trained FNO.
- [DeepXDE documentation](https://deepxde.readthedocs.io/en/latest/) — **Lu Lu (Yale)** — the DeepONet side, with worked operator-learning demos.
- [Physics Informed Machine Learning](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa) — **Steve Brunton** — the lecture series that situates operator learning inside scientific machine learning.

## Videos

- [Physics Informed Neural Networks (PINNs)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — **Steve Brunton** — the prerequisite lecture; operator learning is introduced as the generalisation.
- [Physics-Informed Neural Networks — An Introduction (Ben Moseley)](https://www.youtube.com/watch?v=G_hIppUWcsc) — **Jousef Murad LITE** — covers when to reach for an operator instead of a PINN.

## Key Papers

- [Fourier Neural Operator for Parametric PDEs](https://arxiv.org/abs/2010.08895) — **Li et al. (2020)** — the most influential operator architecture.
- [Neural Operator: Learning Maps Between Function Spaces](https://arxiv.org/abs/2108.08481) — **Kovachki et al. (2021)** — the general theory, including the discretisation-invariance and universal-approximation results.
- [DeepONet](https://arxiv.org/abs/1910.03193) — **Lu, Jin & Karniadakis (2019)** — the branch-trunk operator network.
- [GraphCast](https://arxiv.org/abs/2212.12794) — **Lam et al. (DeepMind, 2022)** — mesh graph neural operator; the model that changed operational weather forecasting.
- [FourCastNet](https://arxiv.org/abs/2202.11214) — **Pathak et al. (NVIDIA, 2022)** — adaptive FNO at 0.25° resolution; a week-long forecast in seconds.
- [GenCast: Diffusion-based ensemble forecasting for medium-range weather](https://arxiv.org/abs/2312.15796) — **Price et al. (DeepMind, 2023)** — the probabilistic successor; where operator learning meets diffusion models.

## Articles / Blogs (free, no paywall)

- [Fourier Neural Operator](https://zongyi-li.github.io/blog/2020/fourier-pde/) — **Zongyi Li** — the first author's explanation, the best free FNO writeup.
- [GraphCast: AI model for faster and more accurate global weather forecasting](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/) — **Google DeepMind** — the primary announcement, with the verification numbers.
- [CRUNCH group](https://www.brown.edu/research/projects/crunch/) — **George Karniadakis (Brown University)** — the DeepONet group's own research index.

## In this platform

- Prerequisites: [Physics-Informed Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/physics-informed-neural-networks/physics-informed-neural-networks) · [Graph Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks)
- Next: [Equivariant and Geometric Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning/equivariant-and-geometric-deep-learning)
- The generative machinery GenCast reuses: [Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm)
