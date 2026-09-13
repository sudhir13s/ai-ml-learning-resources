---
id: "18-mlops/scaling-inference/references"
topic: "Scaling Inference (autoscaling · GPU · Ray Serve) — References"
parent: "18-mlops/scaling-inference"
type: references
updated: 2026-09-13
---

# Scaling Inference (autoscaling · GPU · Ray Serve) — references

> Companion link library for **[Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group; every entry is from a primary author or a recognized deep explainer.

**Start here — suggested path**:

1. **Frame the goal** — read [Considerations for Deploying ML Models in Production](https://www.anyscale.com/blog/considerations-for-deploying-machine-learning-models-in-production). *Throughput, latency and cost as the objective scaling serves.*
2. **See the scaling model** — watch [Introducing Ray Serve](https://www.youtube.com/watch?v=gV4YS4e1CXg). *Replicas, autoscaling and batching in one programmable layer.*
3. **Learn the signal** — read the [Ray Serve Autoscaling Guide](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) and [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/). *Scaling on ongoing requests, and the HPA defaults the simulation uses.*
4. **Share the GPUs** — read the [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/), then watch [Distributed Inference with vLLM](https://www.youtube.com/watch?v=LH2QZehVJoc). *Splitting one card for small models, then spanning several for a large one.*
5. **Connect to cost** — move to [Cost Optimization](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization). *Warm floors, batching and GPU sharing are the main levers on the inference bill.*

**In this platform**:
- [Continuous Batching and Scheduling](/ai-ml/ai-ml-learning-resources/inference-and-serving/continuous-batching-and-scheduling/continuous-batching-and-scheduling) — the scheduler that makes one GPU replica batch well.
- [Cost Optimization](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization) — autoscaling, batching and GPU sharing as levers on the inference bill.
- [Inference Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — quantization, paged attention and batching inside a replica.
- [KV Cache in Production](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-in-production) — the memory that constrains each replica, and disaggregated prefill/decode.
- [LLM Serving Engines](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) — the engine each replica runs, and what fits on one GPU.
- [ML Pipelines and Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) — the orchestration layer beneath training and serving jobs.
- [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — quality and drift signals beside the fleet metrics.
- [Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) — online versus batch serving, the step before scaling.

**Videos**:
- [Introducing Ray Serve: Scalable & Programmable ML Serving](https://www.youtube.com/watch?v=gV4YS4e1CXg) — **Anyscale (Simon Mo)** — the scaling model: replicas, autoscaling, batching.
- [Productionizing ML at Scale with Ray Serve](https://www.youtube.com/watch?v=UtH-CMpmxvI) — **Anyscale** — GPU serving and scaling under real load.
- [Ray Serve: Patterns of ML Models in Production](https://www.youtube.com/watch?v=mM4hJLelzSw) — **Anyscale (Simon Mo)** — scaling composite and multi-model pipelines.
- [vLLM Office Hours: Distributed Inference with vLLM](https://www.youtube.com/watch?v=LH2QZehVJoc) — **Neural Magic (vLLM maintainers)** — tensor and pipeline parallelism, and how they change the scaling unit.

**Courses**:
- [Made With ML — MLOps Course (serving and scaling)](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — situates scaling in the full production workflow.

**Articles**:
- [Considerations for Deploying ML Models in Production](https://www.anyscale.com/blog/considerations-for-deploying-machine-learning-models-in-production) — **Anyscale** — throughput, latency and cost as the scaling objective.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — infrastructure and scaling in the level-2 architecture.
- [Production-grade LLM inference at scale: KServe + llm-d + vLLM](https://llm-d.ai/blog/production-grade-llm-inference-at-scale-kserve-llm-d-vllm) — **llm-d project** — cache-aware routing and disaggregated serving as a Kubernetes-native pattern.
- [vLLM V1: a major upgrade to vLLM's core architecture](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html) — **vLLM maintainers** — the rewrite that made the scheduler and KV-cache manager the bottleneck to reason about.

**Papers**:
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — scalability and resource failures in production ML.

**Documentation**:
- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) — **Kubernetes** — custom Pods metrics, sync period and the stabilization window used on the page.
- [Kubernetes — Autoscaling Workloads](https://kubernetes.io/docs/concepts/workloads/autoscaling/) — **Kubernetes** — horizontal and vertical pod autoscaler fundamentals.
- [NVIDIA device plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin) — **NVIDIA** — how `nvidia.com/gpu` is advertised, with time-slicing and MIG strategies.
- [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/) — **NVIDIA** — MIG profiles, isolation guarantees and partitioning.
- [Ray Serve — Autoscaling Guide](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) — **Anyscale** — `target_ongoing_requests` and the replica bounds.
- [Ray Serve — Documentation](https://docs.ray.io/en/latest/serve/index.html) — **Anyscale** — scalable serving with built-in autoscaling and batching.
- [Serving LLMs with Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html) — **Anyscale** — multi-node LLM deployments with autoscaling and prefill/decode disaggregation.
- [SGLang documentation](https://docs.sglang.ai/) — **SGLang team** — the RadixAttention scheduler, the main open alternative to vLLM.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — **NVIDIA** — compiled kernels and in-flight batching on NVIDIA hardware.
- [Time-Slicing GPUs in Kubernetes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html) — **NVIDIA GPU Operator** — GPU sharing without memory or fault isolation.
- [vLLM — Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics.html) — **vLLM maintainers** — `num_requests_waiting`, `kv_cache_usage_perc` and the latency histograms to scale and alert on.

**Books**:
- [Designing Machine Learning Systems — Ch. 7 "Model Deployment" and Ch. 10 "Infrastructure and Tooling"](https://huyenchip.com/mlops/) — **Chip Huyen** — scaling and GPU infrastructure in context.
- [Machine Learning Engineering — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — scaling and throughput patterns.
