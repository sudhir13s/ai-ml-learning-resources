---
id: "model-adaptation"
topic: "Model Adaptation"
level: advanced
built_from: ["large-language-models", "model-building", "optimization-and-training"]
updated: 2026-09-13
---

# Model Adaptation

> Everything that changes a model after pretraining. Post-training is now where most of a
> model's perceived quality comes from: demonstrations teach it to answer, instruction diversity
> makes it generalize to unseen task types, preference data makes it pleasant, and reinforcement
> learning against verifiable rewards makes it *reason*. The seven resource pages follow that
> pipeline in order, then add the cheap tricks — adapters, distillation, merging — that make
> it affordable; the two courses at the end do it end to end — a seven-page fine-tuning run and
> the eight-page build that turns a base checkpoint into a chat model.

**Start here:** [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) — the same next-token loss as pretraining, with curated demonstrations and a response-masked objective; every later page is a variation on it.

## Concept index

Each page is a self-contained resource card with a curated `.references.md` companion where one
exists: a plain-words definition, why it matters in 2026, a five-step start-here path, and
verified courses, videos, papers, articles and books.

### Teaching the model to answer

1. [Supervised Fine-Tuning (SFT)](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) — curated demonstration pairs and response masking; what makes post-training different from more pretraining.
2. [Instruction Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/instruction-tuning/instruction-tuning) — SFT scaled across many task types, and the task-count curve that produces zero-shot generalization.

The data these stages consume — filtering, deduplication, quality classification, and generating then filtering model-written data — is [Synthetic Data and Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation) in the data section.

### Doing it cheaply

3. [LoRA and Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — low-rank updates, QLoRA, adapters; rank selection and what merging a LoRA actually does.
4. [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation) — the teacher's soft distribution as a training signal, and why the relative ranking of wrong answers carries information.

### Shaping behaviour

5. [RLHF and DPO (preference alignment)](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training) — the Bradley-Terry reward model, the proximal-policy-optimization loop with its KL penalty, and the direct-preference alternative that removes both.
6. [Reinforcement Learning Post-Training — GRPO and Verifiable Rewards](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining) — group-relative policy optimization against graders, tests and compilers; how long chains of thought are learned rather than prompted.

### Combining what you trained

7. [Model Merging](/ai-ml/ai-ml-learning-resources/model-adaptation/model-merging/model-merging) — task vectors, TIES and DARE, weight averaging; several specialisations in one deployment, with no gradients.

### Doing it, end to end

8. [Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/decide-whether-to-fine-tune) — **7 pages** — decide whether to fine-tune at all, prepare instruction data, build the supervised baseline, apply LoRA and QLoRA, tune and debug the run, evaluate capability and regression, and ship a production fine-tuning pipeline.
9. [Build a Small Chat Model](/ai-ml/ai-ml-learning-resources/model-adaptation/build-a-small-chat-model/from-base-model-to-assistant) — **8 pages** — the base checkpoint from [Model Building](/ai-ml/ai-ml-learning-resources/model-building/readme) turned into something you can talk to: conversation templating, multi-turn loss masking, supervised fine-tuning, preference alignment, a regression check, quantization and a chat loop.

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

- Before this section: [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) · [Model Building](/ai-ml/ai-ml-learning-resources/model-building/readme) · After it: [Inference and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/readme) · [Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/readme)
- The reinforcement-learning machinery these pages borrow: [Proximal Policy Optimization (PPO)](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/proximal-policy-optimization-ppo/proximal-policy-optimization-ppo) · [Policy Gradients (REINFORCE)](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/policy-gradients-reinforce/policy-gradients-reinforce)
- What the trained model is judged by: [Model Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) · [Alignment and Safety Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/alignment-and-safety-evaluation/alignment-and-safety-evaluation)
- Where the training compute comes from: [Distributed Training — Parallelism, FSDP and ZeRO](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero)
- The mental models: [LoRA](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/adaptation/lora-intuition) · [Knowledge Distillation](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/knowledge-distillation-intuition) · [Transfer Learning and Fine-Tuning](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/adaptation/transfer-learning-and-fine-tuning-intuition) · [PPO and RLHF](/ai-ml/ai-ml-intuitions/decision-making-and-control/stable-policy-optimization/ppo-and-rl-from-human-feedback-intuition)
- Workflows that harvest in here at W3: [Preference Alignment](/ai-ml/practitioner-workflows/training-and-adaptation/preference-alignment) · [Synthetic Data Generation](/ai-ml/practitioner-workflows/data-and-inputs/synthetic-data-generation) · The production spine the chat build points at: [small-chat-model](/python/python-production-examples/small-chat-model/readme)
