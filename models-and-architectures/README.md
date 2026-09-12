---
id: "models-and-architectures"
topic: "Models and Architectures"
level: intermediate
built_from: ["deep-learning"]
updated: 2026-09-13
---

# Models and Architectures

> The model families, as families: how each is wired, what each is good at, and why the field
> moved from one to the next. [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
> teaches how any network learns; this section teaches the shapes those networks take — from
> convolution and recurrence through attention to the large language models and the generative
> families. A new family gets one landing place here.

**Start here:** [Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism) if you want the one mechanism every modern model shares, or [Classic Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/readme) to see what came before it and what is coming after.

## Sub-areas

Each sub-area has its own curated index; each page inside is a resource card with a definition,
a five-step start-here path, and verified courses, videos, papers, articles and books.

1. [Classic Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/readme) — **8 pages** — convolutional networks, recurrent networks, autoencoders, and the sequence-modeling line from recurrence through state-space models to linear and hybrid attention.
2. [Attention and Transformers](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism) — **4 pages** — the attention mechanism, the transformer architecture, positional encoding, and efficient attention (FlashAttention).
3. [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — **11 pages** — objectives, the decoder-only shape, scaling laws, the redesigned attention block, long context, mixture-of-experts, diffusion language models, and reasoning at inference time.
4. [Generative Model Families](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/readme) — **24 pages** — variational autoencoders, generative adversarial networks, flows and energy-based models, then the diffusion line from DDPM to flow matching and few-step generation.

## Courses (free)

- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — builds backprop → GPT from scratch in plain Python; the best hands-on course in existence.
- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar where architecture authors present their own work.
- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang and Tatsunori Hashimoto (Stanford)** — the architecture lectures are a data-driven survey of what frontier models actually changed.
- [Stanford CS236 — Deep Generative Models](https://deepgenerativemodels.github.io/) — **Stefano Ermon (Stanford)** — the score-based and diffusion lectures, from the group that co-invented score matching.

## Videos

- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — the decoder stack visualized end to end; watch it before any equation.
- [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM) — **Stanford MLSys Seminars (Albert Gu)** — the definitive author talk on the non-attention branch.
- [Variational Autoencoders and Diffusion Models](https://www.youtube.com/watch?v=pea3sH6orMc) — **Tim Salimans (Google DeepMind)** — a researcher who built progressive distillation explaining why few-step sampling works.

## Key Papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — **Vaswani et al. (2017)** — the architecture the whole section revolves around.
- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) — **He et al. (2015)** — the idea that made networks deep.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu and Dao (2023)** — the non-attention alternative that became competitive at scale.
- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) — **Ho, Jain and Abbeel (2020)** — the paper that made diffusion the dominant generative family.

## Articles / Blogs

- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka** — the single best free survey of what recent models actually changed.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — **Jay Alammar** — still the most-linked explainer in the field.
- [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — **Lilian Weng** — the canonical open math walkthrough of the generative family that won.

## Books (free)

- [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) — **Zhang, Lipton, Li and Smola** — free, interactive, runnable code for every architecture in this section.
- [*Understanding Deep Learning*](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; transformers, generative adversarial networks, variational autoencoders and diffusion in one modern text.

## In this platform

- Before this section: [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) — how any of these networks learns.
- After this section: [Data and Representation](/ai-ml/ai-ml-learning-resources/data-and-representation/readme) · [Model Building](/ai-ml/ai-ml-learning-resources/model-building/readme) · [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme) · [Inference and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/readme)
- Where the families meet data: [Multimodal and Generative Media](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/readme) · [World Models and Embodied AI](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/readme)
- The mental models: [Multi-Head Attention](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/multi-head-attention-intuition) · [Convolution](/ai-ml/ai-ml-intuitions/architectural-mechanisms/locality-and-weight-sharing/convolution-intuition) · [Diffusion Forward and Reverse Process](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition)
