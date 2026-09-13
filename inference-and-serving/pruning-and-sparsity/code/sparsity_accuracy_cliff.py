"""The sparsity-accuracy cliff, measured, then pushed back with iterative pruning.

Trains a small multilayer perceptron on a learnable two-class problem, then runs three
experiments on the SAME trained weights:

1. One-shot global magnitude pruning at increasing sparsity. Every weight matrix is ranked
   together by |w|, the smallest fraction is zeroed with a mask m = 1[|W| > tau], and test
   accuracy is measured with no retraining. Accuracy holds, then falls off a cliff.
2. Iterative pruning with fine-tuning. The same final sparsity is reached in small steps,
   and between steps the surviving weights are trained for a few hundred updates with the
   mask re-applied after every optimizer step, so pruned weights stay exactly zero.
3. Storage. A 90%-sparse weight matrix saved densely is exactly as big as the dense one;
   only a compressed sparse row (CSR) copy is smaller, and at low sparsity CSR is BIGGER.

Runs offline on CPU in a few seconds; downloads nothing.

Run:
    uv run --python 3.12 --with torch python sparsity_accuracy_cliff.py
"""

from __future__ import annotations

import io

import torch
from torch import nn

SEED = 0
SAMPLE_COUNT = 2000
TRAIN_COUNT = 1600
FEATURE_COUNT = 20
INFORMATIVE_FEATURES = 5
LABEL_NOISE = 0.3
HIDDEN_WIDTH = 128
CLASS_COUNT = 2
LEARNING_RATE = 1e-2
TRAIN_STEPS = 300
FINE_TUNE_STEPS_PER_ROUND = 100
ONE_SHOT_SPARSITIES = (0.0, 0.5, 0.7, 0.8, 0.9, 0.95, 0.98, 0.99)
ITERATIVE_SCHEDULE = (0.5, 0.7, 0.8, 0.9, 0.95, 0.98, 0.99)
STORAGE_SPARSITIES = (0.0, 0.5, 0.9)
BYTES_PER_KILOBYTE = 1e3


def make_dataset() -> dict[str, torch.Tensor]:
    """Two classes separated by the sign of a noisy sum of the first five features."""
    features = torch.randn(SAMPLE_COUNT, FEATURE_COUNT)
    signal = features[:, :INFORMATIVE_FEATURES].sum(dim=1)
    labels = (signal + LABEL_NOISE * torch.randn(SAMPLE_COUNT) > 0).long()
    return {
        "train_x": features[:TRAIN_COUNT],
        "train_y": labels[:TRAIN_COUNT],
        "test_x": features[TRAIN_COUNT:],
        "test_y": labels[TRAIN_COUNT:],
    }


def build_model() -> nn.Sequential:
    return nn.Sequential(
        nn.Linear(FEATURE_COUNT, HIDDEN_WIDTH),
        nn.ReLU(),
        nn.Linear(HIDDEN_WIDTH, HIDDEN_WIDTH),
        nn.ReLU(),
        nn.Linear(HIDDEN_WIDTH, CLASS_COUNT),
    )


def weight_parameters(model: nn.Module) -> dict[str, nn.Parameter]:
    """The weight matrices pruning acts on; biases are left dense."""
    return {name: param for name, param in model.named_parameters() if name.endswith("weight")}


def train(model: nn.Module, data: dict[str, torch.Tensor], steps: int,
          masks: dict[str, torch.Tensor] | None = None) -> None:
    """Full-batch Adam; when masks are given, pruned weights are forced back to zero."""
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
    loss_function = nn.CrossEntropyLoss()
    for _ in range(steps):
        optimizer.zero_grad()
        loss_function(model(data["train_x"]), data["train_y"]).backward()
        optimizer.step()
        if masks is not None:
            apply_masks(model, masks)


@torch.no_grad()
def test_accuracy(model: nn.Module, data: dict[str, torch.Tensor]) -> float:
    predictions = model(data["test_x"]).argmax(dim=1)
    return (predictions == data["test_y"]).float().mean().item() * 100


@torch.no_grad()
def global_magnitude_masks(model: nn.Module, sparsity: float) -> dict[str, torch.Tensor]:
    """Rank every weight in the network together; keep those strictly above the threshold.

    tau is the k-th smallest |w| over all matrices, with k = sparsity * total weights,
    so exactly k weights fall at or below it when magnitudes are distinct.
    """
    weights = weight_parameters(model)
    if sparsity == 0.0:
        return {name: torch.ones_like(param, dtype=torch.bool) for name, param in weights.items()}
    all_magnitudes = torch.cat([param.abs().flatten() for param in weights.values()])
    zeroed_count = int(sparsity * all_magnitudes.numel())
    threshold = all_magnitudes.kthvalue(zeroed_count).values
    return {name: param.abs() > threshold for name, param in weights.items()}


@torch.no_grad()
def apply_masks(model: nn.Module, masks: dict[str, torch.Tensor]) -> None:
    for name, param in weight_parameters(model).items():
        param.mul_(masks[name])


def realized_sparsity_percent(masks: dict[str, torch.Tensor]) -> float:
    kept = sum(int(mask.sum()) for mask in masks.values())
    total = sum(mask.numel() for mask in masks.values())
    return 100 * (1 - kept / total)


def serialized_kilobytes(tensor: torch.Tensor) -> float:
    buffer = io.BytesIO()
    torch.save(tensor, buffer)
    return buffer.getbuffer().nbytes / BYTES_PER_KILOBYTE


def run_small_matrix() -> None:
    """The page's hand-worked 3x4 example: global vs per-row masks at 50% sparsity."""
    weight = torch.tensor([[0.60, -0.02, 0.15, -0.40],
                           [0.05, 0.90, -0.08, 0.03],
                           [-0.25, 0.10, -0.70, 0.12]])
    probe = torch.ones(4)
    magnitudes = weight.abs()
    zeroed_count = weight.numel() // 2
    kth_threshold = magnitudes.flatten().kthvalue(zeroed_count).values.item()
    quantile_threshold = torch.quantile(magnitudes.flatten(), 0.5).item()
    global_mask = magnitudes >= quantile_threshold
    kth_inclusive_mask = magnitudes >= kth_threshold
    row_keep = weight.shape[1] // 2
    row_mask = torch.zeros_like(weight, dtype=torch.bool)
    row_mask.scatter_(1, magnitudes.topk(row_keep, dim=1).indices, True)
    dense_output = weight @ probe
    print(f"k-th smallest |w| = {kth_threshold:.3f}; 50th percentile |w| = {quantile_threshold:.3f}")
    print(f"'>= k-th value' keeps {int(kth_inclusive_mask.sum())} of 12 (off by one)")
    for label, mask in (("global", global_mask), ("per-row", row_mask)):
        pruned = weight * mask
        mass = pruned.abs().sum().item() / magnitudes.sum().item() * 100
        output = pruned @ probe
        squared_error = ((output - dense_output) ** 2).sum().item()
        print(f"{label:>8}: kept {int(mask.sum())}, mass kept {mass:.1f}%, "
              f"output {[round(v, 2) for v in output.tolist()]}, squared error {squared_error:.4f}")
        print(f"          mask rows {mask.int().tolist()}")
    print(f"   dense: output {[round(v, 2) for v in dense_output.tolist()]}")


def run_one_shot(dense_state: dict[str, torch.Tensor], data: dict[str, torch.Tensor]) -> None:
    print(f"{'target sparsity':>16}{'real sparsity':>15}{'accuracy %':>13}")
    model = build_model()
    for sparsity in ONE_SHOT_SPARSITIES:
        model.load_state_dict(dense_state)
        masks = global_magnitude_masks(model, sparsity)
        apply_masks(model, masks)
        real = realized_sparsity_percent(masks)
        print(f"{sparsity * 100:>15.0f}%{real:>14.1f}%{test_accuracy(model, data):>13.1f}")


def run_iterative(dense_state: dict[str, torch.Tensor], data: dict[str, torch.Tensor]) -> None:
    print(f"{'round sparsity':>15}{'after prune %':>15}{'after fine-tune %':>19}")
    model = build_model()
    model.load_state_dict(dense_state)
    for sparsity in ITERATIVE_SCHEDULE:
        masks = global_magnitude_masks(model, sparsity)
        apply_masks(model, masks)
        pruned_accuracy = test_accuracy(model, data)
        train(model, data, FINE_TUNE_STEPS_PER_ROUND, masks)
        tuned_accuracy = test_accuracy(model, data)
        print(f"{sparsity * 100:>14.0f}%{pruned_accuracy:>15.1f}{tuned_accuracy:>19.1f}")


def run_storage(dense_state: dict[str, torch.Tensor]) -> None:
    model = build_model()
    print(f"{'sparsity':>9}{'dense save (kB)':>17}{'CSR save (kB)':>15}")
    for sparsity in STORAGE_SPARSITIES:
        model.load_state_dict(dense_state)
        masks = global_magnitude_masks(model, sparsity)
        apply_masks(model, masks)
        hidden = model[2].weight.detach().clone()          # the 128 x 128 matrix
        dense_size = serialized_kilobytes(hidden)
        csr_size = serialized_kilobytes(hidden.to_sparse_csr())
        print(f"{sparsity * 100:>8.0f}%{dense_size:>17.1f}{csr_size:>15.1f}")


def main() -> None:
    print("Worked 3x4 matrix, 50% sparsity")
    run_small_matrix()
    print()
    torch.manual_seed(SEED)
    data = make_dataset()
    model = build_model()
    train(model, data, TRAIN_STEPS)
    dense_state = {name: tensor.clone() for name, tensor in model.state_dict().items()}
    total_weights = sum(param.numel() for param in weight_parameters(model).values())
    print(f"torch {torch.__version__} · {total_weights:,} prunable weights")
    print(f"dense baseline accuracy: {test_accuracy(model, data):.1f}%\n")

    print("One-shot global magnitude pruning (no retraining)")
    run_one_shot(dense_state, data)
    print(f"\nIterative pruning, {FINE_TUNE_STEPS_PER_ROUND} fine-tune steps per round")
    run_iterative(dense_state, data)
    print("\nStorage of the 128x128 hidden matrix")
    run_storage(dense_state)


if __name__ == "__main__":
    main()
