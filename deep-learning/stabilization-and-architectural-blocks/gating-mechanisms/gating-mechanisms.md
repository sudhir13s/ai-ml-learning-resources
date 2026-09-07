---
id: "deep-learning/stabilization-and-architectural-blocks/gating-mechanisms"
topic: "Gating Mechanisms"
level: intermediate
built_from: ["activation-functions", "rnn-lstm-gru", "residual-skip-connections"]
leads_to: ["selective-state-space-models-mamba"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 13
title: "Gating Mechanisms"
minutes: 13
category: stabilization-and-architectural-blocks
---

# Gating Mechanisms

> A gate is a learned, data-dependent multiplier in $[0, 1]$ (or an unbounded scalar) applied
> elementwise to a signal: $\text{out} = \sigma(W_g x) \odot h$. That single construction shows up
> as LSTM forget gates, highway-network transform gates, the gated linear unit (GLU) and SwiGLU in
> transformer feed-forward blocks, the selection mechanism in Mamba, and the router in a
> mixture-of-experts layer.

**Why it matters:** gating is how a network gets **multiplicative, input-conditioned** control
over information flow — additive layers alone cannot express "let this through, block that". It is
also a gradient device: the LSTM's forget gate creates the additive cell path that turns a
repeated matrix product into a near-identity highway. In 2026 the most common gate in production
is SwiGLU, which is why nearly every open LLM feed-forward block has three weight matrices instead
of two and a hidden width of about $\tfrac{8}{3}d$ rather than $4d$.

**Start here — suggested path:**

1. **See the original gate** — read [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — **Chris Olah**. *Forget, input and output gates drawn as valves on a conveyor belt; still the clearest account.*
2. **See it as a depth device** — read [Highway Networks](https://arxiv.org/abs/1505.00387) — **Srivastava, Greff & Schmidhuber (2015)**. *A gate that interpolates between transform and carry; residual connections are the special case where the gate is fixed open.*
3. **See it enter feedforward layers** — read [Language Modeling with Gated Convolutional Networks](https://arxiv.org/abs/1612.08083) — **Dauphin, Fan, Auli & Grangier (2016)**. *The GLU: half the projection becomes a gate on the other half.*
4. **See the variant everyone ships** — read [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) — **Noam Shazeer (2020)**. *Two pages, an honest "we offer no explanation", and the SwiGLU block now used by Llama, Mistral, Qwen and Gemma.*
5. **See gating as selection** — read [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)**. *The input-dependent step size is a forget gate on a linear recurrence.*

## The same idea in six places

- **Recurrent gates (LSTM, GRU)** — control what the state keeps, and create the additive gradient path.
- **Highway gates** — control how much of a layer's input passes through unchanged; the ancestor of residual connections.
- **GLU / SwiGLU** — an elementwise gate inside the feed-forward block; the 2026 default.
- **Gated attention** — a sigmoid gate on the attention output that suppresses attention sinks and adds sparsity.
- **Selection (Mamba)** — a gate on a linear recurrence's step size, which is what makes a state-space model content-aware.
- **Routers (mixture of experts)** — a gate over *experts* rather than over features; the same softmax, applied to a different axis.

## Courses (free)

- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Chris Manning)** — the LSTM/GRU lecture derives each gate and its gradient effect.
- [Dive into Deep Learning — Recurrent Neural Networks](https://d2l.ai/chapter_recurrent-neural-networks/index.html) — **Zhang, Lipton, Li & Smola** — gated recurrence with runnable PyTorch, free and open.

## Videos

- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — the feed-forward block where the modern GLU gate lives, drawn geometrically.
- [Mamba and S4 Explained](https://www.youtube.com/watch?v=8Q_tqwpTpVU) — **Umar Jamil** — shows the selection gate explicitly as a learned forget mechanism.

## Key Papers

- [Highway Networks](https://arxiv.org/abs/1505.00387) — **Srivastava, Greff & Schmidhuber (2015)** — gating as the enabler of very deep networks.
- [Learning Phrase Representations using RNN Encoder-Decoder (GRU)](https://arxiv.org/abs/1406.1078) — **Cho et al. (2014)** — the update and reset gates; the LSTM simplified to two gates.
- [LSTM: A Search Space Odyssey](https://arxiv.org/abs/1503.04069) — **Greff, Srivastava, Koutník, Steunebrink & Schmidhuber (2015)** — the ablation that identifies the forget gate as the indispensable one.
- [Language Modeling with Gated Convolutional Networks](https://arxiv.org/abs/1612.08083) — **Dauphin et al. (2016)** — introduces the GLU.
- [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) — **Shazeer (2020)** — SwiGLU and GEGLU; the source of the modern feed-forward block.
- [Transformer Quality in Linear Time](https://arxiv.org/abs/2202.10447) — **Hua, Dai, Liu & Le (2022)** — the gated attention unit, a single-head gated block replacing attention plus feed-forward.
- [Gated Attention for Large Language Models](https://arxiv.org/abs/2505.06708) — **Qiu et al. (Qwen team, 2025)** — a 2025 study of where a gate helps in attention, and its effect on attention sinks.

## Articles / Blogs (free, no paywall)

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — **Chris Olah** — the canonical gate diagrams.
- [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) — **Andrej Karpathy** — includes visualisations of what individual gates learn to track.
- [Hybrid Attention](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/) — **Sebastian Raschka** — shows where gates sit in current open-model architectures.

## In this platform

- Prerequisites: [Activation Functions](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/activation-functions/activation-functions) · [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru)
- The ungated special case: [Residual / Skip Connections](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/residual-skip-connections/residual-skip-connections)
- Gating over experts is owned by [Mixture of Experts](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/mixture-of-experts/mixture-of-experts); gating over a linear recurrence by [Selective State-Space Models (Mamba)](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/selective-state-space-models-mamba/selective-state-space-models-mamba).
- Why the gradient path matters: [Vanishing / Exploding Gradients](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/vanishing-exploding-gradients/vanishing-exploding-gradients)
