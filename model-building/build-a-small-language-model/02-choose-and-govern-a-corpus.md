---
title: "Choose and Govern a Corpus"
id: lr-slm-choose-and-govern-a-corpus
minutes: 16
core_idea: "The corpus is the one input a model carries forever, so its licence and its provenance are engineering decisions rather than paperwork — and its size, not the architecture, is what usually caps the result."
builds_on: [lr-slm-why-build-a-model-from-scratch]
leads_to: [lr-slm-clean-deduplicate-and-split]
related: [pw-data-preparation]
section: "ai-ml-learning-resources"
workflow: "build-a-small-language-model"
chapter: 1
status: complete
template: workflow
category: model-building
---

# Choose and Govern a Corpus

A trained model is a lossy, irreversible compression of its training text. You cannot remove a
document from it later, you cannot audit which passage produced a given sentence, and you cannot
relicense it after the fact. Everything you decide about the corpus, you decide permanently.

That makes two questions engineering questions rather than administrative ones. **May you train on
this?** And **is there enough of it?**

---

## The licence question comes first

The rule this estate applies to every corpus is simple: **openly licensed, provenance recorded, or
it does not go in.** The project states its own compliance in a file beside the text:

```text
data/corpus/
├── tiny-shakespeare.txt     1,115,394 bytes
└── SOURCES.md               what it is, where it came from, why we may use it
```

`SOURCES.md` records the work, the author, the public-domain status of the underlying text, the MIT
licence of the distribution it was retrieved from, the size, and the date it was retrieved. That is
the whole obligation, and it takes five minutes at the start and is impossible to reconstruct at the
end.

**Two distinct claims have to hold**, and they are frequently confused:

- **The text itself** must be free to use. Shakespeare died in 1616; the plays are public domain
  worldwide.
- **The copy you obtained** must be free to redistribute. This one comes from a repository
  distributed under the MIT licence, so committing it to a repository is permitted.

A public-domain work inside a paywalled edition fails the second test. An openly licensed compilation
of copyrighted articles fails the first.

---

## Then the size question, which is usually the real constraint

The corpus here is about a million characters. The model trained on it has twelve million
parameters. Those two numbers are wildly out of proportion, and the mismatch is the single most
important fact about the result — it is why the held-out loss stops improving after five hundred
steps and climbs from there.

| Quantity | This build |
|---|---|
| Corpus | 1,115,394 characters |
| After cleaning | 6,278 documents, 1,050,000 characters |
| Training split, tokenized | **294,181 tokens** |
| Model parameters | **12,194,688** |
| Ratio | roughly 0.024 tokens per parameter |

Published scaling work puts the compute-efficient ratio around **20 tokens per parameter**. This
build is off by nearly three orders of magnitude, and it is off deliberately: the point is to run
the arc end to end on a laptop, not to reach a frontier.

**The consequence to internalise:** when this model disappoints, the answer is *more text*, not more
layers. A chapter later you will watch that happen in the loss curves rather than take it on trust.

---

## What a document is, and why it matters here

The pipeline does not work on files or on lines. It works on **documents**, and the document is the
unit of three separate later decisions:

- **Deduplication** — a duplicate is a duplicate *document*.
- **Splitting** — a document goes to exactly one of train, validation or test.
- **Provenance** — a token traces back to the document it came from.

The bundled corpus is dialogue, so a document is one speech: a speaker line and what they say, with
blank lines between them.

```text
First Citizen:
Before we proceed any further, hear me speak.

All:
Speak, speak.

First Citizen:
You are all resolved rather to die than to famish?
```

Three documents. Seven thousand two hundred and thirty-one of them in the file.

```python
def load_documents(path: Path) -> list[Document]:
    """Load a corpus from a file or a directory, cut into blank-line-separated documents."""
    if not path.exists():
        raise CorpusError(f"corpus path does not exist: {path}")
    documents = list(_iter_documents(path))
    if not documents:
        raise CorpusError(f"corpus contained no documents: {path}")
    return documents
```

---

## Identity follows content, not position

The single design decision in this stage that pays off three chapters later: **a document's
identifier is a hash of its text**, not a running index.

```python
def content_id(text: str) -> str:
    """A stable 16-hex-character identifier for a piece of text."""
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return digest[:16]
```

Two consequences follow, and both are load-bearing:

- **Deduplication becomes a set operation.** The same speech appearing in two plays gets the same
  identifier, so finding exact duplicates is a lookup rather than a comparison.
- **Split assignment becomes reproducible and safe.** Because the split is a function of the
  identifier, and the identifier is a function of the text, two copies of a passage *cannot* land on
  opposite sides of the train/held-out boundary. A held-out score is only a measurement if that is
  true.

---

## Running it

```bash
cd python_based/python-production-examples/small-language-model
PYTHONPATH=. python -m slmkit.cli corpus --preset scale
```

```text
corpus: 7231 -> 6278 documents (86.8% retained); dropped 879 short, 0 low-alphabetic, 74 exact-duplicate, 0 near-duplicate
splits: {'train': 5637, 'validation': 325, 'test': 316}
```

The next chapter is about every number on that first line.

---

## Using a different corpus

Point the loader at anything — a directory of `.txt` or `.md` files, or a single file of
blank-line-separated blocks:

```bash
SLM_CORPUS_PATH=/path/to/your/corpus PYTHONPATH=. python -m slmkit.cli corpus --preset scale
```

Nothing else in the pipeline changes, because `slmkit/data/corpus.py` is the only module that knows
how raw text becomes documents. A JSONL dump or a parquet shard is a new loader there and nowhere
else.

Whatever you point it at, answer the two questions at the top of this chapter first, and write the
answers down beside the text.

## Pitfalls

- **Committing a corpus you cannot redistribute.** The text's licence and the copy's licence are two
  different claims and both have to hold.
- **Recording provenance later.** Nobody can reconstruct where a file came from six months on, and
  the model has already absorbed it.
- **Treating a line as a document.** Then deduplication removes common phrases and splitting scatters
  one passage across all three sets.
- **Blaming the architecture for a corpus problem.** Check the token-to-parameter ratio before
  changing a single hyperparameter.

## Key takeaways

- **A corpus is permanent in a way code is not** — record the licence and the provenance before you
  train, in a file beside the text.
- **The text's licence and the copy's licence are separate claims.**
- **Size is usually the binding constraint.** This build sits at 0.024 tokens per parameter against a
  compute-efficient 20, and the loss curves will show it.
- **The document is the unit of deduplication, splitting and provenance** — and identity has to
  follow content for the last two to be sound.

## References

- The project's own provenance record: `data/corpus/SOURCES.md` in
  [small-language-model](/python/python-production-examples/small-language-model/readme)
- The corpus distribution, MIT licensed: <https://github.com/karpathy/char-rnn>
- Hoffmann et al., *Training Compute-Optimal Large Language Models* — where the twenty-tokens-per-parameter
  figure comes from: <https://arxiv.org/abs/2203.15556>
- Deeper on the reusable mechanism:
  [Data Preparation (workflow)](/ai-ml/practitioner-workflows/data-and-inputs/data-preparation)
