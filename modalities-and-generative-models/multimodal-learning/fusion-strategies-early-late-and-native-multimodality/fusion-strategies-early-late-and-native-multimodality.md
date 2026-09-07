---
id: "modalities-and-generative-models/multimodal-learning/fusion-strategies-early-late-and-native-multimodality"
topic: "Fusion Strategies — Early, Late and Native Multimodality"
level: advanced
built_from: ["interleaved-and-few-shot-vlms-flamingo", "visual-instruction-tuning-llava"]
leads_to: ["unified-token-spaces-and-any-to-any-models", "modern-open-vlm-architectures"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 13
title: "Fusion Strategies — Early, Late and Native Multimodality"
minutes: 13
category: multimodal-learning
---

# Fusion Strategies — Early, Late and Native Multimodality
> Every multimodal model answers one question: **where do the modalities meet?** *Late fusion*
> keeps two towers and compares embeddings at the end (Contrastive Language-Image Pretraining,
> CLIP). *Adapter fusion* bolts a pretrained vision encoder onto a pretrained language model
> through a projector or cross-attention (LLaVA, Flamingo). *Early / native fusion* puts both
> modalities into one token stream and trains one transformer from scratch on all of it
> (Chameleon). Later fusion is cheaper and safer; earlier fusion has the higher ceiling.

**Why it matters:** "how would you combine modalities?" is the design question behind every
multimodal system, and the answer determines cost, data needs, and what the model can never do.

- **The 2025 evidence:** Apple's scaling study found early-fusion native models are *not* worse
  than late-fusion ones at equal compute — and are cheaper to serve — which is why frontier
  models moved that way.
- **What interviewers probe:** why adapter fusion dominates open models (you reuse two
  expensive pretrained artifacts), and why it caps grounding (the language model never learned
  to see, it learned to read a translation).
- **The failure mode people get wrong:** *modality collapse* — with a frozen language model and
  weak visual supervision, the model answers from language priors and barely looks at the image.
  Object-hallucination benchmarks exist precisely to catch this.

**Start here — suggested path:**

1. **Learn the two mainstream designs** — read [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) — **Sebastian Raschka**. *Decoder-only projection vs cross-attention, drawn clearly and then traced through ten real models.*
2. **Get the systems view** — read [Multimodality and Large Multimodal Models](https://huyenchip.com/2023/10/10/multimodal.html) — **Chip Huyen**. *Fusion as an engineering decision: data, training cost, and what each choice commits you to.*
3. **Compare the connectors** — read [BLIP-2](https://arxiv.org/abs/2301.12597) — **Li et al. (2023)** — against [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) — **Liu et al. (2023)**. *Querying Transformer vs a plain projector: same job, different inductive bias and training cost.*
4. **See the native-fusion argument** — read [Scaling Laws for Native Multimodal Models](https://arxiv.org/abs/2504.07951) — **Shukor et al. (2025)**. *Controlled scaling experiments comparing early and late fusion — the numbers behind the 2025–26 shift.*
5. **Watch the whole map in one lecture** — watch [Stanford CS25 V4: From Large Language Models to Large Multimodal Models](https://www.youtube.com/watch?v=cYfKQ6YG9Qo) — **Stanford Online**. *Fusion choices lined up with the models that made them.*

## Courses (free)

- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/pre-intro) — **Hugging Face** — free unit that contrasts fusion styles with runnable examples.
- [Stanford CS231n — Lecture 16, "Vision and Language" (slides)](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf) — **Stanford (Spring 2025)** — the academic framing of fusion, from joint embeddings to token-level fusion.

## Videos

- [Stanford CS25 V4: From Large Language Models to Large Multimodal Models](https://www.youtube.com/watch?v=cYfKQ6YG9Qo) — **Stanford Online** — the design space of connecting vision to a language model, with the trade-offs stated.

## Key Papers

- [Scaling Laws for Native Multimodal Models](https://arxiv.org/abs/2504.07951) — **Shukor et al. (2025)** — the controlled early-vs-late fusion comparison at matched compute; the paper to cite in this argument.
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) — **Alayrac et al. (2022)** — gated cross-attention fusion into a frozen language model.
- [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) — **Li et al. (2023)** — the Q-Former: a learned query bottleneck between the frozen towers.
- [Visual Instruction Tuning (LLaVA)](https://arxiv.org/abs/2304.08485) — **Liu et al. (2023)** — the simplest connector that works: one projection into the token space.
- [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818) — **Chameleon Team, Meta (2024)** — one transformer, one token vocabulary, both modalities from step one, plus the stability tricks it needed.

## Articles / Blogs (free, no paywall)

- [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) — **Sebastian Raschka** — the reference explainer for the two dominant fusion designs.
- [Multimodality and Large Multimodal Models](https://huyenchip.com/2023/10/10/multimodal.html) — **Chip Huyen** — systems-level survey; strong on why training data, not architecture, usually decides.
- [Generalized Visual Language Models](https://lilianweng.github.io/posts/2022-06-09-vlm/) — **Lilian Weng** — a taxonomy of ways to attach vision to a language model, with the frozen-model line traced.
- [A Dive into Vision-Language Models](https://huggingface.co/blog/vision_language_pretraining) — **Hugging Face** — pretraining objectives per fusion style, with code.

## In this platform

- Concept depth (the *why*): [Multimodal LLMs (intuition)](/ai-ml/ai-ml-intuitions/multimodal-integration/modality-fusion/multimodal-llms-intuition)
- Prerequisites: [Interleaved and Few-Shot VLMs (Flamingo)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/interleaved-and-few-shot-vlms-flamingo/interleaved-and-few-shot-vlms-flamingo) · [Visual Instruction Tuning (LLaVA)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/visual-instruction-tuning-llava/visual-instruction-tuning-llava)
- Next: [Unified Token Spaces and Any-to-Any Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/unified-token-spaces-and-any-to-any-models/unified-token-spaces-and-any-to-any-models) · [Modern Open VLM Architectures](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-open-vlm-architectures/modern-open-vlm-architectures)
- Related: [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) · [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding) — modality collapse is a grounding failure
