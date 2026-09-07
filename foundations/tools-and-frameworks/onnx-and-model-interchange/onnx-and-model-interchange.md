---
id: "17-tools-and-frameworks/onnx"
topic: "ONNX & Model Interchange (export, runtime, portability)"
parent: "17-tools-and-frameworks"
level: intermediate
built_from: ["python", "pytorch", "neural-networks"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "ONNX & Model Interchange (export, runtime, portability)"
minutes: 10
category: tools-and-frameworks
---

# ONNX & Model Interchange — Export · Runtime · Portability
> The **Open Neural Network Exchange**: a standard, framework-agnostic format for representing models
> as a computation graph, plus **ONNX Runtime**, a high-performance cross-platform inference engine.
> Train in PyTorch or TensorFlow, export to ONNX, and run anywhere — server, browser, mobile, edge —
> with graph optimizations and hardware acceleration.

**Why it matters:** model portability and inference performance are core deployment concerns, and
ONNX is the lingua franca that decouples training framework from serving target. Interviews and
real work touch on why you'd export to ONNX, how the graph + opsets work, ONNX Runtime's graph
optimizations (fusion, constant folding), and how it enables hardware-specific execution providers.

**Interchange in 2026 — ONNX is one of three formats, and you should know which is which:**

- **ONNX** — a full computation graph plus opsets; the portable choice for classical models, vision, speech and embedded targets, executed by ONNX Runtime with per-hardware execution providers.
- **safetensors** — weights only, no graph: the Hub's default checkpoint format, chosen because it loads zero-copy and cannot execute arbitrary code the way `pickle` can.
- **GGUF** — weights plus metadata plus quantization, aimed at `llama.cpp` and local runners such as Ollama; the format behind consumer-hardware LLM inference.

The rule of thumb: **ONNX for portable graphs, safetensors for training and serving weights, GGUF for local quantized LLMs.**

**Start here — suggested path:**

1. **Grasp the concept** — read [ONNX Concepts](https://onnx.ai/onnx/intro/concepts.html). *Understand the model-as-graph + operators/opsets idea — that's the whole format.*
2. **See an export end to end** — [Export a PyTorch model to ONNX](https://pytorch.org/tutorials/beginner/onnx/intro_onnx.html). *The canonical workflow: train → `torch.onnx.export` → run with ONNX Runtime.*
3. **Know the neighbouring formats** — skim [safetensors](https://huggingface.co/docs/safetensors/index) and [GGUF on the Hub](https://huggingface.co/docs/hub/gguf). *Half of "which format?" questions are really "graph or weights?" — this settles them.*
4. **Learn the runtime** — read the [ONNX Runtime docs](https://onnxruntime.ai/docs/) and watch [Introduction to ONNX Runtime](https://www.youtube.com/watch?v=Wp5PaRpudlk). *The optimizations + execution providers are what make ONNX worth it in production.*
5. **Adapt a tutorial** — browse [onnx/tutorials](https://github.com/onnx/tutorials) for your framework. *Find the closest conversion example and adapt it.*

## Courses (free)
- [ONNX documentation](https://onnx.ai/onnx/intro/concepts.html) — **ONNX team** — the official intro to the format, graphs, and operators.
- [ONNX Runtime documentation](https://onnxruntime.ai/docs/) — **ONNX Runtime team (Microsoft)** — the guide to optimizing and deploying ONNX models.
- [onnx/tutorials](https://github.com/onnx/tutorials) — **ONNX team** — a free collection of conversion and inference tutorials across frameworks.

## Videos
- [Introduction to ONNX Runtime](https://www.youtube.com/watch?v=Wp5PaRpudlk) — **NVIDIA Developer** — the runtime, its graph optimizations, and accelerated inference.
- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **Andrej Karpathy** — the training-side PyTorch graph you will be exporting, including the precision choices that decide what survives export.

## Key Papers
- [ONNX Concepts (format specification)](https://onnx.ai/onnx/intro/concepts.html) — **ONNX team** — the authoritative description of the interchange format.
- [ONNX Runtime documentation](https://onnxruntime.ai/docs/) — **Microsoft** — the canonical reference for the inference engine and its optimizations.

## Articles / Blogs (free, no paywall)
- [ONNX home](https://onnx.ai/) — **ONNX team** — what ONNX is and the ecosystem around it.
- [Export a PyTorch model to ONNX](https://pytorch.org/tutorials/beginner/onnx/intro_onnx.html) — **PyTorch team** — the end-to-end export + run workflow.
- [ONNX Runtime home](https://onnxruntime.ai/) — **Microsoft** — the cross-platform, accelerated inference engine.
- [safetensors](https://huggingface.co/docs/safetensors/index) — **Hugging Face** — the weights-only interchange format used across the Hub, and why it replaced pickled checkpoints.
- [GGUF](https://huggingface.co/docs/hub/gguf) — **Hugging Face** — the quantized single-file format consumed by `llama.cpp` and Ollama for local LLM inference.
- [Optimum](https://huggingface.co/docs/optimum/index) — **Hugging Face** — the bridge that exports Transformers models to ONNX Runtime and other accelerators without hand-writing the export.

## Books (free, with chapters)
- [onnx/tutorials (collection)](https://github.com/onnx/tutorials) — **ONNX team** — a free, chapter-like set of conversion/inference guides.
- [ONNX Runtime documentation (full)](https://onnxruntime.ai/docs/) — **Microsoft** — a book-length, free guide to deployment and optimization.

## In this platform
- Related domain: [12. Deployment & MLOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme) · [05. Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
- Pairs with: [05 PyTorch](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pytorch/pytorch) · [06 TensorFlow & Keras](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/tensorflow-and-keras/tensorflow-and-keras)
- Deeper concept (the *why*): model serving & optimization → [Deployment & MLOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
