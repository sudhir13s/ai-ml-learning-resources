"""Build the data file for the page's interactive 3-D embedding-space explorer.

Reads the real pretrained GloVe vectors the page measures in "Code 2"
(`glove-wiki-gigaword-50`: GloVe 6B, 50 dimensions, Wikipedia 2014 + Gigaword 5,
400,000 words), keeps a curated vocabulary chosen so clusters and analogies are
visible, projects it to 3-D with PCA, and writes `../assets/glove-embedding-space.json`.

What the explorer needs, and why each part is here:

* the FULL 50-d vector of every curated word, so neighbours and analogies are computed
  in the real space, never in the 3-D shadow;
* the 3-D PCA coordinates and the variance they explain, so the page can say honestly
  how much of the space the picture shows;
* the full-400k-vocabulary answers for the preset analogies, so the explorer can show
  what the analogy returns when every word is a candidate, not only the curated ones.

The analogy arithmetic is exactly gensim's `KeyedVectors.most_similar`: average the
unit-normalized inputs (negatives subtracted), normalize, rank every word by cosine
with that direction, and exclude the input words. The script asserts the numbers the
page prints (queen 0.8524, rome 0.8466, the six cosines) before it writes anything.

Run (no gensim needed; it reads the file gensim's downloader already fetched):

    python build_embedding_space.py                 # reads ~/gensim-data/...
    GENSIM_DATA_DIR=/path python build_embedding_space.py

Verified on Python 3.12 / numpy 2.x. Deterministic; CPU; about ten seconds.
"""

from __future__ import annotations

import gzip
import json
import os
from dataclasses import dataclass
from pathlib import Path

import numpy as np

MODEL_NAME = "glove-wiki-gigaword-50"
DEFAULT_DATA_DIR = Path.home() / "gensim-data"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "assets" / "glove-embedding-space.json"
DIMENSIONS = 50
PROJECTED_DIMENSIONS = 3
DECIMALS_3D = 4
FULL_VOCAB_TOP_N = 5
CHECK_TOLERANCE = 5e-5

# Curated vocabulary, one list per visible cluster. Every word the page quotes is here.
GROUPS: dict[str, tuple[str, list[str]]] = {
    "royalty-and-gender": (
        "Royalty and gendered pairs",
        ["king", "queen", "man", "woman", "prince", "princess", "boy", "girl", "brother", "sister",
         "father", "mother", "son", "daughter", "husband", "wife", "uncle", "aunt", "nephew", "niece",
         "actor", "actress", "emperor", "empress", "lord", "lady", "he", "she", "throne", "crown",
         "kingdom", "monarch", "royal"],
    ),
    "countries": (
        "Countries",
        ["france", "italy", "germany", "spain", "japan", "china", "russia", "england", "egypt",
         "greece", "canada", "india", "brazil", "australia", "portugal", "sweden", "poland",
         "turkey", "mexico", "kenya"],
    ),
    "capitals": (
        "Capital and major cities",
        ["paris", "rome", "berlin", "madrid", "tokyo", "beijing", "moscow", "london", "cairo",
         "athens", "ottawa", "delhi", "brasilia", "canberra", "lisbon", "stockholm", "warsaw",
         "ankara", "nairobi", "milan", "turin", "naples", "florence"],
    ),
    "numbers": (
        "Numbers",
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "twenty", "hundred", "thousand", "million"],
    ),
    "verbs": (
        "Verbs and their tenses",
        ["walk", "walked", "walking", "run", "ran", "running", "swim", "swam", "swimming",
         "go", "went", "going", "eat", "ate", "eating", "see", "saw", "seeing", "write",
         "wrote", "writing", "speak", "spoke", "speaking", "take", "took", "taking"],
    ),
    "animals": (
        "Animals",
        ["cat", "dog", "kitten", "puppy", "horse", "rabbit", "cow", "pig", "lion", "tiger",
         "mouse", "wolf", "bird", "fish", "sheep", "elephant"],
    ),
    "adjectives": (
        "Adjectives and comparatives",
        ["good", "better", "best", "bad", "worse", "worst", "great", "big", "bigger", "biggest",
         "small", "smaller", "smallest", "happy", "sad", "fast", "slow"],
    ),
    "other": (
        "Other words the page uses",
        ["democracy", "freedom", "government", "ice", "steam", "solid", "gas", "water", "fashion",
         "bank", "river", "money", "doctor", "nurse", "computer", "programmer", "homemaker"],
    ),
}

# Analogy presets (a - b + c, written as b is to a as c is to ?): gensim positive=[a, c], negative=[b].
# `expected` is the answer a human would give; the explorer reports where it actually ranks.
ANALOGY_PRESETS: list[dict[str, str]] = [
    {"positive1": "king", "negative": "man", "positive2": "woman", "expected": "queen", "label": "king − man + woman"},
    {"positive1": "paris", "negative": "france", "positive2": "italy", "expected": "rome", "label": "paris − france + italy"},
    {"positive1": "berlin", "negative": "germany", "positive2": "japan", "expected": "tokyo", "label": "berlin − germany + japan"},
    {"positive1": "walked", "negative": "walk", "positive2": "swim", "expected": "swam", "label": "walked − walk + swim"},
    {"positive1": "bigger", "negative": "big", "positive2": "small", "expected": "smaller", "label": "bigger − big + small"},
    {"positive1": "actress", "negative": "actor", "positive2": "prince", "expected": "princess", "label": "actress − actor + prince"},
]

# The numbers the page prints in "Code 2", asserted before anything is written.
PAGE_COSINES: list[tuple[str, str, float]] = [
    ("cat", "dog", 0.9218), ("cat", "kitten", 0.6386), ("cat", "democracy", 0.0368),
    ("king", "queen", 0.7839), ("good", "great", 0.7983), ("good", "bad", 0.7965),
]
PAGE_ANALOGIES: list[tuple[str, str, str, list[tuple[str, float]]]] = [
    ("king", "woman", "man", [("queen", 0.8524), ("throne", 0.7664), ("prince", 0.7592)]),
    ("paris", "italy", "france", [("rome", 0.8466), ("milan", 0.7766), ("turin", 0.7666)]),
]


@dataclass(frozen=True)
class Embeddings:
    """The pretrained vectors: one row per word, rows L2-normalized for cosine work."""

    words: list[str]
    index: dict[str, int]
    raw_rows: list[str]
    unit: np.ndarray


def load_glove(data_dir: Path) -> Embeddings:
    """Read gensim-data's word2vec-format text file (header line, then `word v1 … v50`)."""
    path = data_dir / MODEL_NAME / f"{MODEL_NAME}.gz"
    words: list[str] = []
    raw_rows: list[str] = []
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        header = handle.readline().split()
        if int(header[1]) != DIMENSIONS:
            raise ValueError(f"expected {DIMENSIONS}-d vectors in {path}, header says {header}")
        for line in handle:
            word, _, values = line.rstrip("\n").partition(" ")
            words.append(word)
            raw_rows.append(values)
    vectors = np.array([np.array(row.split(), dtype=np.float32) for row in raw_rows])
    unit = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
    return Embeddings(words=words, index={w: i for i, w in enumerate(words)}, raw_rows=raw_rows, unit=unit)


def cosine(embeddings: Embeddings, a: str, b: str) -> float:
    """Cosine similarity of two words in the full 50-d space."""
    return float(embeddings.unit[embeddings.index[a]] @ embeddings.unit[embeddings.index[b]])


def most_similar(embeddings: Embeddings, positive: list[str], negative: list[str], top_n: int) -> list[tuple[str, float]]:
    """gensim's `most_similar`: mean of signed unit vectors, normalized, ranked by cosine, inputs excluded."""
    signed = [embeddings.unit[embeddings.index[w]] for w in positive] + [-embeddings.unit[embeddings.index[w]] for w in negative]
    direction = np.mean(signed, axis=0)
    direction /= np.linalg.norm(direction)
    scores = embeddings.unit @ direction
    excluded = {embeddings.index[w] for w in positive + negative}
    ranked = [i for i in np.argsort(-scores) if i not in excluded][:top_n]
    return [(embeddings.words[i], round(float(scores[i]), 4)) for i in ranked]


def verify_page_numbers(embeddings: Embeddings) -> None:
    """Fail loudly if this data would contradict a number the page prints."""
    for a, b, expected in PAGE_COSINES:
        actual = cosine(embeddings, a, b)
        assert abs(actual - expected) < CHECK_TOLERANCE, f"cos({a}, {b}) = {actual:.4f}, page says {expected}"
    for p1, p2, neg, expected in PAGE_ANALOGIES:
        actual = most_similar(embeddings, [p1, p2], [neg], top_n=len(expected))
        for (word, score), (want_word, want_score) in zip(actual, expected, strict=True):
            assert word == want_word and abs(score - want_score) < CHECK_TOLERANCE, f"{p1}+{p2}-{neg}: {actual} vs page {expected}"


def curated_words(embeddings: Embeddings) -> list[tuple[str, str]]:
    """(word, group id) for every curated word, in group order, each word once."""
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for group_id, (_, words) in GROUPS.items():
        for word in words:
            if word in embeddings.index and word not in seen:
                seen.add(word)
                out.append((word, group_id))
    missing = [w for _, (_, ws) in GROUPS.items() for w in ws if w not in embeddings.index]
    if missing:
        raise KeyError(f"curated words missing from {MODEL_NAME}: {missing}")
    return out


def pca_3d(unit_rows: np.ndarray) -> tuple[np.ndarray, list[float]]:
    """Project the curated unit vectors onto their top three principal components (SVD of the centred matrix)."""
    centred = unit_rows - unit_rows.mean(axis=0)
    _, singular_values, components = np.linalg.svd(centred, full_matrices=False)
    variance = singular_values**2
    explained = (variance[:PROJECTED_DIMENSIONS] / variance.sum()).tolist()
    coordinates = centred @ components[:PROJECTED_DIMENSIONS].T
    coordinates /= np.abs(coordinates).max()  # fit the cloud inside [-1, 1]^3
    return coordinates, [round(v, 4) for v in explained]


def build_space(embeddings: Embeddings) -> dict[str, object]:
    """Assemble the explorer's JSON document."""
    words = curated_words(embeddings)
    rows = np.array([embeddings.unit[embeddings.index[w]] for w, _ in words])
    coordinates, explained = pca_3d(rows)
    analogies = []
    for preset in ANALOGY_PRESETS:
        positive = [preset["positive1"], preset["positive2"]]
        full = most_similar(embeddings, positive, [preset["negative"]], top_n=len(embeddings.words))
        expected_rank = next(rank for rank, (w, _) in enumerate(full, start=1) if w == preset["expected"])
        analogies.append({
            **preset,
            "fullVocabularyTop": [{"word": w, "cosine": s} for w, s in full[:FULL_VOCAB_TOP_N]],
            "expectedFullVocabularyRank": expected_rank,
        })
    return {
        "source": {
            "model": MODEL_NAME,
            "description": "GloVe 6B, 50 dimensions, trained on Wikipedia 2014 + Gigaword 5 (400,000 words)",
            "vocabularySize": len(embeddings.words),
            "url": "https://nlp.stanford.edu/projects/glove/",
        },
        "dimensions": DIMENSIONS,
        "projection": {"method": "PCA on the curated words' unit vectors", "explainedVariance": explained},
        "groups": [{"id": gid, "label": label} for gid, (label, _) in GROUPS.items()],
        "words": [
            {
                "word": w,
                "group": gid,
                "xyz": [round(float(c), DECIMALS_3D) for c in coordinates[k]],
                # The file's own decimal strings: exact, so the browser's cosines equal the page's.
                "vector": [float(v) for v in embeddings.raw_rows[embeddings.index[w]].split()],
            }
            for k, (w, gid) in enumerate(words)
        ],
        "analogies": analogies,
    }


def main() -> None:
    data_dir = Path(os.environ.get("GENSIM_DATA_DIR", DEFAULT_DATA_DIR))
    embeddings = load_glove(data_dir)
    verify_page_numbers(embeddings)
    space = build_space(embeddings)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(space, separators=(",", ":")) + "\n", encoding="utf-8")
    explained = space["projection"]["explainedVariance"]  # type: ignore[index]
    print(f"wrote {OUTPUT_PATH.name}: {len(space['words'])} words, 3-D PCA explains {sum(explained):.1%}")  # type: ignore[arg-type]
    for preset in space["analogies"]:  # type: ignore[union-attr]
        print(f"  {preset['label']:<26} -> {preset['fullVocabularyTop'][:3]}")


if __name__ == "__main__":
    main()
