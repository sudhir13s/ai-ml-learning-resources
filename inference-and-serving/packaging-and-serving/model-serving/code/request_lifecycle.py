"""One LLM request through a paged-KV serving engine, worked as arithmetic.

Traces a 600-token prompt and a 50-token answer on a Mistral-7B-shaped model:
the blocks the engine allocates and frees, the latency clock the user feels,
how much of a 24 GB GPU is left for the KV cache at each weight precision, and
the memory bill for serving five LoRA tenants. Plain Python on purpose: every
number is a product of model shape and engine settings, so no GPU is needed.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

GB = 1e9
MB = 1e6
PROMPT_TOKENS = 600
OUTPUT_TOKENS = 50
TTFT_MS = 180.0
TPOT_MS = 22.0
LONG_CONTEXT_TOKENS = 8192
LORA_RANK = 32
LORA_TENANTS = 5


@dataclass(frozen=True)
class ModelShape:
    name: str
    parameters: float
    layers: int
    hidden: int
    mlp_hidden: int
    kv_heads: int
    head_dim: int


@dataclass(frozen=True)
class EngineSettings:
    block_size_tokens: int = 16            # vLLM default block size
    kv_bytes_per_element: int = 2          # FP16 / BF16 cache
    gpu_memory_gb: float = 24.0
    gpu_memory_utilization: float = 0.90   # vLLM --gpu-memory-utilization
    runtime_overhead_gb: float = 1.5       # CUDA context, activations, graphs (assumed)


@dataclass(frozen=True)
class BlockEvent:
    event: str
    tokens_in_cache: int
    blocks_held: int


@dataclass(frozen=True)
class VramBudget:
    precision: str
    weights_gb: float
    kv_cache_gb: float
    concurrent_long_requests: int


MISTRAL_7B = ModelShape("Mistral-7B", parameters=7.24e9, layers=32, hidden=4096,
                        mlp_hidden=14336, kv_heads=8, head_dim=128)
ENGINE = EngineSettings()
BITS_PER_WEIGHT = {"FP16": 16.0, "INT8": 8.0, "INT4 (AWQ, group 128)": 4.25}


def kv_bytes_per_token(model: ModelShape, engine: EngineSettings) -> int:
    """A key and a value vector, in every layer, for one token."""
    return 2 * model.layers * model.kv_heads * model.head_dim * engine.kv_bytes_per_element


def blocks_for(tokens: int, engine: EngineSettings) -> int:
    return math.ceil(tokens / engine.block_size_tokens)


def trace_request(prompt_tokens: int, output_tokens: int, engine: EngineSettings) -> list[BlockEvent]:
    """Every moment the request's block count changes, from prefill to EOS."""
    held = blocks_for(prompt_tokens, engine)
    events = [BlockEvent("prefill writes the prompt", prompt_tokens, held)]
    # Output token k enters the cache when it is fed back to produce token k+1,
    # so the last token is never cached: the cache peaks at prompt + output - 1.
    for generated in range(1, output_tokens):
        cached = prompt_tokens + generated
        if blocks_for(cached, engine) > held:
            held = blocks_for(cached, engine)
            events.append(BlockEvent(f"output token {generated + 1} needs a new block", cached, held))
    events.append(BlockEvent("EOS returns every block to the pool", prompt_tokens + output_tokens - 1, held))
    return events


def end_to_end_ms(ttft_ms: float, tpot_ms: float, output_tokens: int) -> float:
    """The first token arrives at TTFT; each later token costs one TPOT."""
    return ttft_ms + tpot_ms * (output_tokens - 1)


def vram_budget(model: ModelShape, engine: EngineSettings, precision: str, context_tokens: int) -> VramBudget:
    weights_gb = model.parameters * BITS_PER_WEIGHT[precision] / 8 / GB
    usable_gb = engine.gpu_memory_gb * engine.gpu_memory_utilization
    kv_cache_gb = usable_gb - weights_gb - engine.runtime_overhead_gb
    per_request_gb = kv_bytes_per_token(model, engine) * context_tokens / GB
    concurrent = max(0, math.floor(kv_cache_gb / per_request_gb))
    return VramBudget(precision, weights_gb, kv_cache_gb, concurrent)


def lora_adapter_mb(model: ModelShape, rank: int) -> float:
    """Rank-r A and B matrices on all seven linear projections of every layer, FP16."""
    kv_width = model.kv_heads * model.head_dim
    shapes = [
        (model.hidden, model.hidden), (model.hidden, kv_width), (model.hidden, kv_width),
        (model.hidden, model.hidden), (model.hidden, model.mlp_hidden),
        (model.hidden, model.mlp_hidden), (model.mlp_hidden, model.hidden),
    ]
    per_layer = sum(rank * (fan_in + fan_out) for fan_in, fan_out in shapes)
    return per_layer * model.layers * 2 / MB


def print_lifecycle() -> None:
    per_token = kv_bytes_per_token(MISTRAL_7B, ENGINE)
    block_mb = per_token * ENGINE.block_size_tokens / MB
    print(f"KV cache per token : {per_token:,} bytes ({per_token / 1024:.0f} KiB)")
    print(f"one 16-token block : {block_mb:.2f} MB")
    print("\n== block timeline for one request ==")
    for step in trace_request(PROMPT_TOKENS, OUTPUT_TOKENS, ENGINE):
        size_mb = step.blocks_held * block_mb
        print(f"  {step.event:<38} cache={step.tokens_in_cache:>4} tokens  "
              f"blocks={step.blocks_held:>2}  ({size_mb:5.1f} MB)")
    total_ms = end_to_end_ms(TTFT_MS, TPOT_MS, OUTPUT_TOKENS)
    print(f"\nfirst token at {TTFT_MS:.0f} ms; last of {OUTPUT_TOKENS} tokens at {total_ms:,.0f} ms")


def print_budgets() -> None:
    print(f"\n== 24 GB GPU at utilization {ENGINE.gpu_memory_utilization}, "
          f"{LONG_CONTEXT_TOKENS}-token requests ==")
    for precision in BITS_PER_WEIGHT:
        budget = vram_budget(MISTRAL_7B, ENGINE, precision, LONG_CONTEXT_TOKENS)
        print(f"  {precision:<22} weights={budget.weights_gb:5.2f} GB  "
              f"kv={budget.kv_cache_gb:5.2f} GB  concurrent={budget.concurrent_long_requests}")


def print_lora_bill() -> None:
    adapter_mb = lora_adapter_mb(MISTRAL_7B, LORA_RANK)
    base_gb = MISTRAL_7B.parameters * 2 / GB
    separate_gb = LORA_TENANTS * base_gb
    shared_gb = base_gb + LORA_TENANTS * adapter_mb / 1000
    print(f"\n== {LORA_TENANTS} LoRA tenants, rank {LORA_RANK}, all linear layers ==")
    print(f"  one adapter            : {adapter_mb:.0f} MB")
    print(f"  {LORA_TENANTS} full model copies    : {separate_gb:.1f} GB")
    print(f"  1 base + {LORA_TENANTS} adapters    : {shared_gb:.1f} GB")


def main() -> None:
    print_lifecycle()
    print_budgets()
    print_lora_bill()


if __name__ == "__main__":
    main()
