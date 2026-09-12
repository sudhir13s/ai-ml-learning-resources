---
id: "world-models-and-embodied-ai/spatial-and-physical-world-models/causal-world-models"
topic: "Causal World Models"
level: advanced
built_from: ["world-models-and-embodied-ai/spatial-and-physical-world-models/intuitive-physics", "causal-inference"]
leads_to: ["world-models-and-embodied-ai/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency", "world-models-and-embodied-ai/memory-and-cognitive-maps/cognitive-maps"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Causal World Models"
minutes: 18
category: spatial-and-physical-world-models
---

# Causal World Models
> A predictive model answers "what comes next given this history?" A **causal** model answers
> "what would come next if I intervened?" — a different question, needing a different object.
> Causal world models learn variables and mechanisms that stay valid when you reach in and change
> something, which is exactly the situation an agent is in every time it acts. The one sentence:
> **prediction is about observed distributions; agency is about interventional ones.**

**Why it matters:** Richens and Everitt proved a sharp result in 2024 — **any agent robust to a
broad class of distribution shifts has already learned an approximate causal model**, so causality
is not optional decoration on a world model, it is what generalisation costs. This is Bernhard
Schölkopf's **causal representation learning** programme and Yoshua Bengio's **independent
mechanisms** line meeting the world-model literature. Interviewers probe the intervention-versus-
prediction distinction and the identifiability problem: **you cannot in general recover causal
variables from passive observation alone** — you need interventions, temporal structure or
grouping assumptions.

**Start here — suggested path:**

1. **Get the programme** — read [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107) — **Schölkopf, Locatello, Bauer, Ke, Kalchbrenner, Goyal & Bengio (2021)**. *The agenda: recover causal variables from low-level observation, and why independent mechanisms matter.*
2. **Hear it from the source** — watch [Causality — MLSS Tübingen](https://www.youtube.com/watch?v=KsbftkwZTq4) — **Bernhard Schölkopf & Dominik Janzing (Max Planck Institute for Intelligent Systems)**. *Structural causal models, interventions and the independence of cause and mechanism, taught properly.*
3. **See why agents need it** — read [Robust agents learn causal world models](https://arxiv.org/abs/2402.10877) — **Richens & Everitt, Google DeepMind (ICLR 2024)**. *The theorem: robustness to distribution shift implies an approximate causal model of the data-generating process.*
4. **See counterfactual rollouts in practice** — read [Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search](https://arxiv.org/abs/1811.06272) — **Buesing, Weber, Zwols et al., DeepMind (2018)**. *Re-running past episodes under different actions with the noise held fixed — the counterfactual as a data source.*
5. **Meet the benchmark** — skim [CausalWorld: A Robotic Manipulation Benchmark for Causal Structure and Transfer Learning](https://arxiv.org/abs/2010.04296) — **Ahmed, Träuble, Goyal et al. (2020)**. *Interventions on masses, sizes and colours you can actually run, so the claim becomes testable.*

## Courses (free)

- [Introduction to Causal Inference](https://www.bradyneal.com/causal-inference-course) — **Brady Neal** — a complete free course with videos, notes and exercises; the fastest path from association to intervention to counterfactual.
- [CS 285: Deep Reinforcement Learning](http://rail.eecs.berkeley.edu/deeprlcourse/) — **UC Berkeley (Sergey Levine)** — the model-learning and offline-reinforcement-learning lectures, where confounding and distribution shift bite hardest.

## Videos

- [Causality 1 — MLSS 2013 Tübingen](https://www.youtube.com/watch?v=KsbftkwZTq4) — **Bernhard Schölkopf & Dominik Janzing (Max Planck Institute for Intelligent Systems)** — the tutorial that most later talks compress.
- [Towards Neural Nets for Conscious Processing and Causal Reasoning](https://www.youtube.com/watch?v=psfh1fk2Qig) — **Yoshua Bengio** — the sparse-mechanism and attention-over-modules argument, from its author.

## Key Papers

- [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107) — **Schölkopf et al. (2021)** — the reference statement of the problem and its open questions.
- [Causality for Machine Learning](https://arxiv.org/abs/1911.10500) — **Bernhard Schölkopf (2019)** — the shorter, sharper essay; independent causal mechanisms and what they buy for transfer.
- [Robust agents learn causal world models](https://arxiv.org/abs/2402.10877) — **Richens & Everitt (2024)** — the formal link between robustness and causal structure.
- [Recurrent Independent Mechanisms](https://arxiv.org/abs/1909.10893) — **Goyal, Lamb, Hoffmann et al. (2019)** — dynamics factored into sparsely interacting modules, so an intervention touches few of them.
- [A Meta-Transfer Objective for Learning to Disentangle Causal Mechanisms](https://arxiv.org/abs/1901.10912) — **Bengio, Deleu, Rahaman et al. (2019)** — adaptation speed after a distribution change as a signal for the correct causal direction.
- [Learning Neural Causal Models from Unknown Interventions](https://arxiv.org/abs/1910.01075) — **Ke, Bilaniuk, Goyal et al. (2019)** — structure learning when you know an intervention happened but not where.
- [Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search](https://arxiv.org/abs/1811.06272) — **Buesing et al. (2018)** — structural causal models used as the world model, giving counterfactual rollouts.
- [Contrastive Learning of Structured World Models](https://arxiv.org/abs/1911.12247) — **Kipf, van der Pol & Welling (2019)** — object-factored latent dynamics; the practical route to intervenable variables.
- [Systematic Evaluation of Causal Discovery in Visual Model Based Reinforcement Learning](https://arxiv.org/abs/2107.00848) — **Ke, Didolkar, Mittal et al. (2021)** — an honest measurement of how little current agents recover.
- [CausalWorld: A Robotic Manipulation Benchmark for Causal Structure and Transfer Learning](https://arxiv.org/abs/2010.04296) — **Ahmed et al. (2020)** — the simulator built for interventional evaluation.

## Articles / Blogs (free, no paywall)

- [Simulation as an engine of physical scene understanding](https://doi.org/10.1073/pnas.1306572110) — **Battaglia, Hamrick & Tenenbaum (PNAS, 2013)** — the human baseline: mental simulation used to answer intervention-style questions.
- [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman** — why the variables you model determine what interventions are even expressible.

## Books (free, with chapters)

- [*Elements of Causal Inference: Foundations and Learning Algorithms*](https://mitp-content-server.mit.edu/books/content/sectbyfn?collid=books_pres_0&id=11283&fn=11283.pdf) — **Peters, Janzing & Schölkopf** — free full PDF from MIT Press; Chapters 2 and 6 are the ones a world-model reader needs.
- [*Algorithms for Decision Making* — Part IV "Model Uncertainty"](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — free textbook; acting when the model itself may be wrong.

## In this platform

- Previous: [Intuitive Physics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/intuitive-physics/intuitive-physics) · sub-area start: [Spatial Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/spatial-representations/spatial-representations)
- Canonical home elsewhere: [Causal Inference](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/causal-inference/causal-inference) · [Model-Based RL](/ai-ml/ai-ml-learning-resources/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl) · [Markov Decision Processes](/ai-ml/ai-ml-learning-resources/reinforcement-learning/foundations/markov-decision-processes/markov-decision-processes)
- Where it is tested: [Evaluating World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency) · [Search and Rollouts (MuZero)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/learning-and-planning/search-and-rollouts-muzero/search-and-rollouts-muzero)
- Structure elsewhere in the estate: [Cognitive Maps](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/cognitive-maps/cognitive-maps)
