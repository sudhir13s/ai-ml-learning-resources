---
id: "09-llms/decoding-and-sampling/constrained-and-guided-decoding"
topic: "Decoding: Constrained and Guided Decoding"
parent: "09-llms"
chapter_of: "09-llms/decoding-and-sampling"
chapter: 4
level: intermediate
built_from: ["09-llms/decoding-and-sampling"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: flagship
est_minutes: 6
leads_to: ["09-llms/decoding-and-sampling/decoding-in-production"]
core_idea: "Constrained decoding masks every token that would break a grammar, schema or regular expression before the decoder picks, so invalid output becomes unreachable while the model still chooses freely among the valid tokens."
title: "Constrained and Guided Decoding"
minutes: 6
category: inference-and-serving
---

# Constrained and guided decoding: making invalid output unreachable

Sampling decides which plausible token to emit; this page covers the decoders that also guarantee the output is well-formed.

## The idea

- **Structured / constrained decoding** layers a *grammar* on top of sampling.
  - At each step, mask out tokens that would violate a JSON schema or regex before sampling.
  - It's the same truncation idea (zero out disallowed tokens, renormalize) applied to *syntactic validity* rather than probability.
  - It's how reliable "respond in JSON" modes work.

---

## References

Shared with the topic's companion file — see [Decoding & Sampling — references](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling#references-further-reading).
