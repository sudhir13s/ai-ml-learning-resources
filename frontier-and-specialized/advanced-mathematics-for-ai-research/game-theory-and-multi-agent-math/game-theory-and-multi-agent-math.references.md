---
id: "19-advanced-math/game-theory-multi-agent/references"
topic: "Game Theory & Multi-Agent Math — References"
parent: "19-advanced-math/game-theory-multi-agent"
type: references
updated: 2026-09-14
---

# Game Theory & Multi-Agent Math — references

> Companion link library for **[Game Theory & Multi-Agent Math](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/game-theory-and-multi-agent-math/game-theory-and-multi-agent-math)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Get the five core ideas** — watch [Yale ECON-159, Lecture 1: five first lessons](https://www.youtube.com/watch?v=nM3rTU927io). *Dominance, best response, and why rational play can be self-defeating.*
2. **Nail Nash equilibrium** — watch [Game Theory 101 (#5): What Is a Nash Equilibrium?](https://www.youtube.com/watch?v=5TcYV6CZ7mI). *The single most important solution concept, cleanly.*
3. **See mixed strategies** — watch [What Is a Nash Equilibrium? (Stoplight Game)](https://www.youtube.com/watch?v=0i7p9DNvtjk). *Why randomizing can be optimal — the bridge to minimax.*
4. **Read the reference** — work [Multiagent Systems (Shoham & Leyton-Brown), Ch. 3–5](https://www.masfoundations.org/mas.pdf). *Normal/extensive games, equilibria, and computation, the free standard text.*
5. **Connect to ML** — read [GANs](https://arxiv.org/abs/1406.2661) and link to [bandits/RL](/ai-ml/ai-ml-learning-resources/reinforcement-learning/readme). *Minimax games, self-play, and learning dynamics in modern ML.*

**In this platform**:
- Prerequisite & related: [04 Convex Analysis & Duality (minimax)](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/convex-analysis-and-duality/convex-analysis-and-duality) · [14 Causal Inference (interventions)](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/causal-inference/causal-inference) · [09 Optimal Transport (WGAN)](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/optimal-transport-wasserstein/optimal-transport-wasserstein)
- Related domain (multi-agent decisions): [10. Reinforcement Learning](/ai-ml/ai-ml-learning-resources/reinforcement-learning/readme)
- Concept depth (the *why*): [ai-ml-intuitions 5.04 GANs & WGAN](/ai-ml/ai-ml-intuitions/generation/adversarial-generation/gans-and-wasserstein-gans-intuition) · [6.04 MDPs & Exploration](/ai-ml/ai-ml-intuitions/decision-making-and-control/mdps-and-environments/mdps-and-exploration-intuition)
- Where this math is applied today: [Multi-Agent Systems](/ai-ml/practitioner-workflows/agentic-systems/multi-agent-systems/multi-agent-systems) · [Multi-Agent Reinforcement Learning](/ai-ml/ai-ml-learning-resources/reinforcement-learning/multi-agent-reinforcement-learning/multi-agent-rl/multi-agent-rl)

**Videos**:
- [Game Theory — full Open Yale lecture](https://www.youtube.com/watch?v=M3oWYHYoBvk) — **Yale University (Ben Polak)** — the complete classroom treatment of strategic reasoning.
- [Game Theory 101 (#5): What Is a Nash Equilibrium?](https://www.youtube.com/watch?v=5TcYV6CZ7mI) — **William Spaniel** — the cleanest short explanation of Nash equilibrium.
- [Game Theory 101: What Is a Nash Equilibrium? (Stoplight Game)](https://www.youtube.com/watch?v=0i7p9DNvtjk) — **William Spaniel** — mixed strategies and the intuition behind randomization.
- [Yale ECON-159 — Lecture 1: Introduction, five first lessons](https://www.youtube.com/watch?v=nM3rTU927io) — **Ben Polak (Yale)** — dominance and best response, the foundations.

**Courses**:
- [Bandit Algorithms — free book](https://tor-lattimore.com/downloads/book/book.pdf) — **Lattimore & Szepesvári** — the single-agent decision theory that multi-agent learning generalizes, free from the author.
- [Game Theory (Open Yale ECON-159)](https://oyc.yale.edu/economics/econ-159) — **Ben Polak (Yale)** — the legendary full course: dominance, Nash, mixed strategies, signaling, free video + transcripts.
- [Multiagent Systems — free book & course](https://www.masfoundations.org/) — **Shoham & Leyton-Brown** — game theory, mechanism design, and multi-agent learning, fully free.

**Articles**:
- [Multiagent Systems — full free book](https://www.masfoundations.org/mas.pdf) — **Shoham & Leyton-Brown** — equilibria, computation of Nash, mechanism design, openly posted.
- [Open Yale Game Theory — lecture transcripts](https://oyc.yale.edu/economics/econ-159) — **Ben Polak** — the full course in readable transcript form, free.

**Papers**:
- [Game Theory and Multi-Agent Reinforcement Learning: From Nash Equilibria to Evolutionary Dynamics](https://arxiv.org/abs/2412.20523) — **(survey, 2024)** — the modern bridge from equilibria to MARL, free on arXiv.
- [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661) — **Goodfellow et al. (2014)** — generative modeling as a two-player minimax game, the flagship ML application.
- [Wasserstein GAN](https://arxiv.org/abs/1701.07875) — **Arjovsky, Chintala & Bottou (2017)** — reframes the GAN game with a better-behaved minimax objective.
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) — **Cemri, Pan, … Zaharia, Gonzalez & Stoica (UC Berkeley, 2025)** — where the theory meets 2026 practice: 1,600 annotated traces showing that multi-agent large-language-model (LLM) failures are coordination failures — misaligned incentives, no verification — not model failures.

**Books**:
- [Bandit Algorithms — **Ch. on adversarial bandits & game-theoretic learning**](https://tor-lattimore.com/downloads/book/book.pdf) — **Lattimore & Szepesvári** — no-regret learning as equilibrium-finding, free PDF.
- [Convex Optimization — **§5.4–5.8 (duality, minimax, saddle points)**](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) — **Boyd & Vandenberghe** — the minimax-duality math behind zero-sum games, free.
- [Multiagent Systems — **Ch. 3 (normal-form games), Ch. 5 (extensive-form), Ch. 7 (learning in games)**](https://www.masfoundations.org/mas.pdf) — **Shoham & Leyton-Brown** — the free standard text.
