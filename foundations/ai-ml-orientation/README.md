---
id: "foundations/ai-ml-orientation"
topic: "AI/ML Orientation"
level: beginner
built_from: []
updated: 2026-09-07
---

# AI/ML Orientation

> The first five pages of the whole library. They answer the questions a newcomer actually has
> — what artificial intelligence (AI), machine learning (ML) and deep learning (DL) are and how
> they nest, which of the three learning paradigms fits a problem, what a real project looks like
> end to end, how a model learns at all, and why a model that scores well can still be useless.
> Everything later in the estate assumes this vocabulary.

**Start here:** [What is AI / ML / Deep Learning](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/what-is-ai-ml-deep-learning/what-is-ai-ml-deep-learning) for the nesting, then work straight down the index — these five are written to be read in order, each one using the previous one's words.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### The map of the field

1. [What is AI / ML / Deep Learning](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/what-is-ai-ml-deep-learning/what-is-ai-ml-deep-learning) — the nesting AI ⊃ ML ⊃ DL, and what each layer actually contributes.
2. [Types of Machine Learning](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/types-of-machine-learning/types-of-machine-learning) — supervised, unsupervised and reinforcement, split by what feedback the model receives.

### How a project runs

3. [The ML Workflow and Lifecycle](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/the-ml-workflow-and-lifecycle/the-ml-workflow-and-lifecycle) — frame → data → features → train → evaluate → deploy → monitor, as a loop rather than a line.

### How learning actually works

4. [How Models Learn](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/how-models-learn/how-models-learn) — loss, gradient descent and the training loop: predict, score the wrongness, step downhill.
5. [Overfitting and Underfitting](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/overfitting-and-underfitting/overfitting-and-underfitting) — bias, variance, the U-curve, and why held-out data is the only honest judge.

## References

**In this platform**:
- Curating a real training corpus: [Curating a Web Corpus](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation-curating-a-web-corpus) · [The Training Loop](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-the-training-loop)
- Evaluation done properly: [Model Selection and Evaluation](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/readme)
- Next in this section: [Programming and Data Foundations](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/readme) · [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) · [Data Preparation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme) · [Tools and Frameworks](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/readme) · [Research Literacy](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme) · [AI Paradigms and Knowledge](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/readme)
- Section index: [Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme)
- The mental models behind these pages: [Gradient Descent and SGD](/ai-ml/ai-ml-intuitions/learning-and-optimization/first-order-optimization/gradient-descent-and-stochastic-gradient-descent-intuition) · [Bias-Variance Tradeoff](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/generalization/bias-variance-tradeoff-intuition) · [Mean Squared Error](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/training-objectives/mean-squared-error-intuition)
- Where the three paradigms are taught in depth: [Supervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/readme) · [Unsupervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/readme) · [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/reinforcement-learning/readme)

**Videos**:
- [A Chat with Andrew Ng on MLOps: From Model-centric to Data-centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo) — **DeepLearningAI** — why the data stage, not the model stage, decides whether a project works.
- [A Gentle Introduction to Machine Learning](https://www.youtube.com/watch?v=Gv9_4yMHFhI) — **StatQuest with Josh Starmer** — first contact with training data, testing data and the bias-variance idea, at a friendly pace.
- [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) — **3Blue1Brown** — the best visual answer to what the "deep learning" layer of the nesting actually is.
- [What is Machine Learning?](https://www.youtube.com/watch?v=ukzFI9rgwfU) — **DeepLearning.AI (Andrew Ng)** — the definition from the field's best-known teacher, in under ten minutes.

**Courses**:
- [Elements of AI — Ch. 1 "What is AI?"](https://course.elementsofai.com/1) — **University of Helsinki and MinnaLearn** — the clearest non-technical answer to "what is AI", built for people with no background at all.
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — **Google** — free and applied; defines ML and frames every stage of a project with interactive exercises.
- [Kaggle Learn — Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) — **Kaggle** — hands-on in notebooks; the build-train-evaluate loop in an afternoon.
- [Machine Learning Specialization (free to audit)](https://www.coursera.org/specializations/machine-learning-introduction) — **Andrew Ng, DeepLearning.AI** — the field's standard first course; courses 1 to 3 walk supervised, unsupervised and recommenders.

**Articles**:
- [A (Long) Peek into Reinforcement Learning](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) — **Lilian Weng** — the clearest free overview of the third paradigm, for readers who want more than the one-page treatment.
- [Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing) — **Google** — how to decide classification versus regression versus clustering for a real task, before writing code.
- [The end-to-end ML workflow](https://ml-ops.org/content/end-to-end-ml-workflow) — **ml-ops.org (INNOQ)** — a vendor-neutral reference for the lifecycle the third page teaches.
- [What is Machine Learning?](https://developers.google.com/machine-learning/intro-to-ml/what-is-ml) — **Google** — crisp, authoritative separation of AI, ML and DL, and of the supervised/unsupervised split.

**Papers**:
- [A Few Useful Things to Know About Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — **Pedro Domingos (2012)** — learning as representation plus evaluation plus optimization; the single best short read on what generalization means.
- [Computing Machinery and Intelligence](https://courses.cs.umbc.edu/471/papers/turing.pdf) — **Alan Turing (1950)** — the founding question, still the clearest statement of what "intelligent behaviour" would mean.
- [Deep Learning](https://www.nature.com/articles/nature14539) — **LeCun, Bengio and Hinton (Nature, 2015)** — the field's authoritative review by its founders; where DL sits inside ML.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — the model is the small box; the lifecycle around it is where the cost lives.

**Books**:
- [*An Introduction to Statistical Learning*](https://www.statlearning.com/) — **James, Witten, Hastie and Tibshirani** — free PDF; Ch. 2 is the reference treatment of the U-curve pages 4 and 5 introduce.
- [*Artificial Intelligence: A Modern Approach* — Ch. 1](https://aima.cs.berkeley.edu/) — **Russell and Norvig** — the standard AI textbook; chapter 1 defines the field and its history (sample chapters free).
- [*Dive into Deep Learning* — Ch. 1 "Introduction"](https://d2l.ai/chapter_introduction/index.html) — **Zhang, Lipton, Li and Smola** — frames the data → model → objective → optimization loop with runnable code.
- [*Neural Networks and Deep Learning* — Ch. 1](http://neuralnetworksanddeeplearning.com/chap1.html) — **Michael Nielsen** — free online; the gentlest complete account of what a network does.
