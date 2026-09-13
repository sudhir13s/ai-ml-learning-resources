---
id: "06-nlp/tokenization/references"
topic: "Tokenization & Subword Algorithms — References"
parent: "06-nlp/tokenization"
type: references
updated: 2026-09-13
---

# Tokenization & Subword Algorithms — references

> Companion link library for **[Tokenization & Subword Algorithms](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Build intuition** — watch [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) (**Andrej Karpathy**). *Implements byte-level BPE from scratch; the single best resource for making tokenization stick.*
2. **See the algorithms side by side** — read [Summary of the tokenizers](https://huggingface.co/docs/transformers/en/tokenizer_summary) (**Hugging Face**). *Crisp contrast of BPE vs WordPiece vs Unigram.*
3. **Walk the merges** — work through [Byte-Pair Encoding tokenization](https://huggingface.co/learn/llm-course/en/chapter6/5) (**Hugging Face course**). *A numeric BPE training example you can redo by hand.*
4. **Read the source** — read [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909) (**Sennrich et al., 2016**). *The paper that brought BPE to NLP.*
5. **Connect to the probabilistic view** — read [Subword Regularization (Unigram LM)](https://arxiv.org/abs/1804.10959) (**Kudo, 2018**). *The probabilistic alternative to merge-based tokenization.*

**In this platform**:
- [Contextual Embeddings (ELMo / BERT)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/contextual-embeddings-elmo-bert/contextual-embeddings-elmo-bert) — builds on this: what the model does with token ids in context.
- [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — puts it to work: tokens are what fills the cache at inference.
- [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — puts it to work in applications built on tokenized text.
- [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) — chat templates and loss masking around the token sequences this page builds.
- [Text Preprocessing & Normalization](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/text-preprocessing-and-normalization/text-preprocessing-and-normalization) — comes before this: cleaning text before it is tokenized.
- [Tokenization & BPE (intuition)](/ai-ml/ai-ml-intuitions/representation/discrete-representations/tokenization-and-bpe-intuition) — the *why* behind subword units.
- [Tokenization & Subword Algorithms](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms) — the concept page this library accompanies.
- [Word Embeddings (Word2Vec / GloVe / FastText)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/word-embeddings-word2vec-glove-fasttext/word-embeddings-word2vec-glove-fasttext) — builds on this: dense vectors for tokens.

**Videos**:
- [Byte Pair Encoding Tokenization](https://www.youtube.com/watch?v=HEikzVL-lZU) — **Hugging Face** — concise official walkthrough of the BPE training loop.
- [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) — **Andrej Karpathy** — builds a byte-level BPE tokenizer line by line (~2 hrs); the definitive deep walkthrough.
- [Natural Language Processing - Tokenization (NLP Zero to Hero - Part 1)](https://www.youtube.com/watch?v=fNxaJsNG3-s) — **TensorFlow** — gentle on-ramp from words to token ids in code.
- [Tokenization & Byte Pair Encoding](https://www.youtube.com/watch?v=gstdcCDqdlc) — **Luis Serrano** — gentle, visual intuition for what BPE does and why subword wins.
- [Unigram Tokenization](https://www.youtube.com/watch?v=TGZfZVuF9Yc) — **Hugging Face** — the probabilistic prune-down model behind SentencePiece/T5.
- [What makes LLM tokenizers different from each other?](https://www.youtube.com/watch?v=rT6wVLEDC_w) — **Jay Alammar** — the same text through GPT-4, Flan-T5, StarCoder and BERT tokenizers, compared piece by piece.
- [WordPiece Tokenization](https://www.youtube.com/watch?v=qpv6ms_t_1A) — **Hugging Face** — how BERT's tokenizer scores merges by likelihood (vs BPE's frequency).

**Courses**:
- [Hugging Face LLM Course — Ch. 6: The Tokenizers Library](https://huggingface.co/learn/llm-course/en/chapter6/1) — **Hugging Face** — builds BPE, WordPiece, and Unigram tokenizers in code; the most practical hands-on treatment.
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford (Manning)** — the subword-modeling lecture sets the linguistic and modeling context.

**Interactive**:
- [OpenAI Tokenizer playground](https://platform.openai.com/tokenizer) — **OpenAI** — paste any text and watch it split into colored tokens with a live count.
- [The Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) — **Xenova (Hugging Face)** — paste text and see the pieces and counts for many open models' tokenizers, leading spaces included.
- [Tiktokenizer](https://tiktokenizer.vercel.app/) — **Diagram (community)** — side-by-side token counts across GPT, Llama, and other tokenizers, with token ids shown.

**Articles**:
- [Byte-Pair Encoding tokenization](https://huggingface.co/learn/llm-course/en/chapter6/5) — **Hugging Face** — worked numeric example of learning BPE merges.
- [The Technical User's Introduction to LLM Tokenization](https://christophergs.com/blog/understanding-llm-tokenization) — **Christopher Samiullah** — practical tour of tiktoken, byte-level BPE, and the gotchas (digits, whitespace, glitch tokens).
- [Unigram tokenization](https://huggingface.co/learn/llm-course/en/chapter6/7) — **Hugging Face** — the EM training + Viterbi decoding of the Unigram model, step by step.
- [WordPiece tokenization](https://huggingface.co/learn/llm-course/en/chapter6/6) — **Hugging Face** — the likelihood-score merge rule and `##` encoding, worked through.

**Papers**:
- [BPE-Dropout: Simple and Effective Subword Regularization](https://arxiv.org/abs/1910.13267) — **Provilkov et al. (2020)** — stochastic BPE segmentation, the BPE analogue of subword regularization.
- [Byte Latent Transformer: Patches Scale Better Than Tokens (BLT)](https://arxiv.org/abs/2412.09871) — **Pagnoni et al. (2024)** — the tokenizer-free line: group raw bytes into *dynamic* patches by next-byte entropy. Read it as the strongest answer to "why is a fixed vocabulary still here?", not as a replacement you would deploy today.
- [Google's Neural Machine Translation System (GNMT)](https://arxiv.org/abs/1609.08144) — **Wu et al. (2016)** — describes the WordPiece scheme later used by BERT.
- [Japanese and Korean Voice Search (WordPiece)](https://research.google/pubs/japanese-and-korean-voice-search/) — **Schuster & Nakajima (2012)** — the original WordPiece, later adopted by BERT.
- [Language Models are Unsupervised Multitask Learners (GPT-2)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) — **Radford et al. (2019)** — §2.2 introduces byte-level BPE, the no-OOV tokenizer behind GPT.
- [Neural Machine Translation of Rare Words with Subword Units (BPE)](https://arxiv.org/abs/1508.07909) — **Sennrich, Haddow & Birch (2016)** — brought BPE to NLP; the foundation of modern subword tokenization.
- [SentencePiece: A simple and language-independent subword tokenizer](https://arxiv.org/abs/1808.06226) — **Kudo & Richardson (2018)** — whitespace-as-`▁`, fully reversible, language-agnostic (used by T5, LLaMA).
- [Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder (ModernBERT)](https://arxiv.org/abs/2412.13663) — **Warner et al. (2024)** — §2 documents practical tokenizer choices for a new model (a code-aware BPE vocabulary, and why the old BERT WordPiece vocabulary was retired).
- [Subword Regularization: Improving NMT with Multiple Subword Candidates (Unigram LM)](https://arxiv.org/abs/1804.10959) — **Kudo (2018)** — the probabilistic Unigram model and subword-regularization sampling.

**Documentation**:
- [Chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating) — **Hugging Face** — `apply_chat_template`, the control tokens each model family expects, and why hand-added special tokens get duplicated.
- [Hugging Face Tokenizers](https://github.com/huggingface/tokenizers) — **Hugging Face** — production BPE/WordPiece/Unigram trainers and encoders in Rust with Python bindings.
- [SentencePiece](https://github.com/google/sentencepiece) — **Google** — the reference implementation of the SentencePiece framework (BPE + Unigram).
- [Summary of the tokenizers](https://huggingface.co/docs/transformers/en/tokenizer_summary) — **Hugging Face** — crisp side-by-side of BPE vs WordPiece vs Unigram.
- [tiktoken](https://github.com/openai/tiktoken) — **OpenAI** — the fast byte-level BPE tokenizer used by GPT-3.5/4 and by this page's code.

**Books**:
- [Dive into Deep Learning — Ch. 15.6 "Subword Embedding"](https://d2l.ai/chapter_natural-language-processing-pretraining/subword-embedding.html) — **Zhang, Lipton, Li & Smola** — BPE explained with runnable code.
- [Speech and Language Processing, 3rd ed. — Ch. 2 "Regular Expressions, Text Normalization, and Edit Distance"](https://web.stanford.edu/~jurafsky/slp3/2.pdf) — **Jurafsky & Martin** — tokenization and BPE in the standard NLP textbook.
