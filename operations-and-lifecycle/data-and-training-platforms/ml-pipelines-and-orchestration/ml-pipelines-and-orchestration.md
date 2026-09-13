---
id: "18-mlops/ml-pipelines-and-orchestration"
topic: "ML Pipelines & Orchestration (Airflow · Kubeflow)"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["ml-lifecycle", "reproducibility"]
leads_to: ["18-mlops/cicd-for-ml-and-continuous-training"]
interview_frequency: high
template: concept-deep
updated: 2026-09-13
tier: standard
est_minutes: 25
core_idea: "An ML workflow becomes reliable when its steps are declared as a dependency graph that a scheduler runs, retries and caches, so repeating the same inputs does no work and changing one input redoes only what depends on it."
title: "ML Pipelines & Orchestration (Airflow · Kubeflow)"
minutes: 25
category: data-and-training-platforms
---

# ML Pipelines and Orchestration: the workflow as a graph, not a person

> Turning a notebook's sequence of cells into a declared graph of steps that an orchestrator
> schedules, retries, caches and records. Pipelines, not people, run the workflow.

**Why it matters:** "how do you move from a notebook to a production pipeline?" is a standard MLOps question.

- **What gets probed:** the directed acyclic graph (DAG) model, idempotency and retries, caching, and why ML pipelines need data validation and lineage.
- **The tool landscape:** Airflow 3, Kubeflow Pipelines 2, and asset- or flow-first options such as Dagster, Prefect and Metaflow.
- **The strong answer:** explains **what the orchestrator decides for you** — order, retries, reuse — not only which tool you picked.

We use **one pipeline** throughout: the training pipeline for `iris-classifier`, which ingests a snapshot, validates it, trains, evaluates and registers.

## Why a script with five steps is not a pipeline

A `train.py` that runs ingest, validate, train, evaluate and register in order works — until something goes wrong.

- **A failure at step four reruns steps one to three,** paying for data loading and training again.
- **Nobody knows which inputs produced which output,** so a surprising accuracy cannot be traced.
- **A person has to start it,** so it runs when someone remembers, not when data arrives.
- **A flaky step fails the whole run,** and there is no record of what to retry.

## Declaring the pipeline as a DAG

The fix is to describe the workflow as data: named steps and the dependencies between them.

- **Directed:** each edge says "this step consumes that step's output".
- **Acyclic:** no step can depend, even indirectly, on itself, so there is always a valid order.

```mermaid
graph LR
    ING(["Ingest<br/>versioned snapshot"]):::ingest --> VAL(["Validate<br/>schema + stats"]):::val
    VAL --> TR(["Train<br/>pinned image + seed"]):::train
    TR --> EV(["Evaluate<br/>holdout metrics"]):::eval
    EV --> RG(["Register<br/>if the gate passes"]):::reg
    RG --> DP(["Deploy<br/>canary rollout"]):::deploy

    classDef ingest fill:#3A6B96,stroke:#2A5B86,color:#fff
    classDef val fill:#2A5B80,stroke:#1A4B70,color:#fff
    classDef train fill:#5D4A8A,stroke:#4D3A7A,color:#fff
    classDef eval fill:#7D5A2C,stroke:#6D4A1C,color:#fff
    classDef reg fill:#7A6528,stroke:#6A5518,color:#fff
    classDef deploy fill:#2E7A5A,stroke:#1E6A4A,color:#fff
```

Each box is typically a **container** with declared inputs and outputs, so the orchestrator can run it anywhere and record exactly what it read and wrote.

- **Validate before train:** a silently broken upstream source is the most common cause of a bad model; the pipeline refuses to train on it.
- **Register only if the gate passes:** the evaluation gate from [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) sits between evaluate and register.

## What an orchestrator adds: order, retries, caching

Given the graph, the orchestrator makes three decisions a script leaves to you.

- **Order:** a topological sort gives a sequence in which every step runs after all its upstreams.
- **Retries:** a transient failure, such as a pre-empted worker, is retried a bounded number of times.
  - Retrying is only safe if the step is **idempotent**: running it twice with the same inputs leaves the same result.
- **Caching:** a step whose inputs have not changed is not run again; its stored output is reused.

The cache is keyed by a **fingerprint** that folds in everything that could change a step's output:

$$f_s = H\big(\text{name}_s,\ \text{code version}_s,\ \text{params}_s,\ f_{u_1}, \dots, f_{u_n}\big)$$

- $H$: a cryptographic hash such as SHA-256.
- $f_{u_1}, \dots, f_{u_n}$: the fingerprints of the step's upstream steps.

Because upstream fingerprints are inputs, a change **propagates downstream only**:

```mermaid
graph LR
    I(["ingest<br/>unchanged"]):::same --> V(["validate<br/>unchanged"]):::same
    V --> T(["train<br/>lr changed"]):::changed
    T --> E(["evaluate<br/>new upstream"]):::changed
    E --> R(["register<br/>new upstream"]):::changed

    classDef same fill:#4A5B6E,stroke:#3A4B5E,color:#fff
    classDef changed fill:#7A6528,stroke:#6A5518,color:#fff
```

Changing the learning rate changes `train`'s fingerprint, which changes `evaluate`'s and `register`'s. Ingest and validate keep theirs and are reused.

## A pipeline runner you can run

The runner below is a complete, small orchestrator: topological order, fingerprint caching, bounded retries and cycle rejection.

```python
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
```

Its output:

```text
== run 1: cold cache, evaluate pre-empted once ==
step      | status | attempts | fingerprint | output
------------------------------------------------------------------------------
ingest    | ran    |        1 | 13a35f0adf  | {'snapshot': 'iris@2026-09-01', 'rows': 150}
validate  | ran    |        1 | 8bc42c08a3  | {'rows_valid': 150}
train     | ran    |        1 | 20a78f3a7d  | {'weights_sha256': '5910226bd3bb'}
evaluate  | ran    |        2 | 082f8ea803  | {'accuracy': 0.917}
register  | ran    |        1 | d74befad4a  | {'registered': True, 'accuracy': 0.917}

== run 2: nothing changed ==
step      | status | attempts | fingerprint | output
------------------------------------------------------------------------------
ingest    | cached |        0 | 13a35f0adf  | {'snapshot': 'iris@2026-09-01', 'rows': 150}
validate  | cached |        0 | 8bc42c08a3  | {'rows_valid': 150}
train     | cached |        0 | 20a78f3a7d  | {'weights_sha256': '5910226bd3bb'}
evaluate  | cached |        0 | 082f8ea803  | {'accuracy': 0.917}
register  | cached |        0 | d74befad4a  | {'registered': True, 'accuracy': 0.917}

== run 3: lr 0.01 -> 0.005 ==
step      | status | attempts | fingerprint | output
------------------------------------------------------------------------------
ingest    | cached |        0 | 13a35f0adf  | {'snapshot': 'iris@2026-09-01', 'rows': 150}
validate  | cached |        0 | 8bc42c08a3  | {'rows_valid': 150}
train     | ran    |        1 | 0e78531daf  | {'weights_sha256': 'ac546dcd7e75'}
evaluate  | ran    |        1 | 1607846c09  | {'accuracy': 0.934}
register  | ran    |        1 | b9aa0a8882  | {'registered': True, 'accuracy': 0.934}

== run 4: validate made to depend on register ==
rejected before running: cycle validate -> train -> evaluate -> register -> validate
```

Read the four runs against the three decisions:

- **Retries (run 1):** `evaluate` was pre-empted once and succeeded on attempt 2. Nothing upstream reran.
- **Caching (run 2):** every fingerprint matched, so zero steps executed. On a real cluster that is zero GPU hours.
- **Propagation (run 3):** only `train`, `evaluate` and `register` got new fingerprints and ran; `ingest` and `validate` kept `13a35f0adf` and `8bc42c08a3`.
- **Validation of the graph (run 4):** the cycle was reported before any step ran, naming every node on it.

> **Note:**
> - The step bodies are stand-ins: `train` hashes its recipe instead of fitting a model, so the example runs in milliseconds.
> - The orchestration logic is the real thing; swap the bodies for real work and nothing else changes.

## Choosing an orchestrator

The tools share the DAG model and differ in what they treat as the unit of work.

| Tool | Model | Reach for it when |
|---|---|---|
| **Apache Airflow 3** | general workflow scheduler; DAG versioning and a task-execution API since 3.0 | the organisation already schedules data jobs and ML is one more workload |
| **Kubeflow Pipelines 2** | Kubernetes-native, each step a container with typed inputs and outputs | training already runs on Kubernetes and you want ML metadata tracked per step |
| **Dagster** | asset-first: declare the data assets, the graph is derived | lineage between datasets and models is the main thing you need to see |
| **Prefect** | Python-native flows with dynamic, runtime-defined graphs | the graph shape depends on data discovered while running |
| **Metaflow** | data-scientist-facing flows with built-in artifact versioning | a small team wants notebooks-to-cloud scale-out with little platform work |

## From pipeline to continuous training

The same DAG, triggered by something other than a person, is continuous training.

- **On a schedule or a drift signal:** see [Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/continuous-training/continuous-training) for when the loop should fire.
- **Into a release:** a registered candidate enters the gated release pipeline in [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training).
- **On hardware:** the train step's GPUs come from [Cluster Scheduling and Training Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/cluster-scheduling-and-training-orchestration/cluster-scheduling-and-training-orchestration).

## Common misconceptions

- **"An orchestrator is a cron job with a UI."** Cron starts things; an orchestrator also orders, retries, caches and records them.
- **"Retries make a pipeline reliable."** Retrying a non-idempotent step, such as one that appends rows, makes it wrong.
- **"Caching is just an optimization."** It is also a correctness claim: a cached output is only valid if the fingerprint covers every input.

## Pitfalls

| Symptom you see | Likely cause | Fix |
|---|---|---|
| **A stale model after the data changed** | Fingerprint covered the snapshot name, not its content | Include a content hash or immutable version of the data |
| **Duplicate rows after a retry** | Step appends instead of overwriting | Write to a path keyed by run and step; make every step idempotent |
| **Code change had no effect** | Code version not part of the fingerprint | Fold the image digest or commit into the key |
| **One slow step blocks every run** | All steps scheduled serially | Let independent branches run in parallel; the DAG already says which are independent |
| **Pipeline trained on a broken source** | No validation step before training | Add a data contract check that fails the run loudly |

## Key takeaways

- A pipeline is the workflow **declared as a DAG**, not a script a person runs.
- The orchestrator decides **order, retries and caching** from that declaration.
- Cache keys fold in **code, parameters and upstream fingerprints**, so changes propagate downstream only.
- Retries are safe only for **idempotent** steps.
- The same DAG on a trigger **is** continuous training.

## Production implementation

Runnable services in this estate that implement what this page teaches:

- **[ml-platform](/python/python-production-examples/ml-platform/readme)** — an idempotent DAG runner with state-driven readiness, cycle detection, and skip propagation that stops a model failing its evaluation gate from ever reaching registration.

## References

The curated link library for this topic — videos, courses, articles, papers and internal cross-links — lives in a companion file so it can be reused as a standalone reference list:

**→ [ML Pipelines and Orchestration — references](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration#references-further-reading)**
