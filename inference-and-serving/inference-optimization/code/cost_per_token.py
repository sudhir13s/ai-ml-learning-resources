"""Dollars per million output tokens for self-hosted decode, derived from the roofline model.

The serving page derives decode throughput from named A100 / Llama-3-8B constants
(inference_serving.py). A rented GPU is billed per hour whether it emits 125 tokens/s or
19,500, so the same throughput curve IS a cost curve:

    $/1M tokens = GPU $/hour / (throughput tok/s * 3600 s/hour) * 1e6

Every number printed here is MODELED: the hardware constants come from inference_serving.py,
and the $2/hour rental rate is an illustrative round number, not a quote. Change
GPU_DOLLARS_PER_HOUR to your own rate and every row re-prices.

Run:
    python cost_per_token.py
"""

from __future__ import annotations

from dataclasses import dataclass

from inference_serving import (
    BATCH_SIZES,
    ROOFLINE_CONTEXT_TOKENS,
    decode_step_time_s,
    roofline_crossover_batch,
)

GPU_DOLLARS_PER_HOUR = 2.0     # illustrative A100 rental rate (modeled, not a price quote)
SECONDS_PER_HOUR = 3600
TOKENS_PER_MILLION = 1e6
LONG_CONTEXT_TOKENS = 2048     # the page's long-context case, where decode never turns compute-bound
UTILIZATION_LEVELS = (1.0, 0.5, 0.25)  # share of paid hours the GPU spends decoding


@dataclass(frozen=True)
class CostRow:
    """One batch size priced at one context length."""

    batch: int
    throughput_tok_per_s: float
    dollars_per_million: float


def throughput_tok_per_s(batch: int, context_tokens: int) -> float:
    """Modeled decode throughput: B tokens per step divided by the slower of memory and compute."""
    memory_time, compute_time = decode_step_time_s(batch, context_tokens)
    return batch / max(memory_time, compute_time)


def dollars_per_million_tokens(throughput: float, utilization: float = 1.0) -> float:
    """Price a million tokens: the hourly bill spread over the tokens actually produced that hour."""
    assert 0 < utilization <= 1, "utilization is a fraction of paid hours in (0, 1]"
    tokens_per_paid_hour = throughput * SECONDS_PER_HOUR * utilization
    return GPU_DOLLARS_PER_HOUR / tokens_per_paid_hour * TOKENS_PER_MILLION


def cost_table(context_tokens: int) -> list[CostRow]:
    """Cost rows over the page's batch sweep at one context length (full utilization)."""
    rows = []
    for batch in BATCH_SIZES:
        throughput = throughput_tok_per_s(batch, context_tokens)
        rows.append(CostRow(batch, throughput, dollars_per_million_tokens(throughput)))
    return rows


def _verify_claims(short: list[CostRow], long: list[CostRow]) -> None:
    """The lessons the page states, checked before any number is printed."""
    costs = [row.dollars_per_million for row in short]
    assert all(a > b for a, b in zip(costs, costs[1:-1])), "cost must fall while decode is memory-bound"
    assert abs(costs[-1] - costs[-2]) / costs[-1] < 1e-9, "cost must flatten past the compute roofline"
    assert all(lo.dollars_per_million > sh.dollars_per_million for lo, sh in zip(long[1:], short[1:])), (
        "longer context must cost more per token at the same batch (more KV bytes per step)"
    )


def main() -> None:
    short = cost_table(ROOFLINE_CONTEXT_TOKENS)
    long = cost_table(LONG_CONTEXT_TOKENS)
    _verify_claims(short, long)

    print(f"All values MODELED: A100 / Llama-3-8B constants, GPU at ${GPU_DOLLARS_PER_HOUR:.2f}/hour.\n")
    print(f"{'batch':>6} | {'tok/s @256':>11} | {'$/1M @256':>10} | {'tok/s @2048':>12} | {'$/1M @2048':>11}")
    print("-" * 64)
    for sh, lo in zip(short, long):
        print(f"{sh.batch:>6} | {sh.throughput_tok_per_s:>11.0f} | {sh.dollars_per_million:>10.4f} | "
              f"{lo.throughput_tok_per_s:>12.0f} | {lo.dollars_per_million:>11.4f}")

    crossover = roofline_crossover_batch(ROOFLINE_CONTEXT_TOKENS)
    floor_cost = short[-1].dollars_per_million
    print(f"\ncost floor at the compute roofline (B* = {crossover:.0f}): ${floor_cost:.4f} per 1M tokens")
    print(f"batch 1 costs {short[0].dollars_per_million / floor_cost:.0f}x the floor")

    print("\nIdle hours are still billed -- batch 128 at 256-token context:")
    throughput_128 = next(row.throughput_tok_per_s for row in short if row.batch == 128)
    for utilization in UTILIZATION_LEVELS:
        cost = dollars_per_million_tokens(throughput_128, utilization)
        print(f"  utilization {utilization:>4.0%}: ${cost:.4f} per 1M tokens")


if __name__ == "__main__":
    main()
