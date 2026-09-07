---
id: "specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/open-problems"
topic: "Open Problems"
level: advanced
built_from: ["specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations", "specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/compositional-reasoning"]
leads_to: []
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Open Problems"
minutes: 16
category: evaluation-and-limitations
---

# Open Problems
> The field's own list of what is not solved: how to **learn symbols from data** rather than
> receiving them from a person, how to get **deliberate, System 2 style reasoning** out of a
> learned system, and which **benchmarks resist scale** long enough to be worth optimizing. The
> one sentence: **nobody disputes that neural and symbolic components both help — the open
> question is whether the symbolic part should be built, learned, or made to emerge.**

**Why it matters:** these are the questions a research-facing interview actually explores, and the
positions have names. **Kautz's taxonomy** gives the vocabulary for integration patterns;
**Marcus** argues for explicit structure as a design requirement; **Bengio** argues for learned
System 2 mechanisms — attention, sparse factors, causal structure — rather than bolted-on symbols.
The empirical referee is **ARC-AGI**: on ARC-AGI-2 the 2025 Kaggle competition's top score reached
**24%**, and the report's stated theme was the **per-task refinement loop** — search with a
feedback signal, which is the neuro-symbolic pattern under a different name.

**Start here — suggested path:**

1. **Get the field's own history** — read [The Third AI Summer: AAAI Robert S. Engelmore Memorial Lecture](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/19122) — **Henry Kautz (AI Magazine, 2022)**. *Where the neuro-symbolic taxonomy comes from, and why this summer might end like the others.*
2. **Read the structuralist case** — read [The Next Decade in AI: Four Steps Towards Robust Artificial Intelligence](https://arxiv.org/abs/2002.06177) — **Gary Marcus (2020)**. *Hybrid architectures, rich world models, and explicit knowledge, argued at length rather than as a slogan.*
3. **Read the learned-structure case** — read [Inductive Biases for Deep Learning of Higher-Level Cognition](https://arxiv.org/abs/2011.15091) — **Anirudh Goyal & Yoshua Bengio (2020)**. *System 2 competencies as priors — sparse causal factors, attention, and reusable modules — learned rather than programmed.*
4. **Watch the benchmark that keeps score** — watch [ARC-AGI-2 overview](https://www.youtube.com/watch?v=TWHezX43I-4) — **François Chollet (ARC Prize)**. *What the tasks are designed to defeat, and why memorization does not transfer to them.*
5. **Read the current results** — read [ARC Prize 2025: Technical Report](https://arxiv.org/abs/2601.10904) — **Chollet, Knoop et al., ARC Prize Foundation (2026)**. *The refinement loop, contamination risk, and the honest ceiling of frontier reasoning models.*

## Courses (free)
- [Neuro-Symbolic AI Summer School 2025 — Day 1](https://www.youtube.com/live/zVJ59vIden0) — **Centaur AI Institute and the Neuro-Symbolic AI Community** — free lectures from the people setting this agenda; the closest thing to a state-of-the-field syllabus.

## Videos
- [ARC-AGI-2 overview](https://www.youtube.com/watch?v=TWHezX43I-4) — **François Chollet (ARC Prize)** — task design as an argument about what intelligence is, from the benchmark's author.
- [ARC Prize Version 2 launch](https://www.youtube.com/watch?v=M3b59lZYBW8) — **François Chollet & Mike Knoop (Machine Learning Street Talk)** — the longer conversation, including where program search and language models each stall.

## Key Papers
- [Defining neurosymbolic AI](https://arxiv.org/abs/2507.11127) — **De Smet & De Raedt (2025)** — the current attempt to make the term precise enough to argue about.
- [Neurosymbolic AI: The 3rd Wave](https://arxiv.org/abs/2012.05876) — **d'Avila Garcez & Lamb (2020)** — the agenda paper; the open-problem list most later work inherits.
- [Neurosymbolic AI — Why, What, and How](https://arxiv.org/abs/2305.00813) — **Sheth, Roy & Gaur (2023)** — a taxonomy organized around what an application actually needs, useful for scoping a project.
- [The Next Decade in AI](https://arxiv.org/abs/2002.06177) — **Marcus (2020)** — the long-form structuralist argument.
- [Deep Learning: A Critical Appraisal](https://arxiv.org/abs/1801.00631) — **Marcus (2018)** — the earlier ten-point critique; read it to see which points the last eight years actually answered.
- [Inductive Biases for Deep Learning of Higher-Level Cognition](https://arxiv.org/abs/2011.15091) — **Goyal & Bengio (2022)** — the learned-System-2 programme, stated as testable priors.
- [The Consciousness Prior](https://arxiv.org/abs/1709.08568) — **Yoshua Bengio (2017)** — a sparse, low-dimensional conscious state as the bridge between distributed representations and symbol-like variables.
- [Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?](https://arxiv.org/abs/2502.15657) — **Bengio et al. (2025)** — the same structural commitments, restated as a safety architecture with explicit world models.
- [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) — **François Chollet (2019)** — skill-acquisition efficiency as the definition, and the reason ARC exists.
- [ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems](https://arxiv.org/abs/2505.11831) — **Chollet, Knoop, Kamradt et al. (2025)** — what the second version added, and which capabilities it isolates.
- [ARC Prize 2025: Technical Report](https://arxiv.org/abs/2601.10904) — **ARC Prize Foundation (2026)** — the competition results, the refinement-loop finding, and the preview of interactive ARC-AGI-3.
- [Symbol Grounding in Neuro-Symbolic AI: A Gentle Introduction to Reasoning Shortcuts](https://arxiv.org/abs/2510.14538) — **Emanuele Marconato et al. (2025)** — the open problem underneath all of the above: learning symbols whose meaning is the intended one.

## Articles / Blogs (free, no paywall)
- [ARC Prize 2025: results and analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis) — **ARC Prize Foundation** — the readable summary of what worked in 2025 and what the scores do and do not show.
- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) — **Richard Sutton** — the opposing thesis in one page; any position on this list has to answer it.
- [The 6 Types of Neuro-Symbolic Systems](https://harshakokel.com/posts/neurosymbolic-systems/) — **Harsha Kokel** — Kautz's taxonomy with a concrete example per category, which makes the debate easier to place.

## Books (free, with chapters)
- [*Neurosymbolic Programming*](https://www.cs.utexas.edu/~swarat/pubs/PGL-049-Plain.pdf) — **Chaudhuri, Ellis, Polozov, Singh, Solar-Lezama & Yue** — free monograph; the "open problems" chapter is a research agenda you can actually pick tasks from.

## In this platform
- Previous in this section: [Scalability Limitations](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations/scalability-limitations) · [Interpretability and Verifiability](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/interpretability-and-verifiability/interpretability-and-verifiability)
- The orientation page (canonical home): [Neuro-Symbolic AI Overview](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview/neuro-symbolic-ai-overview) · [Symbolic AI and Good Old-Fashioned AI](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/symbolic-ai-and-good-old-fashioned-ai/symbolic-ai-and-good-old-fashioned-ai)
- The measured cases: [Compositional Reasoning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/compositional-reasoning/compositional-reasoning) · [Program Synthesis and Code Reasoning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/program-synthesis-and-code-reasoning)
- Sub-area index: [Neuro-Symbolic and Structured Intelligence](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/readme)
