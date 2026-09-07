---
id: "modalities-and-generative-models/multimodal-learning/interleaved-and-few-shot-vlms-flamingo"
topic: "Interleaved and Few-Shot VLMs — the Flamingo Lineage"
level: advanced
built_from: ["clip-and-contrastive-vision-language-pretraining"]
leads_to: ["visual-instruction-tuning-llava", "fusion-strategies-early-late-and-native-multimodality"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 13
title: "Interleaved and Few-Shot VLMs — the Flamingo Lineage"
minutes: 13
category: multimodal-learning
---

# Interleaved and Few-Shot VLMs — the Flamingo Lineage
> Flamingo was the first model to make a frozen language model *see* well enough to learn a new
> visual task from a handful of examples in the prompt. Two ideas carry it: a **Perceiver
> Resampler** that squeezes a variable number of image features into a fixed set of visual
> tokens, and **gated cross-attention layers** inserted between the frozen language model's
> blocks — initialized at zero so the model starts exactly as good as the text-only model it
> began from.

**Why it matters:** this is where multimodal *in-context learning* came from, and the
cross-attention branch of the design space that the field still weighs against plain projection.

- **Where it is used today (2026):** the cross-attention pattern survives wherever visual tokens
  must stay cheap — long video, many-image prompts, and Llama 3.2 Vision's adapter design.
- **What interviewers probe:** why the gating is *tanh-gated and zero-initialized* (so adding
  vision cannot destroy the language model on step one), and why interleaved image-text
  documents — not caption pairs — are what create few-shot ability.
- **The trade-off people get wrong:** freezing the language model preserves text quality and
  saves compute, but caps visual grounding; every later open model that wanted stronger
  perception unfroze it.

**Start here — suggested path:**

1. **Get the shape of the model** — read [Tackling multiple tasks with a single visual language model](https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/) — **DeepMind**. *The authors' own diagram of frozen towers plus gated cross-attention, before the paper's detail.*
2. **Read the primary source** — read [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) — **Alayrac et al. (2022)**. *Section 3 defines the Perceiver Resampler and the gated cross-attention; the ablations in Section 4 are the real lesson.*
3. **See why the data mattered** — read [OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents](https://arxiv.org/abs/2306.16527) — **Laurençon et al. (2023)**. *Flamingo's secret ingredient, rebuilt in the open: web pages with images in place, not caption pairs.*
4. **Watch the lineage in one talk** — watch [Large Multimodal Models (CVPR 2024 tutorial)](https://www.youtube.com/watch?v=S0CpenMvG48) — **Chunyuan Li (LLaVA co-author)**. *Places Flamingo, BLIP-2 and LLaVA on one timeline and explains what each fixed.*
5. **Run an open replica** — use [OpenFlamingo](https://arxiv.org/abs/2308.01390) — **Awadalla et al. (2023)** — or the [IDEFICS models](https://huggingface.co/blog/idefics) — **Hugging Face**. *Open weights with the same architecture, so the few-shot behaviour is reproducible on your own prompts.*

## Courses (free)

- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro) — **Hugging Face** — free walkthrough of VLM architectures including cross-attention fusion.
- [Stanford CS231n — Lecture 16, "Vision and Language" (slides)](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf) — **Stanford (Spring 2025)** — the university framing of image-conditioned language models.

## Videos

- [Large Multimodal Models (CVPR 2024 Vision Foundation Model tutorial)](https://www.youtube.com/watch?v=S0CpenMvG48) — **Chunyuan Li** — a researcher's tour from Flamingo-style cross-attention to instruction-tuned VLMs.

## Key Papers

- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) — **Alayrac et al. (2022)** — the blueprint: frozen vision encoder, Perceiver Resampler, gated cross-attention into a frozen language model, trained on interleaved web documents.
- [OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents](https://arxiv.org/abs/2306.16527) — **Laurençon et al. (2023)** — 141M open interleaved documents; the dataset that made Flamingo reproducible.
- [OpenFlamingo: An Open-Source Framework for Training Large Autoregressive Vision-Language Models](https://arxiv.org/abs/2308.01390) — **Awadalla et al. (2023)** — the open reimplementation, with the gap to the closed model measured honestly.
- [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) — **Li et al. (2023)** — the Querying Transformer (Q-Former): the other way to compress vision into a frozen language model's input.
- [MIMIC-IT: Multi-Modal In-Context Instruction Tuning](https://arxiv.org/abs/2306.05425) — **Li et al. (2023)** — turns interleaved data into in-context instruction data; the bridge from Flamingo's few-shot ability to instruction following.

## Articles / Blogs (free, no paywall)

- [Tackling multiple tasks with a single visual language model](https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/) — **DeepMind** — the authors' own explanation of Flamingo, with the few-shot examples that made the case.
- [Introducing IDEFICS: An Open Reproduction of State-of-the-Art Visual Language Model](https://huggingface.co/blog/idefics) — **Hugging Face** — an open Flamingo-class model, with the training data and evaluation published.
- [IDEFICS 2](https://huggingface.co/blog/idefics2) — **Hugging Face** — the follow-up that moves from cross-attention to a projection-based design; read the two posts back to back for the argument.
- [Generalized Visual Language Models](https://lilianweng.github.io/posts/2022-06-09-vlm/) — **Lilian Weng** — puts frozen-language-model methods (Frozen, Flamingo, BLIP-2) in one taxonomy.

## In this platform

- Prerequisites: [CLIP and Contrastive Vision-Language Pretraining](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/clip-and-contrastive-vision-language-pretraining/clip-and-contrastive-vision-language-pretraining) · [Prompting and In-Context Learning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning)
- Next: [Visual Instruction Tuning (LLaVA)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/visual-instruction-tuning-llava/visual-instruction-tuning-llava) · [Fusion Strategies](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/fusion-strategies-early-late-and-native-multimodality/fusion-strategies-early-late-and-native-multimodality)
- Related: [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) — cross-attention is the fusion operator here
