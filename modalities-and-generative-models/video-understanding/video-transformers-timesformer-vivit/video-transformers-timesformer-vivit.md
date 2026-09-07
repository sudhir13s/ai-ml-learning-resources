---
id: "modalities-and-generative-models/video-understanding/video-transformers-timesformer-vivit"
topic: "Video Transformers — TimeSformer & ViViT"
level: advanced
built_from: ["video-representations-and-temporal-modeling", "vision-transformers"]
leads_to: ["modalities-and-generative-models/video-understanding/self-supervised-video-pretraining-videomae", "modalities-and-generative-models/video-understanding/efficient-video-inference"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Video Transformers — TimeSformer & ViViT"
minutes: 15
category: video-understanding
---

# Video Transformers — TimeSformer & ViViT
> Tokenize a video into space-time patches and attention can model any pair of positions across
> both space and time — but joint space-time attention costs **O((T·N)²)** for `T` frames of `N`
> patches, which is unaffordable past a few seconds.
> Every video transformer is therefore a **factorization**: split attention into a temporal pass
> and a spatial pass (TimeSformer's divided attention, ViViT's factorized encoder), or shrink
> resolution as depth grows (MViT), or restrict attention to local windows (Video Swin).

**Why it matters:** this is the question that separates "I read the ViT paper" from "I have built a
video model." Interviewers ask you to count tokens (16 frames of 14×14 patches is already 3,136
tokens — squared in attention), then name the factorization that buys the accuracy back, and to say
where each one breaks: divided attention loses some fine-grained motion coupling, window attention
needs shifting to communicate across windows, and pooling attention trades spatial detail for depth.

**Start here — suggested path:**

1. **Recall the image case** — read the platform's [Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers) page. *Video transformers are ViT plus a decision about the time axis — nothing else is new.*
2. **See the token blow-up** — read [CS231n 2025 Lecture 10: Video Understanding](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)**. *The slides that put 3D CNNs and space-time attention on the same axes.*
3. **Read the two canonical designs** — [TimeSformer](https://arxiv.org/abs/2102.05095) — **Bertasius et al. (2021)** and [ViViT](https://arxiv.org/abs/2103.15691) — **Arnab et al. (2021)**. *Divided space-time attention and the four factorization variants, with their ablations.*
4. **See the two efficiency families** — [Multiscale Vision Transformers](https://arxiv.org/abs/2104.11227) and [Video Swin Transformer](https://arxiv.org/abs/2106.13230). *Pooling attention versus local windows — the two ways to keep long clips tractable.*
5. **Run one** — load [TimeSformer in Transformers](https://huggingface.co/docs/transformers/en/model_doc/timesformer) or [ViViT](https://huggingface.co/docs/transformers/en/model_doc/vivit) and print the attention shapes per block. *Seeing `[B, heads, T, N, N]` versus `[B, heads, N, T, T]` is the whole idea of factorized attention.*

## Courses (free)
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — the transition from 3D convolution to space-time attention, taught rather than surveyed.
- [Community Computer Vision Course — Transformers in Video Processing](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/transformers-based-models) — **Hugging Face** — free walkthrough of tubelet embedding and the factorization variants, with code.
- [Stanford CS231n](https://cs231n.stanford.edu/) — **Stanford** — the assignments that make attention shapes second nature before you add a time axis.

## Videos
- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)** — establishes the 3D-CNN baseline these transformers replaced, and why cost is the deciding variable.
- [Is Space-Time Attention All You Need for Video Understanding? (ICML 2021 talk page)](https://icml.cc/virtual/2021/poster/8941) — **Gedas Bertasius et al.** — the TimeSformer authors presenting divided attention themselves.

## Key Papers
- [Is Space-Time Attention All You Need for Video Understanding? (TimeSformer)](https://arxiv.org/abs/2102.05095) — **Bertasius, Wang & Torresani (2021)** — divided space-time attention; the ablation table is the lesson.
- [ViViT: A Video Vision Transformer](https://arxiv.org/abs/2103.15691) — **Arnab et al. (2021)** — tubelet embedding plus four factorization models, compared cleanly.
- [Multiscale Vision Transformers (MViT)](https://arxiv.org/abs/2104.11227) — **Fan et al. (2021)** — pooling attention: resolution down, channels up, exactly like a CNN pyramid.
- [MViTv2](https://arxiv.org/abs/2112.01526) — **Li et al. (2021)** — decomposed relative position and residual pooling; the version people actually deploy.
- [Video Swin Transformer](https://arxiv.org/abs/2106.13230) — **Liu et al. (2021)** — 3D shifted windows; locality as an inductive bias for video.
- [UniFormer](https://arxiv.org/abs/2201.04676) — **Li et al. (2022)** — convolution in early layers, attention in late layers; the hybrid that explains why both work.

## Articles / Blogs (free, no paywall)
- [TimeSformer model documentation](https://huggingface.co/docs/transformers/en/model_doc/timesformer) — **Hugging Face** — the divided-attention implementation with a runnable inference snippet.
- [ViViT model documentation](https://huggingface.co/docs/transformers/en/model_doc/vivit) — **Hugging Face** — tubelet embedding in code, including the frame-sampling arguments.
- [torchvision Video Swin Transformer](https://pytorch.org/vision/main/models/video_swin_transformer.html) — **PyTorch** — pretrained Kinetics checkpoints with documented input shapes.
- [PyTorchVideo](https://pytorchvideo.org/) — **Meta AI** — MViT and SlowFast in one library, so architecture comparisons run on the same data pipeline.

## Books (free, with chapters)
- [*Understanding Deep Learning* — Ch. 12 "Transformers"](https://udlbook.github.io/udlbook/) — **Simon Prince** — the attention cost model these factorizations attack, derived symbol by symbol.
- [*Foundations of Computer Vision* — Part VII "Neural Architectures"](https://visionbook.mit.edu) — **Torralba, Isola & Freeman** — convolution and transformers side by side, free online.

## In this platform
- Prerequisites: [Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers) · [Video Representations & Temporal Modeling](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-representations-and-temporal-modeling/video-representations-and-temporal-modeling)
- Related mechanism: [Efficient Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention) (the same quadratic problem, in text)
- Next: [Self-Supervised Video Pretraining](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/self-supervised-video-pretraining-videomae/self-supervised-video-pretraining-videomae) (how these backbones are actually trained) · [Efficient Video Inference](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/efficient-video-inference/efficient-video-inference)
