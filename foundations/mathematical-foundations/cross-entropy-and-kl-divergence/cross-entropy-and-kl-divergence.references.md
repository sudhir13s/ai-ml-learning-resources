---
id: "01-foundations/cross-entropy-and-kl-divergence/references"
topic: "Cross-Entropy & KL Divergence — References"
parent: "01-foundations/cross-entropy-and-kl-divergence"
type: references
updated: 2026-09-07
---

# Cross-Entropy & KL Divergence — References

> Companion link library for **[Cross-Entropy & KL Divergence](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/cross-entropy-and-kl-divergence/cross-entropy-and-kl-divergence)**
> (the concept page). Kept separate so it can be reused as a standalone reference list. Grouped by
> type, alphabetical within each group. Everything here is **free / open** — no paywall. Every source cited under a
> "Source / derivation" line on the concept page appears here, so each formula is traceable to a
> primary source. Chosen for depth on *this* topic, not popularity.

- **In this platform**:
  - [Categorical Cross-Entropy / NLL](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/training-objectives/categorical-cross-entropy-intuition) — the classification and language-model loss, in depth.
  - [Cross-Entropy & KL Divergence](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/cross-entropy-and-kl-divergence/cross-entropy-and-kl-divergence) — the concept page this list accompanies.
  - [Entropy](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/entropy/entropy) — the prerequisite: the why behind bits and surprise.
  - [Entropy & KL](/ai-ml/ai-ml-intuitions/foundational-mental-models/information-and-dependence/entropy-and-kl-divergence-intuition) — the intuition, applied downstream.
  - [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — where the KL penalty in reinforcement learning from human feedback is used.
  - [Maximum Likelihood Estimation](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maximum-likelihood-estimation/maximum-likelihood-estimation) — the unifying theorem it rests on: minimising cross-entropy is maximum likelihood.
  - [Mutual Information](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/mutual-information/mutual-information) — where it goes next: $I(X;Y) = D_{KL}(\text{joint}\,\|\,\text{product of marginals})$, KL applied to dependence.
- **Videos**:
  - [A Short Introduction to Entropy, Cross-Entropy and KL-Divergence](https://www.youtube.com/watch?v=ErfnhcEV1O8) — **Aurélien Géron** — all three concepts and their relationships, the cleanest single bridge.
  - [Entropy (for data science) Clearly Explained](https://www.youtube.com/watch?v=YtebGVx-Fxw) — **StatQuest (Josh Starmer)** — the entropy / surprise baseline that KL is measured against.
  - [Intuitively Understanding the KL Divergence](https://www.youtube.com/watch?v=SxGYPqCgJWM) — **Adian Liusie** — the meaning and asymmetry of KL, forward vs reverse.
  - [KL Divergence — how to tell how different two distributions are](https://www.youtube.com/watch?v=sjgZxuCm_8Q) — **Luis Serrano Academy** — KL built from first principles on small worked examples, with the asymmetry made concrete.
  - [Neural Networks Part 6: Cross Entropy](https://www.youtube.com/watch?v=6ArSys5qHAU) — **StatQuest (Josh Starmer)** — cross-entropy as a training loss, step by step.
  - [Solving Wordle using information theory](https://www.youtube.com/watch?v=v68zYyaEmEA) — **3Blue1Brown** — builds Shannon entropy and information-as-bits from first principles (expected surprise = code length) — the exact intuition this page opens with.
- **Courses**:
  - [Khan Academy — Journey into Information Theory](https://www.khanacademy.org/computing/computer-science/informationtheory) — **Khan Academy** — the entropy / bits / surprise foundations cross-entropy and KL build on.
  - [MIT 6.050J — Information & Entropy](https://ocw.mit.edu/courses/6-050j-information-and-entropy-spring-2008/) — **MIT OCW** — a full free course on entropy, coding, and information from first principles.
  - [Stanford CS231n — Linear Classification (Softmax & cross-entropy loss)](https://cs231n.github.io/linear-classify/) — **Stanford** — cross-entropy derived as *the* classification loss, with the softmax gradient.
- **Articles**:
  - [KL Divergence: Forward vs Reverse?](https://agustinus.kristia.de/blog/forward-reverse-kl/) — **Agustinus Kristiadi** — mode-covering versus mode-seeking made precise, with the fitted-Gaussian pictures this chapter's Demo 2 mirrors.
  - [Kullback-Leibler Divergence Explained](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) — **Will Kurt (Count Bayesie)** — an intuitive, free walkthrough from information loss to VAEs.
  - [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) — **Christopher Olah** — the definitive free visual treatment of cross-entropy and KL as code lengths; the intuition this chapter rests on.
- **Papers**:
  - [A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) — **Shannon (1948), *Bell System Technical Journal*** — the source-coding theorem: entropy is the optimal average code length, the foundation of the "bits / surprise" reading.
  - [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — **Hinton, Vinyals & Dean (2015)** — knowledge distillation as minimising KL to a teacher's soft labels (a "where it's used" reference).
  - [On Information and Sufficiency](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-1/On-Information-and-Sufficiency/10.1214/aoms/1177729694.full) — **Kullback & Leibler (1951), *Annals of Mathematical Statistics*** — the original definition of relative entropy (KL divergence); open access on Project Euclid.
  - [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155) — **Ouyang et al. (2022)** — the reinforcement-learning-from-human-feedback objective with its KL penalty $\beta D_{KL}(\pi_\theta\|\pi_{\text{ref}})$; where the KL "leash" of the crux section lives.
- **Documentation**:
  - [Log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss) — **scikit-learn docs** — the same quantity as an evaluation metric, with the clipping and base conventions spelled out.
  - [`torch.nn.CrossEntropyLoss`](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) — **PyTorch team** — the classifier-loss view in code: why it expects logits, folds in `log_softmax`, and equals negative log-likelihood.
- **Books**:
  - [Deep Learning — Ch. 3.13 (Information Theory) & Ch. 6.2 (softmax + cross-entropy)](https://www.deeplearningbook.org/) — **Goodfellow, Bengio & Courville** — the cross-entropy classification loss and the softmax gradient $\hat q - y$; free online.
  - [Elements of Information Theory — Ch. 2 "Entropy, Relative Entropy, and Mutual Information"](http://staff.ustc.edu.cn/~cgong821/Wiley.Interscience.Elements.of.Information.Theory.Jul.2006.eBook-DDU.pdf) — **Cover & Thomas** — the standard reference; the definitions of entropy, cross-entropy, and KL used in the derivation (free chapter PDF).
  - [Information Theory, Inference, and Learning Algorithms — Ch. 2 (Relative Entropy) & Ch. 4](https://www.inference.org.uk/itprnn/book.pdf) — **David MacKay** — KL, cross-entropy, Gibbs' inequality, and the source-coding theorem, in the free classic (full PDF on the author's site).
  - [Mathematics for Machine Learning — Ch. 8 (esp. 8.3 MLE / cross-entropy)](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — derives minimising cross-entropy / KL to the empirical distribution = maximum likelihood. Free full PDF.
