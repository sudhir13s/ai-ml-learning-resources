---
id: "operations-and-lifecycle/training-infrastructure/mixed-precision-and-memory-efficient-training"
topic: "Mixed Precision & Memory-Efficient Training"
level: advanced
built_from: ["gpus-and-accelerators-for-deep-learning", "distributed-training-parallelism-fsdp-zero"]
leads_to: ["operations-and-lifecycle/training-infrastructure/checkpointing-and-fault-tolerant-training", "18-mlops/cost-optimization"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Mixed Precision & Memory-Efficient Training"
minutes: 18
category: training-infrastructure
---

# Mixed Precision & Memory-Efficient Training
> Accelerator memory, not accelerator arithmetic, is what stops most training runs. A step holds
> four things: **parameters, gradients, optimizer state and activations** — and only the last of
> those scales with batch size and sequence length. Mixed precision shrinks the first three by
> storing them in fewer bits while keeping a high-precision copy where the mathematics needs one;
> recomputation trades arithmetic for activation memory. In one sentence: **decide, per tensor,
> the fewest bits that preserve the update — then recompute whatever you refuse to store.**

**Why it matters:** the difference between a model that fits and one that does not, and the single
biggest throughput lever after parallelism. Interviewers walk a fixed ladder — *where does the
memory go in bytes*, *why does fp16 need loss scaling while bf16 does not*, *what a master weight
copy is for*, *what activation checkpointing costs in floating-point operations (FLOPs)*, and
*why gradient accumulation is not free*. The 2025–26 additions are **fp8 on Hopper and Blackwell**
and the **microscaling (MX) formats** — fp8 and fp4 blocks with a shared exponent — where the
question moves from "does it fit" to "does it still converge". The underrated failure mode:
a run that trains fine for 100 billion tokens, then diverges when a rare activation outlier
overflows a per-tensor scale that was calibrated far too early.

**Start here — suggested path:**

1. **Count the bytes before anything else** — read [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **Quentin Anthony, Stella Biderman & Hailey Schoelkopf (EleutherAI)**. *Parameters, gradients, optimizer state and activations as explicit formulas; every later decision is arithmetic on these.*
2. **Learn the original recipe** — read [Mixed Precision Training](https://arxiv.org/abs/1710.03740) — **Micikevicius et al. (NVIDIA & Baidu)**. *Master weights in fp32, arithmetic in fp16, loss scaling to keep small gradients out of the subnormal range — still the mental model for every later format.*
3. **Turn it on and measure** — do the [Automatic Mixed Precision recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html) — **PyTorch maintainers**. *`autocast` plus `GradScaler` in twenty lines, with the timing comparison that shows where the win actually comes from.*
4. **Trade compute for memory deliberately** — read [Current and New Activation Checkpointing Techniques in PyTorch](https://pytorch.org/blog/activation-checkpointing-techniques/) — **PyTorch team**. *Full versus selective recomputation, and how `torch.compile` chooses what to save rather than recompute.*
5. **See the frontier recipe** — read the [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — **DeepSeek-AI**. *The fp8 training section is the first published, industrial-scale account: fine-grained tile and block scaling, and which accumulations stayed in higher precision.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang & Tatsunori Hashimoto (Stanford)** — the assignments make you implement a training loop and account for its memory; lecture materials and code are fully public.
- [How to Scale Your Model — the "Training" chapter](https://jax-ml.github.io/scaling-book/training/) — **Google DeepMind JAX team** — derives the memory and communication cost of a training step from first principles, so precision choices become arithmetic rather than folklore.
- [GPU MODE lectures](https://github.com/gpu-mode/lectures) — **Mark Saroufim, Andreas Köpf and the GPU MODE community** — an ongoing open lecture series with several sessions on low-precision numerics, quantized optimizers and profiling, all notebooks included.

## Videos

- [FP8 Training From Hopper To Blackwell](https://www.youtube.com/watch?v=SBO2PmUKfUA) — **Luca Wehrstedt (Meta), on the PyTorch channel** — what actually changed between the two hardware generations, and which parts of the step can and cannot move to eight bits.
- [Training LLMs at Scale — Stanford MLSys #83](https://www.youtube.com/watch?v=JA1l96tjrs4) — **Deepak Narayanan (NVIDIA), Stanford MLSys Seminars** — places precision alongside parallelism and recomputation in one throughput budget instead of treating it as a separate trick.
- [Stanford CS336 — Language Modeling from Scratch, 2025 lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the kernels and training lectures profile a real step and show precision changing the bandwidth bill, not the FLOP count.

## Key Papers

- [Mixed Precision Training](https://arxiv.org/abs/1710.03740) — **Micikevicius et al. (2018, NVIDIA & Baidu)** — master weights, loss scaling and fp32 accumulation; the paper that made tensor cores usable for training.
- [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433) — **Micikevicius et al. (2022, NVIDIA, Arm & Intel)** — E4M3 and E5M2 defined, with the argument for which one belongs on the forward and which on the backward pass.
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — **DeepSeek-AI (2024)** — an fp8 pre-training run at frontier scale: per-tile activation scaling, per-block weight scaling, and the accumulations deliberately kept wider.
- [Recipes for Pre-training LLMs with MXFP8](https://arxiv.org/abs/2506.08027) — **Mishra, Stosic, Layton et al. (2025, NVIDIA)** — the microscaling format on Blackwell, with the rounding and scaling choices that decide whether the loss curve matches bf16.
- [Microscaling Data Formats for Deep Learning](https://arxiv.org/abs/2310.10537) — **Rouhani et al. (2023, Microsoft and the OCP MX group)** — the block-with-shared-exponent idea behind MXFP8 and MXFP4; read it before any fp4 claim.
- [Training Deep Nets with Sublinear Memory Cost](https://arxiv.org/abs/1604.06174) — **Chen, Xu, Zhang & Guestrin (2016)** — gradient checkpointing: store $O(\sqrt{n})$ activations, recompute the rest, for roughly one extra forward pass.
- [8-bit Optimizers via Block-wise Quantization](https://arxiv.org/abs/2110.02861) — **Dettmers, Lewis, Shleifer & Zettlemoyer (2022)** — the Adam moment estimates in eight bits with block-wise dynamic scaling; the basis of the bitsandbytes 8-bit and paged optimizers.

## Articles / Blogs (free, no paywall)

- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI** — the byte-level memory model, including why Adam costs roughly twelve bytes per parameter before anything else is counted.
- [Automatic Mixed Precision recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html) — **PyTorch maintainers** — the reference implementation of `autocast` and gradient scaling, with the operation allowlist that explains why some layers stay in fp32.
- [Current and New Activation Checkpointing Techniques in PyTorch](https://pytorch.org/blog/activation-checkpointing-techniques/) — **PyTorch team** — full, selective and compile-driven recomputation compared on the same model, with the memory and time deltas.
- [Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) — **PyTorch maintainers** — kernel fusion is a memory-bandwidth lever, not just a speed one; fewer round trips to high-bandwidth memory means fewer bytes and fewer intermediates.
- [Supercharging training using float8 and FSDP2](https://pytorch.org/blog/training-using-float8-fsdp2/) — **PyTorch and IBM teams** — a measured end-to-end fp8 result with the numerics caveats stated rather than buried.
- [Transformer Engine user guide](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/index.html) — **NVIDIA** — the delayed-scaling machinery behind production fp8: amax history, scale updates, and which modules are safe to convert.

## Books (free, with chapters)

- [*The Ultra-Scale Playbook: Training LLMs on GPU Clusters*](https://huggingface.co/spaces/nanotron/ultrascale-playbook) — **Nouamane Tazi, Ferdinand Mom and the Hugging Face nanotron team** — free and interactive; the memory chapters sweep activation recomputation, gradient accumulation and precision against real measurements on up to 512 accelerators.

## In this platform

- Prerequisites: [GPUs & Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning) — the bandwidth numbers precision is spent on · [Distributed Training — Parallelism, FSDP & ZeRO](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) — the other half of the memory bill
- Next in this sub-area: [Checkpointing & Fault-Tolerant Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/checkpointing-and-fault-tolerant-training/checkpointing-and-fault-tolerant-training) — what you write to disk once the step fits
- The inference mirror image: [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) · [Inference Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)
- Where these budgets get spent: [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) · [LoRA & Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — where paged and quantized optimizers show up in practice
- The platform underneath: [Data & Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme) · [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization)
- Practitioner workflow: [Model Training](/ai-ml/practitioner-workflows/training-and-adaptation/model-training) — the same decisions inside a build-it-yourself chapter
