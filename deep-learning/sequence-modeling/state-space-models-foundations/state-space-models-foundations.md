---
id: "deep-learning/sequence-modeling/state-space-models-foundations"
topic: "State-Space Models — Foundations"
level: advanced
built_from: ["sequence-models-recurrent-convolutional-transformer", "rnn-lstm-gru"]
leads_to: ["deep-learning/sequence-modeling/structured-state-space-models-s4", "deep-learning/sequence-modeling/selective-state-space-models-mamba"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "State-Space Models — Foundations"
minutes: 16
category: sequence-modeling
---

# State-Space Models — Foundations

> A state-space model (SSM) is the control-theory recurrence $x'(t) = Ax(t) + Bu(t)$,
> $y(t) = Cx(t) + Du(t)$, **discretised** into $x_k = \bar{A}x_{k-1} + \bar{B}u_k$ and dropped
> into a neural network as a layer. Because the recurrence is **linear** in the state, it can be
> unrolled into a convolution or computed with a **parallel scan** — so it trains in parallel like
> a transformer while running in constant memory like a recurrent network (RNN).

**Why it matters:** the linearity is the whole trick, and the whole limitation. It buys parallel
training and $O(1)$ decoding state, and it is why **HiPPO** matters: a *randomly* initialised
linear recurrence forgets almost immediately, so the state matrix $A$ must be constructed to
project history onto an orthogonal polynomial basis — that construction, not the layer shape, is
what gives long-range memory. Interviewers probe exactly this: *why is the initialisation of $A$
load-bearing, and what do you lose relative to attention?*

**Start here — suggested path:**

1. **Get the picture before the algebra** — read [On the Tradeoffs of State Space Models and Transformers](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu (2025)**. *The SSM author's own framing: a fixed-size compressed state versus an exact but growing cache.*
2. **See where long memory comes from** — read [HiPPO: Recurrent Memory with Optimal Polynomial Projections](https://arxiv.org/abs/2008.07669) — **Gu, Dao, Ermon, Rudra & Ré (2020)**. *Derives the $A$ matrix as an online projection of the input history onto Legendre polynomials.*
3. **Build one line by line** — work through [The Annotated S4](https://srush.github.io/annotated-s4/) — **Sasha Rush & Sidd Karamcheti**. *A literate JAX implementation: discretisation, the convolutional kernel, and the recurrence, all runnable.*
4. **Hear it from the author** — watch [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)**. *The talk that connects continuous-time systems, HiPPO, and the sequence-model layer.*
5. **Understand the parallel-scan claim** — read [Efficient Parallelization of a Ubiquitous Sequential Computation](https://arxiv.org/abs/2311.06281) — **Heinsen (2023)**. *The associative-scan formulation that makes a first-order linear recurrence $O(\log T)$ deep instead of $O(T)$.*

## The three views of one layer

- **Continuous** — an ordinary differential equation (ODE) over a hidden state; the parameterisation lives here.
- **Recurrent** — after discretisation (zero-order hold or bilinear), a linear RNN with $O(1)$ memory per step; this is the inference view.
- **Convolutional** — unroll the recurrence and the output is a convolution with kernel $\bar{K} = (C\bar{B}, C\bar{A}\bar{B}, C\bar{A}^2\bar{B}, \dots)$; this is the parallel training view.

## Courses (free)

- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar series whose recent editions cover state-space models next to attention, with the researchers themselves.
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Chris Manning)** — the prerequisite sequence-modeling grounding these lectures assume.

## Videos

- [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)** — the primary-author talk on HiPPO, discretisation, and S4.
- [MAMBA and State Space Models explained](https://www.youtube.com/watch?v=vrF3MtGwD0Y) — **AI Coffee Break with Letitia** — a tight visual introduction to the recurrence-versus-convolution duality.
- [MAMBA from Scratch: Neural Nets Better and Faster than Transformers](https://www.youtube.com/watch?v=N6Piou4oYx8) — **Algorithmic Simplicity** — derives the linear-recurrence layer from first principles rather than presenting it as given.

## Key Papers

- [HiPPO: Recurrent Memory with Optimal Polynomial Projections](https://arxiv.org/abs/2008.07669) — **Gu et al. (2020)** — the memory theory; read this before S4 or Mamba make sense.
- [Combining Recurrent, Convolutional, and Continuous-time Models with Linear State-Space Layers](https://arxiv.org/abs/2110.13985) — **Gu et al. (2021)** — the LSSL paper that states the three-views equivalence explicitly.
- [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396) — **Gu, Goel & Ré (2021)** — S4: makes the HiPPO recurrence computationally practical.
- [Simplified State Space Layers for Sequence Modeling](https://arxiv.org/abs/2208.04933) — **Smith, Warrington & Linderman (2022)** — S5 replaces the convolutional kernel with a parallel scan over a multi-input system.
- [Long Range Arena: A Benchmark for Efficient Transformers](https://arxiv.org/abs/2011.04006) — **Tay et al. (2020)** — the benchmark on which SSMs first beat transformers decisively.
- [Efficient Parallelization of a Ubiquitous Sequential Computation](https://arxiv.org/abs/2311.06281) — **Heinsen (2023)** — the clean statement of the associative scan used by every modern SSM kernel.

## Articles / Blogs (free, no paywall)

- [The Annotated S4](https://srush.github.io/annotated-s4/) — **Sasha Rush & Sidd Karamcheti** — literate, runnable, and the fastest way to actually understand discretisation.
- [Structured State Spaces: Combining Continuous-Time, Recurrent, and Convolutional Models](https://hazyresearch.stanford.edu/blog/2022-01-14-s4-3) — **Hazy Research (Stanford)** — the lab's own three-part explainer, written for people who found the paper dense.
- [On the Tradeoffs of State Space Models and Transformers](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu (2025)** — the current, honest account of what a compressed state can and cannot do.
- [Goomba Lab](https://goombalab.github.io/) — **Albert Gu's group (CMU)** — the primary blog where new SSM results are explained before the papers circulate.

## In this platform

- Prerequisites: [Sequence Models — Recurrent, Convolutional, Transformer, State-Space](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/sequence-models-recurrent-convolutional-transformer/sequence-models-recurrent-convolutional-transformer) · [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru)
- Next: [Structured State-Space Models (S4)](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/structured-state-space-models-s4/structured-state-space-models-s4) · [Selective State-Space Models (Mamba)](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/selective-state-space-models-mamba/selective-state-space-models-mamba)
- Why the gradient behaves: [Vanishing / Exploding Gradients](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/vanishing-exploding-gradients/vanishing-exploding-gradients)
