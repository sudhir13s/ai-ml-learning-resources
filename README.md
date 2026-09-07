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

## Structure (one pattern, everywhere)
The tree is the chartered one: **section → sub-area → topic package**, all kebab-case, with
`course.yaml` declaring the sections and a `metadata.yaml` (`page-order:`) fixing the reading
order inside every sub-area. A topic package holds its teaching page, its optional
`*.references.md` companion, and its own `images/`, `code/` and `notebooks/` assets. Every
sub-area keeps a single **`README.md`** — the curated resource index, with YAML frontmatter
(`id`, `topic`, `level`, `built_from`) and sections for Courses / Videos / Papers / Articles /
Books. *This consistent, parseable format lets the library double as a dataset for the
interview-prep project.*

## Sections

### [Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme)
| Sub-area | Level |
| :--- | :--- |
| [AI/ML Orientation](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/readme) | beginner |
| [Programming and Data Foundations](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/readme) | beginner |
| [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) — incl. the [full math curriculum](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maths-for-ai-ml/readme) | beginner |
| [Data Preparation](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/readme) | beginner |
| [AI Paradigms and Knowledge](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/readme) | beginner |
| [Tools and Frameworks](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/readme) | beginner |
| [Research Literacy](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme) | advanced |

### [Core Machine Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/readme)
| Sub-area | Level |
| :--- | :--- |
| [Supervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/readme) | intermediate |
| [Unsupervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/readme) | intermediate |
| [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/readme) | advanced |
| [Model Selection and Evaluation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/readme) — bias-variance, cross-validation, calibration, uncertainty, error analysis | intermediate |

### [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
Neural-network foundations · optimization and training · stabilization and architectural
blocks · neural architectures · attention and transformers · sequence modeling (state-space
models, Mamba, linear and hybrid attention) · self-supervised learning · scientific and
specialized deep learning (graph networks, physics-informed networks, neural operators,
equivariance) · interpretability and analysis (mechanistic interpretability, circuits,
sparse autoencoders, probing).

### [Modalities and Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/readme)
| Sub-area | Level |
| :--- | :--- |
| [Natural Language Processing](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme) | intermediate |
| [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme) | intermediate |
| [Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme) | advanced |
| [Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme) — DDPM to flow matching, DiT, distillation, editing, video, 3D, provenance | advanced |
| [Multimodal Learning](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/readme) — CLIP to native multimodal models, multimodal RAG and evaluation | advanced |
| [Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/readme) | advanced |
| [Audio and Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme) — representations, codecs, ASR, TTS, voice agents | advanced |

### [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
| Sub-area | Level |
| :--- | :--- |
| [Large Language Model Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/readme) | advanced |
| [LLM Model Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/readme) — attention variants, positional bridge, long context, mixture of experts, diffusion language models | advanced |
| [Training and Adaptation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/readme) — SFT, instruction tuning, synthetic data, LoRA, distillation, preference training, RL for reasoning, model merging | advanced |
| [Inference and Runtime](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/readme) — KV cache, decoding, speculative decoding, quantization, batching, caching, on-device models | advanced |
| [Reasoning, Evaluation and Alignment](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/readme) — prompting, chain of thought, test-time computation, hallucination, evaluation, alignment | advanced |
| [RAG and Knowledge Systems](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/overview) | advanced |
| [Agentic AI](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/overview) — the agent loop, tools, memory, context engineering, MCP and A2A, coding and computer-use agents, evaluation, safety and prompt injection | advanced |

### [Deployment and MLOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
| Sub-area | Level |
| :--- | :--- |
| [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/readme) | intermediate |
| [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/readme) — feature stores, pipelines, GPUs and accelerators, distributed training | intermediate |
| [Packaging and Serving](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/readme) | intermediate |
| [Release and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/readme) — CI/CD, canary and shadow, rollback and recovery | intermediate |
| [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/readme) — monitoring, drift, AI incident response | intermediate |
| [Governance and Economics](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/readme) | intermediate |

### [World Models and Embodied Intelligence](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/readme)
World-model foundations · predictive representation models (JEPA) · latent dynamics ·
learning and planning (Dreamer, MuZero, model-predictive control) · spatial and physical
world models (3D scene understanding, intuitive physics, causal world models) · video and
generative world models · memory and cognitive maps · embodied intelligence
(vision-language-action models) · evaluation and safety.

### [Specialized Studies](/ai-ml/ai-ml-learning-resources/specialized-studies/readme)
| Sub-area | Level |
| :--- | :--- |
| [Advanced Mathematics for AI Research](/ai-ml/ai-ml-learning-resources/specialized-studies/advanced-mathematics-for-ai-research/readme) | advanced |
| [Neuroscience and Brain-Inspired AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/readme) | advanced |
| [Neuro-Symbolic and Structured Intelligence](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/readme) | advanced |

### Specializations (deep-dive curricula)
- [Computer Vision math](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme) · [Neuroscience and Brain-Inspired AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/readme) · [Advanced Research Math](/ai-ml/ai-ml-learning-resources/specialized-studies/advanced-mathematics-for-ai-research/readme) — full what/why/resources curricula
- [LLM Systems Engineering curriculum](/ai-ml/ai-ml-learning-resources/meta/llm-systems-curriculum) — 14-chapter inference-stack syllabus (personal study notebook, held in `_meta/` until absorbed into the chartered sections)

## Sibling projects
- [ai-ml-intuitions](/ai-ml/ai-ml-intuitions) — deep concept pages (the *why*)
- [Practitioner Workflows](/ai-ml/practitioner-workflows) — build-it courses (the *how*)
- [AI-ML-problemsets](../AI-ML-problemsets/) — problems, labs and build projects (the *practice*)
- [PyTorch-fundamental-notes](../PyTorch-fundamental-notes/) — PyTorch mechanics
