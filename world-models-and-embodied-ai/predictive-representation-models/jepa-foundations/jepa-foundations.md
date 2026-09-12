---
id: "world-models-and-embodied-ai/predictive-representation-models/jepa-foundations"
topic: "JEPA Foundations"
level: advanced
built_from: ["latent-prediction-and-object-centric-representations", "world-model-taxonomy"]
leads_to: ["world-models-and-embodied-ai/predictive-representation-models/video-jepa-and-action-conditioned-jepa"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "JEPA Foundations"
minutes: 15
category: predictive-representation-models
---

# JEPA Foundations
> A **joint-embedding predictive architecture (JEPA)** predicts the *representation* of a masked
> part of the input from the representation of the visible part — never the pixels. Two encoders,
> one predictor, and a loss computed entirely in embedding space. The point is not efficiency; it is
> that a model should not be forced to predict what is fundamentally unpredictable.

**Why it matters:** JEPA is Yann LeCun's answer to why generative pretraining does not produce
world understanding — and, since he founded AMI Labs in December 2025 to build world models, it is
the most consequential architectural bet in the field. The interview substance is the trade-off:
dropping reconstruction removes the pixel-level supervision signal, which raises the **representation
collapse** risk that the target encoder's exponential moving average (EMA) and masking strategy exist
to control.

**Start here — suggested path:**

1. **Get the architecture in one picture** — read [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) — **Assran et al., Meta FAIR (2023)**. *I-JEPA: predict masked-block representations from a context block; no pixel decoder anywhere.*
2. **Read the manifesto behind it** — skim [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf) — **Yann LeCun (2022)**. *Where JEPA sits inside a full agent: configurator, perception, world model, cost.*
3. **Watch the argument delivered** — watch [Objective-Driven AI](https://www.youtube.com/watch?v=MiqLoAZFRSE) — **Harvard CMSA (Yann LeCun)**. *Why predicting in representation space is the only tractable objective for high-dimensional futures.*
4. **See a paper walkthrough** — watch [V-JEPA (Explained)](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher**. *Includes a recap of the original JEPA idea before moving to video.*
5. **Read the code** — browse [facebookresearch/ijepa](https://github.com/facebookresearch/ijepa) — **Meta FAIR**. *The masking strategy and the EMA target encoder are ~100 lines; reading them removes the mystery.*

## Courses (free)

- [NYU Deep Learning (DLSP21)](https://atcold.github.io/NYU-DLSP21/) — **Yann LeCun & Alfredo Canziani** — free lectures and notebooks; the energy-based and self-supervised lectures are the direct ancestors of JEPA.
- [CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the representation-learning-to-world-modeling seminar track keeps pace with each JEPA release.

## Videos

- [Objective-Driven AI](https://www.youtube.com/watch?v=MiqLoAZFRSE) — **Harvard CMSA (Yann LeCun)** — the primary source for the JEPA design rationale.
- [V-JEPA: Revisiting Feature Prediction (Explained)](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher** — a technical read-through, including what could collapse and why it does not.
- [From Machine Learning to Autonomous Intelligence](https://www.youtube.com/watch?v=pd0JmT6rYcI) — **LMU München (Yann LeCun)** — more time on energy-based models and hierarchical JEPA than the shorter talks.

## Key Papers

- [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) — **Assran et al. (2023)** — I-JEPA, the reference implementation of the idea.
- [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf) — **Yann LeCun (2022)** — the position paper; JEPA is proposed here before any JEPA model existed.
- [Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471) — **Bardes et al., Meta FAIR (2024)** — V-JEPA: the same objective applied to video, and the first strong evidence it scales.

## Articles / Blogs (free, no paywall)

- [facebookresearch/ijepa](https://github.com/facebookresearch/ijepa) — **Meta FAIR** — official code and checkpoints (Meta's own blog posts block automated fetches, so the repository and paper are the citable primary sources).
- [facebookresearch/jepa](https://github.com/facebookresearch/jepa) — **Meta FAIR** — the V-JEPA repository; the training recipe and masking schedules are documented in the README.
- [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman** — the complementary view from the generative side of the same trade-off.

## In this platform

- Prerequisite: [World Model Taxonomy](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/world-model-foundations/world-model-taxonomy/world-model-taxonomy) · [Latent Prediction and Object-Centric Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/predictive-representation-models/latent-prediction-and-object-centric-representations/latent-prediction-and-object-centric-representations)
- Next: [Video JEPA and Action-Conditioned JEPA](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/predictive-representation-models/video-jepa-and-action-conditioned-jepa/video-jepa-and-action-conditioned-jepa)
- Canonical home for the collapse-avoidance machinery: [Teacher-Student Self-Distillation (DINO, BYOL)](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/teacher-student-self-distillation-dino-byol/teacher-student-self-distillation-dino-byol) · [Contrastive Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning)
