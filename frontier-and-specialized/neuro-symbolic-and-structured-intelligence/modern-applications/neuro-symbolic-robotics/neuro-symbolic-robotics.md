---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-robotics"
topic: "Neuro-Symbolic Robotics"
core_idea: "A robot's plan must be solved jointly as a discrete task sequence and a continuous motion, because a symbolically perfect plan is worthless when geometry makes it infeasible."
level: advanced
built_from: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/knowledge-grounded-agents", "vision-language-action-models"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Neuro-Symbolic Robotics"
minutes: 18
category: modern-applications
---

# Neuro-Symbolic Robotics
> A robot has to answer two questions at once: **what to do** (pick up the mug, then open the
> drawer) and **how to move** (a collision-free trajectory that actually reaches the mug). The
> first is discrete and symbolic, the second continuous and geometric, and they constrain each
> other. **Task and motion planning (TAMP)** solves them jointly; the neural part supplies the
> perception, the affordances, and increasingly the plan sketch. The one sentence: **symbols pick
> the sequence, geometry decides whether that sequence is even possible.**

**Why it matters:** it is the clearest domain where "just scale the model" has a measurable
ceiling — a plan that is linguistically perfect and geometrically infeasible is worthless, and
only a planner or simulator can tell you which one you have. The 2025–26 frontier makes the
tension explicit: **vision-language-action (VLA) models** learn control end to end, while
embodied-reasoning models such as **Gemini Robotics-ER 1.5** put an explicit thinking-and-planning
stage in front of the controller. The failure mode to name: **symbol grounding** — the planner's
`on(cup, table)` predicate is only as good as the perception module that decides it is true.

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Neuro-Symbolic Robotics — references](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-robotics/neuro-symbolic-robotics#references-further-reading)**
