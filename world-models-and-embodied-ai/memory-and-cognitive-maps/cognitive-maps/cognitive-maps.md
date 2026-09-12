---
id: "world-models-and-embodied-ai/memory-and-cognitive-maps/cognitive-maps"
topic: "Cognitive Maps"
level: advanced
built_from: ["world-models-and-embodied-ai/memory-and-cognitive-maps/spatial-memory", "memory-systems-hippocampus-replay"]
leads_to: ["world-models-and-embodied-ai/memory-and-cognitive-maps/persistent-environment-state", "world-models-and-embodied-ai/spatial-and-physical-world-models/causal-world-models"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Cognitive Maps"
minutes: 17
category: memory-and-cognitive-maps
---

# Cognitive Maps
> A **cognitive map** is a relational model of an environment — not a photograph of it. Tolman
> argued in 1948 that rats build one; place and grid cells later showed where. The modern claim is
> stronger and more useful to machine learning: the same machinery maps **any** relational
> structure, spatial or not. The one sentence: **a cognitive map factorises "what things are"
> from "how they are arranged", so structure learned in one environment transfers to the next.**

**Why it matters:** this is the neuroscience the world-model field keeps rediscovering. The
**successor representation (SR)** explains place-cell firing as a predictive map, and it is a
reinforcement-learning object — a discounted expectation of future state occupancy — which is why
it transfers cleanly between the two fields. The **Tolman-Eichenbaum Machine (TEM)** derives grid,
band, border and place cells from one generalisation objective, and its transformer variant links
that directly to attention. Interviewers probe the difference between **model-free values, the
successor representation, and a full model**. The underrated point: **the SR sits between them —
it re-plans instantly for a moved reward, but not for a moved wall.**

**Start here — suggested path:**

1. **Read the original claim** — read [Cognitive Maps in Rats and Men](http://psychclassics.yorku.ca/Tolman/Maps/maps.htm) — **Edward C. Tolman (1948)**. *Free full text; the experiments that made "map" rather than "stimulus-response chain" the right word.*
2. **See the cells** — watch [Nobel Lecture: grid cells and the entorhinal map of space](https://www.youtube.com/watch?v=nm7ONLCNLP8) — **Edvard I. Moser (Uppsala universitet)**. *Place cells, grid cells and the coordinate system they form, from the person who found them.*
3. **Get the computational bridge** — read [The hippocampus as a predictive map](https://www.biorxiv.org/content/10.1101/097170v3) — **Stachenfeld, Botvinick & Gershman (2017)**. *Place fields as a successor representation; the paper that made this a reinforcement-learning topic.*
4. **See one model produce every cell type** — read [The Tolman-Eichenbaum Machine](https://www.biorxiv.org/content/10.1101/770495v2) — **Whittington, Muller, Mark, Chen, Barry, Burgess & Behrens (2020)**. *Factorise structure from sensory input, and grid, band, border and place cells fall out of the same objective.*
5. **Connect it to modern architectures** — skim [Relating transformers to models and neural representations of the hippocampal formation](https://arxiv.org/abs/2112.04035) — **Whittington, Warren & Behrens (2021)**. *Transformer with recurrent positional encoding equals TEM; attention and hippocampal indexing as the same operation.*

## Courses (free)

- [Neuromatch Academy: Computational Neuroscience](https://compneuro.neuromatch.io/) — **Neuromatch** — free tutorials with runnable notebooks; the hippocampus, reinforcement learning and latent-state modules are the relevant ones.
- [RES.9-003 Brains, Minds and Machines Summer Course](https://ocw.mit.edu/courses/res-9-003-brains-minds-and-machines-summer-course-summer-2015/) — **MIT OpenCourseWare (CBMM)** — lectures connecting spatial coding to general relational reasoning.

## Videos

- [Nobel Lecture in Uppsala](https://www.youtube.com/watch?v=nm7ONLCNLP8) — **Edvard I. Moser (Uppsala universitet)** — the discovery narrative, with the recordings that make grid structure undeniable.
- [Grid Cells and the Entorhinal Map of Space](https://www.youtube.com/watch?v=Z550DeGoTgU) — **Edvard Moser (UC Irvine Center for the Neurobiology of Learning and Memory)** — the longer technical keynote, including remapping.
- [Grid Cells and Cortical Maps for Space](https://www.youtube.com/watch?v=BEScyWMvSKk) — **May-Britt Moser (Videnskabernes Selskab)** — the complementary half of the same programme, on modules and scale.

## Key Papers

- [The hippocampus as a predictive map](https://www.biorxiv.org/content/10.1101/097170v3) — **Stachenfeld, Botvinick & Gershman (2017)** — the successor-representation account of place and grid coding.
- [The Tolman-Eichenbaum Machine: Unifying space and relational memory through generalisation in the hippocampal formation](https://www.biorxiv.org/content/10.1101/770495v2) — **Whittington et al. (2020)** — one objective, many observed cell types, spatial and non-spatial alike.
- [Relating transformers to models and neural representations of the hippocampal formation](https://arxiv.org/abs/2112.04035) — **Whittington, Warren & Behrens (2021)** — the explicit TEM-to-transformer correspondence.
- [What is a cognitive map? Organising knowledge for flexible behaviour](https://www.biorxiv.org/content/10.1101/365593v1) — **Behrens, Muller, Whittington, Mark, Baram, Stachenfeld & Kurth-Nelson (2018)** — the review that generalised maps beyond physical space.
- [Predictive representations: building blocks of intelligence](https://arxiv.org/abs/2402.06590) — **Carvalho, Tomov, de Cothi, Barry & Gershman (2024)** — the current synthesis of successor representations across reinforcement learning and neuroscience.
- [Vector-based navigation using grid-like representations in artificial agents](https://www.nature.com/articles/s41586-018-0102-6) — **Banino et al., DeepMind (Nature, 2018)** — grid-like units emerging in a trained network, then used for shortcut navigation.
- [Emergence of Maps in the Memories of Blind Navigation Agents](https://arxiv.org/abs/2301.13261) — **Wijmans et al. (2023)** — the machine-side echo: map-like memory without any map module.

## Articles / Blogs (free, no paywall)

- [The Successor Representation: Its Computational Logic and Neural Substrates](https://gershmanlab.com/pubs/Gershman18.pdf) — **Samuel Gershman (Harvard)** — free PDF; the clearest short derivation of the successor representation and what it does and does not buy.
- [Cognitive Maps in Rats and Men](http://psychclassics.yorku.ca/Tolman/Maps/maps.htm) — **Edward C. Tolman (1948)**, hosted by *Classics in the History of Psychology* — the founding paper, free and short.

## Books (free, with chapters)

- [*Reinforcement Learning: An Introduction* — Ch. 17 "Frontiers"](http://incompleteideas.net/book/the-book-2nd.html) — **Sutton & Barto** — free textbook; predictive representations and options, the reinforcement-learning side of this page.

## In this platform

- Previous: [Spatial Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/spatial-memory/spatial-memory) · next: [Persistent Environment State](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/persistent-environment-state/persistent-environment-state)
- Canonical home for the biology: [Memory Systems, Hippocampus and Replay](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuroscience-and-brain-inspired-ai/memory-systems-hippocampus-replay/memory-systems-hippocampus-replay) · [Neural Coding](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuroscience-and-brain-inspired-ai/neural-coding/neural-coding) · [Predictive Coding](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuroscience-and-brain-inspired-ai/predictive-coding/predictive-coding)
- The reinforcement-learning side: [Model-Based RL](/ai-ml/ai-ml-learning-resources/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl) · [Markov Decision Processes](/ai-ml/ai-ml-learning-resources/reinforcement-learning/foundations/markov-decision-processes/markov-decision-processes)
- Related in this section: [Causal World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/causal-world-models/causal-world-models) · [World Model Taxonomy](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/world-model-foundations/world-model-taxonomy/world-model-taxonomy)
