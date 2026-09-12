# AI-ML Learning Resources

> A **curated library of the best free resources on the internet** for learning AI / ML / DL —
> not a link dump. For each concept, a short shortlist of *the* best courses, videos, papers,
> articles, and books, chosen for **authority and clarity** (top institutions, researchers, and
> the people who explained it best), and **free / open** wherever possible.

## The curation bar
- **Authoritative** — Stanford/MIT/Berkeley/CMU lectures, DeepMind/OpenAI/Anthropic/Meta FAIR primary
  posts, the paper's own authors, 3Blue1Brown, Karpathy, Raschka, Olah, Weng, Alammar, StatQuest…
  the best explainer, not the top search result. Tutorial-tier and clickbait channels never qualify.
- **Free / open** preferred (audit links, free books, open courses); paywalled work is a pointer, never copied.
- **Current** — every page reflects where its subject stands today (2026): reasoning models, hybrid
  attention, agent protocols, flow matching, native multimodality, vision-language-action models.
- **Verified** — every link is fetched before it is written down; YouTube links are checked to be public.
- Every entry says **who made it and why it's the best**.

## What this library is
This is the **model layer** of the AI/ML hub: anything that makes, changes, measures or serves a
model, taught to depth, plus the foundations underneath. Using a model — retrieval, agents,
prompting in an application, application evaluation and operations — is the application layer,
which lives in [Practitioner Workflows](/ai-ml/practitioner-workflows). The test for where a
subject belongs: change the model → here; use the model → there.

## Structure (one pattern, everywhere)
The tree is the chartered one: **section → sub-area → topic package**, all kebab-case, with
`course.yaml` declaring the sections and a `metadata.yaml` (`page-order:`) fixing the reading
order inside every sub-area. In the lifecycle sections (model building, model adaptation,
inference and serving, evaluation) the section *is* the sub-area and topic packages sit directly
under it. A topic package holds its teaching page, its optional `*.references.md` companion, and
its own `images/`, `code/` and `notebooks/` assets. Every section and sub-area keeps a single
**`README.md`** — the curated resource index, with YAML frontmatter (`id`, `topic`, `level`,
`built_from`) and sections for Courses / Videos / Papers / Articles / Books. *This consistent,
parseable format lets the library double as a dataset for the interview-prep project.*

## Sections, in lifecycle order

### [Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme)
| Sub-area | Level |
| :--- | :--- |
| [AI/ML Orientation](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/readme) | beginner |
| [Programming and Data Foundations](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/readme) | beginner |
| [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) — incl. the [full math curriculum](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maths-for-ai-ml/readme) | beginner |
| [AI Paradigms and Knowledge](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/readme) | beginner |
| [Tools and Frameworks](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/readme) | beginner |
| [Research Literacy](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme) | advanced |

### [Classical Machine Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/readme)
| Sub-area | Level |
| :--- | :--- |
| [Supervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/readme) | intermediate |
| [Unsupervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/readme) | intermediate |
| [Model Selection and Evaluation](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/readme) — bias-variance, cross-validation, calibration, uncertainty, error analysis | intermediate |

### [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/reinforcement-learning/readme)
Foundations (Markov decision processes, Bellman equations, dynamic programming, exploration,
bandits, reward shaping) · value-based learning (Monte Carlo, temporal difference, Q-learning,
SARSA, DQN) · policy learning (REINFORCE, actor-critic, TRPO, PPO, continuous control) ·
model-based · offline · multi-agent.

### [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
How a network learns: neural-network foundations · optimization and training · stabilization
and architectural blocks · self-supervised learning · interpretability and analysis (mechanistic
interpretability, circuits, sparse autoencoders, probing).

### [Models and Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/readme)
| Sub-area | Level |
| :--- | :--- |
| [Classic Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/readme) — CNNs, RNN/LSTM/GRU, autoencoders, state-space models, Mamba, linear and hybrid attention | intermediate |
| [Attention and Transformers](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism) — attention, the transformer, positional encoding, FlashAttention | intermediate |
| [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — objectives, decoder-only shape, scaling laws, attention variants, long context, mixture of experts, diffusion language models, prompting and reasoning | advanced |
| [Generative Model Families](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/readme) — [generative models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme) and [diffusion models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme): VAEs to flow matching, DiT, distillation, editing, video, 3D, provenance | advanced |

### [Data and Representation](/ai-ml/ai-ml-learning-resources/data-and-representation/readme)
| Sub-area | Level |
| :--- | :--- |
| [Data Preparation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme) | beginner |
| [Synthetic Data and Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation) | advanced |

### [Model Building](/ai-ml/ai-ml-learning-resources/model-building/readme)
[Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) — corpora, compute, parallelism and the dynamics of a long run ·
[Build a Small Language Model](/ai-ml/ai-ml-learning-resources/model-building/build-a-small-language-model/why-build-a-model-from-scratch) — ten pages, from random weights to a generating 12.2M-parameter transformer.

### [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme)
Supervised fine-tuning · instruction tuning · LoRA and parameter-efficient fine-tuning ·
knowledge distillation · preference and alignment training (RLHF, DPO) · reinforcement-learning
post-training (GRPO, verifiable rewards) · model merging · two end-to-end courses:
[Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/decide-whether-to-fine-tune) (seven pages) and
[Build a Small Chat Model](/ai-ml/ai-ml-learning-resources/model-adaptation/build-a-small-chat-model/from-base-model-to-assistant) (eight pages).

### [Inference and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/readme)
KV cache (five pages) · decoding and sampling · speculative decoding · quantization · inference
optimization (vLLM, paged attention) · continuous batching · caching and cost · small and
on-device models · [packaging and serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/readme).

### [Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/readme)
Model evaluation and benchmarks · hallucination and grounding · alignment and safety evaluation.

### [Operations and Lifecycle](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme)
| Sub-area | Level |
| :--- | :--- |
| [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/readme) | intermediate |
| [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme) — feature stores, pipelines and orchestration | intermediate |
| [Training Infrastructure](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/readme) — GPUs and accelerators, mixed precision, distributed training, checkpointing, cluster scheduling, training cost | advanced |
| [Release and Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/readme) — CI/CD, canary and shadow, rollback and recovery | intermediate |
| [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/readme) — monitoring, drift, AI incident response | intermediate |
| [Governance and Economics](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/readme) | intermediate |

### [Multimodal and Generative Media](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/readme)
| Sub-area | Level |
| :--- | :--- |
| [Natural Language Processing](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/readme) | intermediate |
| [Computer Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme) | intermediate |
| [Multimodal Learning](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/readme) — CLIP to native multimodal models, multimodal RAG and evaluation | advanced |
| [Video Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/readme) | advanced |
| [Audio and Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/readme) — representations, codecs, ASR, TTS, voice agents | advanced |

### [World Models and Embodied AI](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/readme)
World-model foundations · predictive representation models (JEPA) · latent dynamics ·
learning and planning (Dreamer, MuZero, model-predictive control) · spatial and physical
world models (3D scene understanding, intuitive physics, causal world models) · video and
generative world models · memory and cognitive maps · embodied intelligence
(vision-language-action models) · evaluation and safety.

### [Frontier and Specialized](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/readme)
| Sub-area | Level |
| :--- | :--- |
| [Advanced Mathematics for AI Research](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/readme) | advanced |
| [Neuroscience and Brain-Inspired AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuroscience-and-brain-inspired-ai/readme) | advanced |
| [Neuro-Symbolic and Structured Intelligence](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/readme) | advanced |
| [Scientific and Specialized Deep Learning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/readme) — graph networks, physics-informed networks, neural operators, equivariance | advanced |

### [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme) — transitional
The two application-layer sub-areas, held here until they harvest into Practitioner Workflows:
[RAG and Knowledge Systems](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/overview) ·
[Agentic AI](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/overview).

### Specializations (deep-dive curricula)
- [Computer Vision math](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme) · [Neuroscience and Brain-Inspired AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuroscience-and-brain-inspired-ai/readme) · [Advanced Research Math](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/readme) — full what/why/resources curricula
- [LLM Systems Engineering curriculum](/ai-ml/ai-ml-learning-resources/meta/llm-systems-curriculum) — 14-chapter inference-stack syllabus (personal study notebook, held in `_meta/` until absorbed into the chartered sections)

## Sibling projects
- [ai-ml-intuitions](/ai-ml/ai-ml-intuitions) — deep concept pages (the *why*)
- [Practitioner Workflows](/ai-ml/practitioner-workflows) — build-it courses, the application layer (the *how*)
- [AI-ML-problemsets](../AI-ML-problemsets/) — problems, labs and build projects (the *practice*)
- [PyTorch-fundamental-notes](../PyTorch-fundamental-notes/) — PyTorch mechanics
