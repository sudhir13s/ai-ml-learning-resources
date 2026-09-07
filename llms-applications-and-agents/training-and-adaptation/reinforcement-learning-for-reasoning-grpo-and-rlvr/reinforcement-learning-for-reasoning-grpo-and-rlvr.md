---
id: "llms-applications-and-agents/training-and-adaptation/reinforcement-learning-for-reasoning-grpo-and-rlvr"
topic: "Reinforcement Learning for Reasoning — GRPO and Verifiable Rewards"
level: advanced
built_from: ["preference-and-alignment-training", "supervised-fine-tuning", "chain-of-thought-and-reasoning"]
leads_to: ["llms-applications-and-agents/reasoning-evaluation-and-alignment/test-time-computation-and-scaling", "09-llms/llm-evaluation-and-benchmarks"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Reinforcement Learning for Reasoning — GRPO and Verifiable Rewards"
minutes: 18
category: training-and-adaptation
---

# Reinforcement Learning for Reasoning — GRPO and Verifiable Rewards

> Reasoning models are trained, not prompted. Instead of a learned reward model scoring how *nice*
> an answer sounds, **reinforcement learning with verifiable rewards (RLVR)** scores whether the
> answer is *checkably correct* — a math grader, a unit test, a compiler — and optimises the policy
> against that ground truth. The model discovers long chains of thought on its own because longer
> thinking earns more reward.

**Why it matters:** this is the single biggest capability shift of 2024–2026 (o1 → DeepSeek-R1 → o3,
Qwen3, gpt-oss) and the most-asked frontier question in interviews today.

- **What is probed:** why a *verifiable* reward dodges reward hacking that a learned reward model cannot; how **group relative policy optimization (GRPO)** removes proximal policy optimization's (PPO) value network by using a group mean as the baseline; outcome reward models (ORM) versus process reward models (PRM).
- **The trap:** calling this "RLHF for math." RLHF optimises a *learned* human-preference proxy; RLVR optimises a *checker*. Different reward source, different failure modes, different data pipeline.
- **The other trap:** assuming R1-Zero (pure RL, no supervised fine-tuning (SFT)) is the recipe. The shipped DeepSeek-R1 adds an SFT cold start precisely because pure RL produced unreadable, language-mixed chains.

**Start here — suggested path:**

1. **Get the landscape in one read** — read [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) — **Sebastian Raschka**. *The four ways reasoning is built (inference-time scaling, pure RL, SFT+RL, distillation), with the R1 variants mapped onto them.*
2. **Read the recipe from the people who reverse-engineered it** — read [DeepSeek R1's recipe to replicate o1](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1) — **Nathan Lambert (Interconnects)**. *R1-Zero → cold-start SFT → reasoning RL → rejection sampling → general RL, stage by stage.*
3. **Read the primary source** — read [DeepSeek-R1](https://arxiv.org/abs/2501.12948) — **DeepSeek-AI (2025)**. *The paper that made the recipe public: the emergent "aha moment," the length-grows-with-training curve, the distilled dense models.*
4. **Get the algorithm exactly right** — read the [RLHF Book — "Policy Gradient Algorithms"](https://rlhfbook.com/c/11-policy-gradients.html) — **Nathan Lambert**. *PPO and GRPO derived side by side; where the value network goes and what replaces it.*
5. **Build one** — watch [Build a Reasoning Model From Scratch, part 1](https://www.youtube.com/watch?v=Kh9mqTzjuEQ) — **Sebastian Raschka**, then work through the free companion repo [reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch). *Reasoning methods coded on top of a small open base model — the abstraction becomes concrete.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang & Tatsunori Hashimoto (Stanford)** — the post-training and alignment lectures place reasoning RL inside the full model-building stack; slides, assignments and lecture list are free on the course site.
- [Open-R1](https://github.com/huggingface/open-r1) — **Hugging Face** — the fully open reproduction of the R1 pipeline: GRPO training code, datasets, evaluation. The closest thing to a lab you can actually run.
- [Reasoning with o1](https://www.deeplearning.ai/short-courses/reasoning-with-o1/) — **DeepLearning.AI × OpenAI** — free short course on what a reasoning model changes for the person *using* it (prompting, planning, cost).

## Videos

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the reinforcement-learning section is the clearest existing explanation of why RL on verifiable answers produces reasoning, and how it differs from SFT.
- [Build a Reasoning Model From Scratch — Motivation and Code Setup](https://www.youtube.com/watch?v=Kh9mqTzjuEQ) — **Sebastian Raschka** — opens the from-scratch series that codes reasoning methods on a small open base model.
- [Stanford CS336 — Lecture 1: Overview and Tokenization](https://www.youtube.com/watch?v=SQ3fZ1sAqXI) — **Stanford Online** — the entry point to the lecture series whose later post-training lectures cover SFT and RL.

## Key Papers

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) — **DeepSeek-AI (2025)** — the open recipe: R1-Zero's pure RL, the cold-start SFT fix, and distillation into dense models.
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning](https://arxiv.org/abs/2402.03300) — **Shao et al. (2024)** — introduces **GRPO**; read §4 for the critic-free objective everyone now cites.
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) — **Lightman et al. (2023)** — process supervision beats outcome supervision; the origin of the PRM-versus-ORM debate.
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) — **Zelikman et al. (2022)** — the pre-RL ancestor: keep the chains that reach the right answer, fine-tune on them, repeat.
- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124) — **Lambert et al. (2024)** — the paper that named **RLVR** and published a full, reproducible post-training stack.
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) — **Qwen Team (2025)** — thinking/non-thinking modes in one model plus a thinking budget; the 2025 open-weight reasoning reference.
- [gpt-oss-120b and gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925) — **OpenAI (2025)** — OpenAI's open-weight reasoning models: reasoning-effort levels and the chain-of-thought monitoring argument.

## Articles / Blogs (free, no paywall)

- [Why We Think](https://lilianweng.github.io/posts/2025-05-01-thinking/) — **Lilian Weng (2025)** — the deepest free survey of test-time thinking: latent versus verbalised reasoning, RL for reasoning, faithfulness of chains.
- [Reward Hacking in Reinforcement Learning](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) — **Lilian Weng** — why a learned reward gets gamed, and why a verifiable one is the structural fix (and where even that leaks).
- [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) — **OpenAI (2024)** — the o1 announcement: accuracy rising with both train-time RL and test-time thinking.
- [Open-R1: a fully open reproduction of DeepSeek-R1](https://huggingface.co/blog/open-r1) — **Hugging Face** — what actually had to be rebuilt to reproduce R1, including the parts the paper leaves out.
- [Tülu 3: The next era in open post-training](https://allenai.org/blog/tulu-3) — **Allen Institute for AI** — the open post-training recipe end to end, with the RLVR stage explained in plain terms.

## Books (free, with chapters)

- [*Reinforcement Learning from Human Feedback* — "Reasoning and Inference-Time Scaling"](https://rlhfbook.com/c/14-reasoning.html) — **Nathan Lambert** — free online book; the definitive written treatment of RLVR, GRPO variants and reasoning-training practice.
- [*Reinforcement Learning from Human Feedback* — "Reward Models"](https://rlhfbook.com/c/07-reward-models.html) — **Nathan Lambert** — outcome versus process reward models, and when a verifier replaces both.
- [*Build a Reasoning Model (From Scratch)*](https://www.manning.com/books/build-a-reasoning-model-from-scratch) — **Sebastian Raschka** — paid book, free companion code and chapter hub at [sebastianraschka.com/reasoning-from-scratch](https://sebastianraschka.com/reasoning-from-scratch/); pointer only.

## In this platform

- Prerequisite (canonical home of RLHF, PPO and DPO): [Preference and Alignment Training](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/preference-and-alignment-training/preference-and-alignment-training) · [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/supervised-fine-tuning/supervised-fine-tuning)
- The reasoning behaviour being trained: [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning)
- What you spend the trained ability on at inference: [Test-Time Computation and Scaling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/test-time-computation-and-scaling/test-time-computation-and-scaling)
- The RL machinery underneath: [Proximal Policy Optimization](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/policy-learning/proximal-policy-optimization-ppo/proximal-policy-optimization-ppo) · [Policy Gradients and REINFORCE](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/policy-learning/policy-gradients-reinforce/policy-gradients-reinforce) · [Reward Shaping](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/foundations/reward-shaping/reward-shaping)
- Where the data for the cold start comes from: [Synthetic Data and Data Curation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/synthetic-data-and-data-curation/synthetic-data-and-data-curation) · compressing a reasoner: [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/knowledge-distillation/knowledge-distillation)
- How the result is measured: [LLM Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation)
- Intuition track: [PPO and RL from Human Feedback](/ai-ml/ai-ml-intuitions/decision-making-and-control/stable-policy-optimization/ppo-and-rl-from-human-feedback-intuition) · [Test-Time Computation](/ai-ml/ai-ml-intuitions/reasoning-and-agency/reasoning/test-time-computation-intuition)
- Build it as a workflow: [Preference Alignment](/ai-ml/practitioner-workflows/workflow-library/training-and-adaptation/preference-alignment)
