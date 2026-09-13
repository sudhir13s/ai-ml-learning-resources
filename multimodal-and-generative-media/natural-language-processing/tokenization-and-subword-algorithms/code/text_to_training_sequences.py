"""From text to training sequences with a real tokenizer (tiktoken cl100k_base).

Four things the tokenization page teaches after the algorithms:
  1. encode a string, then decode each id on its own to SEE the pieces;
  2. the leading space belongs to the token, so encoding pieces separately
     does not give the ids of the whole string;
  3. measure characters and words per token on real text;
  4. fit documents to a fixed sequence length: truncate, chunk, or pack
     (with an end-of-text separator between packed documents).

Run:  uv run --python 3.12 --with tiktoken python text_to_training_sequences.py
CPU only, no downloads beyond the tiktoken merge table.
"""

from dataclasses import dataclass

import tiktoken

ENCODING_NAME = "cl100k_base"
SEQUENCE_LENGTH = 16
CHUNK_OVERLAP = 4

SAMPLE_SENTENCE = "Cats are wonderful pets"
PROSE = (
    "Tokenizers are trained once, frozen, and then used as a lookup for the "
    "whole life of the model. Every request you send is billed in tokens, and "
    "every context window is measured in tokens, so it pays to know how many "
    "tokens your text really costs before you design anything around it."
)
DOCUMENTS = [
    "Cats nap in the sun.",
    "Dogs enjoy long walks outdoors.",
    "Birds fly south for the winter when it gets cold.",
    "Fish are quiet pets that can live in a small glass tank for years.",
]


@dataclass(frozen=True)
class PackedBatch:
    """Fixed-length rows plus how many positions hold real tokens."""

    rows: list[list[int]]
    real_token_count: int
    total_positions: int


def show_pieces(encoding: tiktoken.Encoding, text: str) -> None:
    ids = encoding.encode(text)
    pieces = [encoding.decode([token_id]) for token_id in ids]
    print(f"text   : {text!r}")
    print(f"pieces : {pieces}")
    print(f"ids    : {ids}")


def show_leading_space_trap(encoding: tiktoken.Encoding) -> None:
    print(f"'cats'  -> {encoding.encode('cats')}")
    print(f"' cats' -> {encoding.encode(' cats')}")
    whole = encoding.encode("Hello world")
    glued = encoding.encode("Hello") + encoding.encode("world")
    spaced = encoding.encode("Hello") + encoding.encode(" world")
    print(f"encode('Hello world')                  -> {whole}")
    print(f"encode('Hello') + encode('world')       -> {glued}  equal={glued == whole}")
    print(f"encode('Hello') + encode(' world')      -> {spaced}  equal={spaced == whole}")


def show_token_economics(encoding: tiktoken.Encoding, text: str) -> None:
    token_count = len(encoding.encode(text))
    word_count = len(text.split())
    print(f"chars={len(text)} words={word_count} tokens={token_count}")
    print(f"chars/token={len(text) / token_count:.2f}  words/token={word_count / token_count:.2f}")


def truncate(ids: list[int], length: int) -> list[int]:
    return ids[:length]


def chunk(ids: list[int], length: int, overlap: int) -> list[list[int]]:
    stride = length - overlap
    return [ids[start:start + length] for start in range(0, max(1, len(ids) - overlap), stride)]


def pad_each(documents: list[list[int]], length: int, pad_id: int) -> PackedBatch:
    rows = [doc[:length] + [pad_id] * (length - len(doc[:length])) for doc in documents]
    real = sum(min(len(doc), length) for doc in documents)
    return PackedBatch(rows, real, len(rows) * length)


def pack(documents: list[list[int]], length: int, eos_id: int, pad_id: int) -> PackedBatch:
    stream = [token for doc in documents for token in doc + [eos_id]]
    rows = [stream[start:start + length] for start in range(0, len(stream), length)]
    last_real = len(rows[-1])
    rows[-1] = rows[-1] + [pad_id] * (length - last_real)
    return PackedBatch(rows, len(stream), len(rows) * length)


def show_sequence_fitting(encoding: tiktoken.Encoding) -> None:
    long_ids = encoding.encode(PROSE)
    chunks = chunk(long_ids, SEQUENCE_LENGTH, CHUNK_OVERLAP)
    print(f"long document: {len(long_ids)} tokens, sequence length {SEQUENCE_LENGTH}")
    print(f"truncate -> keeps {len(truncate(long_ids, SEQUENCE_LENGTH))} tokens, "
          f"drops {len(long_ids) - SEQUENCE_LENGTH}")
    print(f"chunk    -> {len(chunks)} windows, lengths {[len(c) for c in chunks]}, "
          f"overlap {CHUNK_OVERLAP}")

    eos_id = encoding.eot_token
    documents = [encoding.encode(doc) for doc in DOCUMENTS]
    print(f"short documents: lengths {[len(d) for d in documents]}, EOS id {eos_id}")
    padded = pad_each(documents, SEQUENCE_LENGTH, pad_id=eos_id)
    packed = pack(documents, SEQUENCE_LENGTH, eos_id=eos_id, pad_id=eos_id)
    for name, batch in (("pad ", padded), ("pack", packed)):
        share = batch.real_token_count / batch.total_positions
        print(f"{name} -> {len(batch.rows)} rows x {SEQUENCE_LENGTH} = {batch.total_positions} "
              f"positions, {batch.real_token_count} real ({share:.0%})")
    boundary = packed.rows[0].index(eos_id)
    print(f"packed row 0 decoded: {encoding.decode(packed.rows[0])!r}")
    print(f"first EOS at position {boundary}: the next document starts at {boundary + 1}")


def main() -> None:
    encoding = tiktoken.get_encoding(ENCODING_NAME)
    print("== pieces ==")
    show_pieces(encoding, SAMPLE_SENTENCE)
    print("== leading space ==")
    show_leading_space_trap(encoding)
    print("== token economics ==")
    show_token_economics(encoding, PROSE)
    print("== truncate, chunk, pad, pack ==")
    show_sequence_fitting(encoding)


if __name__ == "__main__":
    main()
