---
id: "models-and-architectures/generative-model-families/diffusion-models/video-diffusion-models"
topic: "Video Diffusion Models"
level: advanced
built_from: ["latent-diffusion-stable-diffusion", "diffusion-transformers-dit", "flow-matching-and-rectified-flow"]
leads_to: ["models-and-architectures/generative-model-families/diffusion-models/3d-generation-score-distillation", "models-and-architectures/generative-model-families/diffusion-models/diffusion-inference-optimization"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Video Diffusion Models"
minutes: 16
category: diffusion-models
---

# Video Diffusion Models
> A video model denoises a **space-time latent** instead of a single image. Two design decisions
> define the field: how time enters the network (bolt-on **temporal layers** over a frozen image model
> versus full **space-time attention** in a diffusion transformer), and how resolution and length are
> reached (a **cascade** of upsamplers versus one latent model with a video autoencoder that
> compresses time as well as space).

**Why it matters:** video is where generative modelling now spends its compute — Sora, Veo, and the
open Wan and CogVideoX families are the 2025–26 reference points. Interviewers probe: why **temporal
consistency** is not free (independent per-frame sampling flickers, so noise must be correlated across
frames); the cost curve — attention over `frames × height × width` tokens makes context length the
binding constraint; why **image-to-video** conditioning is easier to control than text-to-video; and
how these systems are evaluated at all (VBench dimensions, human preference, not FID alone).

**Start here — suggested path:**

1. **Get the survey** — read [Diffusion Models for Video Generation](https://lilianweng.github.io/posts/2024-04-12-diffusion-video/) — **Lilian Weng**. *The map of the field: 3D U-Nets, temporal layers, cascades, and training-free adaptation.*
2. **See the first formulation** — read [Video Diffusion Models](https://arxiv.org/abs/2204.03458) — **Ho et al. (2022)**. *A 3D U-Net plus the gradient method for extending videos in time; everything later is a variation.*
3. **Learn the latent recipe** — read [Align your Latents (Video LDM)](https://arxiv.org/abs/2304.08818) — **Blattmann et al. (2023)**. *Freeze an image latent diffusion model, insert temporal layers, fine-tune only those — the dominant open-source pattern.*
4. **Read the transformer turn** — read [Video generation models as world simulators](https://openai.com/index/video-generation-models-as-world-simulators/) — **OpenAI (2024)** with [Stable Video Diffusion](https://arxiv.org/abs/2311.15127) — **Blattmann et al. (2023)**. *Space-time patches and the data-curation story behind them.*
5. **Run an open model** — follow the [Diffusers video generation guide](https://huggingface.co/docs/diffusers/using-diffusers/text-img2vid) — **Hugging Face**, then read the [Wan 2.2 repository](https://github.com/Wan-Video/Wan2.2) — **Alibaba Wan team**. *Open weights make the frame-count/memory wall tangible.*

## Courses (free)

- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — the current lecture series on large vision models, including video generation.
- [MIT 6.S184: Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) — **MIT (Holderrieth & Erives)** — the flow-matching objective that most 2025–26 video models train with.

## Videos

- [Video Generation with Diffusion Transformers](https://www.youtube.com/watch?v=KAYYo3lNOHY) — **ExplainingAI** — patchifying space-time latents and the attention pattern, with code.

## Key Papers

- [Video Diffusion Models](https://arxiv.org/abs/2204.03458) — **Ho, Salimans, Gritsenko, Chan, Norouzi & Fleet (2022)** — the founding formulation: 3D U-Net, joint image-video training, reconstruction-guided extension.
- [Imagen Video: High Definition Video Generation with Diffusion Models](https://arxiv.org/abs/2210.02303) — **Ho et al. (2022)** — the cascade approach: base model plus spatial and temporal super-resolution stages.
- [Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2304.08818) — **Blattmann et al. (2023)** — temporal layers on a frozen image model; the template for open video models.
- [Stable Video Diffusion](https://arxiv.org/abs/2311.15127) — **Blattmann et al. (2023)** — open weights plus the three-stage data-curation methodology that mattered as much as the architecture.
- [Wan: Open and Advanced Large-Scale Video Generative Models](https://arxiv.org/abs/2503.20314) — **Wan Team, Alibaba (2025)** — a current open flow-matching video system with a full technical report.
- [VBench: Comprehensive Benchmark Suite for Video Generative Models](https://arxiv.org/abs/2311.17982) — **Huang et al. (2023)** — decomposes "quality" into measurable dimensions; the evaluation everyone cites.

## Articles / Blogs (free, no paywall)

- [Diffusion Models for Video Generation](https://lilianweng.github.io/posts/2024-04-12-diffusion-video/) — **Lilian Weng** — the best free survey of the architecture space, with the maths kept intact.
- [Video generation models as world simulators](https://openai.com/index/video-generation-models-as-world-simulators/) — **OpenAI** — the Sora technical report: space-time patches, variable duration and aspect ratio, scaling behaviour.
- [Veo — model page](https://deepmind.google/models/veo/) — **Google DeepMind** — capabilities, native audio, and the SynthID watermarking commitment for a frontier video model.

## In this platform

- Prerequisites: [Diffusion Transformers (DiT)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-transformers-dit/diffusion-transformers-dit) · [Latent Diffusion & Stable Diffusion](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion) · [Flow Matching & Rectified Flow](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/flow-matching-and-rectified-flow/flow-matching-and-rectified-flow)
- Next: [3D Generation & Score Distillation](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/3d-generation-score-distillation/3d-generation-score-distillation) · [Diffusion Inference Optimization](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-inference-optimization/diffusion-inference-optimization)
- Related: [Video Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/readme) (the recognition side of video) · [Optical Flow & Video](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/optical-flow-and-video/optical-flow-and-video) · [Safety, Provenance & Watermarking](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/safety-provenance-and-watermarking/safety-provenance-and-watermarking)
- Field overview: [Diffusion Models index](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme)
