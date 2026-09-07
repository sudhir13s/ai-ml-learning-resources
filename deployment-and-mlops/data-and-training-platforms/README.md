---
id: "deployment-and-mlops/data-and-training-platforms"
topic: "Data and Training Platforms"
level: advanced
built_from: ["lifecycle-and-reproducibility", "data-preparation"]
updated: 2026-09-07
---

# Data and Training Platforms

> The substrate models are trained on: the system that guarantees a feature means the same thing
> offline and online, the orchestrator that turns a notebook into a retryable directed acyclic
> graph (DAG), the accelerator whose compute-to-bandwidth ratio decides what is fast, and the
> sharding strategies that let a model too large for one device train anyway.

**Start here:** [GPUs and Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning) if your work is deep learning, [Feature Stores](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/feature-stores/feature-stores) if it is tabular — the two halves of this sub-area serve different stacks.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### The data platform

1. [Feature Stores](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/feature-stores/feature-stores) — one feature definition serving both point-in-time-correct training data and low-latency online lookups; the cure for train/serve skew.
2. [ML Pipelines and Orchestration](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) — ingest → validate → transform → train → evaluate → deploy as a scheduled, retried, monitored DAG in Airflow or Kubeflow.

### The training platform

3. [GPUs and Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning) — arithmetic intensity, the roofline, memory hierarchy, kernels and mixed precision; why most deep-learning code is memory bound.
4. [Distributed Training — Parallelism, FSDP and ZeRO](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) — data, tensor, pipeline, sequence and expert parallelism, and what each split costs in communication.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang and Tatsunori Hashimoto (Stanford)** — the assignments make you implement distributed training and profile it yourself.
- [Deep Learning Systems (CMU 10-414/714)](https://dlsyscourse.org/lectures/) — **Tianqi Chen and Zico Kolter (Carnegie Mellon)** — the definitive open course on what sits under PyTorch: autodiff, operators, GPU backends.
- [GPU MODE lectures](https://github.com/gpu-mode/lectures) — **Mark Saroufim, Andreas Köpf and the GPU MODE community** — a free ongoing series on CUDA, Triton and kernel performance, with the code.
- [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) — **OpenAI Triton maintainers** — vector add → fused softmax → matmul → fused attention; the shortest path to writing a real kernel.
- [Made With ML — Feature Store](https://madewithml.com/courses/mlops/feature-store/) — **Goku Mohandas** — feature stores inside a complete production workflow rather than in isolation.

## Videos

- [Stanford CS336 — 2025 lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the Parallelism 1 and 2 lectures are the clearest recorded derivation of collectives, sharding and their costs.
- [Hardware-aware Algorithms for Sequence Modeling — Stanford MLSys #87](https://www.youtube.com/watch?v=foG0ebzuw34) — **Tri Dao (Stanford MLSys Seminars)** — why the memory hierarchy, not the FLOP count, sets the ceiling.
- [FlashAttention — Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Tri Dao (Stanford MLSys Seminars)** — tiling into on-chip memory instead of materializing the score matrix; the canonical worked example of the roofline idea.
- [Intro to Kubeflow Pipelines](https://www.youtube.com/watch?v=_AY8mmbR1o4) — **Google Cloud Tech** — ML-native pipelines, reusable components and metadata tracking.

## Key Papers

- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) — **Rajbhandari, Rasley, Ruwase and He (Microsoft, 2020)** — the three sharding stages: optimizer state, then gradients, then parameters.
- [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](https://arxiv.org/abs/2304.11277) — **Zhao et al. (Meta, 2023)** — the production design: flat parameters, communication/computation overlap, and the sharp edges.
- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) — **Shoeybi et al. (NVIDIA, 2019)** — intra-layer tensor parallelism with two all-reduces per transformer block.
- [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473) — **Narayanan et al. (2021)** — how tensor, pipeline and data parallelism compose, and where to place each axis.
- [Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures](https://digitalassets.lib.berkeley.edu/techreports/ucb/text/EECS-2008-134.pdf) — **Williams, Waterman and Patterson (UC Berkeley, 2008)** — the compute-versus-bandwidth model behind every "this is memory bound" claim.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — the pipeline-jungle and data-dependency debt that feature stores and orchestrators exist to cut.

## Articles / Blogs (free, no paywall)

- [How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/) — **Lilian Weng** — every parallelism axis plus mixed precision, offloading and recomputation, in one compact survey.
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI** — the memory and FLOP formulas every capacity estimate starts from.
- [Introducing PyTorch Fully Sharded Data Parallel (FSDP) API](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/) — **PyTorch team (Meta)** — the maintainers' own explanation of where all-gather and reduce-scatter sit.
- [Feature Stores — A Hierarchy of Needs](https://eugeneyan.com/writing/feature-stores/) — **Eugene Yan** — the clearest free explainer of what problem a feature store solves before which one to buy.
- [Collective operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) — **NVIDIA NCCL documentation** — all-reduce, all-gather, reduce-scatter and all-to-all defined precisely; the vocabulary every parallelism paper assumes.

## Books (free, with chapters)

- [*The Ultra-Scale Playbook: Training LLMs on GPU Clusters*](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Hugging Face nanotron team** — free and interactive; the current canonical text on five-dimensional parallelism, with sweepable plots.
- [*How to Scale Your Model* — "Training" and "Parallelism"](https://jax-ml.github.io/scaling-book/training/) — **Google DeepMind (Austin et al.)** — free online; derives the arithmetic-intensity crossover for each sharding scheme.
- [*How to Scale Your Model* — "All About Roofline"](https://jax-ml.github.io/scaling-book/roofline/) — **Google DeepMind** — free online; the best modern restatement of the roofline model, applied to real accelerators.
- [*Designing Machine Learning Systems* — Ch. 5 "Feature Engineering"](https://huyenchip.com/mlops/) — **Chip Huyen** — feature engineering, train/serve skew and stores; author notes free.

## In this platform

- Section index: [MLOps and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
- Sibling sub-areas: [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/readme) · [Packaging and Serving](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/readme) · [Release and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/readme) · [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/readme) · [Governance and Economics](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/readme)
- What this platform is built to train: [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/pretraining/pretraining) · [Mixture-of-Experts](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/mixture-of-experts/mixture-of-experts)
- The same hardware argument, at inference time: [KV Cache — FlashAttention and FlashDecoding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache-flashattention-and-flashdecoding) · [Inference Optimization and Serving](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization)
- Upstream of the features: [Data Preparation](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/readme)
- Doing it rather than reading it: [Model Training workflow](/ai-ml/practitioner-workflows/workflow-library/training-and-adaptation/model-training) · [Data Preparation workflow](/ai-ml/practitioner-workflows/workflow-library/data-and-inputs/data-preparation)
