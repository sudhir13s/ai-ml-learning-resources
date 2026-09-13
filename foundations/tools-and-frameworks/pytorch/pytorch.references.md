---
id: "17-tools-and-frameworks/pytorch/references"
topic: "PyTorch (tensors, autograd, nn, training loops) — References"
parent: "17-tools-and-frameworks/pytorch"
type: references
updated: 2026-09-14
---

# PyTorch — Tensors · Autograd · nn · Training Loops — references

> Companion link library for **[PyTorch — Tensors · Autograd · nn · Training Loops](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pytorch/pytorch)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Do the 60-minute blitz** — [Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html). *The official fast intro to tensors, autograd, and a first network.*
2. **Learn the basics properly** — work the [Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) series. *A clean, modern path through datasets, models, autograd, and the training loop.*
3. **Build it end to end on video** — [Learn PyTorch for deep learning in a day](https://www.youtube.com/watch?v=Z_ikDlimN6A) — **Daniel Bourke**. *Watching the workflow built from scratch cements the training-loop pattern.*
4. **Understand autograd deeply** — build it yourself with [micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) (Karpathy), then read how `requires_grad`, `.backward()` and the dynamic graph work in the [docs](https://pytorch.org/docs/stable/index.html). *Autograd is the most-asked PyTorch interview topic, and 100 lines of scalar autodiff explains all of it.*
5. **Turn on the 2.x compiler** — take a working model through the [torch.compile tutorial](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) and measure before/after. *Knowing what compiles, what graph-breaks, and what it buys you is the current practitioner bar.*

**In this platform**:
- [05. Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) — related domain.
- [08 Hugging Face](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/hugging-face/hugging-face) — pairs with.
- [09 ONNX](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/onnx-and-model-interchange/onnx-and-model-interchange) — pairs with.
- [12 Weights & Biases](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/weights-and-biases/weights-and-biases) — pairs with.
- [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — related domain.

**Videos**:
- [Learn PyTorch for deep learning in a day. Literally.](https://www.youtube.com/watch?v=Z_ikDlimN6A) — **Daniel Bourke** — a single-sitting, hands-on fundamentals course from the author of the free book below.
- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **Andrej Karpathy** — modern PyTorch as practitioners write it: mixed precision, `torch.compile`, flash attention, distributed data parallel.
- [PyTorch Tutorials — Complete Beginner Course](https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4) — **Patrick Loeber** — short, sharply-scoped episodes (tensors, autograd, `Dataset`/`DataLoader`, transfer learning); the best "look up one mechanism" series.
- [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy** — autograd rebuilt from nothing, so PyTorch's `.backward()` stops being magic.

**Courses**:
- [Learn PyTorch for Deep Learning (Zero to Mastery)](https://www.learnpytorch.io/) — **Daniel Bourke** — a free, comprehensive online book + course with runnable notebooks.

**Articles**:
- [Get Started (install + first run)](https://pytorch.org/get-started/locally/) — **PyTorch team** — the official install/setup guide.
- [PyTorch 2 paper walkthrough](https://pytorch.org/blog/pytorch-2-paper-tutorial/) — **PyTorch team** — the design of TorchDynamo and TorchInductor, from the people who built them.

**Papers**:
- [PyTorch: An Imperative Style, High-Performance Deep Learning Library](https://arxiv.org/abs/1912.01703) — **Paszke et al. (2019), NeurIPS** — the foundational paper on PyTorch's design.

**Documentation**:
- [Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) — **PyTorch team** — the fastest correct on-ramp.
- [Introduction to `torch.compile`](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) — **PyTorch team** — what Dynamo traces, what causes a graph break, and how to measure the speedup.
- [PyTorch — Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) — **PyTorch team** — the modern step-by-step fundamentals series.
- [PyTorch documentation](https://pytorch.org/docs/stable/index.html) — **PyTorch team** — the canonical reference for tensors, autograd, and `nn`.
- [PyTorch official tutorials](https://pytorch.org/tutorials/) — **PyTorch team** — the authoritative library of tutorials, from the blitz to advanced topics.

**Books**:
- [Learn PyTorch for Deep Learning (online book)](https://www.learnpytorch.io/) — **Daniel Bourke** — a free, chapter-structured book with notebooks.
- [pytorch-deep-learning (course materials)](https://github.com/mrdbourke/pytorch-deep-learning) — **Daniel Bourke** — all notebooks and exercises, free on GitHub.
