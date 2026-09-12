---
id: "21-frontier/how-to-read-papers"
topic: "How to Read ML Papers"
parent: "21-frontier"
level: intermediate
built_from: ["basic-deep-learning", "linear-algebra"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "How to Read ML Papers"
minutes: 10
category: research-literacy
---

# How to Read ML Papers
> A repeatable, multi-pass system for extracting the idea, the evidence, and the limitations from an
> ML paper — without reading every word. The single highest-leverage skill for staying current:
> the field moves in papers, and the people who keep up are the ones who can triage 20 and deep-read 2.

**Why it matters:** in interviews and on the job you'll be handed a paper ("walk me through how
this works / would you trust this result?") and expected to find the contribution, the baseline,
the ablations, and the threats to validity fast. Reading skill is what separates "I saw the
headline" from "I understand the method and its limits."

**Start here — suggested path:**

1. **Adopt the three-pass method** — read ["How to Read a Paper" (Keshav)](http://ccr.sigcomm.org/online/files/p83-keshavA.pdf), one page, then watch [How To Read AI Research Papers Effectively](https://www.youtube.com/watch?v=K6Wui3mn-uI). *Pass 1 = title/abstract/figures/conclusion; pass 2 = method + results skim; pass 3 = reconstruct it yourself. This is the backbone of everything below.*
2. **Practice triage** — read titles → abstracts → figures of 10 papers in your area before deep-reading any. *Andrew Ng's rule: 5–20 papers gives basic grasp of a field, 50–100 gives mastery. Breadth first, depth on demand.*
3. **Read for the contribution and the evidence** — for each paper answer: what's new? what's the baseline? what do the ablations remove? *A method "works" only relative to a baseline; the ablation table tells you which part actually matters.*
4. **Hunt the limitations** — read the limitations/related-work sections and ask what the authors did *not* test. *This is the "evaluate hype vs substance" muscle — and exactly what interviewers probe.*
5. **Reconstruct, then move on** — write 3 sentences (problem / method / result) in your own words; only re-open the paper if you'd build on it. *Active recall beats re-reading; the note becomes your searchable memory.*

## Courses (free)
- [Stanford CS230 — lecture materials (incl. Reading Research Papers)](https://cs230.stanford.edu/lecture/) — **Andrew Ng, Kian Katanforoosh / Stanford** — the canonical lecture on a paper-reading workflow and how many papers to read.
- [Harvard CS197: AI Research Experiences](https://www.cs197.seas.harvard.edu/course-content) — **Pranav Rajpurkar / Harvard** — a full free course (lecture notes online) on reading, critiquing, and producing AI research.

## Videos
- [How To Read AI Research Papers Effectively](https://www.youtube.com/watch?v=K6Wui3mn-uI) — **DeepLearningAI** — a practical, ML-specific reading workflow from Andrew Ng's team.
- [Attention Is All You Need — paper walkthrough](https://www.youtube.com/watch?v=iDulhoQ2pro) — **Yannic Kilcher** — watch a researcher read a landmark paper end to end; the best available model of pass 2 and pass 3.
- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **Andrej Karpathy** — pass 3 taken to its conclusion: a paper rebuilt in code, decision by decision.

## Key Papers
- [How to Read a Paper](http://ccr.sigcomm.org/online/files/p83-keshavA.pdf) — **S. Keshav (2007)** — the original "three-pass" method; the canonical reference for this skill.
- [How to Write a Great Research Paper](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) — **Simon Peyton Jones (Microsoft Research)** — reading the structure authors are taught to write makes papers easier to read.
- [Troubling Trends in Machine Learning Scholarship](https://arxiv.org/abs/1807.03341) — **Lipton & Steinhardt (2018)** — what to be skeptical of when reading ML papers (a critical-reading checklist).

## Articles / Blogs (free, no paywall)
- [How to Read a Paper (Keshav) — HTML mirror](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) — **Stanford** — the three-pass method as a printable handout.
- [Semantic Scholar](https://www.semanticscholar.org/) — **Allen Institute for AI** — citation graph, TLDR summaries, and "cited by" trails: the triage tooling the multi-pass method runs on.
- [alphaXiv](https://www.alphaxiv.org/) — **alphaXiv (Stanford)** — arXiv papers with a public comment layer; read the discussion when a claim looks too clean (2025-era replacement for the retired Papers with Code).
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — **Jay Alammar** — a model of how a hard paper (Attention Is All You Need) becomes readable; use it as a "what good understanding looks like" target.

## Books (free, with chapters)
- [Speech and Language Processing, 3rd ed.](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky & Martin** — each chapter's "Bibliographical and Historical Notes" models how to place a paper in its lineage.
- [Dive into Deep Learning](https://d2l.ai/) — **Zhang et al.** — pairs prose with runnable code; the gold standard for "reconstruct the method to understand it."

## In this platform
- Per-concept index: [Frontier & Staying Current — concepts](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme)
- Where to find papers to read: [02 arXiv and Paper Discovery](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/arxiv-and-paper-discovery/arxiv-and-paper-discovery) · [04 Newsletters & Blogs to Follow](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/newsletters-and-blogs-to-follow/newsletters-and-blogs-to-follow)
- Apply it to a frontier area: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme) · [10. GenAI](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme)
