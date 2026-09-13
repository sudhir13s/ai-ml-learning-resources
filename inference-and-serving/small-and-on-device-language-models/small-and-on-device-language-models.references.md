---
id: "inference-and-serving/small-and-on-device-language-models/references"
topic: "Small and On-Device Language Models — References"
parent: "inference-and-serving/small-and-on-device-language-models"
type: references
updated: 2026-09-14
---

# Small and On-Device Language Models — references

> Companion link library for **[Small and On-Device Language Models](/ai-ml/ai-ml-learning-resources/inference-and-serving/small-and-on-device-language-models/small-and-on-device-language-models)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See the data-quality thesis** — read [Phi-3 Technical Report](https://arxiv.org/abs/2404.14219) — **Microsoft (2024)**. *A 3.8-billion-parameter model on a phone, and the curated-data argument that got it there.*
2. **Read the fully open counterpart** — read [SmolLM2](https://arxiv.org/abs/2502.02737) — **Ben Allal et al. (2025)** and the [SmolLM blog](https://huggingface.co/blog/smollm) — **Hugging Face**. *Every dataset and decision released, so you can copy the recipe rather than admire it.*
3. **Learn the deployment stack** — read the [llama.cpp](https://github.com/ggml-org/llama.cpp) README — **Georgi Gerganov and contributors**, then [MLX](https://github.com/ml-explore/mlx) — **Apple** for Apple silicon and [ExecuTorch](https://pytorch.org/executorch/stable/index.html) — **PyTorch** for mobile. *Three runtimes, three different reasons they exist.*
4. **Do the memory arithmetic** — read [Transformer Inference Arithmetic](https://kipp.ly/transformer-inference-arithmetic/) — **Carol Chen (kipp.ly)**. *Weights plus key-value cache versus your device's memory: the number that decides feasibility.*
5. **Read the agentic argument** — read [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153) — **Belcak et al. (2025, NVIDIA)**. *When to route to a small model and escalate, with a conversion recipe.*

**In this platform**:
- [Agent Frameworks](/ai-ml/practitioner-workflows/agentic-systems/agent-frameworks/agent-frameworks) — where they are routed to in production.
- [Attention Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) — architecture choices that make small models cheap.
- [Caching and Cost Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/caching-and-cost-optimization/caching-and-cost-optimization) — where they are routed to in production.
- [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation) — prerequisite (canonical home).
- [Knowledge Distillation](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/knowledge-distillation-intuition) — intuition track.
- [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — the memory they are fighting.
- [KV Cache Variants](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-variants) — the memory they are fighting.
- [Mixture of Experts](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/mixture-of-experts/mixture-of-experts) — architecture choices that make small models cheap.
- [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — prerequisite (canonical home): the 4-bit weights every on-device deployment depends on.
- [Quantization](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/quantization-intuition) — intuition track.
- [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws) — why small models are viable at all now.
- [Speculative Decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) — where they are routed to in production: as a speculation draft.
- [Synthetic Data and Data Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation) — why small models are viable at all now.

**Videos**:
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the sections on model size, data and post-training are the best free explanation of what you give up as parameters shrink.

**Courses**:
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; the fine-tuning and optimisation chapters are exactly the small-model workflow.
- [Hugging Face smol course](https://huggingface.co/learn/smol-course/unit0/1) — **Hugging Face** — a course built specifically around aligning and shipping small models ([repo](https://github.com/huggingface/smol-course)).
- [nanochat](https://github.com/karpathy/nanochat) — **Andrej Karpathy** — a full from-scratch pipeline (tokenizer, pretraining, fine-tuning, inference, web user interface) for a small ChatGPT-class model; the best hands-on way to feel what a small model is.

**Articles**:
- [Gemma 3](https://huggingface.co/blog/gemma3) — **Hugging Face / Google** — what changed architecturally to make a small model handle 128K context on modest hardware.
- [ggml and llama.cpp join Hugging Face](https://huggingface.co/blog/ggml-joins-hf) — **Hugging Face** — context on the local-inference stack that most on-device deployments actually use.
- [SmolLM: blazingly fast and remarkably powerful](https://huggingface.co/blog/smollm) — **Hugging Face** — how the small-model family was built, with the data mixture spelled out.
- [SmolLM3](https://huggingface.co/blog/smollm3) — **Hugging Face** — a 3-billion-parameter model with long context and dual reasoning modes, recipe included.
- [Updates to Apple's On-Device and Server Foundation Models](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) — **Apple Machine Learning Research** — a shipped on-device model described by its authors: quantisation scheme, adapters, latency budget.

**Papers**:
- [Gemma 3 Technical Report](https://arxiv.org/abs/2503.19786) — **Gemma Team (2025)** — 1B–27B models with interleaved local/global attention specifically to shrink the key-value cache for long context on small devices.
- [MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases](https://arxiv.org/abs/2402.14905) — **Liu et al. (2024, Meta)** — depth beats width below a billion parameters; embedding sharing and grouped-query attention as necessities.
- [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219) — **Abdin et al. (2024)** — the flagship data-quality-over-scale result, with on-device latency numbers.
- [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115) — **Qwen Team (2024)** — the 0.5B–7B tier that most local deployments actually run.
- [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153) — **Belcak et al. (2025, NVIDIA)** — the routing-and-escalation position paper for agent systems.
- [SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model](https://arxiv.org/abs/2502.02737) — **Ben Allal et al. (2025)** — the open, reproducible small-model recipe.

**Books**:
- [*Dive into Deep Learning*](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — free, runnable; the attention and computational-performance chapters give the cost model that decides what fits on a device.
