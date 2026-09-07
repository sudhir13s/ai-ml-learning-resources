---
id: "modalities-and-generative-models/multimodal-learning/modern-dual-encoders-siglip-and-retrieval"
topic: "Modern Dual Encoders — SigLIP and Retrieval"
level: intermediate
built_from: ["clip-and-contrastive-vision-language-pretraining"]
leads_to: ["modalities-and-generative-models/multimodal-learning/visual-instruction-tuning-llava", "modalities-and-generative-models/multimodal-learning/modern-open-vlm-architectures", "modalities-and-generative-models/multimodal-learning/multimodal-rag"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 13
title: "Modern Dual Encoders — SigLIP and Retrieval"
minutes: 13
category: multimodal-learning
---

# Modern Dual Encoders — SigLIP and Retrieval
> A *dual encoder* embeds images and text with two separate towers and compares them with a
> dot product — cheap enough to index millions of items. The 2023 upgrade was the loss:
> Sigmoid Loss for Language Image Pretraining (SigLIP) replaces Contrastive Language-Image
> Pretraining's (CLIP) batch-wide softmax with an independent **sigmoid on every pair**, so
> training no longer needs a global normalization over the batch. Same architecture, better
> small-batch behaviour, and — by 2026 — the default vision tower inside open VLMs.

**Why it matters:** the dual encoder is the workhorse of production multimodal systems: search,
deduplication, safety filtering, and the frozen image tower that vision-language models (VLMs)
are built on.

- **Where it shows up in 2026:** SigLIP / SigLIP 2 towers ship inside PaliGemma, Qwen-VL,
  InternVL, SmolVLM and most open VLMs; the encoder is chosen before the language model is.
- **What interviewers probe:** why softmax contrastive loss makes batch size a *hyperparameter
  of the objective*, how the sigmoid loss decouples it, and why a dual encoder (fast, no
  cross-attention) loses to a cross-encoder re-ranker on fine-grained matching.
- **The failure mode:** dual encoders compress a whole image into one vector, so anything
  requiring localization, counting or reading text is lost at indexing time — you cannot
  re-rank your way out of information the embedding never kept.

**Start here — suggested path:**

1. **Frame the design choice** — read [Generalized Visual Language Models](https://lilianweng.github.io/posts/2022-06-09-vlm/) — **Lilian Weng**. *Dual encoder vs fusion encoder, and what each buys you, before any specific model.*
2. **Read the one-idea paper** — read [Sigmoid Loss for Language Image Pre-Training](https://arxiv.org/abs/2303.15343) — **Zhai et al. (2023)**. *Four pages in you have the whole change: pairwise sigmoid instead of batch softmax, plus the batch-size ablation.*
3. **Hear it from the author** — watch [Vision in the Age of LLMs (ETH Zurich Robot Learning, 2026)](https://www.youtube.com/watch?v=0XB7fNS_ONg) — **Lucas Beyer**. *SigLIP's and PaliGemma's co-author on why the encoder still matters when a language model does the reasoning.*
4. **See the 2025 state** — read [SigLIP 2: Multilingual Vision-Language Encoders](https://arxiv.org/abs/2502.14786) — **Tschannen et al. (2025)**. *Adds captioning and self-distillation objectives, dense features, and multilingual data — the current default tower.*
5. **Build a search index** — follow the [Sentence Transformers image-search documentation](https://sbert.net/) — **UKP Lab / Hugging Face**. *Encode a folder of images, encode queries, and feel where a single-vector index stops working.*

## Courses (free)

- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/pre-intro) — **Hugging Face** — free unit that builds up from contrastive encoders to full VLMs, with notebooks.
- [Stanford CS231n — Lecture 16, "Vision and Language" (slides)](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf) — **Stanford (Spring 2025)** — places dual encoders in the wider vision-and-language map.

## Videos

- [Vision in the Age of LLMs (ETH Zurich Robot Learning, 2026)](https://www.youtube.com/watch?v=0XB7fNS_ONg) — **Lucas Beyer (guest lecture, Oier Mees' course)** — the researcher behind SigLIP and PaliGemma on what vision encoders are still for.

## Key Papers

- [Sigmoid Loss for Language Image Pre-Training (SigLIP)](https://arxiv.org/abs/2303.15343) — **Zhai et al. (2023)** — the pairwise sigmoid objective; memory-efficient, works at small batch sizes, and beats softmax CLIP at equal compute.
- [SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://arxiv.org/abs/2502.14786) — **Tschannen et al. (2025)** — adds captioning-based pretraining and self-distillation; the current open default.
- [EVA-CLIP: Improved Training Techniques for CLIP at Scale](https://arxiv.org/abs/2303.15389) — **Sun et al. (2023)** — initialization, optimizer and augmentation recipe that makes very large contrastive towers trainable.
- [LiT: Zero-Shot Transfer with Locked-image text Tuning](https://arxiv.org/abs/2111.07991) — **Zhai et al. (2022)** — locking the image tower and tuning only text; the cheap path to a new aligned space.
- [AltCLIP: Altering the Language Encoder in CLIP for Extended Language Capabilities](https://arxiv.org/abs/2211.06679) — **Chen et al. (2022)** — swap the text tower to go multilingual; the pattern most non-English retrieval stacks reuse.

## Articles / Blogs (free, no paywall)

- [SigLIP 2: A better multilingual vision language encoder](https://huggingface.co/blog/siglip2) — **Hugging Face** — what changed versus SigLIP, with loading and fine-tuning code.
- [big_vision](https://github.com/google-research/big_vision) — **Google Research** — the JAX codebase SigLIP, LiT and PaliGemma were trained in; the configs are the real documentation.
- [A Dive into Vision-Language Models](https://huggingface.co/blog/vision_language_pretraining) — **Hugging Face** — compares contrastive, matching and generative pretraining objectives side by side.
- [Sentence Transformers documentation](https://sbert.net/) — **UKP Lab / Hugging Face** — the practical library for image-text embedding search, including multi-vector and re-ranking recipes.

## In this platform

- Prerequisite: [CLIP and Contrastive Vision-Language Pretraining](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/clip-and-contrastive-vision-language-pretraining/clip-and-contrastive-vision-language-pretraining)
- The retrieval side: [Embedding Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models) · [Vector Search](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/vector-search/vector-search) · [Reranking](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/reranking/reranking)
- Next: [Visual Instruction Tuning (LLaVA)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/visual-instruction-tuning-llava/visual-instruction-tuning-llava) · [Modern Open VLM Architectures](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-open-vlm-architectures/modern-open-vlm-architectures) · [Multimodal RAG](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/multimodal-rag/multimodal-rag)
