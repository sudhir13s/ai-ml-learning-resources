---
id: "06-nlp/word-embeddings/glove"
topic: "Word Embeddings: GloVe"
parent: "06-nlp"
chapter_of: "06-nlp/word-embeddings"
chapter: 3
level: intermediate
built_from: ["06-nlp/word-embeddings"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 14
leads_to: ["06-nlp/word-embeddings/fasttext"]
core_idea: "GloVe fits word vectors so their dot products match log co-occurrence counts, built so that vector differences encode the co-occurrence ratios that carry meaning; skip-gram with negative sampling turns out to factorize nearly the same matrix implicitly."
title: "GloVe"
minutes: 14
category: natural-language-processing
---

# GloVe: the count-based route to the same vectors

Word2vec learns from one window at a time; GloVe counts every co-occurrence first, and this page shows the two meet in the same place.

## The deep result: SGNS is implicitly factorizing a PMI matrix

Here is the unification that ties this course together and that strong candidates love to drop. **Levy & Goldberg (2014)** proved that skip-gram with negative sampling (SGNS), at its optimum, is **implicitly factorizing** a word–context matrix whose entries are the **shifted pointwise mutual information**:

$$u_o^\top v_c \;=\; \text{PMI}(o, c) - \log k, \qquad \text{where}\quad \text{PMI}(o,c) = \log \frac{P(o, c)}{P(o)\,P(c)}.$$

In words:

- The dot product SGNS learns for a (context, center) pair *converges to* how much more often those two words co-occur than chance (their PMI), shifted down by $\log k$ (the number of negatives).
- So the "predictive" neural method and the "count-based" methods are **secretly doing the same thing**: both extract a low-rank approximation of a co-occurrence/PMI matrix.
- This is *why* word2vec and GloVe vectors behave almost identically despite opposite-looking training.
- It is also the bridge to GloVe, which factorizes log-co-occurrence *explicitly*.

> [!NOTE]
> **Source:**
>
> - The SGNS ≈ shifted-PMI factorization result is [Levy & Goldberg, *Neural Word Embedding as Implicit Matrix Factorization* (NeurIPS 2014)](https://papers.nips.cc/paper/5477-neural-word-embedding-as-implicit-matrix-factorization).
> - PMI as a word-association measure predates it by decades — [Church & Hanks, *Word Association Norms, Mutual Information, and Lexicography* (1990)](https://aclanthology.org/J90-1003/).

---

## GloVe: the count-based cousin

[GloVe](https://nlp.stanford.edu/pubs/glove.pdf) (Global Vectors; Pennington, Socher & Manning, 2014) reaches the same destination from the *opposite* direction.

- Instead of *predicting* one local window at a time, it first builds the **global co-occurrence matrix** $X$ in one pass over the corpus — $X_{ij}$ = how often word $j$ appears in the context of word $i$.
- Then it factorizes $X$ so that vector dot products match **log co-occurrence counts**.

### Deriving the objective

GloVe's design starts from one observation: it's not raw co-occurrence but **ratios** of co-occurrence probabilities that carry meaning. Let $P_{ij} = X_{ij}/X_i$ be the probability that $j$ appears in $i$'s context. Consider *ice* and *steam*:

- $P(\text{solid}\mid \text{ice}) / P(\text{solid}\mid \text{steam})$ is **large** (solid relates to ice, not steam).
- The $P(\text{gas}\mid\cdot)$ ratio is **small**.
- For a word like *water* or *fashion* (related to both, or neither) the ratio is **~1**.

The *ratio* cleanly isolates the relevant dimension of meaning. From there:

- GloVe asks for vectors whose differences capture these ratios.
- Working that requirement through (a function of $w_i - w_j$ acting on $\tilde w_k$, made linear and symmetric) lands on the target $w_i^\top \tilde w_j \approx \log X_{ij}$.
- Turning that into a weighted least-squares fit gives the objective:

$$\boxed{\ J = \sum_{i,j=1}^{V} f(X_{ij})\,\big(w_i^\top \tilde w_j + b_i + \tilde b_j - \log X_{ij}\big)^2\ }$$

Every term earns its place:

- $w_i^\top \tilde w_j$ — the dot product of word $i$'s vector and context-word $j$'s vector, which we want to equal $\log X_{ij}$ (the **same dot-product-equals-association** target as SGNS, just made explicit).
- $b_i, \tilde b_j$ — per-word **bias** terms that absorb each word's overall frequency, so the dot product only has to model the *interaction*.
- $f(X_{ij})$ — a **weighting function** that down-weights both extremes:
  - it's 0 at $X_{ij}=0$ (skip pairs that never co-occur — the matrix is sparse, which makes this cheap);
  - it rises with count, then **caps** so that hyper-frequent pairs like ("the", "of") don't dominate the fit;
  - the paper uses $f(x) = \min\!\big((x/x_{\max})^{0.75},\ 1\big)$ — and there's that **0.75** again, the same frequency-damping instinct as negative sampling.

![GloVe's weighting function f(x) = min((x/x_max)^0.75, 1): exactly zero at x=0 (never-co-occurring pairs are skipped — the matrix is sparse, so this is cheap), rising with the co-occurrence count, then flattening to a hard cap of 1 once x ≥ x_max so that a handful of ultra-frequent pairs can't dominate the least-squares fit. The same 0.75 frequency-damping exponent appears in word2vec's negative-sampling distribution.](images/we_glove_weighting.png)

### Worked example: the ice/steam ratio, by the numbers

The ratio intuition is easy to *measure*. Take a (toy) co-occurrence matrix for `ice` and `steam` against four probe words, and turn counts into conditional probabilities $P(j\mid i) = X_{ij}/X_i$:

| probe word $j$ | $P(j\mid\text{ice})$ | $P(j\mid\text{steam})$ | ratio $P(j\mid\text{ice})/P(j\mid\text{steam})$ | reads as |
|---|---|---|---|---|
| solid | 0.606 | 0.067 | **9.09** | ≫ 1 → belongs to **ice** |
| gas | 0.081 | 0.611 | **0.13** | ≪ 1 → belongs to **steam** |
| water | 0.303 | 0.311 | **0.97** | ≈ 1 → related to **both** |
| fashion | 0.010 | 0.011 | **0.91** | ≈ 1 → related to **neither** |

![The co-occurrence ratio P(j|ice)/P(j|steam) on a log axis for four probe words: solid sits at 9.09 (≫1, belongs to ice), gas at 0.13 (≪1, belongs to steam), while water (0.97) and fashion (0.91) both land on the dashed ratio=1 line — for opposite reasons. The discriminating signal that distinguishes ice from steam lives in the ratio, not the raw counts, which is exactly what GloVe is built to encode in vector differences.](images/we_ice_steam_ratio.png)

Look at what the **ratio** does that a raw probability can't:

- `water` and `fashion` both give ratio ≈ 1, but for opposite reasons (both-relevant vs both-irrelevant).
- `solid`/`gas` cleanly point to one word each.
- The discriminating signal — "what distinguishes ice from steam" — lives in the *ratio*, not the raw counts.

GloVe is engineered so that **vector differences reproduce these ratios**:

- It sets $w_i^\top \tilde w_j \approx \log X_{ij}$.
- So $w_{\text{ice}}^\top \tilde w_j - w_{\text{steam}}^\top \tilde w_j \approx \log\!\big(X_{\text{ice},j}/X_{\text{steam},j}\big)$ — exactly the log-ratio that isolates meaning.
- That is *why* differences of GloVe vectors are linear and analogies work.

(These numbers are reproducible; the structure, not the toy counts, is the point.)

> [!TIP]
> **The clean interview contrast:**
>
> - **word2vec is predictive** (stream local windows, online SGD, never builds a matrix); **GloVe is count-based** (build the global co-occurrence matrix once, then batch-factorize it).
> - But by **Levy & Goldberg**, skip-gram is *implicitly* factorizing a (shifted-PMI) co-occurrence matrix too — so the two extract the same statistics, which is why their vectors are nearly interchangeable in practice.
> - "Different roads, same city."

> [!NOTE]
> **A fourth method you should be able to name: SVD on the PMI matrix.**
>
> - The oldest count-based route is to build the PMI (or PPMI = positive PMI) word–context matrix *directly* and take its truncated **SVD** (singular value decomposition) for low-rank vectors.
> - Levy & Goldberg (2015) showed that, tuned well, this classic method is *competitive* with word2vec/GloVe.
> - All four (SVD-PPMI, SGNS, GloVe, and even good old LSA, latent semantic analysis) are variations on **factorize a co-occurrence-association matrix**.
> - The neural framing was a faster, online way to do something statistics had been doing for decades.
>
> **Source:** the weighted-least-squares objective and the $f(x)$ weighting are [Pennington, Socher & Manning, *GloVe: Global Vectors for Word Representation* (EMNLP 2014)](https://nlp.stanford.edu/pubs/glove.pdf).
>
> - §3 derives $w_i^\top\tilde w_j \approx \log X_{ij}$ from the ratio requirement.
> - §4.2 gives $f(x)=\min((x/x_{\max})^{0.75},1)$.
> - §3 opens with the ice/steam ratio table.

---

## References

Shared with the topic's companion file — see [Word Embeddings — references and further reading](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/word-embeddings-word2vec-glove-fasttext/word-embeddings-word2vec-glove-fasttext#references-further-reading).
