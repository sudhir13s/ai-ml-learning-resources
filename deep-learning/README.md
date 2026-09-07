---
id: "05-deep-learning"
topic: "Deep Learning"
level: intermediate
built_from: ["linear-algebra", "calculus", "python", "machine-learning-basics"]
updated: 2026-09-07
---

# Deep Learning
> Neural networks that learn hierarchical representations from data — the engine behind modern
> vision, language, and generative AI. This is the curated shortlist of the *best free* resources;
> for the math intuition behind each idea, see the platform links at the bottom.

**Start here:** [Neural Networks — 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) for intuition, then [Neural Networks: Zero to Hero — Karpathy](https://karpathy.ai/zero-to-hero.html) to build one from scratch.

## Concept Index
Every chapter is a self-contained folder (`<topic>/<topic>.md`) with its page and a curated
`.references.md` resource card (free, open courses · videos · papers · articles · books · cross-links).
> New to deep learning? Start with the field overview below, then work top to bottom.

### Foundations of neural nets
1. [Perceptron & MLP (Feedforward Networks)](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/perceptron-and-mlp/perceptron-and-mlp)
2. [Backpropagation & Computational Graphs](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/backpropagation-and-computational-graphs/backpropagation-and-computational-graphs)
3. [Activation Functions (ReLU · GELU · sigmoid · tanh · softmax)](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/activation-functions/activation-functions)
4. [Loss Functions (MSE · cross-entropy)](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/loss-functions/loss-functions)
5. [Weight Initialization (Xavier/Glorot · He)](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/weight-initialization/weight-initialization)
6. [Vanishing / Exploding Gradients & Gradient Clipping](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/vanishing-exploding-gradients/vanishing-exploding-gradients)

### Training & optimization
7. [Optimizers (SGD · Momentum · Adam · AdamW · RMSprop)](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers)
8. [Learning-Rate Schedules & Warmup](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/learning-rate-schedules-and-warmup/learning-rate-schedules-and-warmup)
9. [Regularization (L1/L2 · weight decay · early stopping)](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/regularization/regularization)
10. [Dropout](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/dropout/dropout)
11. [Normalization (Batch · Layer · Group)](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/normalization/normalization)
12. [Hyperparameter Tuning](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/hyperparameter-tuning/hyperparameter-tuning)

### Architectures
13. [CNNs & Convolution](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/cnns-and-convolution/cnns-and-convolution)
14. [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru)
15. [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism)
16. [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture)
17. [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding)
18. [Residual / Skip Connections](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/residual-skip-connections/residual-skip-connections)
19. [Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/autoencoders/autoencoders)
20. [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention)
21. [Gating Mechanisms](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/gating-mechanisms/gating-mechanisms)

### Sequence modeling (recurrence, convolution, attention, state space)
22. [Sequence Models — Recurrent, Convolutional, Transformer, State-Space](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/sequence-models-recurrent-convolutional-transformer/sequence-models-recurrent-convolutional-transformer)
23. [State-Space Models — Foundations](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/state-space-models-foundations/state-space-models-foundations)
24. [Structured State-Space Models — S4, S4D, Diagonal SSMs](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/structured-state-space-models-s4/structured-state-space-models-s4)
25. [Selective State-Space Models — Mamba and Mamba-2](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/selective-state-space-models-mamba/selective-state-space-models-mamba)
26. [Linear and Hybrid Attention Architectures](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/linear-and-hybrid-attention-architectures/linear-and-hybrid-attention-architectures)

### Self-supervised learning
27. [Contrastive Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning)
28. [Masked Modeling — MAE and BERT-Style Pretraining](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/masked-modeling-mae-and-bert-style-pretraining/masked-modeling-mae-and-bert-style-pretraining)
29. [Teacher-Student Self-Distillation — BYOL, DINO, DINOv3](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/teacher-student-self-distillation-dino-byol/teacher-student-self-distillation-dino-byol)

### Scientific and specialized deep learning
30. [Graph Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks)
31. [Physics-Informed Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/physics-informed-neural-networks/physics-informed-neural-networks)
32. [Neural Operators](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/neural-operators/neural-operators)
33. [Equivariant and Geometric Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/equivariant-and-geometric-deep-learning/equivariant-and-geometric-deep-learning)

### Interpretability and analysis
34. [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability)
35. [Transformer Circuits, Induction Heads and Attention Patterns](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns/transformer-circuits-induction-heads-and-attention-patterns)
36. [Superposition and Sparse Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders/superposition-and-sparse-autoencoders)
37. [Probing, Attribution and Feature Visualization](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization/probing-attribution-and-feature-visualization)
38. [Interpretability for Vision and Classic Models](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/interpretability-for-vision-and-classic-models/interpretability-for-vision-and-classic-models)

### Sub-area indexes
- [Sequence Modeling](/ai-ml/ai-ml-learning-resources/deep-learning/sequence-modeling/readme) · [Scientific and Specialized Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/readme) · [Interpretability and Analysis](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/readme)

### Related concepts (canonical home is another section)
> These topics are used across many areas, so they're kept in one place to avoid repetition.
- **Word / sentence embeddings** — Word2Vec · GloVe · contextual embeddings → [NLP](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme)
- **Vision architectures in depth** — ResNet/Inception, detection, segmentation → [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme)
- **Pretraining & LLM-scale models** — BERT · GPT · scaling laws · RLHF → [LLMs](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- **Pure math** — PCA/SVD · probability · optimization theory → [Foundations · Maths for AI-ML](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)

## Courses (free)
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — builds backprop → GPT from scratch in plain Python; the best hands-on course in existence.
- [Practical Deep Learning for Coders](https://course.fast.ai/) — **fast.ai (Jeremy Howard)** — top-down, code-first, get models working fast; the best "learn by doing" path.
- [MIT 6.S191: Intro to Deep Learning](https://introtodeeplearning.com/) — **MIT (Amini et al.)** — concise, current, free lectures + labs (refreshed yearly).
- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar where sequence-model and interpretability authors present their own work.

## Videos / Lectures
- [Neural Networks series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — **3Blue1Brown** — the definitive visual intuition for what a network *is* and how backprop works.
- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — the attention chapter of the same series.
- [The Dark Matter of AI (Mechanistic Interpretability)](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — the best visual introduction to what is actually inside a trained network.

## Key Papers
- [Deep Learning](https://www.nature.com/articles/nature14539) — **LeCun, Bengio & Hinton (Nature, 2015)** — the field's authoritative review by its founders.
- [Deep Residual Learning (ResNet)](https://arxiv.org/abs/1512.03385) — **He et al. (2015)** — the idea that made networks *deep*; one of the most-cited papers in ML.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — **Vaswani et al. (2017)** — the architecture the last two sections of this index revolve around.
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — **Gu & Dao (2023)** — the non-attention alternative that became competitive at scale.

## Articles / Blogs
- [colah.github.io](https://colah.github.io/) — **Chris Olah** — the gold standard for explaining backprop, LSTMs, and representations visually.
- [Distill.pub](https://distill.pub/) — **Distill** — interactive, peer-reviewed deep-learning explainers (archival but timeless).
- [Transformer Circuits Thread](https://transformer-circuits.pub/) — **Anthropic interpretability team** — where the modern mechanistic results are published first.

## Books (free)
- [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) — **Zhang, Lipton, Li & Smola** — free, interactive, runnable code in PyTorch/JAX; the best modern textbook.
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) — **Michael Nielsen** — free, the clearest from-first-principles introduction.
- [Deep Learning](https://www.deeplearningbook.org/) — **Goodfellow, Bengio & Courville** — free online; the rigorous reference text.

## In this platform
- **Understand the math:** [ai-ml-intuitions — Learning & Optimization](/ai-ml/ai-ml-intuitions/learning-and-optimization) · [Training Stability](/ai-ml/ai-ml-intuitions/training-stability)
- **Build it:** [AI-ML problemsets](/ai-ml/ai-ml-problemsets)
- **Prereq math:** [Maths for AI-ML curriculum](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maths-for-ai-ml/readme)
