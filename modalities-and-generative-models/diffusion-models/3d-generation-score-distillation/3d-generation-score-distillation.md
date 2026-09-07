---
id: "modalities-and-generative-models/diffusion-models/3d-generation-score-distillation"
topic: "3D Generation & Score Distillation"
level: advanced
built_from: ["sampling-and-guidance-techniques", "text-to-image-systems", "video-diffusion-models"]
leads_to: ["modalities-and-generative-models/diffusion-models/diffusion-inference-optimization"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 14
title: "3D Generation & Score Distillation"
minutes: 14
category: diffusion-models
---

# 3D Generation & Score Distillation
> There is no ImageNet-scale dataset of 3D assets, so **DreamFusion** did something else: it optimized
> a neural radiance field (NeRF) so that *every rendered view* looks plausible to a frozen 2D
> text-to-image diffusion model. That loop is **score distillation sampling (SDS)** — render, add
> noise, ask the image model which direction reduces the noise, backpropagate that direction through
> the renderer into the 3D parameters.

**Why it matters:** SDS is the general recipe for "use a 2D prior to supervise a representation you
have no data for", and it now drives text-to-3D, texture synthesis, and 4D generation. Interviewers
probe: why SDS needs an enormous guidance scale (~100) and still produces **over-saturated, blurry,
low-diversity** results — the mode-seeking behaviour that **ProlificDreamer**'s variational score
distillation fixes; the **Janus problem** (multi-face artifacts from view-inconsistent 2D priors) and
its cure, multi-view-aware diffusion; and the 2024–26 shift away from per-asset optimization toward
**feed-forward 3D generators** (TRELLIS, large reconstruction models) that produce meshes or Gaussians
in seconds.

**Start here — suggested path:**

1. **See the loop** — read the [DreamFusion project page](https://dreamfusion3d.github.io/) — **Poole, Jain, Barron & Mildenhall (Google Research)**. *Renders, prompts, and failure cases in one scroll; SDS in a single figure.*
2. **Get the objective** — read [DreamFusion: Text-to-3D using 2D Diffusion](https://arxiv.org/abs/2209.14988) — **Poole et al. (2022)**, Section 3. *Why the U-Net Jacobian is dropped, and what the resulting gradient actually is.*
3. **Understand the quality problem** — read [ProlificDreamer](https://arxiv.org/abs/2305.16213) — **Wang et al. (2023)**. *Variational score distillation: treat the 3D scene as a distribution, not a point estimate; the saturation goes away.*
4. **Learn the representation shift** — read [3D Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) — **Kerbl, Kopanas, Leimkühler & Drettakis (2023)**. *Real-time differentiable rendering; the substrate most 2025–26 3D generators optimize or emit.*
5. **See the feed-forward era** — read [TRELLIS: Structured 3D Latents](https://microsoft.github.io/TRELLIS/) — **Xiang et al., Microsoft Research (2024)**. *A rectified-flow transformer over structured 3D latents, decoding to radiance fields, Gaussians, or meshes — no per-asset optimization.*

## Courses (free)

- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — the 2D priors and samplers that 3D generation distils from.
- [MIT 6.S184: Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) — **MIT (Holderrieth & Erives)** — the objective used by current feed-forward 3D generators.

## Key Papers

- [DreamFusion: Text-to-3D using 2D Diffusion](https://arxiv.org/abs/2209.14988) — **Poole, Jain, Barron & Mildenhall (2022)** — introduces score distillation sampling; the paper the whole area cites.
- [Magic3D: High-Resolution Text-to-3D Content Creation](https://arxiv.org/abs/2211.10440) — **Lin et al. (2022)** — coarse-to-fine (NeRF then textured mesh); the pattern production pipelines copy.
- [ProlificDreamer: High-Fidelity Text-to-3D with Variational Score Distillation](https://arxiv.org/abs/2305.16213) — **Wang et al. (2023)** — diagnoses and repairs SDS's mode-seeking behaviour.
- [Zero-1-to-3: Zero-shot One Image to 3D Object](https://arxiv.org/abs/2303.11328) — **Liu et al. (2023)** — fine-tunes a diffusion model for viewpoint control, the fix for view inconsistency.
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079) — **Kerbl et al. (2023)** — the representation that replaced NeRF in most generation pipelines.
- [DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://arxiv.org/abs/2309.16653) — **Tang et al. (2023)** — swaps the NeRF for Gaussians and cuts per-asset optimization from hours to minutes.
- [Structured 3D Latents for Scalable and Versatile 3D Generation (TRELLIS)](https://arxiv.org/abs/2412.01506) — **Xiang et al. (2024)** — feed-forward generation with one latent that decodes to several 3D formats.

## Articles / Blogs (free, no paywall)

- [DreamFusion project page](https://dreamfusion3d.github.io/) — **Google Research** — interactive results and the clearest statement of the SDS loop.
- [3D Gaussian Splatting project page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) — **Inria GraphDeco** — paper, code, and viewers from the authors.
- [TRELLIS project page](https://microsoft.github.io/TRELLIS/) — **Microsoft Research** — the structured-latent design with side-by-side output formats.

## In this platform

- Prerequisites: [Text-to-Image Systems](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/text-to-image-systems/text-to-image-systems) (the frozen 2D prior) · [Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques) (why the guidance scale is so high here)
- Related: [3D & Depth Estimation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/3d-and-depth-estimation/3d-and-depth-estimation) (NeRF and the geometry background) · [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/video-diffusion-models/video-diffusion-models) (multi-view priors now often come from video models)
- Next: [Diffusion Inference Optimization](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-inference-optimization/diffusion-inference-optimization)
- Field overview: [Diffusion Models index](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme)
