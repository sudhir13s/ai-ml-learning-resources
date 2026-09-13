---
id: "model-adaptation/reinforcement-learning-posttraining/references"
topic: "Reinforcement Learning Post-training — References"
parent: "model-adaptation/reinforcement-learning-posttraining"
type: references
updated: 2026-09-13
---

# Reinforcement Learning Post-training — references

> Companion link library for **[Reinforcement Learning for Reasoning — GRPO and Verifiable Rewards](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See why RL produces reasoning** — watch [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (**Andrej Karpathy**). *The RL section is the clearest account of why rewarding verifiable answers makes long thinking emerge.*
2. **Map the landscape** — read [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) (**Sebastian Raschka**). *The four ways reasoning is built: inference-time scaling, pure RL, SFT plus RL, and distillation.*
3. **Follow the recipe** — read [DeepSeek R1's recipe to replicate o1](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1) (**Nathan Lambert**). *R1-Zero, the cold-start SFT, reasoning RL, rejection sampling and general RL, stage by stage.*
4. **Go to the primary source** — read [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) (**DeepSeek-AI, 2025**). *The emergent "aha moment" and the response length that grows with training.*
5. **Get the algorithm exactly** — read [*Reinforcement Learning from Human Feedback* — "Policy Gradient Algorithms"](https://rlhfbook.com/c/11-policy-gradients.html) (**Nathan Lambert**). *PPO and GRPO derived side by side, matching the page's derivation.*
6. **Build one** — run [reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch) (**Sebastian Raschka**). *Reasoning methods coded on a small open model; pair it with the [video series](https://www.youtube.com/watch?v=Kh9mqTzjuEQ).*

**In this platform**:
- [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) — the reasoning behaviour being trained.
- [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation) — compressing a trained reasoner into a smaller dense model.
- [LLM Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) — how a reasoning model's gains are measured.
- [Policy Gradients and REINFORCE](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/policy-gradients-reinforce/policy-gradients-reinforce) — the estimator underneath PPO and GRPO.
- [PPO and RL from Human Feedback Intuition](/ai-ml/ai-ml-intuitions/decision-making-and-control/stable-policy-optimization/ppo-and-rl-from-human-feedback-intuition) — the clipped update, intuition first.
- [Preference and Alignment Training (RLHF & DPO)](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training) — the prerequisite: the PPO objective, KL leash and value model GRPO modifies.
- [Proximal Policy Optimization](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/proximal-policy-optimization-ppo/proximal-policy-optimization-ppo) — PPO as an RL algorithm.
- [Reward Shaping](/ai-ml/ai-ml-learning-resources/reinforcement-learning/foundations/reward-shaping/reward-shaping) — why reward design decides what gets learned.
- [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) — the cold-start stage before reasoning RL.
- [Synthetic Data and Data Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation) — where cold-start and rejection-sampled data come from.
- [Test-Time Computation and Scaling](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/test-time-computation-and-scaling/test-time-computation-and-scaling) — spending the trained ability at inference.
- [Test-Time Computation Intuition](/ai-ml/ai-ml-intuitions/reasoning-and-agency/reasoning/test-time-computation-intuition) — thinking longer, visually.

**Videos**:
- [Build a Reasoning Model From Scratch — Motivation and Code Setup](https://www.youtube.com/watch?v=Kh9mqTzjuEQ) — **Sebastian Raschka** — opens the series that codes reasoning methods on a small open base model.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the RL section is the clearest explanation of why RL on verifiable answers produces reasoning.
- [Stanford CS336 — Lecture 1: Overview and Tokenization](https://www.youtube.com/watch?v=SQ3fZ1sAqXI) — **Stanford Online** — entry point to the series whose later lectures cover SFT and RL.

**Courses**:
- [Hugging Face LLM Course — Open R1 for Students](https://huggingface.co/learn/llm-course/chapter12/1) — **Hugging Face** — RL for language models, the DeepSeek-R1 paper, and implementing GRPO.
- [Reasoning with o1](https://www.deeplearning.ai/short-courses/reasoning-with-o1/) — **DeepLearning.AI and OpenAI** — what a reasoning model changes for the person using it.
- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang & Tatsunori Hashimoto (Stanford)** — reasoning RL inside the full model-building stack.

**Articles**:
- [DeepSeek R1's recipe to replicate o1](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1) — **Nathan Lambert (Interconnects)** — the R1 pipeline, stage by stage.
- [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) — **OpenAI (2024)** — accuracy rising with both train-time RL and test-time thinking.
- [Open-R1: a fully open reproduction of DeepSeek-R1](https://huggingface.co/blog/open-r1) — **Hugging Face** — what had to be rebuilt to reproduce R1.
- [Reward Hacking in Reinforcement Learning](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) — **Lilian Weng** — why a learned reward gets gamed, and where even a verifiable one leaks.
- [Tülu 3: The next era in open post-training](https://allenai.org/blog/tulu-3) — **Allen Institute for AI** — the RLVR stage explained in plain terms.
- [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) — **Sebastian Raschka** — the four ways reasoning is built, with the R1 variants mapped onto them.
- [Why We Think](https://lilianweng.github.io/posts/2025-05-01-thinking/) — **Lilian Weng (2025)** — the deepest survey of test-time thinking and RL for reasoning.

**Papers**:
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) — **DeepSeek-AI (2025)** — R1-Zero's pure RL, the cold-start fix, and distillation into dense models.
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning](https://arxiv.org/abs/2402.03300) — **Shao et al. (2024)** — introduces GRPO; §4 holds the critic-free objective.
- [gpt-oss-120b and gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925) — **OpenAI (2025)** — open-weight reasoning models with reasoning-effort levels.
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) — **Lightman et al. (2023)** — process supervision beats outcome supervision; the origin of the PRM-versus-ORM debate.
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) — **Qwen Team (2025)** — thinking and non-thinking modes in one model, with a thinking budget.
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) — **Zelikman et al. (2022)** — the pre-RL ancestor: keep chains that reach the right answer and fine-tune on them.
- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124) — **Lambert et al. (2024)** — names RLVR and publishes a reproducible post-training stack.

**Books**:
- [*Build a Reasoning Model (From Scratch)*](https://www.manning.com/books/build-a-reasoning-model-from-scratch) — **Sebastian Raschka** — the book behind the video series and companion code; pointer only.
- [*Reinforcement Learning from Human Feedback* — "Policy Gradient Algorithms"](https://rlhfbook.com/c/11-policy-gradients.html) — **Nathan Lambert** — PPO and GRPO derived side by side.
- [*Reinforcement Learning from Human Feedback* — "Reasoning and Inference-Time Scaling"](https://rlhfbook.com/c/14-reasoning.html) — **Nathan Lambert** — the definitive written treatment of RLVR and GRPO variants.
- [*Reinforcement Learning from Human Feedback* — "Reward Models"](https://rlhfbook.com/c/07-reward-models.html) — **Nathan Lambert** — outcome versus process reward models, and when a verifier replaces both.

**Resources**:
- [Open-R1](https://github.com/huggingface/open-r1) — **Hugging Face** — the open reproduction of the R1 pipeline: GRPO training code, datasets, evaluation.
- [reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch) — **Sebastian Raschka** — companion code for building reasoning methods on a small open model.
