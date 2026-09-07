---
id: "llms-applications-and-agents/inference-and-runtime/continuous-batching-and-scheduling"
topic: "Continuous Batching and Scheduling"
level: advanced
built_from: ["inference-optimization", "kv-cache"]
leads_to: ["caching-and-cost-optimization", "small-and-on-device-language-models"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Continuous Batching and Scheduling"
minutes: 16
category: inference-and-runtime
---

# Continuous Batching and Scheduling

> A serving engine is a scheduler wrapped around a model. **Continuous (iteration-level) batching**
> re-forms the batch after *every* decode step, so a finished sequence frees its slot immediately
> instead of idling until the slowest member of a static batch completes. **Chunked prefill** and
> **prefill/decode disaggregation** then stop long prompts from stalling everyone else.

**Why it matters:** this is where serving cost is actually won or lost, and where senior interviews
go after the candidate has recited "the key-value cache is big."

- **What is probed:** why prefill is compute-bound and decode is memory-bandwidth bound, and what follows for scheduling; how iteration-level scheduling (Orca) differs from static batching; what **goodput** means — requests per second *that meet their latency service-level objective (SLO)*, not raw throughput.
- **The core tension:** time to first token (TTFT) and time per output token (TPOT) pull in opposite directions. A bigger batch raises tokens per second and delays every individual first token.
- **The 2025 answer:** stop mixing the two phases. **Chunked prefill** (Sarathi-Serve) slices a long prompt so decodes ride along; **disaggregation** (DistServe, Splitwise) runs prefill and decode on separate pools tuned for different bottlenecks.

**Start here — suggested path:**

1. **See the win in one picture** — read [How Continuous Batching Enables 23x Throughput in LLM Inference](https://www.anyscale.com/blog/continuous-batching-llm-inference) — **Anyscale**. *Static versus continuous batching, with the occupancy diagram everyone reuses.*
2. **Read the paper that started it** — read [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu) — **Yu et al. (OSDI 2022)**. *Iteration-level scheduling and selective batching; free USENIX PDF.*
3. **Understand the memory the scheduler manages** — read [PagedAttention](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)**. *Blocks, block tables and preemption: the allocator that makes admission decisions possible.*
4. **Learn the two phase-separation techniques** — read [Sarathi-Serve](https://arxiv.org/abs/2403.02310) — **Agrawal et al. (2024)** (chunked prefill, stall-free batching) and [DistServe](https://arxiv.org/abs/2401.09670) — **Zhong et al. (2024)** (disaggregation, goodput). *The two answers to prefill–decode interference.*
5. **Read a real engine end to end** — read [Inside vLLM: Anatomy of a High-Throughput LLM Inference System](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html) — **vLLM maintainers**. *Scheduler, block manager, and the V1 execution loop, in the maintainers' own words.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the Inference lecture builds the prefill/decode roofline that every scheduling decision follows from; free slides and code.
- [vLLM disaggregated prefilling documentation](https://docs.vllm.ai/en/latest/features/disagg_prefill.html) — **vLLM maintainers** — run a disaggregated deployment yourself and watch TTFT and TPOT move independently.
- [vLLM automatic prefix caching documentation](https://docs.vllm.ai/en/latest/design/prefix_caching.html) — **vLLM maintainers** — the design note for the cache-aware scheduling that shared system prompts depend on.

## Videos

- [vLLM Office Hours — Intro to vLLM V1](https://www.youtube.com/watch?v=jmzIvQZCLZM) — **Neural Magic / vLLM** — the V1 rewrite explained by maintainers: scheduler, memory manager, and why the loop was restructured.
- [Stanford CS336 — Lecture 1: Overview and Tokenization](https://www.youtube.com/watch?v=SQ3fZ1sAqXI) — **Stanford Online** — the entry point to the lecture series that later covers inference and systems.

## Key Papers

- [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu) — **Yu et al. (2022)** — iteration-level scheduling and selective batching; the origin of continuous batching.
- [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)** — the vLLM paper: paged key-value blocks, sharing, preemption.
- [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310) — **Agrawal et al. (2024)** — chunked prefill and stall-free batching; also at [USENIX OSDI 2024](https://www.usenix.org/conference/osdi24/presentation/agrawal).
- [DistServe: Disaggregating Prefill and Decoding for Goodput-Optimized Serving](https://arxiv.org/abs/2401.09670) — **Zhong et al. (2024)** — separate the phases onto separate resources; defines goodput under SLOs. Also at [USENIX OSDI 2024](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin).
- [Splitwise: Efficient Generative LLM Inference Using Phase Splitting](https://arxiv.org/abs/2311.18677) — **Patel et al. (2023, Microsoft)** — the same split argued from cluster economics and power.

## Articles / Blogs (free, no paywall)

- [How Continuous Batching Enables 23x Throughput in LLM Inference](https://www.anyscale.com/blog/continuous-batching-llm-inference) — **Anyscale (Cade Daniel et al.)** — the clearest free explanation of static versus continuous batching, with benchmarks.
- [Inside vLLM: Anatomy of a High-Throughput LLM Inference System](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html) — **vLLM** — a guided tour of a production engine's scheduler and memory manager.
- [vLLM V1: A Major Upgrade to vLLM's Core Architecture](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html) — **vLLM** — what a modern scheduler had to become: zero-overhead loops, unified prefill/decode batches.
- [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — **Carol Chen (kipp.ly)** — the back-of-envelope model for batch size, bandwidth and latency you should be able to reproduce in an interview.

## Books (free, with chapters)

- [*How to Scale Your Model* — "Inference"](https://jax-ml.github.io/scaling-book/inference) — **Google DeepMind (Austin et al.)** — free online; prefill/decode rooflines, batch-size arithmetic and the latency–throughput frontier, derived.
- [*How to Scale Your Model* — "Transformers"](https://jax-ml.github.io/scaling-book/transformers/) — **Google DeepMind** — the parameter and FLOP accounting the scheduling maths sits on top of.

## In this platform

- Canonical home of the serving picture and its levers: [Inference Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization) · [vLLM and PagedAttention](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/vllm-and-paged-attention)
- What the scheduler is allocating: [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache) · [KV Cache in Production](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache-in-production) · [KV Cache Optimization Stack](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache-optimization-stack)
- The lever that competes for the same idle compute: [Speculative Decoding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/speculative-decoding/speculative-decoding)
- Where prefix reuse turns into money: [Caching and Cost Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/caching-and-cost-optimization/caching-and-cost-optimization) · [Quantization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/quantization/quantization)
- Long prompts are the hard scheduling case: [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures)
- Intuition track: [Speculative Decoding](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/inference-efficiency/speculative-decoding-intuition)
