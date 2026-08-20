---
id: "04-unsupervised-learning"
topic: "Unsupervised Learning"
level: intermediate
built_from: ["foundations", "linear-algebra"]
updated: 2026-06-27
---

# Unsupervised Learning
> Finding structure without labels — clustering (k-means, DBSCAN), dimensionality reduction
> (PCA, t-SNE, UMAP), and density estimation.

## 📑 Concept Index
Every chapter is a self-contained folder (`NN-Concept/NN-Concept.md`) with its page and a curated
`.references.md` resource card (free, open courses · videos · papers · articles · books · cross-links).
> **✅ ready · ⬜ coming soon.** New to the area? Start with the field overview below, then work top to bottom.

### Clustering
1. ✅ [K-Means Clustering](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/clustering/k-means-clustering/k-means-clustering)
2. ✅ [Hierarchical Clustering (agglomerative & divisive)](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/clustering/hierarchical-clustering/hierarchical-clustering)
3. ✅ [DBSCAN (density-based clustering)](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/clustering/dbscan/dbscan)
4. ✅ [Gaussian Mixture Models & EM](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/clustering/gaussian-mixture-models-and-em/gaussian-mixture-models-and-em)
5. ✅ [Spectral Clustering](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/clustering/spectral-clustering/spectral-clustering)

### Dimensionality reduction & manifold learning
6. ✅ [Dimensionality Reduction — overview (PCA · SVD framing, cross-link to math)](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/dimensionality-reduction/dimensionality-reduction-overview/dimensionality-reduction-overview)
7. ✅ [t-SNE](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/dimensionality-reduction/t-sne/t-sne)
8. ✅ [UMAP](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/dimensionality-reduction/umap/umap)

### Density & anomaly
9. ✅ [Anomaly / Outlier Detection (Isolation Forest · LOF · One-Class SVM)](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/anomaly-detection/anomaly-outlier-detection/anomaly-outlier-detection)
10. ✅ [Kernel Density Estimation](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/density-estimation/kernel-density-estimation/kernel-density-estimation)

### Patterns & structure
11. ✅ [Association Rule Learning (Apriori · FP-Growth)](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/association-rules/association-rule-learning/association-rule-learning)

### Representation (self-supervised)
12. ✅ [Contrastive / Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning)

### Related concepts (canonical home is another section)
> These topics are used across many areas, so they're kept in one place to avoid repetition.
- **PCA / SVD (the math)** — eigendecomposition, variance maximization, the SVD view → [Foundations — Maths for AI-ML](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maths-for-ai-ml/readme)
- **Autoencoders** — non-linear, learned dimensionality reduction → [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
- **Word / sentence embeddings** — representation learning over text → [NLP](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme)

## 🎓 Courses (free)
- [Machine Learning Specialization (Course 3)](https://www.coursera.org/specializations/machine-learning-introduction) — **Andrew Ng** — clustering & anomaly detection.
- [Kaggle Learn: Clustering & PCA notebooks](https://www.kaggle.com/learn) — **Kaggle** — applied, runnable.

## 🎥 Videos
- [StatQuest: PCA, t-SNE, k-means, Hierarchical clustering](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **Josh Starmer** — the canonical visual explanations.

## 📄 Key Papers / Articles
- [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) — **Distill** — interactive; the pitfalls everyone hits.
- [UMAP](https://arxiv.org/abs/1802.03426) — **McInnes et al. (2018)** — the modern manifold method + [great docs](https://umap-learn.readthedocs.io/).

## 📚 Books (free)
- [An Introduction to Statistical Learning (ISLP), Ch. 12](https://www.statlearning.com/) — **James et al.** — free; clustering & PCA, applied.

## 🔗 In this platform
- The geometry behind it: [ai-ml-intuitions 1.05 PCA/SVD, 1.11–1.12 t-SNE/UMAP, 1.18 k-Means](../../../ai-ml-intuitions/representation/)
