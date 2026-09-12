---
id: "deep-learning/self-supervised-learning/masked-modeling-mae-and-bert-style-pretraining"
topic: "Masked Modeling — MAE and BERT-Style Pretraining"
level: intermediate
built_from: ["contrastive-self-supervised-learning", "transformer-architecture", "autoencoders"]
leads_to: ["deep-learning/self-supervised-learning/teacher-student-self-distillation-dino-byol"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Masked Modeling — MAE and BERT-Style Pretraining"
minutes: 14
category: self-supervised-learning
---

# Masked Modeling — MAE and BERT-Style Pretraining

> Hide part of the input, ask the model to reconstruct it, and the label comes from the data
> itself. **BERT** masks 15% of tokens and predicts them from both sides; the **masked
> autoencoder (MAE)** masks 75% of image patches, encodes only the visible quarter, and
> reconstructs raw pixels with a small decoder. Same recipe, and the difference in mask ratio is
> the whole lesson: language is dense in information, pixels are enormously redundant.

**Why it matters:** masked modeling is the pretraining objective for most encoders in production —
BERT-family text encoders, MAE and BEiT vision backbones, HuBERT and data2vec for audio. It is
also the cheapest self-supervised family to run, because MAE's asymmetric design (encoder sees
25% of patches) makes pretraining roughly 3× faster than a contrastive method with no negative
sampling machinery at all. Interviewers probe the **pretrain-finetune mismatch**: the `[MASK]`
token appears in pretraining and never at inference, which is precisely the flaw later objectives
were designed to remove.

**Start here — suggested path:**

1. **See the text original** — read [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) — **Devlin, Chang, Lee & Toutanova (2018)**. *Masked language modeling plus next-sentence prediction; the objective everything else adapts.*
2. **Get it visually** — read [The Illustrated BERT](https://jalammar.github.io/illustrated-bert/) — **Jay Alammar**. *The clearest free diagram set for what masked pretraining actually produces.*
3. **See the vision version** — read [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) — **He, Chen, Xie, Li, Dollár & Girshick (2021)**. *The 75% mask, the asymmetric encoder-decoder, and why pixels are a fine reconstruction target.*
4. **Watch the walkthrough** — [Masked Autoencoders Are Scalable Vision Learners — paper explained](https://www.youtube.com/watch?v=Dp6iICL2dVI) — **AI Coffee Break with Letitia**. *Animated, accurate, and short.*
5. **See it generalised across modalities** — read [data2vec](https://arxiv.org/abs/2202.03555) — **Baevski et al. (Meta AI, 2022)**. *One masked-prediction framework for speech, vision and language, predicting latent targets rather than raw inputs.*

## The design choices that matter

- **Mask ratio** — 15% for text, 40–75% for images and video; too low and the task is solved by local interpolation.
- **Reconstruction target** — raw pixels (MAE), discrete visual tokens (BEiT), latent teacher features (data2vec), or clustered units (HuBERT).
- **Where the decoder lives** — MAE's lightweight decoder is discarded after pretraining; only the encoder transfers.
- **What it gives you** — strong *fine-tuning* performance, but weaker linear-probe features than teacher-student methods, because nothing forces the representation to be linearly separable.

## Courses (free)

- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Chris Manning)** — the pretraining lecture derives masked language modeling and its variants.
- [Dive into Deep Learning](https://d2l.ai/chapter_recurrent-neural-networks/index.html) — **Zhang, Lipton, Li & Smola** — free text with runnable BERT pretraining code.

## Videos

- [Masked Autoencoders Are Scalable Vision Learners — paper explained](https://www.youtube.com/watch?v=Dp6iICL2dVI) — **AI Coffee Break with Letitia** — animated explanation of the asymmetric design.
- [DINO: Emerging Properties in Self-Supervised Vision Transformers](https://www.youtube.com/watch?v=h3ij3F3cPIk) — **Yannic Kilcher** — useful as the contrast case: what masked modeling does *not* give you.

## Key Papers

- [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) — **Devlin et al. (2018)** — the masked language modeling objective.
- [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) — **He et al. (2021)** — MAE; the reference masked vision model.
- [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254) — **Bao, Dong, Piao & Wei (2021)** — discrete visual tokens as the reconstruction target.
- [SimMIM: A Simple Framework for Masked Image Modeling](https://arxiv.org/abs/2111.09886) — **Xie et al. (2021)** — the ablation study showing how little machinery masked vision modeling needs.
- [HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units](https://arxiv.org/abs/2106.07447) — **Hsu et al. (2021)** — the speech counterpart; masked prediction over clustered acoustic units.
- [data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language](https://arxiv.org/abs/2202.03555) — **Baevski et al. (2022)** — one objective, three modalities, latent targets.
- [VideoMAE](https://arxiv.org/abs/2203.12602) — **Tong, Song, Wang & Wang (2022)** — 90%+ masking for video, where redundancy is even higher.

## Articles / Blogs (free, no paywall)

- [The Illustrated BERT, ELMo, and co.](https://jalammar.github.io/illustrated-bert/) — **Jay Alammar** — the diagrams that made masked pretraining legible to everyone.
- [Self-Supervised Representation Learning](https://lilianweng.github.io/posts/2019-11-10-self-supervised/) — **Lilian Weng** — the survey that maps masked modeling against every other pretext task.
- [facebookresearch/mae](https://github.com/facebookresearch/mae) — **Meta AI Research** — the official MAE implementation and pretrained checkpoints.
- [A Cookbook of Self-Supervised Learning](https://arxiv.org/abs/2304.12210) — **Balestriero et al. (Meta AI, 2023)** — practical recipes, including when masked modeling beats the alternatives.

## In this platform

- Prerequisites: [Transformer Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/transformer-architecture/transformer-architecture) · [Autoencoders](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/autoencoders/autoencoders)
- Sibling objectives: [Contrastive Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning) · [Teacher-Student Self-Distillation (DINO, BYOL)](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/teacher-student-self-distillation-dino-byol/teacher-student-self-distillation-dino-byol)
- Downstream: [Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism)
