---
id: "09-llms/knowledge-distillation/references"
topic: "Knowledge Distillation — References"
parent: "09-llms/knowledge-distillation"
type: references
updated: 2026-09-07
---

# Knowledge Distillation — references and further reading

> Companion link library for **[Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation)** (the concept page). This file holds the curated links — external sources *and* internal links to related pages on this platform — kept separate so it can be reused as a standalone reference list. Grouped by type, best-first within each group. Every entry is free/open and chosen for depth on *this* topic. The papers cited for formulas on the concept page all appear under **Papers** below.

**Start here — suggested path**:
1. **Build intuition** — watch [Knowledge Distillation in Neural Networks — Explained!](https://www.youtube.com/watch?v=BUCSTKQOzcM) (**CodeEmporium**). *Teacher/student, soft targets, and temperature in plain terms — the cleanest conceptual intro.*
2. **Read the source** — read [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) (**Hinton, Vinyals & Dean, 2015**). *Soft targets, temperature, and the $T^2$ factor — short and foundational.*
3. **See it in code** — follow the [PyTorch Knowledge Distillation tutorial](https://docs.pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html) (**PyTorch**). *Implement teacher→student distillation end to end yourself.*
4. **Connect to LLMs** — read [DistilBERT](https://arxiv.org/abs/1910.01108) (**Sanh et al., 2019**). *The canonical compression result: 40% smaller, ~97% of the performance.*
5. **Go to generation** — read [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947) (**Kim & Rush, 2016**). *Distilling on teacher generations — the form that powers modern small LLMs.*

**Videos**:
- [Knowledge Distillation in Neural Networks — Explained!](https://www.youtube.com/watch?v=BUCSTKQOzcM) — **CodeEmporium** — the clearest conceptual intro: teacher/student, soft targets, temperature.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — where distilled small models and synthetic-data training fit in the modern LLM landscape.
- [Stanford CS336 — Language Modeling from Scratch, Spring 2025 (lectures)](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — distillation alongside quantization and pruning in the efficiency lectures, costed against a real training budget.

**Interactive & hands-on**:
- [Knowledge Distillation tutorial (runnable notebook)](https://docs.pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html) — **PyTorch** — the soft-target loss, the temperature, and a CIFAR teacher→student run you can execute cell by cell.
- [Hugging Face — DistilBERT distillation example (archived at v4.40)](https://github.com/huggingface/transformers/tree/v4.40.0/examples/research_projects/distillation) — **Hugging Face** — the actual DistilBERT distillation code (triple loss, layer init) to read and adapt; pinned to the last release that carried it, since `research_projects/` was removed from `main`.

**Courses (free)**:
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — distillation within the full efficiency/compression stack for LLMs.
- [Hugging Face — LLM optimization guide](https://huggingface.co/docs/transformers/en/llm_optims) — **Hugging Face** — distillation and quantization for practical inference speedups.

**Articles / blogs (free, no paywall)**:
- [Knowledge Distillation — PyTorch tutorial](https://docs.pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html) — **PyTorch** — hands-on teacher→student with the soft-target KD loss, well annotated.
- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) — **Gou et al. (2021)** — the comprehensive map of the field: response/feature/relation, offline/online/self, with a clear taxonomy.
- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) — **Lilian Weng (OpenAI)** — distillation in the broader inference-compression toolbox (with quantization and pruning).
- [Knowledge Distillation — illustrated walkthrough](https://nn.labml.ai/distillation/index.html) — **labml.ai** — an annotated, runnable PyTorch implementation of the Hinton KD loss, line by line.

**Papers**:
- [Born-Again Neural Networks](https://arxiv.org/abs/1805.04770) — **Furlanello et al. (2018)** — self-distillation into an identically-sized student that *beats* the teacher; isolates the regularization benefit of soft targets.
- [DistilBERT, a distilled version of BERT](https://arxiv.org/abs/1910.01108) — **Sanh et al. (2019)** — the triple loss (soft-target + MLM + cosine-embedding), layer-init from the teacher; 40% smaller, 60% faster, ~97% of BERT's GLUE.
- [Distilling Step-by-Step!](https://arxiv.org/abs/2305.02301) — **Hsieh et al. (Google, 2023)** — distill a teacher's chain-of-thought *rationales* so a small student reasons like a big one with less data; the reasoning-distillation idea.
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — **Hinton, Vinyals & Dean (2015)** — the founding paper: soft targets, temperature, and the $T^2$ gradient-rescaling factor. *(Concept-page source for the softmax-with-temperature, the KD loss, and the $T^2$ derivation.)*
- [FitNets: Hints for Thin Deep Nets](https://arxiv.org/abs/1412.6550) — **Romero et al. (2014)** — feature-based distillation: regress student hidden layers onto teacher "hints," enabling thinner-and-deeper students. *(Concept-page source for feature distillation.)*
- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) — **Gou et al. (2021)** — the standard survey; the source of the response/feature/relation and offline/online/self taxonomy used on the page.
- [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947) — **Kim & Rush (2016)** — distill on the teacher's *generated sequences* rather than per-token soft targets; the generation/LLM-relevant form. *(Concept-page source for sequence-level KD.)*
- [TinyBERT: Distilling BERT for Natural Language Understanding](https://arxiv.org/abs/1909.10351) — **Jiao et al. (2019)** — multi-component feature distillation (embeddings, hidden states, **attention matrices**) in a two-stage scheme. *(Concept-page source for TinyBERT.)*
- [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) — **Gu et al. (2023, ICLR 2024)** — swaps forward KL for **reverse** KL so the student stops trying to cover the teacher's whole distribution and instead concentrates on its high-probability modes; the correction that makes generative distillation work.
- [Gemma 2: Improving Open Language Models at a Practical Size](https://arxiv.org/abs/2408.00118) — **Gemma team, Google DeepMind (2024)** — distillation used as the *pretraining* objective, not a post-hoc compression step: train the 2B and 9B models on a large teacher's full token distribution and beat same-size models trained on hard labels. The 2025-26 reason small open models are as good as they are.
- [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116) — **Xu et al. (2024)** — the modern map: black-box distillation from API models, self-instruct data generation, rationale and preference distillation, plus the licensing question every practitioner hits.

**Books (free chapters)**:
- [Dive into Deep Learning](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — the efficiency/computational-performance chapters that frame compression (distillation, quantization, pruning).
- [Speech and Language Processing, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky & Martin** — softmax, cross-entropy, and the LM objective that distillation matches against.

**In this platform**:
- Concept page (full explanation): [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation)
- The other compression levers: [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) · [Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)
- Builds on these: [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/language-modeling-objectives/language-modeling-objectives) · [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining)
- Distillation targets these: [Chain-of-Thought Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) (reasoning distillation) · [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) (synthetic-data fine-tuning is distillation) · [LoRA and PEFT](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning)
- Concept depth (the *why*): [Module 7.04 Knowledge Distillation](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/knowledge-distillation-intuition)
