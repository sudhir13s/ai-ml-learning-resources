---
id: "18-mlops/scaling-inference"
topic: "Scaling Inference (autoscaling · GPU · Ray Serve)"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["model-serving", "distributed-systems"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Scaling Inference (autoscaling · GPU · Ray Serve)"
minutes: 10
category: packaging-and-serving
---

# Scaling Inference — Autoscaling · GPU · Ray Serve
> Meeting variable demand without over-paying: horizontally scale replicas, autoscale on the right
> signal (queue depth / latency, not just CPU), pack and share GPUs, and batch requests to raise
> throughput. The systems layer that turns a single prediction service into one that survives traffic spikes.

**Why it matters:** the "your model gets 10× traffic at peak — how do you scale it cost-effectively?"
question. Interviewers want horizontal vs vertical scaling, the right autoscaling metric (queue depth /
concurrency beats CPU% for inference), GPU specifics (cold starts, sharing/MIG, batching for utilization),
and tools like Ray Serve + Kubernetes horizontal pod autoscaler (HPA). For large language models
(LLMs), add the 2025–26 layer: **continuous batching**, tensor/pipeline parallelism across GPUs, and
**disaggregated prefill/decode** — running the compute-bound prompt phase and the memory-bound token
phase on separately scaled pools, with cache-aware routing between them. The bridge between serving
and cost.

**Start here — suggested path:**

1. **Frame the goal** — read [Considerations for Deploying ML Models in Production](https://www.anyscale.com/blog/considerations-for-deploying-machine-learning-models-in-production). *Throughput, latency, and cost as the scaling objective function.*
2. **Learn the autoscaling signal** — read [Ray Serve Autoscaling Guide](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) and [Kubernetes Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/). *Why queue depth/concurrency is the right metric for inference, not CPU%.*
3. **See it in a framework** — read [Ray Serve docs](https://docs.ray.io/en/latest/serve/index.html) and watch [Introducing Ray Serve](https://www.youtube.com/watch?v=gV4YS4e1CXg). *Replicas, autoscaling, and batching in one programmable layer.*
4. **Scale on GPUs** — watch [Productionizing ML at Scale with Ray Serve](https://www.youtube.com/watch?v=UtH-CMpmxvI), then [Distributed Inference with vLLM](https://www.youtube.com/watch?v=LH2QZehVJoc). *GPU packing and multi-model serving, then what changes once one model no longer fits on one GPU.*
5. **Connect to cost** — move to [16 Cost Optimization](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization). *Autoscaling, batching, and GPU sharing are the main levers on the inference bill.*

## Courses (free)
- [Ray Serve — Documentation](https://docs.ray.io/en/latest/serve/index.html) — **Anyscale** — scalable serving with built-in autoscaling and batching.
- [Made With ML — MLOps Course (serving & scaling)](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — situates scaling in the full production workflow.

## Videos
- [Introducing Ray Serve: Scalable & Programmable ML Serving](https://www.youtube.com/watch?v=gV4YS4e1CXg) — **Anyscale (Simon Mo)** — the scaling model: replicas, autoscaling, batching.
- [Ray Serve: Patterns of ML Models in Production](https://www.youtube.com/watch?v=mM4hJLelzSw) — **Anyscale (Simon Mo)** — scaling composite/multi-model pipelines.
- [Productionizing ML at Scale with Ray Serve](https://www.youtube.com/watch?v=UtH-CMpmxvI) — **Anyscale** — GPU serving and scaling under real load.
- [vLLM Office Hours: Distributed Inference with vLLM](https://www.youtube.com/watch?v=LH2QZehVJoc) — **Neural Magic (vLLM maintainers)** — when one GPU stops being enough: tensor and pipeline parallelism, and how they change the scaling unit.

## Key Papers
- [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — scalability and resource failures in production ML.
- [MLOps: Continuous delivery and automation pipelines in ML](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — infrastructure and scaling in the level-2 architecture.

## Articles / Blogs (free, no paywall)
- [Considerations for Deploying ML Models in Production](https://www.anyscale.com/blog/considerations-for-deploying-machine-learning-models-in-production) — **Anyscale** — throughput/latency/cost trade-offs that drive scaling.
- [Ray Serve — Autoscaling Guide](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) — **Anyscale** — the right autoscaling signals for inference.
- [Kubernetes — Autoscaling Workloads](https://kubernetes.io/docs/concepts/workloads/autoscaling/) — **Kubernetes** — horizontal and vertical pod autoscaler fundamentals underneath ML autoscaling.
- [vLLM V1: a major upgrade to vLLM's core architecture](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html) — **vLLM maintainers** — the 2025 rewrite that made the scheduler and KV-cache manager the scaling bottleneck to reason about.
- [Serving LLMs with Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html) — **Anyscale** — multi-node LLM deployments with autoscaling, parallelism strategies, and prefill/decode disaggregation.
- [Production-grade LLM inference at scale: KServe + llm-d + vLLM](https://llm-d.ai/blog/production-grade-llm-inference-at-scale-kserve-llm-d-vllm) — **llm-d project** — cache-aware routing and disaggregated serving as a Kubernetes-native scaling pattern.
- [SGLang documentation](https://docs.sglang.ai/) — **SGLang team** — the RadixAttention prefix-cache scheduler; the main open alternative to vLLM when prompt reuse dominates.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — **NVIDIA** — compiled kernels and in-flight batching when you are pinned to NVIDIA hardware and want the last 20% of throughput.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 7 "Model Deployment"** & **Ch. 10 "Infrastructure & Tooling"** (scaling, GPUs)](https://huyenchip.com/mlops/) — **Chip Huyen** — author notes/talks free.
- [Machine Learning Engineering — **Ch. 8 "Model Deployment"** (scaling & throughput)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

## In this platform
- Builds on: [06 ML Pipelines & Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) · [09 Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving)
- Next concepts: [16 Cost Optimization](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization)
- The scheduler that makes GPU inference scale: [Continuous Batching & Scheduling](/ai-ml/ai-ml-learning-resources/inference-and-serving/continuous-batching-and-scheduling/continuous-batching-and-scheduling)
- The memory that constrains it: [KV Cache in Production](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-in-production)
- Related concept (covered elsewhere): LLM inference optimization (quantization, paged attention, batching) → [LLMs — Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)
