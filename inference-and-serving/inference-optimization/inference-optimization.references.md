---
id: "09-llms/inference-optimization-and-serving/references"
topic: "Inference Optimization & Serving — References"
parent: "09-llms/inference-optimization-and-serving"
type: references
updated: 2026-09-13
---

# Inference Optimization & Serving — references

> Companion link library for **[Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Split prefill from decode** — watch [How a Transformer works at inference vs training time](https://www.youtube.com/watch?v=IGu7ivuy1Ag) (**Niels Rogge, Hugging Face**). *The two phases every serving optimization on the page is built around.*
2. **Hear the levers from the engine's author** — watch [Fast LLM Serving with vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U) (**Anyscale, Woosuk Kwon**). *PagedAttention and continuous batching explained by the person who built them.*
3. **Derive why decode is memory-bound** — read [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) (**kipply**). *The per-token FLOP and KV-cache arithmetic the page's math section rests on.*
4. **Measure the biggest win** — read [How Continuous Batching Enables 23× Throughput in LLM Inference](https://www.anyscale.com/blog/continuous-batching-llm-inference) (**Anyscale**). *Static against continuous batching on production-shaped traffic.*
5. **Go to the source** — read [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) (**Kwon et al., 2023**). *Paging the KV cache like virtual memory, with the 2–4× throughput result.*

**In this platform**:
- [Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism) — the *why* behind the queries, keys and values the cache stores.
- [Caching & Cost Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/caching-and-cost-optimization/caching-and-cost-optimization) — skipping repeated work entirely, the cheapest token of all.
- [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/decoder-only-models/decoder-only-models) — the model being served.
- [Decoding & Sampling](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling) — the per-step token choice the decode loop serves.
- [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention) — the kernels under the engine.
- [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — the prefill/decode split, the memory-bound decode arithmetic, and the cache-shrinking levers this page builds on.
- [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — cutting the bytes streamed per decode step.
- [Speculative Decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) — draft-and-verify, in depth.
- [Transformer Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/transformer-architecture/transformer-architecture) — the block whose weights decode reads every step.

**Videos**:
- [Fast LLM Serving with vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U) — **Anyscale (Woosuk Kwon)** — the first author of vLLM walks through PagedAttention and continuous batching.
- [How a Transformer works at inference vs training time](https://www.youtube.com/watch?v=IGu7ivuy1Ag) — **Niels Rogge (Hugging Face)** — prefill vs decode, the split every serving optimization is built on.
- [Inference, Serving, PagedAttention and vLLM](https://www.youtube.com/watch?v=3TBT4WPkDaw) — **AI Makerspace** — the serving-engine view: paging, continuous batching, and the metrics that matter.
- [Stanford CS336 — Language Modeling from Scratch, Spring 2025 (lectures)](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the inference, GPU/kernel and parallelism lectures, taught from a real build.

**Courses**:
- [Stanford CS336 — Language Modeling from Scratch (inference & serving systems)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the systems view of efficient LLM inference: batching, paging, parallelism.

**Interactive**:
- [LLM Visualizer (3D)](https://bbycroft.net/llm) — **Brendan Bycroft** — walk a token through a small GPT's forward pass and see where prefill ends and decode begins.

**Articles**:
- [Accelerating Generative AI II: GPT, Fast](https://pytorch.org/blog/accelerating-generative-ai-2/) — **PyTorch team** — KV cache, quantization, and speculative decoding in a real fast-decode implementation.
- [Deploying DeepSeek with PD disaggregation and large-scale expert parallelism](https://lmsys.org/blog/2025-05-05-large-scale-ep/) — **LMSYS / SGLang team (2025)** — a measured production account of disaggregated prefill/decode on a frontier mixture-of-experts model.
- [Flash-Decoding for long-context inference](https://pytorch.org/blog/flash-decoding/) — **Tri Dao, Daniel Haziza, Francisco Massa, Grigory Sizov (PyTorch)** — parallelizing a single decode query across the KV cache.
- [How Continuous Batching Enables 23× Throughput in LLM Inference](https://www.anyscale.com/blog/continuous-batching-llm-inference) — **Anyscale** — static vs continuous batching measured on production-shaped traffic (source for the 23× figure).
- [How to Scale Your Model — Inference](https://jax-ml.github.io/scaling-book/inference) — **Google DeepMind JAX team (2025)** — first-principles prefill vs decode arithmetic and batch-size sweet spots.
- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) — **Lilian Weng** — the full toolbox: quantization, distillation, sparsity, speculative decoding.
- [LLM Inference Performance Engineering: Best Practices](https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices) — **Databricks** — time-to-first-token, time-per-output-token, batching, and the latency/throughput budget in practice.
- [The Anatomy of vLLM](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html) — **vLLM team (2025)** — a guided walk through the engine's code path, from request arrival to sampled token.
- [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — **kipply** — the memory-bandwidth math behind every serving decision (source for the per-token FLOP and KV-cache derivations).
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI** — the $2\times\text{params}$ inference-FLOP rule and full memory accounting.
- [vLLM V1: a major upgrade to the core architecture](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html) — **vLLM team (2025)** — zero-overhead scheduling, with prefix caching and chunked prefill on by default.
- [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html) — **vLLM team (UC Berkeley)** — the canonical intro to paging the KV cache, with benchmarks.

**Papers**:
- [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318) — **Chen et al. (2023, DeepMind)** — concurrent derivation of speculative sampling with the distribution-preserving acceptance step.
- [DistServe: Disaggregating Prefill and Decoding for Goodput-Optimized LLM Serving](https://arxiv.org/abs/2401.09670) — **Zhong et al. (2024, OSDI)** — separate GPU pools for prefill and decode so a long prompt never stalls another request.
- [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023, SOSP)** — PagedAttention and vLLM; the 2–4× throughput result and the KV-size formula.
- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102) — **Pope et al. (2022, Google)** — establishes that autoregressive decode is memory-bound.
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) — **Leviathan, Kalman & Matias (2023, ICML)** — §3.1 derives the expected-speedup formula used on the page.
- [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) — **Dao et al. (2022)** — the IO-aware tiled attention kernel serving engines build on.
- [Medusa: Simple LLM Inference Acceleration with Multiple Decoding Heads](https://arxiv.org/abs/2401.10774) — **Cai et al. (2024)** — self-speculation with extra heads instead of a separate draft model.
- [Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving](https://arxiv.org/abs/2407.00079) — **Qin et al. (2024, Moonshot AI)** — disaggregated prefill/decode with a shared KV-cache pool across machines.
- [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu) — **Yu et al. (2022, OSDI)** — introduces iteration-level (continuous) batching.
- [Roofline: An Insightful Visual Performance Model](https://escholarship.org/content/qt78h8v7mr/qt78h8v7mr.pdf) — **Williams, Waterman & Patterson (CACM 2009)** — the compute-vs-bandwidth model behind "decode is memory-bound".
- [SGLang: Efficient Execution of Structured Language Model Programs (RadixAttention)](https://arxiv.org/abs/2312.07104) — **Zheng et al. (2023)** — prefix-sharing the KV cache via a radix tree.

**Documentation**:
- [LLM inference optimization](https://huggingface.co/docs/transformers/en/llm_optims) — **Hugging Face Transformers** — KV cache, static cache, quantization, and speculative decoding in runnable code.
- [vLLM Documentation](https://docs.vllm.ai/en/latest/) — **vLLM project** — PagedAttention, continuous batching, chunked prefill, prefix caching, and speculative decoding configuration.
