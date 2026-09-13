---
id: "09-llms/long-context-methods/references"
topic: "Long-Context Methods — References"
parent: "09-llms/long-context-methods"
type: references
updated: 2026-09-07
---

# Long-Context Methods — references

> Companion link library for **[Long-Context Methods](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Get RoPE first** — watch [Rotary Positional Embeddings: Combining Absolute and Relative](https://www.youtube.com/watch?v=o29P0Kpobz0) (**Efficient NLP**). *Why rotation gives relative positions and graceful extrapolation — the foundation for everything else here.*
2. **See it in real code** — watch [Coding LLaMA 2 from scratch — RoPE, KV cache, GQA](https://www.youtube.com/watch?v=oM4VmoabDAI) (**Umar Jamil**). *Rotary embeddings and cache-friendly attention implemented line by line, so the scaling tricks below have something concrete to modify.*
3. **Read the angle problem and its fix** — read [Position Interpolation, interactive](https://mbrenndoerfer.com/writing/position-interpolation-rope-context-extension) (**Michael Brenndoerfer**), then the [YaRN paper](https://arxiv.org/abs/2309.00071) (**Peng et al.**). *Why naive extrapolation breaks and how interpolation/frequency-scaling fixes it.*
4. **Read the alternative philosophy** — [ALiBi: Train Short, Test Long](https://arxiv.org/abs/2108.12409) (**Press et al.**). *Distance-bias positions that extrapolate without rescaling the geometry.*
5. **Bound the cache** — [StreamingLLM / Attention Sinks](https://arxiv.org/abs/2309.17453) (**Xiao et al.**). *Why a few first tokens are load-bearing, and how that enables endless streaming.*
6. **Connect to compute & memory** — [FlashAttention](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention) + [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache). *The other two walls of long context.*
7. **See where 2026 landed** — read the [DeepSeek-V2 paper](https://arxiv.org/abs/2405.04434) (**DeepSeek-AI**) for multi-head latent attention, then [Jamba](https://arxiv.org/abs/2403.19887) for the hybrid Mamba-plus-attention answer. *The two designs that made million-token contexts affordable rather than merely possible.*

**In this platform**:
- The attention shapes these methods assume: [Attention Architectures (GQA, MLA, sliding, linear)](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear)
- Builds on this: [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/decoder-only-models/decoder-only-models) (the modern RoPE recipe) · [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) (compressing the cache) · [Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)
- The other two walls: [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention) · [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache)
- The alternative to a longer window: [Long Context vs RAG](/ai-ml/practitioner-workflows/llm-applications/long-context-vs-rag/long-context-vs-rag)
- Concept page (full explanation): [Long-Context Methods](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures)
- Foundations (the *why* behind RoPE and attention): [Positional Encoding](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/positional-encoding/positional-encoding) · [Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism)

**Videos**:
- [Coding LLaMA 2 from scratch — RoPE, KV cache, GQA](https://www.youtube.com/watch?v=oM4VmoabDAI) — **Umar Jamil** — builds rotary embeddings and the sliding-window-friendly attention line by line in PyTorch.
- [FlashAttention — Tri Dao | Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Stanford MLSys** — the kernel that makes the $O(N^2)$ compute wall tractable at long context.
- [Rotary Positional Embeddings: Combining Absolute and Relative](https://www.youtube.com/watch?v=o29P0Kpobz0) — **Efficient NLP** — the cleanest RoPE explainer; start here if rotation-as-position still feels abstract.
- [Stanford CS336 — Language Modeling from Scratch, Spring 2025 (lectures)](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the architecture and attention lectures place positional schemes and sparse/linear attention in the cost model of a real training run.

**Courses**:
- [Hugging Face — GPU inference optimization](https://huggingface.co/docs/transformers/en/perf_infer_gpu_one) — **Hugging Face** — long-context attention kernels and RoPE scaling in practice.
- [Stanford CS336 — Language Modeling from Scratch (long context & efficiency)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — positional schemes and attention cost at length, within the full LLM stack.

**Interactive**:
- [Position Interpolation: Extending LLM Context with RoPE Scaling](https://mbrenndoerfer.com/writing/position-interpolation-rope-context-extension) — **Michael Brenndoerfer** — interactive walkthrough of squeezing positions back into the trained angle range.
- [YaRN: Selective Interpolation and Temperature Scaling](https://mbrenndoerfer.com/writing/yarn-rope-context-extension-llm) — **Michael Brenndoerfer** — interactive companion showing YaRN's frequency-dependent scaling vs PI.

**Articles**:
- [In the long (context) run](https://www.harmdevries.com/post/context-length/) — **Harm de Vries** — the economics and practical limits of long context.
- [LLM Context Length Extension](https://aman.ai/primers/ai/context-length-extension/) — **Aman Chadha** — a clear survey of PI, NTK-aware scaling, YaRN, and ALiBi side by side.
- [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI** — the definitive intuition + derivation for RoPE, the basis of every scaling trick here.
- [The Transformer Family v2](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — **Lilian Weng (OpenAI)** — long-range and sparse attention variants surveyed in one place.

**Papers**:
- [Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062) — **Zaheer et al. (2020)** — sparse attention (window + global + random) proven to be a universal approximator.
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)** — introduces **multi-head latent attention (MLA)**: compress K and V into a shared low-rank latent so the per-token cache falls to a few percent of multi-head attention. The single biggest change to the long-context memory wall since GQA, and now the default in the DeepSeek and Kimi lineages.
- [Efficient Streaming Language Models with Attention Sinks (StreamingLLM)](https://arxiv.org/abs/2309.17453) — **Xiao et al. (2023)** — the attention-sink phenomenon; bounding the cache with sinks + a recent window for infinite-length streaming.
- [Extending Context Window of LLMs via Positional Interpolation (PI)](https://arxiv.org/abs/2306.15595) — **Chen et al. (2023)** — squeeze the position index by $L_\text{train}/L_\text{target}$ so RoPE angles stay in the trained range.
- [FlashAttention: Fast and Memory-Efficient Exact Attention](https://arxiv.org/abs/2205.14135) — **Dao et al. (2022)** — IO-aware tiled attention; the compute-wall solution that makes long sequences trainable.
- [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887) — **Lieber et al. (2024, AI21)** — the hybrid that won in practice: interleave a few full-attention layers among many state-space layers, keeping recall while collapsing the cache. The shape most 2025-26 long-context models converged on.
- [Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) — **Beltagy et al. (2020)** — sliding-window + global-token sparse attention, linear in sequence length.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — **Liu et al. (2023)** — the U-shaped retrieval curve; why advertised context length overstates *effective* context.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)** — the selective state-space model: constant-size state, linear-time scan, no KV cache at all; the credible non-attention answer to long sequences.
- [Mistral 7B](https://arxiv.org/abs/2310.06825) — **Jiang et al. (2023)** — sliding-window attention with the layered-receptive-field argument (a window $w$ over $L$ layers reaches $\approx L\,w$ tokens).
- [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383) — **Qwen team (2025)** — a documented million-token open model: the progressive length-extension curriculum, the chunked-attention inference stack, and honest long-context evaluation.
- [RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864) — **Su et al. (2021)** — the rotary scheme behind nearly every long-context LLM and the relative-position derivation.
- [RULER: What's the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654) — **Hsieh et al. (2024, NVIDIA)** — the benchmark that replaced needle-in-a-haystack: nearly every model's *effective* context is far below its advertised one. The evaluation half of the 2025-26 long-context story.
- [Train Short, Test Long: Attention with Linear Biases (ALiBi)](https://arxiv.org/abs/2108.12409) — **Press et al. (2021)** — distance-bias positions that extrapolate to longer sequences without learned embeddings.
- [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/abs/1901.02860) — **Dai et al. (2019)** — segment-level recurrence + relative positional encodings, an ancestor of RoPE.
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)** — NTK-by-parts frequency-dependent interpolation + attention-temperature correction; 128K with minimal fine-tuning.
