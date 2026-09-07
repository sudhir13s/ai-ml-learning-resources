---
id: "deep-learning/sequence-modeling/linear-and-hybrid-attention-architectures"
topic: "Linear and Hybrid Attention Architectures"
level: advanced
built_from: ["selective-state-space-models-mamba", "attention-mechanism"]
leads_to: ["09-llms/efficient-attention-flashattention"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Linear and Hybrid Attention Architectures"
minutes: 16
category: sequence-modeling
---

# Linear and Hybrid Attention Architectures

> Drop the softmax and attention becomes associative: $(\phi(Q)\phi(K)^\top)V = \phi(Q)(\phi(K)^\top V)$,
> so the $T \times T$ score matrix never has to exist and the layer collapses into a **recurrent
> update of a fixed-size matrix-valued state**. Every "linear attention" model — Performer, RetNet,
> RWKV, DeltaNet — is a different choice of feature map, decay rule, and state-update rule for that
> same recurrence, which is why the 2024–26 literature treats them and state-space models (SSMs)
> as one family.

**Why it matters:** the 2026 production answer is not "linear instead of attention" but **hybrid**:
Jamba, Zamba2, Nemotron-H and Qwen3-Next interleave a minority of full-attention layers (typically
1-in-4 to 1-in-8) with a majority of linear or SSM layers, because the linear layers give
$O(1)$-per-token decoding and the few softmax layers restore exact retrieval. The interview trap is
assuming linear attention is strictly worse — the modern **delta rule** variants fixed the
"unbounded state, no forgetting" problem that sank the 2020 generation.

**Start here — suggested path:**

1. **See the algebra that removes the quadratic term** — read [Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention](https://arxiv.org/abs/2006.16236) — **Katharopoulos, Vyas, Pappas & Fleuret (2020)**. *The associativity trick and the recurrent form, in six pages.*
2. **See the decay generation** — read [Retentive Network: A Successor to Transformer for Large Language Models](https://arxiv.org/abs/2307.08621) — **Sun et al. (Microsoft, 2023)**. *Parallel, recurrent, and chunkwise-recurrent forms of one layer — the template everyone copied.*
3. **Understand the fix that made them competitive** — read [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464) — **Yang, Kautz & Hatamizadeh (NVIDIA, 2024)**. *Error-correcting state updates plus a decay gate; the layer inside Qwen3-Next.*
4. **See how 2026 models actually stack them** — read [vLLM Now Supports Qwen3-Next: Hybrid Architecture with Extreme Efficiency](https://blog.vllm.ai/2025/09/11/qwen3-next.html) — **vLLM team (2025)**. *A serving-side account of a 3:1 Gated-DeltaNet-to-attention stack with real numbers.*
5. **Compare the design space** — read [Hybrid Attention](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/) — **Sebastian Raschka**. *A side-by-side gallery of how current open models mix the two layer types.*

## The design space in four choices

- **Feature map $\phi$** — elu+1 (linear attention), random features (Performer), low-rank projection (Linformer), or none at all with an explicit decay (RetNet, RWKV).
- **Forgetting** — no decay (state grows stale), scalar decay (RetNet), data-dependent gate (Mamba, Gated DeltaNet).
- **State update** — additive outer product $S \mathrel{+}= k v^\top$ versus the **delta rule**, which first *removes* the value currently stored at that key.
- **Stacking** — pure linear, or hybrid with a minority of full-attention layers for retrieval.

## Courses (free)

- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar covering efficient-attention and SSM variants from the researchers who built them.
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Chris Manning)** — the attention grounding these variants modify.

## Videos

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces (Paper Explained)](https://www.youtube.com/watch?v=9dSkvxS2EB0) — **Yannic Kilcher** — includes the clearest verbal account of why linear attention and SSMs are the same object.
- [Mamba and S4 Explained](https://www.youtube.com/watch?v=8Q_tqwpTpVU) — **Umar Jamil** — the recurrent/chunkwise duality worked through in detail.
- [MAMBA from Scratch](https://www.youtube.com/watch?v=N6Piou4oYx8) — **Algorithmic Simplicity** — derives the linear recurrence that every model on this page is a variation of.

## Key Papers

- [Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention](https://arxiv.org/abs/2006.16236) — **Katharopoulos et al. (2020)** — the founding result of the family.
- [Rethinking Attention with Performers](https://arxiv.org/abs/2009.14794) — **Choromanski et al. (2020)** — unbiased softmax approximation via positive random features.
- [Linformer: Self-Attention with Linear Complexity](https://arxiv.org/abs/2006.04768) — **Wang et al. (2020)** — the low-rank projection baseline, useful mainly as a contrast.
- [Retentive Network](https://arxiv.org/abs/2307.08621) — **Sun et al. (2023)** — the "impossible triangle" framing: parallel training, cheap inference, good performance.
- [RWKV: Reinventing RNNs for the Transformer Era](https://arxiv.org/abs/2305.13048) — **Peng et al. (2023)** — a community-built linear-attention LLM with a genuinely recurrent formulation.
- [Parallelizing Linear Transformers with the Delta Rule over Sequence Length](https://arxiv.org/abs/2406.06484) — **Yang, Wang, Zhang & Kim (2024)** — makes DeltaNet trainable at scale with a chunkwise algorithm.
- [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464) — **Yang, Kautz & Hatamizadeh (2024)** — decay gate plus delta rule; the current strong default.
- [Griffin: Mixing Gated Linear Recurrences with Local Attention](https://arxiv.org/abs/2402.19427) — **De et al. (Google DeepMind, 2024)** — the RG-LRU hybrid that matched Llama-2 at 6B.
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887) — **Lieber et al. (AI21, 2024)** — the first production hybrid with published ablations on the mixing ratio.
- [Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models](https://arxiv.org/abs/2504.03624) — **NVIDIA (2025)** — a 2025 hybrid family with throughput measurements at 8B–56B.
- [The Zamba2 Suite](https://arxiv.org/abs/2411.15242) — **Glorioso et al. (Zyphra, 2024)** — shared-attention hybrid designed for on-device inference.

## Articles / Blogs (free, no paywall)

- [vLLM Now Supports Qwen3-Next](https://blog.vllm.ai/2025/09/11/qwen3-next.html) — **vLLM team (2025)** — how a hybrid stack is actually served, including the state-cache changes it forces.
- [Hybrid Attention](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/) — **Sebastian Raschka** — the clearest comparative gallery of 2025–26 hybrid designs.
- [State Space Duality (Mamba-2)](https://goombalab.github.io/blog/2024/mamba2-part1-model/) — **Albert Gu & Tri Dao** — the theory that makes "linear attention" and "SSM" interchangeable terms.
- [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) — **fla-org** — Triton kernels for every layer named on this page; the fastest way to read them side by side.

## In this platform

- Prerequisites: [Selective State-Space Models (Mamba)](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/selective-state-space-models-mamba/selective-state-space-models-mamba) · [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism)
- Exact-attention systems work lives here: [Efficient Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention)
- The LLM-scale attention variants — grouped-query attention (GQA), multi-head latent attention (MLA) and sliding-window attention — are owned by [Attention Architectures: GQA, MLA, Sliding and Linear](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear); this page owns the linear and state-space side of that story.
- Also related: [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures) · [Mixture of Experts](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/mixture-of-experts/mixture-of-experts)
