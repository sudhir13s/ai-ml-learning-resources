---
id: "models-and-architectures/classic-architectures/selective-state-space-models-mamba"
topic: "Selective State-Space Models — Mamba and Mamba-2"
level: advanced
built_from: ["structured-state-space-models-s4", "state-space-models-foundations"]
leads_to: ["models-and-architectures/classic-architectures/linear-and-hybrid-attention-architectures"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Selective State-Space Models — Mamba and Mamba-2"
minutes: 16
category: classic-architectures
---

# Selective State-Space Models — Mamba and Mamba-2

> Mamba makes the state-space model (SSM) parameters $\bar{B}$, $\bar{C}$ and the step size
> $\Delta$ **functions of the input token**. That one change — *selection* — lets the layer decide
> per token what to write into the state and what to forget, which is exactly the content-based
> routing a fixed convolutional kernel cannot do. The cost is that the layer is no longer a
> convolution, so Mamba replaces the fast Fourier transform kernel with a **hardware-aware
> parallel scan** that keeps the expanded state in static random-access memory (SRAM).

**Why it matters:** Mamba is the first non-attention architecture to match transformers on
language at scale, and Mamba-2's **state-space duality (SSD)** proved that a large class of
attention variants and SSMs are the *same* computation viewed through different decompositions of
a structured semiseparable matrix. In 2026 the practical descendants are hybrid stacks, not pure
Mamba — the honest trade-off is that a fixed-size state gives $O(1)$ decoding but loses exact
long-range retrieval, which is why production models interleave a few full-attention layers.

**Start here — suggested path:**

1. **Get the one-sentence idea** — read [On the Tradeoffs of State Space Models and Transformers](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu (2025)**. *Selection as "compress with judgement" versus attention's "keep everything".*
2. **Watch a careful derivation** — [Mamba and S4 Explained: Architecture, Parallel Scan, Kernel Fusion, Recurrent, Convolution, Math](https://www.youtube.com/watch?v=8Q_tqwpTpVU) — **Umar Jamil**. *Two hours that build the whole layer including the scan and the fused kernel.*
3. **Read the paper** — [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)**. *Selection, the selective-scan algorithm, and the Mamba block.*
4. **See the theory that unified it** — read [Transformers are SSMs (Mamba-2)](https://arxiv.org/abs/2405.21060) — **Dao & Gu (2024)**. *The SSD framework, and the 2–8× faster core layer it produced.*
5. **Read the reference implementation** — browse [state-spaces/mamba](https://github.com/state-spaces/mamba) — **Gu & Dao**. *The selective-scan CUDA kernel is where the paper's memory argument becomes real.*

## What selection changes

- **Input-dependent $\Delta$** — a large step size resets the state (attend to the new token), a small one holds it (ignore the token); this is a learned gate in disguise.
- **No convolutional form** — time-varying parameters break the single-kernel unroll, hence the scan.
- **Hardware-aware scan** — the $N$-times-expanded state is materialised only in SRAM and recomputed in the backward pass, the same input/output-aware idea as FlashAttention.
- **Mamba-2 / SSD** — restricts $A$ to a scalar times identity, which turns the layer into a structured masked-attention matmul that maps onto tensor cores.

## Courses (free)

- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar where the Mamba authors present the tradeoffs argument directly.
- [MIT 6.S191: Introduction to Deep Learning](https://introtodeeplearning.com/) — **MIT (Alexander Amini et al.)** — the current sequence-modeling lecture places Mamba beside transformers for beginners.

## Videos

- [Mamba and S4 Explained: Architecture, Parallel Scan, Kernel Fusion, Recurrent, Convolution, Math](https://www.youtube.com/watch?v=8Q_tqwpTpVU) — **Umar Jamil** — the most complete free walkthrough, math and kernel included.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces (Paper Explained)](https://www.youtube.com/watch?v=9dSkvxS2EB0) — **Yannic Kilcher** — a critical reading that separates the claims from the evidence.
- [MAMBA from Scratch: Neural Nets Better and Faster than Transformers](https://www.youtube.com/watch?v=N6Piou4oYx8) — **Algorithmic Simplicity** — derives the architecture rather than describing it.
- [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)** — the S4 background talk Mamba builds on.

## Key Papers

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)** — selection plus the hardware-aware selective scan.
- [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/abs/2405.21060) — **Dao & Gu (2024)** — Mamba-2 and the duality result; the deepest paper in this lineage.
- [Hungry Hungry Hippos: Towards Language Modeling with State Space Models](https://arxiv.org/abs/2212.14052) — **Fu et al. (2022)** — the associative-recall diagnosis that motivated selection.
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887) — **Lieber et al. (AI21, 2024)** — the first large hybrid, and the clearest evidence that a few attention layers are still needed.
- [Efficient Parallelization of a Ubiquitous Sequential Computation](https://arxiv.org/abs/2311.06281) — **Heinsen (2023)** — the associative scan underpinning the kernel.

## Articles / Blogs (free, no paywall)

- [Mamba: The Hard Way](https://srush.github.io/annotated-mamba/hard.html) — **Sasha Rush** — a from-scratch Triton implementation of the selective scan that reproduces the CUDA results.
- [State Space Duality (Mamba-2)](https://goombalab.github.io/blog/2024/mamba2-part1-model/) — **Albert Gu & Tri Dao (2024)** — the authors' own multi-part explanation of SSD, far more readable than the paper.
- [On the Tradeoffs of State Space Models and Transformers](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu (2025)** — the 2025 statement of where SSMs win and where they do not.
- [state-spaces/mamba](https://github.com/state-spaces/mamba) — **Gu & Dao** — reference implementation, kernels, and pretrained checkpoints.

## In this platform

- Prerequisites: [Structured State-Space Models (S4)](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/structured-state-space-models-s4/structured-state-space-models-s4) · [State-Space Models — Foundations](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/state-space-models-foundations/state-space-models-foundations)
- Next: [Linear and Hybrid Attention Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/linear-and-hybrid-attention-architectures/linear-and-hybrid-attention-architectures)
- The systems comparison: [Efficient Attention](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention) · [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) · [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures)
- The gating idea behind selection: [Gating Mechanisms](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/gating-mechanisms/gating-mechanisms)
