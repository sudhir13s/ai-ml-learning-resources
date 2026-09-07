---
id: "modalities-and-generative-models"
topic: "Modalities and Generative Models"
level: advanced
built_from: ["deep-learning", "core-machine-learning"]
updated: 2026-09-07
---

# Modalities and Generative Models

> What happens when the same architectural ideas meet different kinds of data — text, images,
> video, audio — and when the goal changes from predicting a label to producing a sample. Seven
> sub-areas: the two classical modalities, the generative families that culminated in diffusion,
> and the three areas where modalities meet. Text *generation* lives in
> [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme); this section owns everything else.

**Start here:** [Natural Language Processing](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme) or [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme) depending on your modality, then [Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme) — it is the deepest sub-area here and the one the generative frontier runs through.

## Sub-areas

Each sub-area has its own curated index; each page inside is a resource card with a definition,
a five-step start-here path, and verified courses, videos, papers, articles and books.

### The classical modalities

1. [Natural Language Processing](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme) — **18 pages** — tokenization, word and sentence embeddings, sequence labelling, machine translation, retrieval and the transformer-era NLP task set.
2. [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme) — **16 pages** — images as signals, convolution and frequency thinking, projective geometry, convolutional and vision-transformer backbones, detection, segmentation and depth.

### Generation

3. [Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme) — **7 pages** — the family map: autoregressive, variational autoencoders and the evidence lower bound, generative adversarial networks, normalizing flows, energy-based models.
4. [Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme) — **17 pages** — forward and reverse processes, the score-based view, latent diffusion, samplers and guidance, diffusion transformers, flow matching, few-step distillation, control and editing, serving and provenance.

### Where modalities meet

5. [Multimodal Learning](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/readme) — **10 pages** — contrastive image-text pretraining, fusion architectures, vision-language models and any-to-any systems.
6. [Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/readme) — **8 pages** — temporal representation, action recognition, video-language reasoning, and making hour-long video tractable.
7. [Audio and Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme) — **10 pages** — audio representations and neural codecs, automatic speech recognition (ASR), text-to-speech (TTS), and the realtime voice stack.

## Courses (free)

- [Stanford CS224N — Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Christopher Manning)** — the standard NLP course; lectures, slides and assignments free.
- [Stanford CS231n — Deep Learning for Computer Vision](https://cs231n.github.io/) — **Stanford** — the standard vision course; the notes alone are one of the best free texts in the field.
- [Stanford CS236 — Deep Generative Models](https://deepgenerativemodels.github.io/) — **Stefano Ermon (Stanford)** — the score-based and diffusion lectures, from the group that co-invented score matching.
- [MIT 6.S184: Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) — **Peter Holderrieth and Ezra Erives (MIT)** — the current objective behind most new generative systems, taught from first principles.
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — free and code-first; conditioning, guidance and fine-tuning with runnable notebooks.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — the university treatment of speech, from phonetics to end-to-end models.

## Videos

- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — the architecture the text and multimodal sub-areas both assume, visualized.
- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Justin Johnson (Michigan Online)** — the clearest free lecture on video classification and the baselines that keep winning.
- [Variational Autoencoders and Diffusion Models](https://www.youtube.com/watch?v=pea3sH6orMc) — **Tim Salimans (Google DeepMind)** — a researcher who built progressive distillation explaining why few-step sampling works.
- [Stanford CS25 V4: From Large Language Models to Large Multimodal Models](https://www.youtube.com/watch?v=cYfKQ6YG9Qo) — **Stanford Online** — the road from CLIP to modern multimodal systems, told by people who built stops along it.
- [ML for Audio Study Group — Intro to Audio and ASR Deep Dive](https://www.youtube.com/watch?v=D-MH6YjuIlE) — **Hugging Face** — the engineering view of speech: data, features, models and evaluation in one sitting.

## Key Papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — **Vaswani et al. (2017)** — the architecture every sub-area in this section now runs on, introduced for translation.
- [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) — **Devlin et al. (2018)** — masked language modelling and the pretrain-then-fine-tune paradigm that reorganized NLP.
- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) — **He et al. (2015)** — skip connections; the idea that made vision networks deep, and one of the most-cited papers in science.
- [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598) — **Ho and Salimans (2022)** — one model, condition dropout and extrapolation at sampling time; the knob every image model exposes.
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) — **Alayrac et al. (DeepMind, 2022)** — gated cross-attention into a frozen language model; the fusion design most VLMs still echo.
- [BLIP-2: Bootstrapping Language-Image Pre-training](https://arxiv.org/abs/2301.12597) — **Li et al. (2023)** — the query-transformer bottleneck between two frozen towers, and why it is cheap.

## Articles / Blogs (free, no paywall)

- [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — **Lilian Weng** — the canonical open math walkthrough from forward process to the training loss.
- [Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/) — **Yang Song** — the score-based view of diffusion from its originator; the natural second read.
- [Learning the integral of a diffusion model](https://sander.ai/2026/05/06/flow-maps.html) — **Sander Dieleman** — the unifying flow-map perspective on diffusion, flow matching and few-step generation.
- [Generalized Visual Language Models](https://lilianweng.github.io/posts/2022-06-09-vlm/) — **Lilian Weng** — the canonical map of how vision meets language models, with CLIP at the root.
- [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — the current open-model landscape, including which models actually read documents well.

## Books (free, with chapters)

- [*Speech and Language Processing*, 3rd ed.](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky and Martin** — free draft; the standard text for NLP and, in Ch. 16, for speech.
- [*Computer Vision: Algorithms and Applications*, 2nd ed.](https://szeliski.org/Book/) — **Richard Szeliski** — free online; the geometric-vision backbone under everything in sub-area 2.
- [*Understanding Deep Learning* — Ch. 18 "Diffusion models"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the clearest careful derivation of the denoising objective.
- [*Probabilistic Machine Learning: Advanced Topics* — Ch. 25 "Diffusion models"](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; the rigorous modern treatment.
- [*Foundations of Computer Vision*](https://visionbook.mit.edu) — **Torralba, Isola and Freeman** — free online; the MIT text, strong on representation and recognition.
- [*Dive into Deep Learning* — Ch. 14 "Computer Vision"](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang, Lipton, Li and Smola** — free and runnable; the backbone implementations with working code.

## In this platform

- Before this section: [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) — the architectures every sub-area here specializes.
- After this section: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme) · [World Models and Embodied Intelligence](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/readme) · [MLOps and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
- Where text generation is taught instead: [Large Language Model Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/readme) · [Diffusion Language Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/diffusion-language-models/diffusion-language-models)
- Where these representations get used: [Embedding Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models) · [Vision-Language-Action Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/embodied-intelligence/vision-language-action-models/vision-language-action-models)
- The mental models: [Convolution](/ai-ml/ai-ml-intuitions/architectural-mechanisms/locality-and-weight-sharing/convolution-intuition) · [Diffusion Forward and Reverse Process](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition) · [Latent Variable Models and the ELBO](/ai-ml/ai-ml-intuitions/generation/latent-variable-generation/latent-variable-models-and-elbo-intuition) · [Contrastive Learning](/ai-ml/ai-ml-intuitions/representation/representation-learning/contrastive-learning-intuition) · [Multimodal LLMs](/ai-ml/ai-ml-intuitions/multimodal-integration/modality-fusion/multimodal-llms-intuition)
- Doing it rather than reading it: [Multimodal Pipelines workflow](/ai-ml/practitioner-workflows/workflow-library/llm-application-workflows/multimodal-pipelines) · [Embeddings and Vector Search workflow](/ai-ml/practitioner-workflows/workflow-library/data-and-inputs/embeddings-and-vector-search)
