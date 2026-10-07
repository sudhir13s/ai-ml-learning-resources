---
id: "06-nlp/word-embeddings"
topic: "Word Embeddings (Word2Vec, GloVe, FastText)"
parent: "06-nlp"
level: intermediate
built_from: ["linear-algebra", "softmax", "logistic-regression"]
interview_frequency: very-high
template: concept-deep
updated: 2026-10-08
tier: core
est_minutes: 15
leads_to: ["06-nlp/word-embeddings/word2vec"]
chapters:
  - "word2vec.md"
  - "negative-sampling.md"
  - "glove.md"
  - "fasttext.md"
  - "the-embedding-space.md"
  - "using-word-embeddings.md"
title: "Word Embeddings (Word2Vec, GloVe, FastText)"
minutes: 15
category: natural-language-processing
core_idea: "Give each word a learned point in space so that words sharing contexts sit close and relations become directions; word2vec, GloVe and FastText are three routes to factorizing the same co-occurrence statistics, and all share the one-vector-per-word limit."
---

# Word Embeddings: turning words into geometry

To a neural network a word is just a symbol, and symbols have no notion of *meaning* or *similarity*. The very first job of any NLP system is to turn words into numbers, and the *way* you do it decides everything downstream.

Do it the obvious way and the damage is immediate:

- **One slot per word** — a single 1 in a sea of zeros.
- "cat" and "kitten" end up *exactly* as far apart as "cat" and "thermodynamics."
- The model starts with zero knowledge that any two words are related, and **relearns every fact about every word from scratch**.

**Word embeddings** fix this by placing every word at a point in a few-hundred-dimensional space. Two things hold:

- **Words used in similar contexts land near each other.**
- Remarkably, *directions* in that space carry meaning.

The most famous demonstration is that, with real pretrained vectors, the arithmetic

$$\text{king} - \text{man} + \text{woman} \approx \text{queen}$$

actually works (we'll *measure* it later in this page — GloVe-50 returns `queen` at cosine **0.852**, the nearest word). Embeddings turned text into geometry, and they are the direct conceptual ancestor of every modern token-embedding layer at the bottom of every transformer.

I'm going to teach this the way I'd explain it at a whiteboard:

- **Why one-hot has to die** (feel the waste), then the 1950s idea that rescues us.
- **word2vec** end to end: both objectives, the softmax bottleneck, and the negative-sampling trick that made it scale.
- **GloVe** (the count-based cousin), the deep result that *unifies* the two, and **FastText** (words made of pieces).
- **Four numeric examples** worked by hand and by measurement, closing on the one limitation that ended the era and gave us BERT.

By the end you'll be able to:

- explain precisely **why one-hot fails** and what the **distributional hypothesis** buys you;
- **derive** the skip-gram softmax objective $p(o\mid c)$ and its **gradient**, and explain the **softmax bottleneck**;
- **derive** the negative-sampling loss $\log\sigma(u_o^\top v_c) + \sum_k \mathbb{E}[\log\sigma(-u_k^\top v_c)]$ and the $\text{freq}^{0.75}$ sampling trick — and compute one update **by hand**;
- contrast **skip-gram vs CBOW**, **word2vec vs GloVe** (predictive vs count-based), and state the **Levy & Goldberg** result that SGNS (skip-gram with negative sampling) ≈ shifted PMI (pointwise mutual information) factorization;
- **derive** the GloVe least-squares objective $J = \sum f(X_{ij})(w_i^\top\tilde w_j + b_i + \tilde b_j - \log X_{ij})^2$ and explain *why* ratios make analogies linear;
- explain what **FastText** adds (subword n-grams → OOV, out-of-vocabulary, handling + morphology) and *measure* it on an unseen word;
- reason about the **embedding geometry** — cosine similarity, analogies as parallelograms, and the **bias** embeddings inherit (Bolukbasi et al.);
- explain the fatal limitation — **one vector per word, regardless of context** — that motivated [contextual embeddings (ELMo/BERT)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/contextual-embeddings-elmo-bert/contextual-embeddings-elmo-bert).

Intuition first, then the math (with sources), then runnable, verified code.

> [!NOTE]
> "Embedding" just means a learned, dense, low-dimensional vector for a discrete thing.
> Word embeddings are the famous case, but the *same idea* embeds users, products, graph nodes, and — in every transformer — **tokens**.
> Get the intuition here and it transfers everywhere.

---

## The problem: one-hot has no notion of similarity

The most literal way to feed a word to a model is **one-hot encoding**. Fix a vocabulary of $V$ words (say $V = 50{,}000$) and represent each word as a $V$-long vector of zeros with a single 1 in its slot.

- "cat" might be slot 8,123; "dog" slot 8,124; "thermodynamics" slot 41,002.
- Clean and unambiguous — and quietly catastrophic, for two reasons.

**Flaw 1 — no similarity, by construction.**

- Any two distinct one-hot vectors are **orthogonal**: dot product exactly 0, Euclidean distance exactly $\sqrt 2$, *for every pair*.
- So the representation says "cat" and "kitten" are precisely as related as "cat" and "Tuesday" — not at all.
- One-hot encodes *identity* and nothing else; every shred of meaning must be relearned, per word, with zero sharing.

> [!NOTE]
> **Make it concrete:**
>
> - With one-hot, "I adopted a **cat**" and "I adopted a **kitten**" share *no* input features for the differing word, so a classifier that learned something from the first sentence transfers **nothing** to the second.
> - Dense embeddings let "cat" and "kitten" share most of their vector, so learning about one teaches the model about the other for free.
> - That *generalization* is the whole prize.

**Flaw 2 — huge and sparse.**

- The dimension *equals the vocabulary*.
- A first weight matrix mapping one-hot inputs into a hidden layer of size $h$ is $V \times h$ — for $V=50{,}000$, $h=300$ that's **15 million parameters in the input layer alone**, almost all touched by exactly one word each.
- It's a lookup table wearing a matrix-multiply costume, and a wasteful one.

![Top: a one-hot vector — its length equals the whole vocabulary, all zeros but a single 1, so every word sits orthogonal to every other and cos('cat','kitten') = cos('cat','tuesday') = 0. Bottom: a short dense embedding where every dimension carries graded meaning and two words are compared by cosine. The whole chapter is the recipe for getting from the top row to the bottom one.](images/we_onehot_vs_dense.png)

The fix rests on a simple 1950s idea, the **distributional hypothesis**, captured by J.R. Firth's slogan *"you shall know a word by the company it keeps"* (Firth, 1957).

- Words that appear in similar contexts (you *ruled* a *kingdom*; you *wore* a *crown*; you *sat* on a *throne*) tend to mean similar things.
- The recipe: **learn a dense vector per word such that words sharing contexts get similar vectors.**
- That single sentence is the entire research program of this page — word2vec, GloVe, and FastText are three different ways to carry it out.

> [!NOTE]
> **Source:**
>
> - The distributional hypothesis traces to Firth's *"A synopsis of linguistic theory"* (1957) and [Harris, *Distributional Structure* (1954)](https://doi.org/10.1080/00437956.1954.11659520).
> - Its modern, operational form — vectors learned so context-sharing words are close — is laid out in [Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 6 "Vector Semantics and Embeddings"](https://web.stanford.edu/~jurafsky/slp3/6.pdf) (also in the references).

---

## What it is: meaning as location

A **word embedding** maps each word to a dense vector — typically 50–300 dimensions — learned so that the *geometry* reflects meaning. Two properties make it feel like magic:

1. **Similar words cluster.** Cosine similarity between vectors tracks semantic similarity.
   - With real GloVe-50 vectors (measured later): $\cos(\text{cat}, \text{dog}) = 0.92$, $\cos(\text{cat}, \text{kitten}) = 0.64$, but $\cos(\text{cat}, \text{democracy}) = 0.04$.
   - Related words are close; unrelated words are near-orthogonal.
2. **Meaning becomes arithmetic.** Consistent relationships show up as consistent *directions*.
   - The vector from *man* to *king* is roughly the same as from *woman* to *queen* — the displacement *encodes* "royalty."
   - So you can **add and subtract meanings**, and `king − man + woman` lands next to `queen`.

The picture below is **not a cartoon** — it is a PCA (principal component analysis) projection of *real* pretrained GloVe-50 vectors.

- Royalty, animals, capitals, and countries each form their own region of the space.
- The dashed arrows show the *same* male→female direction shared by `king→queen` and `prince→princess`.

![A 2-D PCA of real GloVe-50 vectors: royalty (king/queen/prince/princess), animals (cat/dog/rabbit/horse), capitals (paris/london/rome/berlin), and countries (france/england/italy/germany) each cluster in a distinct region; dashed purple arrows show the shared king→queen / prince→princess direction.](images/we_pca_real.png)

> [!TIP]
> **See it for real:** the **[TensorFlow Embedding Projector](https://projector.tensorflow.org/)** loads real pretrained word2vec/GloVe vectors.
> Fly through the space in 3-D, search a word, and watch its nearest neighbours light up — the best way to *feel* that this geometry is real, not a story.

---

## Intuition: the map of meaning

Here's the analogy I'd actually draw at a whiteboard. You're handed thousands of books in a language you can't read and asked to organize the words.

- You can't look up definitions, but you *can* see which words tend to appear near each other.
- Some word always shows up next to "ruled," "throne," "crown" — and another word shows up in those *same* slots.
- Without learning what either means, you'd file them together: they *act the same*, so they probably *mean* something similar.

Do this for every word and you've drawn a **map** where proximity = "appears in similar company." That map is exactly what an embedding is. The distributional hypothesis is the bet that **the map of company is a good map of meaning.**

Now the more surprising part — *why directions mean things*.

- On that map, walk from "man" to "king." What changed? You added "royalty."
- If the map is consistent, walking the *same direction and distance* from "woman" should also add "royalty" — landing you on "queen."
- The relationship isn't stored in any single word; it's a **direction you can travel** that means the same thing everywhere on the map.
- So `king − man + woman ≈ queen` is not a parlor trick but a *structural* property: when a corpus uses "king/man" and "queen/woman" in parallel ways, gradient descent has no choice but to place them in a parallelogram.

> [!NOTE]
> **Why a few hundred dimensions?**
>
> - **Too few** (say 2): you can't fit all the independent "directions of meaning" a language needs — gender, tense, plurality, formality, topic, sentiment — so they collide.
> - **Too many** (say 50,000, i.e. one-hot): you're back to no sharing.
> - **A few hundred** is the empirical sweet spot: enough axes to disentangle the major factors of variation, few enough that words must *share* structure (which is what forces similar words together).
> - The 2-D pictures on this page are PCA *shadows* of that richer space — useful, but lossy.

> [!TIP]
> **The one-sentence interview answer.** If asked "what is a word embedding, in one breath?":
>
> *"A learned dense vector per word, trained so that words appearing in similar contexts get similar vectors — which turns semantic similarity into cosine distance and analogies into vector arithmetic."*
>
> Everything else on this page is the *how* behind that sentence.

---

## References

The curated link library for this topic — videos, courses, interactive demos, articles, papers, books, and internal cross-links — lives in a companion file so it can be reused as a standalone reference list:

**→ [Word Embeddings — references and further reading](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/word-embeddings-word2vec-glove-fasttext/word-embeddings-word2vec-glove-fasttext#references-further-reading)**
