---
id: "06-nlp/contextual-embeddings/references"
topic: "Contextual Embeddings — References"
parent: "06-nlp/contextual-embeddings"
type: references
updated: 2026-09-07
---

# Contextual Embeddings — references

> Companion link library for **[Contextual Embeddings (ELMo · BERT)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/contextual-embeddings-elmo-bert/contextual-embeddings-elmo-bert)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Build intuition** — read [The Illustrated BERT, ELMo & co.](https://jalammar.github.io/illustrated-bert/) (**Jay Alammar**). *The clearest visual story of how contextual representations work — the one explainer to read first.*
2. **Watch it explained** — [BERT Neural Network — EXPLAINED!](https://www.youtube.com/watch?v=xI0HHN5XKDo) (**CodeEmporium**), then [CMU Neural Nets for NLP 2021 (9): Sentence and Contextual Word Representations](https://www.youtube.com/watch?v=0UNNRxhnjHg) (**Graham Neubig**). *A short take on masked-LM and bidirectionality, then the lecture that places ELMo and BERT in one lineage.*
3. **Place it in history** — [NLP's ImageNet Moment Has Arrived](https://www.ruder.io/nlp-imagenet/) (**Sebastian Ruder**). *Why pretrained contextual models reset the whole field.*
4. **Read the sources** — [ELMo](https://arxiv.org/abs/1802.05365) → [BERT](https://arxiv.org/abs/1810.04805). *Deep contextualized representations, then masked-LM deep bidirectionality.*
5. **Make it concrete** — [BERT Word Embeddings Tutorial](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/) (**Chris McCormick**). *Extract real contextual vectors and inspect them, layer by layer — mirrors this page's code.*

**In this platform**:
- Concept depth (the *why* behind dense vectors): [ai-ml-intuitions 1.02 Dense Embeddings](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/dense-embeddings-intuition)
- Concept page (full explanation): [Contextual Embeddings (ELMo · BERT)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/contextual-embeddings-elmo-bert/contextual-embeddings-elmo-bert)
- The decoder lineage: [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) (why encoders don't need one) · the [LLMs concept index](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme)
- Builds on this: [Sentence & Document Embeddings (Sentence-BERT · USE)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/sentence-and-document-embeddings/sentence-and-document-embeddings) — the naive-`[CLS]` trap and its fix.
- Runnable code: [step-by-step teaching notebook](code/contextual-embeddings-elmo-bert.ipynb) · [source-of-truth module](code/contextual_embeddings.py) · [figure generator](code/make_figures_06.py) — the same functions produce the page's numbers, the notebook, and every figure.
- Foundations: [Tokenization & Subword Algorithms](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms) · [Transformer Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/transformer-architecture/transformer-architecture) · [Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism)
- The static limitation it fixes: [Word Embeddings (word2vec · GloVe · fastText)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/word-embeddings-word2vec-glove-fasttext/word-embeddings-word2vec-glove-fasttext)

**Videos**:
- [BERT explained: training, inference, BERT vs GPT, fine-tuning, [CLS]](https://www.youtube.com/watch?v=90mGPxR2GgY) — **Umar Jamil** — a deep, careful walkthrough of exactly the topics on this page (MLM, [CLS], BERT vs GPT, fine-tuning).
- [BERT Explained!](https://www.youtube.com/watch?v=OR0wfP2FD3c) — **Connor Shorten** — walks through the paper's key ideas.
- [BERT Neural Network — EXPLAINED!](https://www.youtube.com/watch?v=xI0HHN5XKDo) — **CodeEmporium** — clear intuition for masked-LM and why bidirectional context matters.
- [BERT: Pre-training of Deep Bidirectional Transformers (paper walkthrough)](https://www.youtube.com/watch?v=-9evrZnBorM) — **Yannic Kilcher** — a section-by-section read of the original BERT paper.
- [CMU Neural Nets for NLP 2021 (9): Sentence and Contextual Word Representations](https://www.youtube.com/watch?v=0UNNRxhnjHg) — **Graham Neubig (CMU)** — ELMo, BERT, and the contextual-representation family taught as one line of work rather than three separate models.
- [Transformer Models and BERT Model: Overview](https://www.youtube.com/watch?v=hsp1OAcoLBY) — **Google Cloud** — concise official overview tying transformers to BERT.

**Courses**:
- [Hugging Face LLM Course — Ch. 1: Transformer Models](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — how pretrained encoders produce and use contextual representations, code-first.
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Manning)** — the contextual-representations + pretraining lectures (ELMo → BERT), the canonical academic treatment.

**Interactive**:
- [A Visual Notebook to Using BERT for the First Time (Colab)](https://colab.research.google.com/github/jalammar/jalammar.github.io/blob/master/notebooks/bert/A_Visual_Notebook_to_Using_BERT_for_the_First_Time.ipynb) — **Jay Alammar** — a runnable, click-through notebook that loads BERT and extracts contextual features step by step.
- [BertViz — visualize attention in BERT](https://github.com/jessevig/bertviz) — **Jesse Vig** — an interactive notebook tool to *see* which tokens each head attends to, layer by layer; the most direct way to watch bidirectional attention build context.

**Articles**:
- [BERT 101 — State Of The Art NLP Model Explained](https://huggingface.co/blog/bert-101) — **Hugging Face** — a clean, modern walkthrough of BERT, MLM/NSP, and how to use it.
- [BERT Word Embeddings Tutorial](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/) — **Chris McCormick** — hands-on extraction of contextual vectors, which layers to pool, subword handling (blog + Colab).
- [Finally, a Replacement for BERT (ModernBERT)](https://huggingface.co/blog/modernbert) — **Hugging Face** — the authors' own write-up of what changed and what it costs, with benchmark tables; the practical answer to "should I still fine-tune BERT in 2026?".
- [NLP's ImageNet Moment Has Arrived](https://www.ruder.io/nlp-imagenet/) — **Sebastian Ruder** — the historical context for why pretrained contextual models took over.
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — **Harvard NLP** — the encoder internals (self-attention, FFN, layer-norm) behind BERT, implemented line by line.
- [The Illustrated BERT, ELMo & co.](https://jalammar.github.io/illustrated-bert/) — **Jay Alammar** — the definitive visual explainer of contextual embeddings, ELMo, and BERT.

**Papers**:
- [ALBERT: A Lite BERT for Self-supervised Learning](https://arxiv.org/abs/1909.11942) — **Lan et al. (2019)** — cross-layer parameter sharing, factorized embeddings, and SOP in place of NSP.
- [BERT Rediscovers the Classical NLP Pipeline](https://arxiv.org/abs/1905.05950) — **Tenney et al. (2019)** — layer probing: BERT learns POS→syntax→semantics bottom-to-top.
- [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) — **Devlin et al. (2018)** — masked-LM + NSP; the deep-bidirectional encoder and the pretrain→fine-tune paradigm shift.
- [DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) — **He et al. (2020)** — disentangled content/position attention; topped many encoder leaderboards.
- [Deep Contextualized Word Representations (ELMo)](https://arxiv.org/abs/1802.05365) — **Peters et al. (2018)** — contextual vectors from a deep biLSTM LM and the learned per-task layer weighting.
- [DistilBERT, a distilled version of BERT](https://arxiv.org/abs/1910.01108) — **Sanh et al. (2019)** — 40% smaller, ~97% of the quality via knowledge distillation.
- [ELECTRA: Pre-training Text Encoders as Discriminators](https://arxiv.org/abs/2003.10555) — **Clark et al. (2020)** — replaced-token detection, far more sample-efficient than MLM.
- [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) — **Liu et al. (2019)** — more data, no NSP, dynamic masking; "BERT was undertrained."
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084) — **Reimers & Gurevych (2019)** — why raw BERT sentence vectors fail, and the Siamese fix.
- [Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder (ModernBERT)](https://arxiv.org/abs/2412.13663) — **Warner et al. (2024)** — the 2024–25 encoder refresh: rotary position embeddings, alternating local/global attention, an 8k context, and 2 trillion training tokens; the encoder to reach for now instead of BERT-base.

**Books**:
- [Dive into Deep Learning — BERT: pretraining + fine-tuning](https://d2l.ai/chapter_natural-language-processing-pretraining/bert.html) — **Zhang et al.** — BERT built from scratch with runnable code.
- [Speech and Language Processing, 3rd ed. — Ch. 11 "Fine-Tuning and Masked Language Models"](https://web.stanford.edu/~jurafsky/slp3/11.pdf) — **Jurafsky & Martin** — contextual embeddings, BERT, MLM, and fine-tuning in the standard text.
