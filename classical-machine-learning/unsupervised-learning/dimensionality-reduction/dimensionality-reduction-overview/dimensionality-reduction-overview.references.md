---
id: "04-unsupervised-learning/dimensionality-reduction-overview/references"
topic: "Dimensionality Reduction — References"
parent: "04-unsupervised-learning/dimensionality-reduction-overview"
type: references
updated: 2026-09-07
---

# Dimensionality Reduction — References

> Companion link library for **[Dimensionality Reduction — Overview](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/dimensionality-reduction/dimensionality-reduction-overview/dimensionality-reduction-overview)** (the concept page, PCA-centric). Curated links — external sources *and* internal cross-links to related pages on this platform — kept separate so it can be reused as a standalone reference list. Grouped by type, alphabetical within each group. Every entry is a primary author or a recognized deep explainer, chosen for depth on *this* topic, and every link verified.

- **In this platform**:
  - [Data Preparation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme) — scaling and standardization, which PCA depends on.
  - [Deep Learning (autoencoders)](/ai-ml/ai-ml-learning-resources/deep-learning/readme) — learned, non-linear compression.
  - [Dimensionality Reduction — Overview](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/dimensionality-reduction/dimensionality-reduction-overview/dimensionality-reduction-overview) — the concept page this list accompanies.
  - [Foundations — PCA, the math](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/principal-component-analysis-math/principal-component-analysis-math) — the PCA and SVD math foundations, the why.
  - [k-Nearest Neighbors (curse of dimensionality)](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/classification/k-nearest-neighbors/k-nearest-neighbors) — the failure mode that motivates reduction.
  - [Spectral Methods (PCA / SVD)](/ai-ml/ai-ml-intuitions/representation/dimensionality-and-latent-structure/pca-and-svd-intuition) — the intuition behind the linear method.
  - [t-SNE](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/dimensionality-reduction/t-sne/t-sne) — a non-linear sibling among the manifold methods.
  - [UMAP](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/dimensionality-reduction/umap/umap) — a non-linear sibling among the manifold methods.
  - [Unsupervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/readme) — the field overview.
- **Videos**:
  - [PCA in Python — Machine Learning From Scratch 11](https://www.youtube.com/watch?v=52d7ha-GdV8) — **Patrick Loeber** — mean-centring, the covariance matrix, `numpy.linalg.eig`, and projecting onto the top components, written out in NumPy.
  - [PCA, main ideas in only 5 minutes](https://www.youtube.com/watch?v=HMOI_lkzW08) — **StatQuest (Josh Starmer)** — the fastest correct mental model of components and scree.
  - [PCA, Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ) — **StatQuest (Josh Starmer)** — components, loadings, and scree plots built from scratch.
  - [Principal Component Analysis (PCA)](https://www.youtube.com/watch?v=g-Hb26agBFg) — **Luis Serrano** — illustrations-over-formulas intro; the best first watch for variance/projection.
  - [PyData: PCA, t-SNE, and UMAP — Modern Approaches to Dimension Reduction](https://www.youtube.com/watch?v=YPJQydzTLwQ) — **Leland McInnes (UMAP author)** — the unifying tour across linear and non-linear methods.
  - [Singular Value Decomposition (SVD) and PCA](https://www.youtube.com/watch?v=gXbThCXjZFM) — **Steve Brunton (UW)** — the SVD view of PCA, the numerically preferred route, derived cleanly.
- **Interactive**:
  - [Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html) — **scikit-learn** — PCA vs t-SNE vs Isomap vs LLE on one dataset; the clearest "which method" picture.
  - [Principal Component Analysis — interactive explainer](https://setosa.io/ev/principal-component-analysis/) — **Victor Powell & Lewis Lehe (Setosa)** — drag the data, watch the components rotate.
  - [Understanding UMAP](https://pair-code.github.io/understanding-umap/) — **Google PAIR** — how UMAP and t-SNE distort distances, and why their geometry isn't literal — the caveats every practitioner needs.
- **Articles**:
  - [A Tutorial on Principal Components Analysis](https://www.cs.otago.ac.nz/cosc453/student_tutorials/principal_components.pdf) — **Lindsay I. Smith (Otago)** — the classic from-scratch walkthrough: covariance, eigenvectors, and a fully worked numeric example, free PDF.
  - [CS229: Machine Learning — PCA & ICA lecture notes](https://cs229.stanford.edu/main_notes.pdf) — **Stanford (Andrew Ng)** — PCA and ICA derived rigorously, the variance and SVD views together.
  - [In Depth: Principal Component Analysis](https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html) — **Jake VanderPlas (Python Data Science Handbook)** — PCA for visualization, noise filtering, and compression, with code.
  - [Principal Components Analysis (lecture notes)](https://www.stat.cmu.edu/~cshalizi/uADA/12/lectures/ch18.pdf) — **Cosma Shalizi (CMU)** — a rigorous yet readable derivation of PCA as variance maximization and reconstruction (the Hotelling/Pearson views), free.
- **Papers**:
  - [A Global Geometric Framework for Nonlinear Dimensionality Reduction (Isomap)](https://wearables.cc.gatech.edu/paper_of_week/isomap.pdf) — **Tenenbaum, de Silva & Langford (2000)** — geodesic-distance manifold learning; unrolls the Swiss roll; free PDF.
  - [A Tutorial on Principal Component Analysis](https://arxiv.org/abs/1404.1100) — **Jonathon Shlens (2014)** — the most-cited free PCA tutorial; derives PCA from variance and from the SVD.
  - [Dimensionality Reduction: A Comparative Review](https://lvdmaaten.github.io/publications/papers/TR_Dimensionality_Reduction_Review_2009.pdf) — **van der Maaten, Postma & van den Herik (2009)** — free survey benchmarking PCA against the non-linear methods; the landscape in one paper.
  - [Nonlinear Component Analysis as a Kernel Eigenvalue Problem](https://www.mlpack.org/papers/kpca.pdf) — **Schölkopf, Smola & Müller (1998)** — the original kernel-PCA paper.
  - [Nonlinear Dimensionality Reduction by Locally Linear Embedding (LLE)](https://www.robots.ox.ac.uk/~az/lectures/ml/lle.pdf) — **Roweis & Saul (2000)** — local-neighbour reconstruction embedding; free PDF.
  - [On Lines and Planes of Closest Fit to Systems of Points in Space](https://pca.narod.ru/pearson1901.pdf) — **Karl Pearson (1901)** — the original PCA paper, the reconstruction-error ("closest fit") view; free scanned PDF.
  - [The Approximation of One Matrix by Another of Lower Rank](https://link.springer.com/article/10.1007/BF02288367) — **Eckart & Young (1936)** — the theorem that the truncated SVD is the optimal low-rank approximation (= min reconstruction error).
- **Documentation**:
  - [scikit-learn — Decomposition (PCA, kernel PCA, truncated SVD, ICA, NMF)](https://scikit-learn.org/stable/modules/decomposition.html#pca) — **scikit-learn** — the linear family with the explained-variance API and runnable code.
  - [scikit-learn — Manifold learning user guide](https://scikit-learn.org/stable/modules/manifold.html) — **scikit-learn** — the non-linear side (Isomap, LLE, t-SNE) placed next to PCA.
- **Books**:
  - [An Introduction to Statistical Learning (ISLP) — Ch. 12.2 "Principal Components Analysis"](https://www.statlearning.com/) — **James, Witten, Hastie, Tibshirani & Taylor** — free PDF; PCA intuition + the labs.
  - [Mathematics for Machine Learning — Ch. 10 "Dimensionality Reduction with PCA"](https://mml-book.github.io/) — **Deisenroth, Faisal & Ong** — PCA derived from first principles (projection, eigenvectors, SVD); the cleanest modern treatment.
  - [The Elements of Statistical Learning — Ch. 14.5 "Principal Components, Curves and Surfaces"](https://hastie.su.domains/ElemStatLearn/) — **Hastie, Tibshirani & Friedman** — free PDF; PCA and its non-linear generalizations, the reference treatment.
