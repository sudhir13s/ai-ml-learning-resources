---
id: "inference-and-serving/small-and-on-device-language-models"
topic: "Small and On-Device Language Models"
level: intermediate
built_from: ["quantization", "knowledge-distillation"]
leads_to: ["15-rag-and-llm-apps/caching-and-cost-optimization", "16-agentic-ai/frameworks"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Small and On-Device Language Models"
minutes: 15
category: inference-and-serving
---

# Small and On-Device Language Models

> A small language model (SLM) is a 0.1–10-billion-parameter model good enough for a *bounded* job —
> classification, extraction, routing, a tool-calling agent step — and small enough to run on a phone,
> a laptop or a single central processing unit (CPU) box. The 2024–2026 shift is that data quality
> and distillation made these models genuinely useful, not merely cheap.

**Why it matters:** most production agent traffic is repetitive, narrow work, and paying frontier
prices for it is a design error. Interviewers probe whether you can size a model to a job.

- **What is probed:** the on-device budget — weights in memory after quantisation, key-value cache growth with context, tokens per second on the target hardware, and battery or thermal limits; why 4-bit weights plus a small key-value cache is usually the binding constraint, not FLOPs.
- **The trade-off:** small models lose breadth of world knowledge and long-horizon reasoning first. They keep format-following, extraction and routing. Retrieval and tools substitute for knowledge; nothing fully substitutes for reasoning depth.
- **The 2025–26 argument:** NVIDIA's position paper claims SLMs, not frontier models, are the right default for *agentic* systems — most agent calls are narrow and repetitive, so route them to a small model and escalate only the hard ones.

**Start here — suggested path:**

1. **See the data-quality thesis** — read [Phi-3 Technical Report](https://arxiv.org/abs/2404.14219) — **Microsoft (2024)**. *A 3.8-billion-parameter model on a phone, and the curated-data argument that got it there.*
2. **Read the fully open counterpart** — read [SmolLM2](https://arxiv.org/abs/2502.02737) — **Ben Allal et al. (2025)** and the [SmolLM blog](https://huggingface.co/blog/smollm) — **Hugging Face**. *Every dataset and decision released, so you can copy the recipe rather than admire it.*
3. **Learn the deployment stack** — read the [llama.cpp](https://github.com/ggml-org/llama.cpp) README — **Georgi Gerganov and contributors**, then [MLX](https://github.com/ml-explore/mlx) — **Apple** for Apple silicon and [ExecuTorch](https://pytorch.org/executorch/stable/index.html) — **PyTorch** for mobile. *Three runtimes, three different reasons they exist.*
4. **Do the memory arithmetic** — read [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — **Carol Chen (kipp.ly)**. *Weights plus key-value cache versus your device's memory: the number that decides feasibility.*
5. **Read the agentic argument** — read [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153) — **Belcak et al. (2025, NVIDIA)**. *When to route to a small model and escalate, with a conversion recipe.*

## Courses (free)

- [nanochat](https://github.com/karpathy/nanochat) — **Andrej Karpathy** — a full from-scratch pipeline (tokenizer, pretraining, fine-tuning, inference, web user interface) for a small ChatGPT-class model; the best hands-on way to feel what a small model is.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; the fine-tuning and optimisation chapters are exactly the small-model workflow.
- [Hugging Face smol course](https://huggingface.co/learn/smol-course/unit0/1) — **Hugging Face** — a course built specifically around aligning and shipping small models ([repo](https://github.com/huggingface/smol-course)).

## Videos

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the sections on model size, data and post-training are the best free explanation of what you give up as parameters shrink.

## Key Papers

- [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219) — **Abdin et al. (2024)** — the flagship data-quality-over-scale result, with on-device latency numbers.
- [SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model](https://arxiv.org/abs/2502.02737) — **Ben Allal et al. (2025)** — the open, reproducible small-model recipe.
- [Gemma 3 Technical Report](https://arxiv.org/abs/2503.19786) — **Gemma Team (2025)** — 1B–27B models with interleaved local/global attention specifically to shrink the key-value cache for long context on small devices.
- [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115) — **Qwen Team (2024)** — the 0.5B–7B tier that most local deployments actually run.
- [MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases](https://arxiv.org/abs/2402.14905) — **Liu et al. (2024, Meta)** — depth beats width below a billion parameters; embedding sharing and grouped-query attention as necessities.
- [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153) — **Belcak et al. (2025, NVIDIA)** — the routing-and-escalation position paper for agent systems.

## Articles / Blogs (free, no paywall)

- [SmolLM: blazingly fast and remarkably powerful](https://huggingface.co/blog/smollm) — **Hugging Face** — how the small-model family was built, with the data mixture spelled out.
- [SmolLM3](https://huggingface.co/blog/smollm3) — **Hugging Face** — a 3-billion-parameter model with long context and dual reasoning modes, recipe included.
- [Gemma 3](https://huggingface.co/blog/gemma3) — **Hugging Face / Google** — what changed architecturally to make a small model handle 128K context on modest hardware.
- [Updates to Apple's On-Device and Server Foundation Models](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) — **Apple Machine Learning Research** — a shipped on-device model described by its authors: quantisation scheme, adapters, latency budget.
- [ggml and llama.cpp join Hugging Face](https://huggingface.co/blog/ggml-joins-hf) — **Hugging Face** — context on the local-inference stack that most on-device deployments actually use.

## Books (free, with chapters)

- [*Dive into Deep Learning*](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — free, runnable; the attention and computational-performance chapters give the cost model that decides what fits on a device.

## In this platform

- Prerequisite (canonical home): [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — the 4-bit weights every on-device deployment depends on · [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation)
- Why small models are viable at all now: [Synthetic Data and Data Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation) · [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws)
- The memory they are fighting: [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) · [KV Cache Variants](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-variants)
- Architecture choices that make small models cheap: [Attention Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) · [Mixture of Experts](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/mixture-of-experts/mixture-of-experts)
- Where they are routed to in production: [Caching and Cost Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/caching-and-cost-optimization/caching-and-cost-optimization) · [Agent Frameworks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-frameworks/agent-frameworks) · as a speculation draft: [Speculative Decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding)
- Intuition track: [Quantization](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/quantization-intuition) · [Knowledge Distillation](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/knowledge-distillation-intuition)
