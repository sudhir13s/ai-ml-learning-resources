---
id: "18-mlops/model-serving"
topic: "Model Serving (REST/gRPC · batch vs online · BentoML/Triton/TF-Serving)"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["model-packaging-and-containerization", "apis"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Model Serving (REST/gRPC · batch vs online · BentoML/Triton/TF-Serving)"
minutes: 10
category: packaging-and-serving
---

# Model Serving — REST/gRPC · Batch vs Online · BentoML · Triton · TF-Serving
> Exposing a model so applications can get predictions: wrap it behind an API (REST or gRPC), or run it
> over a dataset in bulk. The choice — **online** (low-latency, per-request) vs **batch/offline**
> (high-throughput, scheduled) — and the runtime (BentoML, Triton, TF-Serving) shape your whole
> production architecture.

**Why it matters:** the single most common deployment question. Interviewers want the online vs batch
trade-off (latency vs throughput vs cost), REST vs gRPC, request batching, why purpose-built servers
(Triton, BentoML, KServe) beat a hand-rolled Flask app, and the prediction-service contract
(versioning, warmup, health checks). For a large language model (LLM) the same question has a
2026 answer: an inference engine — **vLLM**, SGLang, or TensorRT-LLM — fronted by **KServe** or
**Ray Serve**, with continuous batching and a paged KV cache doing the work request batching used to.

**Start here — suggested path:**

1. **Get the split** — read [Google: Static vs Dynamic (batch vs online) Inference](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-inference). *The first decision; everything else follows from it.*
2. **See the patterns** — read [Serving ML Models in Production: Common Patterns](https://www.anyscale.com/blog/serving-ml-models-in-production-common-patterns). *Pipeline, ensemble, online/offline — the vocabulary of serving architectures.*
3. **Build a REST service** — work [Made With ML: API](https://madewithml.com/courses/mlops/api/), then follow [BentoML: Hello World](https://docs.bentoml.com/en/latest/get-started/hello-world.html). *Model → versioned REST endpoint in minutes.*
4. **See the deployment modes** — watch [MLOps Zoomcamp: Three Ways of Deploying a Model](https://www.youtube.com/watch?v=JMGe4yIoBRA). *Web service vs streaming vs batch, side by side.*
5. **Meet the high-perf servers** — skim [Triton Inference Server docs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html), [KServe architecture](https://kserve.github.io/website/docs/concepts/architecture) and [vLLM docs](https://docs.vllm.ai/en/latest/). *Dynamic batching, multi-framework, GPU, scale-to-zero — why these exist.*

## Courses (free)
- [Made With ML — Serving / API](https://madewithml.com/courses/mlops/api/) — **Goku Mohandas** — design and ship a production prediction API.
- [BentoML — Documentation](https://docs.bentoml.com/en/latest/) — **BentoML** — turn any model into a REST/gRPC service with batching and packaging.

## Videos
- [MLOps Zoomcamp 4.1 — Three Ways of Deploying a Model](https://www.youtube.com/watch?v=JMGe4yIoBRA) — **DataTalksClub** — web service vs streaming vs batch.
- [Introduction to Model Deployment with Ray Serve](https://www.youtube.com/watch?v=TdjJpAHLuxQ) — **Toronto Machine Learning Society (TMLS)** — programmable online serving and composition.
- [Ray Serve: Patterns of ML Models in Production](https://www.youtube.com/watch?v=mM4hJLelzSw) — **Anyscale (Simon Mo)** — serving patterns: pipelines, ensembles, business logic.
- [vLLM Office Hours: Intro to vLLM V1](https://www.youtube.com/watch?v=jmzIvQZCLZM) — **Neural Magic (vLLM maintainers)** — the V1 rewrite: scheduler, memory manager, and API server, explained by the people who wrote it.

## Key Papers
- [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — real serving/latency/scaling failures from industry.
- [MLOps: Continuous delivery and automation pipelines in ML](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — where the prediction service sits in the architecture.

## Articles / Blogs (free, no paywall)
- [Static vs Dynamic Inference (batch vs online)](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-inference) — **Google** — the foundational serving trade-off.
- [Serving ML Models in Production: Common Patterns](https://www.anyscale.com/blog/serving-ml-models-in-production-common-patterns) — **Anyscale** — the serving-architecture pattern catalog.
- [KServe — System Architecture Overview](https://kserve.github.io/website/docs/concepts/architecture) — **KServe (CNCF)** — control plane vs data plane, InferenceService, scale-to-zero: the Kubernetes-native serving model.
- [vLLM Documentation](https://docs.vllm.ai/en/latest/) — **vLLM maintainers** — the reference engine for LLM serving: paged attention, continuous batching, OpenAI-compatible server.
- [Production-grade LLM inference at scale: KServe + llm-d + vLLM](https://llm-d.ai/blog/production-grade-llm-inference-at-scale-kserve-llm-d-vllm) — **llm-d project** — how the 2025–26 stack composes: KServe for the control plane, llm-d for cache-aware routing and disaggregation, vLLM as the engine.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 7 "Model Deployment & Prediction Service"** (batch vs online, REST/gRPC)](https://huyenchip.com/mlops/) — **Chip Huyen** — author notes/talks free.
- [Machine Learning Engineering — **Ch. 8 "Model Deployment"** (serving patterns)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

## In this platform
- Builds on: [08 Model Packaging & Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization)
- How an LLM server actually batches requests: [Continuous Batching & Scheduling](/ai-ml/ai-ml-learning-resources/inference-and-serving/continuous-batching-and-scheduling/continuous-batching-and-scheduling)
- Next concepts: [10 Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference) · [11 Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) · [14 A/B Testing · Shadow & Canary](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment)
- Related concept (covered elsewhere): LLM inference internals (KV-cache, paged attention) → [LLMs — Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)
