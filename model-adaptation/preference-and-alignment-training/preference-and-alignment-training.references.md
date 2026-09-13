---
id: "09-llms/rlhf-and-dpo/references"
topic: "RLHF & DPO — References"
parent: "09-llms/rlhf-and-dpo"
type: references
updated: 2026-09-13
---

# RLHF & DPO — references

> Companion link library for **[RLHF & DPO](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training)** and its two chapters. External sources and internal links, grouped by type and alphabetical within each group. Every entry is from a primary author or a recognized deep explainer.

**Start here — suggested path**:
1. **Build intuition** — watch [Reinforcement Learning with Human Feedback (RLHF), Clearly Explained](https://www.youtube.com/watch?v=qPN_XZcJf_s) (**StatQuest**). *The three-stage pipeline without the heavy math.*
2. **See the pipeline drawn** — read [Illustrating Reinforcement Learning from Human Feedback](https://huggingface.co/blog/rlhf) (**Hugging Face**). *Reward model, PPO loop and KL penalty, visually.*
3. **Follow the DPO derivation** — watch [Direct Preference Optimization (DPO) explained](https://www.youtube.com/watch?v=hvGa5Mba4c8) (**Umar Jamil**), then the derivation section of the concept page. *The implicit reward and the cancelling partition function, slowly.*
4. **Read the sources** — [InstructGPT](https://arxiv.org/abs/2203.02155), then [DPO](https://arxiv.org/abs/2305.18290). *The full RLHF recipe, then the reward-model-free alternative.*
5. **Run it for real** — work through the [DPO Trainer docs](https://huggingface.co/docs/trl/dpo_trainer) (**Hugging Face TRL**) alongside [Running and evaluating an alignment run](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training-running-and-evaluating-alignment). *The recipe, its logged implicit rewards, and how to judge the result.*

- **In this platform**:
  - [Alignment and Safety Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/alignment-and-safety-evaluation/alignment-and-safety-evaluation) — refusal, red-teaming and over-refusal checks for an aligned model.
  - [Data Preparation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme) — curating, deduplicating and splitting the prompts behind a preference set.
  - [Instruction Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/instruction-tuning/instruction-tuning) — the stage usually run before preference alignment.
  - [LoRA and Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — the adapters that let a 7B DPO run fit one GPU.
  - [Policy Gradients and REINFORCE](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/policy-gradients-reinforce/policy-gradients-reinforce) — the gradient estimator underneath PPO.
  - [Policy Gradients Intuition](/ai-ml/ai-ml-intuitions/decision-making-and-control/policy-learning/policy-gradients-intuition) — how a reward signal nudges a policy, visually.
  - [PPO and RL from Human Feedback Intuition](/ai-ml/ai-ml-intuitions/decision-making-and-control/stable-policy-optimization/ppo-and-rl-from-human-feedback-intuition) — the clipped update and the KL leash, intuition first.
  - [Preference Alignment: Preference Data and Reward Models](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training-preference-data-and-reward-models) — the collection loop, quality gates and reward-model training.
  - [Preference Alignment: Running and Evaluating an Alignment Run](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training-running-and-evaluating-alignment) — sizing, a runnable PPO step, the DPO recipe, win-rate and pitfalls.
  - [Proximal Policy Optimization](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/proximal-policy-optimization-ppo/proximal-policy-optimization-ppo) — PPO as an RL algorithm, outside language models.
  - [Reinforcement Learning for Reasoning (GRPO and RLVR)](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining) — the same RL machinery pointed at verifiable rewards, with GRPO's group baseline.
  - [RLHF & DPO](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training) — the concept page these references support.
  - [RLHF Alignment Production Example](/python/python-production-examples/rlhf-alignment/readme) — pair collection, a DPO run against a frozen reference, and a measured before-and-after win-rate.
  - [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) — the prerequisite stage and the source of the reference model.
  - [Synthetic Data and Data Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation) — generating and filtering AI-labelled preference data.
- **Videos**:
  - [Direct Preference Optimization (DPO) explained: Bradley-Terry model, log probabilities, math](https://www.youtube.com/watch?v=hvGa5Mba4c8) — **Umar Jamil** — the full DPO derivation, slowly, with the log-probability bookkeeping.
  - [Direct Preference Optimization (DPO) — math insight explained](https://www.youtube.com/watch?v=PZ6k5T5s5lY) — **Ricardo Calix** — the DPO objective and its equivalence to RLHF.
  - [DPO — fine-tune LLMs without reinforcement learning](https://www.youtube.com/watch?v=k2pD3k1485A) — **Luis Serrano** — DPO intuition, clearly.
  - [Reinforcement Learning with Human Feedback (RLHF), Clearly Explained](https://www.youtube.com/watch?v=qPN_XZcJf_s) — **StatQuest (Josh Starmer)** — the gentlest correct overview of the pipeline.
  - [RLHF explained with math derivations and PyTorch code](https://www.youtube.com/watch?v=qGyFrqc34yc) — **Umar Jamil** — reward model, PPO and KL, derived and coded line by line.
- **Courses**:
  - [Hugging Face Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) — **Hugging Face** — policy gradients and PPO from scratch, hands-on.
  - [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — the course whose fine-tuning chapters use TRL's trainers.
  - [Hugging Face LLM Course — Open R1 for Students](https://huggingface.co/learn/llm-course/chapter12/1) — **Hugging Face** — RL for language models, the DeepSeek-R1 paper, and implementing GRPO.
  - [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — reward modeling, PPO and DPO inside the full post-training stack.
- **Articles**:
  - [Illustrating Reinforcement Learning from Human Feedback (RLHF)](https://huggingface.co/blog/rlhf) — **Hugging Face** — the canonical illustrated explainer.
  - [LLM Training: RLHF and Its Alternatives](https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives) — **Sebastian Raschka** — RLHF, DPO and the preference-tuning landscape.
  - [Preference Tuning LLMs with Direct Preference Optimization Methods](https://huggingface.co/blog/pref-tuning) — **Hugging Face** — DPO, IPO and KTO compared on 7B models, with the β sensitivity measured.
  - [RLHF: Reinforcement Learning from Human Feedback](https://huyenchip.com/2023/05/02/rlhf.html) — **Chip Huyen** — a clear, systems-minded walkthrough.
  - [The N Implementation Details of RLHF with PPO](https://huggingface.co/blog/the_n_implementation_details_of_rlhf_with_ppo) — **Shengyi Huang, Tianlin Liu, Leandro von Werra (Hugging Face)** — the details that decide whether a PPO-RLHF reproduction works.
- **Papers**:
  - [A General Theoretical Paradigm to Understand Learning from Human Preferences (IPO)](https://arxiv.org/abs/2310.12036) — **Azar et al. (2023)** — fixes DPO's tendency to overfit the preference margin.
  - [A Survey of Large Language Models — §5 Alignment Tuning](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — RLHF and its alternatives, book-length.
  - [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) — **Bai et al. (2022)** — RLAIF: AI feedback against written principles replaces human labels.
  - [Deep Reinforcement Learning from Human Preferences](https://arxiv.org/abs/1706.03741) — **Christiano et al. (2017)** — the origin of learning a reward from pairwise comparisons.
  - [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) — **DeepSeek-AI (2025)** — GRPO against verifiable rewards, with reasoning emerging from RL.
  - [DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO)](https://arxiv.org/abs/2402.03300) — **Shao et al. (2024)** — introduces critic-free group relative policy optimization.
  - [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) — **Rafailov et al. (2023)** — the DPO derivation and loss in full.
  - [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438) — **Schulman et al. (2015)** — GAE, the advantage recipe PPO-RLHF uses.
  - [KTO: Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306) — **Ethayarajh et al. (2024)** — alignment from unpaired good/bad labels.
  - [Learning to Summarize from Human Feedback](https://arxiv.org/abs/2009.01325) — **Stiennon et al. (2020)** — the reward-model plus PPO recipe, bridging Christiano to InstructGPT.
  - [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) — **Touvron et al. (2023)** — a detailed chat recipe with rejection sampling and PPO.
  - [ORPO: Monolithic Preference Optimization without Reference Model](https://arxiv.org/abs/2403.07691) — **Hong, Lee & Thorne (2024)** — preference tuning folded into SFT, no reference model.
  - [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) — **Schulman et al. (2017)** — the clipped-surrogate algorithm RLHF uses.
  - [Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons](https://www.jstor.org/stable/2334029) — **Bradley & Terry (1952)** — the pairwise-comparison model behind the reward-model loss.
  - [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760) — **Gao, Schulman & Hilton (2022)** — the Goodhart over-optimization curve, measured.
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://arxiv.org/abs/2405.14734) — **Meng, Xia & Chen (2024)** — length-normalized implicit reward plus a target margin, no reference model.
  - [Training Language Models to Follow Instructions with Human Feedback (InstructGPT)](https://arxiv.org/abs/2203.02155) — **Ouyang et al. (2022)** — the canonical three-stage RLHF pipeline, with annotator-agreement and reward-model accuracy figures.
  - [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124) — **Lambert et al. (2024)** — a fully open SFT, DPO and RLVR recipe with data and evaluation.
- **Documentation**:
  - [DPO Trainer](https://huggingface.co/docs/trl/dpo_trainer) — **Hugging Face TRL** — the `DPOTrainer` API, loss variants, and the implicit-reward metrics it logs.
  - [Reward Modeling](https://huggingface.co/docs/trl/reward_trainer) — **Hugging Face TRL** — the `RewardTrainer` API, preference formats and logged accuracy.
  - [TRL — Transformers Reinforcement Learning](https://huggingface.co/docs/trl/index) — **Hugging Face** — the trainer catalog: SFT, reward modeling, DPO, GRPO, RLOO and the experimental variants.
- **Books**:
  - [*A Little Bit of Reinforcement Learning from Human Feedback* (the RLHF Book)](https://rlhfbook.com/) — **Nathan Lambert** — the free, continuously updated book on post-training: reward models, PPO, DPO, GRPO and RLVR in one notation.
  - [*AI Engineering*](https://huyenchip.com/books/) — **Chip Huyen (O'Reilly, 2025)** — the finetuning chapter's treatment of preference tuning; pointer only.
  - [*Speech and Language Processing*, 3rd ed. — "Model Alignment, Prompting and In-Context Learning"](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky & Martin** — RLHF in the alignment chapter.
