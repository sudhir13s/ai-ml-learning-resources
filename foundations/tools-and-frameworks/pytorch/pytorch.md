---
id: "17-tools-and-frameworks/pytorch"
topic: "PyTorch (tensors, autograd, nn, training loops)"
core_idea: "PyTorch is eager tensors plus a dynamic autograd graph driven by an explicit training loop — zero_grad, forward, loss, backward, step — with torch.compile as the 2.x route to speed without a rewrite."
parent: "17-tools-and-frameworks"
level: intermediate
built_from: ["python", "numpy", "neural-networks"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "PyTorch (tensors, autograd, nn, training loops)"
minutes: 10
category: tools-and-frameworks
---

# PyTorch — Tensors · Autograd · nn · Training Loops
> The dominant research and production deep-learning framework: GPU-accelerated tensors with a
> NumPy-like API, reverse-mode autodiff (`autograd`), the `nn.Module` building blocks, and the
> explicit Python training loop that makes it easy to read, debug, and extend.

**Why it matters:** PyTorch is the default for modern deep learning and the framework most interviews
assume — explaining autograd and the computation graph, writing a correct training loop (`zero_grad`
→ `forward` → `loss` → `backward` → `step`), the train/eval mode distinction, and moving tensors
between CPU and GPU. It is also the substrate for Hugging Face, Lightning, and most LLM code.

**Where it is in 2026 (PyTorch 2.x):** eager code still reads the same, but the performance story
now runs through the compiler:

- **`torch.compile`** traces your model (TorchDynamo) and generates fused GPU kernels (TorchInductor) — typically a one-line change for a large speedup, and the first thing to try before hand-optimizing.
- **`scaled_dot_product_attention`** gives you FlashAttention-class kernels from the standard API, no custom CUDA.
- **Distributed training** has consolidated on FSDP2 and `DeviceMesh`/`DTensor` for sharding across GPUs.
- **Compiled autograd, `torch.export` and AOTInductor** carry the same graphs into ahead-of-time and non-Python deployment.

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, documentation, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [PyTorch — Tensors · Autograd · nn · Training Loops — references](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pytorch/pytorch#references-further-reading)**
