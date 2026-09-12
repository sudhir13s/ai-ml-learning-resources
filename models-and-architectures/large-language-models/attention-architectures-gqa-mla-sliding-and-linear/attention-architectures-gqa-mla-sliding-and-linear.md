---
id: "models-and-architectures/large-language-models/attention-architectures-gqa-mla-sliding-and-linear"
topic: "Attention Architectures — GQA, MLA, Sliding-Window and Linear"
level: advanced
built_from: ["attention-mechanism", "efficient-attention", "kv-cache-variants"]
leads_to: ["09-llms/long-context-methods", "09-llms/mixture-of-experts"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Attention Architectures — GQA, MLA, Sliding-Window and Linear"
minutes: 18
category: large-language-models
---

# Attention Architectures — GQA, MLA, Sliding-Window and Linear

> Every frontier model since 2023 has redesigned its attention block, and always for the same
> reason: exact multi-head attention costs O(T²) compute and an O(T) cache per layer. The design
> space has four moves — **share** key/value heads (multi-query attention (MQA), grouped-query
> attention (GQA)), **compress** them (multi-head latent attention (MLA)), **restrict** what each
> token sees (sliding-window, sparse), or **replace** attention in some layers with a recurrent or
> linear operator (Mamba, gated linear attention).

**Why it matters:** naming the attention variant a model uses — and why — is the fastest way to show
you read architectures rather than headlines.

- **What is probed:** the MQA → GQA → MLA progression and exactly what each trades (quality versus cache bytes); why sliding-window attention still has a global receptive field across layers; what a hybrid stack (a few full-attention layers among many linear/state-space layers) buys and costs.
- **The 2025 turn:** *trainable* sparse attention. DeepSeek's native sparse attention (NSA) and Moonshot's mixture of block attention (MoBA) make the sparsity pattern part of training rather than an inference-time hack — the first sparse designs that hold quality at scale.
- **The boundary to respect:** the cache *mechanics* of these variants (bytes per token, what MLA actually stores) belong to the KV Cache Variants page; the *kernel* that makes exact attention fast belongs to the FlashAttention page. This page is the architecture map.

**Start here — suggested path:**

1. **See the whole 2025 design space at once** — read [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka**. *DeepSeek-V3, Llama, Gemma 3, Qwen3, gpt-oss and more, block by block, with the attention choice highlighted in each.*
2. **Read the head-sharing line** — read [Fast Transformer Decoding (MQA)](https://arxiv.org/abs/1911.02150) — **Shazeer (2019)** and [GQA](https://arxiv.org/abs/2305.13245) — **Ainslie et al. (2023)**. *One write-head, then the interpolation everybody actually ships.*
3. **Read the compression line** — read [DeepSeek-V2](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)**, §2.1. *MLA projects keys and values into a shared low-rank latent that is what gets cached; the cleanest description is in the paper itself.*
4. **See windows and hybrids in shipped models** — watch [Mistral / Mixtral Explained](https://www.youtube.com/watch?v=UiX8K-xBUpE) — **Umar Jamil**, then read [Jamba](https://arxiv.org/abs/2403.19887) — **Lieber et al. (2024)**. *Sliding-window with a rolling buffer, then a Transformer–Mamba hybrid stack.*
5. **Read the 2025 sparse-attention turn** — read [Native Sparse Attention](https://arxiv.org/abs/2502.11089) — **Yuan et al. (2025)** and [MoBA](https://arxiv.org/abs/2502.13189) — **Lu et al. (2025)**. *Hardware-aligned, natively trainable sparsity — the current frontier.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the Architectures and Mixture-of-Experts lectures are a data-driven survey of exactly these choices across real models; free slides, code and assignments.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; gives you the `transformers` attention-implementation vocabulary (eager, SDPA, FlashAttention) these variants plug into.

## Videos

- [Mistral / Mixtral Explained: Sliding Window Attention, Sparse Mixture of Experts, Rolling Buffer](https://www.youtube.com/watch?v=UiX8K-xBUpE) — **Umar Jamil** — the best free visual explanation of sliding-window attention and its rolling buffer, drawn mask by mask.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://www.youtube.com/watch?v=9dSkvxS2EB0) — **Yannic Kilcher** — the selective state-space mechanism that hybrid stacks put next to attention layers.
- [Flash Attention derived and coded from first principles](https://www.youtube.com/watch?v=zy8ChVd_oTM) — **Umar Jamil** — the exact-attention kernel every one of these variants is measured against.

## Key Papers

- [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150) — **Shazeer (2019)** — MQA: one shared key/value head, the original cache-shrinking move.
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) — **Ainslie et al. (2023)** — the middle ground that became the default, plus cheap uptraining from an existing multi-head checkpoint.
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)** — introduces MLA; also read [DeepSeek-V3](https://arxiv.org/abs/2412.19437) for MLA at production scale.
- [Mistral 7B](https://arxiv.org/abs/2310.06825) — **Jiang et al. (2023)** — sliding-window attention and the rolling-buffer cache, stated compactly.
- [Gemma 3 Technical Report](https://arxiv.org/abs/2503.19786) — **Gemma Team (2025)** — interleaved local and global attention (5:1) as a deliberate cache-versus-context trade.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)** — the selective state-space model that made the non-attention branch competitive.
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887) — **Lieber et al. (2024)** — the hybrid stack, with the ablations that justify the ratio.
- [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464) — **Yang et al. (2024)** — the gated linear-attention layer behind several 2025 hybrid releases.
- [MiniMax-01: Scaling Foundation Models with Lightning Attention](https://arxiv.org/abs/2501.08313) — **MiniMax (2025)** — linear attention scaled to a 456-billion-parameter production model.
- [Native Sparse Attention](https://arxiv.org/abs/2502.11089) — **Yuan et al. (2025)** — hardware-aligned, natively trainable sparse attention; compression, selection and a sliding branch combined.
- [MoBA: Mixture of Block Attention for Long-Context LLMs](https://arxiv.org/abs/2502.13189) — **Lu et al. (2025)** — route each query to a few key/value blocks; mixture-of-experts routing applied to attention itself.

## Articles / Blogs (free, no paywall)

- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka** — the single best free survey of what 2025's models actually changed, attention block included.
- [On the Tradeoffs of State Space Models](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu** — the Mamba author on what a fixed-size recurrent state can and cannot do versus attention; read this before claiming linear attention "replaces" attention.
- [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI** — the positional scheme these attention variants all assume; needed to reason about MLA's decoupled rotary key.
- [Qwen3-Next-80B-A3B model card](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct) — **Qwen Team** — a shipped hybrid: gated linear attention in most layers, gated full attention in the rest, plus a sparse mixture of experts.

## Books (free, with chapters)

- [*How to Scale Your Model* — "Transformers"](https://jax-ml.github.io/scaling-book/transformers/) — **Google DeepMind (Austin et al.)** — free online; the parameter, FLOP and memory accounting that turns "which attention variant" into a number.
- [*Dive into Deep Learning* — Ch. 11 "Attention Mechanisms and Transformers"](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — free and runnable; the baseline multi-head implementation every variant modifies.

## In this platform

- Prerequisite (canonical home): [Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism) · [Transformer Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/transformer-architecture/transformer-architecture) · [Efficient Attention (FlashAttention and the approximate family)](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention)
- Cache mechanics for these variants (not repeated here): [KV Cache Variants](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-variants) · [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache)
- Positions and length: [Positional Representations in LLMs](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/positional-representations-in-llms/positional-representations-in-llms) · [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures)
- The other axis of the same design space: [Mixture of Experts](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/mixture-of-experts/mixture-of-experts) · the non-autoregressive alternative: [Diffusion Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/diffusion-language-models/diffusion-language-models)
- What these choices buy at serving time: [Inference Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) · [Small and On-Device Language Models](/ai-ml/ai-ml-learning-resources/inference-and-serving/small-and-on-device-language-models/small-and-on-device-language-models)
- Intuition track: [Scaled Dot-Product Attention](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/scaled-dot-product-attention-intuition) · [Multi-Head Attention](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/multi-head-attention-intuition) · [Mixture-of-Experts Routing](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/mixture-of-experts-routing-intuition)
