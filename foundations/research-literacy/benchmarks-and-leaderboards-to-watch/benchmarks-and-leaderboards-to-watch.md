---
id: "21-frontier/benchmarks-and-leaderboards"
topic: "Benchmarks & Leaderboards to Watch"
parent: "21-frontier"
level: intermediate
built_from: ["model-evaluation-basics"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Benchmarks & Leaderboards to Watch"
minutes: 10
category: research-literacy
---

# Benchmarks & Leaderboards to Watch
> The standardized tasks and public rankings that let you compare models objectively — and the
> skill of reading them critically (what a benchmark measures, where it saturates, and how it gets
> gamed). Leaderboards are how the field tracks progress; knowing which to trust is half the battle.

**Why it matters:** "how would you evaluate / which model is best for X?" is a core interview and
on-the-job question. You need to know the major benchmarks, what each actually tests, and the
failure modes — contamination, saturation, and overfitting to the leaderboard — so you don't
mistake a high score for real capability.

**The 2026 short list** — the older ones (MMLU, HumanEval) are saturated and now serve mainly as
sanity checks:

- **LMArena** — human-preference Elo across chat models; the closest thing to a general ranking.
- **Open LLM Leaderboard v2** — reproducible open-model scores on harder tasks (MMLU-Pro, GPQA, MuSR, math).
- **SWE-bench Verified** — real GitHub issues resolved end to end; the coding-agent yardstick.
- **Humanity's Last Exam (HLE)** and **GPQA** — expert-level questions built to resist saturation.
- **MTEB** — the embedding/retrieval leaderboard behind RAG stack choices.

**Start here — suggested path:**

1. **Learn what benchmarks measure** — read [30 LLM benchmarks and how they work](https://www.evidentlyai.com/llm-guide/llm-benchmarks). *Each benchmark tests a narrow slice (knowledge, code, reasoning); knowing the slice is how you read a score correctly.*
2. **Watch the live leaderboards** — bookmark [LMArena](https://lmarena.ai/leaderboard) (human-preference Elo), [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) (reproducible open models) and [MTEB](https://huggingface.co/spaces/mteb/leaderboard) (embeddings). *Human-preference, task-level and retrieval rankings answer different questions; use the one that matches your decision.*
3. **Understand rigorous, multi-metric eval** — skim [Stanford HELM](https://crfm.stanford.edu/helm/). *HELM evaluates many models on many scenarios with many metrics — the antidote to single-number hype.*
4. **Know the failure modes** — read about contamination/saturation in the Chatbot Arena and benchmark-survey papers. *A benchmark stops being useful once it's saturated or leaks into training data; spotting this is the key skill.*
5. **Run an eval yourself** — try the [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) on a small model. *Reproducing a benchmark number teaches you how brittle and configuration-dependent these scores are.*

## Courses (free)
- [Stanford HELM](https://crfm.stanford.edu/helm/) — **Stanford CRFM** — a living, transparent evaluation suite; the docs teach what holistic evaluation should look like.
- [Hugging Face — Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — **Hugging Face** — an open, reproducible leaderboard whose methodology page is a mini-course in fair eval.

## Videos
- [How To Read AI Research Papers Effectively](https://www.youtube.com/watch?v=K6Wui3mn-uI) — **DeepLearningAI** — read the eval section critically: baselines, metrics, ablations.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the evaluation segment explains why benchmark scores and felt quality diverge.
- [PyTorch Paper Replicating (Vision Transformer)](https://www.youtube.com/watch?v=tjpW_BY8y3g) — **Daniel Bourke** — replicating reported numbers shows how configuration-sensitive benchmark results are.

## Key Papers
- [Measuring Massive Multitask Language Understanding (MMLU)](https://arxiv.org/abs/2009.03300) — **Hendrycks et al. (2021)** — the 57-subject knowledge benchmark; the canonical "broad knowledge" score.
- [Evaluating Large Language Models Trained on Code (HumanEval)](https://arxiv.org/abs/2107.03374) — **Chen et al. (2021)** — the pass@k code benchmark behind "coding ability" claims.
- [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132) — **Chiang et al. (2024)** — the Elo, human-preference leaderboard methodology.
- [Holistic Evaluation of Language Models (HELM)](https://arxiv.org/abs/2211.09110) — **Liang et al. (2022)** — multi-metric, multi-scenario evaluation; the case against single-number rankings.
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — **Jimenez et al. (2024), ICLR** — the benchmark that moved coding evaluation from snippets to repositories.
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) — **Phan et al. (2025)** — expert-written questions designed to stay unsaturated as frontier models improve.
- [MMLU-Pro](https://arxiv.org/abs/2406.01574) — **Wang et al. (2024), NeurIPS** — the harder, less contaminated MMLU used by Open LLM Leaderboard v2.
- [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879) — **Singh et al. (2025)** — how arena rankings are distorted by private testing and selective disclosure.

## Articles / Blogs (free, no paywall)
- [30 LLM evaluation benchmarks and how they work](https://www.evidentlyai.com/llm-guide/llm-benchmarks) — **Evidently AI** — a clear catalogue of what each major benchmark measures.
- [Chatbot Arena — Benchmarking LLMs in the Wild with Elo](https://www.lmsys.org/blog/2023-05-03-arena/) — **LMSYS** — how human-preference ranking works and why it complements static tests.
- [SWE-bench and SWE-bench Verified](https://www.swebench.com/) — **Princeton NLP / OpenAI (Verified split)** — the live coding-agent leaderboard; Verified is the human-validated subset most 2026 claims quote.
- [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — **Hugging Face / MTEB team** — embedding models ranked across retrieval, clustering and reranking; the first stop before choosing a RAG encoder.
- [Humanity's Last Exam](https://agi.safe.ai/) — **Center for AI Safety & Scale AI** — the current-frontier exam, with live results; useful precisely because scores are still low.

## Books (free, with chapters)
- [Dive into Deep Learning](https://d2l.ai/) — **Zhang et al.** — its evaluation chapters ground the metrics that benchmarks aggregate.
- [Speech and Language Processing, 3rd ed. — Ch. on evaluation](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky & Martin** — the reference on NLP metrics (BLEU, F1, perplexity) that underlie many leaderboards.

## In this platform
- Per-concept index: [Frontier & Staying Current — concepts](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme)
- Pair with: [02 arXiv & Papers with Code](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/arxiv-and-papers-with-code/arxiv-and-papers-with-code) · [11 Evaluating Hype vs Substance](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/evaluating-hype-vs-substance/evaluating-hype-vs-substance)
- Evaluation depth lives in: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme) · [12. Deployment & MLOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
