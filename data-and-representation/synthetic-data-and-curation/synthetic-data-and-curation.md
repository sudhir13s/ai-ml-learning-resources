---
id: "data-and-representation/synthetic-data-and-curation"
topic: "Synthetic Data and Data Curation"
level: intermediate
built_from: ["pretraining", "instruction-tuning"]
leads_to: ["model-adaptation/reinforcement-learning-posttraining", "09-llms/llm-evaluation-and-benchmarks"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Synthetic Data and Data Curation"
minutes: 16
category: data-and-representation
---

# Synthetic Data and Data Curation

> Modern model quality is decided by the dataset far more than by the architecture. Two levers do
> the work: **curation** — filtering, deduplicating and quality-classifying web text until what is
> left is worth training on — and **synthesis** — generating instructions, answers and textbook-style
> explanations with a strong model, then filtering those too.

**Why it matters:** every post-2023 open model that punches above its size (Phi, SmolLM, Nemotron,
Tülu, the R1 distills) got there through data work, not a new block.

- **What is probed:** the Self-Instruct loop and how Evol-Instruct deepens it; why an educational-quality classifier (FineWeb-Edu) beats bigger raw corpora; the deduplication and decontamination pipeline; who owns the licence to the generated data.
- **The trade-off:** synthetic data is cheap and targetable but inherits the teacher's blind spots, narrows diversity, and — unchecked — leaks the benchmark into training.
- **The failure mode:** a model that improves on every benchmark and on nothing real. **Contamination** is the default outcome of naive web-scale synthesis, not an edge case; decontaminate against your eval sets *and* keep a private held-out set.

**Start here — suggested path:**

1. **See what curation actually is** — read [The FineWeb blog post](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face (Penedo et al.)**. *Every filtering decision, ablated, with the resulting benchmark delta — the best free tour of a real pipeline.*
2. **Read the founding synthesis loop** — read [Self-Instruct](https://arxiv.org/abs/2212.10560) — **Wang et al. (2022)**. *Seed tasks, generate, filter, feed back. Everything since is a variation.*
3. **See it made harder on purpose** — read [WizardLM / Evol-Instruct](https://arxiv.org/abs/2304.12244) — **Xu et al. (2023)**. *In-depth and in-breadth evolution turns easy instructions into hard ones automatically.*
4. **See the "small model, great data" thesis** — read [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644) — **Gunasekar et al. (2023)** and [SmolLM2](https://arxiv.org/abs/2502.02737) — **Ben Allal et al. (2025)**. *Phi's synthetic-textbook argument, then the fully open, data-centric replication.*
5. **Learn to distrust your own numbers** — read [A Careful Examination of LLM Performance on Grade School Arithmetic](https://arxiv.org/abs/2405.00332) — **Zhang et al. (2024)**. *A fresh GSM1k reveals which models were memorising; this is the contamination check you should copy.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the two Data lectures are the most rigorous free treatment of filtering, deduplication and mixture design; slides and assignments are on the course site.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free, code-first; the dataset chapters give you `datasets` fluency before you attempt a pipeline.
- [Cosmopedia](https://huggingface.co/blog/cosmopedia) — **Hugging Face** — a fully documented 25-billion-token synthetic corpus: prompt design, topic clustering, dedup, and the failure cases they hit.

## Videos

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the pretraining-data and post-training-data sections show, concretely, what a token in a training set actually is and where it came from.
- [Stanford CS336 — Lecture 1: Overview and Tokenization](https://www.youtube.com/watch?v=SQ3fZ1sAqXI) — **Stanford Online** — starts the series whose Data lectures cover Common Crawl processing end to end.

## Key Papers

- [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) — **Penedo et al. (2024)** — ablation-driven curation, and the FineWeb-Edu classifier that made "quality filtering" measurable.
- [FineWeb2: One Pipeline to Scale Them All](https://arxiv.org/abs/2506.20920) — **Penedo et al. (2025)** — the same pipeline adapted automatically to every language; the multilingual reference.
- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) — **Wang et al. (2022)** — bootstrapping instruction data from a handful of seeds.
- [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://arxiv.org/abs/2304.12244) — **Xu et al. (2023)** — Evol-Instruct: evolve prompts toward difficulty and breadth.
- [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644) — **Gunasekar et al. (2023)** — the phi recipe: textbook-quality synthetic data beats far more web tokens.
- [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704) — **NVIDIA (2024)** — a model family released explicitly as a *synthetic-data generator*, with the alignment data pipeline documented.
- [Rephrasing the Web](https://arxiv.org/abs/2401.16380) — **Maini et al. (2024)** — rewriting existing web text in a cleaner style is cheaper than generating from scratch and trains faster.
- [SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model](https://arxiv.org/abs/2502.02737) — **Ben Allal et al. (2025)** — the open, reproducible answer to phi: every dataset released.

## Articles / Blogs (free, no paywall)

- [FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face** — the interactive blog post; read the ablation plots, they teach the method better than the paper.
- [Cosmopedia: how to create large-scale synthetic data for pre-training](https://huggingface.co/blog/cosmopedia) — **Hugging Face** — the honest write-up of prompt diversity, contamination and dedup at 25-billion-token scale.
- [SmolLM3](https://huggingface.co/blog/smollm3) — **Hugging Face** — a full open recipe for a small model, with the data mixture and staged curriculum spelled out.
- [Tülu 3: The next era in open post-training](https://allenai.org/blog/tulu-3) — **Allen Institute for AI** — how a modern post-training data mix is assembled, decontaminated and released.

## Books (free, with chapters)

- [*Speech and Language Processing* (3rd ed.) — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky & Martin** — free PDF; the pretraining-data section: sources, filtering, and what the corpus decides.
- [*A Survey of Large Language Models*](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — free; §4 is a citation-rich map of data collection, quality filtering and deduplication.

## In this platform

- Where the curated data is consumed: [Pretraining](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) · [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) · [Instruction Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/instruction-tuning/instruction-tuning)
- Generating data *from* a stronger model: [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation)
- The reasoning traces that become cold-start data: [Reinforcement Learning for Reasoning](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining)
- Why data budget beats parameter budget: [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws)
- Contamination is an evaluation problem too: [LLM Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks)
- Small models are the main beneficiary: [Small and On-Device Language Models](/ai-ml/ai-ml-learning-resources/inference-and-serving/small-and-on-device-language-models/small-and-on-device-language-models)
