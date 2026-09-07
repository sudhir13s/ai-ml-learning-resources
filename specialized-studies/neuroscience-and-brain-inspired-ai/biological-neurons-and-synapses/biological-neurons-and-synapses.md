---
id: "20-neuroscience/biological-neurons-and-synapses"
topic: "Biological Neurons & Synapses"
parent: "20-neuroscience"
level: intermediate
built_from: ["differential-equations", "basic-circuits", "activation-functions"]
interview_frequency: low
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Biological Neurons & Synapses"
minutes: 10
category: neuroscience-and-brain-inspired-ai
---

# Biological Neurons & Synapses
> The real computing element the artificial neuron is a cartoon of: a membrane that integrates
> incoming current, fires an all-or-none **spike** when its voltage crosses threshold, and talks to
> other neurons across chemical **synapses**. Understand the Hodgkin–Huxley and leaky
> integrate-and-fire models and you understand why a biological neuron is *not* a weighted sum.

**Why it matters:** this is the ground truth every brain-inspired idea (SNNs, STDP, neuromorphic
hardware) builds on. The interview-relevant payoff is the contrast: a `y = σ(Wx + b)` unit is a
rate-coded, stateless caricature of a leaky, threshold, spiking dynamical system — knowing exactly
where the analogy holds and breaks is the whole point of this domain.

**Start here — suggested path:**

1. **Get the picture** — watch [The Action Potential](https://www.youtube.com/watch?v=oa6rvUJlg7o). *A correct mental model of spike generation before any equations.*
2. **Get the core equation** — watch [The Core Equation Of Neuroscience](https://www.youtube.com/watch?v=zOmhHE2xctw). *Hodgkin–Huxley made visual — ion channels, gating, voltage.*
3. **Read the model math** — [Neuronal Dynamics Ch. 1 (Integrate-and-Fire)](https://neuronaldynamics.epfl.ch/online/Ch1.html) then [Ch. 2 (Hodgkin–Huxley)](https://neuronaldynamics.epfl.ch/online/Ch2.html). *The LIF and HH equations you can actually simulate.*
4. **See dendrites compute** — watch [Your Brain Is 150,000 Mini-Brains](https://www.youtube.com/watch?v=Dykkubb-Qus). *Why a single neuron is closer to a small network than a single unit.*
5. **Simulate one** — work the [Neuromatch Computational Neuroscience](https://compneuro.neuromatch.io/) biological-neuron notebooks. *Implementing LIF cements the "leaky ReLU with state" intuition.*

## Courses (free)
- [Neuromatch Academy — Computational Neuroscience](https://compneuro.neuromatch.io/) — **Neuromatch** — notebook-driven curriculum; the biological-neuron-models week builds LIF and Hodgkin–Huxley from scratch.
- [Neuronal Dynamics (EPFL online course)](https://neuronaldynamics.epfl.ch/online/index.html) — **Gerstner et al.** — the canonical free course + book on single-neuron and synapse models.

## Videos
- [The Action Potential](https://www.youtube.com/watch?v=oa6rvUJlg7o) — **Harvard Extension School** — clear walkthrough of depolarization, threshold, and the all-or-none spike.
- [The Core Equation Of Neuroscience](https://www.youtube.com/watch?v=zOmhHE2xctw) — **Artem Kirsanov** — the Hodgkin–Huxley model visualized: ion channels, gating variables, membrane voltage.
- [Your Brain Is 150,000 Mini-Brains](https://www.youtube.com/watch?v=Dykkubb-Qus) — **Artem Kirsanov** — dendritic computation: why one neuron is far richer than a single artificial unit.
- [CNS2.3 — Hodgkin-Huxley Model](https://www.youtube.com/watch?v=ZX1skUJbBpc) — **Gerstner Lab (EPFL)** — the textbook's own author deriving the four HH equations, gating variable by gating variable.
- [CNS2.4 — Threshold in the Hodgkin-Huxley Model](https://www.youtube.com/watch?v=Y7qK7FTObp0) — **Gerstner Lab (EPFL)** — why a "firing threshold" is an emergent approximation, not a parameter of the model: the detail that separates LIF from biophysics.

## Key Papers
- [A quantitative description of membrane current… (Hodgkin & Huxley, 1952)](https://www.ncbi.nlm.nih.gov/books/NBK11164/) — **Hodgkin & Huxley** — the Nobel-winning model of the action potential (background + the equations).
- [Single Cortical Neurons as Deep Artificial Neural Networks](https://www.biorxiv.org/content/10.1101/613141v2) — **Beniaguev, Segev & London (2020)** — fits a deep network to one biological neuron and needs 5–8 layers to match it: the sharpest measurement of how far `σ(Wx + b)` is from a real cell.
- [Dendritic computation (review)](https://www.frontiersin.org/articles/10.3389/fnins.2018.00774/full) — **open-access review** — how single neurons perform nonlinear computation in their dendrites.

## Articles / Blogs (free, no paywall)
- [Neuronal Dynamics — Ch. 1: Integrate-and-Fire](https://neuronaldynamics.epfl.ch/online/Ch1.html) — **Gerstner et al.** — the LIF neuron derived and explained, fully free online.
- [Neuronal Dynamics — Ch. 2: Hodgkin–Huxley](https://neuronaldynamics.epfl.ch/online/Ch2.html) — **Gerstner et al.** — the biophysical spiking model in readable form.
- [Neuronal Dynamics — §3.2: Spatial Structure, the Dendritic Tree](https://neuronaldynamics.epfl.ch/online/Ch3.S2.html) — **Gerstner et al.** — Rall's cable equation: how voltage spreads and decays along a dendrite, the math behind "mini-brains" (this replaces the Scholarpedia cable-theory article, whose host has been down since 2026-09).

## Books (free, with chapters)
- [Neuronal Dynamics — **Ch. 1–2 (LIF, Hodgkin–Huxley)** and **Ch. 4 (dimensionality, phase plane)**](https://neuronaldynamics.epfl.ch/online/Ch4.html) — **Gerstner, Kistler, Naud & Paninski** — the anchor text for single-neuron models, free in full online.
- [Neuroscience Online / NBK reference — **action potential & membrane chapters**](https://www.ncbi.nlm.nih.gov/books/NBK11164/) — **NCBI Bookshelf** — open biology reference for the underlying physiology.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 4.14 Activation Functions & Softmax](/ai-ml/ai-ml-intuitions/architectural-mechanisms/nonlinear-transformation/activation-functions-and-softmax-intuition) — the artificial neuron a LIF neuron is a caricature of.
- Next concepts: [02 Neural Coding](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/neural-coding/neural-coding) · [03 Spiking Neural Networks](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/spiking-neural-networks/spiking-neural-networks)
- Related domain: [05. Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
