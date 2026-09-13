---
id: "18-mlops/model-packaging-and-containerization/references"
topic: "Model Packaging & Containerization (Docker) — References"
parent: "18-mlops/model-packaging-and-containerization"
type: references
updated: 2026-09-13
---

# Model Packaging & Containerization (Docker) — references

> Companion link library for **[Model Packaging and Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group; every entry is from a primary author or a recognized deep explainer.

**Start here — suggested path**:

1. **Learn containers** — read [Docker: Get Started](https://docs.docker.com/get-started/). *Images, containers and Dockerfiles, from the maintainers.*
2. **Build production images** — read [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) and [Docker build cache](https://docs.docker.com/build/cache/). *Layer order, multi-stage builds and slim images — the reason the artifact layer goes last.*
3. **Do it the MLOps way** — work through [Made With ML: Docker](https://madewithml.com/courses/mlops/docker/). *Packaging inside a real serving workflow, with a clean interface.*
4. **Pick the weight format** — read [safetensors](https://huggingface.co/docs/safetensors/index) and the [GGUF specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md). *Why pickled checkpoints are a supply-chain risk, and what replaced them.*
5. **Connect to serving** — move to [Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving). *The image is what a serving runtime runs; packaging and serving are two halves of deployment.*

**In this platform**:
- [A/B testing, shadow and canary deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) — releasing the packaged image gradually.
- [Data and Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) — the data snapshot and weights version an artifact points at.
- [LLM Serving Engines](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) — how an LLM's weights directory is loaded and served.
- [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance) — versions, stages and the promotion gate that reads the manifest's metrics.
- [Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) — exposing the artifact behind an API.
- [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — weight formats and their size/accuracy trade-off.
- [Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) — pinning seeds and environments so the artifact can be rebuilt.
- [Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference) — running many copies of the image under variable load.

**Videos**:
- [Introducing Docker Model Runner](https://www.youtube.com/watch?v=zQi-8mCTNf8) — **Docker** — models pulled as OCI artifacts from a registry rather than baked into an image.
- [Web Deployment — Testing & Deployment](https://www.youtube.com/watch?v=1BegV7gjqDo) — **The Full Stack** — packaging a trained model behind a web interface, with the trade-offs spelled out.

**Courses**:
- [Docker — Get Started Guide](https://docs.docker.com/get-started/) — **Docker** — hands-on introduction to images and containers.
- [Made With ML — Docker](https://madewithml.com/courses/mlops/docker/) — **Goku Mohandas** — package an ML application into a reproducible image.

**Articles**:
- [Cog — Containers for ML](https://cog.run/) — **Replicate** — opinionated ML packaging on top of Docker: GPU, weights, predict interface.

**Papers**:
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — environment and dependency failures that containerization prevents.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — configuration and environment debt; packaging is part of the cure.

**Documentation**:
- [Docker build cache](https://docs.docker.com/build/cache/) — **Docker** — how layer caching decides what rebuilds.
- [Docker Model Runner](https://docs.docker.com/ai/model-runner/) — **Docker** — models distributed as OCI artifacts and run beside containers.
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) — **Docker** — layers, caching, multi-stage builds, slim images.
- [GGUF format specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md) — **ggml (Georgi Gerganov et al.)** — single-file quantized weights plus metadata, behind llama.cpp and Ollama.
- [ONNX Runtime documentation](https://onnxruntime.ai/docs/) — **Microsoft / ONNX Runtime** — exporting to a framework-neutral graph and the execution providers that run it.
- [safetensors](https://huggingface.co/docs/safetensors/index) — **Hugging Face** — the zero-copy weight format that stores tensors and nothing that can execute.

**Books**:
- [Designing Machine Learning Systems — Ch. 7 "Model Deployment and Prediction Service"](https://huyenchip.com/mlops/) — **Chip Huyen** — packaging and serving in context.
- [Machine Learning Engineering — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — packaging and deployment patterns.
