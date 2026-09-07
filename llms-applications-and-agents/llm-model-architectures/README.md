---
id: "llms-applications-and-agents/llm-model-architectures"
topic: "LLM Model Architectures"
level: advanced
built_from: ["large-language-model-foundations", "attention-and-transformers"]
updated: 2026-09-07
---

# LLM Model Architectures

> What frontier labs actually changed inside the transformer between 2023 and 2026. Every page
> here answers the same engineering question from a different angle: exact attention costs
> O(T²) compute and an O(T) cache per layer, and a dense feed-forward network couples capacity to
> compute — so which structural change buys the most quality per unit of memory bandwidth?

**Start here:** [Attention Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) — the four moves (share, compress, restrict, linearize) are the vocabulary the rest of the sub-area uses.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### The attention block, redesigned

1. [Attention Architectures — GQA, MLA, Sliding-Window and Linear](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) — multi-query and grouped-query attention, multi-head latent attention, local and interleaved windows, linear and hybrid stacks.
2. [Positional Representations in LLMs](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/positional-representations-in-llms/positional-representations-in-llms) — which scheme shipped models chose, and how position interacts with long context and cache variants.

### Making the context window long

3. [Long-Context Methods](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures) — RoPE scaling (position interpolation, NTK-aware, YaRN), efficient kernels and cache compression as one stack, not one trick.

### Decoupling capacity from compute

4. [Mixture-of-Experts](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/mixture-of-experts/mixture-of-experts) — routing, load balancing, expert parallelism, and why total parameters stopped predicting inference cost.

### A different generation paradigm

5. [Diffusion Language Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/diffusion-language-models/diffusion-language-models) — masked and continuous denoising over a whole sequence in a handful of parallel passes, and where it beats autoregression.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the Architectures and Mixture-of-Experts lectures are a data-driven survey of exactly these choices, by people who reimplemented them.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; gives you the attention-implementation vocabulary the model cards use.
- [Mixture of Experts Explained](https://huggingface.co/blog/moe) — **Hugging Face** — course-grade treatment of routing, load balancing, training instabilities and serving.
- [How to Build a Diffusion Language Model](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) — **Kuleshov Group (Cornell)** — a workshop-derived tutorial by the authors of MDLM; the closest thing to a course on text diffusion.

## Videos

- [Mistral / Mixtral Explained: Sliding Window Attention, Sparse Mixture of Experts, Rolling Buffer](https://www.youtube.com/watch?v=UiX8K-xBUpE) — **Umar Jamil** — the best free visual explanation of sliding-window attention and its rolling buffer, drawn from the paper.
- [Mixture of Experts (MoE), Visually Explained](https://www.youtube.com/watch?v=0QQlYR1r6pQ) — **Jia-Bin Huang** — the cleanest visual intuition for routers, experts and sparsity.
- [Rotary Positional Embeddings: Combining Absolute and Relative](https://www.youtube.com/watch?v=o29P0Kpobz0) — **Efficient NLP** — the clearest RoPE explainer; start here if rotation-as-position still feels abstract.
- [FlashAttention — Tri Dao, Stanford MLSys #67](https://www.youtube.com/watch?v=gMOAud7hZg4) — **Stanford MLSys Seminars** — the exact-attention kernel every variant on these pages is measured against, from its author.

## Key Papers

- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) — **Ainslie et al. (2023)** — the share-the-key/value middle ground that became the default, plus cheap uptraining from an existing model.
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)** — introduces multi-head latent attention (MLA) and a production MoE stack in one report.
- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) — **Su et al. (2021)** — the rotary scheme behind nearly every long-context LLM, with the relative-position derivation.
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)** — frequency-dependent interpolation plus attention-temperature correction; the extension method most open models use.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu and Dao (2023)** — the selective state-space model that made the non-attention branch competitive at scale.

## Articles / Blogs (free, no paywall)

- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka** — the single best free survey of what recent models actually changed, attention block by attention block.
- [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI** — the positional scheme every page here assumes, derived carefully.
- [On the Tradeoffs of State Space Models](https://goombalab.github.io/blog/2025/tradeoffs/) — **Albert Gu** — the Mamba author on what a fixed-size recurrent state can and cannot do versus attention; the honest case for hybrids.
- [Diffusion language models](https://sander.ai/2023/01/09/diffusion-language.html) — **Sander Dieleman** — the essay that framed the discreteness problem, with the [2026 continuous follow-up](https://sander.ai/2026/08/24/continuous-dlms.html).

## Books (free, with chapters)

- [*How to Scale Your Model* — "Transformers"](https://jax-ml.github.io/scaling-book/transformers/) — **Google DeepMind (Austin et al.)** — free online; the accounting that turns "which attention variant" into a memory-bandwidth number.
- [*Dive into Deep Learning* — Ch. 11 "Attention Mechanisms and Transformers"](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html) — **Zhang, Lipton, Li and Smola** — free and runnable; the baseline multi-head implementation every variant modifies.
- [*Understanding Deep Learning* — Ch. 18 "Diffusion models"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the forward and reverse process in the notation the diffusion-LM page uses.

## In this platform

- Section index: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- Before this: [Large Language Model Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/readme) · Alongside: [Training and Adaptation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/readme) · [Inference and Runtime](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/readme) · [Reasoning, Evaluation and Alignment](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/readme)
- The mechanisms these variants modify: [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) · [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding) · [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention)
- The non-attention branch, in full: [Selective State-Space Models — Mamba and Mamba-2](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/selective-state-space-models-mamba/selective-state-space-models-mamba) · [Linear and Hybrid Attention Architectures](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/linear-and-hybrid-attention-architectures/linear-and-hybrid-attention-architectures)
- What these choices cost at serving time: [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache) · [KV Cache — Variants](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache-variants)
- The diffusion side, taught elsewhere: [Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme)
- The mental models: [Multi-Head Attention](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/multi-head-attention-intuition) · [Mixture-of-Experts Routing](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/mixture-of-experts-routing-intuition) · [Positional Representations](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/positional-representations-intuition)
