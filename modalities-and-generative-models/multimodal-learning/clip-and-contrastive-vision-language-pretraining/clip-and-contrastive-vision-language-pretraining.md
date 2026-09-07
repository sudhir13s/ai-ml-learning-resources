---
id: "modalities-and-generative-models/multimodal-learning/clip-and-contrastive-vision-language-pretraining"
topic: "CLIP and Contrastive Vision-Language Pretraining"
level: intermediate
built_from: ["vision-transformers", "contrastive-self-supervised-learning", "contextual-embeddings-elmo-bert"]
leads_to: ["modern-dual-encoders-siglip-and-retrieval", "interleaved-and-few-shot-vlms-flamingo", "multimodal-rag"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 14
title: "CLIP and Contrastive Vision-Language Pretraining"
minutes: 14
category: multimodal-learning
---

# CLIP and Contrastive Vision-Language Pretraining
> Contrastive Language-Image Pretraining (CLIP) trains an image encoder and a text encoder
> *jointly* so that a photo and its caption land at the same place in one shared embedding
> space. The supervision is free — 400 million (image, alt-text) pairs off the web — and the
> payoff is **zero-shot classification**: name the classes in English, embed the names, pick
> the nearest. One sentence: *CLIP replaced the fixed label set with language itself.*

**Why it matters:** almost every vision-language model (VLM) shipping in 2026 still starts
from a contrastively-pretrained image encoder — Large Language and Vision Assistant (LLaVA),
PaliGemma, Qwen-VL, InternVL all bolt a language model onto a CLIP-family tower.

- **What interviewers probe:** why the loss is a symmetric InfoNCE over an in-batch similarity
  matrix, why the temperature is learned, and why batch size *is* the negative count.
- **The trade-off people get wrong:** CLIP is a *retrieval* model, not a *reasoning* model. It
  scores whole-image ↔ whole-caption similarity, so it is famously weak at counting,
  compositional word order ("dog chasing cat" vs "cat chasing dog"), and text rendered in the
  image — a bag-of-concepts matcher, not a grounded parser.

**Start here — suggested path:**

1. **Get the picture before the loss** — read [CLIP: Connecting text and images](https://openai.com/index/clip/) — **OpenAI**. *The original announcement, with the zero-shot framing and the failure cases stated honestly by the authors.*
2. **Watch the mechanism** — watch [OpenAI CLIP: Connecting Text and Images (Paper Explained)](https://www.youtube.com/watch?v=T9XSU0pKX2E) — **Yannic Kilcher**. *The batch similarity matrix, the symmetric cross-entropy, and the prompt-engineering trick, walked through the paper.*
3. **Read the primary source** — read [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) — **Radford et al. (2021)**. *Section 2 is the whole method in one page of pseudocode; Section 3 is the zero-shot evaluation that made it famous.*
4. **See what the neurons learned** — read [Multimodal Neurons in Artificial Neural Networks](https://distill.pub/2021/multimodal-neurons/) — **Goh et al., Distill (2021)**. *Interpretability evidence that CLIP learns concept-level, modality-agnostic features — and the typographic attack that breaks them.*
5. **Reproduce it at small scale** — use [OpenCLIP](https://github.com/mlfoundations/open_clip) — **LAION / ML Foundations**. *Open weights and open training code; swap the data and watch the scaling laws from Cherti et al. reproduce.*

## Courses (free)

- [Hugging Face Community Computer Vision Course — CLIP and relatives](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/clip-and-relatives/clip) — **Hugging Face** — free and code-first: builds the contrastive objective, then runs zero-shot classification in a notebook.
- [Stanford CS231n — Lecture 16, "Vision and Language" (slides)](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf) — **Stanford (Spring 2025)** — the current university treatment: CLIP through to instruction-tuned VLMs in one deck.
- [Stanford CS231n — Deep Learning for Computer Vision](https://cs231n.stanford.edu/) — **Stanford** — the surrounding course; assignments and notes are free even though the lecture videos are not.

## Videos

- [OpenAI CLIP: Connecting Text and Images (Paper Explained)](https://www.youtube.com/watch?v=T9XSU0pKX2E) — **Yannic Kilcher** — a careful read of the paper: the loss, the prompt ensembling, and the limits.
- [Stanford CS25 V4: From Large Language Models to Large Multimodal Models](https://www.youtube.com/watch?v=cYfKQ6YG9Qo) — **Stanford Online** — where contrastive pretraining sits in the road from CLIP to modern multimodal systems.

## Key Papers

- [Learning Transferable Visual Models From Natural Language Supervision (CLIP)](https://arxiv.org/abs/2103.00020) — **Radford et al. (2021)** — the paper; the symmetric InfoNCE objective, learned temperature, and zero-shot transfer to 30+ datasets.
- [Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision (ALIGN)](https://arxiv.org/abs/2102.05918) — **Jia et al. (2021)** — the concurrent Google result: 1.8B *noisy* pairs beat carefully curated data; scale substitutes for cleaning.
- [LiT: Zero-Shot Transfer with Locked-image text Tuning](https://arxiv.org/abs/2111.07991) — **Zhai et al. (2022)** — freeze a strong image tower and train only the text tower; the cheapest way to get a CLIP-style space, and the ancestor of modern projector training.
- [Reproducible scaling laws for contrastive language-image learning](https://arxiv.org/abs/2212.07143) — **Cherti et al. (2023)** — OpenCLIP's open replication: how zero-shot accuracy scales with compute, data, and model size.
- [DataComp: In search of the next generation of multimodal datasets](https://arxiv.org/abs/2304.14108) — **Gadre et al. (2023)** — fixes the training code and competes on *data filtering*; the paper that made "the dataset is the model" concrete.
- [Demystifying CLIP Data (MetaCLIP)](https://arxiv.org/abs/2309.16671) — **Xu et al. (2024)** — reverse-engineers OpenAI's undisclosed curation recipe and releases it; read with DataComp.

## Articles / Blogs (free, no paywall)

- [Generalized Visual Language Models](https://lilianweng.github.io/posts/2022-06-09-vlm/) — **Lilian Weng** — the canonical map of how vision meets language models, with CLIP as the root of the tree.
- [Contrastive Representation Learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/) — **Lilian Weng** — the loss-function lineage (InfoNCE, NT-Xent, temperature) that CLIP inherits.
- [Multimodal Neurons in Artificial Neural Networks](https://distill.pub/2021/multimodal-neurons/) — **Goh et al., Distill (2021)** — what a CLIP neuron actually responds to, and the typographic attack that fools it.
- [A Dive into Vision-Language Models](https://huggingface.co/blog/vision_language_pretraining) — **Hugging Face** — pretraining objectives compared (contrastive, matching, masked) with runnable code.
- [OpenCLIP](https://github.com/mlfoundations/open_clip) — **LAION / ML Foundations** — the reference open implementation; the model card table doubles as a scaling-law cheat sheet.

## Books (free, with chapters)

- [*Understanding Deep Learning* — Ch. 12 "Transformers"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the encoder background CLIP's two towers assume.

## In this platform

- Concept depth (the *why*): [Multimodal LLMs (intuition)](/ai-ml/ai-ml-intuitions/multimodal-integration/modality-fusion/multimodal-llms-intuition)
- Prerequisites: [Contrastive / Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning) (the InfoNCE loss CLIP reuses) · [Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers) (the image tower) · [Contextual Embeddings (ELMo, BERT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/contextual-embeddings-elmo-bert/contextual-embeddings-elmo-bert) (the text tower)
- Next: [Modern Dual Encoders (SigLIP and retrieval)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-dual-encoders-siglip-and-retrieval/modern-dual-encoders-siglip-and-retrieval) · [Interleaved and Few-Shot VLMs (Flamingo)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/interleaved-and-few-shot-vlms-flamingo/interleaved-and-few-shot-vlms-flamingo)
- Downstream use: [Multimodal RAG](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/multimodal-rag/multimodal-rag) · [Embedding Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models)
