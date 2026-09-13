"""Curate TinyCorpus: clean, exact-dedup, MinHash near-dedup, decontaminate, split.

A ten-document corpus salted with every defect a web crawl carries (an exact
duplicate, a reworded near-duplicate, an email address, a junk string, a French
sentence, and a sentence that also appears in an evaluation set) travels through
the curation funnel. Standard library only, deterministic, runs in well under a
second:

    uv run --python 3.12 python curate_tiny_corpus.py
"""

import hashlib
import html
import random
import re
import unicodedata

SPLIT_SEED = 0
SHINGLE_WORDS = 2
SIGNATURE_LENGTH = 64
NEAR_DUP_THRESHOLD = 0.3
LSH_BANDS = 16
LSH_ROWS_PER_BAND = SIGNATURE_LENGTH // LSH_BANDS
DECONTAMINATION_NGRAM = 6
MIN_WORDS = 4
MIN_DISTINCT_CHARS = 10
MIN_STOPWORD_HITS = 2
SPLIT_FRACTIONS = (0.6, 0.2)

ENGLISH_STOPWORDS = {
    "the", "a", "an", "is", "are", "to", "of", "in", "and", "for",
    "that", "can", "when", "it", "love", "enjoy",
}
PII_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+|\b\d{3}[-.]?\d{3}[-.]?\d{4}\b")
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")

RAW_CORPUS = [
    "Cats are wonderful pets that love to nap in the sun.",
    "Cats are wonderful pets that love to nap in the sun.",        # exact duplicate
    "Cats are wonderful pets that love napping in the sunshine.",  # reworded near-duplicate
    "Dogs are loyal companions and enjoy long walks outdoors.",
    "Birds can fly south for the winter when it gets cold.",
    "Fish are quiet pets that can live in a small glass tank.",
    "Horses are strong animals and enjoy running in the field.",   # also in the eval set
    "Email the team at jane.doe@example.com for the report.",      # English with PII
    "aaaaaaaaaaaaaaaaaaaa",                                        # low-quality junk
    "Le chat dort sur le canape toute la journee.",               # not English
]

EVAL_SET = [
    "Q: Complete the sentence: Horses are strong animals and enjoy running in the ___ A: field",
    "Q: Where do birds go in winter? A: They migrate to warmer places.",  # paraphrase: no n-gram hit
]


# ---------------------------------------------------------------- cleaning ---
def normalize_markup(text):
    """Unicode NFC, unescape entities, strip tags, collapse whitespace."""
    text = unicodedata.normalize("NFC", html.unescape(text))
    text = HTML_TAG_PATTERN.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def is_english(text):
    """Crude language ID: an English document hits several English stopwords."""
    words = set(re.findall(r"[a-z]+", text.lower()))
    return len(words & ENGLISH_STOPWORDS) >= MIN_STOPWORD_HITS


def passes_quality(text):
    """Reject documents that are too short or have too little character variety."""
    return len(text.split()) >= MIN_WORDS and len(set(text.lower())) >= MIN_DISTINCT_CHARS


def redact_pii(text):
    """Mask emails and phone numbers in place; the rest of the document is kept."""
    return PII_PATTERN.sub("[REDACTED]", text)


def clean_corpus(documents):
    kept = []
    for document in documents:
        document = normalize_markup(document)
        if not passes_quality(document) or not is_english(document):
            continue
        kept.append(redact_pii(document))
    return kept


# ------------------------------------------------------------ exact dedup ---
def dedup_key(text):
    """The comparison form: lowercase, whitespace collapsed."""
    return re.sub(r"\s+", " ", text.lower().strip())


def md5_of(text):
    return hashlib.md5(dedup_key(text).encode()).hexdigest()


def exact_dedup(documents):
    seen_hashes, unique = set(), []
    for document in documents:
        digest = md5_of(document)
        if digest not in seen_hashes:
            seen_hashes.add(digest)
            unique.append(document)
    return unique


# ------------------------------------------------------- near-dup (MinHash) ---
def shingles(text, width=SHINGLE_WORDS):
    words = dedup_key(text).split()
    return {" ".join(words[i:i + width]) for i in range(max(1, len(words) - width + 1))}


def jaccard(set_a, set_b):
    return len(set_a & set_b) / len(set_a | set_b)


def minhash_signature(shingle_set, length=SIGNATURE_LENGTH):
    """Slot k holds the minimum of hash function k over the set; seed k picks the function."""
    return [
        min(int(hashlib.md5(f"{seed}:{piece}".encode()).hexdigest(), 16) for piece in shingle_set)
        for seed in range(length)
    ]


def estimated_jaccard(signature_a, signature_b):
    return sum(a == b for a, b in zip(signature_a, signature_b)) / len(signature_a)


def lsh_candidate_probability(similarity, bands=LSH_BANDS, rows=LSH_ROWS_PER_BAND):
    """Chance that two documents share at least one whole band of their signatures."""
    return 1 - (1 - similarity ** rows) ** bands


def lsh_band_keys(signature, bands=LSH_BANDS, rows=LSH_ROWS_PER_BAND):
    return {(band, tuple(signature[band * rows:(band + 1) * rows])) for band in range(bands)}


def near_dedup(documents, threshold=NEAR_DUP_THRESHOLD):
    """Greedy first-wins: drop a document whose estimate against any kept one clears the bar."""
    signatures = [minhash_signature(shingles(d)) for d in documents]
    kept_indices = []
    for index in range(len(documents)):
        if any(estimated_jaccard(signatures[index], signatures[j]) >= threshold
               for j in kept_indices):
            continue
        kept_indices.append(index)
    return [documents[i] for i in kept_indices]


# ---------------------------------------------------------- decontamination ---
def word_ngrams(text, n=DECONTAMINATION_NGRAM):
    words = re.findall(r"[a-z]+", text.lower())
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def decontaminate(documents, eval_items, n=DECONTAMINATION_NGRAM):
    """Drop any training document sharing a word n-gram with any evaluation item."""
    eval_ngrams = set().union(*(word_ngrams(item, n) for item in eval_items))
    kept, flagged = [], []
    for document in documents:
        overlap = word_ngrams(document, n) & eval_ngrams
        (flagged if overlap else kept).append((document, sorted(overlap)))
    return [d for d, _ in kept], flagged


# ---------------------------------------------------------------- splitting ---
def split_corpus(documents, seed=SPLIT_SEED):
    shuffled = documents[:]
    random.Random(seed).shuffle(shuffled)
    train_end = int(len(shuffled) * SPLIT_FRACTIONS[0])
    val_end = train_end + int(len(shuffled) * SPLIT_FRACTIONS[1])
    return shuffled[:train_end], shuffled[train_end:val_end], shuffled[val_end:]


def cross_split_overlap(train, val, test):
    train_keys = set(map(dedup_key, train))
    return (train_keys & set(map(dedup_key, val))) | (train_keys & set(map(dedup_key, test)))


# ------------------------------------------------------------------- report ---
def report_pair(doc_a, doc_b):
    shingles_a, shingles_b = shingles(doc_a), shingles(doc_b)
    shared, union = shingles_a & shingles_b, shingles_a | shingles_b
    true_similarity = jaccard(shingles_a, shingles_b)
    print(f"[pair]   |A|={len(shingles_a)} |B|={len(shingles_b)} shared={len(shared)} "
          f"union={len(union)} true Jaccard={true_similarity:.3f}")
    for length in (16, 64, 256):
        estimate = estimated_jaccard(minhash_signature(shingles_a, length),
                                     minhash_signature(shingles_b, length))
        print(f"[pair]   MinHash estimate, signature length {length:>3}: {estimate:.3f}")
    signature_a = minhash_signature(shingles_a)
    signature_b = minhash_signature(shingles_b)
    shared_bands = len(lsh_band_keys(signature_a) & lsh_band_keys(signature_b))
    print(f"[lsh]    {LSH_BANDS} bands x {LSH_ROWS_PER_BAND} rows: A and B share "
          f"{shared_bands} whole band(s) -> candidate={shared_bands > 0}")
    for similarity in (0.2, true_similarity, 0.8):
        print(f"[lsh]    P(candidate | s={similarity:.3f}) = "
              f"{lsh_candidate_probability(similarity):.3f}")


def main():
    cleaned = clean_corpus(RAW_CORPUS)
    print(f"[clean]  {len(RAW_CORPUS)} -> {len(cleaned)} docs")
    print(f"[clean]  redacted: '{next(d for d in cleaned if '[REDACTED]' in d)}'")

    for document in (RAW_CORPUS[0], RAW_CORPUS[2]):
        print(f"[md5]    {md5_of(document)}  '{document}'")
    unique = exact_dedup(cleaned)
    print(f"[exact]  {len(cleaned)} -> {len(unique)} docs")

    report_pair(RAW_CORPUS[0], RAW_CORPUS[2])
    distinct = near_dedup(unique)
    print(f"[near]   {len(unique)} -> {len(distinct)} docs (threshold {NEAR_DUP_THRESHOLD})")

    clean_for_training, flagged = decontaminate(distinct, EVAL_SET)
    for document, overlap in flagged:
        print(f"[decon]  dropped '{document}' via {overlap}")
    print(f"[decon]  {len(distinct)} -> {len(clean_for_training)} docs")

    train, val, test = split_corpus(clean_for_training)
    leakage = cross_split_overlap(train, val, test)
    assert not leakage, f"leakage across splits: {leakage}"
    print(f"[split]  train={len(train)} val={len(val)} test={len(test)} leakage={len(leakage)}")
    for name, split in (("train", train), ("val", val), ("test", test)):
        print(f"[split]  {name:<5} {split}")


if __name__ == "__main__":
    main()
