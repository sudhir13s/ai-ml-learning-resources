---
id: "models-and-architectures/large-language-models/positional-representations-in-llms"
topic: "Positional Representations in LLMs"
core_idea: "At language-model scale, position handling decides long-context behaviour: rotary encodings dominate, extrapolation past the trained range breaks, and interpolation methods such as YaRN stretch the usable range."
level: advanced
built_from: ["positional-encoding", "attention-architectures-gqa-mla-sliding-and-linear"]
leads_to: ["09-llms/long-context-methods"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Positional Representations in LLMs"
minutes: 10
category: large-language-models
---

# Positional Representations in LLMs

> A short bridge page. The mechanics of sinusoidal, learned, rotary (RoPE) and attention-with-linear-biases
> (ALiBi) encodings are taught in the deep-learning owner page; this page covers only what changes at
> **large-language-model scale**: which scheme shipped models chose, how positions interact with long
> context and cache variants, and where extrapolation actually breaks.

**Why it matters:** almost every long-context question resolves into a positional question.

- **What is probed:** why RoPE became universal (relative distances fall out of the dot product, and the same weights work at any offset); why naive extrapolation past the trained range collapses; what position interpolation and YaRN do about it.
- **The scale-specific facts:** RoPE's base frequency θ is a *tuned* hyperparameter in long-context models, not a constant; multi-head latent attention keeps a small **decoupled** rotary key because the compressed latent cannot carry rotation; sliding-window layers change which relative distances a layer ever sees.
- **The surprise:** decoder-only models with **no** positional encoding at all (NoPE) still learn position from the causal mask, and generalise to longer inputs better than some explicit schemes.

## References

The curated link library for this topic — in this platform, articles, papers — lives in a companion file so it can be reused as a standalone reference list:

**→ [Positional Representations in LLMs — references](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/positional-representations-in-llms/positional-representations-in-llms#references-further-reading)**
