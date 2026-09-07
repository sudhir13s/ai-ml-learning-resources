---
id: "09-llms/long-context-methods/references"
topic: "Long-Context Methods — References"
parent: "09-llms/long-context-methods"
type: references
updated: 2026-09-07
---

# Long-Context Methods — references and further reading

> Companion link library for **[Long-Context Methods](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures)** (the concept page). This file holds the curated links — external sources *and* internal cross-links — kept separate so it can be reused as a standalone reference list. Grouped by type, best-first. Every entry is free/open and chosen for depth on *this* topic — positional extension (RoPE scaling, YaRN, ALiBi), sparse/sliding attention, and bounded-cache streaming — not popularity.

**Start here — suggested path**:
1. **Get RoPE first** — watch [Rotary Positional Embeddings: Combining Absolute and Relative](https://www.youtube.com/watch?v=o29P0Kpobz0) (**Efficient NLP**). *Why rotation gives relative positions and graceful extrapolation — the foundation for everything else here.*
2. **See it in real code** — watch [Coding LLaMA 2 from scratch — RoPE, KV cache, GQA](https://www.youtube.com/watch?v=oM4VmoabDAI) (**Umar Jamil**). *Rotary embeddings and cache-friendly attention implemented line by line, so the scaling tricks below have something concrete to modify.*
3. **Read the angle problem and its fix** — read [Position Interpolation, interactive](https://mbrenndoerfer.com/writing/position-interpolation-rope-context-extension) (**Michael Brenndoerfer**), then the [YaRN paper](https://arxiv.org/abs/2309.00071) (**Peng et al.**). *Why naive extrapolation breaks and how interpolation/frequency-scaling fixes it.*
4. **Read the alternative philosophy** — [ALiBi: Train Short, Test Long](https://arxiv.org/abs/2108.12409) (**Press et al.**). *Distance-bias positions that extrapolate without rescaling the geometry.*
5. **Bound the cache** — [StreamingLLM / Attention Sinks](https://arxiv.org/abs/2309.17453) (**Xiao et al.**). *Why a few first tokens are load-bearing, and how that enables endless streaming.*
6. **Connect to compute & memory** — [FlashAttention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention) + [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache). *The other two walls of long context.*
7. **See where 2026 landed** — read the [DeepSeek-V2 paper](https://arxiv.org/abs/2405.04434) (**DeepSeek-AI**) for multi-head latent attention, then [Jamba](https://arxiv.org/abs/2403.19887) for the hybrid Mamba-plus-attention answer. *The two designs that made million-token contexts affordable rather than merely possible.*

**Videos**:
- [Rotary Positional Embeddings: Combining Absolute and Relative](https://www.youtube.com/watch?v=o29P0Kpobz0) — **Efficient NLP** — the cleanest RoPE explainer; start here if rotation-as-position still feels abstract.
- [Coding LLaMA 2 from scratch — RoPE, KV cache, GQA](https://www.youtube.com/watch?v=oM4VmoabDAI) — **Umar Jamil** — builds rotary embeddings and the sliding-window-friendly attention line by line in PyTorch.
- [Stanford CS336 — Language Modeling from Scratch, Spring 2025 (lectures)](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the architecture and attention lectures place positional schemes and sparse/linear attention in the cost model of a real training run.
- [FlashAttention — Tri Dao | Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Stanford MLSys** — the kernel that makes the $O(N^2)$ compute wall tractable at long context.

**Interactive & visual**:
- [Position Interpolation: Extending LLM Context with RoPE Scaling](https://mbrenndoerfer.com/writing/position-interpolation-rope-context-extension) — **Michael Brenndoerfer** — interactive walkthrough of squeezing positions back into the trained angle range.
- [YaRN: Selective Interpolation and Temperature Scaling](https://mbrenndoerfer.com/writing/yarn-rope-context-extension-llm) — **Michael Brenndoerfer** — interactive companion showing YaRN's frequency-dependent scaling vs PI.

**Courses (free)**:
- [Stanford CS336 — Language Modeling from Scratch (long context & efficiency)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — positional schemes and attention cost at length, within the full LLM stack.
- [Hugging Face — GPU inference optimization](https://huggingface.co/docs/transformers/en/perf_infer_gpu_one) — **Hugging Face** — long-context attention kernels and RoPE scaling in practice.

**Articles / blogs (free, no paywall)**:
- [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI** — the definitive intuition + derivation for RoPE, the basis of every scaling trick here.
- [LLM Context Length Extension](https://aman.ai/primers/ai/context-length-extension/) — **Aman Chadha** — a clear survey of PI, NTK-aware scaling, YaRN, and ALiBi side by side.
- [The Transformer Family v2](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — **Lilian Weng (OpenAI)** — long-range and sparse attention variants surveyed in one place.
- [In the long (context) run](https://www.harmdevries.com/post/context-length/) — **Harm de Vries** — the economics and practical limits of long context.

**Key papers**:
- [Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062) — **Zaheer et al. (2020)** — sparse attention (window + global + random) proven to be a universal approximator.
- [Efficient Streaming Language Models with Attention Sinks (StreamingLLM)](https://arxiv.org/abs/2309.17453) — **Xiao et al. (2023)** — the attention-sink phenomenon; bounding the cache with sinks + a recent window for infinite-length streaming.
- [Extending Context Window of LLMs via Positional Interpolation (PI)](https://arxiv.org/abs/2306.15595) — **Chen et al. (2023)** — squeeze the position index by $L_\text{train}/L_\text{target}$ so RoPE angles stay in the trained range.
- [Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) — **Beltagy et al. (2020)** — sliding-window + global-token sparse attention, linear in sequence length.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — **Liu et al. (2023)** — the U-shaped retrieval curve; why advertised context length overstates *effective* context.
- [Mistral 7B](https://arxiv.org/abs/2310.06825) — **Jiang et al. (2023)** — sliding-window attention with the layered-receptive-field argument (a window $w$ over $L$ layers reaches $\approx L\,w$ tokens).
- [RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864) — **Su et al. (2021)** — the rotary scheme behind nearly every long-context LLM and the relative-position derivation.
- [Train Short, Test Long: Attention with Linear Biases (ALiBi)](https://arxiv.org/abs/2108.12409) — **Press et al. (2021)** — distance-bias positions that extrapolate to longer sequences without learned embeddings.
- [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/abs/1901.02860) — **Dai et al. (2019)** — segment-level recurrence + relative positional encodings, an ancestor of RoPE.
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)** — NTK-by-parts frequency-dependent interpolation + attention-temperature correction; 128K with minimal fine-tuning.
- [FlashAttention: Fast and Memory-Efficient Exact Attention](https://arxiv.org/abs/2205.14135) — **Dao et al. (2022)** — IO-aware tiled attention; the compute-wall solution that makes long sequences trainable.
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)** — introduces **multi-head latent attention (MLA)**: compress K and V into a shared low-rank latent so the per-token cache falls to a few percent of multi-head attention. The single biggest change to the long-context memory wall since GQA, and now the default in the DeepSeek and Kimi lineages.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)** — the selective state-space model: constant-size state, linear-time scan, no KV cache at all; the credible non-attention answer to long sequences.
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887) — **Lieber et al. (2024, AI21)** — the hybrid that won in practice: interleave a few full-attention layers among many state-space layers, keeping recall while collapsing the cache. The shape most 2025-26 long-context models converged on.
- [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383) — **Qwen team (2025)** — a documented million-token open model: the progressive length-extension curriculum, the chunked-attention inference stack, and honest long-context evaluation.
- [RULER: What's the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654) — **Hsieh et al. (2024, NVIDIA)** — the benchmark that replaced needle-in-a-haystack: nearly every model's *effective* context is far below its advertised one. The evaluation half of the 2025-26 long-context story.

**In this platform**:
- Concept page (full explanation): [Long-Context Methods](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures)
- Foundations (the *why* behind RoPE and attention): [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding) · [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism)
- The other two walls: [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention) · [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache)
- The attention shapes these methods assume: [Attention Architectures (GQA, MLA, sliding, linear)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear)
- The alternative to a longer window: [Long Context vs RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/long-context-vs-rag/long-context-vs-rag)
- Builds on this: [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/decoder-only-models/decoder-only-models) (the modern RoPE recipe) · [Quantization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/quantization/quantization) (compressing the cache) · [Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization)
