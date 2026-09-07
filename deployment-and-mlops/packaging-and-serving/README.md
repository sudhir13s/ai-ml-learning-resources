---
id: "deployment-and-mlops/packaging-and-serving"
topic: "Packaging and Serving"
level: advanced
built_from: ["lifecycle-and-reproducibility", "tools-and-frameworks"]
updated: 2026-09-07
---

# Packaging and Serving

> Turning a trained artifact into something an application can call. Three decisions in sequence:
> what the deployable unit is (an image containing the model, its serving code and every
> dependency), how predictions are requested (online per-request versus batch over a dataset),
> and how the service survives real traffic (replicas, the right autoscaling signal, request
> batching, shared accelerators).

**Start here:** [Model Packaging and Containerization](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization) — the unit of deployment has to exist before serving or scaling means anything.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### The deployable unit

1. [Model Packaging and Containerization](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization) — model plus serving code plus dependencies as one reproducible image; layers, caching and slim builds.

### Exposing predictions

2. [Model Serving](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/model-serving/model-serving) — REST versus gRPC, online versus batch, and what BentoML, Triton and TF-Serving each give you.

### Surviving traffic

3. [Scaling Inference](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/scaling-inference/scaling-inference) — replicas and autoscaling on queue depth or latency rather than CPU, GPU packing and sharing, and request batching.

## Courses (free)

- [Made With ML — MLOps Course](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — the Docker and API lessons build exactly this sub-area's three pages inside one working project.
- [Docker — Get Started Guide](https://docs.docker.com/get-started/) — **Docker** — the official hands-on introduction to images and containers; the correct place to learn the primitives.
- [BentoML documentation](https://docs.bentoml.com/en/latest/) — **BentoML maintainers** — turning any model into a REST or gRPC service with batching and packaging, from the maintainers.
- [Ray Serve documentation](https://docs.ray.io/en/latest/serve/index.html) — **Anyscale** — scalable serving with built-in autoscaling, batching and model composition.

## Videos

- [Introduction to Model Deployment with Ray Serve](https://www.youtube.com/watch?v=TdjJpAHLuxQ) — **Anyscale** — programmable online serving and composing several models into one endpoint.
- [Ray Serve: Patterns of ML Models in Production](https://www.youtube.com/watch?v=mM4hJLelzSw) — **Simon Mo (Anyscale)** — the serving pattern catalogue: pipelines, ensembles, business logic between models.
- [Introducing Ray Serve: Scalable and Programmable ML Serving](https://www.youtube.com/watch?v=gV4YS4e1CXg) — **Simon Mo (Anyscale)** — the scaling model in detail: replicas, autoscaling, batching.
- [MLOps Zoomcamp 4.1 — Three Ways of Deploying a Model](https://www.youtube.com/watch?v=JMGe4yIoBRA) — **DataTalks.Club** — web service versus streaming versus batch, and how to pick.

## Key Papers

- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma and Lawrence (2020)** — the environment and dependency failures that containerization exists to prevent, catalogued from real projects.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — where the prediction service sits in the reference architecture.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — configuration and environment debt; packaging is part of the cure.

## Articles / Blogs (free, no paywall)

- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) — **Docker** — layers, cache ordering, multi-stage builds and slim images; the difference between a 300 MB and a 6 GB model image.
- [Static versus dynamic inference](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-inference) — **Google** — the batch-versus-online trade-off stated in its cleanest form.
- [Serving ML Models in Production: Common Patterns](https://www.anyscale.com/blog/serving-ml-models-in-production-common-patterns) — **Anyscale** — the four serving architectures and when each applies.
- [Ray Serve — Autoscaling Guide](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) — **Anyscale** — which signal to autoscale inference on, and why CPU utilization is the wrong one.
- [Cog — Containers for ML](https://cog.run/) — **Replicate** — opinionated ML-specific packaging on top of Docker: GPU base images, weights and a predict interface.

## Books (free, with chapters)

- [*Designing Machine Learning Systems* — Ch. 7 "Model Deployment and Prediction Service"](https://huyenchip.com/mlops/) — **Chip Huyen** — the reference chapter on packaging and serving; author notes and companion code free.
- [*Machine Learning Engineering* — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — deployment patterns and their trade-offs; read-first chapters free.
- [*Site Reliability Engineering*](https://sre.google/books/) — **Google** — free online; the load-balancing, overload-handling and capacity chapters apply directly to an inference service.

## In this platform

- Section index: [MLOps and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
- Sibling sub-areas: [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/readme) · [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/readme) · [Release and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/readme) · [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/readme) · [Governance and Economics](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/readme)
- Serving an LLM specifically, in depth: [Inference Optimization and Serving](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization) · [Continuous Batching and Scheduling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/continuous-batching-and-scheduling/continuous-batching-and-scheduling) · [Quantization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/quantization/quantization)
- What happens right after this: [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) · [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
- Doing it rather than reading it: [Model Serving workflow](/ai-ml/practitioner-workflows/inference-and-serving/model-serving) · [MLOps and Deployment workflow](/ai-ml/practitioner-workflows/production-lifecycle/mlops-and-deployment)
