---
id: "10-generative-ai/latent-diffusion"
topic: "Latent Diffusion & Stable Diffusion"
parent: "10-generative-ai"
level: advanced
built_from: ["diffusion-ddpm", "vae", "conditional-cfg", "attention", "clip"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Latent Diffusion & Stable Diffusion"
minutes: 10
category: diffusion-models
---

# Latent Diffusion & Stable Diffusion
> Pixel-space diffusion is expensive. **Latent Diffusion Models (LDM)** first compress images into a
> small latent space with a pretrained **VAE**, run the whole diffusion process *there*, then decode
> back to pixels — orders of magnitude cheaper. Add **cross-attention** to a text encoder and you get
> **Stable Diffusion**: a U-Net denoiser conditioned on a CLIP text embedding, steered by
> classifier-free guidance.

**Why it matters:** the architecture behind the open-source image-generation explosion, and the
go-to systems-design answer for "how does Stable Diffusion work?" Interviews probe: *why* diffuse in
latent space (perceptual compression vs. semantic detail; the VAE handles the high-frequency pixels so
the U-Net models semantics), the three components (VAE encoder/decoder, conditioning text encoder,
denoising U-Net with cross-attention), where **CFG** plugs in, and the trade-offs vs pixel-space
diffusion (speed and memory vs a slight quality ceiling from the autoencoder).

**⭐ Start here — suggested path:**

1. **Build intuition** — watch [How AI Image Generators Work (Stable Diffusion / DALL·E)](https://www.youtube.com/watch?v=1CIpzeNxIhU) — **Computerphile**. *The clearest plain-language tour of the full pipeline.*
2. **See why it works** — read [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) — **Jay Alammar**. *Visual, component-by-component: VAE, text encoder, U-Net, cross-attention.*
3. **Get the math** — watch [How does Stable Diffusion work? — Latent Diffusion Models EXPLAINED](https://www.youtube.com/watch?v=J87hffSMB60) — **AI Coffee Break (Letitia)** + read [Stable Diffusion with Diffusers](https://huggingface.co/blog/stable_diffusion). *Why latent space, and how the pieces connect.*
4. **Read the source** — [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) — **Rombach et al. (2022)**. *The LDM paper; perceptual compression + cross-attention conditioning.*
5. **Make it concrete** — run the [Hugging Face `diffusers` quickstart](https://huggingface.co/docs/diffusers/index), or watch [Coding Stable Diffusion from scratch](https://www.youtube.com/watch?v=ZBKpAp_6TGI) — **Umar Jamil**. *Generating from a prompt and tweaking the guidance scale cements it.*

## Courses (free)
- [Hugging Face — Diffusion Models Course (Stable Diffusion unit)](https://huggingface.co/learn/diffusion-course/unit0/1) — **Hugging Face** — free, code-first; build conditioned latent diffusion with `diffusers`.
- [Stanford CS236 — Deep Generative Models](https://deepgenerativemodels.github.io/) — **Stanford (Ermon)** — free notes; situates latent diffusion within the broader generative-models map.

## Videos
- [How AI Image Generators Work (Stable Diffusion / DALL·E)](https://www.youtube.com/watch?v=1CIpzeNxIhU) — **Computerphile** — the best plain-language overview of the whole pipeline.
- [How does Stable Diffusion work? — Latent Diffusion Models EXPLAINED](https://www.youtube.com/watch?v=J87hffSMB60) — **AI Coffee Break (Letitia)** — why latent space, and the VAE + U-Net + text-encoder design.
- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — the current Stanford course on diffusion and large vision models, covering the latent-space design choices this page introduces.
- [Coding Stable Diffusion from scratch in PyTorch](https://www.youtube.com/watch?v=ZBKpAp_6TGI) — **Umar Jamil** — builds the full system (VAE, CLIP, U-Net, sampler) line by line.

## Key Papers
- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) — **Rombach et al. (2022)** — Stable Diffusion: diffuse in VAE latent space with cross-attention conditioning.
- [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598) — **Ho & Salimans (2022)** — the guidance mechanism that gives Stable Diffusion its prompt adherence.
- [SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis](https://arxiv.org/abs/2307.01952) — **Podell et al. (2023)** — a bigger U-Net, two text encoders, and size/crop conditioning; the last major U-Net-based Stable Diffusion.
- [Scalable Diffusion Models with Transformers (DiT)](https://arxiv.org/abs/2212.09748) — **Peebles & Xie (2023)** — replaces the U-Net with a transformer over latent patches; the architecture every 2024–26 system adopted.
- [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis (Stable Diffusion 3)](https://arxiv.org/abs/2403.03206) — **Esser et al. (2024)** — rectified-flow training plus the MMDiT two-stream transformer; the current shape of the open text-to-image stack.

## Articles / Blogs (free, no paywall)
- [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) — **Jay Alammar** — the canonical visual explainer; VAE, text encoder, U-Net, cross-attention.
- [Stable Diffusion with 🧨 Diffusers](https://huggingface.co/blog/stable_diffusion) — **Hugging Face** — the architecture plus runnable code for each stage, free.
- [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) — **Hugging Face** — the U-Net denoiser internals that latent diffusion reuses, free.

## Books (free, with chapters)
- [Understanding Deep Learning — **Ch. 18 "Diffusion models"**](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; conditioning and latent diffusion in the diffusion chapter.
- [Probabilistic Machine Learning: Advanced Topics — **Ch. 25 "Diffusion models"**](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; latent and conditional diffusion in the modern treatment.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 5.03 Diffusion Models](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition) · [5.02 ELBO & VAEs](/ai-ml/ai-ml-intuitions/generation/latent-variable-generation/latent-variable-models-and-elbo-intuition)
- Prereq: [05 Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm) · [01 Variational Autoencoders](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo) (the latent compressor) · [04 Conditional Generation & CFG](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/conditional-generation-and-classifier-free-guidance/conditional-generation-and-classifier-free-guidance)
- Related: [Deep Learning — Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) (cross-attention conditions the U-Net)
- Next concepts: [11 Text-to-Image Systems](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/text-to-image-systems/text-to-image-systems) · [13 Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques)
- Where the architecture went: [Diffusion Transformers (DiT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-transformers-dit/diffusion-transformers-dit) — the U-Net replaced by a transformer over latent patches
- Where the training objective went: [Flow Matching & Rectified Flow](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/flow-matching-and-rectified-flow/flow-matching-and-rectified-flow) — straight-line paths instead of a noise schedule, as used by Stable Diffusion 3 and FLUX
- Field overview: [9. Generative AI](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme)
