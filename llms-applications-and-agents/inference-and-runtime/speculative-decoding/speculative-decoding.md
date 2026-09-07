---
id: "llms-applications-and-agents/inference-and-runtime/speculative-decoding"
topic: "Speculative Decoding"
level: advanced
built_from: ["decoding-and-sampling", "kv-cache"]
leads_to: ["continuous-batching-and-scheduling", "inference-optimization"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Speculative Decoding"
minutes: 15
category: inference-and-runtime
---

# Speculative Decoding

> Decoding one token per forward pass wastes a graphics processing unit (GPU): the step is
> memory-bandwidth bound, so the arithmetic units idle while weights stream from memory. Speculative
> decoding has a cheap **draft** propose several tokens, then lets the **target** model verify them
> all in *one* batched pass — accepting the longest prefix that the target would have produced
> anyway. Same output distribution, fewer target passes.

**Why it matters:** it is the standard latency lever in production serving and the cleanest
"free lunch" question an interviewer can ask, because the free lunch has precise conditions.

- **What is probed:** why the modified-rejection-sampling verification step is *lossless* (the accepted tokens are distributed exactly as the target would have sampled them); what the expected speedup depends on — acceptance rate α and draft cost c; why it helps latency at *low* batch size and can hurt throughput at high batch size.
- **The trade-off:** you spend idle compute to buy time. Once continuous batching has already saturated the GPU's arithmetic units, there is no idle compute left to spend — speculation then costs throughput.
- **The families:** an independent **draft model** (small model of the same family), self-drafting **Medusa** heads, and feature-level **EAGLE**, which drafts in the target's own hidden-state space and gets much higher acceptance.

**Start here — suggested path:**

1. **Get the idea and the guarantee** — read [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) — **Leviathan et al. (2022)**. *The algorithm plus the proof that the output distribution is unchanged.*
2. **Read the parallel derivation** — read [Accelerating LLM Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318) — **Chen et al. (2023, DeepMind)**. *The same result reached independently, with Chinchilla-scale numbers.*
3. **See it engineered** — read [A Hitchhiker's Guide to Speculative Decoding](https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/) — **PyTorch team**. *Draft selection, acceptance rates and the measured wins on real hardware.*
4. **Learn the draft-free variants** — read [Medusa](https://arxiv.org/abs/2401.10774) — **Cai et al. (2024)** and [EAGLE](https://arxiv.org/abs/2401.15077) — **Li et al. (2024)**. *Extra decoding heads versus drafting in feature space; EAGLE is where most of 2025's gains came from.*
5. **Know when it pays in your serving stack** — read [How Speculative Decoding Boosts vLLM Performance](https://blog.vllm.ai/2024/10/17/spec-decode.html) — **vLLM team**. *The batch-size crossover, stated by the maintainers with measurements.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the Inference lecture derives the memory-bandwidth bound that speculation exploits; slides free on the course site.
- [vLLM speculative decoding documentation](https://docs.vllm.ai/en/latest/features/spec_decode.html) — **vLLM maintainers** — configure draft models, n-gram and EAGLE speculation and measure the effect yourself.
- [Assisted Generation](https://huggingface.co/blog/assisted-generation) — **Hugging Face (Joao Gante)** — free walkthrough that turns speculation into three lines of `transformers` code.

## Videos

- [ML Performance Reading Group: Speculative Decoding](https://www.youtube.com/watch?v=1XDi8_VPCDU) — **EleutherAI** — a paper-by-paper tour of the field (original speculative decoding, Medusa, EAGLE 1/2/3) at research depth.
- [vLLM Office Hours — Intro to vLLM V1](https://www.youtube.com/watch?v=jmzIvQZCLZM) — **Neural Magic / vLLM** — the maintainers on the V1 scheduler and where speculative decoding hooks into it.

## Key Papers

- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) — **Leviathan, Kalman & Matias (2022)** — the original algorithm and the losslessness proof.
- [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318) — **Chen et al. (2023)** — the DeepMind formulation; 2–2.5× on Chinchilla with no quality change.
- [Medusa: Simple LLM Inference Acceleration with Multiple Decoding Heads](https://arxiv.org/abs/2401.10774) — **Cai et al. (2024)** — no separate draft model: extra heads predict several future tokens, verified with a tree attention mask.
- [EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://arxiv.org/abs/2401.15077) — **Li et al. (2024)** — draft in the target's feature space, not token space; the acceptance-rate breakthrough.
- [EAGLE-3: Scaling up Inference Acceleration via Training-Time Test](https://arxiv.org/abs/2503.01840) — **Li et al. (2025)** — the current state of the art, and why draft training must simulate multi-step drafting.
- [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)** — the memory system speculation runs on; the draft's key-value cache is not free.

## Articles / Blogs (free, no paywall)

- [A Hitchhiker's Guide to Speculative Decoding](https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/) — **PyTorch** — the most practical free write-up: what to draft with, measured acceptance rates, when it stops paying.
- [How Speculative Decoding Boosts vLLM Performance by up to 2.8x](https://blog.vllm.ai/2024/10/17/spec-decode.html) — **vLLM** — maintainer measurements including the batch-size crossover where the win disappears.
- [Accelerating Generative AI with PyTorch II: GPT, Fast](https://pytorch.org/blog/accelerating-generative-ai-2/) — **PyTorch** — speculative decoding stacked with quantisation and compilation, with the contribution of each isolated.
- [Together AI: Medusa](https://www.together.ai/blog/medusa) — **Together AI** — the accessible explanation of tree-structured drafts and their verification mask.
- [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — **Carol Chen (kipp.ly)** — the arithmetic-intensity model that tells you, before you benchmark, whether you have idle compute to speculate with.

## Books (free, with chapters)

- [*How to Scale Your Model* — "Inference"](https://jax-ml.github.io/scaling-book/inference) — **Google DeepMind (Austin et al.)** — free online book; the roofline treatment of prefill versus decode that makes speculation's economics obvious.

## In this platform

- Prerequisite: [Decoding and Sampling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/decoding-and-sampling/decoding-and-sampling) (the sampler speculation must reproduce exactly) · [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache)
- Canonical home of the serving mechanism and its other levers: [Inference Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization) · [vLLM and PagedAttention](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/vllm-and-paged-attention)
- The scheduler that decides whether speculation pays: [Continuous Batching and Scheduling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/continuous-batching-and-scheduling/continuous-batching-and-scheduling)
- Stacks with: [Quantization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/quantization/quantization) · [Caching and Cost Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/caching-and-cost-optimization/caching-and-cost-optimization)
- Where the draft model comes from: [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/knowledge-distillation/knowledge-distillation) · [Small and On-Device Language Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/small-and-on-device-language-models/small-and-on-device-language-models)
- Intuition track: [Speculative Decoding](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/inference-efficiency/speculative-decoding-intuition)
