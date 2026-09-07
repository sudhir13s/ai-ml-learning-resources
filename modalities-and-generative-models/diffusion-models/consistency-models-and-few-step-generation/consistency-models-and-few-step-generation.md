---
id: "modalities-and-generative-models/diffusion-models/consistency-models-and-few-step-generation"
topic: "Consistency Models & Few-Step Generation"
level: advanced
built_from: ["score-based-and-sde-diffusion", "sampling-and-guidance-techniques", "flow-matching-and-rectified-flow"]
leads_to: ["modalities-and-generative-models/diffusion-models/distillation-for-fast-sampling", "modalities-and-generative-models/diffusion-models/diffusion-inference-optimization"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Consistency Models & Few-Step Generation"
minutes: 14
category: diffusion-models
---

# Consistency Models & Few-Step Generation
> A **consistency model** learns a function `f(x_t, t)` that maps *any* point on a probability-flow
> ordinary differential equation (ODE) trajectory straight back to the trajectory's origin — the clean
> sample. If every point on the path returns the same answer (that is the *consistency* constraint),
> one network call generates an image, and extra calls only refine it.

**Why it matters:** it reframes acceleration. Samplers make each step cheaper; consistency models
change what a step *means*, giving 1–4-step generation without an adversarial loss. Interviewers
probe: the difference between **consistency distillation** (a teacher diffusion model supplies the
ODE path) and **consistency training** (no teacher at all); why the boundary condition
`f(x_ε, ε) = x_ε` must be baked into the parameterization rather than learned; why the discrete-time
version is so sensitive to the step-count schedule that OpenAI's **sCM** moved to continuous time;
and the honest trade-off — few-step samples lose diversity and fine texture relative to the teacher.

**Start here — suggested path:**

1. **Get the core claim** — read the [Consistency Models paper](https://arxiv.org/abs/2303.01469) — **Song, Dhariwal, Chen & Sutskever (2023)**, Sections 1–3. *The self-consistency property and the two training modes, stated in three pages.*
2. **See why it was hard to scale** — read [Simplifying, stabilizing and scaling continuous-time consistency models](https://openai.com/index/simplifying-stabilizing-and-scaling-continuous-time-consistency-models/) — **OpenAI (2024)**. *What broke in discrete time and how TrigFlow fixed it; two-step samples within 10% of the teacher's FID.*
3. **Place it in the family** — read [Learning the integral of a diffusion model](https://sander.ai/2026/05/06/flow-maps.html) — **Sander Dieleman (Google DeepMind)**. *Flow maps as the umbrella over consistency models, shortcut models, and MeanFlow — the clearest 2026 framing.*
4. **Read the practical variant** — [Latent Consistency Models](https://arxiv.org/abs/2310.04378) — **Luo et al. (2023)**. *The version that made 4-step Stable Diffusion mainstream, plus LCM-LoRA as a plug-in accelerator.*
5. **Run one** — follow the [Diffusers LCM guide](https://huggingface.co/docs/diffusers/using-diffusers/inference_with_lcm) and compare 4-step and 50-step outputs on the same seed. *Seeing where detail and diversity go is the lesson no paper figure teaches.*

## Courses (free)

- [MIT 6.S184: Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) — **MIT (Holderrieth & Erives)** — the ODE-trajectory view that consistency models short-circuit, taught from first principles.
- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — includes the fast-sampling and distillation landscape as deployed in 2025.

## Videos

- [Variational Autoencoders and Diffusion Models (M2L summer school)](https://www.youtube.com/watch?v=pea3sH6orMc) — **Tim Salimans (Google DeepMind)** — a researcher who built progressive distillation explaining why few-step generation is possible at all.
- [MIT 6.S184 Lecture 01 — Generative AI with SDEs](https://www.youtube.com/watch?v=GCoP2w-Cqtg) — **Peter Holderrieth (MIT)** — the probability-flow ODE whose solution map consistency models approximate.

## Key Papers

- [Consistency Models](https://arxiv.org/abs/2303.01469) — **Song, Dhariwal, Chen & Sutskever (2023)** — the original: self-consistency along the ODE, one-step generation, distillation and standalone training.
- [Improved Techniques for Training Consistency Models](https://arxiv.org/abs/2310.14189) — **Song & Dhariwal (2023)** — the fixes (loss weighting, dropping the exponential moving average teacher) that made consistency *training* competitive.
- [Simplifying, Stabilizing and Scaling Continuous-Time Consistency Models (sCM)](https://arxiv.org/abs/2410.11081) — **Lu & Song (2024)** — TrigFlow parameterization; scales to 1.5B parameters and two-step ImageNet 512×512.
- [Latent Consistency Models](https://arxiv.org/abs/2310.04378) — **Luo et al. (2023)** — consistency distillation in latent space; the practical 2–8-step Stable Diffusion accelerator.
- [Mean Flows for One-Step Generative Modeling](https://arxiv.org/abs/2505.13447) — **Geng et al. (2025)** — average-velocity fields give one-step generation trained from scratch, no distillation.

## Articles / Blogs (free, no paywall)

- [Simplifying, stabilizing and scaling continuous-time consistency models](https://openai.com/index/simplifying-stabilizing-and-scaling-continuous-time-consistency-models/) — **OpenAI** — the authors' own account, with sample-quality and speed numbers.
- [Learning the integral of a diffusion model](https://sander.ai/2026/05/06/flow-maps.html) — **Sander Dieleman** — the unifying flow-map perspective; long, and worth every paragraph.
- [The paradox of diffusion distillation](https://sander.ai/2024/02/28/paradox.html) — **Sander Dieleman** — why compressing many steps into one is theoretically odd and empirically fine.

## In this platform

- Prerequisites: [Score-Based & SDE Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/score-based-and-sde-diffusion/score-based-and-sde-diffusion) · [Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques) · [Flow Matching & Rectified Flow](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/flow-matching-and-rectified-flow/flow-matching-and-rectified-flow)
- Next: [Distillation for Fast Sampling](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/distillation-for-fast-sampling/distillation-for-fast-sampling) · [Diffusion Inference Optimization](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-inference-optimization/diffusion-inference-optimization)
- Related: [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/knowledge-distillation/knowledge-distillation) (the same idea for language models) · [Evaluation of Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/evaluation-of-generative-models/evaluation-of-generative-models) (how the quality loss is measured)
- Field overview: [Diffusion Models index](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme)
