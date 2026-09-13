---
id: "18-mlops/model-serving/references"
topic: "Model Serving — References"
parent: "18-mlops/model-serving"
type: references
updated: 2026-09-14
---

# Model Serving — references

> Companion link library for **[Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group; every entry is from a primary author or a recognized deep explainer.

**Start here — suggested path**:

1. **See an engine from its creators** — watch [Fast LLM Serving with vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U). *Paging and batching explained by the people who built them.*
2. **Get the first split** — read [Static vs Dynamic Inference](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-inference). *Online or batch decides everything after it.*
3. **Learn the serving patterns** — read [Serving ML Models in Production: Common Patterns](https://www.anyscale.com/blog/serving-ml-models-in-production-common-patterns). *Pipelines, ensembles and online/offline, the vocabulary of serving architectures.*
4. **Stand one up** — work through [vLLM — Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/). *`vllm serve` and the OpenAI-compatible endpoints the teaching page uses.*
5. **Put it on a platform** — skim [KServe — System Architecture Overview](https://kserve.github.io/website/docs/concepts/architecture). *Control plane, data plane and scale-to-zero around the engine.*

**In this platform**:
- [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) — releasing a new model behind a live endpoint.
- [Continuous Batching and Scheduling](/ai-ml/ai-ml-learning-resources/inference-and-serving/continuous-batching-and-scheduling/continuous-batching-and-scheduling) — the per-step scheduler every engine runs.
- [Inference Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — why decode is memory-bound, PagedAttention and the serving levers.
- [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — the per-token cache formula behind every block on the page.
- [KV Cache in Production](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-in-production) — the engines' cache bets, preemption and disaggregated serving.
- [LoRA and Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — the adapters swapped per tenant.
- [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — watching the endpoint once it serves traffic.
- [Model Packaging and Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization) — shipping weights safely before an engine loads them.
- [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — the quality and cost side of the precision table.
- [Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference) — many engine replicas under variable traffic.
- [Speculative Decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) — a latency lever for the decode loop.

**Videos**:
- [Fast LLM Serving with vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U) — **Anyscale** — the vLLM authors on paging and batching.
- [Introduction to Model Deployment with Ray Serve](https://www.youtube.com/watch?v=TdjJpAHLuxQ) — **Toronto Machine Learning Society (TMLS)** — programmable online serving and composition.
- [MLOps Zoomcamp 4.1 — Three Ways of Deploying a Model](https://www.youtube.com/watch?v=JMGe4yIoBRA) — **DataTalksClub** — web service vs streaming vs batch, side by side.
- [Ray Serve: Patterns of ML Models in Production](https://www.youtube.com/watch?v=mM4hJLelzSw) — **Anyscale (Simon Mo)** — serving patterns: pipelines, ensembles, business logic.
- [vLLM Office Hours: Distributed Inference with vLLM](https://www.youtube.com/watch?v=LH2QZehVJoc) — **Neural Magic (vLLM maintainers)** — what changes once one model spans several GPUs.
- [vLLM Office Hours: Intro to vLLM V1](https://www.youtube.com/watch?v=jmzIvQZCLZM) — **Neural Magic (vLLM maintainers)** — the V1 rewrite: scheduler, memory manager and API server.
- [vLLM: Easy, Fast, and Cheap LLM Serving for Everyone](https://www.youtube.com/watch?v=9ih0EmcXRHE) — **PyTorch (Woosuk Kwon and Xiaoxuan Liu, UC Berkeley)** — engine architecture from its creators.

**Courses**:
- [Made With ML — Serving / API](https://madewithml.com/courses/mlops/api/) — **Goku Mohandas** — design and ship a production prediction API.

**Articles**:
- [How continuous batching enables 23x throughput in LLM inference while reducing p50 latency](https://www.anyscale.com/blog/continuous-batching-llm-inference) — **Anyscale (Cade Daniel et al.)** — the canonical measurement of batching in real engines.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — where the prediction service sits in the architecture.
- [Production-grade LLM inference at scale: KServe + llm-d + vLLM](https://llm-d.ai/blog/production-grade-llm-inference-at-scale-kserve-llm-d-vllm) — **llm-d project** — KServe for the control plane, llm-d for cache-aware routing, vLLM as the engine.
- [Serving ML Models in Production: Common Patterns](https://www.anyscale.com/blog/serving-ml-models-in-production-common-patterns) — **Anyscale** — the serving-architecture pattern catalog.
- [Static vs Dynamic Inference](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-inference) — **Google** — the foundational batch-versus-online trade-off.
- [vLLM V1: a major upgrade to vLLM's core architecture](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html) — **vLLM maintainers** — the scheduler and KV-cache manager rewrite behind current defaults.

**Papers**:
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — real serving, latency and scaling failures from industry.
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)** — the vLLM paper: block tables and near-zero KV waste.
- [S-LoRA: Serving Thousands of Concurrent LoRA Adapters](https://arxiv.org/abs/2311.03285) — **Sheng et al. (2023)** — unified paging of adapters and KV cache for multi-tenant serving.
- [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104) — **Zheng et al. (2023)** — RadixAttention and fast constrained decoding.

**Documentation**:
- [BentoML — Documentation](https://docs.bentoml.com/en/latest/) — **BentoML** — turn any model into a REST or gRPC service with batching and packaging.
- [KServe — System Architecture Overview](https://kserve.github.io/website/docs/concepts/architecture) — **KServe (CNCF)** — control plane vs data plane, InferenceService and scale-to-zero.
- [SGLang documentation](https://docs.sglang.ai/) — **SGLang team** — launching and tuning the RadixAttention engine.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — **NVIDIA** — building compiled engines and in-flight batching.
- [Text Generation Inference — LoRA](https://huggingface.co/docs/text-generation-inference/conceptual/lora) — **Hugging Face** — `LORA_ADAPTERS` and per-request `adapter_id` for existing TGI deployments.
- [Text Generation Inference repository](https://github.com/huggingface/text-generation-inference) — **Hugging Face** — the maintenance-mode notice and the recommended successors.
- [Triton Inference Server — User Guide](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html) — **NVIDIA** — dynamic batching and multi-framework model serving on GPUs.
- [vLLM — LoRA Adapters](https://docs.vllm.ai/en/latest/features/lora.html) — **vLLM maintainers** — `--enable-lora`, `--lora-modules`, `--max-loras` and `--max-lora-rank`.
- [vLLM — Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/) — **vLLM maintainers** — `vllm serve` and the OpenAI-compatible endpoints.
- [vLLM — Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics.html) — **vLLM maintainers** — the queue, KV-usage and latency metrics named in the pitfalls.
- [vLLM Documentation](https://docs.vllm.ai/en/latest/) — **vLLM maintainers** — the reference engine: paged attention, continuous batching, OpenAI-compatible server.

**Books**:
- [AI Engineering — Ch. 9 "Inference Optimization"](https://huyenchip.com/books/) — **Chip Huyen (2025)** — serving end to end, from engine choice to cost.
- [Designing Machine Learning Systems — Ch. 7 "Model Deployment and Prediction Service"](https://huyenchip.com/mlops/) — **Chip Huyen** — batch vs online and REST vs gRPC prediction services.
- [Machine Learning Engineering — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — serving patterns in practice.
