---
id: "07-computer-vision/vision-transformers"
topic: "Vision Transformers (ViT)"
parent: "07-computer-vision"
level: advanced
built_from: ["transformers", "attention", "image-classification"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Vision Transformers (ViT)"
minutes: 10
category: computer-vision
---

# Vision Transformers (ViT)
> ViT applies the NLP transformer directly to images: split the image into fixed-size **patches**
> (e.g. 16×16), linearly embed each patch into a token, add positional encodings, prepend a `[CLS]`
> token, and run a standard transformer encoder. With enough data it matches or beats CNNs — trading
> the convolutional locality prior for global self-attention and scale.

**Why it matters:** the defining modern-vision question — how an image becomes a sequence of patch
tokens, why ViT needs large-scale pretraining (it lacks the CNN's built-in locality/translation
priors), how it compares to CNNs on data efficiency, and what hybrids (Swin, hierarchical windows)
add back. Expected for any role touching modern vision or multimodal models.

**⭐ Start here — suggested path:**

1. **Build intuition** — watch ⭐ [Lecture 13: Attention (EECS 498)](https://www.youtube.com/watch?v=YAgjfMR9R_M) — **Michigan Online (Justin Johnson)**. *Self-attention as a general layer, then images as sequences — the setup ViT needs.*
2. **Hear the original read** — watch [An Image is Worth 16×16 Words (Paper Explained)](https://www.youtube.com/watch?v=TrdevFK_am4) — **Yannic Kilcher**. *Patch embedding, `[CLS]` token, positional encodings, and why scale matters.*
3. **Get the transformer half cold** — watch [Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc) — **3Blue1Brown**. *The attention geometry ViT inherits unchanged from NLP.*
4. **Read the source** — the ⭐ [ViT paper](https://arxiv.org/abs/2010.11929), then [Swin Transformer](https://arxiv.org/abs/2103.14030). *The pure transformer, then the hierarchical/windowed hybrid.*
5. **Make it concrete** — work through [d2l: Vision Transformer](https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html). *Implement patch embedding + encoder and classify.*
6. **See the 2026 view** — read [DINOv3](https://arxiv.org/abs/2508.10104) — **Siméoni et al. (2025)**. *Where the ViT backbone actually lives today: self-supervised, frozen, and reused across dense tasks.*

## Courses (free)
- [Dive into Deep Learning — Vision Transformer](https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html) — **Zhang et al.** — free chapter implementing ViT from scratch with code.
- [Stanford CS231n](https://cs231n.github.io/) — **Stanford** — recent editions include a Vision Transformer lecture in the schedule.

## Videos
- [An Image is Worth 16×16 Words (Paper Explained)](https://www.youtube.com/watch?v=TrdevFK_am4) — **Yannic Kilcher** — a critical read of the original paper and why scale matters.
- [Lecture 13: Attention (EECS 498)](https://www.youtube.com/watch?v=YAgjfMR9R_M) — **Michigan Online (Justin Johnson)** — self-attention derived as a vision layer, the lecture ViT sits on top of.
- [Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc) — **3Blue1Brown** — the clearest geometric account of the attention block inside every ViT.
- [Lecture 12 | Visualizing and Understanding (CS231n)](https://www.youtube.com/watch?v=6wcs6szJWMY) — **Stanford University School of Engineering** — what backbone features actually encode, the question attention maps are asked to answer.

## Key Papers
- [An Image is Worth 16×16 Words (ViT)](https://arxiv.org/abs/2010.11929) — **Dosovitskiy et al. (2020)** — the pure-transformer image classifier; the landmark.
- [Swin Transformer](https://arxiv.org/abs/2103.14030) — **Liu et al. (2021)** — hierarchical, windowed attention; a strong general-purpose vision backbone.
- [Sigmoid Loss for Language Image Pre-Training (SigLIP)](https://arxiv.org/abs/2303.15343) — **Zhai et al. (2023)** — the pairwise-sigmoid objective that made ViT image towers cheap to train and is the default encoder in 2025–26 vision-language models (VLMs).
- [DINOv3](https://arxiv.org/abs/2508.10104) — **Siméoni et al. (2025)** — the current self-supervised ViT backbone: one frozen model whose dense features beat task-specific training.

## Articles / Blogs (free, no paywall)
- [Vision Transformer (d2l)](https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html) — **Zhang et al.** — explanation plus runnable code, free.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — **Jay Alammar** — the attention/transformer foundation ViT reuses, free.
- [Hugging Face — Vision Transformer (ViT) docs](https://huggingface.co/docs/transformers/model_doc/vit) — **Hugging Face** — usage and pretrained ViT models, open.

## Books (free, with chapters)
- [Dive into Deep Learning — **Ch. 11.8 (Transformers for Vision)**](https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html) — **Zhang et al.** — ViT with runnable code.
- [Computer Vision: Algorithms and Applications, 2nd ed. — **Ch. 5.5 (Transformers in vision)**](https://szeliski.org/Book/) — **Richard Szeliski** — ViT in the architecture landscape, free.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 4.15 The Transformer Block](/ai-ml/ai-ml-intuitions/architectural-mechanisms/composition/transformer-block-intuition) · [4.08 Multi-Head Attention](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/multi-head-attention-intuition)
- Foundation: [Deep Learning › Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) · [Deep Learning › Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism)
- Next concepts: [Self-Supervised Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/self-supervised-vision/self-supervised-vision) (MAE/DINO build on ViT)
- Where the ViT goes multimodal: [CLIP and Contrastive Vision-Language Pretraining](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/clip-and-contrastive-vision-language-pretraining/clip-and-contrastive-vision-language-pretraining) — the ViT as the image tower of a vision-language model
