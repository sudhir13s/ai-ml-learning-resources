---
id: "world-models-and-embodied-ai/memory-and-cognitive-maps/spatial-memory"
topic: "Spatial Memory"
level: advanced
built_from: ["world-models-and-embodied-ai/memory-and-cognitive-maps/episodic-world-memory", "world-models-and-embodied-ai/spatial-and-physical-world-models/3d-scene-understanding"]
leads_to: ["world-models-and-embodied-ai/memory-and-cognitive-maps/cognitive-maps", "world-models-and-embodied-ai/embodied-intelligence/embodied-agents-and-perception-action-loops"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Spatial Memory"
minutes: 16
category: memory-and-cognitive-maps
---

# Spatial Memory
> **Spatial memory** is what an agent keeps about places it has been: a metric map, a learned
> feature grid, a topological graph of views, or nothing but a recurrent state that happens to
> encode geometry. Classical simultaneous localisation and mapping (SLAM) builds the map by
> optimisation; learned agents build one because navigation forces them to. The one sentence:
> **a navigating agent needs an allocentric store, and if you do not give it one it will grow a
> partial one inside its hidden state.**

**Why it matters:** the strongest evidence is negative — **blind navigation agents**, given only
touch and self-motion, developed map-like memory anyway (ICLR 2023 Outstanding Paper). On the
engineering side **Active Neural SLAM** and the **Habitat** stack showed that an explicit
differentiable map beats end-to-end recurrence on long-horizon navigation, and 2025's video world
models rediscovered the same lesson as **geometry-grounded long-term memory**. Interviewers probe
metric versus topological maps and the **loop-closure** problem. The underrated failure mode:
**drift** — a map that is locally perfect and globally inconsistent, which no per-step loss sees.

**Start here — suggested path:**

1. **Learn the classical problem** — watch [Introduction to SLAM](https://www.youtube.com/watch?v=0I30M6yTklo) — **Cyrill Stachniss (University of Bonn)**. *What a map is, why localisation and mapping are one joint problem, and where uncertainty enters.*
2. **See the learned map** — read [Cognitive Mapping and Planning for Visual Navigation](https://arxiv.org/abs/1702.03920) — **Gupta, Davidson, Levine, Sukthankar & Malik (2017)**. *A differentiable egocentric map plus a planner, trained end to end.*
3. **See it beat end-to-end recurrence** — read [Learning to Explore using Active Neural SLAM](https://arxiv.org/abs/2004.05155) — **Chaplot, Gandhi, Gupta, Gupta & Salakhutdinov (2020)**. *Modular map-build, global policy, local policy — the design most embodied stacks still copy.*
4. **See maps appear unbidden** — read [Emergence of Maps in the Memories of Blind Navigation Agents](https://arxiv.org/abs/2301.13261) — **Wijmans, Datta, Emmons et al. (ICLR 2023)**. *No vision, no map module, yet probing the memory recovers occupancy and collision structure.*
5. **See the 2025 video-model version** — read [Video World Models with Long-term Spatial Memory](https://arxiv.org/abs/2506.05284) — **Wu, Zhang, Chen et al. (2025)**. *Geometry-anchored memory so a generated scene survives leaving and returning.*

## Courses (free)

- [Mobile Robotics and SLAM lectures](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — **Cyrill Stachniss (University of Bonn)** — the full free SLAM course: filters, graph optimisation, loop closure, in order.
- [Online training: mobile robotics](https://www.ipb.uni-bonn.de/online-training-robotics/index.html) — **StachnissLab, University of Bonn** — the accompanying exercises and slides.
- [Embodied AI Workshop](https://embodied-ai.org/) — **CVPR Embodied AI community** — the annual index of navigation benchmarks, challenge results and recorded talks.

## Videos

- [Introduction to SLAM](https://www.youtube.com/watch?v=0I30M6yTklo) — **Cyrill Stachniss** — the clearest single hour on what a map costs and why drift happens.
- [MIT Robotics — From SLAM to Spatial AI](https://www.youtube.com/watch?v=BRRtlR0C_CY) — **Andrew Davison (Imperial College London)** — the argument that the map representation should be chosen by the downstream task.

## Key Papers

- [Cognitive Mapping and Planning for Visual Navigation](https://arxiv.org/abs/1702.03920) — **Gupta et al. (2017)** — the differentiable mapper-planner that started the learned-map line.
- [Neural Map: Structured Memory for Deep Reinforcement Learning](https://arxiv.org/abs/1702.08360) — **Parisotto & Salakhutdinov (2017)** — a spatially structured write-and-read memory rather than a flat recurrent state.
- [Learning to Explore using Active Neural SLAM](https://arxiv.org/abs/2004.05155) — **Chaplot et al. (2020)** — modular mapping plus hierarchical policies; still a strong baseline.
- [Emergence of Maps in the Memories of Blind Navigation Agents](https://arxiv.org/abs/2301.13261) — **Wijmans et al. (2023)** — map-like structure emerging from navigation pressure alone.
- [Habitat: A Platform for Embodied AI Research](https://arxiv.org/abs/1904.01201) — **Savva, Kadian, Maksymets et al. (2019)** — the simulator that made navigation memory measurable at scale.
- [Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots](https://arxiv.org/abs/2310.13724) — **Puig, Undersander, Szot et al. (2023)** — the current version, with humans in the scene and longer horizons.
- [Video World Models with Long-term Spatial Memory](https://arxiv.org/abs/2506.05284) — **Wu et al. (2025)** — spatial memory rediscovered inside generative world models.
- [FutureMapping: The Computational Structure of Spatial AI Systems](https://arxiv.org/abs/1803.11288) — **Andrew Davison (2018)** — the position paper on what the map should be once learning is available.
- [Vector-based navigation using grid-like representations in artificial agents](https://www.nature.com/articles/s41586-018-0102-6) — **Banino, Barry, Uria et al., DeepMind (Nature, 2018)** — grid-like units emerging in a navigating network, and the vector-navigation ability they support.

## Articles / Blogs (free, no paywall)

- [AI Habitat](https://aihabitat.org/) — **Meta AI and collaborators** — simulator, datasets, tasks and baselines; the fastest route to running a navigation-memory experiment.

## Books (free, with chapters)

- [*Algorithms for Decision Making* — Part II "Sequential Problems" and Part V "State Uncertainty"](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — free textbook; belief states and mapping under uncertainty, stated formally.

## In this platform

- Previous: [Episodic World Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/episodic-world-memory/episodic-world-memory) · next: [Cognitive Maps](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/cognitive-maps/cognitive-maps)
- Where it is used: [Embodied Agents and Perception-Action Loops](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/embodied-intelligence/embodied-agents-and-perception-action-loops/embodied-agents-and-perception-action-loops) · [Vision-Language-Action Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/embodied-intelligence/vision-language-action-models/vision-language-action-models)
- Perception it depends on: [3D Scene Understanding](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/3d-scene-understanding/3d-scene-understanding) · [3D and Depth Estimation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/3d-and-depth-estimation/3d-and-depth-estimation)
- The brain's version: [Memory Systems, Hippocampus and Replay](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuroscience-and-brain-inspired-ai/memory-systems-hippocampus-replay/memory-systems-hippocampus-replay)
