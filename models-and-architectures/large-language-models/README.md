---
id: "models-and-architectures/large-language-models"
topic: "Large Language Models"
level: advanced
built_from: ["attention-and-transformers", "natural-language-processing", "classic-architectures"]
updated: 2026-09-13
---

# Large Language Models

> The large language model (LLM) as a model family: the training objective, the decoder-only
> shape that objective selected for, the power laws that decide how big and how long, what
> frontier labs changed inside the transformer between 2023 and 2026, and the behaviour a trained
> model shows at inference time — prompting, chains of thought, and spending more compute per
> question. Building one is [Model Building](/ai-ml/ai-ml-learning-resources/model-building/readme);
> changing one is [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme);
> serving one is [Inference and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/readme).

**Start here:** [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/language-modeling-objectives/language-modeling-objectives) — causal versus masked is one mask flag and one choice of scored positions, and getting that straight makes every other page easy.

## Concept index

Each page is a self-contained resource card with a curated `.references.md` companion where one
exists: a plain-words definition, why it matters in 2026, a five-step start-here path, and
verified courses, videos, papers, articles and books.

### What the model is trained to do

1. [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/language-modeling-objectives/language-modeling-objectives) — causal, masked and span-corruption objectives; the chain-rule factorization and perplexity.
2. [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/decoder-only-models/decoder-only-models) — the GPT family shape and why it won: pre-norm blocks, weight tying, causal masking, the modern LLaMA-class recipe.
3. [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws) — Kaplan to Chinchilla: the power-law fits, the roughly 20-tokens-per-parameter result, and why inference cost moves the optimum.

### The attention block, redesigned

4. [Attention Architectures — GQA, MLA, Sliding-Window and Linear](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear) — multi-query and grouped-query attention, multi-head latent attention, local and interleaved windows, linear and hybrid stacks.
5. [Positional Representations in LLMs](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/positional-representations-in-llms/positional-representations-in-llms) — which scheme shipped models chose, and how position interacts with long context and cache variants.
6. [Long-Context Methods](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures) — RoPE scaling (position interpolation, NTK-aware, YaRN), efficient kernels and cache compression as one stack, not one trick.

### Decoupling capacity from compute, and a different generation paradigm

7. [Mixture-of-Experts](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/mixture-of-experts/mixture-of-experts) — routing, load balancing, expert parallelism, and why total parameters stopped predicting inference cost.
8. [Diffusion Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/diffusion-language-models/diffusion-language-models) — masked and continuous denoising over a whole sequence in a handful of parallel passes, and where it beats autoregression.

### Reasoning at inference time

9. [Prompting and In-Context Learning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/prompting-and-in-context-learning/prompting-and-in-context-learning) — what few-shot examples actually do, and where prompting stops and training has to start.
10. [Chain-of-Thought Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) — intermediate steps, self-consistency, least-to-most, tree of thoughts, and the unfaithfulness problem.
11. [Test-Time Computation and Scaling](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/test-time-computation-and-scaling/test-time-computation-and-scaling) — think longer, sample more, or search; inference compute as a tunable axis alongside parameters and tokens.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang and Tatsunori Hashimoto (Stanford)** — you build the tokenizer, the model, the training loop and the inference path yourself; the Architectures and Mixture-of-Experts lectures survey exactly the choices on these pages.
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — builds a decoder-only GPT from backpropagation upward in plain Python; the best hands-on path in existence.
- [Stanford CS324 — Large Language Models](https://stanford-cs324.github.io/winter2022/) — **Stanford (Liang, Hashimoto et al.)** — defines the objective and interprets the scaling fits inside a full LLM curriculum.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; encoder versus decoder versus encoder-decoder with runnable examples, and the attention-implementation vocabulary the model cards use.
- [Mixture of Experts Explained](https://huggingface.co/blog/moe) — **Hugging Face** — course-grade treatment of routing, load balancing, training instabilities and serving.
- [How to Build a Diffusion Language Model](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) — **Kuleshov Group (Cornell)** — a workshop-derived tutorial by the authors of MDLM; the closest thing to a course on text diffusion.

## Videos

- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **Andrej Karpathy** — the one-hour mental model built entirely on next-token prediction; the best single framing talk.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — where pretraining sits in the full pipeline, what each later stage adds, and why intermediate thinking tokens help.
- [Let's build GPT: from scratch, in code](https://www.youtube.com/watch?v=kCc8FmEb1nY) — **Andrej Karpathy** — the decoder block, causal mask and training loop written line by line in PyTorch.
- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — the decoder stack visualized end to end; watch it before any equation.
- [Mixture of Experts (MoE), Visually Explained](https://www.youtube.com/watch?v=0QQlYR1r6pQ) — **Jia-Bin Huang** — the cleanest visual intuition for routers, experts and sparsity.
- [Rotary Positional Embeddings: Combining Absolute and Relative](https://www.youtube.com/watch?v=o29P0Kpobz0) — **Efficient NLP** — the clearest RoPE explainer; start here if rotation-as-position still feels abstract.
- [Tree of Thoughts — Deliberate Problem Solving with LLMs](https://www.youtube.com/watch?v=ut5kp56wW_4) — **Yannic Kilcher** — a paper walkthrough of search over reasoning steps, the branching generalization of chain of thought.

## Key Papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — **Vaswani et al. (2017)** — the original Transformer; the decoder block and causal masking these pages build on.
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — **Brown et al. (2020)** — the canonical decoder-only LM at scale, and the appearance of in-context learning.
- [Training Compute-Optimal Large Language Models (Chinchilla)](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (DeepMind, 2022)** — the compute-optimal correction that reset how everyone allocates a training budget.
- [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) — **Touvron et al. (Meta, 2023)** — RMSNorm plus rotary position embedding (RoPE) plus SwiGLU: the modern decoder recipe, spelled out.
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) — **Ainslie et al. (2023)** — the share-the-key/value middle ground that became the default, plus cheap uptraining from an existing model.
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) — **DeepSeek-AI (2024)** — introduces multi-head latent attention (MLA) and a production MoE stack in one report.
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071) — **Peng et al. (2023)** — frequency-dependent interpolation plus attention-temperature correction; the extension method most open models use.
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) — **Wei et al. (2022)** — the founding result, and the source of the GSM8K numbers everyone quotes.
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Parameters](https://arxiv.org/abs/2408.03314) — **Snell et al. (2024)** — when spending inference compute beats training a bigger model.

## Articles / Blogs (free, no paywall)

- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) — **Sebastian Raschka** — the single best free survey of what recent models actually changed, attention block by attention block.
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI (Quentin Anthony et al.)** — the `C ≈ 6ND` compute arithmetic and full memory accounting behind the scaling page.
- [Rotary Embeddings: A Relative Revolution](https://blog.eleuther.ai/rotary-embeddings/) — **EleutherAI** — the positional scheme every page here assumes, derived carefully.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — **Jay Alammar** — the visual foundation under the decoder block; still the most-linked explainer in the field.
- [Understanding Large Language Models](https://magazine.sebastianraschka.com/p/understanding-large-language-models) — **Sebastian Raschka** — situates causal versus masked objectives across the key papers, with the history of how each was chosen.
- [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) — **OpenAI** — the lab's own statement of long internal chains trained by reinforcement learning, and the test-time-compute paradigm.
- [Diffusion language models](https://sander.ai/2023/01/09/diffusion-language.html) — **Sander Dieleman** — the essay that framed the discreteness problem, with the [2026 continuous follow-up](https://sander.ai/2026/08/24/continuous-dlms.html).

## Books (free, with chapters)

- [*Speech and Language Processing*, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky and Martin** — free draft; the decoder-only architecture and autoregressive decoding in textbook form.
- [*Speech and Language Processing*, 3rd ed. — Ch. 12 "Model Alignment, Prompting and In-Context Learning"](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky and Martin** — free draft; the textbook treatment of the prompting material.
- [*Dive into Deep Learning* — Ch. 11 "Attention Mechanisms and Transformers"](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html) — **Zhang, Lipton, Li and Smola** — free and runnable; the baseline multi-head implementation every variant modifies.
- [*How to Scale Your Model* — "Transformers"](https://jax-ml.github.io/scaling-book/transformers/) — **Google DeepMind (Austin et al.)** — free online; the accounting that turns "which attention variant" into a memory-bandwidth number.
- [*Reinforcement Learning from Human Feedback* — "Reasoning and Inference-Time Scaling"](https://rlhfbook.com/c/14-reasoning.html) — **Nathan Lambert** — free online; ties inference-time scaling back to the training recipe that produced it.

## In this platform

- Section index: [Models and Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/readme) · Sibling sub-areas: [Classic Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/readme) · [Attention and Transformers](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/readme) · [Generative Model Families](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/readme)
- The mechanisms these variants modify: [Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism) · [Positional Encoding](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/positional-encoding/positional-encoding) · [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/efficient-attention/efficient-attention)
- The non-attention branch, in full: [Selective State-Space Models — Mamba and Mamba-2](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/selective-state-space-models-mamba/selective-state-space-models-mamba) · [Linear and Hybrid Attention Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/linear-and-hybrid-attention-architectures/linear-and-hybrid-attention-architectures)
- The lifecycle around the model: [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) · [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme) · [Inference and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/readme) · [Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/readme)
- Where reasoning is trained rather than prompted: [Reinforcement Learning Post-Training — GRPO and Verifiable Rewards](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining)
- The mental models: [Neural Scaling Laws and Chinchilla](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/scaling-behavior/neural-scaling-laws-and-chinchilla-intuition) · [Multi-Head Attention](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/multi-head-attention-intuition) · [Mixture-of-Experts Routing](/ai-ml/ai-ml-intuitions/architectural-mechanisms/attention-and-routing/mixture-of-experts-routing-intuition) · [In-Context Learning and Prompting](/ai-ml/ai-ml-intuitions/reasoning-and-agency/in-context-behavior/in-context-learning-and-prompting-intuition) · [Test-Time Computation](/ai-ml/ai-ml-intuitions/reasoning-and-agency/reasoning/test-time-computation-intuition)
- Doing it rather than reading it: [Prompt Engineering workflow](/ai-ml/practitioner-workflows/workflow-library/llm-application-workflows/prompt-engineering)
