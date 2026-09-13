---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/references"
topic: "Program Synthesis and Code Reasoning — References"
parent: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning"
type: references
updated: 2026-09-14
---

# Program Synthesis and Code Reasoning — references

> Companion link library for **[Program Synthesis and Code Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/program-synthesis-and-code-reasoning)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Get the classical framing** — read [Program Synthesis](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/10/program_synthesis_now.pdf) — **Gulwani, Polozov & Singh (2017)**. *Specifications, search spaces, and search strategies, before neural methods enter.*
2. **See the neuro-symbolic version** — read [DreamCoder](https://arxiv.org/abs/2006.08381) — **Ellis, Wong, Nye et al. (2020)**. *A wake-sleep loop that grows its own library of abstractions while a neural recognition model guides search.*
3. **See it scale with language models** — read [Competition-Level Code Generation with AlphaCode](https://arxiv.org/abs/2203.07814) — **Li, Choi, Chung et al. (2022)**. *Massive sampling, filtered by executing the given tests — search plus a verifier, at scale.*
4. **Use code as a reasoning substrate** — read [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435) — **Gao, Madaan, Zhou et al. (2022)**. *Let the model write the program and the interpreter do the arithmetic; the accuracy gain is the argument for symbolic offloading.*
5. **Check the 2025-26 evidence** — read [ARC Prize 2025: results and analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis) — **ARC Prize Foundation (Chollet, Knoop et al.)**. *Iterative program refinement against a feedback signal was the year's defining technique.*

**In this platform**:
- The applied owner (canonical home): [Code Agents](/ai-ml/practitioner-workflows/agentic-systems/coding-and-computer-use-agents/code-agents) · [Computer-Use and GUI Agents](/ai-ml/practitioner-workflows/agentic-systems/coding-and-computer-use-agents/computer-use-and-gui-agents)
- Prerequisites: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Neural Theorem Proving](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving/neural-theorem-proving)
- Related: [Tool Use and Function Calling](/ai-ml/practitioner-workflows/agentic-systems/tool-use/tool-use) · [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) · [LLM Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks)

**Videos**:
- [Chasing Real AGI: Inside ARC Prize 2025](https://www.youtube.com/watch?v=qzb1y9gT0Sg) — **François Chollet and Mike Knoop (The MAD Podcast)** — what actually worked in the 2025 competition, including test-time program refinement.
- [Pattern Recognition vs True Intelligence](https://www.youtube.com/watch?v=JTU8Ha4Jyfc) — **François Chollet (Machine Learning Street Talk)** — the creator of the ARC benchmark on why program search, not memorization, is the missing capability.

**Courses**:
- [Introduction to Program Synthesis](https://people.csail.mit.edu/asolar/SynthesisCourse/) — **Armando Solar-Lezama (MIT)** — the free canonical course: specifications, constraint-based synthesis, enumerative search, and sketching.
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — the prerequisite if you want to understand the generative half rather than call it.

**Articles**:
- [ARC Prize 2025: results and analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis) — **ARC Prize Foundation** — the clearest current account of where program-search methods stand against frontier models.
- [ARC Prize resources](https://arcprize.org/resources) — **ARC Prize Foundation** — datasets, baselines, and papers, all open.
- [Competitive programming with AlphaCode](https://deepmind.google/discover/blog/competitive-programming-with-alphacode/) — **Google DeepMind** — the authors' own walkthrough of sampling, filtering, and clustering.
- [SWE-bench](https://www.swebench.com/) — **Princeton NLP** — the live leaderboard and task format; the most-cited practical measure of code agents.

**Papers**:
- [ARC Prize 2024: Technical Report](https://arxiv.org/abs/2412.04604) — **Chollet, Knoop, Kamradt & Landers (2024)** — what program-synthesis approaches achieved on abstraction and reasoning, measured honestly.
- [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://arxiv.org/abs/2502.19411) — **Yang, Liu, Zhang et al. (2025)** — the current survey of the two-way relationship between code and reasoning.
- [Competition-Level Code Generation with AlphaCode](https://arxiv.org/abs/2203.07814) — **Li et al., DeepMind (2022)** — generate-and-filter at competition scale, with the filtering analysis that matters more than the headline.
- [DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning](https://arxiv.org/abs/2006.08381) — **Ellis, Wong, Nye et al. (2020)** — library learning plus neural search; the reference neuro-symbolic synthesis system.
- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) — **Chen, Tworek, Jun et al., OpenAI (2021)** — Codex and HumanEval: functional correctness as the metric, which reframed the whole area.
- [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435) — **Gao, Madaan, Zhou et al. (2022)** — offload computation to an interpreter; reasoning stays in the model, execution does not.
- [Program of Thoughts Prompting](https://arxiv.org/abs/2211.12588) — **Chen, Ma, Wang & Cohen (2022)** — the same separation, derived independently, with the numerical-reasoning evaluation.
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — **Jimenez, Yang, Wettig et al. (2023)** — the benchmark that moved evaluation from snippets to repositories, verified by the project's own tests.

**Books**:
- [*Program Synthesis*](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/10/program_synthesis_now.pdf) — **Gulwani, Polozov & Singh (2017)** — free monograph; still the best structured survey of the classical search techniques neural methods now guide.
