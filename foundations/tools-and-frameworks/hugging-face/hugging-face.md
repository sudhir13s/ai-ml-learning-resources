---
id: "17-tools-and-frameworks/hugging-face"
topic: "Hugging Face (Transformers · Datasets · Hub)"
core_idea: "Hugging Face puts one uniform interface — Auto classes, pipelines, Datasets and the Hub — over thousands of pretrained models, with peft, trl and accelerate layered on for fine-tuning and post-training."
parent: "17-tools-and-frameworks"
level: intermediate
built_from: ["python", "pytorch", "transformers"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Hugging Face (Transformers · Datasets · Hub)"
minutes: 10
category: tools-and-frameworks
---

# Hugging Face — Transformers · Datasets · Hub
> The center of gravity for modern NLP/LLM work: **Transformers** (load and run thousands of
> pretrained models with a uniform API), **Datasets** (efficient, streaming data loading),
> **Tokenizers**, and the **Hub** (the GitHub of models and datasets). The `pipeline()` one-liner
> takes you from "I want sentiment analysis" to a working model in three lines.

**Why it matters:** almost every applied LLM/NLP role expects Hugging Face fluency — `pipeline`,
`AutoModel`/`AutoTokenizer`, fine-tuning with `Trainer`, loading/streaming datasets, and pushing to
the Hub. It is the practical layer on top of the transformer architecture and the default toolkit
for RAG, fine-tuning, and inference.

**Where it is in 2026:** the ecosystem has split into focused libraries around the same Hub:

- **`transformers` v5** — leaner and PyTorch-first: the TensorFlow/Flax model classes are gone, weights load as `safetensors`, and attention implementations (SDPA, FlashAttention) are selectable per model.
- **`peft`** for parameter-efficient fine-tuning (LoRA/QLoRA) and **`trl`** for supervised fine-tuning, direct preference optimization (DPO) and GRPO-style reinforcement learning.
- **`accelerate`** for device placement and distributed launch, under `Trainer` and most training scripts.
- The **2025 LLM Course** replaced the older NLP course as the official curriculum.

## References

The curated link library for this topic — in this platform, videos, courses, papers, documentation, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Hugging Face — Transformers · Datasets · Hub — references](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/hugging-face/hugging-face#references-further-reading)**
