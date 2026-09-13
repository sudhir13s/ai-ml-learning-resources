"""Package a PyTorch model as a verifiable artifact, then serve it the way a container would.

The artifact is safetensors weights plus a manifest that records the weight hash, the
preprocessing statistics and the input signature. The loader refuses anything that
breaks those promises: a flipped byte, a missing feature, a string where a number
belongs. The last demo shows why pickled checkpoints are the wrong format to ship.
Runs on CPU in a few seconds.
"""
from __future__ import annotations

import hashlib
import json
import pickle
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path

import torch
from safetensors.torch import load_file, save_file
from torch import nn

MODEL_NAME = "transaction-risk"
MODEL_VERSION = "1.0.0"
FEATURES = ["amount_usd", "account_age_days", "txn_count_24h", "distance_km"]
CLASSES = ["low", "medium", "high"]
CLASS_CENTERS = torch.tensor([
    [40.0, 900.0, 2.0, 5.0],
    [400.0, 300.0, 6.0, 80.0],
    [2500.0, 20.0, 20.0, 900.0],
])
SPREAD = 0.35
HIDDEN_UNITS = 16
SAMPLES_PER_CLASS = 200
TRAIN_FRACTION = 0.7
TRAIN_STEPS = 300
LEARNING_RATE = 0.05
SEED = 0


class SignatureError(ValueError):
    """A request that does not match the artifact's input contract."""


class IntegrityError(ValueError):
    """Weights on disk that do not match the manifest's hash."""


@dataclass(frozen=True)
class LabelledData:
    features: torch.Tensor
    labels: torch.Tensor


class RiskClassifier(nn.Module):
    def __init__(self, in_features: int, hidden: int, out_classes: int) -> None:
        super().__init__()
        self.net = nn.Sequential(nn.Linear(in_features, hidden), nn.ReLU(),
                                 nn.Linear(hidden, out_classes))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def make_data(generator: torch.Generator) -> LabelledData:
    """Gaussian clusters around each class centre, each feature spread 35 percent."""
    features, labels = [], []
    for index, center in enumerate(CLASS_CENTERS):
        noise = torch.randn(SAMPLES_PER_CLASS, len(FEATURES), generator=generator)
        features.append(center + noise * center * SPREAD)
        labels.append(torch.full((SAMPLES_PER_CLASS,), index))
    return LabelledData(torch.cat(features), torch.cat(labels))


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def train_and_package(out_dir: Path) -> dict:
    generator = torch.Generator().manual_seed(SEED)
    torch.manual_seed(SEED)
    data = make_data(generator)
    order = torch.randperm(len(data.labels), generator=generator)
    cut = int(TRAIN_FRACTION * len(order))
    train, test = order[:cut], order[cut:]
    mean, std = data.features[train].mean(0), data.features[train].std(0)

    model = RiskClassifier(len(FEATURES), HIDDEN_UNITS, len(CLASSES))
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
    for _ in range(TRAIN_STEPS):
        loss = nn.functional.cross_entropy(model((data.features[train] - mean) / std), data.labels[train])
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        predicted = model((data.features[test] - mean) / std).argmax(1)
    accuracy = (predicted == data.labels[test]).float().mean().item()

    weights_path = out_dir / "model.safetensors"
    save_file(model.state_dict(), str(weights_path))
    manifest = {
        "name": MODEL_NAME, "version": MODEL_VERSION,
        "framework": f"torch=={torch.__version__}",
        "weights_file": weights_path.name, "weights_format": "safetensors",
        "weights_sha256": sha256_of(weights_path),
        "architecture": {"class": "RiskClassifier", "in_features": len(FEATURES),
                         "hidden": HIDDEN_UNITS, "out_classes": len(CLASSES)},
        "preprocessing": {"standardize": {"mean": mean.tolist(), "std": std.tolist()}},
        "signature": {"inputs": [{"name": name, "dtype": "float32"} for name in FEATURES],
                      "outputs": [{"name": "risk", "dtype": "string", "values": CLASSES}]},
        "metrics": {"holdout_accuracy": round(accuracy, 4)},
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return manifest


class ModelService:
    """The container entrypoint: trusts only the manifest, verifies before it serves."""

    def __init__(self, artifact_dir: Path) -> None:
        self.manifest = json.loads((artifact_dir / "manifest.json").read_text())
        weights_path = artifact_dir / self.manifest["weights_file"]
        if sha256_of(weights_path) != self.manifest["weights_sha256"]:
            raise IntegrityError("weights sha256 does not match the manifest; refusing to serve")
        shape = self.manifest["architecture"]
        self.model = RiskClassifier(shape["in_features"], shape["hidden"], shape["out_classes"])
        self.model.load_state_dict(load_file(str(weights_path)), strict=True)
        self.model.eval()
        stats = self.manifest["preprocessing"]["standardize"]
        self.mean, self.std = torch.tensor(stats["mean"]), torch.tensor(stats["std"])
        self.input_names = [spec["name"] for spec in self.manifest["signature"]["inputs"]]
        self.classes = self.manifest["signature"]["outputs"][0]["values"]

    def validate(self, record: dict) -> torch.Tensor:
        missing = [name for name in self.input_names if name not in record]
        unknown = sorted(set(record) - set(self.input_names))
        if missing or unknown:
            raise SignatureError(f"missing={missing} unknown={unknown}")
        wrong_type = [name for name in self.input_names
                      if isinstance(record[name], bool) or not isinstance(record[name], (int, float))]
        if wrong_type:
            raise SignatureError(f"not numeric: {wrong_type}")
        return torch.tensor([[float(record[name]) for name in self.input_names]])

    def score(self, features: torch.Tensor) -> dict:
        with torch.no_grad():
            probabilities = self.model(features).softmax(1)[0]
        index = int(probabilities.argmax())
        return {"risk": self.classes[index], "confidence": round(float(probabilities[index]), 3)}

    def predict(self, record: dict) -> dict:
        return self.score((self.validate(record) - self.mean) / self.std)


class RunsCodeOnLoad:
    """Any pickled object can name a function for the unpickler to call."""

    def __reduce__(self):
        return (print, ("  pickle.loads just called print() -- it could call anything",))


def demo_integrity(artifact: Path) -> None:
    tampered = Path(tempfile.mkdtemp(prefix="tampered-"))
    shutil.copytree(artifact, tampered, dirs_exist_ok=True)
    weights = bytearray((tampered / "model.safetensors").read_bytes())
    weights[-1] ^= 0x01                                   # flip one bit of one weight
    (tampered / "model.safetensors").write_bytes(bytes(weights))
    try:
        ModelService(tampered)
    except IntegrityError as error:
        print("  tampered artifact :", error)


def main() -> None:
    artifact = Path(tempfile.mkdtemp(prefix="artifact-"))
    manifest = train_and_package(artifact)
    print("== packaged artifact ==")
    print("  files            :", sorted(path.name for path in artifact.iterdir()))
    print("  framework        :", manifest["framework"])
    print("  weights sha256   :", manifest["weights_sha256"][:16], "...")
    print("  holdout accuracy :", manifest["metrics"]["holdout_accuracy"])

    service = ModelService(artifact)
    request = {"amount_usd": 420.0, "account_age_days": 280, "txn_count_24h": 7, "distance_km": 95.0}
    print("\n== one request, served ==")
    print("  with the manifest's preprocessing   :", service.predict(request))
    print("  raw features, preprocessing skipped :", service.score(service.validate(request)))

    print("\n== requests that break the contract ==")
    for bad in ({"amount_usd": 420.0}, {**request, "amount_usd": "420.0"}):
        try:
            service.predict(bad)
        except SignatureError as error:
            print("  rejected          :", error)
    demo_integrity(artifact)

    print("\n== why the weights are not a pickle ==")
    pickle.loads(pickle.dumps(RunsCodeOnLoad()))


if __name__ == "__main__":
    main()
