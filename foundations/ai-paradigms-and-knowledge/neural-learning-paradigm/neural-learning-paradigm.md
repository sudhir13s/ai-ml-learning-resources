---
id: "foundations/ai-paradigms-and-knowledge/neural-learning-paradigm"
topic: "The Neural Learning Paradigm"
level: beginner
built_from: ["statistical-learning-paradigm"]
leads_to: ["foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models", "foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 15
title: "The Neural Learning Paradigm"
minutes: 15
category: ai-paradigms-and-knowledge
---

# The Neural Learning Paradigm
> The third paradigm — **connectionism**: intelligence emerges from many simple units with learned
> weights, and the useful *representations* are discovered by the model rather than designed by a
> person. Stack differentiable layers, define a loss, follow the gradient, and features come out of
> the optimization instead of a feature-engineering meeting.

**Why it matters:** representation learning is the whole reason deep learning displaced hand-built
pipelines, and it is the assumption behind every foundation model in 2026 — one pretrained
representation, many downstream tasks. The interview probe is the trade-off: neural systems buy
representation power with data, compute, and opacity, and they still cannot guarantee a symbolic
constraint the way a solver can.

**Start here — suggested path:**

1. **See what a network computes** — watch [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) — **3Blue1Brown (Grant Sanderson)**. *The geometric picture of layers as learned feature detectors, before any code.*
2. **Read the founders' own summary** — [Deep Learning](https://www.nature.com/articles/nature14539) — **LeCun, Bengio & Hinton (Nature, 2015)**. *The authoritative statement of the paradigm: learned representations, end to end, at scale.*
3. **Understand the learning rule** — [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0) — **Rumelhart, Hinton & Williams (Nature, 1986)**. *The paper that made hidden layers trainable and revived connectionism.*
4. **Build one from nothing** — watch [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy**. *Two hours from scalar autograd to a working network; the paradigm stops being abstract.*
5. **Get the "why representations" argument** — read [Representation Learning: A Review and New Perspectives](https://arxiv.org/abs/1206.5538) — **Bengio, Courville & Vincent (2012)**. *The case for learned features, written before it won.*

## Courses (free)
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — builds autograd, then a language model, from scratch in plain Python; the best hands-on entry to the paradigm.
- [Dive into Deep Learning](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — free interactive textbook and course, every chapter runnable in PyTorch, JAX, and TensorFlow.
- [Stanford CS336: Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford (Percy Liang, Tatsunori Hashimoto)** — the current graduate course that carries the paradigm to modern scale, with free lectures and assignments.

## Videos
- [Neural networks (full series)](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — **3Blue1Brown** — the definitive visual account of what layers, weights, and gradient descent are doing.
- [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy** — the implementer's view; every abstraction is opened.
- [The Deep Learning Revolution — 2018 ACM A.M. Turing Award Lecture](https://www.youtube.com/watch?v=VsnQf7exv5I) — **Geoffrey Hinton and Yann LeCun (ACM)** — the paradigm's history and claims from the people who were awarded for it.

## Key Papers
- [Deep Learning](https://www.nature.com/articles/nature14539) — **LeCun, Bengio & Hinton (2015)** — the field's authoritative review; read it as the paradigm's position statement.
- [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0) — **Rumelhart, Hinton & Williams (1986)** — backpropagation as the mechanism that makes learned internal representations possible.
- [The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain](https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf) — **Frank Rosenblatt (1958)** — where connectionism starts, and the model whose limits caused its first winter.
- [Representation Learning: A Review and New Perspectives](https://arxiv.org/abs/1206.5538) — **Bengio, Courville & Vincent (2012)** — the survey that framed "learn the features" as the central problem.
- [Deep Learning for AI](https://dl.acm.org/doi/10.1145/3448250) — **Bengio, LeCun & Hinton (2021 Turing Lecture)** — the retrospective, including the open problems the authors admit remain.

## Articles / Blogs (free, no paywall)
- [Deep Learning, NLP, and Representations](https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/) — **Chris Olah** — the clearest intuition for why learned embeddings carry structure.
- [Feature Visualization](https://distill.pub/2017/feature-visualization/) — **Olah, Mordvintsev & Schubert (Distill)** — what the learned representations actually look like, made visible.

## Books (free, with chapters)
- [*Neural Networks and Deep Learning* — Ch. 1 "Using neural nets to recognize handwritten digits"](http://neuralnetworksanddeeplearning.com/) — **Michael Nielsen** — free; the gentlest complete derivation of the paradigm's core loop.
- [*Deep Learning* — Ch. 6 "Deep Feedforward Networks", Ch. 15 "Representation Learning"](https://www.deeplearningbook.org/) — **Goodfellow, Bengio & Courville** — free online; the rigorous reference.
- [*Dive into Deep Learning* — Ch. 5 "Multilayer Perceptrons"](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — free and runnable, one notebook per idea.

## In this platform
- Prior paradigm: [The Statistical Learning Paradigm](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/statistical-learning-paradigm/statistical-learning-paradigm) · Next: [Probabilistic Reasoning and Graphical Models](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models/probabilistic-reasoning-and-graphical-models)
- The mechanisms, taught in depth: [Perceptron and MLP](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/perceptron-and-mlp/perceptron-and-mlp) · [Backpropagation and Computational Graphs](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/backpropagation-and-computational-graphs/backpropagation-and-computational-graphs) · [How Models Learn](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/how-models-learn/how-models-learn)
- Where the two traditions meet: [Neuro-Symbolic AI Overview](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview/neuro-symbolic-ai-overview) · [Differentiable Programming](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-programming/differentiable-programming)
