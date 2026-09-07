---
id: "modalities-and-generative-models/diffusion-models/flow-matching-and-rectified-flow"
topic: "Flow Matching & Rectified Flow"
level: advanced
built_from: ["score-based-and-sde-diffusion", "diffusion-models-ddpm", "normalizing-flows"]
leads_to: ["diffusion-transformers-dit", "consistency-models-and-few-step-generation", "distillation-for-fast-sampling"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Flow Matching & Rectified Flow"
minutes: 16
category: diffusion-models
---

# Flow Matching & Rectified Flow
> **Flow matching** trains a network to predict a *velocity* — the direction that carries a noise
> sample to a data sample along a chosen path — by regressing on straight lines between the two.
> **Rectified flow** is the version everyone ships: the path is the straight interpolation
> `x_t = (1 − t)·x_0 + t·ε`, so sampling is just integrating an ordinary differential equation (ODE)
> along an almost-straight trajectory in a handful of steps.

**Why it matters:** this is the training objective of Stable Diffusion 3, FLUX.1, and most 2025–26
video models — the field moved from denoising diffusion probabilistic models (DDPM) to flow matching
without changing the architecture. Interviewers probe: why flow matching and diffusion are *the same
family* under a change of variables (a noise schedule is a path; a score is a velocity in disguise);
why straight paths cut the number of function evaluations; what **logit-normal timestep sampling**
does in the SD3 recipe; and why "simulation-free" training was the breakthrough that made continuous
normalizing flows practical at scale.

**Start here — suggested path:**

1. **Build the picture** — read [An Introduction to Flow Matching](https://mlg.eng.cam.ac.uk/blog/2024/01/20/flow-matching.html) — **Cambridge Machine Learning Group (Fjelde, Mathieu & Dutordoir)**. *Probability paths and velocity fields, with animations, before any measure theory.*
2. **Connect it to what you know** — read [Diffusion Meets Flow Matching: Two Sides of the Same Coin](https://diffusionflow.github.io/) — **Gao, Hoogeboom, Heek, Salimans, Dieleman (Google DeepMind)**. *Shows the two frameworks are equivalent up to reparameterization — the single most clarifying read here.*
3. **Get the math** — work through the [MIT 6.S184 lecture notes](https://arxiv.org/abs/2506.02070) — **Holderrieth & Erives (MIT)**. *Derives conditional flow matching from scratch; the marginal-versus-conditional velocity argument is the crux.*
4. **Read the sources** — [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) — **Lipman et al. (2022)** and [Rectified Flow](https://arxiv.org/abs/2209.03003) — **Liu, Gong & Liu (2022)**. *The objective, then the straight-path special case that industrial models use.*
5. **Implement it** — follow the [Flow Matching Guide and Code](https://arxiv.org/abs/2412.06264) — **Lipman et al., Meta FAIR (2024)** with the [`facebookresearch/flow_matching`](https://github.com/facebookresearch/flow_matching) library. *A 30-line training loop makes the "regress a velocity" claim real.*

## Courses (free)

- [MIT 6.S184: Flow Matching and Diffusion Models (2026)](https://www.youtube.com/playlist?list=PL57nT7tSGAAXwjhDYcxEycx5W7YoSrZyt) — **Peter Holderrieth (MIT)** — the canonical free course on flow matching: lectures, notes, and labs building both frameworks side by side.
- [MIT 6.S184 course site](https://diffusion.csail.mit.edu/) — **MIT CSAIL** — slides, problem sets, and the full lecture notes as a PDF.
- [Stanford CS236: Deep Generative Models](https://deepgenerativemodels.github.io/) — **Stanford (Stefano Ermon)** — free notes placing flow matching among normalizing flows, diffusion, and score matching.

## Videos

- [MIT 6.S184 Lecture 01 — Generative AI with Stochastic Differential Equations](https://www.youtube.com/watch?v=GCoP2w-Cqtg) — **Peter Holderrieth (MIT)** — starts from ODEs and flows, so the velocity field is motivated before it is defined.
- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — covers the rectified-flow training recipe used by current text-to-image systems.

## Key Papers

- [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) — **Lipman, Chen, Ben-Hamu, Nickel & Le (2022)** — conditional flow matching: simulation-free training of continuous normalizing flows.
- [Flow Straight and Fast: Rectified Flow](https://arxiv.org/abs/2209.03003) — **Liu, Gong & Liu (2022)** — the straight-line interpolant and *reflow*, which straightens trajectories for few-step sampling.
- [Stochastic Interpolants: A Unifying Framework](https://arxiv.org/abs/2303.08797) — **Albergo, Boffi & Vanden-Eijnden (2023)** — the general statement that diffusion, flows, and interpolants are one construction.
- [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2403.03206) — **Esser et al. (2024)** — the production recipe: rectified flow plus logit-normal timestep weighting, at Stable Diffusion 3 scale.
- [Flow Matching Guide and Code](https://arxiv.org/abs/2412.06264) — **Lipman et al., Meta FAIR (2024)** — a 100-page self-contained guide with a PyTorch library; the best single reference.

## Articles / Blogs (free, no paywall)

- [Diffusion Meets Flow Matching: Two Sides of the Same Coin](https://diffusionflow.github.io/) — **Google DeepMind (Gao, Hoogeboom, Heek, Salimans, Dieleman)** — the equivalence, worked out with equations you can check.
- [Learning the integral of a diffusion model (flow maps)](https://sander.ai/2026/05/06/flow-maps.html) — **Sander Dieleman (Google DeepMind)** — where the field went next: learning the *solution* of the flow ODE rather than its derivative.
- [An Introduction to Flow Matching](https://mlg.eng.cam.ac.uk/blog/2024/01/20/flow-matching.html) — **Cambridge MLG** — the friendliest correct introduction, with visualisations of probability paths.
- [Noise schedules considered harmful](https://sander.ai/2024/06/14/noise-schedules.html) — **Sander Dieleman** — why the schedule is a coordinate choice, which is exactly the flow-matching insight.

## Books (free, with chapters)

- [*Probabilistic Machine Learning: Advanced Topics* — Ch. 25 "Diffusion models"](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; the continuous-time view that flow matching generalises.

## In this platform

- Prerequisites: [Score-Based & SDE Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/score-based-and-sde-diffusion/score-based-and-sde-diffusion) · [Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm) · [Normalizing Flows](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/normalizing-flows/normalizing-flows)
- Next: [Diffusion Transformers (DiT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-transformers-dit/diffusion-transformers-dit) · [Consistency Models & Few-Step Generation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/consistency-models-and-few-step-generation/consistency-models-and-few-step-generation) · [Distillation for Fast Sampling](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/distillation-for-fast-sampling/distillation-for-fast-sampling)
- Related: [Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques) (the probability-flow ODE) · [Variational Autoencoders (VAE · ELBO)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo)
- Field overview: [Generative Models index](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme)
