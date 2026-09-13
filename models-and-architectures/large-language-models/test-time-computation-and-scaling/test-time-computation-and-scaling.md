---
id: "models-and-architectures/large-language-models/test-time-computation-and-scaling"
topic: "Test-Time Computation and Scaling"
core_idea: "Spending more inference compute through longer reasoning, sampling or search buys accuracy per request, but only a good verifier turns the extra coverage into correct answers."
level: advanced
built_from: ["chain-of-thought-and-reasoning", "decoding-and-sampling"]
leads_to: ["09-llms/llm-evaluation-and-benchmarks", "model-adaptation/reinforcement-learning-posttraining"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Test-Time Computation and Scaling"
minutes: 16
category: large-language-models
---

# Test-Time Computation and Scaling

> Accuracy is not fixed at training time. Let a model **think longer** (more reasoning tokens),
> **think more often** (sample N answers and pick), or **think with search** (expand and prune a tree
> of partial solutions), and it gets measurably better on hard problems. Inference compute became a
> tunable axis alongside parameters and training tokens.

**Why it matters:** it changes the economics of deployment — you now choose an accuracy/latency/cost
point per request — and it is the single most-asked reasoning question of 2025–2026.

- **What is probed:** the difference between **sampling** (best-of-N, self-consistency) and **search** (beam search, tree search) over reasoning steps; what a **verifier** does and why a process reward model (PRM) beats an outcome one for guiding search; the *compute-optimal* result — for easy problems, more test-time compute beats a bigger model; for the hardest ones, it does not.
- **The bound you must state:** pass@N (does *any* sample succeed) rises far faster than accuracy with a *selector*. Without a good verifier, most of the coverage a sampler generates is unusable. This is the whole reason verifiers matter.
- **The cheapest useful trick:** **budget forcing** (s1) — append "Wait" to suppress the end-of-thinking token and force more reasoning, or truncate to force less. A 1,000-example fine-tune plus this control reproduces much of the effect.

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Test-Time Computation and Scaling — references](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/test-time-computation-and-scaling/test-time-computation-and-scaling#references-further-reading)**
