---
id: "19-advanced-math/functional-analysis"
topic: "Functional Analysis"
parent: "19-advanced-research-mathematics"
level: advanced
built_from: ["linear-algebra", "real-analysis", "measure-theory"]
interview_frequency: low
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Functional Analysis"
minutes: 10
category: advanced-mathematics-for-ai-research
---

# Functional Analysis — Banach & Operator Theory
> Linear algebra in infinite dimensions: complete normed spaces (Banach), inner-product spaces
> (Hilbert), bounded linear operators, dual spaces, and spectral theory. The framework that makes
> "a function as a point in a space" and "an operator as a matrix" rigorous — the language of RKHS,
> kernel methods, Fourier analysis, PDE-views of diffusion, and operator-theoretic deep learning.

**Why it matters:** every time you treat a *function* as a vector (kernels, GPs, Fourier, neural
operators) you're standing in a Banach or Hilbert space. The Riesz representation theorem is *why*
RKHS evaluation is an inner product; spectral theory is *why* the graph/Fourier transforms
diagonalize operators. This is the connective tissue under cards 3, 11, and 12.

**Start here — suggested path:**

1. **Anchor on Banach spaces** — watch [Lecture 1: Basic Banach Space Theory](https://www.youtube.com/watch?v=uoL4lQxfgwg) (MIT 18.102). *Completeness + norms is the whole game; start where the rigor starts.*
2. **Get to Hilbert spaces** — watch [Lecture 14: Basic Hilbert Space Theory](https://www.youtube.com/watch?v=EBdgFFf54U0). *Inner products, orthogonality, projections — the setting for least-squares, Fourier, and RKHS.*
3. **Read it carefully** — work the MIT [18.102 course materials](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/) alongside the lectures. *Notes + problem sets are where the definitions become reflexes.*
4. **See the key theorems** — focus on Riesz representation, Hahn–Banach, and the open-mapping theorem in the [18.102 lecture notes and readings](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/). *These four theorems are the "big results" everything else cites.*
5. **Aim at the payoff** — read the spectral-theorem chapter, then jump to [RKHS (card 3)](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/hilbert-spaces-and-rkhs/hilbert-spaces-and-rkhs). *Spectral theory + Riesz is exactly what kernels need.*

## Courses (free)
- [MIT 18.102 — Introduction to Functional Analysis (Spring 2021)](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/) — **Casey Rodriguez (MIT OCW)** — full video course + notes + problem sets, Banach → Hilbert → spectral theory.
- [Functional analysis (34-video course)](https://www.youtube.com/playlist?list=PLBh2i93oe2qsGKDOsuVVw-OCAfprrnGfr) — **The Bright Side of Mathematics** — metric spaces → Banach → Hilbert → Hahn–Banach and spectral theory, one idea per short video.
- [Functional Analysis — lecture notes](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT520_fall_2023/MAT520_Lecture_Notes.pdf) — **Princeton MAT520** — concise graduate notes covering the core theorems.

## Videos
- [MIT 18.102 — Lecture 1: Basic Banach Space Theory](https://www.youtube.com/watch?v=uoL4lQxfgwg) — **Casey Rodriguez (MIT OCW)** — completeness, norms, and why infinite dimensions are different.
- [MIT 18.102 — Lecture 14: Basic Hilbert Space Theory](https://www.youtube.com/watch?v=EBdgFFf54U0) — **Casey Rodriguez (MIT OCW)** — inner products, orthogonal projection, and Riesz.
- [The Geometric Anatomy of Theoretical Physics — Lec 09: tangent vector spaces (linear-algebra primer)](https://www.youtube.com/watch?v=UPGoXBfm6Js) — **Frederic Schuller** — rigorous vector-space thinking that transfers directly to function spaces.
- [Lecture 2 on kernel methods: RKHS](https://www.youtube.com/watch?v=2uvpOKoiYoI) — **Julien Mairal (Inria)** — sees functional analysis put to work building a Hilbert space of functions.

## Key Papers
- [Kernel methods in machine learning](https://projecteuclid.org/journals/annals-of-statistics/volume-36/issue-3/Kernel-methods-in-machine-learning/10.1214/009053607000000677.full) — **Hofmann, Schölkopf & Smola (2008)** — the canonical bridge from operator/Hilbert-space theory to ML.
- [A Primer on Reproducing Kernel Hilbert Spaces](https://arxiv.org/abs/1408.0952) — **Manton & Amblard (2015)** — functional analysis assembled from scratch toward RKHS, free on arXiv.

## Articles / Blogs (free, no paywall)
- [Applied Analysis — Ch. 5 "Banach Spaces"](https://www.math.ucdavis.edu/~hunter/book/ch5.pdf) — **John Hunter & Bruno Nachtergaele (UC Davis)** — normed and Banach spaces built from scratch, one readable chapter, free from the authors.
- [From Zero to Reproducing Kernel Hilbert Spaces in Twelve Pages or Less](http://users.umiacs.umd.edu/~hal3//docs/daume04rkhs.pdf) — **Hal Daumé III** — the fastest path from inner-product spaces to operators that matter in ML.

## Books (free, with chapters)
- [Applied Analysis — **Ch. 5 (Banach Spaces), Ch. 6 (Hilbert Spaces), Ch. 8–9 (bounded operators, spectrum)**](https://www.math.ucdavis.edu/~hunter/book/pdfbook.html) — **John Hunter & Bruno Nachtergaele** — graduate-standard and fully free, chapter by chapter, with the spectral theory the RKHS card needs.
- [Mathematics for Machine Learning — **Ch. 3 (Analytic Geometry: inner products, norms, projections)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — the finite-dimensional on-ramp before infinite dimensions.

## In this platform
- Foundations (the basics this builds on): [Norms, Inner Products & Orthogonality](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/norms-inner-products-and-orthogonality/norms-inner-products-and-orthogonality) · [Eigenvalues & Eigenvectors](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/eigenvalues-and-eigenvectors/eigenvalues-and-eigenvectors) · [SVD](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/singular-value-decomposition/singular-value-decomposition)
- Concept depth (the *why*): [ai-ml-intuitions 1.05 Spectral Methods (PCA/SVD)](/ai-ml/ai-ml-intuitions/representation/dimensionality-and-latent-structure/pca-and-svd-intuition)
- Next concepts: [03 Hilbert Spaces & RKHS](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/hilbert-spaces-and-rkhs/hilbert-spaces-and-rkhs) · [12 Fourier Analysis & Signal Processing](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/fourier-analysis-and-signal-processing/fourier-analysis-and-signal-processing)
