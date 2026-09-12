---
id: "models-and-architectures/generative-model-families/diffusion-models/distillation-for-fast-sampling"
topic: "Distillation for Fast Sampling"
level: advanced
built_from: ["sampling-and-guidance-techniques", "consistency-models-and-few-step-generation"]
leads_to: ["models-and-architectures/generative-model-families/diffusion-models/diffusion-inference-optimization", "models-and-architectures/generative-model-families/diffusion-models/video-diffusion-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Distillation for Fast Sampling"
minutes: 14
category: diffusion-models
---

# Distillation for Fast Sampling
> **Distillation** trains a student network to reproduce in one or four steps what a teacher diffusion
> model does in fifty. The family splits by what the student is asked to match: the teacher's
> *trajectory* (progressive and consistency distillation), the teacher's *output distribution*
> (distribution matching distillation, DMD), or a *discriminator's* judgement of realism (adversarial
> diffusion distillation, ADD — the SDXL-Turbo recipe).

**Why it matters:** it is the difference between a 4-second and a 0.2-second image, and every
real-time product — live canvases, on-device generation, interactive video — runs a distilled model.
Interviewers probe: why halving the step count repeatedly (**progressive distillation**) works while
naively training a 1-step model does not; why **guidance must be distilled too**, since classifier-free
guidance doubles the network calls per step; and the consistent cost — distilled students lose
diversity (mode collapse toward the teacher's high-density modes) even when single-image fidelity
holds up.

**Start here — suggested path:**

1. **Understand the puzzle** — read [The paradox of diffusion distillation](https://sander.ai/2024/02/28/paradox.html) — **Sander Dieleman (Google DeepMind)**. *Why a many-step process should not compress into one step, and what the student is really learning.*
2. **Read the founding method** — [Progressive Distillation for Fast Sampling](https://arxiv.org/abs/2202.00512) — **Salimans & Ho (2022)**. *Halve the steps, retrain, repeat: 1024 → 4 steps, with the v-prediction parameterization that made it stable.*
3. **Hear it from the author** — watch [Variational Autoencoders and Diffusion Models](https://www.youtube.com/watch?v=pea3sH6orMc) — **Tim Salimans (Google DeepMind)**. *The distillation section explains the halving trick and the guidance problem live.*
4. **Compare the modern families** — [Adversarial Diffusion Distillation](https://arxiv.org/abs/2311.17042) — **Sauer et al. (2023)** versus [Distribution Matching Distillation](https://arxiv.org/abs/2311.18828) — **Yin et al. (2023)**. *Adversarial realism versus distribution matching — the two live branches.*
5. **Use one** — load an LCM-LoRA or Turbo checkpoint via the [Diffusers LCM guide](https://huggingface.co/docs/diffusers/using-diffusers/inference_with_lcm) and measure wall-clock and output variety across seeds. *The diversity cost shows up immediately in a 16-image grid.*

## Courses (free)

- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — situates distillation inside the production stack for large vision models.
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — the code path for loading and benchmarking distilled checkpoints.

## Videos

- [Variational Autoencoders and Diffusion Models (M2L summer school)](https://www.youtube.com/watch?v=pea3sH6orMc) — **Tim Salimans (Google DeepMind)** — progressive distillation from the person who invented it.

## Key Papers

- [Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512) — **Salimans & Ho (2022)** — the halving procedure and v-prediction; the ancestor of everything here.
- [On Distillation of Guided Diffusion Models](https://arxiv.org/abs/2210.03142) — **Meng et al. (2022)** — folds classifier-free guidance into the student so guidance costs nothing at inference.
- [Adversarial Diffusion Distillation (SDXL-Turbo)](https://arxiv.org/abs/2311.17042) — **Sauer, Lorenz, Blattmann & Rombach (2023)** — score distillation plus a discriminator; single-step photoreal images.
- [One-step Diffusion with Distribution Matching Distillation (DMD)](https://arxiv.org/abs/2311.18828) — **Yin et al. (2023)** — matches the teacher's *distribution* via a pair of score networks, not its trajectory.
- [LCM-LoRA: A Universal Stable-Diffusion Acceleration Module](https://arxiv.org/abs/2311.05556) — **Luo et al. (2023)** — distillation packaged as a low-rank adapter you can drop onto existing checkpoints.
- [Latent Adversarial Diffusion Distillation (LADD)](https://arxiv.org/abs/2403.12015) — **Sauer, Boesel, Dockhorn, Blattmann, Esser & Rombach (2024)** — moves the adversarial signal into latent space, which is what made turbo-style distillation scale to large transformers.

## Articles / Blogs (free, no paywall)

- [The paradox of diffusion distillation](https://sander.ai/2024/02/28/paradox.html) — **Sander Dieleman** — the conceptual map of the whole area, including why guidance distillation is separate.
- [Learning the integral of a diffusion model](https://sander.ai/2026/05/06/flow-maps.html) — **Sander Dieleman** — the 2026 flow-map framing that subsumes most distillation objectives.
- [Simplifying, stabilizing and scaling continuous-time consistency models](https://openai.com/index/simplifying-stabilizing-and-scaling-continuous-time-consistency-models/) — **OpenAI** — the strongest distillation-free-of-adversarial-loss result to date, with numbers.

## In this platform

- Prerequisites: [Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques) · [Consistency Models & Few-Step Generation](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/consistency-models-and-few-step-generation/consistency-models-and-few-step-generation)
- Next: [Diffusion Inference Optimization](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-inference-optimization/diffusion-inference-optimization) · [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/video-diffusion-models/video-diffusion-models) (where step count dominates cost)
- Related: [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation) · [LoRA & Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) (how LCM-LoRA ships)
- Field overview: [Diffusion Models index](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme)
