---
id: "foundations/ai-paradigms-and-knowledge/symbolic-ai-and-good-old-fashioned-ai"
topic: "Symbolic AI and Good Old-Fashioned AI"
level: beginner
built_from: ["what-is-ai-ml-deep-learning"]
leads_to: ["foundations/ai-paradigms-and-knowledge/statistical-learning-paradigm", "foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Symbolic AI and Good Old-Fashioned AI"
minutes: 14
category: ai-paradigms-and-knowledge
---

# Symbolic AI and Good Old-Fashioned AI
> The first paradigm of artificial intelligence: represent what you know as **symbols and rules**,
> then get intelligent behaviour by **searching and inferring** over them. Good Old-Fashioned AI
> (GOFAI) is the name later given to this tradition — logic, search, planning, and expert systems —
> and it is where almost every piece of AI vocabulary you use came from.

**Why it matters:** the 2026 stack is quietly full of GOFAI. A language model that calls a SAT
solver, a planner, a type checker, or Lean is running symbolic inference under a neural controller.
Knowing what symbolic systems are *good* at (exactness, verifiability, explanation, zero training
data) and what killed them (the knowledge-acquisition bottleneck, brittleness, combinatorial
search) is exactly the judgment interviewers probe when they ask "why not just use rules?"

**Start here — suggested path:**

1. **Meet the tradition on its own terms** — watch [Lecture 1: Introduction and Scope](https://www.youtube.com/watch?v=TjZBTDzGeGg) — **MIT OpenCourseWare (Patrick Winston)**. *Winston opens 6.034 with the symbolic definition of AI: algorithms enabled by representations.*
2. **See a symbolic system actually run** — watch [Reasoning: Goal Trees and Rule-Based Expert Systems](https://www.youtube.com/watch?v=leXa7EKUPFk) — **MIT OpenCourseWare (Patrick Winston)**. *A rule engine solving a problem, and explaining itself — the property neural nets still lack.*
3. **Read the paradigm's manifesto** — [Computer Science as Empirical Inquiry: Symbols and Search](https://dl.acm.org/doi/10.1145/360018.360022) — **Newell & Simon (1976 Turing Award lecture)**. *The physical symbol system hypothesis, stated by the people who built the first AI programs.*
4. **Get the modern textbook framing** — skim [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) — **Russell & Norvig**. *Search, logic, and planning as they are taught today, with free sample chapters and code.*
5. **Learn why it stalled** — read [The Lighthill Report and the 1973 debate](https://www.aiai.ed.ac.uk/events/lighthill1973/) — **University of Edinburgh (AIAI archive)**. *The critique that triggered the first AI winter: combinatorial explosion and no path to scale.*

## Courses (free)
- [MIT 6.034 Artificial Intelligence (Fall 2010)](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) — **MIT OpenCourseWare (Patrick Winston)** — the definitive symbolic-AI course: search, constraints, rules, representation, taught by the person who wrote the field's first textbook.
- [Stanford CS221: Artificial Intelligence — Principles and Techniques](https://stanford-cs221.github.io/autumn2024/) — **Stanford (Percy Liang, Dorsa Sadigh)** — modern treatment that puts search, constraint satisfaction, and logic beside learning instead of against it.

## Videos
- [MIT 6.034 Artificial Intelligence, Fall 2010 (full lecture series)](https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi) — **MIT OpenCourseWare** — thirty lectures; the clearest recorded account of how symbolic AI actually works.
- [Stanford CS221: Artificial Intelligence (Autumn 2021)](https://www.youtube.com/playlist?list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2) — **Stanford Online** — the logic and search modules give the contemporary version of the same material.
- [The Lighthill debate on Artificial Intelligence (1973)](https://www.youtube.com/watch?v=03p2CADwGF8) — **BBC 1973 (archival upload, Pierre-Yves Oudeyer)** — McCarthy and Michie versus Lighthill; the argument that ended the first funding boom, in the participants' own words.

## Key Papers
- [Computer Science as Empirical Inquiry: Symbols and Search](https://dl.acm.org/doi/10.1145/360018.360022) — **Newell & Simon (1976)** — the physical symbol system hypothesis: symbols plus search are necessary and sufficient for general intelligence.
- [Programs with Common Sense](http://www-formal.stanford.edu/jmc/mcc59.pdf) — **John McCarthy (1959)** — the founding proposal for representing knowledge declaratively and deriving conclusions with logic.
- [Steps Toward Artificial Intelligence](https://courses.csail.mit.edu/6.803/pdf/steps.pdf) — **Marvin Minsky (1961)** — search, pattern recognition, learning, and planning laid out before any of them had a field.
- [The Art of Artificial Intelligence: Themes and Case Studies of Knowledge Engineering](https://www.ijcai.org/Proceedings/77-2/Papers/094.pdf) — **Edward Feigenbaum (IJCAI 1977)** — the expert-systems thesis: "knowledge is power", and the knowledge-acquisition bottleneck that followed from it.

## Articles / Blogs (free, no paywall)
- [The Third AI Summer: AAAI Robert S. Engelmore Memorial Lecture](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/19122) — **Henry Kautz (AI Magazine, 2022)** — the best short history of why symbolic and neural AI alternated, and why they are converging now.
- [Logic and Artificial Intelligence](https://plato.stanford.edu/entries/logic-ai/) — **Stanford Encyclopedia of Philosophy (Richmond Thomason)** — rigorous, free account of what logic was supposed to do for AI and where it ran into trouble.
- [The Lighthill Report: Artificial Intelligence — A General Survey](http://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/contents.htm) — **James Lighthill (1973, Chilton Computing archive)** — the full text of the report that cut UK AI funding; read the "combinatorial explosion" section.

## Books (free, with chapters)
- [*Artificial Intelligence: A Modern Approach* — Part II "Problem-solving" and Part III "Knowledge, Reasoning and Planning"](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — the canonical treatment; sample chapters, pseudocode, and the `aima-python` repository are free on the book site.
- [*Learn Prolog Now!*](https://lpn.swi-prolog.org/) — **Blackburn, Bos & Striegnitz** — free online book; the fastest way to feel what "programming in logic" is, running live in SWI-Prolog.

## In this platform
- Where this fits: [What is AI / ML / Deep Learning](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/what-is-ai-ml-deep-learning/what-is-ai-ml-deep-learning)
- Next paradigms: [The Statistical Learning Paradigm](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/statistical-learning-paradigm/statistical-learning-paradigm) · [Neuro-Symbolic AI Overview](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview/neuro-symbolic-ai-overview)
- Depth on the symbolic machinery: [Knowledge Representation](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation/knowledge-representation) · [Logic and Inference](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference/logic-and-inference)
- The vocabulary it gave modern systems: [LLM Agents and the Agent Loop](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-foundations/agent-foundations)
