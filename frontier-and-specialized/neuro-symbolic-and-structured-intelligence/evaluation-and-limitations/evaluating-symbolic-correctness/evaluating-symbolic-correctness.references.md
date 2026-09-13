---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/evaluating-symbolic-correctness/references"
topic: "Evaluating Symbolic Correctness — References"
parent: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/evaluating-symbolic-correctness"
type: references
updated: 2026-09-14
---

# Evaluating Symbolic Correctness — references

> Companion link library for **[Evaluating Symbolic Correctness](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/evaluating-symbolic-correctness/evaluating-symbolic-correctness)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See a checkable benchmark** — read [MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics](https://arxiv.org/abs/2109.00110) — **Zheng, Han & Polu (2022)**. *One problem set, several proof assistants; every score is a compiled proof, not a judgement.*
2. **See logic in natural language, with proofs** — read [FOLIO: Natural Language Reasoning with First-Order Logic](https://arxiv.org/abs/2209.00840) — **Han, Schoelkopf, Zhao et al. (2022)**. *Expert-written stories paired with first-order logic annotations, so the symbolic translation itself is gradeable.*
3. **See the proof chain scored, not the answer** — read [ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language](https://arxiv.org/abs/2012.13048) — **Tafjord, Dalvi & Clark, Allen Institute for AI (2021)**. *Grade the derivation, which makes "right answer, wrong reason" a detectable failure.*
4. **See execution as the oracle** — read [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) — **Chen, Tworek, Jun et al., OpenAI (2021)**. *Functional correctness by running unit tests; the pass@k framing that most agent evaluation inherited.*
5. **Meet the current ceiling** — read [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://arxiv.org/abs/2407.11214) — **Tsoukalas, Lee, Jennings et al. (2024)**. *1,697 formalizations in Lean 4, Isabelle, and Coq, where top systems still solve a handful.*

**In this platform**:
- The evaluation owner elsewhere: [LLM Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) · [Agent Evaluation](/ai-ml/practitioner-workflows/agentic-systems/agent-evaluation/agent-evaluation)
- Prerequisites: [Neuro-Symbolic Language Models](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-language-models/neuro-symbolic-language-models) · [Neural Theorem Proving](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving/neural-theorem-proving)
- Related: [Program Synthesis and Code Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/program-synthesis-and-code-reasoning) · [Constraint-Guided Learning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/constraint-guided-learning/constraint-guided-learning) · [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/evaluation/hallucination-and-grounding/hallucination-and-grounding)

**Videos**:
- [Machine Assisted Proof](https://www.youtube.com/watch?v=AayZuuDDKP0) — **Terence Tao (Joint Mathematics Meetings, 2024)** — what formal verification actually certifies, and what it leaves out, from a working mathematician.
- [Terence Tao at IMO 2024: AI and Mathematics](https://www.youtube.com/watch?v=e049IoFBnLA) — **Terence Tao (AIMO Prize)** — the calibration talk: how to read a headline benchmark result about mathematical reasoning.

**Courses**:
- [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/) — **Lean community (Avigad, Massot et al.)** — free and hands-on; you cannot reason about proof-checked evaluation without having written one proof.

**Articles**:
- [HELM](https://crfm.stanford.edu/helm/) — **Stanford Center for Research on Foundation Models** — the counterweight: broad, multi-metric evaluation, so a single checkable score is not read as general competence.
- [LeanDojo](https://leandojo.org/) — **LeanDojo team (Caltech, NVIDIA et al.)** — the open toolchain for running and scoring proof search against Lean.
- [PutnamBench](https://github.com/trishullab/PutnamBench) — **Trishul Lab (University of Texas at Austin)** — the formalizations themselves, plus the evaluation harness.
- [ROAD-R](https://github.com/EGiunchiglia/ROAD-R) — **Eleonora Giunchiglia** — data, requirements, and the code that counts violations.
- [SWE-bench](https://www.swebench.com/) — **Princeton NLP** — the live leaderboard and the verified subset; read the task format before quoting a number.

**Papers**:
- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) — **Chen et al., OpenAI (2021)** — HumanEval and pass@k; the origin of execution-based scoring.
- [FOLIO](https://arxiv.org/abs/2209.00840) — **Han et al. (2022)** — natural-language reasoning with first-order logic annotations; grades translation as well as conclusion.
- [FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://arxiv.org/abs/2411.04872) — **Glazer, Erdil, Besiroglu et al., Epoch AI (2024)** — unpublished problems with automatically verifiable answers, built to resist contamination.
- [Functional Benchmarks for Robust Evaluation of Reasoning Performance, and the Reasoning Gap](https://arxiv.org/abs/2402.19450) — **Saurabh Srivastava et al. (2024)** — rewrite a benchmark as a function that generates fresh instances, and watch the score fall.
- [Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought](https://arxiv.org/abs/2210.01240) — **Saparov & He (2023)** — ProntoQA: synthetic ontologies where every proof step can be checked against the rules.
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) — **Lightman, Kosaraju, Burda et al., OpenAI (2023)** — process versus outcome supervision; scoring the steps changes what gets optimized.
- [MiniF2F](https://arxiv.org/abs/2109.00110) — **Zheng, Han & Polu (2022)** — the standard formal-mathematics benchmark and the reason cross-system numbers are comparable.
- [ProofWriter](https://arxiv.org/abs/2012.13048) — **Tafjord, Dalvi & Clark (2021)** — implications, proofs, and abduction over rule sets stated in language.
- [PutnamBench](https://arxiv.org/abs/2407.11214) — **Tsoukalas et al. (2024)** — harder, multilingual across proof assistants, with factored answer-plus-proof problems.
- [ROAD-R: The Autonomous Driving Dataset with Logical Requirements](https://arxiv.org/abs/2210.01597) — **Giunchiglia, Stoian, Khan, Cuzzolin & Lukasiewicz (2022)** — constraint-violation rate as a first-class metric, on a real perception task.
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — **Jimenez, Yang, Wettig et al. (2023)** — the project's own tests as the oracle, at repository scale.

**Books**:
- [*Logic and Proof*](https://avigad.github.io/logic_and_proof/) — **Avigad, Lewis & van Doorn (Carnegie Mellon University)** — free, with machine-checked exercises; soundness and completeness are what a "correct" verdict actually rests on.
