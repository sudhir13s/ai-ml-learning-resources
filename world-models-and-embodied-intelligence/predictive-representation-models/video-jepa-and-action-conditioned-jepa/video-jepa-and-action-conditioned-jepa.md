---
id: "world-models-and-embodied-intelligence/predictive-representation-models/video-jepa-and-action-conditioned-jepa"
topic: "Video JEPA and Action-Conditioned JEPA"
level: advanced
built_from: ["jepa-foundations"]
leads_to: ["model-predictive-control-with-learned-models", "vision-language-action-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Video JEPA and Action-Conditioned JEPA"
minutes: 15
category: predictive-representation-models
---

# Video JEPA and Action-Conditioned JEPA
> V-JEPA applies the joint-embedding predictive architecture (JEPA) objective to video: mask a
> spatio-temporal block, predict its *features* from the rest. V-JEPA 2 scales that to over a
> million hours of internet video; **V-JEPA 2-AC** then post-trains an **action-conditioned** head
> on under 62 hours of unlabelled robot video — and plans real pick-and-place motions toward an
> image goal, zero-shot, on robot arms it has never seen.

**Why it matters:** this is the strongest current evidence that a passively-trained video model can
become a *controllable* world model with a tiny amount of interaction data — the sample-efficiency
argument that makes world models interesting for robotics at all. The interview angle is the two-stage
split: **action-free pretraining** buys physics and object dynamics from cheap video; **action
conditioning** buys controllability from expensive robot data, and only the second stage needs a robot.

**Start here — suggested path:**

1. **See the video objective** — read [Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471) — **Bardes et al., Meta FAIR (2024)**. *V-JEPA: masked feature prediction over spacetime blocks, and why it beats pixel reconstruction on motion tasks.*
2. **Watch it explained** — watch [V-JEPA (Explained)](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher**. *Architecture, masking, and the evaluation protocol, walked through slowly.*
3. **Read the 2025 scale-up** — read [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al., Meta FAIR (2025)**. *One million-plus hours of video, then a 62-hour action-conditioned post-train that plans on Franka arms.*
4. **Run it** — clone [facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2) — **Meta FAIR**. *Checkpoints, evaluation code, and the action-conditioned planning loop in PyTorch.*
5. **Check it against physics** — read [IntPhys 2](https://arxiv.org/abs/2506.09849) — **Bordes et al., Meta FAIR (2025)**. *The companion benchmark: does the model actually know that occluded objects persist?*

## Courses (free)

- [CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar's video and world-modeling talks track each V-JEPA release closely.
- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — the planning-with-a-learned-model half that V-JEPA 2-AC plugs into.

## Videos

- [V-JEPA: Revisiting Feature Prediction (Explained)](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher** — the reference walkthrough of the video JEPA objective.
- [Objective-Driven AI](https://www.youtube.com/watch?v=MiqLoAZFRSE) — **Harvard CMSA (Yann LeCun)** — the research programme these models are executing, from its author.

## Key Papers

- [Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471) — **Bardes et al. (2024)** — V-JEPA; establishes that feature prediction alone learns motion-sensitive video representations.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al. (2025)** — scale, plus the action-conditioned world model used for zero-shot robot planning.
- [IntPhys 2: Benchmarking Intuitive Physics Understanding In Complex Synthetic Environments](https://arxiv.org/abs/2506.09849) — **Bordes et al. (2025)** — the violation-of-expectation benchmark released alongside it; most models score near chance.
- [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) — **Assran et al. (2023)** — the image-domain predecessor whose recipe V-JEPA inherits.

## Articles / Blogs (free, no paywall)

- [facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2) — **Meta FAIR** — official code, checkpoints and the action-conditioned planning example (Meta's blog posts block automated fetches; the repository is the citable primary source).
- [facebookresearch/jepa](https://github.com/facebookresearch/jepa) — **Meta FAIR** — the original V-JEPA repository, useful for the masking-schedule details.
- [facebookresearch/IntPhys2](https://github.com/facebookresearch/IntPhys2) — **Meta FAIR** — the benchmark code, so the physics claims can be reproduced rather than believed.

## In this platform

- Prerequisite: [JEPA Foundations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/jepa-foundations/jepa-foundations)
- Where the planning happens: [Model Predictive Control with Learned Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/model-predictive-control-with-learned-models/model-predictive-control-with-learned-models)
- Where it is evaluated: [Evaluating World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency)
- Canonical home elsewhere: [Self-Supervised Video Pretraining (VideoMAE)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/self-supervised-video-pretraining-videomae/self-supervised-video-pretraining-videomae) · [Video Transformers (TimeSformer, ViViT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-transformers-timesformer-vivit/video-transformers-timesformer-vivit)
