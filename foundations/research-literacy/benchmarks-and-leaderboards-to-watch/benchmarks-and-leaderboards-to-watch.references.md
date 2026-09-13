---
id: "21-frontier/benchmarks-and-leaderboards/references"
topic: "Benchmarks & Leaderboards to Watch — References"
parent: "21-frontier/benchmarks-and-leaderboards"
type: references
updated: 2026-09-14
---

# Benchmarks & Leaderboards to Watch — references

> Companion link library for **[Benchmarks & Leaderboards to Watch](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/benchmarks-and-leaderboards-to-watch/benchmarks-and-leaderboards-to-watch)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Learn what benchmarks measure** — read [30 LLM benchmarks and how they work](https://www.evidentlyai.com/llm-guide/llm-benchmarks). *Each benchmark tests a narrow slice (knowledge, code, reasoning); knowing the slice is how you read a score correctly.*
2. **Watch the live leaderboards** — bookmark [LMArena](https://lmarena.ai/leaderboard) (human-preference Elo), [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) (reproducible open models) and [MTEB](https://huggingface.co/spaces/mteb/leaderboard) (embeddings). *Human-preference, task-level and retrieval rankings answer different questions; use the one that matches your decision.*
3. **Understand rigorous, multi-metric eval** — skim [Stanford HELM](https://crfm.stanford.edu/helm/). *HELM evaluates many models on many scenarios with many metrics — the antidote to single-number hype.*
4. **Know the failure modes** — read about contamination/saturation in the Chatbot Arena and benchmark-survey papers. *A benchmark stops being useful once it's saturated or leaks into training data; spotting this is the key skill.*
5. **Run an eval yourself** — try the [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) on a small model. *Reproducing a benchmark number teaches you how brittle and configuration-dependent these scores are.*

**In this platform**:
- [02 arXiv and Paper Discovery](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/arxiv-and-paper-discovery/arxiv-and-paper-discovery) — pair with.
- [11 Evaluating Hype vs Substance](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/evaluating-hype-vs-substance/evaluating-hype-vs-substance) — pair with.
- [12. Deployment & MLOps](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme) — evaluation depth lives in.
- [Frontier & Staying Current — concepts](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme) — per-concept index.
- [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — evaluation depth lives in.

**Videos**:
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the evaluation segment explains why benchmark scores and felt quality diverge.
- [How To Read AI Research Papers Effectively](https://www.youtube.com/watch?v=K6Wui3mn-uI) — **DeepLearningAI** — read the eval section critically: baselines, metrics, ablations.
- [PyTorch Paper Replicating (Vision Transformer)](https://www.youtube.com/watch?v=tjpW_BY8y3g) — **Daniel Bourke** — replicating reported numbers shows how configuration-sensitive benchmark results are.

**Courses**:
- [Hugging Face — Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — **Hugging Face** — an open, reproducible leaderboard whose methodology page is a mini-course in fair eval.
- [Stanford HELM](https://crfm.stanford.edu/helm/) — **Stanford CRFM** — a living, transparent evaluation suite; the docs teach what holistic evaluation should look like.

**Articles**:
- [30 LLM evaluation benchmarks and how they work](https://www.evidentlyai.com/llm-guide/llm-benchmarks) — **Evidently AI** — a clear catalogue of what each major benchmark measures.
- [Chatbot Arena — Benchmarking LLMs in the Wild with Elo](https://www.lmsys.org/blog/2023-05-03-arena/) — **LMSYS** — how human-preference ranking works and why it complements static tests.
- [Humanity's Last Exam](https://agi.safe.ai/) — **Center for AI Safety & Scale AI** — the current-frontier exam, with live results; useful precisely because scores are still low.
- [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — **Hugging Face / MTEB team** — embedding models ranked across retrieval, clustering and reranking; the first stop before choosing a RAG encoder.
- [SWE-bench and SWE-bench Verified](https://www.swebench.com/) — **Princeton NLP / OpenAI (Verified split)** — the live coding-agent leaderboard; Verified is the human-validated subset most 2026 claims quote.

**Papers**:
- [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132) — **Chiang et al. (2024)** — the Elo, human-preference leaderboard methodology.
- [Evaluating Large Language Models Trained on Code (HumanEval)](https://arxiv.org/abs/2107.03374) — **Chen et al. (2021)** — the pass@k code benchmark behind "coding ability" claims.
- [Holistic Evaluation of Language Models (HELM)](https://arxiv.org/abs/2211.09110) — **Liang et al. (2022)** — multi-metric, multi-scenario evaluation; the case against single-number rankings.
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) — **Phan et al. (2025)** — expert-written questions designed to stay unsaturated as frontier models improve.
- [Measuring Massive Multitask Language Understanding (MMLU)](https://arxiv.org/abs/2009.03300) — **Hendrycks et al. (2021)** — the 57-subject knowledge benchmark; the canonical "broad knowledge" score.
- [MMLU-Pro](https://arxiv.org/abs/2406.01574) — **Wang et al. (2024), NeurIPS** — the harder, less contaminated MMLU used by Open LLM Leaderboard v2.
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — **Jimenez et al. (2024), ICLR** — the benchmark that moved coding evaluation from snippets to repositories.
- [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879) — **Singh et al. (2025)** — how arena rankings are distorted by private testing and selective disclosure.

**Books**:
- [Dive into Deep Learning](https://d2l.ai/) — **Zhang et al.** — its evaluation chapters ground the metrics that benchmarks aggregate.
- [Speech and Language Processing, 3rd ed. — Ch. on evaluation](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky & Martin** — the reference on NLP metrics (BLEU, F1, perplexity) that underlie many leaderboards.
