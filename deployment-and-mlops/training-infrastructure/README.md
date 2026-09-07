---
id: "deployment-and-mlops/training-infrastructure"
topic: "Training Infrastructure"
level: advanced
built_from: ["data-and-training-platforms", "optimization-and-training"]
updated: 2026-09-07
---

# Training Infrastructure

> The compute plane a model is trained on: the accelerator whose compute-to-bandwidth ratio
> decides what is fast, the number formats and memory tricks that fit a run onto it, the sharding
> that lets a model too large for one device train anyway, the checkpoints that survive the
> failures a thousand-GPU job will have, the scheduler that places the job, and the arithmetic
> that says what the run costs before it starts.

**Start here:** [GPUs and Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning) — every other page in this sub-area is a consequence of the roofline argument made there.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### One device

1. [GPUs and Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning) — arithmetic intensity, the roofline, memory hierarchy, kernels; why most deep-learning code is memory bound.
2. [Mixed Precision and Memory-Efficient Training](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/mixed-precision-and-memory-efficient-training/mixed-precision-and-memory-efficient-training) — BF16, FP8 and lower, loss scaling, activation recomputation, 8-bit optimizers; the memory formulas a run is budgeted from.

### Many devices

3. [Distributed Training — Parallelism, FSDP and ZeRO](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) — data, tensor, pipeline, sequence and expert parallelism, and what each split costs in communication.
4. [Checkpointing and Fault-Tolerant Training](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/checkpointing-and-fault-tolerant-training/checkpointing-and-fault-tolerant-training) — sharded and asynchronous checkpoints, elastic restarts, stragglers and silent data corruption; the failure statistics of real frontier runs.

### The cluster and the bill

5. [Cluster Scheduling and Training Orchestration](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/cluster-scheduling-and-training-orchestration/cluster-scheduling-and-training-orchestration) — Slurm, Kubernetes operators, Ray and SkyPilot; gang scheduling, topology-aware placement, preemption and GPU sharing.
6. [Training Cost and Capacity Planning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/training-infrastructure/training-cost-and-capacity-planning/training-cost-and-capacity-planning) — the six-N-D rule, model FLOPs utilization, compute-optimal sizing, cloud versus reserved versus on-prem, energy and carbon.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang and Tatsunori Hashimoto (Stanford)** — the assignments make you implement distributed training and profile it yourself.
- [Deep Learning Systems (CMU 10-414/714)](https://dlsyscourse.org/lectures/) — **Tianqi Chen and Zico Kolter (Carnegie Mellon)** — the definitive open course on what sits under PyTorch: autodiff, operators, GPU backends.
- [GPU MODE lectures](https://github.com/gpu-mode/lectures) — **Mark Saroufim, Andreas Köpf and the GPU MODE community** — a free ongoing series on CUDA, Triton and kernel performance, with the code.
- [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) — **OpenAI Triton maintainers** — vector add → fused softmax → matmul → fused attention; the shortest path to writing a real kernel.

## Videos

- [Stanford CS336 — 2025 lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the Parallelism 1 and 2 lectures are the clearest recorded derivation of collectives, sharding and their costs.
- [Hardware-aware Algorithms for Sequence Modeling — Stanford MLSys #87](https://www.youtube.com/watch?v=foG0ebzuw34) — **Tri Dao (Stanford MLSys Seminars)** — why the memory hierarchy, not the FLOP count, sets the ceiling.
- [FlashAttention — Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Tri Dao (Stanford MLSys Seminars)** — tiling into on-chip memory instead of materializing the score matrix; the canonical worked example of the roofline idea.

## Key Papers

- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) — **Rajbhandari, Rasley, Ruwase and He (Microsoft, 2020)** — the three sharding stages: optimizer state, then gradients, then parameters.
- [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](https://arxiv.org/abs/2304.11277) — **Zhao et al. (Meta, 2023)** — the production design: flat parameters, communication/computation overlap, and the sharp edges.
- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) — **Shoeybi et al. (NVIDIA, 2019)** — intra-layer tensor parallelism with two all-reduces per transformer block.
- [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473) — **Narayanan et al. (2021)** — how tensor, pipeline and data parallelism compose, and where to place each axis.
- [Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures](https://digitalassets.lib.berkeley.edu/techreports/ucb/text/EECS-2008-134.pdf) — **Williams, Waterman and Patterson (UC Berkeley, 2008)** — the compute-versus-bandwidth model behind every "this is memory bound" claim.
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — **Llama Team, Meta (2024)** — the infrastructure sections report a real 16,000-GPU run: interruptions, causes, checkpoint strategy and utilization.

## Articles / Blogs (free, no paywall)

- [How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/) — **Lilian Weng** — every parallelism axis plus mixed precision, offloading and recomputation, in one compact survey.
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI** — the memory and FLOP formulas every capacity estimate starts from.
- [Introducing PyTorch Fully Sharded Data Parallel (FSDP) API](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/) — **PyTorch team (Meta)** — the maintainers' own explanation of where all-gather and reduce-scatter sit.
- [Collective operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) — **NVIDIA NCCL documentation** — all-reduce, all-gather, reduce-scatter and all-to-all defined precisely; the vocabulary every parallelism paper assumes.

## Books (free, with chapters)

- [*The Ultra-Scale Playbook: Training LLMs on GPU Clusters*](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Hugging Face nanotron team** — free and interactive; the current canonical text on five-dimensional parallelism, with sweepable plots.
- [*How to Scale Your Model* — "Training" and "Parallelism"](https://jax-ml.github.io/scaling-book/training/) — **Google DeepMind (Austin et al.)** — free online; derives the arithmetic-intensity crossover for each sharding scheme.
- [*How to Scale Your Model* — "All About Roofline"](https://jax-ml.github.io/scaling-book/roofline/) — **Google DeepMind** — free online; the best modern restatement of the roofline model, applied to real accelerators.

## In this platform

- Section index: [MLOps and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
- The data plane this compute plane feeds on: [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/readme)
- Sibling sub-areas: [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/readme) · [Packaging and Serving](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/readme) · [Governance and Economics](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/readme)
- What this infrastructure is built to train: [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/pretraining/pretraining) · [Mixture-of-Experts](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/mixture-of-experts/mixture-of-experts)
- The same hardware argument, at inference time: [KV Cache — FlashAttention and FlashDecoding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache-flashattention-and-flashdecoding) · [Inference Optimization and Serving](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization) · [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/cost-optimization/cost-optimization)
- Doing it rather than reading it: [Model Training workflow](/ai-ml/practitioner-workflows/workflow-library/training-and-adaptation/model-training)
