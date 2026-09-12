---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/compositional-reasoning"
topic: "Compositional Reasoning"
level: advanced
built_from: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/graph-based-reasoning", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/constraint-guided-learning", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/open-problems"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Compositional Reasoning"
minutes: 16
category: structured-reasoning
---

# Compositional Reasoning
> Know what "jump" means and what "twice" means, and you know what "jump twice" means — even if
> you have never heard the phrase. That is **systematic generalization**: recombining known parts
> into unseen wholes. The one sentence: **compositional reasoning is the ability to generalize
> along the grammar of a problem rather than along the distribution of the training data.**

**Why it matters:** this is the sharpest measurable gap between what models learn and what people
do, and it is the empirical core of the neuro-symbolic argument — symbols compose by construction,
learned features do not. The 2023 **meta-learning for compositionality (MLC)** result showed a
standard network can match humans *when trained on a stream of compositional tasks*, which
relocates the debate from architecture to training distribution. The failure mode to name in an
interview: **benchmark-specific fixes**, where a model solves SCAN's splits and still collapses on
a differently-shaped recombination.

**Start here — suggested path:**

1. **See the failure concretely** — read [Generalization without Systematicity (SCAN)](https://arxiv.org/abs/1711.00350) — **Brenden Lake & Marco Baroni (2018)**. *The "jump twice" experiment that turned a philosophical objection into a reproducible test.*
2. **Learn the vocabulary** — read [Compositionality decomposed: how do neural networks generalise?](https://arxiv.org/abs/1908.08351) — **Hupkes, Dankers, Mul & Bruni (2020)**. *Five distinct tests — systematicity, productivity, substitutivity, localism, overgeneralization — instead of one vague word.*
3. **Watch the cognitive-science framing** — watch [Compositional generalization in minds and machines](https://www.youtube.com/watch?v=jGBzCzJ0Uok) — **Brenden Lake (London Machine Learning Meetup)**. *What human participants actually do on these tasks, which is the target the benchmarks encode.*
4. **Read the result that moved the field** — read [Human-like systematic generalization through a meta-learning neural network](https://www.nature.com/articles/s41586-023-06668-3) — **Brenden Lake & Marco Baroni (Nature, 2023)**. *Meta-learning over a dynamic stream of compositional tasks, compared head-to-head against people.*
5. **Check the language-model evidence** — read [Faith and Fate: Limits of Transformers on Compositionality](https://arxiv.org/abs/2305.18654) — **Dziri et al. (2023)**. *Multi-step composition as a computation graph, and why accuracy decays with graph depth rather than with task familiarity.*

## Courses (free)
- [Computational Cognitive Modeling](https://brendenlake.github.io/CCM-site/) — **Brenden Lake (New York University)** — free syllabus, slides, and notebooks; the course behind most of the human-comparison work on this page.
- [Connectionism](https://plato.stanford.edu/entries/connectionism/) — **Stanford Encyclopedia of Philosophy** — free, careful treatment of the systematicity challenge and the replies to it; read it as the background lecture the papers assume.

## Videos
- [Compositional generalization in minds and machines](https://www.youtube.com/watch?v=jGBzCzJ0Uok) — **Brenden Lake (London Machine Learning Meetup)** — the whole research programme, from SCAN to meta-learning, from the person who built the benchmarks.
- [ARC-AGI-2 overview](https://www.youtube.com/watch?v=TWHezX43I-4) — **François Chollet (ARC Prize)** — the same demand for novel recombination, posed as abstract visual puzzles rather than as language.

## Key Papers
- [Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks](https://arxiv.org/abs/1711.00350) — **Lake & Baroni (2018)** — SCAN; the origin point of the modern literature.
- [COGS: A Compositional Generalization Challenge Based on Semantic Interpretation](https://arxiv.org/abs/2010.05465) — **Najoung Kim & Tal Linzen (2020)** — natural-language semantics with systematic train/test gaps, so the test is linguistic rather than toy.
- [A Benchmark for Systematic Generalization in Grounded Language Understanding (gSCAN)](https://arxiv.org/abs/2003.05161) — **Ruis, Andreas, Baroni et al. (2020)** — SCAN moved into a grounded world, where composition must survive perception.
- [Measuring Compositional Generalization: A Comprehensive Method on Realistic Data](https://arxiv.org/abs/1912.09713) — **Keysers et al., Google (2020)** — CFQ and the distribution-based compound divergence metric; how to build a hard split on purpose.
- [Compositionality decomposed: how do neural networks generalise?](https://arxiv.org/abs/1908.08351) — **Hupkes et al. (2020)** — the taxonomy that stops "compositional" from meaning five different things in one paragraph.
- [Human-like systematic generalization through a meta-learning neural network](https://www.nature.com/articles/s41586-023-06668-3) — **Lake & Baroni (2023)** — MLC: optimize for compositional skill and a standard sequence model matches human behaviour.
- [Faith and Fate: Limits of Transformers on Compositionality](https://arxiv.org/abs/2305.18654) — **Dziri et al. (2023)** — composition decays with reasoning depth; performance tracks subgraph frequency in training.
- [Linguistic generalization and compositionality in modern artificial neural networks](https://arxiv.org/abs/1904.00157) — **Marco Baroni (2019)** — the linguist's statement of what the machines must show before the claim is granted.
- [Compositional-ARC: Assessing Systematic Generalization in Abstract Spatial Reasoning](https://arxiv.org/abs/2504.01445) — **Mondorf et al. (2025)** — composition of known transformations, isolated from language and from world knowledge.
- [Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability](https://arxiv.org/abs/2506.15629) — **Sakai et al. (2025)** — thirty-six models measured with concept order controlled, separating composition from instruction following.
- [Fodor and Pylyshyn's Legacy: Still No Human-like Systematic Compositionality in Neural Networks](https://arxiv.org/abs/2506.01820) — **Woydt, Willig, Wüst, Helff, Stammer, Rothkopf & Kersting (2025)** — the sceptical reading of the recent results, including what MLC does and does not settle.

## Articles / Blogs (free, no paywall)
- [Connectionism and Cognitive Architecture: A Critical Analysis](https://ruccs.rutgers.edu/images/personal-zenon-pylyshyn/proseminars/Proseminar13/ConnectionistArchitecture.pdf) — **Jerry Fodor & Zenon Pylyshyn (1988; author's copy, Rutgers)** — the original systematicity argument every paper above is answering.
- [From Frege to chatGPT: Compositionality in language, cognition, and deep neural networks](https://arxiv.org/abs/2405.15164) — **Russin, McGrath, Williams & Elber-Dorozko (2024)** — a readable history of the idea, written for machine-learning readers.
- [Human and Machine Intelligence Lab — publications](https://lake-lab.github.io/publications/) — **Brenden Lake's lab (New York University)** — the running bibliography, so you can see what came after the Nature paper.

## Books (free, with chapters)
- [*Meta-Learning for Compositionality* — code and materials](https://github.com/brendenlake/MLC) — **Lake & Baroni** — not a book but the reproducible artefact: models, human data, and the task stream, released with the Nature paper.
- [*SCAN* — dataset and splits](https://github.com/brendenlake/SCAN) — **Lake & Baroni** — the benchmark itself; five minutes with the splits teaches more than a summary of them.

## In this platform
- Previous in this section: [Causal and Relational Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/causal-and-relational-reasoning/causal-and-relational-reasoning) · [Graph-Based Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/graph-based-reasoning/graph-based-reasoning)
- Next in this section: [Constraint-Guided Learning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/constraint-guided-learning/constraint-guided-learning)
- Where the debate continues: [Open Problems](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/open-problems/open-problems) · [Program Synthesis and Code Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/program-synthesis-and-code-reasoning)
- Related elsewhere: [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) · [LLM Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks)
