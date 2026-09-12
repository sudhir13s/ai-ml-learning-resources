---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-programming"
topic: "Differentiable Programming"
level: advanced
built_from: ["neuro-symbolic-ai"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Differentiable Programming"
minutes: 17
category: differentiable-reasoning
---

# Differentiable Programming
> Treat a **program** — not just a network — as the thing you differentiate. If every operation has
> a derivative, then control flow, physics simulators, optimizers, ordinary differential equation
> solvers, and relaxed logic can all sit inside a model and be trained by gradient descent. Deep
> learning becomes a special case of a much larger idea.

**Why it matters:** this is the mechanism that lets symbolic structure be *learned* rather than
bolted on. Every relaxation in neuro-symbolic AI — soft logic, differentiable solvers, implicit
layers — depends on it, and the practical questions are the same each time: what does the
relaxation break, does the gradient actually carry information, and how much memory does the
backward pass cost?

**Start here — suggested path:**

1. **Build automatic differentiation yourself** — watch [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy**. *A hundred lines of scalar autograd; nothing about the topic stays mysterious afterwards.*
2. **Get the computational picture** — read [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/) — **Chris Olah**. *Forward-mode versus reverse-mode, and why reverse mode is what deep learning uses.*
3. **Read the survey** — [Automatic differentiation in machine learning: a survey](https://arxiv.org/abs/1502.05767) — **Baydin, Pearlmutter, Radul & Siskind (2015)**. *The precise vocabulary: dual numbers, tapes, checkpointing, and what autodiff is not.*
4. **Take the modern book** — [*The Elements of Differentiable Programming*](https://diffprog.github.io/) — **Mathieu Blondel & Vincent Roulet (Google DeepMind)**. *The 2024-25 reference that unifies autodiff, optimization, and probability; free on arXiv with accompanying code.*
5. **Differentiate through a solver** — work the [implicit layers tutorial](http://implicit-layers-tutorial.org/) — **Duvenaud, Kolter & Johnson (NeurIPS 2020)**. *Layers defined by the solution of an optimization or equation, differentiated by the implicit function theorem — the trick behind differentiable reasoning.*

## Courses (free)
- [*The Elements of Differentiable Programming* book site](https://diffprog.github.io/) — **Blondel & Roulet (Google DeepMind)** — free book plus a Python repository; effectively a graduate course with exercises.
- [Deep Implicit Layers: Neural ODEs, Deep Equilibrium Models, and Beyond](http://implicit-layers-tutorial.org/) — **David Duvenaud, Zico Kolter & Matt Johnson** — the free NeurIPS 2020 tutorial, with runnable JAX and PyTorch notebooks.
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — starts by building the autograd engine everything else here assumes.

## Videos
- [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy** — reverse-mode autodiff implemented from first principles.
- [What is Automatic Differentiation?](https://www.youtube.com/watch?v=wG_nF1awSSY) — **Ari Seff** — the clearest short visual explanation of forward versus reverse mode and why symbolic and numeric differentiation are different things.

## Key Papers
- [The Elements of Differentiable Programming](https://arxiv.org/abs/2403.14606) — **Mathieu Blondel & Vincent Roulet (2024, v4 2025)** — the book-length treatment; read Ch. 2-4 for the differentiation machinery and Ch. 10+ for differentiable optimization.
- [Automatic differentiation in machine learning: a survey](https://arxiv.org/abs/1502.05767) — **Baydin, Pearlmutter, Radul & Siskind (2015)** — the standard survey; still the best definition of the field.
- [Neural Ordinary Differential Equations](https://arxiv.org/abs/1806.07366) — **Chen, Rubanova, Bettencourt & Duvenaud (2018)** — a solver as a layer, with constant-memory gradients via the adjoint method.
- [OptNet: Differentiable Optimization as a Layer in Neural Networks](https://arxiv.org/abs/1703.00443) — **Brandon Amos & Zico Kolter (2017)** — differentiating through a quadratic program; the template for putting a constrained solver inside a network.

## Articles / Blogs (free, no paywall)
- [The Autodiff Cookbook](https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html) — **JAX developers (Google)** — Jacobian-vector and vector-Jacobian products, made concrete; the best practical reference in either framework.
- [Autograd mechanics](https://pytorch.org/docs/stable/notes/autograd.html) — **PyTorch team** — how the tape, graph, and in-place operations actually behave, including the failure modes people hit.
- [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/) — **Chris Olah** — the intuition that makes the survey above readable.

## Books (free, with chapters)
- [*The Elements of Differentiable Programming*](https://diffprog.github.io/) — **Blondel & Roulet (2025)** — free, current, and the only book that treats this as one subject rather than a deep-learning appendix.

## In this platform
- Prerequisites: [Backpropagation and Computational Graphs](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/backpropagation-and-computational-graphs/backpropagation-and-computational-graphs) · [The Neural Learning Paradigm](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neural-learning-paradigm/neural-learning-paradigm)
- Why it belongs here: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · next: [Neural Theorem Proving](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving/neural-theorem-proving)
- Tooling: [JAX and Flax](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/jax-and-flax/jax-and-flax) · [PyTorch](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pytorch/pytorch)
