"""Dynamic INT8 post-training quantization on CPU, measured honestly.

Builds a small multilayer perceptron, quantizes its Linear layers to INT8 with PyTorch's
dynamic post-training quantization (weights stored as int8 ahead of time, activations
quantized on the fly), and reports three numbers for both models:

- size: bytes of the serialized state dict;
- latency: mean wall-clock time of one forward pass over a 64-row batch;
- agreement: the share of inputs on which the INT8 model still picks the same class as the
  FP32 model. Agreement is the stand-in for "quality held" when there are no labels.

The point of the script is the honesty of the latency column. On a model this small, the
quantize/dequantize overhead can outweigh the cheaper matrix multiply, so INT8 may be slower
than FP32 even though it is about four times smaller. The memory win is unconditional; the
speed win depends on the model size and the integer kernels of the target hardware.

Runs offline on CPU in a few seconds; downloads nothing.

Run:
    uv run --python 3.12 --with torch python dynamic_int8_on_cpu.py
"""

from __future__ import annotations

import copy
import io
import time

import torch
from torch import nn

SEED = 0
INPUT_FEATURES = 256
HIDDEN_FEATURES = 512
CLASS_COUNT = 10
EVAL_ROWS = 512
LATENCY_BATCH_ROWS = 64
LATENCY_ITERATIONS = 50
BYTES_PER_MEGABYTE = 1e6
MILLISECONDS_PER_SECOND = 1e3
# qnnpack exists on ARM and x86; fbgemm/x86 are x86-only. Try them in this order.
PREFERRED_ENGINES = ("qnnpack", "x86", "fbgemm")


class ReviewSorter(nn.Module):
    """A small classifier head of the kind that ships behind an API."""

    def __init__(self) -> None:
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(INPUT_FEATURES, HIDDEN_FEATURES),
            nn.ReLU(),
            nn.Linear(HIDDEN_FEATURES, HIDDEN_FEATURES),
            nn.ReLU(),
            nn.Linear(HIDDEN_FEATURES, CLASS_COUNT),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        return self.layers(features)


def select_quantized_engine() -> str:
    """Pick an INT8 kernel backend this machine actually supports."""
    supported = torch.backends.quantized.supported_engines
    for engine in PREFERRED_ENGINES:
        if engine in supported:
            torch.backends.quantized.engine = engine
            return engine
    raise RuntimeError(f"no INT8 engine available; supported engines: {supported}")


def serialized_size_megabytes(model: nn.Module) -> float:
    """Size of the state dict as torch.save would write it to disk."""
    buffer = io.BytesIO()
    torch.save(model.state_dict(), buffer)
    return buffer.getbuffer().nbytes / BYTES_PER_MEGABYTE


@torch.no_grad()
def mean_latency_milliseconds(model: nn.Module, batch: torch.Tensor) -> float:
    """Mean forward-pass time after one warm-up call."""
    model(batch)
    started = time.perf_counter()
    for _ in range(LATENCY_ITERATIONS):
        model(batch)
    elapsed = time.perf_counter() - started
    return elapsed / LATENCY_ITERATIONS * MILLISECONDS_PER_SECOND


@torch.no_grad()
def agreement_percent(model: nn.Module, inputs: torch.Tensor, reference: torch.Tensor) -> float:
    """Share of inputs where the model's argmax matches the FP32 reference decision."""
    decisions = model(inputs).argmax(dim=1)
    return (decisions == reference).float().mean().item() * 100


def main() -> None:
    torch.manual_seed(SEED)
    engine = select_quantized_engine()

    fp32_model = ReviewSorter().eval()
    eval_inputs = torch.randn(EVAL_ROWS, INPUT_FEATURES)
    with torch.no_grad():
        reference_decisions = fp32_model(eval_inputs).argmax(dim=1)

    int8_model = torch.ao.quantization.quantize_dynamic(
        copy.deepcopy(fp32_model), {nn.Linear}, dtype=torch.qint8
    ).eval()

    latency_batch = eval_inputs[:LATENCY_BATCH_ROWS]
    print(f"torch {torch.__version__} · INT8 engine: {engine}")
    print(f"{'model':<8}{'size (MB)':>12}{'latency (ms)':>15}{'agreement %':>14}")
    sizes = {}
    for name, model in (("fp32", fp32_model), ("int8", int8_model)):
        sizes[name] = serialized_size_megabytes(model)
        latency = mean_latency_milliseconds(model, latency_batch)
        agreement = agreement_percent(model, eval_inputs, reference_decisions)
        print(f"{name:<8}{sizes[name]:>12.3f}{latency:>15.3f}{agreement:>14.1f}")

    int8_agreement = agreement_percent(int8_model, eval_inputs, reference_decisions)
    print(f"\nsize reduction   : {sizes['fp32'] / sizes['int8']:.2f}x smaller")
    print(f"decisions changed: {100 - int8_agreement:.1f}% of {EVAL_ROWS} inputs")


if __name__ == "__main__":
    main()
