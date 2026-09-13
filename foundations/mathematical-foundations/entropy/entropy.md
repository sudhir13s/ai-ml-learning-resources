---
id: "01-foundations/entropy"
topic: "Entropy"
parent: "01-foundations"
level: intermediate
built_from: ["01-foundations/random-variables-and-distributions"]
interview_frequency: high
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Entropy"
minutes: 10
category: mathematical-foundations
---

# Entropy
> Entropy `H(p) = −Σ p log p` measures the average uncertainty (or information content) of a
> distribution — the expected number of bits to encode samples from it. It's the bedrock of
> information theory and the reason cross-entropy is the default classification loss, why decision
> trees split on information gain, and how we quantify a model's surprise.

**Why it matters:** entropy is the parent concept behind cross-entropy/KL (the losses) and
information gain (tree splits). Interviewers ask what entropy measures, why a uniform distribution
maximizes it, the units (bits vs nats), and how it connects to coding/compression and to the loss
functions you train with.

## How to work through it

1. **Information intuition** — watch [Khan: Information entropy](https://www.youtube.com/watch?v=2s3aJfRr9gE) (and [Measuring information](https://www.youtube.com/watch?v=PtmzfpV6CDE)). *Why "surprise" and "bits" are the right units.*
2. **For data science** — watch [StatQuest: Entropy (for data science), Clearly Explained](https://www.youtube.com/watch?v=YtebGVx-Fxw). *Entropy as used in trees and ML losses.*
3. **Entropy → cross-entropy → KL** — watch [Aurélien Géron: A Short Introduction to Entropy, Cross-Entropy and KL](https://www.youtube.com/watch?v=ErfnhcEV1O8). *The cleanest single bridge to the loss functions.*
4. **Formalize** — read [MacKay, Information Theory, Inference & Learning Algorithms — Ch. 2 & 4](https://www.inference.org.uk/itprnn/book.pdf). *Entropy, the source-coding theorem, and the units.*
5. **Connect to ML** — read [ai-ml-intuitions 5.01 Information Theory: Entropy & KL](/ai-ml/ai-ml-intuitions/foundational-mental-models/information-and-dependence/entropy-and-kl-divergence-intuition). *Where entropy powers ML objectives.*

## References

- **In this platform**:
  - [Cross-Entropy & KL Divergence](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/cross-entropy-and-kl-divergence/cross-entropy-and-kl-divergence) — builds directly on this page: the training losses entropy is the parent of.
  - [Information Theory: Entropy & KL](/ai-ml/ai-ml-intuitions/foundational-mental-models/information-and-dependence/entropy-and-kl-divergence-intuition) — the intuition, and where entropy powers ML objectives.
  - [Mutual Information](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/mutual-information/mutual-information) — builds directly on this page: entropy applied to dependence.
  - [Random Variables & Distributions](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/random-variables-and-distributions/random-variables-and-distributions) — the prerequisite this page builds on.
- **Videos**:
  - [A Short Introduction to Entropy, Cross-Entropy and KL-Divergence](https://www.youtube.com/watch?v=ErfnhcEV1O8) — **Aurélien Géron** — entropy → cross-entropy → KL in 10 minutes.
  - [Entropy (for data science) Clearly Explained](https://www.youtube.com/watch?v=YtebGVx-Fxw) — **StatQuest (Josh Starmer)** — entropy for ML and decision trees.
  - [Information entropy | Journey into information theory](https://www.youtube.com/watch?v=2s3aJfRr9gE) — **Khan Academy** — entropy as expected surprise.
  - [Measuring information | Journey into information theory](https://www.youtube.com/watch?v=PtmzfpV6CDE) — **Khan Academy** — bits, symbols, and information content.
- **Courses**:
  - [Khan Academy — Journey into Information Theory](https://www.khanacademy.org/computing/computer-science/informationtheory) — **Khan Academy** — entropy and information from first principles, free.
  - [Stanford EE376A — Information Theory (course materials)](https://web.stanford.edu/class/ee376a/) — **Stanford** — the rigorous treatment of entropy and coding; free notes.
- **Articles**:
  - [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) — **Christopher Olah** — the best free visual essay on entropy, cross-entropy, and KL.
- **Papers**:
  - [A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) — **Claude Shannon (1948)** — the paper that defined entropy and founded information theory.
- **Books**:
  - [Elements of Information Theory — **Ch. 2 (Entropy, Relative Entropy & Mutual Information)**](http://www.cs.columbia.edu/~vh/courses/LexicalSemantics/Association/Cover&Thomas-Ch2.pdf) — **Cover & Thomas** — the standard reference's entropy chapter (free PDF).
  - [Information Theory, Inference, and Learning Algorithms — **Ch. 2, 4 (Entropy, Source Coding)**](https://www.inference.org.uk/itprnn/book.pdf) — **David MacKay** — entropy and source coding, in the free classic.
  - [Mathematics for Machine Learning — Ch. 6.5 (Entropy)](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — entropy in the probability chapter.
</content>
