---
id: "08-rl/ppo/references"
topic: "Proximal Policy Optimization (PPO) — References"
parent: "08-rl/ppo"
type: references
updated: 2026-09-14
---

# Proximal Policy Optimization (PPO) — references

> Companion link library for **[Proximal Policy Optimization (PPO)](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/proximal-policy-optimization-ppo/proximal-policy-optimization-ppo)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Build intuition** — watch [Arxiv Insights: Policy Gradients & PPO](https://www.youtube.com/watch?v=5P7I-xPq8u8). *The clearest visual story of the step-size problem and the clip that fixes it.*
2. **Read the canonical explainer** — [Spinning Up: PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html). *The clipped objective, GAE advantages, and the full update loop with pseudocode.*
3. **Get the derivation** — [Lilian Weng: Policy Gradient (PPO section)](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/). *PPO as a first-order approximation to TRPO's trust region.*
4. **Read the source + lecture** — [PPO paper](https://arxiv.org/abs/1707.06347) and [Deep RL Bootcamp Core Lecture 5 (Schulman)](https://sites.google.com/view/deep-rl-bootcamp/lectures). *The author's own framing, TRPO → PPO.*

**In this platform**:
- [10 Actor-Critic](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/actor-critic-a2c-a3c/actor-critic-a2c-a3c) — prereq.
- [11 TRPO](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/trust-region-policy-optimization-trpo/trust-region-policy-optimization-trpo) — prereq.
- [ai-ml-intuitions 6.03 PPO & RLHF](/ai-ml/ai-ml-intuitions/decision-making-and-control/stable-policy-optimization/ppo-and-rl-from-human-feedback-intuition) — concept depth (the *why*).
- [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — where RLHF for LLMs (PPO applied to language-model alignment, with reward models + DPO) lives; this card owns the PPO *mechanics* it relies on.
- [Reinforcement Learning for Reasoning — GRPO and RLVR](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining) — where PPO went next (2024–26): GRPO drops the value network and replaces the learned baseline with a group-relative one; the clipped surrogate on this page is still the core.

**Videos**:
- [An Introduction to Policy Gradient Methods (PPO)](https://www.youtube.com/watch?v=5P7I-xPq8u8) — **Arxiv Insights** — the intuition behind the clip and why PPO is stable.
- [Deep RL Bootcamp — Core Lecture 5: Natural Policy Gradients, TRPO, PPO](https://sites.google.com/view/deep-rl-bootcamp/lectures) — **John Schulman (Berkeley Deep RL Bootcamp, 2017)** — the author's own TRPO → PPO walkthrough; video and slides on the official bootcamp page.
- [RL Lecture 7: Policy Gradient Methods](https://www.youtube.com/watch?v=KHZVXao4qXs) — **David Silver (DeepMind)** — the policy-gradient foundation PPO constrains.

**Courses**:
- [Berkeley CS285 — Advanced Policy Gradients](http://rail.eecs.berkeley.edu/deeprlcourse/) — **UC Berkeley (Sergey Levine)** — PPO/TRPO derived from the trust-region view.
- [Hugging Face Deep RL Course — PPO unit](https://huggingface.co/learn/deep-rl-course/unit8/introduction) — **Hugging Face** — hands-on: implement and train PPO yourself.
- [Spinning Up — Proximal Policy Optimization](https://spinningup.openai.com/en/latest/algorithms/ppo.html) — **OpenAI** — the reference exposition: clipped objective, GAE, code.

**Articles**:
- [Policy Gradient Algorithms — PPO](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/) — **Lilian Weng** — PPO derived as first-order TRPO, with the clipping math.
- [Spinning Up — PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html) — **OpenAI** — the definitive open implementation guide.
- [The 37 Implementation Details of PPO](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/) — **Huang et al. (ICLR blog)** — the practical tricks that make PPO actually work.

**Papers**:
- [High-Dimensional Continuous Control with GAE](https://arxiv.org/abs/1506.02438) — **Schulman et al. (2016)** — the advantage estimator PPO uses in practice.
- [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) — **Schulman et al. (2017)** — the clipped-surrogate PPO and the adaptive-KL variant.
- [Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477) — **Schulman et al. (2015)** — the trust-region principle PPO approximates first-order.

**Books**:
- [Dive into Deep Learning — **Ch. 17 (Reinforcement Learning)**](https://d2l.ai/chapter_reinforcement-learning/index.html) — **Zhang et al.** — runnable RL foundations leading to policy optimization.
- [Reinforcement Learning: An Introduction (2nd ed.) — **Ch. 13 "Policy Gradient Methods"**](http://incompleteideas.net/book/RLbook2020.pdf) — **Sutton & Barto** — the policy-gradient backbone; PPO's clip is detailed in the papers above.
