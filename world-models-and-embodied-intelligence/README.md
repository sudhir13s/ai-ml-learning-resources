---
id: "world-models-and-embodied-intelligence"
topic: "World Models and Embodied Intelligence"
level: advanced
built_from: ["deep-learning", "reinforcement-learning", "diffusion-models", "self-supervised-learning"]
updated: 2026-09-07
---

# World Models and Embodied Intelligence

> A **world model** is a learned internal simulator: predict what happens next, then act on the
> prediction instead of on trial and error. **Embodied intelligence** is what happens when that
> loop is closed on a body — a robot whose own actions determine its next observations. This is the
> curated shortlist of the best free resources for both; every page links its canonical home
> elsewhere in the platform rather than re-teaching it.

**Start here:** [What Is a World Model](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/what-is-a-world-model/what-is-a-world-model) for the founding idea and the 2026 landscape, then [World Model Taxonomy](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/world-model-taxonomy/world-model-taxonomy) to tell pixel, latent and JEPA-style models apart before reading anything else.

## Concept index

Each page is a self-contained resource card: a short definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### World model foundations

1. [What Is a World Model](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/what-is-a-world-model/what-is-a-world-model) — Ha & Schmidhuber, LeCun's programme, and the Genie 3 / V-JEPA 2 / Cosmos era.
2. [World Model Taxonomy](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/world-model-taxonomy/world-model-taxonomy) — generative versus latent versus predictive; simulators versus planning models.
3. [Observation, State, Action and Partial Observability](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/observation-state-action-and-partial-observability/observation-state-action-and-partial-observability) — POMDPs, belief states, and why a frame is not a state.

### Predictive representation models

4. [Latent Prediction and Object-Centric Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/latent-prediction-and-object-centric-representations/latent-prediction-and-object-centric-representations) — slot attention, the binding problem, predicting features not pixels.
5. [JEPA Foundations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/jepa-foundations/jepa-foundations) — I-JEPA, the joint-embedding predictive architecture, and why reconstruction is avoided.
6. [Video JEPA and Action-Conditioned JEPA](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/video-jepa-and-action-conditioned-jepa/video-jepa-and-action-conditioned-jepa) — V-JEPA, V-JEPA 2 and V-JEPA 2-AC for zero-shot robot planning.

### Latent dynamics

7. [Recurrent State-Space Models and Stochastic Dynamics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics/recurrent-state-space-models-and-stochastic-dynamics) — RSSM, deterministic plus stochastic latents, discrete categorical states.

### Learning and planning

8. [Imagination-Based Learning (Dreamer)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/imagination-based-learning-dreamer/imagination-based-learning-dreamer) — Dreamer v1 to v4, DayDreamer, and training a policy inside a model.
9. [Search and Rollouts (MuZero)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/search-and-rollouts-muzero/search-and-rollouts-muzero) — value-equivalent latent models, Monte Carlo tree search, the AlphaZero lineage.
10. [Model Predictive Control with Learned Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/model-predictive-control-with-learned-models/model-predictive-control-with-learned-models) — TD-MPC2, PETS, uncertainty-aware replanning.

### Video and generative world models

11. [Interactive Video and Generative Simulators](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators) — Genie 1-3, GameNGen, Oasis, Cosmos, and the Sora-as-simulator debate.

### Embodied intelligence

12. [Embodied Agents and Perception-Action Loops](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/embodied-intelligence/embodied-agents-and-perception-action-loops/embodied-agents-and-perception-action-loops) — Habitat, ManiSkill, sim-to-real and domain randomisation.
13. [Vision-Language-Action Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/embodied-intelligence/vision-language-action-models/vision-language-action-models) — RT-1/RT-2, OpenVLA, π0/π0.5, Gemini Robotics, Helix.

### Evaluation and safety

14. [Evaluating World Models: Prediction, Planning and Physical Consistency](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency) — Physics-IQ, IntPhys 2, Physion, and the failure modes that matter.

### Spatial and physical world models

15. [Spatial Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/spatial-and-physical-world-models/spatial-representations/spatial-representations) — scene graphs, voxels, neural fields, Gaussian splatting, bird's-eye-view features.
16. [3D Scene Understanding](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/spatial-and-physical-world-models/3d-scene-understanding/3d-scene-understanding) — VGGT, DUSt3R, feed-forward geometry, and the VSI-Bench spatial-reasoning gap.
17. [Object Permanence](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/spatial-and-physical-world-models/object-permanence/object-permanence) — occlusion, tracking through occlusion, IntPhys 2, and the developmental evidence.
18. [Intuitive Physics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/spatial-and-physical-world-models/intuitive-physics/intuitive-physics) — Physion, Physics-IQ, V-JEPA surprise, graph-network simulators, Genesis.
19. [Causal World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/spatial-and-physical-world-models/causal-world-models/causal-world-models) — interventions versus predictions, counterfactual rollouts, the Schölkopf and Bengio programme.

### Memory and cognitive maps

20. [Episodic World Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/memory-and-cognitive-maps/episodic-world-memory/episodic-world-memory) — Genie 3's minutes-scale consistency, WorldMem, diffusion forcing, MERLIN.
21. [Spatial Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/memory-and-cognitive-maps/spatial-memory/spatial-memory) — learned maps, Active Neural SLAM, Habitat navigation, maps that emerge unbidden.
22. [Cognitive Maps](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/memory-and-cognitive-maps/cognitive-maps/cognitive-maps) — Tolman, place and grid cells, successor representations, the Tolman-Eichenbaum Machine.
23. [Persistent Environment State](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/memory-and-cognitive-maps/persistent-environment-state/persistent-environment-state) — state that survives episodes, object-level persistence, WorldScore.

## Courses (free)

- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — the closest thing to a full course on learned models and control; lectures 10-12 are the core of this section.
- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — the best single overview of what a learned model is *for*.
- [CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar that hosts the representation-learning-to-world-modeling talks as they happen.
- [Embodied AI Workshop](https://embodied-ai.org/) — **CVPR Embodied AI community** — the annual index of embodied benchmarks, challenges and recorded talks.

## Videos

- [World Models](https://www.youtube.com/watch?v=dPsXxLyqpfs) — **Yannic Kilcher** — the founding architecture explained end to end.
- [Dream to Control: Learning Behaviors by Latent Imagination](https://www.youtube.com/watch?v=BDxRNnhPTlU) — **Danijar Hafner** — the Dreamer line from its author.
- [Objective-Driven AI](https://www.youtube.com/watch?v=MiqLoAZFRSE) — **Harvard CMSA (Yann LeCun)** — the research programme behind JEPA and AMI Labs.
- [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Fruchter, Parker-Holder)** — the 2025 interactive-simulator jump, from the builders.

## Key Papers

- [World Models](https://arxiv.org/abs/1803.10122) — **Ha & Schmidhuber (2018)** — the founding paper; an agent trained inside its own dream.
- [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf) — **Yann LeCun (2022)** — the architecture proposal that set the field's agenda.
- [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) — **Hafner et al. (2023; Nature 2025)** — DreamerV3: one configuration, 150-plus tasks.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Meta FAIR (2025)** — video pretraining that transfers to zero-shot robot planning.
- [Understanding World or Predicting Future? A Comprehensive Survey of World Models](https://arxiv.org/abs/2411.14499) — **Ding et al. (2024)** — the reference taxonomy for the whole area.

## Articles / Blogs

- [World Models (interactive)](https://worldmodels.github.io/) — **David Ha & Jürgen Schmidhuber** — still the clearest single explanation, with playable figures.
- [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind** — the current capability frontier, limitations included.
- [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman** — why prediction moved out of pixel space.
- [The Promise of Generalist Robotic Policies](https://sergeylevine.substack.com/p/the-promise-of-generalist-robotic) — **Sergey Levine** — the embodied half, assessed honestly.

## Books (free, with chapters)

- [*Reinforcement Learning: An Introduction* — Ch. 8 "Planning and Learning with Tabular Methods"](http://incompleteideas.net/book/the-book-2nd.html) — **Sutton & Barto** — Dyna: the ancestor of every learned world model.
- [*Algorithms for Decision Making*](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — free textbook on planning, belief states and decision-making under uncertainty.

## In this platform

- Canonical homes this section links rather than duplicates: [Model-Based RL](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl) · [Markov Decision Processes](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/foundations/markov-decision-processes/markov-decision-processes) · [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/video-diffusion-models/video-diffusion-models) · [Teacher-Student Self-Distillation (DINO, BYOL)](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/teacher-student-self-distillation-dino-byol/teacher-student-self-distillation-dino-byol)
- Perception and video: [Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/readme) · [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme)
- The biological counterpart: [Predictive Coding](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/predictive-coding/predictive-coding) · [Memory Systems, Hippocampus and Replay](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/memory-systems-hippocampus-replay/memory-systems-hippocampus-replay)
- Sequence and generative building blocks: [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru) · [Variational Autoencoders and the ELBO](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo)
