---
title: "Build the Transformer"
id: lr-slm-build-the-transformer
minutes: 30
core_idea: "A current small language model is six choices — pre-normalisation, RMSNorm, rotary positions, fused causal attention, a gated feed-forward block and tied embeddings — and each one replaced something from the 2017 paper for a reason you can state."
builds_on: [lr-slm-train-a-tokenizer]
leads_to: [lr-slm-prove-the-gradient-path]
related: [ait-inf-kv-cache]
section: "ai-ml-learning-resources"
workflow: "build-a-small-language-model"
chapter: 4
status: complete
template: workflow
category: model-building
---

# Build the Transformer

The architecture is about two hundred lines. What makes it worth two hundred lines rather than one
import is that **every component in a current small model replaced something from the original
paper**, and each replacement has a reason you can state in a sentence.

| Component | Original transformer | Here | Why |
|---|---|---|---|
| Normalisation position | after each sub-layer | **before** | the residual stream stays an unobstructed path |
| Normalisation | LayerNorm | **RMSNorm** | the mean subtraction bought nothing; the scale is what mattered |
| Position | learned or sinusoidal, added to the input | **rotary, applied to queries and keys** | attention depends on *distance*, and there is no table to run out of |
| Attention | explicit softmax and mask | **fused, `is_causal=True`** | the mask is never materialised, and the kernel is chosen per device |
| Feed-forward | two layers, ReLU | **gated, SiLU (SwiGLU)** | more quality per parameter |
| Output projection | its own matrix | **tied to the embedding** | at this scale that matrix would be most of the model |

The rest of this chapter is those six sentences, expanded.

---

## The residual stream, and why normalisation moved

Read the block first:

```python
def forward(self, x: Tensor, cos: Tensor, sin: Tensor) -> Tensor:
    """Add each sub-layer's output to the residual stream."""
    x = x + self.attention(self.attention_norm(x), cos, sin)
    return x + self.feedforward(self.feedforward_norm(x))
```

Each sub-layer reads a *normalised copy* of the stream and adds its result back to the **unmodified**
stream. Nothing sits between the embedding and the final norm except additions.

Post-normalisation puts a normalisation between every pair of blocks, so the gradient reaching layer
one has passed through a dozen of them. That is why deep post-norm transformers need a careful
warmup to train at all, and why pre-norm ones mostly do not.

**One consequence to remember:** the residual stream's variance grows with depth, because every block
adds two terms to it. The fix is at initialisation:

```python
scale = 1.0 / math.sqrt(2 * self.config.n_layer)
writes_to_residual = ("attention.proj.weight", "feedforward.down.weight")
with torch.no_grad():
    for name, parameter in self.named_parameters():
        if name.endswith(writes_to_residual):
            parameter.mul_(scale)
```

Shrink the two projections that *write* into the stream by one over the square root of twice the
depth, and the variance is flat from the first step instead of being unlearned over the first few
hundred.

---

## RMSNorm: the half of LayerNorm that was doing the work

```python
def forward(self, x: Tensor) -> Tensor:
    """Scale each position to unit root-mean-square, then apply the learned gain."""
    normalized = x * torch.rsqrt(x.pow(2).mean(dim=-1, keepdim=True) + self.eps)
    return normalized * self.weight
```

LayerNorm subtracts the mean, divides by the standard deviation, scales and shifts. RMSNorm divides
by the root-mean-square and scales. **The mean subtraction and the bias are gone**, and models train
just as well without them — which is the whole finding. One fewer reduction per call, fewer
parameters, same behaviour.

---

## Rotary positions: distance instead of place

The original transformer *adds* a position vector to the input embedding. Rotary embeddings
**rotate** the query and key vectors instead, by an angle proportional to position.

```python
def apply_rope(x: Tensor, cos: Tensor, sin: Tensor) -> Tensor:
    """Rotate channel pairs of ``x`` by the angle for their position."""
    time = x.shape[-2]
    cos_t = cos[:time].unsqueeze(0).unsqueeze(0)
    sin_t = sin[:time].unsqueeze(0).unsqueeze(0)
    even = x[..., 0::2]
    odd = x[..., 1::2]
    rotated_even = even * cos_t - odd * sin_t
    rotated_odd = even * sin_t + odd * cos_t
    return torch.stack((rotated_even, rotated_odd), dim=-1).flatten(-2)
```

Channels are treated as two-dimensional pairs and each pair is rotated in its own plane. The
property that makes this work is one line of trigonometry: **the dot product of a query rotated by
angle *a* and a key rotated by angle *b* depends only on *a − b*.**

Attention scores therefore depend on the *distance* between two tokens, never on where the pair sits
in the window. The project asserts exactly that:

```python
def test_rotary_dot_product_depends_on_distance_not_position() -> None:
    """Two vectors four positions apart score the same wherever that pair sits in the window."""
    ...
    assert score(0, 4) == pytest.approx(score(5, 9), abs=1e-4)
```

Frequencies fall geometrically across the head dimension, so the first channel pairs rotate quickly
and encode local order while the last rotate slowly and encode long-range position.

```python
inverse_frequency = 1.0 / (
    theta ** (torch.arange(0, head_dim, 2, dtype=torch.float32, device=device) / head_dim)
)
```

And a rotation changes direction but never magnitude, which is why nothing has to be re-normalised
afterwards — also a test.

---

## Attention: let the kernel do it

```python
def forward(self, x: Tensor, cos: Tensor, sin: Tensor) -> Tensor:
    batch, time, channels = x.shape
    q, k, v = self.qkv(x).split(channels, dim=2)
    q = q.view(batch, time, self.n_head, self.head_dim).transpose(1, 2)
    k = k.view(batch, time, self.n_head, self.head_dim).transpose(1, 2)
    v = v.view(batch, time, self.n_head, self.head_dim).transpose(1, 2)
    q = apply_rope(q, cos, sin)
    k = apply_rope(k, cos, sin)
    attended = F.scaled_dot_product_attention(q, k, v, is_causal=True)
    merged = attended.transpose(1, 2).contiguous().view(batch, time, channels)
    return self.proj(merged)
```

One projection produces all three of query, key and value — one matrix multiply instead of three.
`is_causal=True` applies the mask without materialising a `time × time` boolean, and PyTorch selects
the best available kernel for the device.

**Causality is a correctness property, not a performance one**, and it is worth testing rather than
assuming: change the last token of a sequence and every earlier position's logits must be identical.

```python
original, _ = tiny_model(idx)
perturbed, _ = tiny_model(changed)
assert torch.allclose(original[:, :-1], perturbed[:, :-1], atol=1e-5)
```

A model that leaks the future trains beautifully and generates nonsense — it learned to read an
answer that is not there at inference time.

---

## The gated feed-forward block

```python
class SwiGLU(nn.Module):
    def __init__(self, config: ModelConfig) -> None:
        super().__init__()
        hidden = _round_to_multiple(int(8 * config.n_embd / 3), 64)
        self.gate = nn.Linear(config.n_embd, hidden, bias=False)
        self.up = nn.Linear(config.n_embd, hidden, bias=False)
        self.down = nn.Linear(hidden, config.n_embd, bias=False)

    def forward(self, x: Tensor) -> Tensor:
        """Gate the up-projection with a SiLU-activated twin, then project back down."""
        return self.down(F.silu(self.gate(x)) * self.up(x))
```

Two projections up, one gating the other, one projection down. The `8/3` width is arithmetic rather
than taste: a gated block has three matrices where a plain block has two, so two-thirds of the
plain block's four-times width keeps the parameter count level. Rounding to a multiple of 64 keeps
the shapes kernel-friendly.

---

## Tied embeddings

```python
self.lm_head.weight = self.embedding.weight
```

One matrix, used twice: as the input lookup and as the output projection. At `vocab_size=4096` and
`n_embd=384` that saves 1.57 million parameters — **13% of this model**. It also ties the two views
of "what a token means", which is a reasonable prior and empirically not a cost.

---

## What is deliberately absent

- **Dropout.** One pass over a small corpus is not the regime where it helps, and it would confuse
  the overfitting story the next chapters measure.
- **Biases.** They cost parameters and buy nothing here.
- **A key-value cache.** Generation at 256 tokens is fast enough without one, and a cache belongs to
  a serving path rather than to the model. That trade is covered in
  [KV Cache](/ai-ml/ai-buzzwords/inference-serving-and-efficiency/kv-cache).

---

## The parameter count, worked out

```text
embedding (tied)        4096 × 384                    = 1,572,864
per block:
  qkv                    384 × 1152                   =   442,368
  attention projection   384 × 384                    =   147,456
  gate / up              384 × 1024, twice            =   786,432
  down                  1024 × 384                    =   393,216
  two norms              384 × 2                      =       768
                                                       ---------
                                                        1,770,240  × 6 blocks = 10,621,440
final norm                                                    384
                                                       ---------
total                                                  12,194,688
```

Which is what the project prints:

```text
training: 12,194,688 parameters (10,621,824 non-embedding); ...
```

Being able to derive that number from the configuration is worth more than it sounds. It is how you
answer "will this fit" before you find out the hard way, and how you notice that at this width the
embedding table is 13% of the model rather than 60%.

## Pitfalls

- **Post-normalisation by habit.** It makes deep stacks need a warmup crutch.
- **Skipping the residual-projection rescaling.** Early training is then spent undoing variance
  growth.
- **Adding positions to the input while also rotating.** Pick one.
- **Assuming causality instead of testing it.** A leak trains fine and generates nonsense.
- **Untying embeddings at small scale.** The output matrix becomes a large share of the model for no
  measured gain.

## Key takeaways

- **Pre-normalisation keeps the residual stream unobstructed**, and the write projections are scaled
  at initialisation to keep its variance flat with depth.
- **RMSNorm is LayerNorm with the part that did nothing removed.**
- **Rotary positions make attention depend on distance**, and the rotation preserves magnitude.
- **`is_causal=True` gets the mask and the fastest kernel** without materialising either.
- **A gated feed-forward block at 8/3 width** matches a plain block's parameters and beats its
  quality.
- **Tied embeddings save 13% of this model**, and the count is derivable from the config.

## References

- The implementation: `slmkit/model/transformer.py` in
  [small-language-model](/python/python-production-examples/small-language-model/readme)
- Vaswani et al., *Attention Is All You Need*: <https://arxiv.org/abs/1706.03762>
- Zhang and Sennrich, *Root Mean Square Layer Normalization*: <https://arxiv.org/abs/1910.07467>
- Su et al., *RoFormer: Enhanced Transformer with Rotary Position Embedding*:
  <https://arxiv.org/abs/2104.09864>
- Shazeer, *GLU Variants Improve Transformer* — where the 8/3 width comes from:
  <https://arxiv.org/abs/2002.05202>
- Press and Wolf, *Using the Output Embedding to Improve Language Models*:
  <https://arxiv.org/abs/1608.05859>
