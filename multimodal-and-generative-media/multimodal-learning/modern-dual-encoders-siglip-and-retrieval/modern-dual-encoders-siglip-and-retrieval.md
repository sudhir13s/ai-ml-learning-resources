---
id: "multimodal-and-generative-media/multimodal-learning/modern-dual-encoders-siglip-and-retrieval"
topic: "Modern Dual Encoders — SigLIP and Retrieval"
level: intermediate
built_from: ["clip-and-contrastive-vision-language-pretraining"]
leads_to: ["multimodal-and-generative-media/multimodal-learning/visual-instruction-tuning-llava", "multimodal-and-generative-media/multimodal-learning/modern-open-vlm-architectures", "multimodal-and-generative-media/multimodal-learning/multimodal-rag"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 13
title: "Modern Dual Encoders — SigLIP and Retrieval"
core_idea: "Two separate towers embed images and text for cheap dot-product search; scoring each pair with its own sigmoid removes the batch-wide normalisation, but one vector per image still discards detail no re-ranker can restore."
minutes: 13
category: multimodal-learning
---

# Modern Dual Encoders — SigLIP and Retrieval
> A *dual encoder* embeds images and text with two separate towers and compares them with a
> dot product — cheap enough to index millions of items. The 2023 upgrade was the loss:
> Sigmoid Loss for Language Image Pretraining (SigLIP) replaces Contrastive Language-Image
> Pretraining's (CLIP) batch-wide softmax with an independent **sigmoid on every pair**, so
> training no longer needs a global normalization over the batch. Same architecture, better
> small-batch behaviour, and — by 2026 — the default vision tower inside open VLMs.

**Why it matters:** the dual encoder is the workhorse of production multimodal systems: search,
deduplication, safety filtering, and the frozen image tower that vision-language models (VLMs)
are built on.

- **Where it shows up in 2026:** SigLIP / SigLIP 2 towers ship inside PaliGemma, Qwen-VL,
  InternVL, SmolVLM and most open VLMs; the encoder is chosen before the language model is.
- **What interviewers probe:** why softmax contrastive loss makes batch size a *hyperparameter
  of the objective*, how the sigmoid loss decouples it, and why a dual encoder (fast, no
  cross-attention) loses to a cross-encoder re-ranker on fine-grained matching.
- **The failure mode:** dual encoders compress a whole image into one vector, so anything
  requiring localization, counting or reading text is lost at indexing time — you cannot
  re-rank your way out of information the embedding never kept.

## References

The curated link library for this topic — a suggested reading path, videos, courses, articles, papers and internal cross-links — lives in a companion file so it can be reused as a standalone reference list:

**→ [Modern Dual Encoders — SigLIP and Retrieval — references](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/modern-dual-encoders-siglip-and-retrieval/modern-dual-encoders-siglip-and-retrieval#references-further-reading)**
