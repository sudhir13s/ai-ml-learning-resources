---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-robotics/references"
topic: "Neuro-Symbolic Robotics — References"
parent: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-robotics"
type: references
updated: 2026-09-14
---

# Neuro-Symbolic Robotics — references

> Companion link library for **[Neuro-Symbolic Robotics](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-robotics/neuro-symbolic-robotics)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Learn the classical problem** — read [Integrated Task and Motion Planning](https://arxiv.org/abs/2010.01083) — **Garrett, Chitnis, Holladay, Kim, Silver, Kaelbling & Lozano-Pérez (2021)**. *The survey that defines the interface between a symbolic action and a continuous sampler.*
2. **Watch a manipulation system get built** — watch [Anatomy of a manipulation system](https://www.youtube.com/watch?v=QlrRb7X4JvA) — **Russ Tedrake (MIT 6.4210)**. *Perception, planning, and control as separate boxes, so you can see exactly which box a language model replaces.*
3. **See the language model as a scorer, not a planner** — read [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) — **Ahn, Brohan, Brown et al., Google (2022)**. *A learned value function says what is possible; the language model says what is useful; the product picks the skill.*
4. **See the language model write the program** — read [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) — **Liang, Huang, Xia et al., Google (2022)**. *Perception calls, control primitives, and loops emitted as Python — a symbolic policy you can read.*
5. **Check the 2025–26 state** — read [Gemini Robotics 1.5](https://arxiv.org/abs/2510.03342) — **Gemini Robotics Team, Google DeepMind (2025)**. *An embodied-reasoning model that plans in language before acting, and transfers motion across robot bodies.*

**In this platform**:
- Planning elsewhere: [Agent Planning](/ai-ml/practitioner-workflows/agentic-systems/planning/planning) · [Model-Based RL](/ai-ml/ai-ml-learning-resources/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl)
- Where the limits are stated: [Scalability Limitations](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations/scalability-limitations)
- The end-to-end alternative (canonical home): [Vision-Language-Action Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/embodied-intelligence/vision-language-action-models/vision-language-action-models) · [Embodied Agents and Perception-Action Loops](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/embodied-intelligence/embodied-agents-and-perception-action-loops/embodied-agents-and-perception-action-loops)

**Videos**:
- [Anatomy of a manipulation system](https://www.youtube.com/watch?v=QlrRb7X4JvA) — **Russ Tedrake (MIT 6.4210, Fall 2022)** — the systems view: what each module owns, and where a learned component can be swapped in.
- [Do As I Can, Not As I Say — supplementary video](https://www.youtube.com/watch?v=ysFav0b472w) — **Fei Xia (SayCan author)** — the real robot executing scored skills; the gap between plan and execution is visible.
- [Motion planning, optimization-based](https://www.youtube.com/watch?v=Sdn9zCMaoBY) — **Russ Tedrake (MIT 6.843)** — the continuous half of TAMP, taught properly rather than assumed.

**Courses**:
- [Robotic Manipulation](https://manipulation.csail.mit.edu/) — **Russ Tedrake (MIT 6.4210)** — free interactive textbook and course; the chapters on task planning and geometric reasoning are the prerequisite for every paper here.
- [Underactuated Robotics](https://underactuated.csail.mit.edu/) — **Russ Tedrake (MIT 6.832)** — free; the dynamics-and-control half, so "geometrically infeasible" stops being a hand-wave.

**Articles**:
- [Code as Policies — project page](https://code-as-policies.github.io/) — **Google Research** — generated policy code you can read next to the resulting robot behaviour.
- [Gemini Robotics 1.5 brings AI agents into the physical world](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/) — **Google DeepMind** — the plain-language version of the thinking-then-acting architecture.
- [Learning and Intelligent Systems group](https://lis.csail.mit.edu/) — **Kaelbling & Lozano-Pérez (MIT)** — the lab that defined modern TAMP; papers, code, and theses in one place.
- [SayCan — project page](https://say-can.github.io/) — **Google Robotics** — videos, prompts, and the skill list; the clearest picture of what "affordance" means operationally.

**Papers**:
- [AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers](https://arxiv.org/abs/2306.06531) — **Chen, Arkin, Dawson, Zhang, Roy & Fan (2024)** — translation to a temporal-logic specification, with the model also checking its own translation.
- [Code as Policies](https://arxiv.org/abs/2209.07753) — **Liang et al., Google (2022)** — policies as generated programs; composition, recursion, and parameterization for free.
- [Do As I Can, Not As I Say (SayCan)](https://arxiv.org/abs/2204.01691) — **Ahn et al., Google (2022)** — affordance-grounded skill selection; the paper that made "language model plus value function" standard.
- [Gemini Robotics 1.5](https://arxiv.org/abs/2510.03342) — **Gemini Robotics Team, Google DeepMind (2025)** — embodied thinking before acting, plus motion transfer across embodiments.
- [Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) — **Huang, Xia, Xiao et al., Google (2022)** — closing the loop with success detectors and scene descriptions, so replanning is grounded in what happened.
- [Integrated Task and Motion Planning](https://arxiv.org/abs/2010.01083) — **Garrett et al. (2021)** — the reference survey; read the interface taxonomy before anything else.
- [LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](https://arxiv.org/abs/2304.11477) — **Liu, Jiang, Zhang et al. (2023)** — translate to the planning domain definition language (PDDL), call a classical planner, translate back; optimality comes from the planner.
- [LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks](https://arxiv.org/abs/2402.01817) — **Kambhampati, Valmeekam, Guan et al. (2024)** — the sceptical position, and the architecture it implies: generate with the model, verify with the planner.
- [PDDLStream: Integrating Symbolic Planners and Blackbox Samplers](https://arxiv.org/abs/1802.08705) — **Garrett, Lozano-Pérez & Kaelbling (2020)** — streams as the bridge between a discrete planner and continuous samplers; the practical TAMP formulation.
- [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) — **Physical Intelligence (2025)** — high-level semantic subtask inference feeding a low-level action expert; the hierarchy reappears inside one model.

**Books**:
- [*Planning Algorithms* — Ch. 5 "Sampling-Based Motion Planning", Ch. 14 "Sampling-Based Planning Under Differential Constraints"](http://lavalle.pl/planning/) — **Steven M. LaValle (University of Illinois)** — free online; the classical foundation the symbolic layer sits on top of.
