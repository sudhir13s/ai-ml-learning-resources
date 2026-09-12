---
title: "Train a Tokenizer"
id: lr-slm-train-a-tokenizer
minutes: 24
core_idea: "Byte-pair encoding is a compression algorithm you run once over your own corpus, and the vocabulary it produces silently fixes the model's context length, its embedding table, and what a perplexity number even means."
builds_on: [lr-slm-clean-deduplicate-and-split]
leads_to: [lr-slm-build-the-transformer]
related: [lr-scm-design-the-conversation-template]
section: "ai-ml-learning-resources"
workflow: "build-a-small-language-model"
chapter: 3
status: complete
template: workflow
category: model-building
---

# Train a Tokenizer

A model does not read text. It reads integers, and the tokenizer is the function that decides which
integers. That function is not downloaded here — it is *learned*, from the training split, in about
a minute.

Three things ride on it, and none of them is obvious from the outside:

- **Context length in practice.** A 256-token window holds 760 characters at this vocabulary's
  compression ratio and 450 at a worse one. The number is the same; what fits is not.
- **The size of the embedding table.** Vocabulary times model width, and at small scale that is most
  of the parameters.
- **What perplexity means.** Perplexity is per token, so two models with different vocabularies are
  not answering the same question.

---

## Byte-level: the choice that removes a whole class of bug

The alphabet is the 256 byte values. Every possible input is therefore representable, and:

```python
tokenizer.decode(tokenizer.encode(text)) == text     # for any UTF-8 string
```

There is **no unknown token**, no normalisation loss, and no failure mode where a rare character
quietly vanishes from the corpus. The project tests this on ASCII, on empty strings, on punctuation,
on Japanese, on emoji, and on mixed digits, because the guarantee is worth nothing if it holds only
for the cases you thought of.

The alternative — a character vocabulary or a word vocabulary — trades that guarantee for either a
longer sequence or an out-of-vocabulary token, and the out-of-vocabulary token is where corpora go
to lose information.

---

## The algorithm, in the order it runs

**Pre-tokenize into word-like chunks.** This is what stops merges from crossing word boundaries.

```python
_PRE_TOKEN = re.compile(
    r"'(?:s|t|re|ve|m|ll|d)| ?[^\W\d_]+| ?\d+| ?[^\s\w]+|\s+(?!\S)|\s+",
    re.UNICODE,
)
```

Contractions, a run of letters *with its leading space*, a run of digits, a run of punctuation,
whitespace. Keeping the leading space attached is why `" the"` becomes a single token and `"e t"`
never does — the convention GPT-2 established, written out in plain `re` because the standard
library has no Unicode-property classes.

**Count chunks, not characters.** A million-character corpus has only tens of thousands of distinct
chunks, so each merge pass scans a table rather than the corpus.

```python
sequences: dict[tuple[int, ...], int] = {
    tuple(chunk.encode("utf-8")): count for chunk, count in chunk_counts.items()
}
```

**Merge the most frequent adjacent pair, repeatedly, recording each merge.**

```python
while len(merges) < vocab_size - floor:
    pair_counts = _count_pairs(sequences)
    if not pair_counts:
        break
    best = max(pair_counts.items(), key=lambda item: (item[1], _tiebreak(item[0])))[0]
    new_id = _BYTE_VOCAB_SIZE + len(merges)
    sequences = {
        tuple(_apply_merge(list(sequence), best, new_id)): count
        for sequence, count in sequences.items()
    }
    merges.append(best)
```

The tiebreak is not decoration. Two pairs with equal frequency must resolve the same way on every
run, or two training runs produce two different vocabularies and nothing is reproducible.

**Encoding replays the merges in the order they were learned**, lowest rank first. That ordering is
the whole state: a saved tokenizer is a list of merges and a list of special tokens, and nothing
else.

---

## The target is a ceiling, not a promise

```python
tokenizer = train_bpe(["the quick brown fox jumps over the lazy dog. ..."], vocab_size=320)
tokenizer.vocab_size        # 296
```

A small corpus runs out of repeated pairs — every chunk has collapsed to a single token — and
training stops there. **Read the resulting vocabulary size rather than assuming the request was
met.** This is a real behaviour, not an edge case: it is what happens on any small domain corpus.

---

## Train it on the training split only

```python
train_text = (splits_dir / "train.txt").read_text(encoding="utf-8")
tokenizer = train_bpe([train_text], vocab_size=settings.target_vocab_size)
```

Learning the vocabulary from the whole corpus lets held-out text influence which sequences get their
own token. That is a quiet contamination: the model is then evaluated on text its tokenizer was
tuned to compress, so the held-out perplexity is flattered by an amount nobody can measure
afterwards.

It costs nothing to avoid, and it is very easy to do by accident.

---

## What the compression ratio tells you

```bash
PYTHONPATH=. python -m slmkit.cli tokenizer --preset scale
```

```text
tokenizer: 4096 ids from 3839 merges; 329515 tokens encoded at 2.97 characters/token
```

| Preset | Vocabulary | Merges | Characters per token | Train split |
|---|---|---|---|---|
| `toy` | 512 | 255 | 1.76 | 496,002 tokens |
| `scale` | 4,096 | 3,839 | 2.97 | 294,181 tokens |

**A larger vocabulary buys shorter sequences and costs embedding parameters.** Going from 512 to
4,096 ids cut the training split by 40% — the same text, 200,000 fewer positions to process — and
added about 1.4 million parameters to the embedding table.

At this scale that trade is worth it: attention is quadratic in sequence length and the embedding
table is a linear cost. At a much larger scale the balance moves, which is why production
vocabularies sit in the 32,000–128,000 range rather than growing without limit.

**Under 3 characters per token is low.** Modern production tokenizers reach 4 or more on English
prose. Two reasons: 4,096 ids is a small vocabulary, and Elizabethan verse has an unusual
distribution — the tokenizer spends merges on `thou`, `'tis` and speaker names.

---

## The special token, and why there is exactly one

```python
END_OF_TEXT = "<|endoftext|>"
```

Documents are concatenated into one stream with this id between them. It does two jobs: it teaches
the model that a document *ends*, and it gives generation a natural stop signal.

One special token is enough for a base model. Chat models need more — the roles and the end-of-turn
marker — and the next course in this build takes a position on that which is worth previewing here:
**it adds markers as plain text rather than as new ids**, because adding an id would resize the
embedding table and invalidate the base checkpoint. Byte-level encoding is what makes that possible.

---

## Verifying it yourself

```python
from slmkit.tokenizer.bpe import BPETokenizer
tok = BPETokenizer.load("runs/scale/tokenizer.json")

tok.decode(tok.encode("unicode: naïve café 日本語 🙂"))   # exactly the input
len(tok.encode(" the"))                                  # 1 — a frequent chunk became one token
tok.vocab_size                                           # 4096 = 256 bytes + 3839 merges + 1 special
```

The third line is the arithmetic worth remembering: **byte alphabet plus one id per merge plus one
id per special token.**

## Pitfalls

- **Training the vocabulary on the whole corpus.** Held-out text influences the merges and the
  evaluation is quietly flattered.
- **Assuming the requested vocabulary size was reached.** A small corpus exhausts its pairs first.
- **Comparing perplexity across tokenizers.** It is a per-token measure; different vocabularies are
  different questions.
- **Adding a special token to a trained model's vocabulary.** It resizes the embedding table and
  invalidates the checkpoint.
- **Forgetting the tiebreak.** Equal-frequency pairs resolving differently make two runs produce two
  vocabularies.

## Key takeaways

- **Byte-level means every input is representable and round-trip is exact** — no unknown token, no
  silent loss.
- **Pre-tokenization is what keeps merges inside words**, and the leading space is part of the token.
- **Counting over a chunk-frequency table** is what makes training a vocabulary a one-minute job.
- **The vocabulary decides effective context length, embedding size, and the meaning of perplexity.**
- **Train it on the training split alone.**

## References

- The implementation: `slmkit/tokenizer/bpe.py` in
  [small-language-model](/python/python-production-examples/small-language-model/readme)
- Sennrich, Haddow and Birch, *Neural Machine Translation of Rare Words with Subword Units* — the
  paper that brought byte-pair encoding to language models: <https://arxiv.org/abs/1508.07909>
- Hugging Face, *Tokenizers* course chapter — a free, careful walk through the same algorithm:
  <https://huggingface.co/learn/llm-course/chapter6>
