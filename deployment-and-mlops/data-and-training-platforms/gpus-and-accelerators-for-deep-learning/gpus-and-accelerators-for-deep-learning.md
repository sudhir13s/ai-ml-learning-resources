---
id: "deployment-and-mlops/data-and-training-platforms/gpus-and-accelerators-for-deep-learning"
topic: "GPUs & Accelerators for Deep Learning"
level: advanced
built_from: ["ml-pipelines-and-orchestration"]
leads_to: ["distributed-training-parallelism-fsdp-zero", "scaling-inference"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 18
title: "GPUs & Accelerators for Deep Learning"
minutes: 18
category: data-and-training-platforms
---

# GPUs & Accelerators for Deep Learning
> A graphics processing unit (GPU) is not a fast central processing unit (CPU) — it is a machine
> with enormous arithmetic throughput sitting behind a comparatively narrow memory pipe. Almost
> every deep-learning performance question reduces to one number: **arithmetic intensity**, the
> floating-point operations you do per byte you move. Below the hardware's compute-to-bandwidth
> ratio you are **memory-bound**; above it you are **compute-bound**. The **roofline** is the
> picture of that threshold, and kernel fusion, mixed precision and tiling are all ways to climb it.

**Why it matters:** the reason an "optimized" model can run at 5% of a device's peak, and the
reason FlashAttention was a breakthrough without changing any mathematics. Interviewers probe the
memory hierarchy (registers → shared memory / static random-access memory (SRAM) → high-bandwidth
memory (HBM) → host), what a **tensor core** actually multiplies, why **bf16** replaced fp16 for
training (same exponent range as fp32, so no loss scaling), what **fp8** buys and costs on Hopper
and Blackwell, and why the three costs of a step are **compute, memory bandwidth and overhead** —
in that order of frequency, but rarely in that order of importance. The trap: optimizing FLOPs on
a workload that is bandwidth-bound, or profiling with the CUDA context initialization included.

**Start here — suggested path:**

1. **Get the mental model** — read [Making Deep Learning Go Brrrr From First Principles](https://horace.io/brrr_intro.html) — **Horace He (PyTorch)**. *Compute, memory bandwidth and overhead: the three-bucket framework the rest of the page hangs on.*
2. **Learn the vocabulary precisely** — read the [GPU Glossary](https://modal.com/gpu-glossary) — **Modal (Charles Frye and colleagues)**. *Streaming multiprocessor, warp, tensor core, HBM, NVLink — each defined with its number, cross-linked.*
3. **Take the course** — work through [Deep Learning Systems: Algorithms and Implementation](https://dlsyscourse.org/lectures/) — **Tianqi Chen & Zico Kolter (CMU)**, with the [lecture channel](https://www.youtube.com/@deeplearningsystemscourse1116). *You build automatic differentiation, kernels and a GPU backend yourself; nothing else replaces that.*
4. **See the payoff** — watch [FlashAttention — Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Tri Dao (Stanford MLSys Seminars)**. *A pure input/output-aware rewrite, no approximation: the canonical demonstration of memory-bound thinking.*
5. **Write a kernel** — do [GPU Puzzles](https://github.com/srush/GPU-Puzzles) — **Sasha Rush (Cornell)**, then the [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html). *Twelve small puzzles teach indexing, blocking and shared memory faster than any reading.*

## Courses (free)

- [Deep Learning Systems: Algorithms and Implementation (CMU 10-414/714)](https://dlsyscourse.org/lectures/) — **Tianqi Chen & Zico Kolter (Carnegie Mellon)** — the definitive open course on what sits under PyTorch: autodiff, operators, GPU acceleration, memory optimization; all [lectures on YouTube](https://www.youtube.com/@deeplearningsystemscourse1116).
- [GPU MODE lectures](https://github.com/gpu-mode/lectures) — **Mark Saroufim, Andreas Köpf and the GPU MODE community** — a free, ongoing lecture series on CUDA, Triton, quantization and profiling, with all notebooks and slides in the open.
- [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) — **OpenAI Triton maintainers** — vector add → fused softmax → matrix multiply → fused attention; the shortest path to writing a real kernel in Python.
- [How to Scale Your Model — TPU and GPU chapters](https://jax-ml.github.io/scaling-book/tpus/) — **Google DeepMind JAX team** — the accelerator that is *not* a GPU, explained with the same roofline discipline; see also the [roofline chapter](https://jax-ml.github.io/scaling-book/roofline/).

## Videos

- [FlashAttention — Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Tri Dao (Stanford MLSys Seminars)** — tiling attention into SRAM to avoid materializing the score matrix in HBM; the clearest worked example of hardware-aware algorithm design.
- [Hardware-aware Algorithms for Sequence Modeling — Stanford MLSys #87](https://www.youtube.com/watch?v=foG0ebzuw34) — **Tri Dao (Stanford MLSys Seminars)** — the follow-up: state-space models and linear attention designed around the memory hierarchy.
- [Stanford CS336 — Language Modeling from Scratch, 2025 lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the GPUs and Kernels/Triton lectures profile a real training step and attribute every microsecond.

## Key Papers

- [Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures](https://escholarship.org/content/qt78h8v7mr/qt78h8v7mr.pdf) — **Williams, Waterman & Patterson (2008, Berkeley)** — the original roofline report; the model every accelerator analysis still uses.
- [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) — **Dao, Fu, Ermon, Rudra & Ré (2022)** — tiling and recomputation instead of an $O(n^2)$ HBM round trip.
- [FlashAttention-2](https://arxiv.org/abs/2307.08691) — **Tri Dao (2023)** — better work partitioning across warps; roughly 2× over the original.
- [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision](https://arxiv.org/abs/2407.08608) — **Shah et al. (2024)** — Hopper-specific asynchrony and fp8; how a kernel is co-designed with a new architecture.
- [Mixed Precision Training](https://arxiv.org/abs/1710.03740) — **Micikevicius et al. (2018, NVIDIA & Baidu)** — the fp16 master-weights + loss-scaling recipe that made tensor cores usable.
- [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433) — **Micikevicius et al. (2022)** — E4M3 and E5M2, and where each is safe; the basis of today's fp8 training and inference.

## Articles / Blogs (free, no paywall)

- [Making Deep Learning Go Brrrr From First Principles](https://horace.io/brrr_intro.html) — **Horace He (PyTorch)** — the single best free explanation of compute-bound versus bandwidth-bound versus overhead-bound.
- [GPU Glossary](https://modal.com/gpu-glossary) — **Modal** — a hyperlinked reference for every hardware and software term on this page; start at the [reading guide](https://modal.com/gpu-glossary/readme).
- [Matrix multiplication background and GPU performance background](https://docs.nvidia.com/deeplearning/performance/dl-performance-getting-started/index.html) — **NVIDIA** — the vendor's own arithmetic-intensity guides, including [the GPU performance background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html) with the exact ratios per architecture.
- [PyTorch performance tuning guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html) — **PyTorch maintainers** — channels-last, `torch.compile`, fused optimizers, `set_to_none`: the cheap wins before any kernel writing.
- [Supercharging training using float8 and FSDP2](https://pytorch.org/blog/training-using-float8-fsdp2/) — **PyTorch and IBM teams** — a measured end-to-end fp8 training result, with the numerics caveats stated.
- [NVIDIA Hopper architecture in depth](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/) — **NVIDIA** — the transformer engine, asynchronous copies and the thread-block cluster that FlashAttention-3 exploits.
- [CUTLASS](https://github.com/NVIDIA/cutlass) and the [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) — **NVIDIA** — the reference templates and the language semantics, when the tutorials stop being enough.

## Books (free, with chapters)

- [*How to Scale Your Model* — "All About Roofline" and "What Is a TPU?"](https://jax-ml.github.io/scaling-book/roofline/) — **Google DeepMind** — free online book; the roofline chapter is the best modern restatement of the 2008 model for accelerators.

## In this platform

- Downstream: [Distributed Training — Parallelism, FSDP & ZeRO](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) — what happens when one device is not enough
- Attention kernels have their own owner: [Efficient Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention) (FlashAttention in depth)
- Serving-side consequences: [Scaling Inference](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/scaling-inference/scaling-inference) · [Model Serving](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/model-serving/model-serving) · [Quantization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/quantization/quantization) · [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache)
- What the hardware bill looks like: [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/cost-optimization/cost-optimization)
