---
id: "llms-applications-and-agents/large-language-model-foundations"
topic: "Large Language Model Foundations"
level: intermediate
built_from: ["attention-and-transformers", "natural-language-processing"]
updated: 2026-09-07
---

# Large Language Model Foundations

> What a large language model (LLM) *is* before anyone fine-tunes, aligns or serves it: the
> training objective, the architecture that objective selected for, the industrial process of
> pretraining, and the power laws that decide how big and how long. Four pages, read in order —
> every other sub-area in this section assumes them.

**Start here:** [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/language-modeling-objectives/language-modeling-objectives) — causal versus masked is one mask flag and one choice of scored positions, and getting that straight makes the other three pages easy.

## Concept index

Each page is a self-contained resource card with a curated `.references.md` companion: a
plain-words definition, why it matters in 2026, a five-step start-here path, and verified courses,
videos, papers, articles and books.

### What the model is trained to do

1. [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/language-modeling-objectives/language-modeling-objectives) — causal, masked and span-corruption objectives; the chain-rule factorization and perplexity.
2. [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/decoder-only-models/decoder-only-models) — the GPT family shape and why it won: pre-norm blocks, weight tying, causal masking, the modern LLaMA-class recipe.

### How the model is built

3. [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/pretraining/pretraining) — corpora and deduplication, mixed precision, parallelism, model FLOPs utilization, and the failure modes of a long run.
4. [Scaling Laws](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/scaling-laws/scaling-laws) — Kaplan to Chinchilla: the power-law fits, the roughly 20-tokens-per-parameter result, and why inference cost moves the optimum.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang and Tatsunori Hashimoto (Stanford)** — you build the tokenizer, the model, the training loop and the inference path yourself; the current best course on this material.
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — builds a decoder-only GPT from backpropagation upward in plain Python; the best hands-on path in existence.
- [Stanford CS324 — Large Language Models](https://stanford-cs324.github.io/winter2022/) — **Stanford (Liang, Hashimoto et al.)** — defines the objective and interprets the scaling fits inside a full LLM curriculum.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; encoder versus decoder versus encoder-decoder with runnable examples.

## Videos

- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **Andrej Karpathy** — the one-hour mental model built entirely on next-token prediction; the best single framing talk.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — where pretraining sits in the full pipeline, and what each later stage adds.
- [Let's build GPT: from scratch, in code](https://www.youtube.com/watch?v=kCc8FmEb1nY) — **Andrej Karpathy** — the decoder block, causal mask and training loop written line by line in PyTorch.
- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — the decoder stack visualized end to end; watch it before any equation.

## Key Papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — **Vaswani et al. (2017)** — the original Transformer; the decoder block and causal masking these pages build on.
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — **Brown et al. (2020)** — the canonical decoder-only LM at scale, and the appearance of in-context learning.
- [Training Compute-Optimal Large Language Models (Chinchilla)](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (DeepMind, 2022)** — the compute-optimal correction that reset how everyone allocates a training budget.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — **Kaplan et al. (OpenAI, 2020)** — the original power-law study over parameters, data and compute.
- [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) — **Touvron et al. (Meta, 2023)** — RMSNorm plus rotary position embedding (RoPE) plus SwiGLU: the modern decoder recipe, spelled out.

## Articles / Blogs (free, no paywall)

- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI (Quentin Anthony et al.)** — the `C ≈ 6ND` compute arithmetic and full memory accounting behind both the pretraining and scaling pages.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — **Jay Alammar** — the visual foundation under the decoder block; still the most-linked explainer in the field.
- [Understanding Large Language Models](https://magazine.sebastianraschka.com/p/understanding-large-language-models) — **Sebastian Raschka** — situates causal versus masked objectives across the key papers, with the history of how each was chosen.
- [FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face** — a web-scale pretraining data pipeline documented in full: extraction, deduplication, filtering, decontamination.

## Books (free, with chapters)

- [*Speech and Language Processing*, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky and Martin** — free draft; the decoder-only architecture and autoregressive decoding in textbook form.
- [*Speech and Language Processing*, 3rd ed. — Ch. 3 "N-gram Language Models"](https://web.stanford.edu/~jurafsky/slp3/3.pdf) — **Jurafsky and Martin** — where the chain-rule factorization and perplexity are actually derived.
- [*Dive into Deep Learning* — Ch. 11 "Attention Mechanisms and Transformers"](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html) — **Zhang, Lipton, Li and Smola** — free and runnable; the transformer block with working code.
- [*How to Scale Your Model* — "Transformers"](https://jax-ml.github.io/scaling-book/transformers/) — **Google DeepMind (Austin et al.)** — free online; the parameter, FLOP and memory accounting that turns architecture choices into budget numbers.

## In this platform

- Section index: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- What comes next: [LLM Model Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/readme) · [Training and Adaptation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/readme) · [Inference and Runtime](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/readme) · [Reasoning, Evaluation and Alignment](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/readme)
- Prerequisites in this platform: [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) · [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) · [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding)
- Where the pretraining systems detail lives: [Distributed Training — Parallelism, FSDP and ZeRO](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) · [GPUs and Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning)
- The mental models: [Neural Scaling Laws and Chinchilla](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/scaling-behavior/neural-scaling-laws-and-chinchilla-intuition) · [Tokenization and BPE](/ai-ml/ai-ml-intuitions/representation/discrete-representations/tokenization-and-bpe-intuition) · [Categorical Cross-Entropy](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/training-objectives/categorical-cross-entropy-intuition)
- Doing it rather than reading it: [Model Training workflow](/ai-ml/practitioner-workflows/workflow-library/training-and-adaptation/model-training)
