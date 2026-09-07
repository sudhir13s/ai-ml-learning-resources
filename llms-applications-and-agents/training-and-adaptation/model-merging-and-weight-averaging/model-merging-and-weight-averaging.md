---
id: "llms-applications-and-agents/training-and-adaptation/model-merging-and-weight-averaging"
topic: "Model Merging and Weight Averaging"
level: advanced
built_from: ["supervised-fine-tuning", "lora-and-parameter-efficient-fine-tuning"]
leads_to: ["mixture-of-experts", "llm-evaluation"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Model Merging and Weight Averaging"
minutes: 14
category: training-and-adaptation
---

# Model Merging and Weight Averaging

> Merging combines several fine-tuned checkpoints of the *same* base model into one set of weights —
> by averaging them, or by adding their **task vectors** (fine-tuned weights minus base weights).
> No gradients, no training data, minutes on a laptop: you get one model that keeps several
> specialisations, and one deployment instead of five.

**Why it matters:** merging is how most strong open-weight community models are actually built, and
it is a cheap alternative to another fine-tuning run.

- **What is probed:** why averaging weights of independently fine-tuned models works at all (they stay in the same loss basin because they share an initialisation); what **task arithmetic** buys you (add a skill, subtract a behaviour); how **TIES** and **DARE** deal with *interference* between task vectors.
- **The trade-off:** merging preserves inference cost — unlike a mixture-of-experts (MoE), which adds parameters — but it cannot merge models with different bases or tokenizers, and gains are not additive.
- **The failure mode people miss:** a merge that scores higher on benchmarks and is *worse* in use. Merged models are notorious for benchmark-contaminated wins; always evaluate on held-out, non-public tasks.

**Start here — suggested path:**

1. **See the mental model** — read [Merge Large Language Models with mergekit](https://huggingface.co/blog/mlabonne/merge-models) — **Maxime Labonne**. *SLERP, TIES, DARE and passthrough explained with the exact YAML you would run.*
2. **Read where the idea came from** — read [Model Soups](https://arxiv.org/abs/2203.05482) — **Wortsman et al. (2022)**. *Averaging many fine-tuned checkpoints beats picking the best one, at zero extra inference cost.*
3. **Get the algebra** — read [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) — **Ilharco et al. (2022)**. *Task vectors add, subtract and compose; this is the paper that made merging a design tool rather than a trick.*
4. **Learn why naive addition breaks** — read [TIES-Merging](https://arxiv.org/abs/2306.01708) — **Yadav et al. (2023)** and [DARE](https://arxiv.org/abs/2311.03099) — **Yu et al. (2023)**. *Trim, elect signs, disjoint-merge; then drop-and-rescale. Both are about interference.*
5. **Do it** — run [mergekit](https://github.com/arcee-ai/mergekit) — **Arcee AI**. *One YAML file merges two checkpoints on CPU; then evaluate the merge honestly.*

## Courses (free)

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — the fine-tuning chapters give the checkpoint-and-adapter vocabulary merging operates on; free and code-first.
- [mergekit](https://github.com/arcee-ai/mergekit) — **Arcee AI (Charles Goddard)** — the reference implementation and, in practice, the tutorial: every merge method above ships as a documented YAML recipe.

## Videos

- [Everything you need to know about Fine-tuning and Merging LLMs](https://www.youtube.com/watch?v=uLrOI65XbDw) — **Maxime Labonne (AI Engineer)** — the clearest talk on where merging sits between fine-tuning and MoE, by the person who wrote the canonical guide.
- [Model Merging and Mixtures of Experts](https://www.youtube.com/watch?v=TKVA17RhgVA) — **Maxime Labonne (AI in Production)** — merging versus frankenMoE construction, with the trade-offs stated plainly.
- [Mergekit founder Charles Goddard on model merging](https://www.youtube.com/watch?v=YhnIvRr-mlQ) — **Arcee AI** — the tool's author on what merges actually do to weights and where they fall over.

## Key Papers

- [Model soups: averaging weights of multiple fine-tuned models improves accuracy](https://arxiv.org/abs/2203.05482) — **Wortsman et al. (2022)** — the founding result: uniform and greedy soups, no inference-time cost.
- [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) — **Ilharco et al. (2022)** — task vectors as first-class objects you can add, negate and compose.
- [TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708) — **Yadav et al. (2023)** — trim small changes, elect a sign, merge only the agreeing parameters.
- [Language Models are Super Mario (DARE)](https://arxiv.org/abs/2311.03099) — **Yu et al. (2023)** — randomly drop most delta parameters and rescale the rest; merges get cleaner, not worse.
- [Evolutionary Optimization of Model Merging Recipes](https://arxiv.org/abs/2403.13187) — **Akiba et al. (2024, Sakana AI)** — search the merge recipe itself, in both parameter space and data-flow space.
- [Arcee's MergeKit: A Toolkit for Merging Large Language Models](https://arxiv.org/abs/2403.13257) — **Goddard et al. (2024)** — the tool paper; the practical taxonomy of what is implemented and why.
- [A Careful Examination of LLM Performance on Grade School Arithmetic](https://arxiv.org/abs/2405.00332) — **Zhang et al. (2024)** — read this before trusting any merged model's leaderboard jump; the cleanest evidence that benchmark contamination inflates exactly these gains.

## Articles / Blogs (free, no paywall)

- [Merge Large Language Models with mergekit](https://huggingface.co/blog/mlabonne/merge-models) — **Maxime Labonne** — the reference walkthrough of every mainstream merge method with runnable configs.
- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka** — context for *why* merging only works within one architecture family, and how those families actually differ.

## Books (free, with chapters)

- [*Understanding Deep Learning* — Ch. 20 "Why does deep learning work?"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; loss-landscape and mode-connectivity intuition, which is the reason weight averaging works at all.

## In this platform

- Prerequisite: [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/supervised-fine-tuning/supervised-fine-tuning) · [LoRA and Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) (adapters merge back into base weights — the same algebra)
- The alternative when you want *capacity*, not just combination: [Mixture of Experts](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/mixture-of-experts/mixture-of-experts)
- The other way to fold a model's ability into another: [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/knowledge-distillation/knowledge-distillation)
- How to check a merge honestly: [LLM Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation)
- Intuition track: [LoRA](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/adaptation/lora-intuition) · [Transfer Learning and Fine-Tuning](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/adaptation/transfer-learning-and-fine-tuning-intuition)
