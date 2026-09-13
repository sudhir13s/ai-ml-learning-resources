---
id: "09-llms/decoding-and-sampling/references"
topic: "Decoding & Sampling — References"
parent: "09-llms/decoding-and-sampling"
type: references
updated: 2026-09-13
---

# Decoding & Sampling — references

> Companion link library for **[Decoding & Sampling](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See the whole menu of strategies** — watch [Greedy? Min-p? Beam Search? How LLMs Actually Pick Words](https://www.youtube.com/watch?v=o-_SZ_itxeA) (**AI Coffee Break with Letitia**). *Greedy through min-p in one pass — the map before the page derives each one.*
2. **Separate the three sampling knobs** — read [How do temperature, top-k, and top-p sampling differ?](https://sebastianraschka.com/faq/docs/temperature-topk-topp-sampling.html) (**Sebastian Raschka**). *A short, correct contrast of what each control does to the distribution, with code.*
3. **See every decoder side by side in code** — read [How to generate text: decoding methods with Transformers](https://huggingface.co/blog/how-to-generate) (**Hugging Face, Patrick von Platen**). *Greedy, beam, top-k and top-p run on the same prompt so the output differences are visible.*
4. **Learn why truncation exists** — read [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) (**Holtzman et al., 2019**). *The degeneration analysis behind the page's "corridor" and the origin of top-p.*
5. **Set the knobs in a serving engine** — read [Sampling parameters](https://docs.vllm.ai/en/latest/api/vllm/sampling_params/) (**vLLM**). *Temperature, top-p, top-k, min-p and the penalties exactly as production exposes them.*

**In this platform**:
- [Chain-of-Thought Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) — sampled reasoning paths, where the decoder choice changes answer quality.
- [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/decoder-only-models/decoder-only-models) — the model whose logits every decoder consumes.
- [Decoding Strategies](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/decoding-strategies/decoding-strategies) — the same strategies in the sequence-to-sequence framing of classic NLP.
- [Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — the engine that runs the decode loop, and what makes it fast.
- [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/language-modeling-objectives/language-modeling-objectives) — why the model outputs a next-token distribution in the first place.
- [LLM Evaluation & Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) — why benchmarks decode greedily, and how sampled metrics report a seed.
- [Loss Functions (softmax & cross-entropy)](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/loss-functions/loss-functions) — the numerically stable softmax the temperature knob reshapes.
- [Speculative Decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) — a speed technique whose output matches the chosen strategy exactly.
- [Test-Time Computation and Scaling](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/test-time-computation-and-scaling/test-time-computation-and-scaling) — spending more decode steps, and more samples, for better answers.

**Videos**:
- [Beam Search — decoding strategy explained](https://www.youtube.com/watch?v=vCcXs5nxmbI) — **The AI Loop** — beam-search intuition and the width and length-penalty tradeoffs.
- [Greedy? Min-p? Beam Search? How LLMs Actually Pick Words](https://www.youtube.com/watch?v=o-_SZ_itxeA) — **AI Coffee Break with Letitia** — the clearest survey of decoding strategies, greedy through min-p.
- [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY) — **Andrej Karpathy** — the generation loop where temperature and sampling are implemented line by line.
- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **Andrej Karpathy** — the sampling loop inside a real training and evaluation script.

**Courses**:
- [NLP Course For You — Language Modeling: generation strategies](https://lena-voita.github.io/nlp_course/language_modeling.html) — **Lena Voita** — an illustrated course page on how each sampling knob reshapes the next-token distribution.
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — decoding within the full LLM inference stack.

**Interactive**:
- [LLM Visualizer (3D)](https://bbycroft.net/llm) — **Brendan Bycroft** — walk a token through a small GPT's forward pass and see the logits a decoder then samples from.

**Articles**:
- [Assisted Generation: a new direction toward low-latency text generation](https://huggingface.co/blog/assisted-generation) — **Hugging Face (Joao Gante)** — draft-and-verify generation animated step by step; a speed technique that leaves the chosen strategy intact.
- [Controllable Neural Text Generation](https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/) — **Lilian Weng** — decoding and steering generation, including degeneration and sampling.
- [How continuous batching enables 23x throughput in LLM inference](https://www.anyscale.com/blog/continuous-batching-llm-inference) — **Anyscale** — the serving loop that runs many decoders side by side.
- [How do temperature, top-k, and top-p sampling differ?](https://sebastianraschka.com/faq/docs/temperature-topk-topp-sampling.html) — **Sebastian Raschka** — a crisp, correct contrast of the three core sampling controls, with code for each.
- [How to generate text: decoding methods with Transformers](https://huggingface.co/blog/how-to-generate) — **Hugging Face (Patrick von Platen)** — the canonical code-first decoding explainer, greedy through top-p side by side.
- [Speeding up the GPT — KV cache](https://www.dipkumar.dev/becoming-the-unbeatable/posts/gpt-kvcache/) — **Dipkumar Patel** — the generation loop the decoder runs inside.
- [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — **Jay Alammar** — autoregressive generation drawn token by token, up to the output distribution.

**Papers**:
- [A Contrastive Framework for Neural Text Generation (Contrastive Search)](https://arxiv.org/abs/2202.06417) — **Su, Lan, Wang, Yogatama, Kong & Collier (2022)** — picks tokens that are probable *and* dissimilar to the context in representation space.
- [CTRL: A Conditional Transformer Language Model for Controllable Generation](https://arxiv.org/abs/1909.05858) — **Keskar, McCann, Varshney, Xiong & Socher (2019)** — introduces the penalized sampling that became the repetition penalty.
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — **Hinton, Vinyals & Dean (2015)** — origin of the temperature-scaled softmax, §2.
- [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)** — the vLLM engine behind the production sampling parameters on the page.
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) — **Leviathan, Kalman & Matias (2023)** — proves draft-and-verify output is distributionally identical to plain sampling.
- [Google's Neural Machine Translation System (GNMT)](https://arxiv.org/abs/1609.08144) — **Wu et al. (2016)** — §7 gives the length-normalized beam-search score.
- [Hierarchical Neural Story Generation (top-k sampling)](https://arxiv.org/abs/1805.04833) — **Fan, Lewis & Dauphin (2018)** — introduces top-k truncated sampling for open-ended generation.
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — **Brown et al. (2020)** — temperature and sampling settings used at scale.
- [Locally Typical Sampling](https://arxiv.org/abs/2202.00666) — **Meister, Pimentel, Wiher & Cotterell (2022)** — keep tokens whose information content is typical, an information-theoretic alternative to top-p.
- [The Curious Case of Neural Text Degeneration (Nucleus Sampling)](https://arxiv.org/abs/1904.09751) — **Holtzman, Buys, Du, Forbes & Choi (2019)** — introduces top-p sampling and the degeneration analysis; the most important paper for this topic.
- [Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs](https://arxiv.org/abs/2407.01082) — **Nguyen et al. (2024, ICLR 2025)** — the cutoff that scales with the top token's probability, now a standard knob in vLLM, llama.cpp and Transformers.

**Documentation**:
- [Generation strategies](https://huggingface.co/docs/transformers/en/generation_strategies) — **Hugging Face Transformers** — every `.generate()` decoding argument, with defaults.
- [Sampling parameters](https://docs.vllm.ai/en/latest/api/vllm/sampling_params/) — **vLLM** — `SamplingParams`: temperature, top-p, top-k, min-p and the penalties as a serving engine exposes them.

**Books**:
- [Dive into Deep Learning — Ch. 10 "Beam Search"](https://d2l.ai/chapter_recurrent-modern/beam-search.html) — **Zhang, Lipton, Li & Smola** — greedy as the $b=1$ case, beam search, and length-normalized scoring with runnable code.
- [Hands-On Large Language Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) — **Jay Alammar & Maarten Grootendorst (2024)** — the open code companion; the generation chapters cover sampling parameters in practice.
- [Speech and Language Processing, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky & Martin** — autoregressive generation, greedy vs sampling, temperature, top-k and top-p.
