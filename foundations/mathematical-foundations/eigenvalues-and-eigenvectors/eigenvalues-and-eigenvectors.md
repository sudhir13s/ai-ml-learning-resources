---
id: "01-foundations/eigenvalues-and-eigenvectors"
topic: "Eigenvalues & Eigenvectors"
parent: "01-foundations"
level: intermediate
built_from: ["01-foundations/matrices-and-matrix-operations"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Eigenvalues & Eigenvectors"
minutes: 10
category: mathematical-foundations
core_idea: "An eigenvector is a direction a matrix only scales and never turns, Av = λv, with the eigenvalue λ as the scale factor; a matrix's eigenvectors are its natural axes, the idea behind PCA, spectral methods and the stability of repeated multiplication."
---

# Eigenvalues & Eigenvectors
> An eigenvector is a direction a matrix only *stretches* (never rotates); its eigenvalue is the
> stretch factor. Diagonalizing a matrix by its eigenvectors reveals the "natural axes" of the
> transformation — the idea behind PCA, spectral clustering, PageRank, and the stability of
> iterative methods.

**Why it matters:** eigen-decomposition is the entry point to PCA and SVD, and it explains why
covariance matrices have orthogonal principal axes, what the Graph Laplacian's spectrum encodes,
and why repeated multiplication by a matrix converges to its dominant eigenvector. Expect "derive
PCA from the covariance eigenvectors" and "what does a negative/zero eigenvalue mean?"

**Watch it move**: one matrix bends the whole grid — most vectors are **turned off their line**, while the two eigenvectors **stay on their line** and are only scaled by their eigenvalue.

```video
src: images/eigenvectors_stay_on_their_line.mp4
poster: images/eigenvectors_stay_on_their_line_poster.png
captions: images/eigenvectors_stay_on_their_line.en.vtt
title: Eigenvectors stay on their line while the plane transforms
caption: A = [[2, 1], [1, 2]] applied to the plane; eigenpairs from numpy (λ = 3 along (1, 1), λ = 1 along (−1, 1)), rendered with Manim Community Edition; regenerate with tools/gen_eigenvectors_video.py in the ai-ml-learning-resources repository.
duration: 0:35
transcript: |
  The matrix A = [[2, 1], [1, 2]] is about to transform the whole plane.
  Four vectors start on their own dashed lines: two ordinary ones and two special ones.
  A moves every grid line. Watch where each vector lands.
  (1, 0) lands on (2, 1) and (−1, 2) lands on (0, 3): each turns 26.6°, off its own line.
  (1, 1) lands on (3, 3), which is 3 × (1, 1): it stays on its line, stretched by λ = 3.
  (−1, 1) lands on (−1, 1), which is 1 × (−1, 1): same line, eigenvalue λ = 1.
  Eigenvectors are the directions a matrix only scales, never turns. The eigenvalue is the scale.
  Because A is symmetric, its two eigenvector lines are perpendicular: the fact PCA relies on.
```

## How to work through it

1. **See it move** — watch [3B1B: Eigenvectors and eigenvalues](https://www.youtube.com/watch?v=PFDu9oVAE-g). *The "axes that don't get knocked off their span" picture makes the definition obvious.*
2. **Compute a few** — watch [StatQuest / Professor Dave: finding eigenvalues & eigenvectors](https://www.youtube.com/watch?v=TQvxWaQnrqI), then do [Khan: eigen-everything](https://www.khanacademy.org/math/linear-algebra/alternate-bases/eigen-everything/v/linear-algebra-introduction-to-eigenvalues-and-eigenvectors). *The characteristic polynomial `det(A − λI) = 0` by hand.*
3. **Diagonalization & spectral theorem** — read [MML Ch. 4.2–4.4](https://mml-book.github.io/book/mml-book.pdf). *Eigendecomposition, symmetric ⇒ orthogonal eigenvectors (the fact PCA relies on).*
4. **The full lecture** — watch [MIT 18.06: Eigenvalues & Eigenvectors (Lec 21)](https://www.youtube.com/watch?v=lXNXrLcoerU). *Strang ties eigenvalues to stability, powers of a matrix, and diagonalization.*
5. **Connect to ML** — read [ai-ml-intuitions 1.05 Spectral Methods (PCA/SVD)](/ai-ml/ai-ml-intuitions/representation/dimensionality-and-latent-structure/pca-and-svd-intuition). *Where eigen-thinking becomes dimensionality reduction.*

## References

- **In this platform**:
  - [Graph Representations](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/graph-representations-intuition) — what the spectrum of a graph's Laplacian encodes.
  - [Matrices & Matrix Operations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/matrices-and-matrix-operations/matrices-and-matrix-operations) — the prerequisite this page builds on.
  - [Matrix Decompositions](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/matrix-decompositions/matrix-decompositions) — builds directly on this page: factorizations beyond the eigendecomposition.
  - [Principal Component Analysis — the math](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/principal-component-analysis-math/principal-component-analysis-math) — builds directly on this page: covariance eigenvectors as principal axes.
  - [Singular Value Decomposition](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/singular-value-decomposition/singular-value-decomposition) — builds directly on this page: the decomposition for any matrix.
  - [Spectral Methods (PCA/SVD)](/ai-ml/ai-ml-intuitions/representation/dimensionality-and-latent-structure/pca-and-svd-intuition) — the intuition, where eigen-thinking becomes dimensionality reduction.
- **Videos**:
  - [Abstract vector spaces | Ch. 16](https://www.youtube.com/watch?v=TgKwz5Ikpc8) — **3Blue1Brown** — why eigenvectors are basis-independent (a recurring interview subtlety).
  - [Eigenvalues & Eigenvectors (18.06 Lec 21)](https://www.youtube.com/watch?v=lXNXrLcoerU) — **Gilbert Strang (MIT OCW)** — full lecture: diagonalization and stability.
  - [Eigenvectors and eigenvalues | Ch. 14](https://www.youtube.com/watch?v=PFDu9oVAE-g) — **3Blue1Brown** — the definitive visual intuition.
  - [Finding Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=TQvxWaQnrqI) — **Professor Dave Explains** — clean worked example of the characteristic equation.
- **Courses**:
  - [Khan Academy — Eigen-everything](https://www.khanacademy.org/math/linear-algebra/alternate-bases/eigen-everything/v/linear-algebra-introduction-to-eigenvalues-and-eigenvectors) — **Khan Academy** — definitions and computation with exercises.
  - [MIT 18.06 — Eigenvalues & Eigenvectors (Lec 21–22)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — **Gilbert Strang (MIT OCW)** — diagonalization, powers, and the spectral theorem.
- **Interactive**:
  - [Explained Visually — Eigenvectors and Eigenvalues](https://setosa.io/ev/eigenvectors-and-eigenvalues/) — **Victor Powell & Lewis Lehe** — drag a vector and watch which directions survive the transformation unrotated; the shortest route to the definition.
  - [Immersive Linear Algebra — Ch. 10 "Eigenvalues and Eigenvectors"](https://immersivemath.com/ila/ch10_eigen/ch10.html) — **Ström, Åström & Akenine-Möller** — interactive eigenvectors with worked examples.
- **Articles**:
  - [CS229 Linear Algebra Review — eigenvalues/eigenvectors](https://cs229.stanford.edu/section/cs229-linalg.pdf) — **Stanford** — the ML-oriented summary, including symmetric and positive semidefinite matrices.
  - [Mathematics for ML (course notes) — eigenstuff & spectral theorem](https://gwthomas.github.io/docs/math4ml.pdf) — **Garrett Thomas (Stanford)** — concise ML-focused treatment.
- **Books**:
  - [Introduction to Applied Linear Algebra (VMLS) — **eigenvalues & dynamics**](https://web.stanford.edu/~boyd/vmls/vmls.pdf) — **Boyd & Vandenberghe** — applied eigen-analysis.
  - [Mathematics for Machine Learning — **Ch. 4.1–4.4 (Matrix Decompositions)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — eigendecomposition, the spectral theorem, and diagonalization.
</content>
