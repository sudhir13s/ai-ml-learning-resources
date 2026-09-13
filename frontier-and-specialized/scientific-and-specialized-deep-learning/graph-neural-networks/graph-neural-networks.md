---
id: "frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks"
topic: "Graph Neural Networks"
core_idea: "Graph neural networks learn node representations by repeated neighbourhood aggregation, which makes them permutation-equivariant but caps their expressivity at the 1-WL test and over-smooths when stacked deep."
level: intermediate
built_from: ["perceptron-and-mlp", "cnns-and-convolution"]
leads_to: ["frontier-and-specialized/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning", "frontier-and-specialized/scientific-and-specialized-deep-learning/neural-operators"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Graph Neural Networks"
minutes: 16
category: scientific-and-specialized-deep-learning
---

# Graph Neural Networks

> A graph neural network (GNN) generalises convolution from a grid to an arbitrary graph: each
> node repeatedly **aggregates messages from its neighbours** and updates its own vector. After
> $k$ rounds every node's representation summarises its $k$-hop neighbourhood, and the whole
> thing is permutation-equivariant by construction because the aggregator is a sum, mean, or max.

**Why it matters:** GNNs are the workhorse behind molecular property prediction, recommendation
graphs, traffic forecasting, and — most visibly in 2026 — DeepMind's GraphCast weather model.
The interview question is almost always **expressivity**: standard message passing is at most as
powerful as the 1-dimensional Weisfeiler-Leman graph isomorphism test, so it cannot distinguish
some structurally different graphs; and **over-smoothing**, where stacking too many rounds makes
every node vector converge to the same value.

## The design space in one screen

- **Message** — what a neighbour sends (its vector, optionally edge features).
- **Aggregate** — sum (most expressive), mean (degree-invariant), max (structure-selective), or attention-weighted (GAT).
- **Update** — how the node combines its own state with the aggregate; a multilayer perceptron (MLP) here is what makes GIN maximally expressive.
- **Readout** — node-level, edge-level, or graph-level pooling, chosen by the task.

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers — lives in a companion file so it can be reused as a standalone reference list:

**→ [Graph Neural Networks — references](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks#references-further-reading)**
