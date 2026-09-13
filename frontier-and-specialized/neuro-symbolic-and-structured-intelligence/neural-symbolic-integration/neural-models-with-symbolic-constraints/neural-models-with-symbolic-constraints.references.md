---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints/references"
topic: "Neural Models with Symbolic Constraints — References"
parent: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints"
type: references
updated: 2026-09-14
---

# Neural Models with Symbolic Constraints — references

> Companion link library for **[Neural Models with Symbolic Constraints](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints/neural-models-with-symbolic-constraints)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Get the soft version** — read [A Semantic Loss Function for Deep Learning with Symbolic Knowledge](https://arxiv.org/abs/1711.11157) — **Xu, Zhang, Friedman, Liang & Van den Broeck (2017)**. *A logical formula becomes the probability the network satisfies it; the negative logarithm is the loss.*
2. **Get the hard version** — read [Semantic Probabilistic Layers for Neuro-Symbolic Learning](https://proceedings.neurips.cc/paper_files/paper/2022/file/c182ec594f38926b7fcb827635b9a8f4-Paper-Conference.pdf) — **Ahmed, Teso, Chang, Van den Broeck & Vergari (2022)**. *A final layer whose support is exactly the set of constraint-satisfying outputs — a guarantee, not a penalty.*
3. **Constrain a real decoder** — work through [Outlines](https://github.com/dottxt-ai/outlines) — **Willard & Louf (.txt)**. *Regular expressions and grammars compiled into token masks; ten lines to make invalid JSON impossible.*
4. **Understand the fast path** — read [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](https://arxiv.org/abs/2411.15100) — **Dong, Ruan, Cai et al. (2024)**. *Splitting the vocabulary into context-independent and context-dependent tokens is why grammar masking is now free.*
5. **Learn the price** — read [Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models](https://arxiv.org/abs/2408.02442) — **Tam, Wu, Tsai, Lin, Lee & Chen (2024)**. *Evidence that format constraints trade reasoning accuracy for parseability, and how to recover it.*

**In this platform**:
- The relaxations in full: [Differentiable Logic](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-logic/differentiable-logic) · [Rules, Constraints and Ontologies](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/rules-constraints-and-ontologies/rules-constraints-and-ontologies)
- Prerequisites: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Symbolic Knowledge as Neural Input](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/symbolic-knowledge-as-neural-input/symbolic-knowledge-as-neural-input)
- Next in this sub-area: [Symbolic Reasoning over Neural Representations](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/symbolic-reasoning-over-neural-representations/symbolic-reasoning-over-neural-representations)
- Where it ships: [Tool Use and Function Calling](/ai-ml/practitioner-workflows/agentic-systems/tool-use/tool-use) · [Code Agents](/ai-ml/practitioner-workflows/agentic-systems/coding-and-computer-use-agents/code-agents) · [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning)

**Videos**:
- [AI Spotlight Seminar: Symbolic Reasoning for Large Language Models](https://www.youtube.com/watch?v=wApPzSqLVhY) — **Guy Van den Broeck (UCLA)** — why probabilistic circuits give guarantees that a penalty term cannot, from the author of semantic loss.
- [Neuro-Symbolic AI Summer School 2025 — Day 2](https://www.youtube.com/live/-uEx0IICBxg) — **Centaur AI Institute** — applied constrained systems, presented by their authors.
- [Probabilistic Circuits](https://www.youtube.com/watch?v=HjAjW6I3pLg) — **Antonio Vergari (University of Edinburgh, at the Nordic Probabilistic AI School)** — the tractable-inference machinery that makes exact constraint enforcement possible in a layer.

**Courses**:
- [Neuro-Symbolic AI Summer School 2025](https://www.youtube.com/playlist?list=PLqk1rh3Hd4UoHA-RkG41JuLOiM-p5dqkG) — **Centaur AI Institute and the Neuro-Symbolic AI Community** — the 2025 school, themed on precise computation; the constraint and probabilistic-circuit sessions are the core of this page.
- [Scallop tutorials](https://www.scallop-lang.org/) — **University of Pennsylvania** — a neurosymbolic language where the logical specification is the layer; the fastest way to write a constrained model yourself.

**Articles**:
- [Guidance](https://github.com/guidance-ai/guidance) — **Guidance contributors (originally Microsoft Research)** — constraints expressed as program structure rather than a schema; a different and instructive interface.
- [Scallop: a language for neurosymbolic programming](https://www.scallop-lang.org/) — **University of Pennsylvania** — provenance semirings make "which constraint mattered" answerable, not just "was it satisfied".
- [XGrammar](https://github.com/mlc-ai/xgrammar) — **MLC AI team (Carnegie Mellon University and NVIDIA)** — the engine's source and documentation; read the mask-cache design.

**Papers**:
- [A Pseudo-Semantic Loss for Autoregressive Models with Logical Constraints](https://arxiv.org/abs/2312.03905) — **Ahmed, Chang & Van den Broeck (2023)** — how to keep the semantic-loss idea tractable when the model generates a sequence.
- [A Semantic Loss Function for Deep Learning with Symbolic Knowledge](https://arxiv.org/abs/1711.11157) — **Xu et al. (2017)** — the derivation from weighted model counting; the canonical soft constraint.
- [Efficient Guided Generation for Large Language Models](https://arxiv.org/abs/2307.09702) — **Willard & Louf (2023)** — decoding as traversal of a finite-state machine indexed over the vocabulary; the Outlines paper.
- [Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation](https://arxiv.org/abs/2403.06988) — **Beurer-Kellner, Fischer & Vechev (2024)** — sub-word misalignment silently damages accuracy, and DOMINO's fix costs nothing.
- [JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models](https://arxiv.org/abs/2501.10868) — **Geng, Cooper, Moskal et al. (Microsoft Research and EPFL, 2025)** — coverage and efficiency measured across engines; the benchmark to quote when someone claims "schema-compliant".
- [Logic Tensor Networks](https://arxiv.org/abs/2012.13635) — **Badreddine, d'Avila Garcez, Serafini & Spranger (2020)** — first-order logic grounded in tensors, with fuzzy semantics and gradient-based satisfiability.
- [PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models](https://arxiv.org/abs/2109.05093) — **Scholak, Schucher & Bahdanau (2021)** — an incremental parser rejecting inadmissible tokens; the text-to-SQL result that made constrained decoding mainstream.
- [Semantic Probabilistic Layers for Neuro-Symbolic Learning](https://proceedings.neurips.cc/paper_files/paper/2022/file/c182ec594f38926b7fcb827635b9a8f4-Paper-Conference.pdf) — **Ahmed et al. (2022)** — constraint satisfaction by construction, trainable end to end by maximum likelihood.
- [XGrammar-2: Dynamic and Efficient Structured Generation Engine for Agentic LLMs](https://arxiv.org/abs/2601.04426) — **Dong et al. (2026)** — structure that switches mid-response, for agents that interleave text, tool calls, and protocols.
- [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](https://arxiv.org/abs/2411.15100) — **Dong et al. (2024)** — the context-free-grammar engine now embedded in mainstream serving stacks.

**Books**:
- [*Probabilistic Machine Learning: Advanced Topics* — Ch. on structured prediction and probabilistic circuits](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; the probabilistic scaffolding under semantic loss and tractable constraint layers.
- [*The Elements of Differentiable Programming*](https://diffprog.github.io/) — **Blondel & Roulet (Google DeepMind)** — free; relaxations, implicit layers, and how to differentiate through an argmax.
