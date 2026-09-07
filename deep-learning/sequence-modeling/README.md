---
id: "deep-learning/sequence-modeling"
topic: "Sequence Modeling"
level: advanced
built_from: ["rnn-lstm-gru", "attention-mechanism", "transformer-architecture"]
updated: 2026-09-07
---

# Sequence Modeling

> How a model lets one position see the positions before it — recurrence, causal convolution,
> attention, and the state-space family that put linear recurrences back on the frontier. This
> sub-area is the curated shortlist of the best free resources for each step of that story.

**Start here:** read [On the Tradeoffs of State Space Models and Transformers](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu (2025)** — for the framing, then work through [The Annotated S4](https://srush.github.io/annotated-s4/) — **Sasha Rush & Sidd Karamcheti** — for the mechanics.

## Concept Index

1. [Sequence Models — Recurrent, Convolutional, Transformer, State-Space](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/sequence-models-recurrent-convolutional-transformer/sequence-models-recurrent-convolutional-transformer)
2. [State-Space Models — Foundations](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/state-space-models-foundations/state-space-models-foundations)
3. [Structured State-Space Models — S4, S4D, Diagonal SSMs](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/structured-state-space-models-s4/structured-state-space-models-s4)
4. [Selective State-Space Models — Mamba and Mamba-2](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/selective-state-space-models-mamba/selective-state-space-models-mamba)
5. [Linear and Hybrid Attention Architectures](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/linear-and-hybrid-attention-architectures/linear-and-hybrid-attention-architectures)

## Courses (free)

- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar series where the state-space and hybrid-attention authors present their own work.
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Chris Manning)** — the recurrence-to-transformer progression this sub-area assumes.

## Videos

- [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)** — the definitive author talk on S4 and HiPPO.
- [Mamba and S4 Explained](https://www.youtube.com/watch?v=8Q_tqwpTpVU) — **Umar Jamil** — the full derivation, scan and kernel included.

## Key Papers

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)** — the paper that made SSMs competitive on language.
- [Transformers are SSMs (Mamba-2)](https://arxiv.org/abs/2405.21060) — **Dao & Gu (2024)** — the duality result unifying attention variants and SSMs.
- [HiPPO: Recurrent Memory with Optimal Polynomial Projections](https://arxiv.org/abs/2008.07669) — **Gu et al. (2020)** — where long-range memory actually comes from.

## Articles / Blogs

- [The Annotated S4](https://srush.github.io/annotated-s4/) — **Sasha Rush & Sidd Karamcheti** — literate, runnable S4.
- [Mamba: The Hard Way](https://srush.github.io/annotated-mamba/hard.html) — **Sasha Rush** — a from-scratch Triton selective scan.
- [Hybrid Attention](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/) — **Sebastian Raschka** — how 2025–26 open models mix linear and softmax layers.

## Books (free, with chapters)

- [*Dive into Deep Learning* — Ch. 9 "Recurrent Neural Networks"](https://d2l.ai/chapter_recurrent-neural-networks/index.html) — **Zhang, Lipton, Li & Smola** — the free, runnable background text.

## In this platform

- Upstream: [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru) · [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) · [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture)
- Downstream: [Efficient Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention) · [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures) · [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache)
