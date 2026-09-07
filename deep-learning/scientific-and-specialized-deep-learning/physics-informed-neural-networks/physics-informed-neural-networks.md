---
id: "deep-learning/scientific-and-specialized-deep-learning/physics-informed-neural-networks"
topic: "Physics-Informed Neural Networks"
level: advanced
built_from: ["backpropagation-and-computational-graphs", "loss-functions"]
leads_to: ["neural-operators"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Physics-Informed Neural Networks"
minutes: 14
category: scientific-and-specialized-deep-learning
---

# Physics-Informed Neural Networks

> A physics-informed neural network (PINN) is a plain multilayer perceptron $u_\theta(x, t)$ whose
> loss contains the **residual of a partial differential equation (PDE)**, evaluated by automatic
> differentiation at randomly sampled collocation points. Minimising
> $\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda\mathcal{L}_{\text{PDE}} + \mathcal{L}_{\text{BC/IC}}$
> makes the network satisfy the physics where you have no data at all.

**Why it matters:** PINNs are mesh-free, handle inverse problems (recovering an unknown
coefficient from sparse measurements) almost for free, and need far less data than a black-box
surrogate — that combination is why they took over scientific machine learning. The honest 2026
picture is equally important: PINNs are **not** faster than a good classical solver on a
well-posed forward problem, and they fail in characteristic ways — stiff or convection-dominated
PDEs create a loss landscape the optimiser cannot traverse, and the gradients of the data and
residual terms routinely differ by orders of magnitude, so $\lambda$ has to be balanced adaptively.

**Start here — suggested path:**

1. **Get the idea in one sitting** — read [So, what is a physics-informed neural network?](https://benmoseley.blog/my-research/so-what-is-a-physics-informed-neural-network/) — **Ben Moseley**. *Builds a PINN for the damped harmonic oscillator with figures at each step.*
2. **Watch the derivation** — [Physics Informed Neural Networks (PINNs)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — **Steve Brunton (University of Washington)**. *Where the residual term comes from and what automatic differentiation is doing inside it.*
3. **Read the founding papers** — [Physics Informed Deep Learning (Part I)](https://arxiv.org/abs/1711.10561) and [(Part II)](https://arxiv.org/abs/1711.10566) — **Raissi, Perdikaris & Karniadakis (2017)**. *Forward solutions and inverse discovery, the two halves of the original method.*
4. **Learn the failure modes before you build** — read [Characterizing possible failure modes in physics-informed neural networks](https://arxiv.org/abs/2109.01050) — **Krishnapriyan et al. (2021)**. *Why a PINN that "should" work returns a smooth, wrong answer.*
5. **Build with a real library** — follow the [DeepXDE documentation](https://deepxde.readthedocs.io/en/latest/) — **Lu Lu (Yale)**. *The reference PINN/DeepONet library, with a worked Burgers equation example.*

## The loss, term by term

- **Data term** — supervised fit at whatever measurements exist; can be empty.
- **Residual term** — the PDE evaluated at collocation points, with derivatives from automatic differentiation, not finite differences.
- **Boundary and initial terms** — either penalised, or imposed exactly by construction (a "hard constraint" ansatz, usually more stable).
- **Weighting $\lambda$** — the single most important hyperparameter; adaptive schemes based on gradient statistics are now standard.

## Courses (free)

- [Physics Informed Machine Learning](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa) — **Steve Brunton (University of Washington)** — a full free lecture series on embedding physics into each stage of the ML pipeline.
- [DeepXDE documentation and demos](https://deepxde.readthedocs.io/en/latest/) — **Lu Lu** — the closest thing to a hands-on course; every demo is a runnable PDE.

## Videos

- [Physics Informed Neural Networks (PINNs)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — **Steve Brunton** — the clearest short explanation of the residual loss.
- [Physics-Informed Neural Networks — An Introduction (Ben Moseley)](https://www.youtube.com/watch?v=G_hIppUWcsc) — **Jousef Murad LITE** — a long-form interview-lecture with a PINN researcher, including where they do not work.

## Key Papers

- [Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear PDEs](https://arxiv.org/abs/1711.10561) — **Raissi, Perdikaris & Karniadakis (2017)** — the forward problem.
- [Physics Informed Deep Learning (Part II): Data-driven Discovery of Nonlinear PDEs](https://arxiv.org/abs/1711.10566) — **Raissi, Perdikaris & Karniadakis (2017)** — the inverse problem, where PINNs are genuinely hard to beat.
- [Physics-informed machine learning](https://www.nature.com/articles/s42254-021-00314-5) — **Karniadakis et al. (Nature Reviews Physics, 2021)** — the field-defining review; the reference for how physics enters a model.
- [Characterizing possible failure modes in physics-informed neural networks](https://arxiv.org/abs/2109.01050) — **Krishnapriyan, Gholami, Zhe, Kirby & Mahoney (2021)** — the optimisation-pathology analysis every practitioner should read.
- [Scientific Machine Learning through Physics-Informed Neural Networks: Where we are and What's next](https://arxiv.org/abs/2201.05624) — **Cuomo et al. (2022)** — a broad survey of variants and applications.

## Articles / Blogs (free, no paywall)

- [So, what is a physics-informed neural network?](https://benmoseley.blog/my-research/so-what-is-a-physics-informed-neural-network/) — **Ben Moseley** — the best free tutorial, with complete code.
- [PINNs reference implementation](https://github.com/maziarraissi/PINNs) — **Maziar Raissi** — the original authors' code for both papers.
- [CRUNCH group](https://www.brown.edu/research/projects/crunch/) — **George Karniadakis (Brown University)** — the lab page that tracks the PINN and neural-operator literature at source.
- [NVIDIA PhysicsNeMo (formerly Modulus)](https://developer.nvidia.com/modulus) — **NVIDIA** — the production framework, useful for seeing what industrial-scale PINN training requires.

## In this platform

- Prerequisites: [Backpropagation & Computational Graphs](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/backpropagation-and-computational-graphs/backpropagation-and-computational-graphs) · [Loss Functions](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/loss-functions/loss-functions)
- Next: [Neural Operators](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/neural-operators/neural-operators) — learn the solution operator instead of one solution.
- Why the loss balance matters: [Optimizers](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers) · [Vanishing / Exploding Gradients](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/vanishing-exploding-gradients/vanishing-exploding-gradients)
