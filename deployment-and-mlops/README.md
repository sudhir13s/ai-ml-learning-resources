---
id: "18-mlops-and-deployment"
topic: "MLOps & Deployment"
level: advanced
built_from: ["tools-and-frameworks", "software-engineering"]
updated: 2026-09-07
---

# MLOps & Deployment
> Getting models into production and keeping them healthy — serving, pipelines, CI/CD,
> monitoring, and the systems discipline around ML.

**⭐ Start here:** [Made With ML](https://madewithml.com/) — **Goku Mohandas** — the best free, end-to-end MLOps course (design → develop → deploy → iterate).

## Concept Index
Every chapter is a self-contained folder (`<topic>/<topic>.md`) — a short guided learning
path plus the best **free, open** courses, videos, papers, articles, and books for that topic.
> Every chapter below is written and ready. New here? Start with the field overview above, then work top to bottom.

### Foundations & lifecycle
1. ✅ [ML Lifecycle & MLOps Maturity](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity)
2. ✅ [Reproducibility (seeds, environments, lineage)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/reproducibility/reproducibility)
3. ✅ [Experiment Tracking (MLflow · Weights & Biases)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking)
4. ✅ [Data & Model Versioning (DVC · lakeFS)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning)

### Pipelines & automation
5. ✅ [Feature Stores (Feast)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/feature-stores/feature-stores)
6. ✅ [ML Pipelines & Orchestration (Airflow · Kubeflow)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration)
7. ✅ [CI/CD for ML & Continuous Training (CT)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training)

### Training infrastructure (the compute plane)
8. ✅ [GPUs & Accelerators for Deep Learning (roofline · kernels · mixed precision)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning)
9. ✅ [Mixed Precision & Memory-Efficient Training](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/mixed-precision-and-memory-efficient-training/mixed-precision-and-memory-efficient-training)
10. ✅ [Distributed Training — Parallelism, FSDP & ZeRO](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero)
11. ✅ [Checkpointing & Fault-Tolerant Training](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/checkpointing-and-fault-tolerant-training/checkpointing-and-fault-tolerant-training)
12. ✅ [Cluster Scheduling & Training Orchestration](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/cluster-scheduling-and-training-orchestration/cluster-scheduling-and-training-orchestration)
13. ✅ [Training Cost & Capacity Planning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/training-cost-and-capacity-planning/training-cost-and-capacity-planning)

### Packaging & serving
14. ✅ [Model Packaging & Containerization (Docker)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization)
15. ✅ [Model Serving (REST/gRPC · batch vs online · BentoML/Triton/TF-Serving)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/model-serving/model-serving)
16. ✅ [Scaling Inference (autoscaling · GPU · Ray Serve)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/scaling-inference/scaling-inference)

### Release, rollback & recovery
17. ✅ [A/B Testing · Shadow & Canary Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment)
18. ✅ [Rollback & Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems)

### Operations, monitoring & governance
19. ✅ [Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
20. ✅ [Data & Concept Drift Detection](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection)
21. ✅ [AI Incident Response & Postmortems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems)
22. ✅ [Model Registry & Governance](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/model-registry-and-governance/model-registry-and-governance)

### LLMs & cost
23. ✅ [LLMOps (eval · guardrails · prompt versioning · cost/latency)](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/llmops/llmops)
24. ✅ [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/cost-optimization/cost-optimization)

### Related concepts (canonical home is another section)
> These topics have a canonical home elsewhere in the platform — linked here, not duplicated.
- **Online experimentation & A/B statistics theory** (hypothesis tests, power, CUPED) → [01. Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)
- **LLM inference internals** (KV-cache, quantization, paged attention, serving stacks) → [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- **Data preprocessing & feature engineering** (cleaning, encoding, scaling, splits) → [02. Data_Preprocessing](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/readme)

## Courses (free)
- [Made With ML](https://madewithml.com/) — **Goku Mohandas** — production ML + MLOps, code and reasoning.
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/) — **FSDL (Charles Frye, Sergey Karayev, Josh Tobin)** — free lectures on shipping ML products.
- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang & Tatsunori Hashimoto (Stanford)** — the training-platform half of MLOps: kernels, GPUs, parallelism, built by hand.
- [Deep Learning Systems (CMU 10-414/714)](https://dlsyscourse.org/lectures/) — **Tianqi Chen & Zico Kolter (Carnegie Mellon)** — what sits under the framework: autodiff, operators, GPU backends.

## Videos
- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — **DataTalks.Club** — free, hands-on, project-based (experiment tracking → orchestration → monitoring → deployment).
- [Full Stack Deep Learning 2022 lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) — **The Full Stack** — deployment, monitoring, troubleshooting and testing, on video.

## Articles / Reference
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Martin Zinkevich (Google)** — 43 hard-won best practices for production ML.
- [Designing ML Systems — notes & talks](https://huyenchip.com/mlops/) — **Chip Huyen** — the practitioner's map of the MLOps landscape.
- [Continuous Delivery for Machine Learning](https://martinfowler.com/articles/cd4ml.html) — **Sato, Wider & Windheuser (martinfowler.com)** — versioning code, model and data as one reversible release.
- [The Ultra-Scale Playbook: Training LLMs on GPU Clusters](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Hugging Face nanotron team** — the current canonical text on large-scale distributed training.

## Books
- [*Site Reliability Engineering* and *The SRE Workbook*](https://sre.google/books/) — **Google** — free online; incident management, release engineering and postmortem culture.
- [*Designing Machine Learning Systems* — notes and companion repository](https://github.com/chiphuyen/dmls-book) — **Chip Huyen** — the definitive modern text; the book is paid, the author's notes and code are free.

## In this platform
- Inference economics: [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/cost-optimization/cost-optimization) · [Scaling Inference](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/scaling-inference/scaling-inference) · [LLM Systems curriculum](/ai-ml/ai-ml-learning-resources/meta/llm-systems-curriculum)
- Offline evaluation feeds everything here: [Error Analysis & Model Debugging](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging) · [Calibration & Reliability Diagrams](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams)
