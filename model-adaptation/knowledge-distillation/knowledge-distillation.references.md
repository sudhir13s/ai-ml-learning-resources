---
id: "09-llms/knowledge-distillation/references"
topic: "Knowledge Distillation — References"
parent: "09-llms/knowledge-distillation"
type: references
updated: 2026-09-13
---

# Knowledge Distillation — references

> Companion link library for **[Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Build intuition** — watch [Knowledge Distillation in Neural Networks — Explained!](https://www.youtube.com/watch?v=BUCSTKQOzcM) (**CodeEmporium**). *Teacher and student, soft targets, and temperature in plain terms.*
2. **Read the source** — read [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) (**Hinton, Vinyals & Dean, 2015**). *Soft targets, temperature, and the $T^2$ factor — short and foundational.*
3. **See it in code** — run [Knowledge Distillation Tutorial](https://docs.pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html) (**PyTorch**). *A teacher-to-student run end to end, cell by cell.*
4. **Connect to language models** — read [DistilBERT, a distilled version of BERT](https://arxiv.org/abs/1910.01108) (**Sanh et al., 2019**). *The canonical compression result: 40% smaller, about 97% of the performance.*
5. **Go to generation** — read [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947) (**Kim & Rush, 2016**). *Distilling on teacher generations — the form that powers modern small LLMs.*

**In this platform**:
- [Chain-of-Thought Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) — the reasoning a student learns when rationales are distilled.
- [Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — where a smaller distilled model pays off at serving time.
- [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation) — the concept page.
- [Knowledge distillation intuition (7.04)](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/knowledge-distillation-intuition) — the one-page mental model.
- [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/language-modeling-objectives/language-modeling-objectives) — the next-token objective distillation matches against.
- [LoRA and PEFT](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — the cheap way to fine-tune a student on teacher data.
- [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) — the stage where distillation can replace hard-label training outright.
- [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — the lever that stores a model in fewer bits instead of training a smaller one.
- [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) — fine-tuning on synthetic teacher data is distillation by another name.

**Videos**:
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — where distilled small models and synthetic-data training fit in the modern LLM landscape.
- [Knowledge Distillation in Neural Networks — Explained!](https://www.youtube.com/watch?v=BUCSTKQOzcM) — **CodeEmporium** — the clearest conceptual intro: teacher and student, soft targets, temperature.
- [Stanford CS336 — Language Modeling from Scratch, Spring 2025 (lectures)](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — distillation alongside quantization and pruning in the efficiency lectures, costed against a real training budget.

**Courses**:
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — distillation within the full efficiency and compression stack for LLMs.

**Articles**:
- [Knowledge Distillation — illustrated walkthrough](https://nn.labml.ai/distillation/index.html) — **labml.ai** — an annotated, runnable PyTorch implementation of the Hinton loss, line by line.
- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) — **Lilian Weng** — distillation in the broader inference-compression toolbox, next to quantization and pruning.

**Papers**:
- [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116) — **Xu et al. (2024)** — black-box distillation from API models, synthetic data generation, rationale and preference distillation, and the licensing question.
- [Born-Again Neural Networks](https://arxiv.org/abs/1805.04770) — **Furlanello et al. (2018)** — self-distillation into a same-size student that beats its teacher, isolating the regularization benefit of soft targets.
- [DistilBERT, a distilled version of BERT](https://arxiv.org/abs/1910.01108) — **Sanh et al. (2019)** — the triple loss and teacher layer initialization; 40% smaller, 60% faster, about 97% of BERT's GLUE score.
- [Distilling Step-by-Step!](https://arxiv.org/abs/2305.02301) — **Hsieh et al. (2023, Google)** — distill a teacher's chain-of-thought rationales so a small student reasons well with less data.
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — **Hinton, Vinyals & Dean (2015)** — the founding paper and the page's source for the tempered softmax, the KD loss and the $T^2$ derivation.
- [FitNets: Hints for Thin Deep Nets](https://arxiv.org/abs/1412.6550) — **Romero et al. (2014)** — feature distillation: regress student hidden layers onto teacher hints; the page's source for that flavor.
- [Gemma 2: Improving Open Language Models at a Practical Size](https://arxiv.org/abs/2408.00118) — **Gemma team, Google DeepMind (2024)** — distillation as the pretraining objective itself, beating same-size models trained on hard labels.
- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) — **Gou et al. (2021)** — the standard survey and source of the response, feature and relation taxonomy used on the page.
- [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) — **Gu et al. (2023, ICLR 2024)** — reverse KL so the student concentrates on the teacher's high-probability modes instead of covering them all.
- [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947) — **Kim & Rush (2016)** — distill on the teacher's generated sequences; the page's source for sequence-level KD.
- [TinyBERT: Distilling BERT for Natural Language Understanding](https://arxiv.org/abs/1909.10351) — **Jiao et al. (2019)** — embeddings, hidden states and attention matrices distilled in two stages; the page's source for TinyBERT.

**Documentation**:
- [Knowledge Distillation Tutorial](https://docs.pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html) — **PyTorch** — the soft-target loss, the temperature, and a CIFAR teacher-to-student run you can execute cell by cell.
- [LLM inference optimization](https://huggingface.co/docs/transformers/en/llm_optims) — **Hugging Face Transformers** — distillation and quantization for practical inference speedups.

**Books**:
- [Dive into Deep Learning](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — the computational-performance chapters that frame compression.
- [Speech and Language Processing, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky & Martin** — softmax, cross-entropy, and the language-modeling objective distillation matches against.

**Resources**:
- [DistilBERT distillation example (archived at v4.40)](https://github.com/huggingface/transformers/tree/v4.40.0/examples/research_projects/distillation) — **Hugging Face** — the actual DistilBERT training code to read and adapt, pinned to the last release that carried `research_projects/`.
