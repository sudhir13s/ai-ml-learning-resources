---
id: "deep-learning/sequence-modeling/structured-state-space-models-s4"
topic: "Structured State-Space Models — S4, S4D, Diagonal SSMs"
level: advanced
built_from: ["state-space-models-foundations"]
leads_to: ["deep-learning/sequence-modeling/selective-state-space-models-mamba"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Structured State-Space Models — S4, S4D, Diagonal SSMs"
minutes: 15
category: sequence-modeling
---

# Structured State-Space Models — S4, S4D, Diagonal SSMs

> S4 makes the HiPPO state-space recurrence *computable*. A naive linear state-space model (SSM)
> layer needs repeated powers of an $N \times N$ state matrix — $O(N^2 T)$ work and $O(N^2)$ memory
> per layer. S4 imposes **structure** on $A$ (a normal-plus-low-rank decomposition, later just a
> **diagonal** matrix) so the whole convolutional kernel can be evaluated in the frequency domain
> in $O((N + T)\log(N + T))$.

**Why it matters:** S4 was the first architecture to solve Path-X on Long Range Arena, a 16k-token
task every transformer variant had failed, and it is the direct ancestor of Mamba. The engineering
lesson generalises: **the parameterisation of $A$ decides both memory and speed**, and S4D showed
that a diagonal matrix initialised from the HiPPO eigenvalues recovers nearly all of S4's quality
with a fraction of the complexity. Interviewers ask why a *diagonal* recurrence is not simply an
exponentially decaying filter — the answer is that the eigenvalues are complex, so each channel is
a damped oscillator at its own frequency.

**Start here — suggested path:**

1. **Read the implementation before the paper** — work through [The Annotated S4](https://srush.github.io/annotated-s4/) — **Sasha Rush & Sidd Karamcheti**. *Discretisation, the kernel, the diagonal-plus-low-rank trick, all as running code.*
2. **Then read the paper** — [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396) — **Gu, Goel & Ré (2021)**. *The Cauchy-kernel argument that turns the matrix power series into an $O((N+T)\log(N+T))$ computation.*
3. **See the simplification that stuck** — read [On the Parameterization and Initialization of Diagonal State Space Models](https://arxiv.org/abs/2206.11893) — **Gu, Gupta, Goel & Ré (2022)**. *S4D: keep only the diagonal, keep the HiPPO-derived initialisation, keep the accuracy.*
4. **Watch the walkthrough** — [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)**. *The author's framing of why structure, not depth, was the bottleneck.*
5. **Run the reference code** — browse [state-spaces/s4](https://github.com/state-spaces/s4) — **Albert Gu et al.** *The official implementation with S4, S4D, and the LRA training configs.*

## What "structured" buys you

- **Normal-plus-low-rank $A$** — lets the kernel be computed by a Cauchy matrix-vector product instead of a matrix power series.
- **Diagonal $A$ (S4D, DSS)** — complex eigenvalues $\lambda_n = -\tfrac{1}{2} + i\pi n$; each state channel becomes a damped oscillator, and the kernel is a Vandermonde product.
- **HiPPO initialisation** — the eigenvalue placement, not the training, is what supplies long-range memory; random initialisation collapses the effective context.

## Courses (free)

- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — seminar lectures covering S4 and its successors from the authors.
- [Dive into Deep Learning](https://d2l.ai/chapter_recurrent-neural-networks/index.html) — **Zhang, Lipton, Li & Smola** — the recurrent-network background S4 assumes, with code.

## Videos

- [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)** — the definitive author talk on S4.
- [MAMBA from Scratch: Neural Nets Better and Faster than Transformers](https://www.youtube.com/watch?v=N6Piou4oYx8) — **Algorithmic Simplicity** — derives the diagonal linear recurrence and shows why the frequency-domain kernel works.

## Key Papers

- [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396) — **Gu, Goel & Ré (2021)** — S4 itself; the first model to solve Path-X.
- [On the Parameterization and Initialization of Diagonal State Space Models](https://arxiv.org/abs/2206.11893) — **Gu, Gupta, Goel & Ré (2022)** — S4D, the simplification that every later SSM inherits.
- [Diagonal State Spaces are as Effective as Structured State Spaces](https://arxiv.org/abs/2203.14343) — **Gupta, Gu & Berant (2022)** — the independent result that diagonal is enough.
- [Hungry Hungry Hippos: Towards Language Modeling with State Space Models](https://arxiv.org/abs/2212.14052) — **Fu et al. (2022)** — H3 diagnoses *why* SSMs underperformed on language (associative recall) and adds the missing multiplicative interaction.
- [It's Raw! Audio Generation with State-Space Models](https://arxiv.org/abs/2202.09729) — **Goel, Gu, Donahue & Ré (2022)** — SaShiMi: S4 on raw waveforms, the clearest non-language demonstration of long-range memory.
- [Simplified State Space Layers for Sequence Modeling](https://arxiv.org/abs/2208.04933) — **Smith, Warrington & Linderman (2022)** — S5's parallel-scan formulation, the bridge to Mamba's kernel.

## Articles / Blogs (free, no paywall)

- [The Annotated S4](https://srush.github.io/annotated-s4/) — **Sasha Rush & Sidd Karamcheti** — the single best S4 resource in existence; literate code you can execute.
- [Structured State Spaces for Sequence Modeling (blog series)](https://hazyresearch.stanford.edu/blog/2022-01-14-s4-3) — **Hazy Research (Stanford)** — the authoring lab's own explainer, with the intuition the paper compresses away.
- [Goomba Lab](https://goombalab.github.io/) — **Albert Gu's group (CMU)** — ongoing primary commentary on the S4 lineage.

## In this platform

- Prerequisite: [State-Space Models — Foundations](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/state-space-models-foundations/state-space-models-foundations)
- Next: [Selective State-Space Models (Mamba)](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/selective-state-space-models-mamba/selective-state-space-models-mamba)
- Compare against attention: [Efficient Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention) · [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture)
