---
id: "llms-applications-and-agents/training-and-adaptation"
topic: "Training and Adaptation"
level: advanced
built_from: ["large-language-model-foundations", "optimization-and-training"]
updated: 2026-09-07
---

# Training and Adaptation

> Everything that happens to a base model after pretraining. Post-training is now where most of a
> model's perceived quality comes from: demonstrations teach it to answer, instruction diversity
> makes it generalize to unseen task types, preference data makes it pleasant, and reinforcement
> learning against verifiable rewards makes it *reason*. The eight pages follow that pipeline in
> order, then add the cheap tricks — adapters, distillation, merging — that make it affordable.

**Start here:** [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/supervised-fine-tuning/supervised-fine-tuning) — the same next-token loss as pretraining, with curated demonstrations and a response-masked objective; every later page is a variation on it.

## Concept index

Each page is a self-contained resource card with a curated `.references.md` companion where one
exists: a plain-words definition, why it matters in 2026, a five-step start-here path, and
verified courses, videos, papers, articles and books.

### Teaching the model to answer

1. [Supervised Fine-Tuning (SFT)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/supervised-fine-tuning/supervised-fine-tuning) — curated demonstration pairs and response masking; what makes post-training different from more pretraining.
2. [Instruction Tuning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/instruction-tuning/instruction-tuning) — SFT scaled across many task types, and the task-count curve that produces zero-shot generalization.
3. [Synthetic Data and Data Curation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/synthetic-data-and-data-curation/synthetic-data-and-data-curation) — filtering, deduplication and quality classification, plus generating and then filtering model-written data.

### Doing it cheaply

4. [LoRA and Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — low-rank updates, QLoRA, adapters; rank selection and what merging a LoRA actually does.
5. [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/knowledge-distillation/knowledge-distillation) — the teacher's soft distribution as a training signal, and why the relative ranking of wrong answers carries information.

### Shaping behaviour

6. [RLHF and DPO (preference alignment)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/preference-and-alignment-training/preference-and-alignment-training) — the Bradley-Terry reward model, the proximal-policy-optimization loop with its KL penalty, and the direct-preference alternative that removes both.
7. [Reinforcement Learning for Reasoning — GRPO and Verifiable Rewards](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/reinforcement-learning-for-reasoning-grpo-and-rlvr/reinforcement-learning-for-reasoning-grpo-and-rlvr) — group-relative policy optimization against graders, tests and compilers; how long chains of thought are learned rather than prompted.

### Combining what you trained

8. [Model Merging and Weight Averaging](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/model-merging-and-weight-averaging/model-merging-and-weight-averaging) — task vectors, TIES and DARE; several specialisations in one deployment, with no gradients.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the post-training and alignment lectures place every page of this sub-area in one pipeline.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; the SFT and preference-tuning chapters run on the `trl` library you would actually use.
- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/index) — **Hugging Face** — the canonical guide to LoRA, QLoRA, adapters, prompt tuning and (IA)³, doubling as a tutorial.
- [Open-R1](https://github.com/huggingface/open-r1) — **Hugging Face** — the fully open reproduction of the R1 reasoning pipeline: GRPO training code, datasets and evaluation, all inspectable.

## Videos

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the clearest tour of pretraining → SFT → RLHF, with what each stage does and does not fix.
- [Stanford CS336 — Lecture 1: Overview and Tokenization](https://www.youtube.com/watch?v=SQ3fZ1sAqXI) — **Stanford Online** — the entry point to the lecture series whose later post-training lectures cover SFT, preference tuning and RLVR.
- [Reinforcement Learning from Human Feedback (RLHF), Clearly Explained](https://www.youtube.com/watch?v=qPN_XZcJf_s) — **StatQuest with Josh Starmer** — the preference-data and Bradley-Terry reward model at a gentle pace.
- [Direct Preference Optimization (DPO) explained: Bradley-Terry model, log probabilities, math](https://www.youtube.com/watch?v=hvGa5Mba4c8) — **Umar Jamil** — the DPO derivation worked through on screen, the best free companion to the paper.

## Key Papers

- [Training Language Models to Follow Instructions with Human Feedback (InstructGPT)](https://arxiv.org/abs/2203.02155) — **Ouyang et al. (2022)** — the three-stage recipe (SFT, reward model, PPO) that the whole industry copied.
- [Finetuned Language Models Are Zero-Shot Learners (FLAN)](https://arxiv.org/abs/2109.01652) — **Wei et al. (2021)** — introduces instruction tuning, with the task-count scaling curve.
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — **Rafailov et al. (2023)** — preference alignment with no reward model and no reinforcement-learning loop, derived in full.
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO)](https://arxiv.org/abs/2402.03300) — **Shao et al. (2024)** — critic-free group-relative policy optimization, the optimizer behind the reasoning-model wave.
- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) — **Zhou et al. (2023)** — around a thousand high-quality examples rivalling far larger noisy mixes; the strongest statement of the quality-over-quantity case.
- [Self-Instruct: Aligning LMs with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) — **Wang et al. (2022)** — bootstrap instruction data from the model itself; the recipe underneath most open instruction sets.

## Articles / Blogs (free, no paywall)

- [Finetuning Large Language Models](https://magazine.sebastianraschka.com/p/finetuning-large-language-models) — **Sebastian Raschka** — instruction tuning versus plain SFT, data quality, and the gotchas, in one readable piece.
- [LLM Training: RLHF and Its Alternatives](https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives) — **Sebastian Raschka** — the preference-tuning landscape mapped: RLHF, DPO and the variants worth knowing.
- [Tülu 3: The next era in open post-training](https://allenai.org/blog/tulu-3) — **Allen Institute for AI** — a complete open post-training recipe with the RLVR stage explained in plain language.
- [Parameter-Efficient Fine-Tuning (PEFT)](https://huggingface.co/blog/peft) — **Hugging Face** — LoRA and QLoRA in practice, with the memory numbers.
- [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) — **Stanford CRFM** — the canonical cheap instruction-tuning recipe and the moment post-training became accessible.

## Books (free, with chapters)

- [*Reinforcement Learning from Human Feedback* — "Reward Models"](https://rlhfbook.com/c/07-reward-models.html) — **Nathan Lambert** — free online; outcome versus process reward models, and when a verifier replaces both.
- [*Reinforcement Learning from Human Feedback* — "Reasoning and Inference-Time Scaling"](https://rlhfbook.com/c/14-reasoning.html) — **Nathan Lambert** — the definitive written treatment of RLVR and the GRPO variants.
- [*Speech and Language Processing*, 3rd ed. — Ch. 12 "Model Alignment, Prompting and In-Context Learning"](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky and Martin** — free draft; instruction tuning inside the alignment chapter.
- [*A Survey of Large Language Models* — §5 Instruction Tuning and Alignment](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — book-length free reference mapping the dataset and method landscape.

## In this platform

- Section index: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- Before this: [Large Language Model Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/readme) · Alongside: [LLM Model Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/readme) · [Inference and Runtime](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/readme) · [Reasoning, Evaluation and Alignment](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/readme)
- The reinforcement-learning machinery these pages borrow: [Proximal Policy Optimization (PPO)](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/policy-learning/proximal-policy-optimization-ppo/proximal-policy-optimization-ppo) · [Policy Gradients (REINFORCE)](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/policy-learning/policy-gradients-reinforce/policy-gradients-reinforce)
- What the trained model is judged by: [LLM Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation) · [Safety and Alignment](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/safety-and-alignment/safety-and-alignment)
- Where the training compute comes from: [Distributed Training — Parallelism, FSDP and ZeRO](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero)
- The mental models: [LoRA](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/adaptation/lora-intuition) · [Knowledge Distillation](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/knowledge-distillation-intuition) · [Transfer Learning and Fine-Tuning](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/adaptation/transfer-learning-and-fine-tuning-intuition) · [PPO and RLHF](/ai-ml/ai-ml-intuitions/decision-making-and-control/stable-policy-optimization/ppo-and-rl-from-human-feedback-intuition)
- Doing it rather than reading it: [Fine-Tuning workflow](/ai-ml/practitioner-workflows/training-and-adaptation/fine-tuning) · [Preference Alignment workflow](/ai-ml/practitioner-workflows/training-and-adaptation/preference-alignment) · [Synthetic Data Generation workflow](/ai-ml/practitioner-workflows/data-and-inputs/synthetic-data-generation)
