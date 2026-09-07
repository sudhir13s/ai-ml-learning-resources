---
id: "llms-applications-and-agents/llm-model-architectures/positional-representations-in-llms"
topic: "Positional Representations in LLMs"
level: advanced
built_from: ["positional-encoding", "attention-architectures-gqa-mla-sliding-and-linear"]
leads_to: ["long-context-architectures"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Positional Representations in LLMs"
minutes: 10
category: llm-model-architectures
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

**Start here — suggested path:**

1. **Learn the mechanism first** — read [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding) on this platform, the canonical owner. *Sinusoidal, learned, relative and rotary, derived.*
2. **Get the geometric picture** — read [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI**. *Why rotating query and key vectors encodes relative distance exactly.*
3. **Read the source** — read [RoFormer](https://arxiv.org/abs/2104.09864) — **Su et al. (2021)**. *The rotary position embedding paper itself.*
4. **See the extension trick** — read [YaRN](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)**. *Interpolate low frequencies, extrapolate high ones; the method most long-context releases use.*
5. **Question the assumption** — read [The Impact of Positional Encoding on Length Generalization](https://arxiv.org/abs/2305.19466) — **Kazemnejad et al. (2023)**. *NoPE, and what the causal mask alone already tells the model.*

## Key Papers

- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) — **Su et al. (2021)** — RoPE, the scheme nearly every modern decoder uses.
- [Train Short, Test Long: Attention with Linear Biases (ALiBi)](https://arxiv.org/abs/2108.12409) — **Press, Smith & Lewis (2021)** — a distance penalty instead of an embedding; the length-extrapolation baseline.
- [The Impact of Positional Encoding on Length Generalization in Transformers](https://arxiv.org/abs/2305.19466) — **Kazemnejad et al. (2023)** — NoPE: decoder-only models infer position from causality alone.
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)** — frequency-aware interpolation, the standard context-extension recipe.
- [DeepSeek-V2](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)** — §2.1.3 explains the decoupled rotary key that multi-head latent attention needs; the clearest example of positions constraining a cache design.

## Articles / Blogs (free, no paywall)

- [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI** — the standard free explainer, with the complex-number derivation.
- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka** — which 2025 models use which positional scheme, and alongside which attention variant.

## In this platform

- Canonical owner of the mechanism (do not learn it here): [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding)
- Where extension, sinks and the retrieval failure modes are taught: [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures)
- What positions attach to: [Attention Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) · [KV Cache Variants](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache-variants)
- Long prompts versus retrieval: [Long Context vs RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/long-context-vs-rag/long-context-vs-rag)
