---
id: "modalities-and-generative-models/video-understanding/self-supervised-video-pretraining-videomae"
topic: "Self-Supervised Video Pretraining — VideoMAE & V-JEPA"
level: advanced
built_from: ["video-transformers-timesformer-vivit", "contrastive-self-supervised-learning"]
leads_to: ["modalities-and-generative-models/video-understanding/action-recognition-and-video-classification", "modalities-and-generative-models/video-understanding/video-language-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Self-Supervised Video Pretraining — VideoMAE & V-JEPA"
minutes: 15
category: video-understanding
---

# Self-Supervised Video Pretraining — VideoMAE & V-JEPA
> Labelled video is scarce and expensive, but raw video is effectively infinite — so modern video
> backbones are pretrained by **hiding part of the video and predicting the hidden part**.
> **VideoMAE** masks ~90–95% of space-time tubes and reconstructs pixels; **V-JEPA** predicts the
> masked region's *representation* instead of its pixels, which sidesteps the fact that most pixel
> detail in a video is unpredictable noise.
> The pretrained encoder is then fine-tuned for classification, retrieval, or fed to a language model.

**Why it matters:** self-supervision is why a video model can be trained without a Kinetics-scale
labelled set, and the reconstruct-pixels versus predict-features split is the live research argument
of 2025–26 (V-JEPA 2 scales it to 1M+ hours and uses the learned model for robot planning).
Interviewers probe why video tolerates a far higher mask ratio than images (temporal redundancy —
an unmasked neighbouring frame would make the task trivial, hence *tube* masking), and why a
pixel-reconstruction loss can score well while learning appearance shortcuts rather than motion.

**Start here — suggested path:**

1. **Recall the image-level idea** — read the platform's [Contrastive Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning) page. *Video pretraining is the same objectives with a time axis and much more redundancy.*
2. **Read the masked-video recipe** — [VideoMAE](https://arxiv.org/abs/2203.12602) — **Tong et al. (2022)**. *Tube masking at 90–95%, and why the naive frame-level mask leaks the answer.*
3. **See it scale** — [VideoMAE V2](https://arxiv.org/abs/2303.16727) — **Wang et al. (2023)**. *Dual masking to make billion-parameter video pretraining affordable.*
4. **Get the competing view** — watch [V-JEPA explained](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher**, then read [Revisiting Feature Prediction (V-JEPA)](https://arxiv.org/abs/2404.08471) — **Bardes et al. (2024)**. *Predicting in latent space instead of pixel space, and what that buys on motion-heavy benchmarks.*
5. **See where it landed in 2025** — [V-JEPA 2](https://arxiv.org/abs/2506.09985) — **Assran et al. (2025)**, then load [the released checkpoint](https://huggingface.co/facebook/vjepa2-vitl-fpc64-256). *A video encoder used as a world model for zero-shot robot planning — the current frontier of this line.*

## Courses (free)
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — where self-supervised video pretraining sits relative to supervised backbones.
- [Community Computer Vision Course — Unit 7: Video Processing](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/introduction-to-video) — **Hugging Face** — the free unit that leads into masked video modeling with runnable code.

## Videos
- [V-JEPA: Revisiting Feature Prediction for Learning Visual Representations from Video (Explained)](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher** — a careful read of the paper including why latent prediction beats pixel reconstruction here.
- [Self-Supervised Learning, JEPA, World Models, and the future of AI](https://www.youtube.com/watch?v=yUmDRxV0krg) — **Yann LeCun (Harvard CMSA, 2025)** — the originator's argument for predicting representations, straight from the source.

## Key Papers
- [VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602) — **Tong et al. (2022)** — tube masking at extreme ratios; the recipe most video backbones still start from.
- [VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking](https://arxiv.org/abs/2303.16727) — **Wang et al. (2023)** — masks the decoder too, making billion-parameter video pretraining tractable.
- [Revisiting Feature Prediction for Learning Visual Representations from Video (V-JEPA)](https://arxiv.org/abs/2404.08471) — **Bardes et al. (2024)** — predict latent features, not pixels; strong gains on motion-sensitive benchmarks.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al. (2025)** — 1M+ hours of video, then zero-shot robot planning from the learned model.
- [InternVideo2: Scaling Foundation Models for Multimodal Video Understanding](https://arxiv.org/abs/2403.15377) — **Wang et al. (2024)** — combines masked modeling, cross-modal contrastive learning, and next-token prediction in one pretraining stack.

## Articles / Blogs (free, no paywall)
- [facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2) — **Meta FAIR** — the official V-JEPA 2 code, checkpoints, and evaluation scripts (the accompanying ai.meta.com blog post refuses non-browser clients, so this repository is the citable primary artifact).
- [facebookresearch/jepa](https://github.com/facebookresearch/jepa) — **Meta FAIR** — the original V-JEPA release, useful for reading the masking implementation directly.
- [V-JEPA 2 model documentation](https://huggingface.co/docs/transformers/en/model_doc/vjepa2) — **Hugging Face** — how to load and use the encoder in a few lines.
- [VideoMAE model documentation](https://huggingface.co/docs/transformers/en/model_doc/videomae) — **Hugging Face** — pretraining and fine-tuning heads explained with code.

## Books (free, with chapters)
- [*Understanding Deep Learning* — Ch. 12 "Transformers"](https://udlbook.github.io/udlbook/) — **Simon Prince** — the encoder-decoder machinery a masked autoencoder is built from, derived cleanly.
- [*Foundations of Computer Vision* — Part IX "Representation Learning"](https://visionbook.mit.edu) — **Torralba, Isola & Freeman** — what a good learned representation is supposed to do, free online.

## In this platform
- Prerequisites: [Contrastive Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning) · [Video Transformers — TimeSformer & ViViT](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-transformers-timesformer-vivit/video-transformers-timesformer-vivit)
- Related: [Self-Supervised Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/self-supervised-vision/self-supervised-vision) (the image-only version of these objectives)
- Next: [Action Recognition & Video Classification](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/action-recognition-and-video-classification/action-recognition-and-video-classification) · [Video-Language Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-language-models/video-language-models)
