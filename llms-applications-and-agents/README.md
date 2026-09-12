---
id: "09-llms"
topic: "Applications and Agents"
level: advanced
built_from: ["large-language-models", "inference-and-serving"]
updated: 2026-09-13
---

# LLMs, Applications and Agents
> The two application-layer sub-areas of this library — retrieval-augmented generation and
> agentic AI — held here until they harvest into Practitioner Workflows, where the application
> layer of the AI/ML hub lives. The model-layer sub-areas that used to sit beside them have
> already moved to their lifecycle homes (listed below).

**⭐ Start here:** [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **Andrej Karpathy** — the best 1-hour mental model of how LLMs work, before building anything on one.

## Sub-areas still here

1. [RAG and Knowledge Systems](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/overview) — retrieval foundations, chunking, embedding models, vector and hybrid search, reranking, query transformation, advanced and agentic RAG, graph RAG, citations and evaluation.
2. [Agentic AI](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/overview) — the agent loop, tools, memory, planning, reflection, multi-agent systems, context engineering, the Model Context Protocol and agent-to-agent protocols, coding and computer-use agents, evaluation, safety and prompt injection.

## Where the rest went (the model layer, by lifecycle stage)

- **What an LLM is** — objectives, the decoder-only shape, scaling laws, the redesigned attention block, long context, mixture-of-experts, diffusion language models, prompting and reasoning → [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme)
- **Pretraining** → [Model Building](/ai-ml/ai-ml-learning-resources/model-building/readme)
- **Post-training** — SFT, instruction tuning, LoRA, distillation, preference training, reinforcement-learning post-training, merging → [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme)
- **Serving** — KV cache, decoding, speculative decoding, quantization, batching, caching, packaging → [Inference and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/readme)
- **Measuring it** — benchmarks, hallucination, alignment and safety → [Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/readme)
- **Synthetic data and curation** → [Data and Representation](/ai-ml/ai-ml-learning-resources/data-and-representation/readme)

## Courses (free)
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — fine-tuning, RLHF, deployment, free.
- [Stanford CS324 — Large Language Models](https://stanford-cs324.github.io/winter2022/) — **Stanford** — capabilities, harms, scaling, alignment; lecture notes free.

## Videos
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — pretraining → SFT → RLHF, end to end.

## Key Papers
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — **Brown et al. (2020)** — in-context learning emerges.
- [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — the field map (pretraining → adaptation → use → eval).

## Articles / Blogs (free, no paywall)
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — **Lilian Weng** — the canonical map of the agent loop and its failure modes.
- [Understanding Large Language Models](https://magazine.sebastianraschka.com/p/understanding-large-language-models) — **Sebastian Raschka** — a curated path through the key papers.

## Books (free, with chapters)
- [Speech and Language Processing, 3rd ed. — **Ch. 10 "Large Language Models"**](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky & Martin** — the standard reference chapter, free PDF.

## In this platform
- Build one: [project_06 ChatGPT-from-scratch](../../AI-ML-problemsets/projects/project_06_chatgpt_from_scratch/) · Intuition: [Module 8 — LLMs & Agentic Systems](/ai-ml/ai-ml-intuitions/reasoning-and-agency) · Systems: [LLM Systems curriculum](/ai-ml/ai-ml-learning-resources/meta/llm-systems-curriculum)
- Doing it rather than reading it: [RAG Pipeline workflow](/ai-ml/practitioner-workflows/llm-applications/rag-pipeline/01-decide-whether-rag-is-needed) · [Agent Building workflow](/ai-ml/practitioner-workflows/agentic-systems/agent-building/01-do-you-need-an-agent)
