---
id: "17-tools-and-frameworks/jax-flax"
topic: "JAX (+ Flax) (functional autodiff, jit, vmap, pmap)"
parent: "17-tools-and-frameworks"
level: advanced
built_from: ["python", "numpy", "neural-networks"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "JAX (+ Flax) (functional autodiff, jit, vmap, pmap)"
minutes: 10
category: tools-and-frameworks
---

# JAX (+ Flax) — Functional Autodiff · jit · vmap · pmap
> A NumPy-compatible array library with **composable function transformations**: `grad` (autodiff),
> `jit` (XLA compilation to fast fused kernels), `vmap` (auto-vectorization/batching), and `pmap`
> (multi-device parallelism). **Flax** layers a neural-network library on top. The functional,
> pure-function style makes high-performance research code reproducible and easy to parallelize.

**Why it matters:** JAX is the framework of choice for a lot of cutting-edge research (and TPUs).
It tests a different mental model than PyTorch — pure functions and immutable state, `grad` as a
function transform, why `jit` needs static shapes/tracing, and `vmap`/`pmap` for batching and
scaling. Understanding it sharpens your grasp of autodiff and compilation in general.

**Two 2026 corrections to older tutorials:** the API moved on, and most blog posts did not.

- **Flax NNX replaced Linen** as the recommended API — real Python objects with mutable state, so `self.param` and `apply({'params': ...})` boilerplate is gone.
- **`pmap` is legacy** — device parallelism is now expressed with `jax.jit` over sharded arrays (`Mesh`, `NamedSharding`) and `shard_map` for explicit per-device code.

**Start here — suggested path:**

1. **See the four transforms** — read the [JAX Quickstart](https://docs.jax.dev/en/latest/quickstart.html). *`grad`, `jit`, `vmap` in a few cells — the whole idea in one page.*
2. **Shift your mental model** — work [Thinking in JAX](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html). *Pure functions, tracing, and why JAX differs from NumPy/PyTorch — the key to not getting surprised.*
3. **Watch the intro** — [Intro to JAX: Accelerating ML research](https://www.youtube.com/watch?v=WdTeDXsOSj4) (Google). *A concise official overview of the design and why it's fast.*
4. **Go hero-level on video** — [Machine Learning with JAX — From Zero to Hero](https://www.youtube.com/watch?v=SstuvS-tVc0) (Aleksa Gordić). *Builds real intuition for PyTrees, stateless models, and transforms.*
5. **Add neural nets with Flax** — follow [Flax NNX basics](https://flax.readthedocs.io/en/latest/nnx_basics.html). *Flax gives you Modules and training state on top of pure JAX.*

## Courses (free)
- [JAX tutorials](https://docs.jax.dev/en/latest/tutorials.html) — **JAX team** — the official, structured learning path through the transforms.
- [UvA Deep Learning — Intro to JAX + Flax](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/JAX/tutorial2/Introduction_to_JAX.html) — **University of Amsterdam** — a rigorous, free university tutorial with notebooks.
- [Flax documentation](https://flax.readthedocs.io/en/latest/) — **Flax team (Google)** — the official guide to building/training neural nets in JAX.

## Videos
- [Intro to JAX: Accelerating Machine Learning research](https://www.youtube.com/watch?v=WdTeDXsOSj4) — **Google / TensorFlow** — the concise official overview.
- [JAX Crash Course — Accelerating Machine Learning code](https://www.youtube.com/watch?v=juo5G3t4qAo) — **AssemblyAI** — a fast, practical first look at `grad`/`jit`/`vmap`.
- [Machine Learning with JAX — From Zero to Hero (Tutorial #1)](https://www.youtube.com/watch?v=SstuvS-tVc0) — **Aleksa Gordić (The AI Epiphany)** — the best deep, intuition-building JAX series.
- [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy** — autodiff built by hand; the clearest contrast for what `grad` as a *function transform* changes.

## Key Papers
- [Compiling machine learning programs via high-level tracing (JAX/XLA)](https://mlsys.org/Conferences/doc/2018/146.pdf) — **Frostig, Johnson & Leary (2018)** — the foundational JAX/Autograd-to-XLA paper.
- [JAX documentation](https://docs.jax.dev/en/latest/index.html) — **JAX team** — the canonical reference for transforms and semantics.

## Articles / Blogs (free, no paywall)
- [JAX Quickstart](https://docs.jax.dev/en/latest/quickstart.html) — **JAX team** — the four transforms in one page.
- [Thinking in JAX](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html) — **JAX team** — the functional/tracing mental model.
- [Flax NNX basics](https://flax.readthedocs.io/en/latest/nnx_basics.html) — **Flax team** — Modules and training state on top of JAX.
- [Why Flax NNX](https://flax.readthedocs.io/en/latest/why.html) — **Flax team** — what NNX changed versus Linen, and how to read older Linen code you will still meet in repositories.
- [Introduction to sharded computation](https://docs.jax.dev/en/latest/sharded-computation.html) — **JAX team** — the current multi-device story: sharded arrays, `jit` with a mesh, and `shard_map` — the material `pmap` tutorials predate.

## Books (free, with chapters)
- [Autodidax: JAX core from scratch](https://docs.jax.dev/en/latest/autodidax.html) — **JAX team** — a book-length walkthrough that builds JAX's autodiff/`jit` internals from scratch.
- [UvA DL Notebooks — JAX track](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/JAX/tutorial2/Introduction_to_JAX.html) — **University of Amsterdam** — free, chapter-like notebooks.

## In this platform
- Related domain: [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) · [Advanced Mathematics for AI Research](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/readme)
- Compare with: [05 PyTorch](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pytorch/pytorch) · [06 TensorFlow & Keras](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/tensorflow-and-keras/tensorflow-and-keras)
