---
id: "foundations/programming-and-data-foundations"
topic: "Programming and Data Foundations"
level: beginner
built_from: ["ai-ml-orientation"]
updated: 2026-09-07
---

# Programming and Data Foundations

> The toolchain every later page assumes you already have: Python, the array and table libraries
> the whole ecosystem is built on, the plotting stack you explore data with, the notebook you work
> in, and the environment discipline that stops "it works on my machine". The sub-area ends with
> one complete scikit-learn project so the tools stop being abstract.

**Start here:** [Python for ML](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/python-for-ml/python-for-ml) if the language is new, otherwise jump straight to [NumPy Essentials](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/numpy-essentials/numpy-essentials) — arrays are the concept the rest of the stack is a wrapper around.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters, a five-step
start-here path, and verified courses, videos, papers, articles and books.

### The language

1. [Python for ML](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/python-for-ml/python-for-ml) — the subset of Python that machine-learning work actually uses, and what you can safely skip.

### The data stack

2. [NumPy Essentials](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/numpy-essentials/numpy-essentials) — the `ndarray`, vectorization, broadcasting and indexing; the object Pandas and PyTorch are both built on.
3. [Pandas Essentials](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/pandas-essentials/pandas-essentials) — DataFrames and Series: loading, cleaning, filtering, grouping and joining the tabular data most projects start from.
4. [Data Visualization Basics](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/data-visualization-basics/data-visualization-basics) — Matplotlib for control and Seaborn for statistical plots; exploratory data analysis (EDA) as a habit.

### The workbench

5. [Jupyter and Google Colab](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/jupyter-and-google-colab/jupyter-and-google-colab) — cell-by-cell exploration, and free graphics processing units (GPUs) with nothing installed.
6. [Environments and Package Management](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/environments-and-package-management/environments-and-package-management) — pip, venv, conda and uv; the isolation discipline that makes a result reproducible.

### Putting it together

7. [Your First ML Project](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/your-first-ml-project/your-first-ml-project) — one end-to-end scikit-learn run: load, explore, split, fit, evaluate, improve.

## Courses (free)

- [Python for Everybody](https://www.py4e.com/) — **Charles Severance, University of Michigan** — free and complete from absolute zero; the standard first Python course.
- [The Python Tutorial](https://docs.python.org/3/tutorial/) — **Python Software Foundation** — the canonical, always-correct reference course for the language itself.
- [Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas) — **Kaggle** — free and interactive; the fastest route to real DataFrame fluency, in a hosted notebook.
- [scikit-learn — Getting Started](https://scikit-learn.org/stable/getting_started.html) — **scikit-learn maintainers** — the `fit`/`predict`/`transform` API and a first pipeline, from the library's own team.

## Videos

- [Get started with Google Colaboratory](https://www.youtube.com/watch?v=inN8seMm7UI) — **TensorFlow** — the official walkthrough of the free notebook environment, runtimes and GPUs included.
- [Track Your PyTorch Experiments with Weights & Biases](https://www.youtube.com/watch?v=KESSYZExK44) — **Weights & Biases** — the habit worth forming the first time you run more than three experiments in a notebook.

## Key Papers

- [Array Programming with NumPy](https://www.nature.com/articles/s41586-020-2649-2) — **Harris et al. (Nature, 2020)** — the definitive account of what NumPy is and why it underpins scientific Python.
- [Data Structures for Statistical Computing in Python](https://proceedings.scipy.org/articles/Majora-92bf1922-00a) — **Wes McKinney (2010)** — the original Pandas paper, by its creator.
- [Scikit-learn: Machine Learning in Python](https://www.jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf) — **Pedregosa et al. (JMLR, 2011)** — the paper introducing scikit-learn and the design that made it the default.
- [API design for machine learning software](https://arxiv.org/abs/1309.0238) — **Buitinck et al. (2013)** — the estimator/transformer philosophy behind the entire library; read it once and the API stops needing memorization.

## Articles / Blogs (free, no paywall)

- [A Visual Intro to NumPy and Data Representation](https://jalammar.github.io/visual-numpy/) — **Jay Alammar** — the clearest visual explanation of arrays, broadcasting and reshaping anywhere.
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) — **NumPy documentation** — the rules that trip everyone up, with diagrams; the official source, not a paraphrase.
- [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html) — **Pandas documentation** — the single most-used Pandas pattern, explained precisely.
- [Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — **scikit-learn documentation** — data leakage and the mistakes that quietly ruin a first project.

## Books (free, with chapters)

- [*Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/) — **Jake VanderPlas** — free online; Ch. 2 NumPy, Ch. 3 Pandas, Ch. 4 Matplotlib, Ch. 5 scikit-learn — this sub-area's shape in one book.
- [*Python for Data Analysis*, 3rd ed.](https://wesmckinney.com/book/) — **Wes McKinney** — free online, written by the creator of Pandas; the definitive tabular-data reference.
- [*Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/) — **Claus Wilke** — free online; how to visualize well rather than which function to call.
- [*The Good Research Code Handbook*](https://goodresearch.dev/) — **Patrick Mineault** — free online; environments, dependencies and project layout treated as part of doing science properly.

## In this platform

- Section index: [Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme)
- Before this: [AI/ML Orientation](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/readme) · After this: [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) · [Data Preparation](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/readme) · [Tools and Frameworks](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/readme) · [Research Literacy](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme) · [AI Paradigms and Knowledge](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/readme)
- What the first project is judged by: [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) · [Bias-Variance Tradeoff](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/bias-variance-tradeoff/bias-variance-tradeoff)
- The array intuitions underneath: [Cosine vs Euclidean Distance](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/cosine-vs-euclidean-distance-intuition) · [One-Hot Encoding](/ai-ml/ai-ml-intuitions/representation/discrete-representations/one-hot-encoding-intuition)
- Doing it rather than reading it: [Data Preparation workflow](/ai-ml/practitioner-workflows/workflow-library/data-and-inputs/data-preparation) · [Experiment Tracking workflow](/ai-ml/practitioner-workflows/workflow-library/training-and-adaptation/experiment-tracking)
