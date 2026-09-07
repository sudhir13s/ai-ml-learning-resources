---
id: "10-generative-ai/conditional-cfg"
topic: "Conditional Generation & Classifier-Free Guidance"
parent: "10-generative-ai"
level: advanced
built_from: ["gans-dcgan", "diffusion-ddpm", "bayes-rule", "cross-entropy"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Conditional Generation & Classifier-Free Guidance"
minutes: 10
category: diffusion-models
---

# Conditional Generation & Classifier-Free Guidance
> Make a generator obey a **condition** `y` (a class label, a text prompt, an input image). For GANs
> this is **cGAN** — feed `y` to both generator and discriminator (pix2pix conditions on a whole
> image). For diffusion, the dominant tool is **Classifier-Free Guidance (CFG)**: jointly train a
> conditional and an unconditional model (by randomly dropping `y`), then at sampling time extrapolate
> `ε̃ = ε_uncond + s·(ε_cond − ε_uncond)` to *amplify* the condition — the knob behind every prompt's
> "guidance scale."

**Why it matters:** the bridge from "generate something" to "generate *this*," and a hot interview
topic because CFG powers Stable Diffusion, DALL·E 2, and Imagen. Expect: how a cGAN conditions both
networks; **classifier guidance** vs **classifier-free guidance** (and why the classifier-free version
won — no separate, noise-robust classifier to train); the Bayes-rule derivation
(`∇log p(x|y) = ∇log p(x) + ∇log p(y|x)`) that links the two; and the guidance-scale trade-off —
higher `s` gives better prompt adherence but less diversity and possible artifacts.

**⭐ Start here — suggested path:**

1. **Build intuition** — watch [Diffusion models explained: how does GLIDE work?](https://www.youtube.com/watch?v=344w5h24-h8) — **AI Coffee Break (Letitia)**. *Shows conditioning + guidance in the system that introduced CFG to text-to-image.*
2. **See why it works** — read [Guidance: a cheat code for diffusion models](https://sander.ai/2022/05/26/guidance.html) — **Sander Dieleman**. *The clearest account of what guidance does and why scaling it trades diversity for fidelity.*
3. **Get the math** — read [Conditional Image Generation with Classifier-Free Guidance](https://www.peterholderrieth.com/blog/2023/Classifier-Free-Guidance-For-Diffusion-Models/) — **Peter Holderrieth (MIT)**. *The training (condition-dropout) and the sampling extrapolation formula, derived from Bayes' rule.*
4. **Read the sources** — [Conditional GANs](https://arxiv.org/abs/1411.1784) — **Mirza & Osindero (2014)** · [Diffusion Models Beat GANs (classifier guidance)](https://arxiv.org/abs/2105.05233) — **Dhariwal & Nichol (2021)** · [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598) — **Ho & Salimans (2022)**. *cGAN → classifier guidance → the classifier-free version everyone uses.*
5. **Make it concrete** — train a conditional GAN with the [official pix2pix PyTorch implementation](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) — **Jun-Yan Zhu & Taesung Park**. *Conditioning a generator on an image makes "conditioning" concrete before the diffusion version.*

## Courses (free)
- [Hugging Face — Diffusion Models Course (conditioning & guidance unit)](https://huggingface.co/learn/diffusion-course/unit0/1) — **Hugging Face** — free, code-first; covers class conditioning and CFG with runnable notebooks.
- [Google — Generative Adversarial Networks](https://developers.google.com/machine-learning/gan) — **Google** — free course; the conditional-GAN section shows label-conditioned generation.

## Videos
- [Diffusion models explained: how does OpenAI's GLIDE work?](https://www.youtube.com/watch?v=344w5h24-h8) — **AI Coffee Break (Letitia)** — text conditioning and guidance in the model that popularized CFG.
- [How AI Image Generators Work (Stable Diffusion / DALL·E)](https://www.youtube.com/watch?v=1CIpzeNxIhU) — **Computerphile** — how a text prompt steers generation, in plain language.
- [MIT 6.S184 Lecture 03B — Classifier-free Guidance](https://www.youtube.com/watch?v=8oWZ1bHwyRI) — **Peter Holderrieth (MIT)** — the 2026 course derivation of CFG from the conditional and unconditional velocity fields.
- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — the current Stanford course; conditioning and guidance inside the modern text-to-image stack.

## Key Papers
- [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784) — **Mirza & Osindero (2014)** — the cGAN: condition both `G` and `D` on a label `y`.
- [Image-to-Image Translation with Conditional Adversarial Networks (pix2pix)](https://arxiv.org/abs/1611.07004) — **Isola et al. (2017)** — conditioning on a full image; the PatchGAN discriminator.
- [Diffusion Models Beat GANs on Image Synthesis](https://arxiv.org/abs/2105.05233) — **Dhariwal & Nichol (2021)** — **classifier guidance**: steer sampling with a noise-aware classifier's gradient.
- [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598) — **Ho & Salimans (2022)** — drop the classifier; train one model with condition-dropout and extrapolate at sampling.
- [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis (Stable Diffusion 3)](https://arxiv.org/abs/2403.03206) — **Esser et al. (2024)** — how conditioning is wired in a 2024–26 system: three text encoders and a two-stream MMDiT that lets text and image tokens attend to each other, with CFG still the sampling-time knob.
- [Adversarial Diffusion Distillation](https://arxiv.org/abs/2311.17042) — **Sauer et al. (2023)** — a distilled few-step student that bakes the guidance in; the reason "guidance scale" behaves differently on turbo/consistency models.

## Articles / Blogs (free, no paywall)
- [Guidance: a cheat code for diffusion models](https://sander.ai/2022/05/26/guidance.html) — **Sander Dieleman** — the definitive intuition for what guidance does and the fidelity/diversity trade-off.
- [Conditional Image Generation with Classifier-Free Guidance](https://www.peterholderrieth.com/blog/2023/Classifier-Free-Guidance-For-Diffusion-Models/) — **Peter Holderrieth (MIT)** — the training trick and sampling formula, derived from Bayes' rule, free.
- [pix2pix project page — Image-to-Image Translation with Conditional Adversarial Networks](https://phillipi.github.io/pix2pix/) — **Isola, Zhu, Zhou & Efros (Berkeley AI Research)** — results, paper, and the reference implementation you can run.

## Books (free, with chapters)
- [Deep Learning — **§20.10.4 (GANs) & §3.9–3.13 (probability / Bayes)**](https://www.deeplearningbook.org/contents/generative_models.html) — **Goodfellow, Bengio & Courville** — conditional generation and the Bayes background under guidance.
- [Dive into Deep Learning — **Ch. 20 "Generative Adversarial Networks"**](https://d2l.ai/chapter_generative-adversarial-networks/index.html) — **Zhang et al.** — free, with conditional-GAN code to adapt.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 5.03 Diffusion Models](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition) · [5.04 GANs & WGAN](/ai-ml/ai-ml-intuitions/generation/adversarial-generation/gans-and-wasserstein-gans-intuition)
- Prereq: [02 GANs & DCGAN](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/gans-and-dcgan/gans-and-dcgan) · [05 Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm)
- Next concepts: [07 Latent Diffusion & Stable Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion) · [11 Text-to-Image Systems](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/text-to-image-systems/text-to-image-systems) · [13 Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques)
- Where conditioning went in 2025–26: [ControlNet & Conditioning Adapters](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/controlnet-and-conditioning-adapters/controlnet-and-conditioning-adapters) (structural control) · [Diffusion Transformers (DiT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-transformers-dit/diffusion-transformers-dit) (conditioning by adaptive layer norm and joint attention) · [Distillation for Fast Sampling](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/distillation-for-fast-sampling/distillation-for-fast-sampling) (guidance folded into the student)
- Field overview: [9. Generative AI](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme)
