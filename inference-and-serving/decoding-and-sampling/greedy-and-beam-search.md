---
id: "09-llms/decoding-and-sampling/greedy-and-beam-search"
topic: "Decoding: Greedy and Beam Search"
parent: "09-llms"
chapter_of: "09-llms/decoding-and-sampling"
chapter: 1
level: intermediate
built_from: ["09-llms/decoding-and-sampling"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: flagship
est_minutes: 10
leads_to: ["09-llms/decoding-and-sampling/sampling-temperature-top-k-top-p"]
core_idea: "Greedy takes the single likeliest token and beam search keeps the b likeliest partial sequences; both hunt the most probable sequence, which suits a task with one right answer and turns bland and repetitive on open-ended text."
title: "Greedy and Beam Search"
minutes: 10
category: inference-and-serving
---

# Greedy and beam search: decoding as a search for the likeliest text

The [menu](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling) offers many dishes; this page covers the two decoders that always order the safest ones.

## The strategies, derived

Generating text is a **search over sequences**, and it cannot be solved exactly:

- The model scores a whole sequence by the chain rule, $p_\theta(x_1, \dots, x_T) = \prod_{t=1}^{T} p_\theta(x_t \mid x_{<t})$, so "the best text" means the $\arg\max$ of that product.
- With $|V|$ choices at each of $T$ steps there are $|V|^T$ candidates: a 50,000-token vocabulary and a 20-token answer give about $10^{94}$.
- Each step depends on the tokens chosen before it, so the search does not split into independent per-position choices.
- **Every decoder is therefore a heuristic** for walking that tree.

> [!NOTE]
> **Source:** the chain-rule factorization and the search-versus-sampling split are laid out in [Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 10](https://web.stanford.edu/~jurafsky/slp3/10.pdf) and in [How to generate text](https://huggingface.co/blog/how-to-generate) (von Platen, Hugging Face).

There are two families.

- **Search** decoders (greedy, beam) try to find the *most probable sequence*.
- **Sampling** decoders (temperature / top-k / top-p) *draw* from the distribution with controlled randomness — the [next page](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/sampling-temperature-top-k-top-p).

### Greedy: argmax, and why it's myopic

Greedy is the simplest possible rule — at each step emit the single highest-probability token:

$$x_t = \arg\max_i \; p_i = \arg\max_i \; z_i$$

- Since softmax is monotonic, the argmax of the probabilities equals the argmax of the logits, so greedy doesn't even need the softmax.
- It's deterministic (same prompt → same output, no seed) and fast.

> [!NOTE]
> **Source:** the greedy / argmax decoder and its myopia are laid out in [Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 10 — Large Language Models](https://web.stanford.edu/~jurafsky/slp3/10.pdf), which frames autoregressive generation and contrasts greedy against search and sampling.

The flaw is structural, not incidental.

- Greedy maximizes $p(x_t \mid x_{<t})$ at each step, but the **product** $\prod_t p(x_t \mid x_{<t})$ — the probability of the whole sequence — is *not* maximized by a chain of locally-greedy choices.
- A token that looks slightly worse now can open up a far more probable continuation later, and greedy can never see it.
- Worse, on open-ended text the locally-optimal choice **reinforces itself into a loop** (the repetition the [first page](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling) describes).
- Greedy is the right tool only when the answer is essentially deterministic: "2 + 2 = ___", or extracting a field from a document.

**A two-step tree shows the myopia in numbers.** After the prompt the model gives $P(A) = 0.55$ and $P(B) = 0.45$, so greedy commits to **A**.

- After A the next token is spread out: $P(X \mid A) = 0.40$, $P(Y \mid A) = 0.35$, $P(Z \mid A) = 0.25$. Greedy ends at **AX**, joint probability $0.55 \times 0.40 = 0.22$.
- After B nearly all the mass sits on one token: $P(P \mid B) = 0.95$. The sequence **BP** scores $0.45 \times 0.95 = 0.4275$ — almost **double**.
- Greedy never considers BP, because B lost the *first* comparison. Beam search with width 2 keeps both first tokens and finds it.

![A two-step generation tree. Greedy takes the locally-best first token A (0.55) and ends at AX with joint probability 0.22; but the globally best sequence is BP (0.4275), reachable only by keeping the lower-probability first token B. Beam search with width 2 keeps both A and B and recovers BP. Numbers computed in `code/decoding_strategies.py`.](images/decode_beam_tree.png)

### Beam search: keep several hypotheses alive

Beam search attacks greedy's myopia directly: instead of committing to one token, keep the **$b$ most-probable partial sequences** ("beams") at every step.

- Expand every beam by every possible next token.
- Score all the resulting candidate sequences by their cumulative log-probability, and keep the top $b$.
- At the end, return the highest-scoring complete sequence.

```mermaid
---
title: Beam search with width b=2, pruning to the two best sequences each step
---
graph TD
    R(["&lt;start&gt;"])
    R --> A["the<br/>logP −0.5"]
    R --> B["a<br/>logP −1.2"]
    R --> C["one<br/>logP −3.0"]
    A --> A1["the cat<br/>logP −1.1"]
    A --> A2["the dog<br/>logP −1.4"]
    B --> B1["a cat<br/>logP −1.9"]
    B --> B2["a man<br/>logP −2.6"]
    A1 --> done(["beam width b=2:<br/>keep the 2 best partial<br/>sequences each step"])
    B1 --> done

    class A,B,A1,B1 success
    class done focus
```

*Beam search with width $b=2$. At each step every surviving beam is expanded by all tokens, the candidates are scored by cumulative log-probability, and only the top $b$ survive (green nodes kept, unmarked nodes pruned). Greedy is the special case $b=1$; exhaustive search is $b = |V|^{T}$.*

> [!NOTE]
> **Source:** beam search for sequence decoding is presented with worked code in [*Dive into Deep Learning*, Ch. 10 — Beam Search](https://d2l.ai/chapter_recurrent-modern/beam-search.html), which derives greedy as the $b=1$ special case and the length-normalized scoring below.

Beam search shines on **closed-ended** tasks and fails on open-ended ones:

- **Closed-ended** — [machine translation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/machine-translation/machine-translation) (MT), [summarization](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/text-summarization/text-summarization), constrained generation. There *is* a single best answer, and beam with length normalization and $b$ of 4–8 reliably beats greedy on the BLEU and ROUGE overlap scores (bilingual evaluation understudy; recall-oriented understudy for gisting evaluation).
- **Open-ended** — it fails in a surprising way: **maximum-probability text is bland and repetitive.**

Why the open-ended case goes wrong:

- Holtzman et al. showed that the most-likely sequences a model can produce are *degenerate*.
- Humans don't write the highest-probability continuation; real language is full of mildly-surprising choices.
- Beam search, by hunting probability, hunts exactly the wrong thing for creative text.

### Length normalization: don't punish long sequences

For closed-ended use, one practical fix targets beam's bias toward *short* sequences.

- Every log-probability is **negative**, so raw cumulative log-prob only ever *subtracts* with each extra token.
- Raw beam search therefore prefers to stop early, which **truncates** translations and summaries.
- **Length normalization** divides the score by a length penalty $\text{lp}(y)$, the Google neural machine translation (NMT) form:

$$\text{score}(y) = \frac{1}{\text{lp}(y)} \sum_{i=1}^{|y|} \log p_\theta(y_i \mid y_{<i}), \qquad \text{lp}(y) = \frac{(5 + |y|)^\alpha}{(5 + 1)^\alpha}$$

How to read the penalty:

- $\alpha = 0$ means no normalization; the usual setting is $\alpha \approx 0.6$–$0.7$.
- The growing denominator offsets the accumulating negative log-probs, so long and short hypotheses compete fairly.
- The $+5$ smoothing keeps even $\alpha = 1$ from becoming an exact per-token mean, which is why $\alpha$ is tuned rather than set to 1. The plain mean log-prob $\frac{1}{|y|}\sum_i \log p_\theta(y_i \mid y_{<i})$ is the fully length-fair score.

> [!NOTE]
> **Source:** length-normalized beam scoring is from [Wu et al., *Google's Neural Machine Translation System* (2016)](https://arxiv.org/abs/1609.08144), §7, Eq. 14 (the $\text{lp}(Y)$ length penalty), and is reproduced with code in [*Dive into Deep Learning*, Ch. 10 — Beam Search](https://d2l.ai/chapter_recurrent-modern/beam-search.html).

> [!WARNING]
> Bigger beams are **not** monotonically better.
> - Past a point, very large beams in machine translation *hurt* quality: they over-favour short, generic, high-probability outputs (the "beam search curse").
> - $b$ between 4 and 10 is the practical sweet spot; $b = 50$ often degrades.
> - **Source:** [Koehn & Knowles, *Six Challenges for Neural Machine Translation* (2017)](https://arxiv.org/abs/1706.03872).

### Diverse beam search

Vanilla beams tend to be near-duplicates — all variations on the single best path — which wastes the width.

- **Diverse beam search** splits the beams into groups and adds a dissimilarity penalty, so each group explores a *different* region of the tree.
- Reach for it when you want several genuinely distinct candidates: caption variety, or an n-best list to rerank.
- **Source:** [Vijayakumar et al., *Diverse Beam Search* (2018)](https://arxiv.org/abs/1610.02424).

### Worked example: a three-step beam trace in log-space

A width-2 trace with explicit scores makes the prune step concrete. Take the vocabulary $\{a, b, c\}$ and natural-log probabilities, all negative:

- **Step 1**, from the prompt: $\log p(a) = -0.5$, $\log p(b) = -0.7$, $\log p(c) = -2.0$. Keep the top two, $\{a: -0.5,\ b: -0.7\}$, and drop $c$.
- **Step 2**: expand each survivor by all three tokens and *add* the new log-prob to its running score.

| Candidate | computation | score |
|---|---|---|
| $aa$ | $-0.5 + (-1.2)$ | $-1.7$ |
| $ab$ | $-0.5 + (-0.4)$ | $\mathbf{-0.9}$ |
| $ac$ | $-0.5 + (-1.6)$ | $-2.1$ |
| $ba$ | $-0.7 + (-0.3)$ | $\mathbf{-1.0}$ |
| $bb$ | $-0.7 + (-1.5)$ | $-2.2$ |
| $bc$ | $-0.7 + (-2.4)$ | $-3.1$ |

Sort all six and keep the top two, $\{ab: -0.9,\ ba: -1.0\}$. Two things to notice:

- **Pruning is global across all expansions.** $ab$ (a child of $a$) and $ba$ (a child of $b$) are compared on one score scale, and the survivors come from different parents.
- **A weaker prefix can win.** $ba$ beats $aa$ ($-1.7$) even though $a$ was the better first token — the same mechanism that recovers BP in the tree above.

![Beam search (width 2) scoring in log-space across two steps on the {a,b,c} tree. Left: step 1 keeps the top-2 first tokens (a, b in green) and prunes c (slate). Right: step 2 expands both survivors into six candidates, scores each by adding the next log-prob, and keeps ab (−0.9) and ba (−1.0) — note ba beats aa (−1.7) even though 'a' was the better first token, because pruning is global across all expansions. Numbers from `code/decoding_strategies.py`.](images/decode_beam_trace.png)

**Step 3** repeats the expand-score-prune cycle on $ab$ and $ba$.

- A beam that emits the end-of-sequence token is set aside as a **finished** candidate, scored with length normalization.
- The search continues until $b$ finished candidates exist or the length cap hits, then returns the best finished one.

> [!NOTE]
> Beams are scored in log-space because raw probabilities **underflow**.
> - After 50 tokens a product like $0.3^{50} \approx 10^{-26}$ is near the edge of float32's range; after a few hundred it rounds to exactly 0.0 and every hypothesis ties.
> - Summing logs ($50 \times \log 0.3 = -60.2$) is numerically stable and keeps the ranking, because log is monotonic.

---

## References

Shared with the topic's companion file — see [Decoding & Sampling — references](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling#references-further-reading).
