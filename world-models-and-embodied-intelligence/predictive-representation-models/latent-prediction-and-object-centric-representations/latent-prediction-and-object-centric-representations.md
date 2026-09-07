---
id: "world-models-and-embodied-intelligence/predictive-representation-models/latent-prediction-and-object-centric-representations"
topic: "Latent Prediction and Object-Centric Representations"
level: advanced
built_from: ["observation-state-action-and-partial-observability", "variational-autoencoders-vae-elbo"]
leads_to: ["jepa-foundations", "recurrent-state-space-models-and-stochastic-dynamics"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Latent Prediction and Object-Centric Representations"
minutes: 15
category: predictive-representation-models
---

# Latent Prediction and Object-Centric Representations
> Predicting the next *frame* forces a model to spend capacity on shadows, grain and texture.
> Predicting the next *latent* lets it spend capacity on what moved. **Object-centric** methods go
> one step further: instead of one flat vector per scene, they learn a **set of slots**, each bound
> to one entity — so "the ball is now behind the box" is a small change in one slot, not a global
> change in every pixel.

**Why it matters:** latent prediction is the design decision that separates a world model from a
video codec, and object-centric structure is the current best answer to the **binding problem** —
how a distributed representation refers to individual things. It is also where the honesty lies: slot
methods work beautifully on synthetic scenes and are still hard to scale to real video, which is
exactly the trade-off an interviewer will push on.

**Start here — suggested path:**

1. **Understand why latent, not pixels** — read [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman**. *What compression buys, and what information it silently throws away.*
2. **Name the problem slots solve** — read [On the Binding Problem in Artificial Neural Networks](https://arxiv.org/abs/2012.05208) — **Greff, van Steenkiste & Schmidhuber (2020)**. *Why a single vector cannot cleanly represent several objects, stated as a research programme.*
3. **Learn the mechanism** — read [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) — **Locatello et al., Google Brain (2020)**. *Iterative attention with a softmax over slots — objects compete to explain each pixel.*
4. **Watch the author** — watch [Thomas Kipf: Transformers at Work (Slot Attention section)](https://www.youtube.com/watch?v=zmZBT7E93ys) — **Zeta Alpha**. *Slot attention, video extensions, and where object-centric perception is headed.*
5. **See it survive real images** — read [Bridging the Gap to Real-World Object-Centric Learning](https://arxiv.org/abs/2209.14860) — **Seitzer et al. (2023)**. *DINOSAUR: reconstruct self-supervised features instead of pixels, and slots start working on real photographs.*

## Courses (free)

- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — the representation-learning section covers what a model should predict and why.
- [CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — slot attention and set-structured representations recur in the seminar's vision weeks.

## Videos

- [Thomas Kipf (Google Brain) — Transformers at Work](https://www.youtube.com/watch?v=zmZBT7E93ys) — **Zeta Alpha** — object-centric perception explained by one of slot attention's authors.
- [V-JEPA: Revisiting Feature Prediction for Learning Visual Representations from Video](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher** — the clearest walkthrough of predicting features rather than pixels.

## Key Papers

- [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) — **Locatello et al. (2020)** — the slot attention module: a differentiable, permutation-invariant grouping mechanism.
- [On the Binding Problem in Artificial Neural Networks](https://arxiv.org/abs/2012.05208) — **Greff, van Steenkiste & Schmidhuber (2020)** — the conceptual paper behind the whole object-centric line.
- [Conditional Object-Centric Learning from Video](https://arxiv.org/abs/2111.12594) — **Kipf et al. (2022)** — SAVi: slots tracked through time with optical-flow supervision, the video version.
- [Bridging the Gap to Real-World Object-Centric Learning](https://arxiv.org/abs/2209.14860) — **Seitzer et al. (2023)** — DINOSAUR: self-supervised features as the reconstruction target, unlocking real-world scenes.

## Articles / Blogs (free, no paywall)

- [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman (Google DeepMind)** — why nearly everything now predicts in a learned latent space.
- [Thomas Kipf — research page](https://tkipf.github.io/) — **Thomas Kipf (Google DeepMind)** — the running index of object-centric work by the person driving most of it.
- [Slot Attention reference implementation](https://github.com/google-research/google-research/tree/master/slot_attention) — **Google Research** — the original code; the iterative-attention loop is ~50 readable lines.
- [SAVi project page](https://slot-attention-video.github.io/) — **Kipf et al.** — videos of slots binding and tracking objects; the fastest way to see what "object-centric" means.

## In this platform

- Prerequisite: [Observation, State, Action and Partial Observability](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/observation-state-action-and-partial-observability/observation-state-action-and-partial-observability) · [Variational Autoencoders and the ELBO](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo)
- Next: [JEPA Foundations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/jepa-foundations/jepa-foundations)
- Related self-supervised objectives: [Teacher-Student Self-Distillation (DINO, BYOL)](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/teacher-student-self-distillation-dino-byol/teacher-student-self-distillation-dino-byol)
- Video representations elsewhere: [Video Representations and Temporal Modeling](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-representations-and-temporal-modeling/video-representations-and-temporal-modeling)
