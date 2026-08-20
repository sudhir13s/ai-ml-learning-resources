# 🌐 AI-ML Learning Resources

> A **curated library of the best free resources on the internet** for learning AI / ML / DL —
> not a link dump. For each topic, a short shortlist of *the* best courses, videos, papers,
> articles, and books, chosen for **authority and clarity** (top institutions, researchers, and
> the people who explained it best), and **free / open** wherever possible.

## The curation bar
- **Authoritative** — Stanford/MIT/DeepMind/Anthropic, seminal-paper authors, 3Blue1Brown, Karpathy, Olah, StatQuest… the best explainer, not the top SEO result.
- **Free / open** preferred (audit links, free books, open courses).
- **~2 per type** — a couple of courses, videos, papers, articles, books. Curated, not exhaustive.
- Every entry says **who made it and why it's the best**.

## Structure (one pattern, everywhere)
The tree is the chartered one: **section → sub-area → topic package**, all kebab-case, with
`course.yaml` declaring the sections and a `metadata.yaml` (`page-order:`) fixing the reading
order inside every sub-area. A topic package holds its teaching page, its
`*.references.md` companion, and its own `images/`, `code/` and `notebooks/` assets. Sub-areas
keep a single **`README.md`** — the curated resource index, with YAML frontmatter
(`id`, `topic`, `level`, `prereqs`) and sections for Courses / Videos / Papers / Articles /
Books. *This consistent, parseable format lets the library double as a dataset for the
interview-prep project.*

## 🗺️ Sections

### [Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme)
| Sub-area | Level |
| :--- | :--- |
| [AI/ML Orientation](/ai-ml/ai-ml-learning-resources/foundations/readme) | beginner |
| [Programming and Data Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme) | beginner |
| [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) — incl. the [full math curriculum](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maths-for-ai-ml/readme) | beginner |
| [Data Preparation](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/readme) | beginner |
| [Tools and Frameworks](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/readme) | beginner |
| [Research Literacy](/ai-ml/ai-ml-learning-resources/foundations/research-literacy/readme) | advanced |

### Core Machine Learning
| Sub-area | Level |
| :--- | :--- |
| [Supervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/readme) | intermediate |
| [Unsupervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/readme) | intermediate |
| [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/readme) | advanced |
| Model Selection and Evaluation | intermediate |

### [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
Neural-network foundations · optimization and training · stabilization and architectural
blocks · neural architectures · attention and transformers · self-supervised learning.

### Modalities and Generative Models
| Sub-area | Level |
| :--- | :--- |
| [Natural Language Processing](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme) | intermediate |
| [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme) | intermediate |
| [Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme) | advanced |
| [Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme) | advanced |
| [Multimodal Learning](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/readme) | advanced |
| [Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/readme) | advanced |
| [Audio and Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme) | advanced |

### LLMs, Applications and Agents
| Sub-area | Level |
| :--- | :--- |
| [RAG and Knowledge Systems](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/overview) | advanced |
| [Agentic AI](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/overview) | advanced |
| [Large Language Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme) — still on its legacy folder name; re-homed by the LLM wave | advanced |

### [Deployment and MLOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
Lifecycle and reproducibility · data and training platforms · packaging and serving ·
release and deployment · monitoring and reliability · governance and economics.

### Specialized Studies
| Sub-area | Level |
| :--- | :--- |
| [Advanced Mathematics for AI Research](/ai-ml/ai-ml-learning-resources/specialized-studies/advanced-mathematics-for-ai-research/readme) | advanced |
| [Neuroscience and Brain-Inspired AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/readme) | advanced |

### Specializations (deep-dive curricula)
- [Computer Vision math](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme) · [Neuroscience & Brain-Inspired AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/readme) · [Advanced Research Math](/ai-ml/ai-ml-learning-resources/specialized-studies/advanced-mathematics-for-ai-research/readme) — full what/why/resources curricula
- [LLM Systems Engineering curriculum](/ai-ml/ai-ml-learning-resources/meta/llm-systems-curriculum) — 14-chapter inference-stack syllabus (personal study notebook, held in `_meta/` until absorbed into the chartered sections)

## 🔗 Sibling projects
- [ai-ml-intuitions](../ai-ml-intuitions/) — deep concept pages (the *why*)
- [AI-ML-problemsets](../AI-ML-problemsets/) — problems, labs & build projects (the *practice*)
- [PyTorch-fundamental-notes](../PyTorch-fundamental-notes/) — PyTorch mechanics
