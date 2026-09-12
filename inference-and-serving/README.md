---
id: "inference-and-serving"
topic: "Inference and Serving"
level: advanced
built_from: ["large-language-models", "model-adaptation"]
updated: 2026-09-13
---

# Inference and Serving

> Serving is where a model's economics are decided. For an LLM, decoding is memory-bandwidth
> bound, so almost every technique here is a way of moving fewer bytes per generated token: cache
> what was already computed, shrink the cache, shrink the weights, verify several tokens per
> forward pass, and keep the accelerator busy with a scheduler that reforms the batch every step.
> The section is the deepest in the library — the KV-cache package alone runs to five pages —
> and it closes with packaging and serving any trained model, LLM or not.

**Start here:** [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — the memory object every later page optimizes, then [Inference Optimization and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) for the engine that serves it.

## Concept index

Each page is a self-contained resource card with a curated `.references.md` companion where one
exists: a plain-words definition, why it matters in 2026, a five-step start-here path, and
verified courses, videos, papers, articles and books.

### The KV-cache package (one main page plus four depth chapters)

1. [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — the main page: why decoding recomputes itself without a cache, the memory formula, and the proof that outputs are identical with and without it.
2. [KV Cache — Variants](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-variants) — multi-query, grouped-query and latent caches; why the KV-head count decides whether a large model is servable at long context.
3. [KV Cache — The Optimization Ladder](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-optimization-stack) — the five levels from naive concatenation to block-addressable paging, each fixing the previous level's cost.
4. [KV Cache — FlashAttention and FlashDecoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-flashattention-and-flashdecoding) — input/output-aware kernels: same mathematics, far fewer high-bandwidth-memory round trips.
5. [KV Cache — In Production](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-in-production) — prefix sharing, eviction, offload, rollback for speculation, and the metrics an on-call engineer watches.

### Choosing the next token

6. [Decoding and Sampling](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling) — greedy, beam, temperature, top-k, top-p and min-p; what each knob does to the distribution.
7. [Speculative Decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) — draft-and-verify with a provably identical output distribution; where the speedup comes from and when it evaporates.

### Making the weights and the engine cheaper

8. [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — GPTQ, AWQ, GGUF, LLM.int8 and NF4: post-hoc numeric compression, and what actually degrades.
9. [Inference Optimization and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — the systems counterpart to the KV cache: vLLM, PagedAttention, the prefill/decode split and the serving roofline.
10. [vLLM and PagedAttention](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/vllm-and-paged-attention) — the paging design in detail, as a companion note to the page above.
11. [Continuous Batching and Scheduling](/ai-ml/ai-ml-learning-resources/inference-and-serving/continuous-batching-and-scheduling/continuous-batching-and-scheduling) — iteration-level batching, chunked prefill, and prefill/decode disaggregation.

### Paying less per request

12. [Caching and Cost Optimization for LLM Apps](/ai-ml/ai-ml-learning-resources/inference-and-serving/caching-and-cost-optimization/caching-and-cost-optimization) — prompt/prefix caching, semantic caching, hit rates and the token cost model.
13. [Small and On-Device Language Models](/ai-ml/ai-ml-learning-resources/inference-and-serving/small-and-on-device-language-models/small-and-on-device-language-models) — the 0.1 to 10-billion-parameter band that is good enough for a bounded job and runs on a phone or a laptop.

### Packaging and serving any model

14. [Model Packaging and Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization) — the deployable unit: an image with the model, its serving code and every dependency pinned.
15. [Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) — REST and gRPC, batch versus online, and the serving frameworks (BentoML, Triton, TF Serving).
16. [Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference) — autoscaling, GPU sharing and Ray Serve; the sub-area index is [Packaging and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/readme).

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the inference lecture builds the prefill/decode roofline that every scheduling decision on these pages follows from.
- [LLM inference optimization](https://huggingface.co/docs/transformers/en/llm_optims) — **Hugging Face** — free, hands-on guide to the latency and cost levers, with working code for each.
- [vLLM automatic prefix caching](https://docs.vllm.ai/en/latest/design/prefix_caching.html) — **vLLM maintainers** — the design note for cache-aware scheduling, from the team that wrote the scheduler.
- [nanochat](https://github.com/karpathy/nanochat) — **Andrej Karpathy** — a full from-scratch pipeline including the inference engine; the shortest path to reading a real decode loop.

## Videos

- [How a Transformer works at inference vs training time](https://www.youtube.com/watch?v=IGu7ivuy1Ag) — **Niels Rogge (Hugging Face)** — prefill versus decode, the split every optimization on these pages is built on.
- [vLLM Office Hours — Intro to vLLM V1](https://www.youtube.com/watch?v=jmzIvQZCLZM) — **vLLM maintainers** — the V1 rewrite explained by the people who wrote it: scheduler, memory manager and why the loop looks like that.
- [FlashAttention — Tri Dao, Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Stanford MLSys Seminars** — the kernel underneath modern attention serving, from its author.
- [Greedy? Min-p? Beam Search? How LLMs Actually Pick Words](https://www.youtube.com/watch?v=o-_SZ_itxeA) — **AI Coffee Break with Letitia** — the clearest survey of decoding strategies, greedy through min-p.

## Key Papers

- [Efficient Memory Management for LLM Serving with PagedAttention (vLLM)](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)** — the paper that made the KV cache a paged, block-addressable object; the default serving design since.
- [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu) — **Yu et al. (OSDI 2022)** — iteration-level scheduling and selective batching; the origin of continuous batching.
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) — **Leviathan, Kalman and Matias (ICML 2023, Google)** — draft-and-verify with the expected-speedup derivation.
- [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) — **Dao et al. (2022)** — the tiled kernel serving engines build on, and the argument that round trips beat FLOPs.
- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102) — **Pope et al. (Google, 2022)** — the canonical cost analysis establishing that autoregressive decode is memory-bandwidth bound.
- [Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving](https://arxiv.org/abs/2407.00079) — **Qin et al. (Moonshot AI, 2024)** — disaggregated prefill and decode over a shared cache pool; the current frontier design.

## Articles / Blogs (free, no paywall)

- [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — **Carol Chen** — the back-of-envelope model for batch size, bandwidth and latency that every page here assumes you can do.
- [How Continuous Batching Enables 23x Throughput in LLM Inference](https://www.anyscale.com/blog/continuous-batching-llm-inference) — **Anyscale** — the clearest free explanation of static versus continuous batching, with measurements.
- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) — **Lilian Weng** — the whole toolbox surveyed in one place: quantization, distillation, sparsity, speculative decoding.
- [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html) — **vLLM team, UC Berkeley** — the canonical introduction to paging the cache, with benchmarks.
- [Flash-Decoding for long-context inference](https://pytorch.org/blog/flash-decoding/) — **Tri Dao, Daniel Haziza, Francisco Massa and Grigory Sizov (PyTorch)** — parallelizing a single decode query across the sequence.

## Books (free, with chapters)

- [*How to Scale Your Model* — "Inference"](https://jax-ml.github.io/scaling-book/inference) — **Google DeepMind (Austin et al.)** — free online; prefill and decode rooflines and the batch-size arithmetic, derived.
- [*Speech and Language Processing*, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky and Martin** — free draft; autoregressive generation, greedy versus sampling, temperature and top-k/top-p.
- [*Dive into Deep Learning* — Ch. 10 "Beam Search"](https://d2l.ai/chapter_recurrent-modern/beam-search.html) — **Zhang, Lipton, Li and Smola** — greedy as the width-1 special case, and length-normalized scoring.
- [*Transformer inference optimization guide*](https://huggingface.co/docs/transformers/en/llm_optims) — **Hugging Face** — the closest free book-length reference on caching, batching and the latency levers, kept current.

## In this platform

- Before this section: [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) · [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme) · After it: [Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/readme) · [Operations and Lifecycle](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme)
- Why the cache has the shape it has: [Attention Architectures — GQA, MLA, Sliding-Window and Linear](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) · [Long-Context Methods](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures)
- The kernel and hardware layer: [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention) · [GPUs and Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning)
- The operations view of the same problem: [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization) · [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
- The mental models: [Speculative Decoding](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/inference-efficiency/speculative-decoding-intuition) · [Quantization](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/quantization-intuition) · [Autoregressive Generation and Sampling Controls](/ai-ml/ai-ml-intuitions/generation/autoregressive-generation/autoregressive-generation-and-sampling-controls-intuition)
- Doing it rather than reading it: [Inference and Decoding workflow](/ai-ml/practitioner-workflows/inference-and-serving/inference-and-decoding) · [Model Serving workflow](/ai-ml/practitioner-workflows/inference-and-serving/model-serving) · [Inference Cost Optimization workflow](/ai-ml/practitioner-workflows/inference-and-serving/inference-cost-optimization) · [Running Local Models workflow](/ai-ml/practitioner-workflows/model-landscape/running-local-models)
