---
id: "06-nlp/word-embeddings/word2vec"
topic: "Word Embeddings: Word2Vec"
parent: "06-nlp"
chapter_of: "06-nlp/word-embeddings"
chapter: 1
level: intermediate
built_from: ["06-nlp/word-embeddings"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 14
leads_to: ["06-nlp/word-embeddings/negative-sampling"]
core_idea: "Word2vec learns two vectors per word by predicting each word's neighbours with a softmax over dot products; the gradient pulls a word toward its real neighbours and away from what the model over-predicts, and that softmax over the whole vocabulary is the cost to remove next."
title: "Word2Vec (Skip-gram and CBOW)"
minutes: 14
category: natural-language-processing
---

# Word2Vec: learning vectors by predicting neighbours

The [map of meaning](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/word-embeddings-word2vec-glove-fasttext/word-embeddings-word2vec-glove-fasttext) needs a way to place words; word2vec places them by training on which words appear together.

## Word2Vec: learn vectors by predicting neighbours

[Word2Vec](https://arxiv.org/abs/1301.3781) (Mikolov et al., 2013) makes the distributional hypothesis **trainable**.

- Slide a window over a giant corpus and learn vectors that are *good at predicting which words co-occur*.
- No labels, no annotation — the text supervises itself.
- It comes in two symmetric variants, and knowing exactly how they mirror each other is a classic interview question.

![Skip-gram (left): one center word 'king' is looked up and used to predict each of its context words (the, ruled, crown). CBOW (right): the context words are averaged into one vector and used to predict the single center word 'king'. The two objectives are mirror images.](images/we_skipgram_vs_cbow.png)

- **Skip-gram** — given the **center** word, predict each **context** word. One center → many predictions. Better for **rare words and small corpora**: every center–context pair is a separate training signal, so rare words get more "at-bats."
- **CBOW** (continuous bag-of-words) — given the **context** (averaged), predict the **center** word. Many context words → one prediction. **Faster to train** and slightly better on frequent words, because it smooths over the whole window in one shot.

We'll derive **skip-gram** in full because it's the one interviewers ask you to write down — and once you have it, CBOW is the same machinery run backwards.

### Two vectors per word — and why

Each word $w$ gets **two** learned vectors:

- A **center** (input) vector $v_w$, used when $w$ is the focus.
- A **context** (output) vector $u_w$, used when $w$ is a neighbour.

This asymmetry isn't a hack.

- A word rarely appears in its own context window, so forcing $u_w = v_w$ would make a word predict itself awkwardly and hurt optimization.
- After training you keep the center vectors $v_w$ as "the embedding" (or average $v_w$ and $u_w$ — both are common).

### The objective

Skip-gram maximizes the average log-probability of the true context words over the whole corpus of length $T$, within a window of half-width $c$:

$$\mathcal{J}(\theta) = \frac{1}{T}\sum_{t=1}^{T}\ \sum_{\substack{-c \le j \le c \\ j \ne 0}} \log p(w_{t+j}\mid w_t)$$

Each conditional is a **softmax over the entire vocabulary**, scoring how compatible a context word $o$ is with a center word $c$ via the dot product of their vectors:

$$\boxed{\ p(o\mid c) = \frac{\exp(u_o^\top v_c)}{\sum_{w \in V}\exp(u_w^\top v_c)}\ }$$

Read it plainly:

- The score of context word $o$ given center $c$ is the **dot product** $u_o^\top v_c$ (high when the two vectors point the same way).
- It is squashed through a softmax so the scores over all possible context words form a probability distribution.
- Maximize this and you are literally pushing $v_c$ toward the $u$'s of the words that *actually* surround $c$ — the distributional hypothesis in equation form.

> [!NOTE]
> **Source:**
>
> - The skip-gram and CBOW architectures are [Mikolov, Chen, Corrado & Dean, *Efficient Estimation of Word Representations in Vector Space* (2013)](https://arxiv.org/abs/1301.3781).
> - The softmax conditional $p(o\mid c)$ and its gradient are derived step by step in [Jurafsky & Martin, *SLP3* Ch. 6](https://web.stanford.edu/~jurafsky/slp3/6.pdf) and [*Dive into Deep Learning*, Ch. 15.1 (word2vec)](https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html).

### Deriving the gradient (the part you should be able to do)

Why does this objective *move vectors the right way*? Take the loss for a single (center $c$, true context $o$) pair, $\ell = -\log p(o\mid c)$, and differentiate with respect to the center vector $v_c$. Write $s_w = u_w^\top v_c$ for the score of each candidate $w$. Then

$$\ell = -\,s_o + \log \sum_{w\in V} \exp(s_w),$$

and differentiating the log-sum-exp gives the clean result

$$\frac{\partial \ell}{\partial v_c} = -\,u_o + \sum_{w\in V} p(w\mid c)\,u_w = -\Big(u_o - \mathbb{E}_{w\sim p(\cdot\mid c)}[u_w]\Big).$$

This is worth pausing on.

- The gradient is the **observed** context vector $u_o$ minus the **model's expected** context vector under its current beliefs.
- A gradient step moves $v_c$ *toward* the true neighbour $u_o$ and *away* from whatever the model currently over-predicts.
- That is exactly "make the real neighbours likely, the rest less so" — entirely standard softmax-classifier calculus.

> [!WARNING]
> **The softmax bottleneck.**
>
> - Look at the denominator $\sum_{w\in V}$. Computing $p(o\mid c)$ — and its gradient, which contains $\sum_w p(w\mid c)\,u_w$ — requires a sum over the **entire vocabulary** on *every* (center, context) pair.
> - With $V$ in the millions and billions of pairs, that's a non-starter: full-softmax skip-gram is correct but **computationally impossible at scale**.
> - Everything clever about word2vec's *training* is about dodging this sum.

![Cost per training pair on log–log axes: the full softmax does O(V) dot products per pair (red, climbs with vocabulary), while negative sampling does a constant O(k)=k+1 (green, flat). At V=10⁶ with k=10 that is roughly 91,000× less work per pair — the change that let word2vec train on billions of words on one machine.](images/we_softmax_bottleneck.png)

### CBOW: the same machinery, run backwards

For completeness, here is CBOW in one equation so you can see how it mirrors skip-gram. Instead of one center predicting many contexts, CBOW **averages** the context vectors into a single $\hat v$ and predicts the center word $c$ from it:

$$\hat v = \frac{1}{2c}\sum_{\substack{-c\le j\le c\\ j\ne 0}} v_{w_{t+j}}, \qquad p(c \mid \text{context}) = \frac{\exp(u_c^\top \hat v)}{\sum_{w\in V}\exp(u_w^\top \hat v)}.$$

The roles of $u$ and $v$ swap and the context is **pooled** before the softmax. That has three consequences:

- **Faster** — one prediction per window instead of $2c$.
- **Smoother on frequent words** — averaging washes out noise.
- **Worse on rare words** — a rare word's signal gets diluted in the average instead of being its own training example.

One mental model: **skip-gram makes $2c$ noisy predictions per window; CBOW makes one averaged prediction.** Same softmax bottleneck, same negative-sampling cure — everything below applies to both.

| | skip-gram | CBOW |
|---|---|---|
| **predicts** | each context word from center | center word from averaged context |
| **examples / window** | $2c$ (one per neighbour) | 1 (pooled) |
| **speed** | slower | **faster** |
| **rare words** | **better** (own signal) | worse (diluted) |
| **frequent words** | good | slightly **better** |
| **best when** | small corpus, rare-word quality | large corpus, speed matters |

---

## References

Shared with the topic's companion file — see [Word Embeddings — references and further reading](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/word-embeddings-word2vec-glove-fasttext/word-embeddings-word2vec-glove-fasttext#references-further-reading).
