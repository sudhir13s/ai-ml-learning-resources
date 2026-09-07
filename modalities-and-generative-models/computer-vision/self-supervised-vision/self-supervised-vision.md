---
id: "07-computer-vision/self-supervised-vision"
topic: "Self-Supervised Vision (SimCLR, MAE, DINO)"
parent: "07-computer-vision"
level: advanced
built_from: ["cnns", "vision-transformers", "data-augmentation", "contrastive-learning"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Self-Supervised Vision (SimCLR, MAE, DINO)"
minutes: 10
category: computer-vision
---

# Self-Supervised Vision — SimCLR · MAE · DINO
> Learn strong visual representations from **unlabeled** images by inventing a pretext task. Three
> families dominate: **contrastive** (SimCLR pulls two augmented views of the same image together,
> pushes others apart via InfoNCE), **masked image modeling** (MAE masks ~75% of patches and
> reconstructs them with a ViT), and **self-distillation** (DINO matches student/teacher outputs,
> yielding emergent segmentation). The pretrained features then transfer with few or no labels.

**Why it matters:** the modern representation-learning question — why self-supervision matters when
labels are expensive, how contrastive learning's positive/negative pairs and InfoNCE work, the role of
augmentation in defining "views," why MAE's high masking ratio works, and how DINO produces
object-segmentation attention for free. Central to foundation-model and multimodal interviews.

**⭐ Start here — suggested path:**

1. **Build intuition (contrastive)** — watch ⭐ [Contrastive Learning — SimCLR illustrated](https://www.youtube.com/watch?v=YZgeWsuyRH8) (AI Bites). *Positive/negative pairs, augmentation views, and the contrastive loss.*
2. **Go a bit deeper** — watch [Can Contrastive Learning Work? — SimCLR Explained](https://www.youtube.com/watch?v=7Id8SPH31UE). *Why big batches, projection heads, and strong augmentation matter.*
3. **Masked image modeling** — watch [Masked Autoencoders (MAE) Paper Explained](https://www.youtube.com/watch?v=-EBqzYIJRaQ), then read the ⭐ [MAE paper](https://arxiv.org/abs/2111.06377). *Mask 75% of patches, reconstruct with an asymmetric ViT encoder/decoder.*
4. **Read the sources** — [SimCLR](https://arxiv.org/abs/2002.05709) → [BYOL](https://arxiv.org/abs/2006.07733) (no negatives) → [DINO](https://arxiv.org/abs/2104.14294) (self-distillation). *The three paradigms and their key tricks.*
5. **See it work** — read the [DINO reference implementation and results](https://github.com/facebookresearch/dino) — **Meta AI (FAIR)**. *Emergent segmentation maps from purely self-supervised ViTs, with the attention visualizations.*
6. **See where this went in 2025–26** — read [DINOv2](https://arxiv.org/abs/2304.07193) → [DINOv3](https://arxiv.org/abs/2508.10104). *Self-supervision stopped being a pretraining trick and became the way general-purpose frozen vision backbones are built.*

## Courses (free)
- [Stanford CS231n](https://cs231n.github.io/) — **Stanford** — recent editions cover self-supervised and contrastive representation learning.
- [CS224W / d2l contrastive-learning material](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang et al.** — the augmentation + representation foundations self-supervision builds on, free.

## Videos
- [Contrastive Learning — SimCLR (illustrated)](https://www.youtube.com/watch?v=YZgeWsuyRH8) — **AI Bites** — positive/negative pairs and the contrastive objective, visualized.
- [Can Contrastive Learning Work? — SimCLR Explained](https://www.youtube.com/watch?v=7Id8SPH31UE) — **Boris Meinardus** — why batch size, projection head, and augmentation matter.
- [Masked Autoencoders (MAE) Paper Explained](https://www.youtube.com/watch?v=-EBqzYIJRaQ) — **Soroush Mehraban** — the asymmetric encoder/decoder and high masking ratio.
- [Self-supervised learning in computer vision (NYU Deep Learning 10L)](https://www.youtube.com/watch?v=8L10w1KoOU8) — **Alfredo Canziani (NYU)** — contrastive, distillation, and reconstruction methods placed in one framework rather than listed.
- [Non-contrastive joint embedding methods for SSL (NYU Deep Learning 10P)](https://www.youtube.com/watch?v=EBrbaD2zyuo) — **Alfredo Canziani (NYU)** — why BYOL/DINO avoid collapse without negatives, which is the question interviewers actually ask.

## Key Papers
- [A Simple Framework for Contrastive Learning (SimCLR)](https://arxiv.org/abs/2002.05709) — **Chen et al. (2020)** — augmentation views + InfoNCE + projection head; the contrastive benchmark.
- [Bootstrap Your Own Latent (BYOL)](https://arxiv.org/abs/2006.07733) — **Grill et al. (2020)** — strong self-supervised features without negative pairs.
- [Masked Autoencoders Are Scalable Vision Learners (MAE)](https://arxiv.org/abs/2111.06377) — **He et al. (2021)** — mask 75% of patches, reconstruct; scalable ViT pretraining.
- [Emerging Properties in Self-Supervised ViTs (DINO)](https://arxiv.org/abs/2104.14294) — **Caron et al. (2021)** — self-distillation; emergent segmentation attention.
- [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193) — **Oquab et al. (2023)** — curated data plus scale turn self-supervision into a general frozen backbone.
- [DINOv3](https://arxiv.org/abs/2508.10104) — **Siméoni et al. (2025)** — the 2025 backbone: dense features strong enough that segmentation and depth heads train on frozen weights.
- [ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808) — **Woo et al. (2023)** — masked pretraining ported back to convnets; proof the recipe is not ViT-specific.

## Articles / Blogs (free, no paywall)
- [DINO — reference implementation](https://github.com/facebookresearch/dino) — **Meta AI (FAIR)** — the code, pretrained weights, and the attention-map visualizations that made emergent segmentation famous.
- [The Illustrated SimCLR Framework](https://amitness.com/posts/simclr) — **Amit Chaudhary** — a clear, fully open visual explanation of SimCLR.
- [Lil'Log — Self-Supervised Representation Learning](https://lilianweng.github.io/posts/2019-11-10-self-supervised/) — **Lilian Weng** — the definitive open survey of pretext tasks and contrastive methods.

## Books (free, with chapters)
- [Dive into Deep Learning — **Ch. 14.8 (Region-based / representation pretraining)** + **Ch. 16 (NLP pretraining, contrastive analog)**](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang et al.** — the augmentation/pretraining machinery, with code.
- [Computer Vision: Algorithms and Applications, 2nd ed. — **Ch. 5.4 (Self-supervised & contrastive pretraining)**](https://szeliski.org/Book/) — **Richard Szeliski** — self-supervision in context, free.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 1.13 Contrastive Learning (SimCLR · InfoNCE)](/ai-ml/ai-ml-intuitions/representation/representation-learning/contrastive-learning-intuition) · [1.14 Triplet Loss](/ai-ml/ai-ml-intuitions/representation/representation-learning/triplet-learning-intuition)
- Foundation: [Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers) (MAE/DINO backbone) · [Data Augmentation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/data-augmentation/data-augmentation) (defines contrastive views)
- Related domain: [Deep Learning › Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/autoencoders/autoencoders) (MAE is a masked autoencoder)
