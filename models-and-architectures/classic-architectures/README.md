---
id: "models-and-architectures/classic-architectures"
topic: "Classic Architectures"
level: intermediate
built_from: ["neural-network-foundations", "stabilization-and-architectural-blocks"]
updated: 2026-09-13
---

# Classic Architectures

> The network families that came before, beside and after the transformer: convolution for
> grids, recurrence for sequences, autoencoders for compression, and the state-space line that put
> linear recurrences back on the frontier. Attention itself has its own sub-area next door; this
> one is the shortlist of the best free resources for every other way a network is wired.

**Start here:** [CNNs and Convolution](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/cnns-and-convolution/cnns-and-convolution) for the first architecture worth understanding in full, then [On the Tradeoffs of State Space Models and Transformers](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu (2025)** — for the framing of everything after it.

## Concept index

### Grids, sequences and compression

1. [CNNs and Convolution](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/cnns-and-convolution/cnns-and-convolution) — local receptive fields, weight sharing, pooling, and the tensor-shape flow through a small network.
2. [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/rnn-lstm-gru/rnn-lstm-gru) — recurrence, the gating that fixed vanishing gradients, and why the family lost to attention on long sequences.
3. [Autoencoders](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/autoencoders/autoencoders) — bottlenecks, denoising and sparsity; the representation-learning shape variational and diffusion models grew out of.

### Sequence modeling — recurrence, convolution, attention, state space

4. [Sequence Models — Recurrent, Convolutional, Transformer, State-Space](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/sequence-models-recurrent-convolutional-transformer/sequence-models-recurrent-convolutional-transformer) — the four ways one position sees the positions before it, compared on the same axes.
5. [State-Space Models — Foundations](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/state-space-models-foundations/state-space-models-foundations) — continuous-time linear systems, discretization, and the recurrent and convolutional views of the same model.
6. [Structured State-Space Models — S4, S4D, Diagonal SSMs](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/structured-state-space-models-s4/structured-state-space-models-s4) — HiPPO initialization and the structure that makes long-range memory trainable.
7. [Selective State-Space Models — Mamba and Mamba-2](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/selective-state-space-models-mamba/selective-state-space-models-mamba) — input-dependent parameters, the parallel scan, and the duality with attention.
8. [Linear and Hybrid Attention Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/linear-and-hybrid-attention-architectures/linear-and-hybrid-attention-architectures) — how 2025–26 open models mix linear and softmax layers.

## Courses (free)

- [Stanford CS231n — Deep Learning for Computer Vision](https://cs231n.github.io/) — **Stanford** — the convolutional-network notes remain the best free text on the subject.
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Chris Manning)** — the recurrence-to-transformer progression this sub-area assumes.
- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar series where the state-space and hybrid-attention authors present their own work.

## Videos

- [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)** — the definitive author talk on S4 and HiPPO.
- [Mamba and S4 Explained](https://www.youtube.com/watch?v=8Q_tqwpTpVU) — **Umar Jamil** — the full derivation, scan and kernel included.

## Key Papers

- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) — **He et al. (2015)** — the idea that made convolutional networks deep; one of the most-cited papers in ML.
- [Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf) — **Hochreiter and Schmidhuber (1997)** — the gated cell that made recurrence trainable over long ranges.
- [HiPPO: Recurrent Memory with Optimal Polynomial Projections](https://arxiv.org/abs/2008.07669) — **Gu et al. (2020)** — where long-range memory actually comes from.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu and Dao (2023)** — the paper that made SSMs competitive on language.
- [Transformers are SSMs (Mamba-2)](https://arxiv.org/abs/2405.21060) — **Dao and Gu (2024)** — the duality result unifying attention variants and SSMs.

## Articles / Blogs

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — **Chris Olah** — the gold-standard visual explanation of gated recurrence.
- [The Annotated S4](https://srush.github.io/annotated-s4/) — **Sasha Rush and Sidd Karamcheti** — literate, runnable S4.
- [Mamba: The Hard Way](https://srush.github.io/annotated-mamba/hard.html) — **Sasha Rush** — a from-scratch Triton selective scan.
- [Hybrid Attention](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/) — **Sebastian Raschka** — how 2025–26 open models mix linear and softmax layers.

## Books (free, with chapters)

- [*Dive into Deep Learning* — Ch. 7 "Convolutional Neural Networks"](https://d2l.ai/chapter_convolutional-neural-networks/index.html) — **Zhang, Lipton, Li and Smola** — free and runnable; convolution from the cross-correlation operation up.
- [*Dive into Deep Learning* — Ch. 9 "Recurrent Neural Networks"](https://d2l.ai/chapter_recurrent-neural-networks/index.html) — **Zhang, Lipton, Li and Smola** — the free, runnable background text for the sequence pages.

## In this platform

- Section index: [Models and Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/readme) · Sibling sub-areas: [Attention and Transformers](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/readme) · [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) · [Generative Model Families](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/readme)
- Upstream: [Perceptron and MLP](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/perceptron-and-mlp/perceptron-and-mlp) · [Residual / Skip Connections](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/residual-skip-connections/residual-skip-connections) · [Gating Mechanisms](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/gating-mechanisms/gating-mechanisms)
- Downstream: [Efficient Attention](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention) · [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures) · [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) · [Classic CNN Architectures](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/classic-cnn-architectures/classic-cnn-architectures)
- The mental models: [Convolution](/ai-ml/ai-ml-intuitions/architectural-mechanisms/locality-and-weight-sharing/convolution-intuition)
