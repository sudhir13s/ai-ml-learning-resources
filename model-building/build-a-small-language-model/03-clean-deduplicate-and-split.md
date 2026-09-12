---
title: "Clean, Deduplicate and Split"
id: lr-slm-clean-deduplicate-and-split
minutes: 22
core_idea: "Deduplication decides what the model memorises and splitting decides whether the held-out number is a measurement or a comfort — and both are silent when they go wrong."
builds_on: [lr-slm-choose-and-govern-a-corpus]
leads_to: [lr-slm-train-a-tokenizer]
related: [pw-data-preparation]
section: "ai-ml-learning-resources"
workflow: "build-a-small-language-model"
chapter: 2
status: complete
template: workflow
category: model-building
---

# Clean, Deduplicate and Split

This is the stage where a project can go wrong without producing a single error, and where the
damage shows up as a *good* number rather than a bad one. A leaky split reports falling held-out
loss forever. A duplicated corpus reports a model that has learned. Both look like success.

Four things happen here, and the order is a decision:

```mermaid
flowchart LR
    N["normalise<br/>NFC · whitespace · controls"] --> D1["exact dedup<br/>content hash"]
    D1 --> Q["quality filter<br/>length · alphabetic ratio"]
    Q --> D2["near dedup<br/>MinHash + LSH"]
    D2 --> S["split<br/>hash of the document id"]
```

---

## Normalise, conservatively

Two spellings of the same passage have to compare equal, or deduplication cannot see them. That is
the entire job of normalisation, and it is a smaller job than it looks.

```python
def normalize_text(text: str) -> str:
    """Normalise Unicode form and whitespace so equal passages compare equal."""
    composed = unicodedata.normalize("NFC", text)
    without_control = _CONTROL_CHARS.sub("", composed)
    collapsed = _WHITESPACE_RUN.sub(" ", without_control)
    return _BLANK_LINES.sub("\n\n", collapsed).strip()
```

Unicode composition, control characters removed, runs of spaces collapsed, no more than one blank
line. **Case, punctuation and spelling are left alone.** A pretraining corpus should teach the model
the text as written; lowercasing it or stripping its punctuation teaches a dialect nobody writes,
and the model will reproduce that dialect at generation time.

---

## Exact duplicates first, because the check is cheap

The order in the diagram is not arbitrary. Exact deduplication is a hash lookup; the near-duplicate
pass is the expensive one, and the quality filter is in between. Removing exact copies first means
neither of the later passes ever processes the same text twice.

```python
normalized = [_normalized(document) for document in documents]
unique, dropped_exact = _drop_exact_duplicates(normalized)
kept, dropped_short, dropped_low_alpha = _filter_quality(unique, config)
survivors, dropped_near = _drop_near_duplicates(kept, config)
```

---

## Quality filtering is two thresholds, both arguable

```python
min_characters: int = 32
min_alphabetic_ratio: float = 0.5
```

A document under thirty-two characters carries no context to learn from. A document less than half
letters and digits is usually markup, a table of numbers, or a corrupted extraction.

Both numbers are corpus-specific and both are visible in the output, which is the point of reporting
them rather than burying them:

```text
dropped 879 short, 0 low-alphabetic, 74 exact-duplicate, 0 near-duplicate
```

Eight hundred and seventy-nine one-line stage directions and interjections went; nothing was
non-textual, because this corpus is prose all the way down.

---

## Near-duplicate detection: MinHash, then banding

Exact duplicates are easy. The ones that matter are passages that differ by a word — a reprinted
article with a new headline, a boilerplate paragraph across a thousand documents. Comparing every
pair is quadratic and impossible past a few thousand documents.

**MinHash** solves the comparison. Each document becomes a set of character shingles; a family of
hash functions each contribute the minimum hash over that set; the resulting signature has a
property worth stating exactly:

> The expected fraction of signature positions where two documents agree **is** the Jaccard
> similarity of their shingle sets.

So a sixty-four-number signature estimates a set comparison of thousands of elements.

**Locality-sensitive hashing** solves the scale. The signature is cut into bands; two documents
become *candidates* only when some band matches exactly. Similar documents share a band with high
probability; dissimilar ones almost never do.

```python
rows = config.minhash_permutations // config.lsh_bands   # 64 // 16 = 4
for band in range(config.lsh_bands):
    key = _band_key(signature, band, rows)
    buckets.setdefault((band, key), []).append(index)
```

Sixteen bands of four rows each. Only candidates get their full signatures compared, and only pairs
estimating above `0.8` are dropped.

**On this corpus it finds nothing**, and that is the honest result rather than a bug: a
single-author play collection has few near-duplicate speeches, and the seventy-four exact repeats
were already gone. The machinery is there because a real corpus is where it earns its cost — and
because a pipeline that has never been run against the case it exists for is a pipeline nobody
should trust.

---

## Splitting: the decision that makes the numbers real

Here is the one to get right.

```python
def split_name_for(doc_id: str, config: CleanConfig) -> SplitName:
    """Assign a document to a split as a pure function of its content identifier."""
    digest = hashlib.blake2b(
        doc_id.encode("ascii"), digest_size=8, key=str(config.seed).encode("ascii")
    ).digest()
    position = struct.unpack(">Q", digest)[0] / float(1 << 64)
    if position < config.test_fraction:
        return "test"
    if position < config.test_fraction + config.validation_fraction:
        return "validation"
    return "train"
```

A seeded digest of the identifier maps to the unit interval; the bottom slices are held out.
**Because the input is the content identifier, and the identifier is a hash of the text**, three
properties follow that no shuffle can give you:

- **Stable across runs.** Re-running the pipeline assigns every document to the same split.
- **Stable as the corpus grows.** Adding a thousand documents does not move the existing ones, so a
  perplexity measured last month is comparable to one measured today.
- **Duplicate-safe.** Two copies of a passage receive the same split *by construction*. A passage
  cannot be trained on and then held out.

**The common alternative is shuffling token offsets**, which fails all three. A model evaluated on
text it trained on reports falling held-out loss for as long as you keep training. The overfitting
does not disappear — it becomes invisible.

---

## An empty split is a configuration error, and it is caught here

```python
def require_populated_splits(splits, config) -> None:
    """Fail here rather than three stages later, when an empty split becomes an empty shard."""
```

A corpus too small for a 5% test slice to draw anything is a configuration problem. Discovering it
in the batcher, four stages later, as "split has 0 tokens" is technically the same information and
practically a much worse experience — so `clean_corpus` stays a pure function and the pipeline
calls this check.

---

## Running it

```bash
PYTHONPATH=. python -m slmkit.cli corpus --preset scale
```

```text
corpus: 7231 -> 6278 documents (86.8% retained); dropped 879 short, 0 low-alphabetic, 74 exact-duplicate, 0 near-duplicate
splits: {'train': 5637, 'validation': 325, 'test': 316}
```

Every number is checkable against the corpus, which is why the stage prints them all rather than a
success message.

---

## Verifying the split does what it claims

Two questions worth answering yourself before trusting any later number:

```python
from slmkit.data.clean import CleanConfig, split_name_for

config = CleanConfig()
print(split_name_for("0123456789abcdef", config))   # same answer every time
print(split_name_for("0123456789abcdef", config))
```

And that the near-duplicate pass really fires when there is something to find:

```python
from slmkit.data.clean import clean_corpus
from slmkit.domain.models import Document

original = ("The measure of a corpus is the text that survives its cleaning, "
            "and the measure of a split is whether it stayed honest.")
docs = [Document("a", original, "t"),
        Document("b", original.replace("honest", "honest indeed"), "t")]
_, stats = clean_corpus(docs, CleanConfig())
print(stats.dropped_near_duplicate)   # 1
```

Both of these are tests in the project, for the same reason.

## Pitfalls

- **Splitting by token offset or by shuffle.** The held-out loss stops measuring generalisation, and
  nothing tells you.
- **Normalising aggressively.** Lowercasing and stripping punctuation teaches a register the model
  will then write in.
- **Running near-duplicate detection before exact deduplication.** The expensive pass pays for text
  a hash lookup would have removed.
- **Trusting a deduplication stage you have never seen fire.** Construct a near-duplicate pair and
  watch it get dropped.
- **Letting a quality threshold hide in the code.** Print what each filter removed; the numbers are
  how you tune them.

## Key takeaways

- **Order matters:** normalise, exact-dedup, filter, near-dedup, split — cheapest checks first.
- **MinHash estimates Jaccard similarity from a short signature; banding makes the search linear.**
- **Split on a hash of the document's content**, so the assignment is stable, growth-safe and
  duplicate-safe.
- **A leaky split does not fail — it flatters.** That is why it is the thing to verify first.
- **Report what every filter removed.** Silent filtering is untunable filtering.

## References

- The implementation: `slmkit/data/clean.py` in
  [small-language-model](/python/python-production-examples/small-language-model/readme)
- Broder, *On the resemblance and containment of documents* — the original MinHash result:
  <https://doi.org/10.1109/SEQUEN.1997.666900>
- Leskovec, Rajaraman and Ullman, *Mining of Massive Datasets*, chapter 3 — the free textbook
  treatment of shingling, MinHash and locality-sensitive hashing: <http://www.mmds.org/>
- Lee et al., *Deduplicating Training Data Makes Language Models Better*:
  <https://arxiv.org/abs/2107.06499>
