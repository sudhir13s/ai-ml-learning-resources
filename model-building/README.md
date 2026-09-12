---
id: "model-building"
topic: "Model Building"
level: advanced
built_from: ["large-language-models", "data-and-representation", "optimization-and-training"]
updated: 2026-09-13
---

# Model Building

> Training a model from nothing: the corpus, the tokenizer, the architecture, the run, and the
> curves you read while it trains. The pretraining page says how it is done at scale; the
> ten-page build does it at laptop scale, from random weights to a generating model. The
> Practitioner Workflows model-training workflow harvests in here in the next wave, so that
> everything that *makes* a model has one home.

**Start here:** [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) — corpora and deduplication, mixed precision, parallelism, model FLOPs utilization, and the failure modes of a long run — then build one: [Why Build a Model From Scratch](/ai-ml/ai-ml-learning-resources/model-building/build-a-small-language-model/why-build-a-model-from-scratch).

## Topics

1. [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) — the industrial process of turning a corpus and a compute budget into a base model.
2. [Build a Small Language Model](/ai-ml/ai-ml-learning-resources/model-building/build-a-small-language-model/why-build-a-model-from-scratch) — **10 pages** — a 12.2M-parameter decoder-only transformer from random weights: corpus → clean and deduplicate → byte-level tokenizer → architecture → gradient proof → pretraining → training curves → perplexity and generation → capabilities and limits. About twelve minutes on a processor.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang and Tatsunori Hashimoto (Stanford)** — you build the tokenizer, the model, the training loop and the inference path yourself; the current best course on this material.
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — builds a decoder-only GPT from backpropagation upward in plain Python.

## Videos

- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **Andrej Karpathy** — a full pretraining run, spelled out.
- [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) — **Andrej Karpathy** — byte-pair encoding and why LLMs are weird at characters and arithmetic.

## Key Papers

- [Training Compute-Optimal Large Language Models (Chinchilla)](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (DeepMind, 2022)** — the compute-optimal correction that reset how everyone allocates a training budget.
- [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) — **Touvron et al. (Meta, 2023)** — the modern decoder recipe and a public training report.

## Articles / Blogs (free, no paywall)

- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI (Quentin Anthony et al.)** — the `C ≈ 6ND` compute arithmetic and full memory accounting behind any pretraining budget.
- [The Ultra-Scale Playbook: Training LLMs on GPU Clusters](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Hugging Face nanotron team** — the current canonical text on large-scale distributed training.
- [FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face** — a web-scale pretraining data pipeline documented in full.

## Books (free, with chapters)

- [*How to Scale Your Model*](https://jax-ml.github.io/scaling-book/) — **Google DeepMind (Austin et al.)** — free online; the parameter, FLOP and memory accounting that turns architecture choices into budget numbers.

## In this platform

- Before this section: [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — what is being built · [Data and Representation](/ai-ml/ai-ml-learning-resources/data-and-representation/readme) — what it is built from
- After this section: [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme) · [Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/readme)
- Where the training compute comes from: [Training Infrastructure](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/readme) — [Distributed Training — Parallelism, FSDP and ZeRO](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) · [GPUs and Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning)
- The mental models: [Neural Scaling Laws and Chinchilla](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/scaling-behavior/neural-scaling-laws-and-chinchilla-intuition) · [Tokenization and BPE](/ai-ml/ai-ml-intuitions/representation/discrete-representations/tokenization-and-bpe-intuition)
- The training loop as a workflow (harvests in here at W3): [Model Training workflow](/ai-ml/practitioner-workflows/training-and-adaptation/model-training) · The production spine the build points at: [small-language-model](/python/python-production-examples/small-language-model/readme)
