---
id: "operations-and-lifecycle/training-infrastructure/distributed-training-parallelism-fsdp-zero"
topic: "Distributed Training — Parallelism, FSDP & ZeRO"
level: advanced
built_from: ["gpus-and-accelerators-for-deep-learning", "ml-pipelines-and-orchestration"]
leads_to: ["18-mlops/cicd-for-ml-and-continuous-training", "18-mlops/cost-optimization"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 20
title: "Distributed Training — Parallelism, FSDP & ZeRO"
minutes: 20
category: training-infrastructure
---

# Distributed Training — Parallelism, FSDP & ZeRO
> One accelerator cannot hold a modern model. Training at scale is therefore a **sharding
> problem**: split the *batch* (data parallelism), the *tensors inside a layer* (tensor
> parallelism), the *layers* (pipeline parallelism), the *sequence* (sequence/context
> parallelism), or the *experts* (expert parallelism) — and pay for each split in **communication**.
> **ZeRO** and **fully sharded data parallel (FSDP)** are the two names for the same core trick:
> shard optimizer state, gradients and parameters across ranks and gather them just in time.

**Why it matters:** the defining systems question of large-model work, and the one that decides
whether a training run costs one week or five. Every serious 2026 interview walks the same ladder —
*where does the memory go* (parameters, gradients, optimizer state, activations), *what does each
parallelism axis cost in bandwidth*, *why ZeRO stage 3 and FSDP shard parameters but must all-gather
them per layer*, and *why pipeline parallelism creates a bubble that micro-batching and
zero-bubble schedules try to fill*. The trap: reaching for tensor parallelism across nodes. Tensor
parallelism is bandwidth-hungry and belongs **inside** a high-bandwidth island (NVLink domain);
pipeline and data parallelism are what you stretch across the slower inter-node fabric.

**Start here — suggested path:**

1. **Get the memory arithmetic first** — read [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **Quentin Anthony, Stella Biderman & Hailey Schoelkopf (EleutherAI)**. *Parameters, gradients, optimizer state and activations in bytes; without this the rest is hand-waving.*
2. **Read the playbook end to end** — read [The Ultra-Scale Playbook: Training LLMs on GPU Clusters](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Nouamane Tazi, Ferdinand Mom and the Hugging Face nanotron team**. *~30,000 words distilled from 4,000+ scaling experiments on up to 512 GPUs; the current canonical text on 5D parallelism.*
3. **Take the systems view** — read [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) — **Jacob Austin, Sholto Douglas and the Google DeepMind JAX team**. *Derives the roofline for each sharding strategy so you can predict, not measure, which one wins.*
4. **Watch it taught** — watch [Stanford CS336: Language Modeling from Scratch, 2025](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online (Percy Liang & Tatsunori Hashimoto)**. *The Parallelism lectures build collectives, then data/tensor/pipeline parallelism, then ZeRO and FSDP, in order.*
5. **Run it** — follow [Getting Started with Fully Sharded Data Parallel (FSDP2)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) — **PyTorch maintainers**, then read [picotron](https://github.com/huggingface/picotron). *One is the production application programming interface (API); the other is a minimal, readable implementation of all four axes.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang & Tatsunori Hashimoto (Stanford)** — assignments make you implement distributed training yourself; [all lecture materials are public](https://github.com/stanford-cs336/spring2025-lectures).
- [How to Scale Your Model — a systems view of LLMs on TPUs and GPUs](https://jax-ml.github.io/scaling-book/) — **Google DeepMind JAX team** — a free online book with exercises; the [training chapter](https://jax-ml.github.io/scaling-book/training/) derives when each parallelism axis pays for itself.
- [The Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Hugging Face nanotron team** — book-length, interactive, with memory and throughput plots you can sweep; the practical companion to the papers below.

## Videos

- [Stanford CS336 — Language Modeling from Scratch, 2025 lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the Parallelism 1 and 2 lectures are the clearest recorded derivation of collectives, ZeRO stages and FSDP.
- [Hardware-aware Algorithms for Sequence Modeling — Stanford MLSys #87](https://www.youtube.com/watch?v=foG0ebzuw34) — **Tri Dao (Stanford MLSys Seminars)** — why the memory hierarchy, not the FLOP count, sets the ceiling on a training step.

## Key Papers

- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) — **Rajbhandari, Rasley, Ruwase & He (2020, Microsoft)** — the three stages: shard optimizer state, then gradients, then parameters; the origin of FSDP.
- [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](https://arxiv.org/abs/2304.11277) — **Zhao et al. (2023, Meta)** — the production design: flat parameters, communication/computation overlap, and the rate-limiter that keeps memory bounded.
- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) — **Shoeybi et al. (2019, NVIDIA)** — intra-layer tensor parallelism with two all-reduces per transformer block.
- [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473) — **Narayanan et al. (2021)** — the 3D-parallelism composition (tensor × pipeline × data) and how to place each axis on the network topology.
- [GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism](https://arxiv.org/abs/1811.06965) — **Huang et al. (2019, Google)** — micro-batching and re-materialization; where the pipeline bubble comes from.
- [PipeDream: Generalized Pipeline Parallelism for DNN Training](https://arxiv.org/abs/1806.03377) — **Narayanan et al. (2019)** — 1F1B scheduling and weight stashing, the basis of every modern pipeline schedule.
- [Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198) — **Korthikanti et al. (2022, NVIDIA)** — sequence parallelism and selective recomputation; the activation-memory half of the story.
- [Ring Attention with Blockwise Transformers for Near-Infinite Context](https://arxiv.org/abs/2310.01889) — **Liu, Zaharia & Abbeel (2023)** — context parallelism: shard the sequence and overlap the key/value exchange with compute.
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) — **Fedus, Zoph & Shazeer (2021, Google)** — expert parallelism and the all-to-all that pays for it; see also [GShard](https://arxiv.org/abs/2006.16668).
- [TorchTitan: One-stop PyTorch Native Solution for Production Ready LLM Pretraining](https://arxiv.org/abs/2410.06511) — **Liang et al. (2024, Meta, ICLR 2025)** — how the axes compose today in a maintained open codebase.

## Articles / Blogs (free, no paywall)

- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI** — the memory and FLOP formulas every capacity estimate starts from.
- [How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/) — **Lilian Weng** — the compact survey of every parallelism axis plus mixed precision, offloading and recomputation.
- [Introducing PyTorch Fully Sharded Data Parallel (FSDP) API](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/) — **PyTorch team (Meta)** — the maintainers' own explanation of sharding, all-gather and reduce-scatter placement.
- [ZeRO tutorial](https://www.deepspeed.ai/tutorials/zero/) — **DeepSpeed team (Microsoft)** — configuring stages 1–3 and offload, with the memory table for each.
- [Efficient training on multiple GPUs](https://huggingface.co/docs/transformers/perf_train_gpu_many) — **Hugging Face** — the decision table: which parallelism to reach for at which model and cluster size.
- [Collective operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) — **NVIDIA NCCL documentation** — all-reduce, all-gather, reduce-scatter and all-to-all defined precisely; the primitives every strategy is built from.

## Books (free, with chapters)

- [*How to Scale Your Model* — Part 3 "Training" and Part 5 "Parallelism"](https://jax-ml.github.io/scaling-book/training/) — **Google DeepMind** — free online book; derives the arithmetic-intensity crossover for each sharding scheme.
- [*The Ultra-Scale Playbook* — memory, data/tensor/pipeline/context/expert parallelism](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Hugging Face** — free; the closest thing to a textbook on 5D parallelism, with [picotron](https://github.com/huggingface/picotron) (minimal) and [torchtitan](https://github.com/pytorch/torchtitan) (production) to read alongside.

## In this platform

- Prerequisite: [GPUs & Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning) — the memory hierarchy and bandwidth numbers this page spends
- Runs on top of: [ML Pipelines & Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) · [Feature Stores](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/feature-stores/feature-stores)
- The inference mirror image: [Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference) · [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) · [Inference Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)
- What a run costs, and how to shrink it: [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization)
- Attention-level efficiency has its own owner: [Efficient Attention](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention)
