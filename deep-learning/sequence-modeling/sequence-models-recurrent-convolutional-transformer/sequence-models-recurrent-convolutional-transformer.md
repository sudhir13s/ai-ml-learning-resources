---
id: "deep-learning/sequence-modeling/sequence-models-recurrent-convolutional-transformer"
topic: "Sequence Models — Recurrent, Convolutional, Transformer, State-Space"
level: intermediate
built_from: ["rnn-lstm-gru", "cnns-and-convolution", "attention-mechanism"]
leads_to: ["deep-learning/sequence-modeling/state-space-models-foundations", "deep-learning/sequence-modeling/linear-and-hybrid-attention-architectures"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Sequence Models — Recurrent, Convolutional, Transformer, State-Space"
minutes: 14
category: sequence-modeling
---

# Sequence Models — Recurrent, Convolutional, Transformer, State-Space

> Four families answer one question — *how does a token get to see the tokens before it?*
> A **recurrent network (RNN)** passes a fixed-size state forward step by step; a **temporal
> convolutional network (TCN)** stacks dilated causal convolutions to grow a receptive field; a
> **transformer** lets every token attend to every other token directly; a **state-space model
> (SSM)** learns a linear recurrence that can be *unrolled as a convolution* and therefore
> trained in parallel like a transformer but run like an RNN.

**Why it matters:** every 2026 long-context architecture is a point on this map — pure attention
(GPT-class), pure SSM (Mamba), or a hybrid stack (Jamba, Nemotron-H, Qwen3-Next). Interviewers
probe the three axes that separate the families: **training parallelism**, **inference cost per
token**, and **exact recall of a distant token**. The trap is calling SSMs "faster transformers":
they buy constant-memory decoding by *compressing* history into a fixed state, which is exactly
where they lose the needle-in-a-haystack retrieval that softmax attention gets for free.

**Start here — suggested path:**

1. **Feel why sequences are different** — read [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) — **Andrej Karpathy**. *A character-level RNN generating Shakespeare makes "state carried across time" concrete before any equation.*
2. **See the recurrent failure mode** — read [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — **Chris Olah**. *The gated-memory picture that explains why plain recurrence forgets and gating fixes it.*
3. **Learn the convolutional alternative** — read [An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling](https://arxiv.org/abs/1803.01271) — **Bai, Kolter & Koltun (2018)**. *The TCN paper: dilated causal convolutions beat LSTMs on many benchmarks and are trivially parallel.*
4. **Get the attention answer** — watch [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown**. *The clearest visual account of why direct all-to-all routing replaced sequential state.*
5. **See the 2026 fourth family** — read [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)**. *The paper that put state-space models back on the frontier; the rest of this sub-area unpacks it.*

## The four families at a glance

- **Recurrent** — $O(T)$ sequential training, $O(1)$ state per step, memory decays with distance.
- **Convolutional (TCN, WaveNet)** — parallel training, receptive field grows exponentially with dilation depth, but is still *finite*.
- **Attention** — parallel training, $O(T^2)$ compute and a key-value (KV) cache growing linearly with context, exact access to any earlier token.
- **State-space** — parallel training via scan or convolution, $O(1)$ state at inference, lossy long-range recall.

## Courses (free)

- [Stanford CS224N: Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Chris Manning)** — the lecture sequence that walks RNN → seq2seq → attention → transformer in the order the field actually discovered them.
- [Dive into Deep Learning — Recurrent Neural Networks](https://d2l.ai/chapter_recurrent-neural-networks/index.html) — **Zhang, Lipton, Li & Smola** — free textbook chapter with runnable PyTorch for every variant.
- [MIT 6.S191: Introduction to Deep Learning](https://introtodeeplearning.com/) — **MIT (Alexander Amini et al.)** — the deep-sequence-modeling lecture is refreshed yearly and now covers SSMs alongside transformers.

## Videos

- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — geometric intuition for why attention routes information better than a hidden state.
- [Attention Is All You Need (paper explained)](https://www.youtube.com/watch?v=iDulhoQ2pro) — **Yannic Kilcher** — a close reading of the paper that ended the RNN era, including what it gave up.
- [MAMBA and State Space Models explained](https://www.youtube.com/watch?v=vrF3MtGwD0Y) — **AI Coffee Break with Letitia** — a short, accurate bridge from RNN intuition to the selective SSM idea.

## Key Papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — **Vaswani et al. (2017)** — removes recurrence entirely; the reference point every other family is measured against.
- [An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling](https://arxiv.org/abs/1803.01271) — **Bai, Kolter & Koltun (2018)** — the TCN case: causal dilated convolutions as a serious sequence baseline.
- [WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499) — **van den Oord et al. (2016)** — dilated causal convolutions at 16 kHz; the origin of the "exponential receptive field" trick.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)** — input-dependent state-space recurrence with a hardware-aware parallel scan.
- [Long Range Arena: A Benchmark for Efficient Transformers](https://arxiv.org/abs/2011.04006) — **Tay et al. (2020)** — the benchmark that exposed how differently these families behave at length.

## Articles / Blogs (free, no paywall)

- [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) — **Andrej Karpathy** — still the best on-ramp to sequence modeling.
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — **Chris Olah** — the diagram set the whole field reuses.
- [WaveNet: A Generative Model for Raw Audio](https://deepmind.google/discover/blog/wavenet-a-generative-model-for-raw-audio/) — **Google DeepMind** — the authors' own walkthrough of dilated causal convolution, with audio samples.
- [On the Tradeoffs of State Space Models and Transformers](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu (2025)** — the most honest current statement of what each family is actually good at.

## Books (free, with chapters)

- [*Dive into Deep Learning* — Ch. 9 "Recurrent Neural Networks"](https://d2l.ai/chapter_recurrent-neural-networks/index.html) — **Zhang, Lipton, Li & Smola** — derivations plus runnable code, free and open.

## In this platform

- Prerequisites: [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru) · [CNNs & Convolution](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/cnns-and-convolution/cnns-and-convolution) · [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism)
- The attention family in depth: [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) · [Efficient Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention)
- Next in this sub-area: [State-Space Models — Foundations](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/state-space-models-foundations/state-space-models-foundations) · [Linear and Hybrid Attention Architectures](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/linear-and-hybrid-attention-architectures/linear-and-hybrid-attention-architectures)
- At LLM scale: [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures) · [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache)
