---
id: "00-basics/ml-workflow-and-lifecycle"
topic: "The ML Workflow & Lifecycle"
parent: "00-basics"
level: beginner
built_from: ["what-is-ai-ml-dl", "types-of-machine-learning"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "The ML Workflow & Lifecycle"
minutes: 10
category: ai-ml-orientation
---

# The ML Workflow & Lifecycle
> Every ML project follows the same arc: **frame the problem → collect & explore data → prepare
> features → train a model → evaluate → deploy → monitor → iterate.** It's a *loop*, not a line —
> you cycle back constantly. The famous rule of thumb: 50–80% of the work is data, not modeling.

**Why it matters:** interviewers ask "walk me through how you'd approach an ML project end to end"
to see if you think like a practitioner, not just an algorithm-memorizer. Knowing the lifecycle
(and that data prep dominates, and that deployment/monitoring are where projects actually fail) is
what separates someone who's shipped ML from someone who's only done tutorials.

**Start here — suggested path:**

1. **See the whole loop** — watch [The 7 Steps of Machine Learning](https://www.youtube.com/watch?v=nKW8Ndu7Mjw). *Google's clean, beginner overview of the end-to-end arc.*
2. **Learn the industry-standard process** — read [What is CRISP-DM?](https://www.datascience-pm.com/crisp-dm-2/), then the [original CRISP-DM 1.0 guide](https://inseaddataanalytics.github.io/INSEADAnalytics/CRISP_DM.pdf). *The six-phase methodology that names every stage you will repeat on real projects.*
3. **Internalize why data dominates** — watch [Andrew Ng on data-centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo). *Why improving data beats tweaking models — the most important lifecycle lesson.*
4. **Read the hard-won rules** — skim [Google: Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml). *Battle-tested guidance for each lifecycle stage from Google engineers.*
5. **Watch one go end to end** — work through a lab from the [ISLP Python labs](https://www.youtube.com/playlist?list=PLoROMvodv4rNHU1-iPeDRH-J0cL-CrIda) — **Stanford Online**. *See data → train → evaluate happen in code, start to finish.*

## Courses (free)
- [Google ML Crash Course — Production ML Systems](https://developers.google.com/machine-learning/crash-course/production-ml-systems) — **Google** — free; the lifecycle from data to deployment and monitoring.
- [Kaggle Learn — Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) — **Kaggle** — free, hands-on; runs you through the build-train-evaluate loop in notebooks.
- [Made With ML — MLOps lessons](https://madewithml.com/) — **Goku Mohandas** — free, open course covering the full design → develop → deploy lifecycle.

## Videos
- [The 7 Steps of Machine Learning](https://www.youtube.com/watch?v=nKW8Ndu7Mjw) — **Google Cloud Tech** — the clearest beginner overview of the end-to-end arc.
- [A Chat with Andrew Ng on MLOps: Model-centric to Data-centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo) — **DeepLearningAI** — why the data stage dominates project success.
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) — **StatQuest with Josh Starmer** — the evaluation stage done honestly, which is what makes the rest of the loop trustworthy.
- [Statistical Learning — ISLP Python labs](https://www.youtube.com/playlist?list=PLoROMvodv4rNHU1-iPeDRH-J0cL-CrIda) — **Stanford Online** — the lifecycle demonstrated end to end in code, dataset by dataset.

## Key Papers
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — why the model is the small part; the lifecycle around it is where debt accumulates.
- [Rules of Machine Learning: Best Practices for ML Engineering](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Martin Zinkevich (Google)** — the canonical practitioner's guide to each lifecycle stage.
- [CRISP-DM 1.0: Step-by-step data mining guide](https://inseaddataanalytics.github.io/INSEADAnalytics/CRISP_DM.pdf) — **Chapman et al. (2000)** — the original document defining the standard lifecycle.

## Articles / Blogs (free, no paywall)
- [What is CRISP-DM?](https://www.datascience-pm.com/crisp-dm-2/) — **Data Science PM** — the six phases explained clearly, with how iteration works.
- [Machine Learning Systems Design (course notes)](https://huyenchip.com/machine-learning-systems-design/toc.html) — **Chip Huyen** — the lifecycle as a design problem: requirements, data, training, deployment, iteration, with the interview questions each stage attracts.
- [The end-to-end ML workflow](https://ml-ops.org/content/end-to-end-ml-workflow) — **ml-ops.org** — vendor-neutral reference for the production ML lifecycle.

## Books (free, with chapters)
- [Dive into Deep Learning — Ch. 1 "Introduction"](https://d2l.ai/chapter_introduction/index.html) — **Zhang et al.** — frames the data → model → evaluate loop with runnable code.
- [An Introduction to Statistical Learning — Ch. 2 "Statistical Learning"](https://www.statlearning.com/) — **James et al.** — free PDF; how to assess models within the workflow.
- [Approaching (Almost) Any Machine Learning Problem](https://github.com/abhishekkrthakur/approachingalmost) — **Abhishek Thakur** — free PDF; a practical, project-shaped walk through the workflow.

## In this platform
- Next concepts: [04 How Models Learn](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/how-models-learn/how-models-learn) · [12 Your First ML Project](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/your-first-ml-project/your-first-ml-project)
- Go deeper — data stages: [02. Data Preprocessing](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/readme)
- Go deeper — deployment & monitoring: [12. Deployment & MLOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
