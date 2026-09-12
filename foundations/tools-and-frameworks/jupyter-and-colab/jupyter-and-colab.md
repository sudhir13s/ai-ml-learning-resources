---
id: "17-tools-and-frameworks/jupyter-colab"
topic: "Jupyter & Colab (notebooks, kernels, free GPUs)"
parent: "17-tools-and-frameworks"
level: beginner
built_from: ["python"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Jupyter & Colab (notebooks, kernels, free GPUs)"
minutes: 10
category: tools-and-frameworks
---

# Jupyter & Colab — Notebooks · Kernels · Free GPUs
> The interactive computing environment at the heart of data science: **Jupyter** notebooks mix
> live code, output, plots, and Markdown in one document, executed cell-by-cell by a **kernel**.
> **Google Colab** is a hosted Jupyter that needs zero setup and gives you free GPUs/TPUs in the
> browser — the fastest way to start training without a local machine.

**Why it matters:** notebooks are where almost all ML exploration, prototyping, and teaching
happens, and Colab removes the environment-setup barrier entirely. Knowing the cell/kernel execution
model (and its pitfalls — hidden state, out-of-order execution) is basic practical literacy for any
data/ML role, and Colab's free GPUs make deep-learning tutorials runnable by anyone.

**Start here — suggested path:**

1. **Open a Colab in one click** — read [Welcome to Colab](https://colab.research.google.com/notebooks/intro.ipynb) and run a cell. *Zero install; you're computing in 30 seconds.*
2. **Learn the notebook model** — [Jupyter Notebook Complete Beginner Guide](https://www.youtube.com/watch?v=5pf0_bpNbkw) (Rob Mulla). *Covers Jupyter, JupyterLab, Colab, and Kaggle in one tour.*
3. **Get comfortable in Colab** — read the [Colab FAQ](https://research.google.com/colaboratory/faq.html) on runtimes, GPU availability and session limits. *Knowing when a free runtime gets reclaimed is what keeps a long training run from vanishing.*
4. **Run Jupyter locally** — follow [Installing the Jupyter stack](https://docs.jupyter.org/en/latest/start/index.html). *For real projects you'll want local notebooks + version control.*
5. **Know the pitfalls** — internalize hidden state / out-of-order execution (covered in the beginner guide). *"Restart & Run All" is the habit that keeps notebooks reproducible.*

## Courses (free)
- [Jupyter documentation](https://docs.jupyter.org/en/latest/) — **Project Jupyter** — the authoritative guide to notebooks, kernels, and the ecosystem.
- [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/latest/) — **Project Jupyter** — the modern notebook IDE, from basics to extensions.

## Videos
- [Jupyter Notebook Complete Beginner Guide](https://www.youtube.com/watch?v=5pf0_bpNbkw) — **Rob Mulla** — Jupyter → JupyterLab → Colab → Kaggle in one video.
- [Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough](https://www.youtube.com/watch?v=HW29067qVWk) — **Corey Schafer** — installation, kernels, magics and the execution model, explained precisely.
- [Learn PyTorch for deep learning in a day. Literally.](https://www.youtube.com/watch?v=Z_ikDlimN6A) — **Daniel Bourke** — a full course taught inside notebooks; the environment in real use, GPU included.

## Key Papers
- [IPython: A System for Interactive Scientific Computing](https://fperez.org/papers/ipython07_pe-gr_cise.pdf) — **Pérez & Granger (2007), *CiSE*** — the paper behind the kernel/front-end architecture every notebook still runs on (author PDF).
- [About Project Jupyter](https://jupyter.org/about) — **Project Jupyter** — the project's own account of the notebook format and the governance behind it; the Kluyver et al. (2016) paper *"Jupyter Notebooks — a publishing format for reproducible computational workflows"* is cited there and remains the formal reference.
- [Jupyter documentation](https://docs.jupyter.org/en/latest/) — **Project Jupyter** — the canonical reference for the notebook architecture.

## Articles / Blogs (free, no paywall)
- [Welcome to Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb) — **Google** — the interactive intro notebook (run it as you read).
- [Project Jupyter home](https://jupyter.org/) — **Project Jupyter** — the ecosystem overview and try-it links.
- [Installing Jupyter](https://docs.jupyter.org/en/latest/start/index.html) — **Project Jupyter** — the official local setup guide.

## Books (free, with chapters)
- [Jupyter documentation (full)](https://docs.jupyter.org/en/latest/) — **Project Jupyter** — a book-length, free reference covering the whole stack.
- [JupyterLab docs (full)](https://jupyterlab.readthedocs.io/en/latest/) — **Project Jupyter** — comprehensive, free, chapter-structured guide.

## In this platform
- Related domain: [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) · [Data Preparation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme)
- Pairs with: [01 NumPy](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/numpy/numpy) · [02 Pandas](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pandas/pandas) · [03 Data Visualization](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/data-visualization/data-visualization)
