---
id: "models-and-architectures/large-language-models/positional-representations-in-llms/references"
topic: "Positional Representations in LLMs — References"
parent: "models-and-architectures/large-language-models/positional-representations-in-llms"
type: references
updated: 2026-09-14
---

# Positional Representations in LLMs — references

> Companion link library for **[Positional Representations in LLMs](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/positional-representations-in-llms/positional-representations-in-llms)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Learn the mechanism first** — read [Positional Encoding](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/positional-encoding/positional-encoding) on this platform, the canonical owner. *Sinusoidal, learned, relative and rotary, derived.*
2. **Get the geometric picture** — read [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI**. *Why rotating query and key vectors encodes relative distance exactly.*
3. **Read the source** — read [RoFormer](https://arxiv.org/abs/2104.09864) — **Su et al. (2021)**. *The rotary position embedding paper itself.*
4. **See the extension trick** — read [YaRN](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)**. *Interpolate low frequencies, extrapolate high ones; the method most long-context releases use.*
5. **Question the assumption** — read [The Impact of Positional Encoding on Length Generalization](https://arxiv.org/abs/2305.19466) — **Kazemnejad et al. (2023)**. *NoPE, and what the causal mask alone already tells the model.*

**In this platform**:
- What positions attach to: [Attention Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) · [KV Cache Variants](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-variants)
- Long prompts versus retrieval: [Long Context vs RAG](/ai-ml/practitioner-workflows/llm-applications/long-context-vs-rag/long-context-vs-rag)
- Where extension, sinks and the retrieval failure modes are taught: [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures)
- Canonical owner of the mechanism (do not learn it here): [Positional Encoding](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/positional-encoding/positional-encoding)

**Articles**:
- [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI** — the standard free explainer, with the complex-number derivation.
- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka** — which 2025 models use which positional scheme, and alongside which attention variant.

**Papers**:
- [DeepSeek-V2](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)** — §2.1.3 explains the decoupled rotary key that multi-head latent attention needs; the clearest example of positions constraining a cache design.
- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) — **Su et al. (2021)** — RoPE, the scheme nearly every modern decoder uses.
- [The Impact of Positional Encoding on Length Generalization in Transformers](https://arxiv.org/abs/2305.19466) — **Kazemnejad et al. (2023)** — NoPE: decoder-only models infer position from causality alone.
- [Train Short, Test Long: Attention with Linear Biases (ALiBi)](https://arxiv.org/abs/2108.12409) — **Press, Smith & Lewis (2021)** — a distance penalty instead of an embedding; the length-extrapolation baseline.
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)** — frequency-aware interpolation, the standard context-extension recipe.
