---
id: "modalities-and-generative-models/multimodal-learning/multimodal-benchmarks-and-evaluation"
topic: "Multimodal Benchmarks and Evaluation"
level: intermediate
built_from: ["visual-instruction-tuning-llava", "modern-open-vlm-architectures"]
leads_to: ["modalities-and-generative-models/multimodal-learning/multimodal-rag"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 13
title: "Multimodal Benchmarks and Evaluation"
minutes: 13
category: multimodal-learning
---

# Multimodal Benchmarks and Evaluation
> Multimodal benchmarks are unusually easy to fake. A "vision" question that a text-only model
> answers from priors measures language, not sight — and a large share of early
> vision-language-model (VLM) benchmark items are exactly that. The modern evaluation stack
> answers with **vision-indispensable question sets** (MMStar), **harder variants that strip
> text-only solvability** (MMMU-Pro), **perception-specific probes** (BLINK), and
> **hallucination tests** (POPE), all run through a standard harness so numbers are comparable.

**Why it matters:** picking a VLM is an evaluation problem, and a leaderboard number that came
from a contaminated or text-solvable benchmark will not survive your own data.

- **The four things worth measuring separately:** perception (can it see?), knowledge and
  reasoning, grounding and hallucination (does it invent objects?), and instruction fidelity
  (does it answer in the format you asked for?).
- **What interviewers probe:** how you would detect contamination or text-only solvability —
  the standard trick is to run the benchmark *without the image* and see how far above chance
  the model scores.
- **The failure mode people get wrong:** multiple-choice accuracy rewards elimination, not
  perception. Two models with equal scores can differ enormously on open-ended answers, so pair
  any leaderboard with a small hand-built set from your own domain.

**Start here — suggested path:**

1. **See the flagship benchmark** — read [MMMU](https://arxiv.org/abs/2311.16502) — **Yue et al. (2024)**. *College-level multi-discipline questions with figures, diagrams and charts; the current headline number.*
2. **Learn why it needed a sequel** — read [MMMU-Pro](https://arxiv.org/abs/2409.02813) — **Yue et al. (2025)**. *Filters out text-only-solvable items, augments options, and adds a vision-only setting; scores drop hard, and that is the finding.*
3. **See the contamination argument** — read [Are We on the Right Way for Evaluating Large Vision-Language Models? (MMStar)](https://arxiv.org/abs/2403.20330) — **Chen et al. (2024)**. *Quantifies how many benchmark items need no image at all, and builds a vision-indispensable set.*
4. **Probe perception directly** — read [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/abs/2404.12390) — **Fu et al. (2024)**. *Tasks humans solve "in a blink" and models fail; the clearest picture of the perception gap.*
5. **Run the harness yourself** — use [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) — **LMMs-Lab**. *One command, 50+ tasks, reproducible prompts; without a shared harness, cross-paper comparisons are meaningless.*

## Courses (free)

- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro) — **Hugging Face** — includes how VLMs are evaluated and where the metrics mislead.
- [Stanford CS231n — Lecture 16, "Vision and Language" (slides)](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf) — **Stanford (Spring 2025)** — the benchmark landscape as taught alongside the models.

## Key Papers

- [MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI](https://arxiv.org/abs/2311.16502) — **Yue et al. (2024)** — 11.5K expert-level questions across six disciplines; the reference multimodal reasoning benchmark.
- [MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](https://arxiv.org/abs/2409.02813) — **Yue et al. (2025)** — the hardened version, including a vision-only setting where the question is embedded in the image.
- [Are We on the Right Way for Evaluating Large Vision-Language Models? (MMStar)](https://arxiv.org/abs/2403.20330) — **Chen et al. (2024)** — measures text-only solvability and data leakage, then releases 1,500 vision-indispensable items.
- [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/abs/2404.12390) — **Fu et al. (2024)** — core visual perception tasks (depth, correspondence, forensics) where strong models are near chance.
- [Evaluating Object Hallucination in Large Vision-Language Models (POPE)](https://arxiv.org/abs/2305.10355) — **Li et al. (2023)** — the polling-based probe that made object hallucination measurable.
- [LMMs-Eval: Reality Check on the Evaluation of Large Multimodal Models](https://arxiv.org/abs/2407.12772) — **Zhang et al. (2025)** — the standard harness plus an analysis of contamination and benchmark redundancy.

## Articles / Blogs (free, no paywall)

- [MMMU benchmark site and leaderboard](https://mmmu-benchmark.github.io/) — **MMMU team** — per-discipline breakdowns and the current standings; more informative than the headline average.
- [VHELM: Holistic Evaluation of Vision Language Models](https://crfm.stanford.edu/helm/vhelm/latest/) — **Stanford CRFM** — multi-aspect evaluation (bias, fairness, robustness, toxicity, knowledge), not one accuracy number.
- [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) — **LMMs-Lab** — the evaluation harness most 2025–26 VLM papers report through.
- [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — which benchmarks the field currently takes seriously, and which it has retired.

## In this platform

- Prerequisites: [Visual Instruction Tuning (LLaVA)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/visual-instruction-tuning-llava/visual-instruction-tuning-llava) · [Modern Open VLM Architectures](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-open-vlm-architectures/modern-open-vlm-architectures)
- The text-side equivalent: [LLM Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation) · [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding)
- Related: [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) · [RAG Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-evaluation/rag-evaluation) — for multimodal retrieval pipelines
