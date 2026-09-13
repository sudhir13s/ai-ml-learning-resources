"""Pipeline-as-code runner for iris-classifier (CPU, offline, standard library only).

The training pipeline is declared as a DAG of named steps with explicit upstream
dependencies. The runner executes it in topological order and caches every step under a
fingerprint of its code version, its parameters and its upstream fingerprints. Re-running
with nothing changed executes nothing; changing one training parameter re-executes only
the steps downstream of it. A transient failure is retried, and a cycle is rejected before
any step runs.

Run:  uv run --python 3.12 python pipeline_dag.py
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, replace
from graphlib import CycleError, TopologicalSorter
from typing import Any, Callable

MAX_ATTEMPTS = 3
FINGERPRINT_CHARS = 10
ACCURACY_FLOOR = 0.90

StepAction = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]


class TransientStepError(RuntimeError):
    """A failure worth retrying: a flaky network read, a pre-empted worker."""


@dataclass(frozen=True)
class Step:
    name: str
    upstream: tuple[str, ...]
    code_version: str
    params: dict[str, Any]
    action: StepAction


@dataclass(frozen=True)
class StepResult:
    name: str
    status: str
    attempts: int
    fingerprint: str
    output: dict[str, Any]


@dataclass
class Orchestrator:
    """Runs a DAG of steps; the cache persists across runs like an artifact store would."""

    cache: dict[str, dict[str, Any]] = field(default_factory=dict)

    def run(self, steps: list[Step], injected_failures: dict[str, int] | None = None
            ) -> list[StepResult]:
        by_name = {step.name: step for step in steps}
        order = TopologicalSorter({s.name: set(s.upstream) for s in steps}).static_order()
        remaining_failures = dict(injected_failures or {})
        fingerprints: dict[str, str] = {}
        outputs: dict[str, dict[str, Any]] = {}
        results = []
        for name in order:
            step = by_name[name]
            fingerprint = self._fingerprint(step, fingerprints)
            fingerprints[name] = fingerprint
            if fingerprint in self.cache:
                outputs[name] = self.cache[fingerprint]
                results.append(StepResult(name, "cached", 0, fingerprint, outputs[name]))
                continue
            upstream_outputs = {parent: outputs[parent] for parent in step.upstream}
            output, attempts = self._execute(step, upstream_outputs, remaining_failures)
            self.cache[fingerprint] = outputs[name] = output
            results.append(StepResult(name, "ran", attempts, fingerprint, output))
        return results

    @staticmethod
    def _fingerprint(step: Step, fingerprints: dict[str, str]) -> str:
        payload = json.dumps({
            "name": step.name,
            "code_version": step.code_version,
            "params": step.params,
            "upstream": [fingerprints[parent] for parent in sorted(step.upstream)],
        }, sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()[:FINGERPRINT_CHARS]

    @staticmethod
    def _execute(step: Step, upstream_outputs: dict[str, Any],
                 remaining_failures: dict[str, int]) -> tuple[dict[str, Any], int]:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                if remaining_failures.get(step.name, 0) > 0:
                    remaining_failures[step.name] -= 1
                    raise TransientStepError(f"{step.name}: worker pre-empted")
                return step.action(upstream_outputs, step.params), attempt
            except TransientStepError:
                if attempt == MAX_ATTEMPTS:
                    raise
        raise AssertionError("unreachable: the loop either returns or raises")


def ingest(_: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
    return {"snapshot": params["snapshot"], "rows": 150}


def validate(upstream: dict[str, Any], _: dict[str, Any]) -> dict[str, Any]:
    rows = upstream["ingest"]["rows"]
    if rows == 0:
        raise ValueError("empty snapshot: refusing to train")
    return {"rows_valid": rows}


def train(upstream: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
    recipe = json.dumps({"rows": upstream["validate"]["rows_valid"], **params}, sort_keys=True)
    return {"weights_sha256": hashlib.sha256(recipe.encode()).hexdigest()[:12]}


def evaluate(upstream: dict[str, Any], _: dict[str, Any]) -> dict[str, Any]:
    digest = upstream["train"]["weights_sha256"]
    return {"accuracy": round(0.90 + int(digest[:2], 16) / 255 * 0.05, 3)}


def register(upstream: dict[str, Any], _: dict[str, Any]) -> dict[str, Any]:
    accuracy = upstream["evaluate"]["accuracy"]
    return {"registered": accuracy >= ACCURACY_FLOOR, "accuracy": accuracy}


def build_pipeline(learning_rate: float) -> list[Step]:
    return [
        Step("ingest", (), "v1", {"snapshot": "iris@2026-09-01"}, ingest),
        Step("validate", ("ingest",), "v1", {}, validate),
        Step("train", ("validate",), "v3", {"lr": learning_rate, "epochs": 20, "seed": 0}, train),
        Step("evaluate", ("train",), "v2", {}, evaluate),
        Step("register", ("evaluate",), "v1", {}, register),
    ]


def print_run(title: str, results: list[StepResult]) -> None:
    print(f"\n== {title} ==")
    print(f"{'step':<9} | {'status':<6} | {'attempts':>8} | {'fingerprint':<11} | output")
    print("-" * 78)
    for result in results:
        print(f"{result.name:<9} | {result.status:<6} | {result.attempts:>8} | "
              f"{result.fingerprint:<11} | {result.output}")


def main() -> None:
    orchestrator = Orchestrator()
    print_run("run 1: cold cache, evaluate pre-empted once",
              orchestrator.run(build_pipeline(0.01), injected_failures={"evaluate": 1}))
    print_run("run 2: nothing changed", orchestrator.run(build_pipeline(0.01)))
    print_run("run 3: lr 0.01 -> 0.005", orchestrator.run(build_pipeline(0.005)))

    cyclic = build_pipeline(0.01)
    cyclic[1] = replace(cyclic[1], upstream=("ingest", "register"))
    try:
        orchestrator.run(cyclic)
    except CycleError as error:
        print(f"\n== run 4: validate made to depend on register ==\nrejected before running: "
              f"cycle {' -> '.join(error.args[1])}")


if __name__ == "__main__":
    main()
