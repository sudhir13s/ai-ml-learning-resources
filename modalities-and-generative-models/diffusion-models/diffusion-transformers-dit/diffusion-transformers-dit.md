---
id: "modalities-and-generative-models/diffusion-models/diffusion-transformers-dit"
topic: "Diffusion Transformers (DiT)"
level: advanced
built_from: ["latent-diffusion-stable-diffusion", "diffusion-models-ddpm", "vision-transformers"]
leads_to: ["modalities-and-generative-models/diffusion-models/flow-matching-and-rectified-flow", "modalities-and-generative-models/diffusion-models/video-diffusion-models", "modalities-and-generative-models/diffusion-models/diffusion-inference-optimization"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Diffusion Transformers (DiT)"
minutes: 14
category: diffusion-models
---

# Diffusion Transformers (DiT)
> A **diffusion transformer (DiT)** throws away the convolutional U-Net denoiser and predicts noise
> with a plain transformer over latent *patches*. Nothing about the diffusion objective changes —
> only the backbone. The payoff is a clean scaling law: more compute (**giga-FLOPs per forward
> pass**) reliably buys lower Fréchet Inception Distance (FID), the same lever that made large
> language models work.

**Why it matters:** every frontier image and video generator shipped since 2024 — Stable Diffusion 3,
FLUX.1, PixArt, Sora, Veo, Wan — is a transformer, not a U-Net. Interviewers probe three things: how
the *timestep* and *class/text* condition enters the block (**adaptive layer norm with zero
initialization**, adaLN-Zero, beats cross-attention and in-context tokens in the DiT ablation); why
patch size is the dominant compute knob (halving it roughly quadruples tokens and FLOPs with no extra
parameters); and how **MMDiT** (SD3) extends this by giving text and image streams their own weights
while attending jointly.

**Start here — suggested path:**

1. **See the swap** — read [Scalable Diffusion Models with Transformers — project page](https://www.wpeebles.com/DiT) — **William Peebles & Saining Xie**. *The one-picture version: latent patches in, transformer blocks, noise out.*
2. **Get the mechanism** — read the [DiT paper](https://arxiv.org/abs/2212.09748) — **Peebles & Xie (2022)**, Sections 3–4. *The four conditioning variants and why adaLN-Zero wins; the FLOPs-versus-FID plot is the whole argument.*
3. **See the modern version** — read [Scaling Rectified Flow Transformers (Stable Diffusion 3)](https://arxiv.org/abs/2403.03206) — **Esser et al. (2024)**. *MMDiT: two weight streams (text, image), one joint attention — the 2024–26 default.*
4. **Watch it applied to video** — [Video Generation with Diffusion Transformers](https://www.youtube.com/watch?v=KAYYo3lNOHY) — **ExplainingAI**. *Patchifying space-time latents, the step from images to Sora-style models.*
5. **Run one** — load a DiT/SD3 pipeline from the [Diffusers documentation](https://huggingface.co/docs/diffusers/index) and print the transformer's block count, hidden size, and patch size. *Seeing `transformer` instead of `unet` in the pipeline makes the change concrete.*

## Courses (free)

- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — the 2025 lecture series covering transformer backbones, rectified flow, and large vision models end to end.
- [MIT 6.S184: Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) — **MIT (Holderrieth & Erives)** — free lectures, notes, and labs; builds the sampler the DiT backbone plugs into.
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — code-first; swap backbones inside `diffusers` and inspect shapes.

## Videos

- [Video Generation with Diffusion Transformers](https://www.youtube.com/watch?v=KAYYo3lNOHY) — **ExplainingAI** — walks the DiT block and its space-time extension with the code in front of you.
- [Stanford CME296 lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — university-level treatment of the backbone shift, from ViT to DiT to MMDiT.

## Key Papers

- [Scalable Diffusion Models with Transformers (DiT)](https://arxiv.org/abs/2212.09748) — **Peebles & Xie (2022)** — the original swap: adaLN-Zero conditioning, patch-size ablation, FID that falls monotonically with FLOPs.
- [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis (SD3)](https://arxiv.org/abs/2403.03206) — **Esser et al. (2024)** — MMDiT plus rectified-flow training; the reference architecture for current text-to-image systems.
- [All are Worth Words: A ViT Backbone for Diffusion Models (U-ViT)](https://arxiv.org/abs/2209.09962) — **Bao et al. (2022)** — the parallel discovery, keeping U-Net-style long skips inside a transformer.
- [PixArt-α: Fast Training of Diffusion Transformers](https://arxiv.org/abs/2310.00426) — **Chen et al. (2023)** — cross-attention DiT trained for a fraction of the usual compute; the open recipe people actually fine-tune.

## Articles / Blogs (free, no paywall)

- [Video generation models as world simulators (Sora technical report)](https://openai.com/index/video-generation-models-as-world-simulators/) — **OpenAI (2024)** — states plainly that Sora is a diffusion transformer over space-time patches, and shows the compute-scaling samples.
- [Perspectives on diffusion](https://sander.ai/2023/07/20/perspectives.html) — **Sander Dieleman (Google DeepMind)** — why the backbone is interchangeable: the objective, not the network, defines a diffusion model.
- [Announcing Black Forest Labs (FLUX.1)](https://blackforestlabs.ai/announcing-black-forest-labs/) — **Black Forest Labs (2024)** — the 12B rectified-flow transformer from the original Stable Diffusion team; architecture and licence tiers.

## Books (free, with chapters)

- [*Understanding Deep Learning* — Ch. 18 "Diffusion models"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the denoiser's role, which is exactly what DiT replaces.

## In this platform

- Prerequisites: [Latent Diffusion & Stable Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion) · [Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm) · [Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers)
- Next: [Flow Matching & Rectified Flow](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/flow-matching-and-rectified-flow/flow-matching-and-rectified-flow) (how these backbones are trained today) · [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/video-diffusion-models/video-diffusion-models) · [Diffusion Inference Optimization](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-inference-optimization/diffusion-inference-optimization)
- Related: [Text-to-Image Systems](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/text-to-image-systems/text-to-image-systems) · [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture)
- Field overview: [Diffusion Models index](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme)
