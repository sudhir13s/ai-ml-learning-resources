---
id: "06-nlp/word-embeddings/the-embedding-space"
topic: "Word Embeddings: The Embedding Space"
parent: "06-nlp"
chapter_of: "06-nlp/word-embeddings"
chapter: 5
level: intermediate
built_from: ["06-nlp/word-embeddings"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 14
leads_to: ["06-nlp/word-embeddings/using-word-embeddings"]
core_idea: "Embeddings are compared by angle, so cosine similarity measures relatedness and consistent relations become parallel offsets; the same geometry carries the biases of the training text and is judged both intrinsically and on downstream tasks."
title: "The Embedding Space"
minutes: 14
category: natural-language-processing
---

# The embedding space: similarity, analogies and bias

With the three methods built, this page reads the space they produce: what near means, how analogies work, and what else the space absorbed.

## The embedding space: similarity, analogies, and bias

### Cosine similarity — why angle, not distance

Two embeddings are compared by **cosine similarity** — the cosine of the angle between them, which ignores their lengths:

$$\cos(a, b) = \frac{a \cdot b}{\lVert a\rVert\,\lVert b\rVert} \in [-1, 1].$$

Why the *angle* and not raw Euclidean distance:

- A word's vector **magnitude** correlates with its frequency and other nuisance factors, while its **direction** carries the meaning.
- Two words pointing the same way are similar regardless of length; cosine throws the length away.
- Cosine = 1 means identical direction (synonyms-ish), 0 means orthogonal (unrelated), negative means opposed.
- Finding a word's nearest neighbours by cosine is how you retrieve synonyms.

### Analogies as parallelograms

The analogy "$a$ is to $b$ as $c$ is to **?**" is solved by the **vector offset method**: compute $b - a + c$ and return the word whose vector is closest (by cosine) to it.

- The geometry is a **parallelogram**: if the displacement $b - a$ (e.g. man→king, the "royalty" direction) is *approximately* the same as $d - c$ (woman→queen), the four points roughly form a parallelogram and $b - a + c \approx d$.
- The picture below is drawn from **real GloVe vectors**: `man→king` and `woman→queen` are near-parallel.
- `king − man + woman` lands *closest to* `queen` (cosine 0.85) — close, but, honestly, not exactly on it.

![A parallelogram drawn from real GloVe-50 vectors, projected onto the plane spanned by the royalty (king−man) and gender (woman−man) directions: man, king, woman, queen as labelled points with near-parallel arrows man→king and woman→queen. The computed point king − man + woman (green ring) is the parallelogram's fourth corner; queen is its NEAREST word (cosine 0.85) but not identical — the dotted line is the small residual, an honest reminder that the analogy is approximate, not exact.](images/we_analogy_parallelogram.png)

> [!WARNING]
> **Analogies are flakier than the famous example suggests.** Two caveats interviewers reward you for knowing:
>
> 1. The search **excludes the input words** $a, b, c$ from the answer — without that exclusion, `king − man + woman` often returns `king` itself, because it's still the nearest vector.
> 2. Analogy accuracy is real but **brittle** — it works well for frequent, "clean" relations (capital–country, male–female, comparatives) and poorly for rare or noisy ones.
>
> It's a *property* of the space, not a reliable reasoning engine.

### Explore the space yourself

The same real GloVe-50 vectors, as a cloud you can turn — pick a word to see its neighbours, or build an analogy and watch the parallelogram close.

<!-- EXPLORER: embedding-space {"data": "assets/glove-embedding-space.json", "initialWord": "king"} -->
> **Interactive explorer — the GloVe embedding space.** 167 curated words (royalty and gendered pairs, countries, capitals, numbers, verb tenses, animals, adjectives, and the page's own examples) in a rotatable 3-D view. Type or click a word for its nearest neighbours with their cosines, or switch to analogy mode for $a - b + c$ with the answer's rank. The dots are a PCA projection keeping 35.5% of the variance; every number is computed in the full 50-dimensional space. Without the widget, the Code 2 output and the PCA and parallelogram figures above show the same vectors.

What to try, and what each move proves:

- **Pick `cat`.** `dog` is its nearest neighbour at 0.9218 — the number Code 2 prints — then `rabbit` at 0.8488; the animals sit together.
- **Pick `king`.** `prince` (0.8236) edges out `queen` (0.7839, as in Code 2), then `emperor` — royalty and family words share contexts.
- **Pick `good`.** `better` leads at 0.9284, then `going` and `happy` — frequent words used in the same slots, not synonyms; distributional similarity is relatedness, not meaning.
- **Run `king − man + woman`.** `queen` comes first at 0.8524, and the full-vocabulary line matches Code 2 (`throne` 0.7664, `prince` 0.7592).
- **Run `bigger − big + small`.** `larger` beats the expected `smaller`, which ranks 2nd — the brittleness the warning above describes.
- **Rotate the cloud.** Countries and their capitals sit in separate regions with the capital offset running roughly the same way, and two dots that look close can still have a low cosine — the picture is a shadow.

### Embeddings inherit bias

> [!WARNING]
> **Embeddings absorb the stereotypes in their training text.**
>
> - Because they're learned from human-written corpora, embeddings encode the biases in that text.
> - The *same* arithmetic that gives `king − man + woman ≈ queen` also yields, on real Google-News vectors, `doctor − man + woman ≈ nurse` and `computer_programmer − man + woman ≈ homemaker` (Bolukbasi et al., 2016).
> - This is a **measured, real-world harm**, not a curiosity: any downstream system — résumé screening, search, recommendation — built on biased embeddings can **propagate and amplify** that bias.
> - "How do embeddings encode bias, and how would you measure/mitigate it?" is a frequent interview *and* ethics question.
> - Mitigations exist (projecting out a learned "gender direction," as in Bolukbasi et al.) but are partial — the bias is diffuse, not confined to one axis.

> [!NOTE]
> **Source:** the measured gender bias and the "gender-direction" projection mitigation are [Bolukbasi, Chang, Zou, Saligrama & Kalai, *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings* (NeurIPS 2016)](https://arxiv.org/abs/1607.06520).

---

## How they're evaluated

You measure embedding quality two ways, and good answers name both:

- **Intrinsic** — does the geometry match human judgment, *directly*? Fast to compute, but a proxy. Two standard probes:
  - **Analogy accuracy:** the king/queen task over a benchmark of thousands of analogies (Google's analogy set).
  - **Word-similarity correlation:** does cosine rank pairs the way humans do, scored by Spearman correlation against human ratings on **WordSim-353**, **SimLex-999**, etc.
- **Extrinsic** — does plugging the embeddings into a *downstream* task (NER, named-entity recognition; sentiment; parsing; retrieval) actually improve it?
  - This is what ultimately matters.
  - Intrinsic scores are a quick sniff test that doesn't always predict downstream gains.

> [!TIP]
> A high intrinsic score doesn't guarantee downstream wins, and vice versa.
> If you can only report one number in an interview, report the **extrinsic** one ("it lifted NER F1 by X") — it's the number that pays the bills.

---

## Code 2: measure the real magic on pretrained GloVe

The from-scratch model proves the *mechanism*; **real pretrained vectors** prove the *magic*. This loads GloVe-50 (66 MB, downloads once) and measures the analogy, the cosines, and a capital-city analogy — every number quoted on this page comes from here.

```step
///FILE glove_measure_analogies.py
"""Measure real GloVe vectors: analogy + cosines. Verified on Python 3.12, gensim 4.x, CPU."""
import numpy as np, gensim.downloader as api
g = api.load("glove-wiki-gigaword-50")          # 400k words, 50-dim, downloads once

def cos(a, b):
    va, vb = g[a], g[b]
    return float(va @ vb / (np.linalg.norm(va) * np.linalg.norm(vb)))

# THE analogy: king - man + woman = ? (input words auto-excluded by most_similar)
print("king - man + woman ->", g.most_similar(positive=["king", "woman"], negative=["man"], topn=3))
# a capital-city analogy: paris - france + italy = ?
print("paris - france + italy ->", g.most_similar(positive=["paris", "italy"], negative=["france"], topn=3))

for a, b in [("cat","dog"), ("cat","kitten"), ("cat","democracy"),
             ("king","queen"), ("good","great"), ("good","bad")]:
    print(f"cos({a:>5}, {b:<9}) = {cos(a,b):+.4f}")
```

Output:

```text
king - man + woman -> [('queen', 0.8524), ('throne', 0.7664), ('prince', 0.7592)]
paris - france + italy -> [('rome', 0.8466), ('milan', 0.7766), ('turin', 0.7666)]
cos(  cat, dog      ) = +0.9218
cos(  cat, kitten   ) = +0.6386
cos(  cat, democracy) = +0.0368
cos( king, queen    ) = +0.7839
cos( good, great    ) = +0.7983
cos( good, bad      ) = +0.7965
```

> [!NOTE]
> **Read the numbers like a researcher.**
>
> - `queen` is the **nearest** word to `king − man + woman` (0.852) — the famous result, *measured*.
> - `paris − france + italy → rome` shows the capital direction is real too.
> - The cat triplet is textbook: `dog` (0.92) ≫ `kitten` (0.64) ≫ `democracy` (0.04).
> - One honest wrinkle: `cos(good, bad) = 0.80`, almost as high as `cos(good, great) = 0.80` — **antonyms look similar** to distributional embeddings because *good* and *bad* appear in nearly identical contexts ("the food was ___").
> - Distributional similarity is **relatedness**, not sentiment — a real limitation, and a great thing to mention in an interview.

---

## References

Shared with the topic's companion file — see [Word Embeddings — references and further reading](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/word-embeddings-word2vec-glove-fasttext/word-embeddings-word2vec-glove-fasttext#references-further-reading).
