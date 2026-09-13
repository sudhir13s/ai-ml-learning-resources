---
id: "multimodal-and-generative-media/multimodal-learning/multimodal-benchmarks-and-evaluation/references"
topic: "Multimodal Benchmarks and Evaluation — References"
parent: "multimodal-and-generative-media/multimodal-learning/multimodal-benchmarks-and-evaluation"
type: references
updated: 2026-09-14
---

# Multimodal Benchmarks and Evaluation — references

> Companion link library for **[Multimodal Benchmarks and Evaluation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/multimodal-benchmarks-and-evaluation/multimodal-benchmarks-and-evaluation)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See the flagship benchmark** — read [MMMU](https://arxiv.org/abs/2311.16502) — **Yue et al. (2024)**. *College-level multi-discipline questions with figures, diagrams and charts; the current headline number.*
2. **Learn why it needed a sequel** — read [MMMU-Pro](https://arxiv.org/abs/2409.02813) — **Yue et al. (2025)**. *Filters out text-only-solvable items, augments options, and adds a vision-only setting; scores drop hard, and that is the finding.*
3. **See the contamination argument** — read [Are We on the Right Way for Evaluating Large Vision-Language Models? (MMStar)](https://arxiv.org/abs/2403.20330) — **Chen et al. (2024)**. *Quantifies how many benchmark items need no image at all, and builds a vision-indispensable set.*
4. **Probe perception directly** — read [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/abs/2404.12390) — **Fu et al. (2024)**. *Tasks humans solve "in a blink" and models fail; the clearest picture of the perception gap.*
5. **Run the harness yourself** — use [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) — **LMMs-Lab**. *One command, 50+ tasks, reproducible prompts; without a shared harness, cross-paper comparisons are meaningless.*

**In this platform**:
- Related: [Cross-Validation](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) · [RAG Evaluation](/ai-ml/practitioner-workflows/llm-applications/rag-evaluation/rag-evaluation) — for multimodal retrieval pipelines
- The text-side equivalent: [LLM Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) · [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/evaluation/hallucination-and-grounding/hallucination-and-grounding)
- Prerequisites: [Visual Instruction Tuning (LLaVA)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/visual-instruction-tuning-llava/visual-instruction-tuning-llava) · [Modern Open VLM Architectures](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/modern-open-vlm-architectures/modern-open-vlm-architectures)

**Courses**:
- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro) — **Hugging Face** — includes how VLMs are evaluated and where the metrics mislead.
- [Stanford CS231n — Lecture 16, "Vision and Language" (slides)](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf) — **Stanford (Spring 2025)** — the benchmark landscape as taught alongside the models.

**Articles**:
- [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) — **LMMs-Lab** — the evaluation harness most 2025–26 VLM papers report through.
- [MMMU benchmark site and leaderboard](https://mmmu-benchmark.github.io/) — **MMMU team** — per-discipline breakdowns and the current standings; more informative than the headline average.
- [VHELM: Holistic Evaluation of Vision Language Models](https://crfm.stanford.edu/helm/vhelm/latest/) — **Stanford CRFM** — multi-aspect evaluation (bias, fairness, robustness, toxicity, knowledge), not one accuracy number.
- [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — which benchmarks the field currently takes seriously, and which it has retired.

**Papers**:
- [Are We on the Right Way for Evaluating Large Vision-Language Models? (MMStar)](https://arxiv.org/abs/2403.20330) — **Chen et al. (2024)** — measures text-only solvability and data leakage, then releases 1,500 vision-indispensable items.
- [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/abs/2404.12390) — **Fu et al. (2024)** — core visual perception tasks (depth, correspondence, forensics) where strong models are near chance.
- [Evaluating Object Hallucination in Large Vision-Language Models (POPE)](https://arxiv.org/abs/2305.10355) — **Li et al. (2023)** — the polling-based probe that made object hallucination measurable.
- [LMMs-Eval: Reality Check on the Evaluation of Large Multimodal Models](https://arxiv.org/abs/2407.12772) — **Zhang et al. (2025)** — the standard harness plus an analysis of contamination and benchmark redundancy.
- [MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](https://arxiv.org/abs/2409.02813) — **Yue et al. (2025)** — the hardened version, including a vision-only setting where the question is embedded in the image.
- [MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI](https://arxiv.org/abs/2311.16502) — **Yue et al. (2024)** — 11.5K expert-level questions across six disciplines; the reference multimodal reasoning benchmark.
