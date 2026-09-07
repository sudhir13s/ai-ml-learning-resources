---
id: "core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging"
topic: "Error Analysis & Model Debugging"
level: intermediate
built_from: ["cross-validation", "calibration-and-reliability-diagrams", "uncertainty-estimation-and-conformal-prediction"]
leads_to: ["18-mlops/ml-lifecycle-and-mlops-maturity", "18-mlops/model-monitoring-and-observability"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Error Analysis & Model Debugging"
minutes: 15
category: model-selection-and-evaluation
---

# Error Analysis & Model Debugging
> A single aggregate score tells you *how much* the model is wrong and nothing about *why*.
> **Error analysis** is the discipline of reading the mistakes: pull a sample of failures,
> tag them into categories, count the categories, and let the counts — not intuition — decide
> what to work on next. **Model debugging** is the systematic search for the *cause* when
> training itself misbehaves.

**Why it matters:** it is the highest-return, least-glamorous skill in applied machine learning,
and the one senior interviews use to separate people who have shipped from people who have only
trained. The question is always some form of *"your model is at 91% and the business needs 95% —
what do you do Monday morning?"* The strong answer is a **prioritized error taxonomy** with
estimated ceilings per category, plus **slice-based evaluation** (aggregate accuracy hides a
minority slice at 40%), plus a debugging protocol that isolates data problems from optimization
problems from capacity problems. The trap is jumping to a bigger model when the label noise on
one slice caps the achievable score.

**Start here — suggested path:**

1. **Adopt the recipe** — read [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — **Andrej Karpathy**. *Become one with the data, overfit a single batch, then regularize — the debugging protocol that prevents most silent failures.*
2. **Learn the prioritization habit** — read [Machine Learning Yearning](https://info.deeplearning.ai/machine-learning-yearning-book) — **Andrew Ng (DeepLearning.AI)**. *Free book; the manual error-analysis loop — sample 100 misclassified examples, tag, count, and estimate the ceiling of each fix.*
3. **See why data beats model tweaks** — watch [A Chat with Andrew on MLOps: From Model-centric to Data-centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo) — **DeepLearningAI**. *The argument, with numbers, for improving labels and slices instead of architectures.*
4. **Test behavior, not just accuracy** — read [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://arxiv.org/abs/2005.04118) — **Ribeiro, Wu, Guestrin & Singh (2020)**. *Turn each error category into a minimum-functionality test so the fix cannot silently regress.*
5. **Make it a course** — take [Introduction to Data-Centric AI](https://dcai.csail.mit.edu/) — **MIT (Northcutt, Mueller, Chuang)**. *Free lectures and labs on label errors, dataset curation, outliers and slice discovery — the systematized version of the whole page.*

## Courses (free)

- [Introduction to Data-Centric AI](https://dcai.csail.mit.edu/) — **MIT CSAIL (Curtis Northcutt, Jonas Mueller, Anish Athalye)** — the only university course dedicated to fixing the dataset rather than the model; lectures, labs and solutions all free, [2024 lecture index here](https://dcai.csail.mit.edu/lectures/).
- [Made With ML — Evaluation](https://madewithml.com/courses/mlops/evaluation/) — **Goku Mohandas** — slice metrics, behavioral tests and error analysis wired into a real project, not a toy notebook.
- [Machine Learning Engineering for Production (MLOps) Specialization](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) — **Andrew Ng, Robert Crowe & Laurence Moroney (DeepLearning.AI)** — free to audit; Course 1 is the canonical treatment of error analysis, the data-centric loop and human-level performance as a baseline.

## Videos

- [A Chat with Andrew on MLOps: From Model-centric to Data-centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo) — **DeepLearningAI** — the talk that reframed the field: fix the data slice, not the architecture.
- [MIT Data-Centric AI, Lecture 1: Data-Centric AI vs. Model-Centric AI](https://www.youtube.com/watch?v=ayzOzZGHZy4) — **Introduction to Data-Centric AI (MIT course channel)** — sets up label noise, dataset curation and the measurement problems behind them.
- [Full Stack Deep Learning 2022 — Troubleshooting and testing](https://fullstackdeeplearning.com/course/2022/lecture-3-troubleshooting-and-testing/) — **Charles Frye, Sergey Karayev & Josh Tobin** — a practitioner's decision tree for "the loss is not going down" and for testing ML code.

## Key Papers

- [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://arxiv.org/abs/2005.04118) — **Ribeiro, Wu, Guestrin & Singh (2020, ACL best paper)** — minimum-functionality, invariance and directional-expectation tests; the template for turning error categories into regression tests.
- [Errudite: Scalable, Reproducible, and Testable Error Analysis](https://aclanthology.org/P19-1073/) — **Wu, Ribeiro, Heer & Weld (2019)** — makes error analysis precise and reproducible instead of a hand-picked anecdote.
- [No Subclass Left Behind: Fine-Grained Robustness in Coarse-Grained Classification Problems](https://arxiv.org/abs/2011.12945) — **Sohoni, Dunnmon, Angus, Gu & Ré (2020)** — hidden stratification: why a strong aggregate score can hide a catastrophic unlabeled subclass.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015, Google)** — the failure modes (entanglement, feedback loops, undeclared consumers) that make ML bugs different from software bugs.

## Articles / Blogs (free, no paywall)

- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — **Andrej Karpathy** — the single most useful debugging document in deep learning; the same text is also kept as a [public gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- [Rules of Machine Learning: Best Practices for ML Engineering](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Martin Zinkevich (Google)** — 43 rules; Rules 14–29 are effectively a checklist for diagnosing a model that underperforms.
- [Data Distribution Shifts and Monitoring](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html) — **Chip Huyen** — free chapter-length article; how the errors you analyse offline reappear as shift online.
- [MLU-Explain — visual essays on ML fundamentals](https://mlu-explain.github.io/) — **Amazon MLU (Jared Wilber and colleagues)** — interactive explanations of cross-validation, bias–variance, precision/recall and ROC that make slice-level reasoning concrete.

## Books (free, with chapters)

- [*Machine Learning Yearning*](https://info.deeplearning.ai/machine-learning-yearning-book) — **Andrew Ng** — free book; Ch. 13–19 are the definitive short treatment of error analysis, eyeball versus blackbox dev sets, and mismatched distributions.
- [*Designing Machine Learning Systems* — Ch. 6 "Model Development and Offline Evaluation"](https://huyenchip.com/mlops/) — **Chip Huyen** — slice-based evaluation, perturbation and invariance tests; author notes and the [companion repository](https://github.com/chiphuyen/dmls-book) are free.

## In this platform

- Prerequisites: [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) · [Bias–Variance Tradeoff](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/bias-variance-tradeoff/bias-variance-tradeoff) (which term your errors belong to) · [Classification Metrics](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/classification/classification-metrics/classification-metrics)
- Uses: [Calibration & Reliability Diagrams](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams) · [Uncertainty Estimation & Conformal Prediction](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/uncertainty-estimation-and-conformal-prediction/uncertainty-estimation-and-conformal-prediction) (the abstained cases are your richest error sample)
- Tuning is a separate owner: [Hyperparameter Search — a bridge](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/hyperparameter-search-a-bridge/hyperparameter-search-a-bridge)
- The same loop after deployment: [Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) · [AI Incident Response & Postmortems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems)
