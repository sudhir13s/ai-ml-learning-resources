---
id: "18-mlops/model-packaging-and-containerization"
topic: "Model Packaging & Containerization (Docker)"
parent: "18-mlops-and-deployment"
level: intermediate
built_from: ["reproducibility", "software-engineering"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Model Packaging & Containerization (Docker)"
minutes: 10
category: packaging-and-serving
---

# Model Packaging & Containerization — Docker
> Bundling a model, its serving code, and every dependency into a portable, reproducible artifact —
> usually a Docker image — that runs identically on a laptop, in CI, and in production. The unit of
> deployment that makes "works on my machine" a non-problem.

**Why it matters:** "how do you ship a trained model to production?" Interviewers probe the artifact
(weights + code + env + interface), why containers solve dependency/parity problems, Dockerfile
fundamentals (layers, caching, slim/multi-stage builds, pinned base images), and ML-specific packaging.
Know the 2026 weight formats too: **safetensors** (the default on the Hugging Face Hub — zero-copy,
no `pickle` code-execution risk), **GGUF** (quantized weights for llama.cpp-class local runtimes),
**ONNX** (framework-neutral graph for ONNX Runtime), and CUDA base images that pin the driver/toolkit
pair. The bridge from "trained" to "served."

**Start here — suggested path:**

1. **Learn containers** — read [Docker: Get Started](https://docs.docker.com/get-started/). *Images, containers, Dockerfiles — the foundation, from the maintainers.*
2. **Build production images** — read [Docker: Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) and [Docker: build cache](https://docs.docker.com/build/cache/). *Layer caching, multi-stage builds, slim images — what separates a toy image from a deployable one.*
3. **Do it the MLOps way** — work [Made With ML: Docker](https://madewithml.com/courses/mlops/docker/). *Packaging within a real serving workflow, with a clean interface.*
4. **Pick the weight format** — read [safetensors](https://huggingface.co/docs/safetensors/index) and the [GGUF spec](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md). *Why `torch.save` pickles are a supply-chain risk and what replaced them.*
5. **Connect to serving** — move to [09 Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving). *The image is the artifact a serving runtime runs; packaging and serving are two halves of deployment.*

## Courses (free)
- [Made With ML — Docker](https://madewithml.com/courses/mlops/docker/) — **Goku Mohandas** — package an ML app into a reproducible image.
- [Docker — Get Started Guide](https://docs.docker.com/get-started/) — **Docker** — official, hands-on intro to images and containers.

## Videos
- [Introducing Docker Model Runner](https://www.youtube.com/watch?v=zQi-8mCTNf8) — **Docker** — the 2025 shift: models pulled as **OCI artifacts** from a registry rather than baked into an image.
- [Web Deployment — Testing & Deployment](https://www.youtube.com/watch?v=1BegV7gjqDo) — **The Full Stack** — packaging a trained model behind a web interface, with the trade-offs spelled out.

## Key Papers
- [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — environment/dependency failures that containerization prevents.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — config and environment debt; packaging is part of the cure.

## Articles / Blogs (free, no paywall)
- [Dockerfile Best Practices](https://docs.docker.com/build/building/best-practices/) — **Docker** — layers, caching, multi-stage, slim images.
- [Docker Model Runner](https://docs.docker.com/ai/model-runner/) — **Docker** — models distributed as OCI artifacts and run beside containers; the 2025–26 packaging direction for local and edge inference.
- [safetensors](https://huggingface.co/docs/safetensors/index) — **Hugging Face** — the zero-copy, no-arbitrary-code weight format that replaced pickled checkpoints as the Hub default.
- [GGUF format specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md) — **ggml (Georgi Gerganov et al.)** — single-file quantized weights + metadata, the format behind llama.cpp and Ollama.
- [ONNX Runtime documentation](https://onnxruntime.ai/docs/) — **Microsoft / ONNX Runtime** — exporting to a framework-neutral graph and the execution providers that then run it.
- [Cog — Containers for ML](https://cog.run/) — **Replicate** — opinionated, ML-specific packaging on top of Docker (GPU, weights, predict interface).

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 7 "Model Deployment & Prediction Service"** (packaging & serving)](https://huyenchip.com/mlops/) — **Chip Huyen** — author notes/talks free.
- [Machine Learning Engineering — **Ch. 8 "Model Deployment"**](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — packaging and deployment patterns; read-first chapters free.

## In this platform
- Builds on: [02 Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility)
- Next concepts: [09 Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) · [10 Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference)
- Weight formats and their size/accuracy trade-off: [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization)
- Related concept (covered elsewhere): LLM-specific serving stacks → [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
