---
id: "01-foundations/norms-inner-products-orthogonality"
topic: "Norms, Inner Products & Orthogonality"
parent: "01-foundations"
level: beginner
built_from: ["01-foundations/vectors-and-vector-spaces"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Norms, Inner Products & Orthogonality"
minutes: 10
category: mathematical-foundations
---

# Norms, Inner Products & Orthogonality
> The inner (dot) product measures *alignment*; a norm measures *length*; orthogonality means
> "no shared direction." Together they give geometry to vector spaces — angles, distances,
> projections — which is exactly what cosine similarity, L1/L2 regularization, least squares, and
> attention's scaled dot-product are built from.

**Why it matters:** the dot product is the most-used operation in ML. Interviewers ask why cosine
similarity divides out magnitude, the difference between L1 and L2 norms (and why one induces
sparsity), what an orthogonal matrix preserves, and why attention scales `QKᵀ` by `1/√d`. All of it
is inner-products and norms.

## How to work through it

1. **Dot product, geometrically** — watch [3B1B: Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0). *Why `a·b` relates to projection and angle, not just a sum of products.*
2. **Norms & distances in ML** — read [ai-ml-intuitions 1.07–1.08 Euclidean vs Cosine](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/cosine-vs-euclidean-distance-intuition) and [1.09 Manhattan/L1](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/manhattan-distance-intuition). *The exact place these definitions get used.*
3. **Formalize it** — read [MML Ch. 3 (Analytic Geometry)](https://mml-book.github.io/book/mml-book.pdf): inner products, norms, orthogonality, projections. *Definitions and the Cauchy–Schwarz inequality you'll quote.*
4. **Orthogonality & projection** — watch [MIT 18.06: Orthogonal Vectors & Subspaces](https://www.youtube.com/watch?v=YzZUIYRCE38). *Sets up least squares = projection onto a subspace.*
5. **Practice** — do [Khan: Projections](https://www.youtube.com/watch?v=27vT-NWuw0M) and norm exercises. *Cement projection formulas and L1/L2 mechanics.*

## References

- **In this platform**:
  - [Convexity](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/convexity/convexity) — related: norm balls are convex sets, which is the geometry behind L1 and L2 regularization.
  - [Euclidean vs Cosine](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/cosine-vs-euclidean-distance-intuition) — where these norms and inner products become similarity measures.
  - [Manhattan/L1](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/manhattan-distance-intuition) — the L1 norm as a distance, and why it favours sparsity.
  - [Scaled Dot-Product](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/scaled-dot-product-intuition) — the intuition for why attention scales the dot product by `1/√d`.
  - [Vectors & Vector Spaces](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/vectors-and-vector-spaces/vectors-and-vector-spaces) — the prerequisite this page builds on.
- **Videos**:
  - [Array, Norm and Dot Product with NumPy](https://www.youtube.com/watch?v=xSO0qOyvevc) — **Dr. Data Science** — the same three objects in code, with the axis and shape conventions that decide what you actually computed.
  - [Dot products and duality | Ch. 9](https://www.youtube.com/watch?v=LyGKycYT2v0) — **3Blue1Brown** — the geometry behind the dot product.
  - [Introduction to projections](https://www.youtube.com/watch?v=27vT-NWuw0M) — **Khan Academy** — the projection formula, worked step by step.
  - [Orthogonal Vectors and Subspaces (18.06 Lec 14)](https://www.youtube.com/watch?v=YzZUIYRCE38) — **Gilbert Strang (MIT OCW)** — orthogonality and the four-subspaces picture.
  - [Projection Matrices and Least Squares (18.06 Lec 16)](https://www.youtube.com/watch?v=osh80YCg_GM) — **Gilbert Strang (MIT OCW)** — projection = best approximation in a subspace.
  - [Understanding Vector Norms in Machine Learning (L1, L2, unit balls, NumPy)](https://www.youtube.com/watch?v=It2g7sDxdqI) — **Dr. Data Science** — the unit balls of each norm drawn, then computed with `numpy.linalg.norm`; the picture behind L1 sparsity.
- **Courses**:
  - [Khan Academy — Alternate coordinate systems (bases, orthogonality)](https://www.khanacademy.org/math/linear-algebra/alternate-bases) — **Khan Academy** — orthonormal bases, projections, Gram–Schmidt with exercises.
  - [MIT 18.06 — Orthogonality & Projections (Lec 14–16)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — **Gilbert Strang (MIT OCW)** — orthogonal subspaces, projections, least squares.
- **Interactive**:
  - [Immersive Linear Algebra — Ch. 3 "The Dot Product"](https://immersivemath.com/ila/ch03_dotproduct/ch03.html) — **Ström, Åström & Akenine-Möller** — interactive dot product, length, and angle.
- **Articles**:
  - [A visual explanation of L1 vs L2 regularization](https://explained.ai/regularization/) — **Terence Parr & Jeremy Howard** — why the L1 norm produces sparse solutions, geometrically.
  - [CS229 Linear Algebra Review](https://cs229.stanford.edu/section/cs229-linalg.pdf) — **Stanford** — norms, inner products, and orthogonal matrices in ML notation.
- **Books**:
  - [Introduction to Applied Linear Algebra (VMLS) — **Ch. 3 (Norm & Distance), Ch. 5 (Orthogonality)**](https://web.stanford.edu/~boyd/vmls/vmls.pdf) — **Boyd & Vandenberghe** — norms, distance, angle, Gram–Schmidt.
  - [Mathematics for Machine Learning — **Ch. 3 (Analytic Geometry)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — inner products, norms, orthogonality, projections, and Cauchy–Schwarz.
</content>
