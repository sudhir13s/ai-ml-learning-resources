---
id: "20-neuroscience/connectomics"
topic: "Connectomics"
parent: "20-neuroscience"
level: intermediate
built_from: ["biological-neurons", "graph-theory"]
interview_frequency: low
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Connectomics"
minutes: 10
category: neuroscience-and-brain-inspired-ai
---

# Connectomics
> Mapping the brain's complete wiring diagram — the **connectome** — neuron by neuron, synapse by
> synapse. From the 302-neuron worm (*C. elegans*, the first complete connectome) through the 2024
> 140,000-neuron adult fruit-fly brain to the 2025 cubic-millimetre of mouse visual cortex
> (200,000 cells, half a billion synapses), connectomics reconstructs neural circuits from electron
> microscopy using large-scale ML for image segmentation and synapse detection.

**Why it matters:** connectomics is both a data-engineering / computer-vision triumph (petabyte EM
volumes segmented by deep nets) and the structural ground truth for everything else in this section.
The interview-relevant angles: (1) it's a massive ML application — 3D segmentation at scale; (2) the
graph it produces is what brain-inspired architectures abstract; (3) "wiring ≠ function" is the
honest caveat — a static map doesn't give you the dynamics.

**Start here — suggested path:**

1. **Get the vision** — watch [I am my connectome (TED)](https://www.youtube.com/watch?v=L74TEED6fzw). *Why a wiring diagram might matter — Sebastian Seung's case.*
2. **Go deeper** — watch [Connectome: How the Brain's Wiring Makes Us Who We Are](https://www.youtube.com/watch?v=qS6nTA3DUuY). *The science and the ML behind reconstructing circuits.*
3. **See the first connectome** — [White et al. 1986 — C. elegans connectome (OpenWorm)](http://openworm.org/ConnectomeToolbox/White_1986/). *The 302-neuron worm: where connectomics began.*
4. **See the frontier** — [Neuronal wiring diagram of an adult brain (FlyWire, 2024)](https://www.nature.com/articles/s41586-024-07558-y). *The full fruit-fly connectome — 140k neurons, 50M synapses.*
5. **Explore the data** — browse [FlyWire](https://flywire.ai/) or [MICrONS Explorer](https://www.microns-explorer.org/). *Interact with real reconstructed circuits.*

## Courses (free)
- [Neuromatch Academy — Computational Neuroscience](https://compneuro.neuromatch.io/) — **Neuromatch** — network/graph analysis of neural circuits, the analytical side of connectomics.
- [Neuronal Dynamics (EPFL)](https://neuronaldynamics.epfl.ch/online/index.html) — **Gerstner et al.** — how circuit structure shapes the dynamics a connectome alone can't reveal.

## Videos
- [I am my connectome (TED)](https://www.youtube.com/watch?v=L74TEED6fzw) — **Sebastian Seung** — the foundational argument for mapping the connectome.
- [Connectome: How the Brain's Wiring Makes Us Who We Are](https://www.youtube.com/watch?v=qS6nTA3DUuY) — **Microsoft Research (Sebastian Seung)** — the science and ML of circuit reconstruction.
- [Your Brain Is 150,000 Mini-Brains](https://www.youtube.com/watch?v=Dykkubb-Qus) — **Artem Kirsanov** — the neuron complexity a connectome must capture per node.
- [The Modular Architecture of Intelligence](https://www.youtube.com/watch?v=-_OgW6KSGE4) — **Artem Kirsanov** — reading structure (modules, motifs) off the wiring graph.

## Key Papers
- [Neuronal wiring diagram of an adult brain (FlyWire)](https://www.nature.com/articles/s41586-024-07558-y) — **Dorkenwald et al. (2024)** — the complete adult Drosophila connectome.
- [Functional connectomics spanning multiple areas of mouse visual cortex](https://www.nature.com/articles/s41586-025-08790-w) — **The MICrONS Consortium (2025)** — the first mammalian dataset pairing a dense electron-microscopy wiring map with calcium imaging of the same 75,000 neurons: structure and activity in one volume.
- [Functional connectomics reveals general wiring rule in mouse visual cortex](https://www.nature.com/articles/s41586-025-08840-3) — **Ding, Fahey, Papadopoulos et al. (2025)** — what the MICrONS volume actually bought: a "like-to-like" connection rule you can only see when wiring and tuning are measured together.
- [Random synaptic feedback weights support error backpropagation](https://www.nature.com/articles/ncomms13276) — **Lillicrap et al. (2016)** — how learning could work without symmetric wiring (relevant to what connectivity implies).
- [Backpropagation and the brain](https://www.nature.com/articles/s41583-020-0277-3) — **Lillicrap et al. (2020)** — connecting structural wiring to plausible learning algorithms.

## Articles / Blogs (free, no paywall)
- [OpenWorm — C. elegans connectome (White et al. 1986)](http://openworm.org/ConnectomeToolbox/White_1986/) — **OpenWorm** — the first complete connectome with open data and tools.
- [WormWiring](https://wormwiring.org/) — **Emmons lab (Albert Einstein College of Medicine)** — the C. elegans connectome datasets themselves: White 1986, Varshney 2011, Witvliet and the Emmons reconstructions, with downloadable chemical and gap-junction connectivity tables.
- [MICrONS Explorer](https://www.microns-explorer.org/) — **MICrONS** — open mammalian cortical connectome data, browseable in 3D.

## Books (free, with chapters)
- [Theoretical Neuroscience — **Ch. 7 (Network Models)**](https://www.gatsby.ucl.ac.uk/~dayan/book/) — **Dayan & Abbott** — how connectivity structure determines network computation.
- [Neuronal Dynamics — **Ch. 12 (Neuronal Populations)**](https://neuronaldynamics.epfl.ch/online/Ch12.html) — **Gerstner et al.** — population/circuit structure and its dynamics, free online.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 1.04 Graph Representations](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/graph-representations-intuition) — the graph formalism a connectome is analyzed with.
- Prereqs in this section: [01 Biological Neurons & Synapses](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuroscience-and-brain-inspired-ai/biological-neurons-and-synapses/biological-neurons-and-synapses)
- Related domains: [05. Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) · [07. Computer Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme)
