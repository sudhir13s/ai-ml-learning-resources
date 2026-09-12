---
id: "17-tools-and-frameworks/tensorflow-keras"
topic: "TensorFlow & Keras (graphs, layers, fit/serve)"
parent: "17-tools-and-frameworks"
level: intermediate
built_from: ["python", "numpy", "neural-networks"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "TensorFlow & Keras (graphs, layers, fit/serve)"
minutes: 10
category: tools-and-frameworks
---

# TensorFlow & Keras — Graphs · Layers · fit / serve
> Google's production-grade DL platform (**TensorFlow**) with **Keras** as its high-level API:
> stack layers, call `model.compile()` / `model.fit()`, and you have a trained model. TensorFlow
> adds graph execution (`tf.function`), `tf.data` pipelines, and a mature serving/mobile/edge stack
> (TF Serving, TFLite, TF.js).

**Why it matters:** Keras is the friendliest on-ramp to deep learning, and TensorFlow still powers
a large installed base of production ML. Interviews probe the Sequential versus Functional API,
eager versus graph execution (`@tf.function`), `tf.data` input pipelines, and how Keras
`fit`/callbacks structure training — plus the trade-offs against PyTorch.

**Where it stands in 2026:** **Keras 3 is multi-backend** — the same model code runs on TensorFlow,
PyTorch or JAX, so "Keras" and "TensorFlow" are no longer the same decision. New research has
largely moved to PyTorch and JAX; TensorFlow's enduring strength is the deployment stack (TF
Serving, TensorFlow Lite/LiteRT, TensorFlow.js) and existing production pipelines. Learn Keras 3
for the modelling API, TensorFlow for the serving and edge story you will inherit.

**Start here — suggested path:**

1. **Build a model in minutes** — read [Keras: Getting started](https://keras.io/getting_started/). *`Sequential` + `fit` gives a working classifier almost immediately.*
2. **Understand the Keras 3 shift** — read [Introducing Keras 3](https://keras.io/keras_3/). *Backend-agnostic models are the single biggest change to this ecosystem in years.*
3. **Learn the APIs that matter** — study the [Keras developer guides](https://keras.io/guides/): the Functional API, custom training loops, and `tf.data` input pipelines. *The Functional API and custom loops are the common interview and extension topics.*
4. **Read the code you will inherit** — skim the [Deep Learning with Python notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks) — **François Chollet**, the author of Keras. *Idiomatic Keras written by its creator, free on GitHub.*
5. **Keep references handy** — bookmark the [Keras examples gallery](https://keras.io/examples/) and the [Keras API reference](https://keras.io/api/). *Adapting a nearby example is the real workflow.*

## Courses (free)
- [Keras developer guides](https://keras.io/guides/) — **Keras team** — a structured course on the Sequential and Functional APIs, training, and customization.
- [Keras API reference](https://keras.io/api/) — **Keras team** — layers, losses, optimizers and callbacks, with the multi-backend behaviour documented per symbol.
- [TensorFlow documentation (source)](https://github.com/tensorflow/docs) — **TensorFlow team** — the official tutorials and guides as notebooks, readable and runnable straight from the repository.

## Videos
- [TensorFlow (official channel)](https://www.youtube.com/@TensorFlow) — **TensorFlow** — release talks, `tf.data` and deployment sessions from the team that ships the framework.
- [Intro to JAX: Accelerating Machine Learning research](https://www.youtube.com/watch?v=WdTeDXsOSj4) — **TensorFlow** — where graph compilation and XLA fit, shared with JAX and Keras 3's JAX backend.
- [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) — **3Blue1Brown** — the model `Sequential` is assembling, before you assemble one.
- [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA) — **StatQuest with Josh Starmer** — what `validation_split` and early-stopping callbacks are actually protecting you from.

## Key Papers
- [TensorFlow: A System for Large-Scale Machine Learning](https://arxiv.org/abs/1603.04467) — **Abadi et al. (2016), OSDI** — the foundational paper on TensorFlow's design.
- [tensorflow/tensorflow (source)](https://github.com/tensorflow/tensorflow) — **TensorFlow team** — the implementation itself, including the RFCs that record why the API looks the way it does.

## Articles / Blogs (free, no paywall)
- [Keras: Getting started](https://keras.io/getting_started/) — **Keras team** — install plus a first model in one page.
- [Introducing Keras 3](https://keras.io/keras_3/) — **François Chollet / Keras team** — the multi-backend rewrite: what changed, what still runs, and how to pick a backend.
- [Keras code examples](https://keras.io/examples/) — **Keras team** — a large, free, copy-adaptable example gallery across domains.
- [TensorFlow blog](https://blog.tensorflow.org/) — **TensorFlow team** — release notes and deployment write-ups; the live source for what is current versus deprecated.

## Books (free, with chapters)
- [Keras developer guides (full set)](https://keras.io/guides/) — **Keras team** — a book-length, free progression through the API.
- [Deep Learning with Python — notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks) — **François Chollet** — every code listing from the book, free and runnable; the book itself is a paid pointer, the notebooks are not.

## In this platform
- Related domain: [05. Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) · [07. Computer Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme)
- Compare with: [05 PyTorch](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pytorch/pytorch) · [07 JAX (+ Flax)](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/jax-and-flax/jax-and-flax)
- Deeper concept (the *why*): serving & deployment → [Deployment & MLOps](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme)
