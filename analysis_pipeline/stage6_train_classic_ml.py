from __future__ import annotations

import argparse
import csv
from functools import partial
import hashlib
import itertools
import json
import math
import os
import random
import subprocess
import time
import warnings
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, pstdev
from typing import Any

import matplotlib
import numpy as np
import pandas as pd
from eeg_condition_psd import build_condition_psd_report
from sklearn.base import BaseEstimator, TransformerMixin, clone
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_selection import SelectFromModel, SelectPercentile, VarianceThreshold, f_classif, mutual_info_classif
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import GroupKFold, StratifiedKFold, StratifiedShuffleSplit
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Avoid torch dynamo/onnx import-time dependency issues in this pipeline runtime.
os.environ.setdefault("TORCH_DISABLE_DYNAMO", "1")
os.environ.setdefault("TORCHDYNAMO_DISABLE", "1")
os.environ.setdefault("PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION", "python")

try:
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader, TensorDataset

    TORCH_AVAILABLE = True
except Exception:  # noqa: BLE001
    torch = None  # type: ignore[assignment]
    nn = None  # type: ignore[assignment]
    DataLoader = None  # type: ignore[assignment]
    TensorDataset = None  # type: ignore[assignment]
    TORCH_AVAILABLE = False


DEEP_MODEL_NAMES = (
    "lstm1d",
    "gru1d",
    "cnn1d",
    "transformer",
    "bilstm1d",
    "bigru1d",
    "cnn1d_deep",
    "transformer_xl",
)


NON_FEATURE_COLUMNS = {
    "fused_row_id",
    "ml_row_id",
    "modality",
    "participant_id",
    "analysis_included",
    "trial_id",
    "epoch_id",
    "block",
    "is_tutorial",
    "difficulty_range",
    "difficulty_bin",
    "difficulty_bin_index",
    "target_label",
    "response_accuracy",
    "outcome",
    "window",
    "segment_index",
    "is_subwindow",
    "epoch_start_s",
    "epoch_end_s",
    "epoch_duration_s",
    "dropout_policy",
    "dropout_threshold_value",
    "dropout_keep",
    "dropped_samples_trial",
    "split_group",
    "baseline_start_s",
    "baseline_end_s",
    "preproc_version",
    "ml_keep",
    "modalities_selected",
    "modalities_present",
    "n_modalities_present",
    "_target_source_label",
    "_target_label_effective",
}


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _features_dir() -> Path:
    return _analysis_root() / "features"


def _models_root() -> Path:
    return _analysis_root() / "models"


def _default_split_manifest() -> Path:
    return _features_dir() / "split_manifest.json"


def _default_results_json() -> Path:
    return _reports_dir() / "ml_results.json"


def _default_summary_md() -> Path:
    return _reports_dir() / "ml_summary.md"


def _default_live_confusion_png_dir() -> Path:
    return _reports_dir() / "confusion_pngs_live"


def _default_eeg_condition_psd_dir() -> Path:
    return _reports_dir() / "eeg_condition_psd"


def _slug(text: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "_" for ch in str(text).strip())
    out = "_".join(part for part in out.split("_") if part)
    return out or "default"


def _resolve_bids_root(bids_root_arg: str) -> Path:
    direct = Path(bids_root_arg).expanduser()
    if direct.is_absolute():
        return direct.resolve()

    from_cwd = (Path.cwd() / direct).resolve()
    if from_cwd.exists():
        return from_cwd

    repo_root = Path(__file__).resolve().parent.parent
    return (repo_root / direct).resolve()


def _translate_wsl_path(path_text: str) -> Path | None:
    normalized = str(path_text).strip().replace("\\", "/")
    if not normalized.startswith("/mnt/") or len(normalized) < 8:
        return None
    drive = normalized[5]
    if not drive.isalpha() or normalized[6] != "/":
        return None
    remainder = normalized[7:]
    return Path(f"{drive.upper()}:/{remainder}")


def _translate_windows_drive_path(path_text: str) -> Path | None:
    normalized = str(path_text).strip().replace("\\", "/")
    if len(normalized) < 4 or normalized[1] != ":" or normalized[2] != "/":
        return None
    drive = normalized[0]
    if not drive.isalpha():
        return None
    remainder = normalized[3:]
    return Path(f"/mnt/{drive.lower()}/{remainder}")


def _resolve_dataset_path(path_text: str, split_manifest_path: Path) -> Path:
    direct = Path(path_text).expanduser()
    if direct.is_absolute() and direct.exists():
        return direct.resolve()

    translated_wsl = _translate_wsl_path(path_text)
    if translated_wsl is not None and translated_wsl.exists():
        return translated_wsl.resolve()
    translated_windows = _translate_windows_drive_path(path_text)
    if translated_windows is not None and translated_windows.exists():
        return translated_windows.resolve()

    from_manifest = (split_manifest_path.parent / direct).resolve()
    if from_manifest.exists():
        return from_manifest

    from_cwd = (Path.cwd() / direct).resolve()
    if from_cwd.exists():
        return from_cwd

    repo_root = Path(__file__).resolve().parent.parent
    repo_candidate = (repo_root / direct).resolve()
    if repo_candidate.exists():
        return repo_candidate

    if direct.is_absolute():
        return direct.resolve()
    if translated_wsl is not None:
        return translated_wsl.resolve()
    return repo_candidate


def _stable_seed_from_text(text: str, base_seed: int) -> int:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return (base_seed + int(digest[:8], 16)) % (2**31 - 1)


def _warning_key(record: warnings.WarningMessage) -> str:
    message = str(record.message).strip().splitlines()[0]
    if len(message) > 160:
        message = message[:157] + "..."
    return f"{record.category.__name__}: {message}"


def _capture_warnings(records: list[warnings.WarningMessage], warning_counter: Counter[str] | None) -> None:
    if warning_counter is None:
        return
    for record in records:
        warning_counter[_warning_key(record)] += 1


def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, float):
        if math.isfinite(value):
            return value
        return None
    text = str(value).strip()
    if not text or text.lower() == "n/a":
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    if not math.isfinite(number):
        return None
    return number


def _percent(value: float) -> str:
    return f"{100.0 * value:.2f}%"


def _product_grid(space: dict[str, list[Any]]) -> list[dict[str, Any]]:
    if not space:
        return [{}]
    keys = list(space.keys())
    values = [space[k] for k in keys]
    out: list[dict[str, Any]] = []
    for combo in itertools.product(*values):
        out.append({k: v for k, v in zip(keys, combo)})
    return out


def _coerce_dataset_list(manifest: dict[str, Any], datasets_arg: list[str] | None) -> list[str]:
    available = list(manifest.get("datasets", {}).keys())
    if not available:
        raise ValueError("No datasets listed in split manifest.")
    if not datasets_arg:
        return available
    picked = [d.strip() for d in datasets_arg if d.strip()]
    unknown = [d for d in picked if d not in available]
    if unknown:
        raise ValueError(f"Unknown datasets requested: {', '.join(sorted(set(unknown)))}")
    return list(dict.fromkeys(picked))


def _coerce_model_list(models_arg: list[str] | None) -> list[str]:
    available = _available_model_names()
    if not models_arg:
        return available
    picked = [m.strip().lower() for m in models_arg if m.strip()]
    unknown = [m for m in picked if m not in available]
    if unknown:
        deep_names = set(DEEP_MODEL_NAMES)
        missing_torch = sorted(set([m for m in unknown if m in deep_names]))
        if missing_torch and not TORCH_AVAILABLE:
            raise ValueError(
                "Unknown model names (PyTorch not available for deep models): "
                + ", ".join(missing_torch)
                + ". Install PyTorch or remove these models."
            )
        raise ValueError(f"Unknown model names: {', '.join(sorted(set(unknown)))}")
    return list(dict.fromkeys(picked))


def _available_feature_selector_names() -> list[str]:
    return ["none", "anova", "mutual_info", "l1", "tree"]


def _coerce_feature_selector_list(selectors_arg: list[str] | None) -> list[str]:
    available = _available_feature_selector_names()
    if not selectors_arg:
        return ["none"]
    picked = [s.strip().lower() for s in selectors_arg if s.strip()]
    unknown = [s for s in picked if s not in available]
    if unknown:
        raise ValueError(f"Unknown feature selectors: {', '.join(sorted(set(unknown)))}")
    return list(dict.fromkeys(picked))


def _coerce_protocol_list(protocols_arg: list[str] | None) -> list[str]:
    available = [
        "loso",
        "group_holdout",
        "within_participant",
        "pooled_stratified",
        "pooled_stratified_holdout",
        "pooled_stratified_one_fold",
    ]
    if not protocols_arg:
        return available
    picked = [p.strip().lower() for p in protocols_arg if p.strip()]
    unknown = [p for p in picked if p not in available]
    if unknown:
        raise ValueError(f"Unknown protocols: {', '.join(sorted(set(unknown)))}")
    return list(dict.fromkeys(picked))


DROP_LABEL_TOKENS = {"drop", "__drop__", "omit", "exclude", "remove"}


def _label_sort_key(label: str, fallback_order: dict[str, int]) -> tuple[float, int]:
    text = str(label).strip()
    lower = text.lower()
    if lower in {"baseline", "rest", "resting"} or lower.startswith("baseline"):
        return 10_000.0, fallback_order.get(text, 10_000)

    if "-" in text:
        left = text.split("-", 1)[0].strip()
        try:
            return float(left), fallback_order.get(text, 10_000)
        except ValueError:
            pass

    digit_parts: list[str] = []
    current = ""
    for ch in text:
        if ch.isdigit() or ch == ".":
            current += ch
        else:
            if current:
                digit_parts.append(current)
                current = ""
    if current:
        digit_parts.append(current)
    for token in digit_parts:
        try:
            return float(token), fallback_order.get(text, 10_000)
        except ValueError:
            continue

    if "low" in lower:
        return 1000.0, fallback_order.get(text, 10_000)
    if "mid" in lower:
        return 2000.0, fallback_order.get(text, 10_000)
    if "high" in lower:
        return 3000.0, fallback_order.get(text, 10_000)
    return 9000.0, fallback_order.get(text, 10_000)


def _reorder_labels_baseline_first(labels: list[str], baseline_label: str | None) -> list[str]:
    if not labels:
        return labels
    baseline_targets = []
    if baseline_label and baseline_label.strip():
        baseline_targets.append(baseline_label.strip())
    baseline_targets.extend(
        [label for label in labels if str(label).strip().lower().startswith("baseline") or str(label).strip().lower() == "baseline"]
    )
    baseline_targets = list(dict.fromkeys(baseline_targets))
    baseline_in_labels = [label for label in labels if label in baseline_targets]
    if not baseline_in_labels:
        return labels
    baseline = baseline_in_labels[0]
    non_baseline = [label for label in labels if label != baseline]
    return [baseline] + non_baseline


def _coerce_label_list(values: list[str] | None) -> list[str]:
    if not values:
        return []
    out: list[str] = []
    for value in values:
        text = str(value).strip()
        if not text:
            continue
        out.append(text)
    return list(dict.fromkeys(out))


def _ordered_counts(values: list[str], preferred_order: list[str] | None = None) -> dict[str, int]:
    counts = Counter(str(v) for v in values if str(v).strip())
    out: dict[str, int] = {}

    if preferred_order:
        for label in preferred_order:
            key = str(label).strip()
            if key in counts:
                out[key] = int(counts.pop(key))

    # Preserve first-seen order for any remaining labels.
    for value in values:
        key = str(value).strip()
        if key in counts and key not in out:
            out[key] = int(counts.pop(key))

    # Deterministic fallback if anything remains.
    for key in sorted(counts.keys()):
        out[key] = int(counts[key])

    return out


def _parse_merge_entry(text: str) -> tuple[str, str]:
    raw = str(text).strip()
    for sep in ("->", "=>", ":", "="):
        if sep in raw:
            left, right = raw.split(sep, 1)
            src = left.strip()
            dst = right.strip()
            if not src or not dst:
                break
            return src, dst
    raise ValueError(f"Invalid --class-merge entry '{text}'. Use formats like old->new or old=new.")


def _load_merge_map_json(path: Path) -> dict[str, str]:
    if not path.exists():
        raise FileNotFoundError(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"--class-merge-json must contain a JSON object of old_label -> new_label: {path}")
    out: dict[str, str] = {}
    for k, v in payload.items():
        src = str(k).strip()
        dst = str(v).strip()
        if not src or not dst:
            raise ValueError(f"Invalid merge map entry in {path}: '{k}' -> '{v}'")
        out[src] = dst
    return out


def _parse_class_merge_map(args: argparse.Namespace) -> dict[str, str]:
    merge_map: dict[str, str] = {}
    if args.class_merge_json:
        merge_map.update(_load_merge_map_json(Path(args.class_merge_json).resolve()))
    if args.class_merge:
        for entry in args.class_merge:
            src, dst = _parse_merge_entry(entry)
            merge_map[src] = dst
    return merge_map


def _build_class_scenario(split_manifest: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    manifest_labels = [
        str(item.get("label", "")).strip()
        for item in split_manifest.get("difficulty_bins", [])
        if str(item.get("label", "")).strip()
    ]
    baseline_from_tutorial_label = str(args.baseline_from_tutorial_label).strip() if args.baseline_from_tutorial_label else ""
    if baseline_from_tutorial_label:
        manifest_labels = [label for label in manifest_labels if label != baseline_from_tutorial_label]
        manifest_labels = [baseline_from_tutorial_label] + manifest_labels
    manifest_labels = list(dict.fromkeys(manifest_labels))
    if not manifest_labels:
        raise ValueError("No difficulty bin labels available in split manifest for class scenario setup.")

    include_labels = _coerce_label_list(args.class_include_labels)
    drop_labels = _coerce_label_list(args.class_drop_labels)
    merge_map = _parse_class_merge_map(args)

    manifest_set = set(manifest_labels)
    unknown_include = sorted(set(include_labels) - manifest_set)
    unknown_drop = sorted(set(drop_labels) - manifest_set)
    unknown_merge = sorted(set(merge_map.keys()) - manifest_set)
    if unknown_include:
        raise ValueError(f"Unknown labels in --class-include-labels: {', '.join(unknown_include)}")
    if unknown_drop:
        raise ValueError(f"Unknown labels in --class-drop-labels: {', '.join(unknown_drop)}")
    if unknown_merge:
        raise ValueError(f"Unknown source labels in class merge map: {', '.join(unknown_merge)}")

    include_set = set(include_labels)
    drop_set = set(drop_labels)
    allowed_original_labels = [
        label for label in manifest_labels if (not include_set or label in include_set) and label not in drop_set
    ]
    if not allowed_original_labels:
        raise ValueError("Class scenario removed all labels before training. Check include/drop settings.")

    final_labels: list[str] = []
    dropped_by_merge: list[str] = []
    for label in allowed_original_labels:
        merged = str(merge_map.get(label, label)).strip()
        if not merged or merged.lower() in DROP_LABEL_TOKENS:
            dropped_by_merge.append(label)
            continue
        if merged not in final_labels:
            final_labels.append(merged)
    final_labels = _reorder_labels_baseline_first(
        labels=final_labels,
        baseline_label=baseline_from_tutorial_label or None,
    )
    if len(final_labels) < 2:
        raise ValueError("Class scenario must keep at least 2 target classes after merge/drop.")

    return {
        "name": (args.class_scenario_name or "default").strip() or "default",
        "baseline_from_tutorial_label": baseline_from_tutorial_label or None,
        "manifest_labels": manifest_labels,
        "include_labels": include_labels,
        "drop_labels": drop_labels,
        "merge_map": merge_map,
        "allowed_original_labels": allowed_original_labels,
        "dropped_by_merge": dropped_by_merge,
        "final_labels": final_labels,
    }


class QuantileClipper(BaseEstimator, TransformerMixin):
    def __init__(self, lower_q: float = 0.01, upper_q: float = 0.99):
        self.lower_q = lower_q
        self.upper_q = upper_q
        self.lower_bounds_: np.ndarray | None = None
        self.upper_bounds_: np.ndarray | None = None

    def fit(self, X: Any, y: Any = None) -> "QuantileClipper":
        arr = np.asarray(X, dtype=np.float64)
        if arr.ndim != 2:
            raise ValueError("QuantileClipper expects 2D input.")
        lowers: list[float] = []
        uppers: list[float] = []
        for col_idx in range(arr.shape[1]):
            col = arr[:, col_idx]
            finite = col[np.isfinite(col)]
            if finite.size == 0:
                lowers.append(np.nan)
                uppers.append(np.nan)
                continue
            lowers.append(float(np.quantile(finite, self.lower_q)))
            uppers.append(float(np.quantile(finite, self.upper_q)))
        self.lower_bounds_ = np.asarray(lowers, dtype=np.float64)
        self.upper_bounds_ = np.asarray(uppers, dtype=np.float64)
        return self

    def transform(self, X: Any) -> np.ndarray:
        if self.lower_bounds_ is None or self.upper_bounds_ is None:
            raise RuntimeError("QuantileClipper must be fit before transform.")
        arr = np.asarray(X, dtype=np.float64).copy()
        for col_idx in range(arr.shape[1]):
            lo = self.lower_bounds_[col_idx]
            hi = self.upper_bounds_[col_idx]
            if not math.isfinite(lo) or not math.isfinite(hi):
                continue
            arr[:, col_idx] = np.clip(arr[:, col_idx], lo, hi)
        return arr


if TORCH_AVAILABLE:

    class _TabularCNN1DNet(nn.Module):
        def __init__(self, input_dim: int, num_classes: int, hidden_dim: int, dropout: float):
            super().__init__()
            self.conv = nn.Sequential(
                nn.Conv1d(1, 16, kernel_size=5, padding=2),
                nn.ReLU(),
                nn.BatchNorm1d(16),
                nn.Conv1d(16, 32, kernel_size=5, padding=2),
                nn.ReLU(),
                nn.BatchNorm1d(32),
                nn.Conv1d(32, 32, kernel_size=3, padding=1),
                nn.ReLU(),
                nn.AdaptiveAvgPool1d(16),
            )
            self.head = nn.Sequential(
                nn.Flatten(),
                nn.Linear(32 * 16, hidden_dim),
                nn.ReLU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, num_classes),
            )

        def forward(self, x: Any) -> Any:
            x = x.unsqueeze(1)
            x = self.conv(x)
            return self.head(x)


    class _TabularTransformerNet(nn.Module):
        def __init__(
            self,
            input_dim: int,
            num_classes: int,
            d_model: int,
            n_heads: int,
            n_layers: int,
            dropout: float,
        ):
            super().__init__()
            self.input_proj = nn.Linear(1, d_model)
            self.positional = nn.Parameter(torch.zeros(1, input_dim, d_model))
            encoder_layer = nn.TransformerEncoderLayer(
                d_model=d_model,
                nhead=n_heads,
                dim_feedforward=max(64, d_model * 2),
                dropout=dropout,
                batch_first=True,
                activation="gelu",
            )
            self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
            self.norm = nn.LayerNorm(d_model)
            self.head = nn.Sequential(
                nn.Linear(d_model, d_model),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(d_model, num_classes),
            )

        def forward(self, x: Any) -> Any:
            x = x.unsqueeze(-1)
            x = self.input_proj(x)
            x = x + self.positional[:, : x.shape[1], :]
            x = self.encoder(x)
            x = self.norm(torch.mean(x, dim=1))
            return self.head(x)


    class _TabularRNNNet(nn.Module):
        def __init__(
            self,
            *,
            input_dim: int,
            num_classes: int,
            hidden_dim: int,
            n_layers: int,
            dropout: float,
            rnn_type: str,
            bidirectional: bool = False,
        ):
            super().__init__()
            rnn_dropout = float(dropout) if int(n_layers) > 1 else 0.0
            hidden_dim_int = int(hidden_dim)
            bidirectional_flag = bool(bidirectional)
            if rnn_type == "lstm":
                self.rnn = nn.LSTM(
                    input_size=1,
                    hidden_size=hidden_dim_int,
                    num_layers=max(1, int(n_layers)),
                    batch_first=True,
                    dropout=rnn_dropout,
                    bidirectional=bidirectional_flag,
                )
            elif rnn_type == "gru":
                self.rnn = nn.GRU(
                    input_size=1,
                    hidden_size=hidden_dim_int,
                    num_layers=max(1, int(n_layers)),
                    batch_first=True,
                    dropout=rnn_dropout,
                    bidirectional=bidirectional_flag,
                )
            else:
                raise ValueError(f"Unknown rnn_type: {rnn_type}")

            rnn_output_dim = hidden_dim_int * (2 if bidirectional_flag else 1)
            self.head = nn.Sequential(
                nn.Linear(rnn_output_dim, hidden_dim_int),
                nn.ReLU(),
                nn.Dropout(float(dropout)),
                nn.Linear(hidden_dim_int, int(num_classes)),
            )

        def forward(self, x: Any) -> Any:
            x = x.unsqueeze(-1)
            out, _ = self.rnn(x)
            last = out[:, -1, :]
            return self.head(last)


    class TorchTabularClassifier(BaseEstimator):
        def __init__(
            self,
            architecture: str = "cnn1d",
            epochs: int = 30,
            batch_size: int = 64,
            lr: float = 1e-3,
            weight_decay: float = 1e-4,
            hidden_dim: int = 64,
            dropout: float = 0.2,
            n_heads: int = 4,
            n_layers: int = 1,
            bidirectional: bool = False,
            grad_clip: float = 1.0,
            random_state: int = 42,
            device: str = "cpu",
        ):
            self.architecture = architecture
            self.epochs = epochs
            self.batch_size = batch_size
            self.lr = lr
            self.weight_decay = weight_decay
            self.hidden_dim = hidden_dim
            self.dropout = dropout
            self.n_heads = n_heads
            self.n_layers = n_layers
            self.bidirectional = bidirectional
            self.grad_clip = grad_clip
            self.random_state = random_state
            self.device = device
            self.model_: Any | None = None
            self.classes_: np.ndarray | None = None
            self.device_: Any | None = None

        def _resolve_device(self) -> Any:
            if self.device == "auto":
                if torch.cuda.is_available():
                    return torch.device("cuda")
                return torch.device("cpu")
            return torch.device(self.device)

        def _build_model(self, input_dim: int, num_classes: int) -> Any:
            if self.architecture == "cnn1d":
                return _TabularCNN1DNet(
                    input_dim=input_dim,
                    num_classes=num_classes,
                    hidden_dim=int(self.hidden_dim),
                    dropout=float(self.dropout),
                )
            if self.architecture == "transformer":
                d_model = int(self.hidden_dim)
                n_heads = max(1, int(self.n_heads))
                if d_model % n_heads != 0:
                    raise ValueError(f"hidden_dim ({d_model}) must be divisible by n_heads ({n_heads}).")
                return _TabularTransformerNet(
                    input_dim=input_dim,
                    num_classes=num_classes,
                    d_model=d_model,
                    n_heads=n_heads,
                    n_layers=max(1, int(self.n_layers)),
                    dropout=float(self.dropout),
                )
            if self.architecture in {"lstm1d", "bilstm1d"}:
                return _TabularRNNNet(
                    input_dim=input_dim,
                    num_classes=num_classes,
                    hidden_dim=int(self.hidden_dim),
                    n_layers=max(1, int(self.n_layers)),
                    dropout=float(self.dropout),
                    rnn_type="lstm",
                    bidirectional=(self.architecture == "bilstm1d") or bool(self.bidirectional),
                )
            if self.architecture in {"gru1d", "bigru1d"}:
                return _TabularRNNNet(
                    input_dim=input_dim,
                    num_classes=num_classes,
                    hidden_dim=int(self.hidden_dim),
                    n_layers=max(1, int(self.n_layers)),
                    dropout=float(self.dropout),
                    rnn_type="gru",
                    bidirectional=(self.architecture == "bigru1d") or bool(self.bidirectional),
                )
            raise ValueError(f"Unknown architecture: {self.architecture}")

        def fit(self, X: Any, y: Any) -> "TorchTabularClassifier":
            x_arr = np.asarray(X, dtype=np.float32)
            if x_arr.ndim != 2:
                raise ValueError("TorchTabularClassifier expects a 2D feature matrix.")

            y_arr = np.asarray(y).astype(str)
            classes = np.unique(y_arr)
            if classes.size < 2:
                raise ValueError("TorchTabularClassifier requires at least 2 classes.")
            self.classes_ = classes
            class_to_idx = {label: idx for idx, label in enumerate(self.classes_)}
            y_idx = np.asarray([class_to_idx[str(label)] for label in y_arr], dtype=np.int64)

            self.device_ = self._resolve_device()
            torch.manual_seed(int(self.random_state))
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(int(self.random_state))

            self.model_ = self._build_model(input_dim=x_arr.shape[1], num_classes=int(classes.size)).to(self.device_)

            class_counts = np.bincount(y_idx, minlength=int(classes.size)).astype(np.float32)
            class_weights = class_counts.sum() / np.maximum(class_counts, 1.0)
            class_weights = class_weights / np.mean(class_weights)
            weight_tensor = torch.tensor(class_weights, dtype=torch.float32, device=self.device_)
            criterion = nn.CrossEntropyLoss(weight=weight_tensor)
            optimizer = torch.optim.AdamW(
                self.model_.parameters(),
                lr=float(self.lr),
                weight_decay=float(self.weight_decay),
            )

            dataset = TensorDataset(
                torch.from_numpy(x_arr.astype(np.float32)),
                torch.from_numpy(y_idx.astype(np.int64)),
            )
            batch_size = int(max(4, min(int(self.batch_size), len(dataset))))
            generator = torch.Generator()
            generator.manual_seed(int(self.random_state))
            loader = DataLoader(
                dataset,
                batch_size=batch_size,
                shuffle=True,
                generator=generator,
                drop_last=False,
            )

            self.model_.train()
            for _ in range(int(self.epochs)):
                for xb, yb in loader:
                    xb = xb.to(self.device_)
                    yb = yb.to(self.device_)
                    optimizer.zero_grad(set_to_none=True)
                    logits = self.model_(xb)
                    loss = criterion(logits, yb)
                    loss.backward()
                    if self.grad_clip and float(self.grad_clip) > 0:
                        nn.utils.clip_grad_norm_(self.model_.parameters(), float(self.grad_clip))
                    optimizer.step()
            return self

        def predict(self, X: Any) -> np.ndarray:
            if self.model_ is None or self.classes_ is None:
                raise RuntimeError("TorchTabularClassifier must be fit before predict.")
            x_arr = np.asarray(X, dtype=np.float32)
            if x_arr.ndim != 2:
                raise ValueError("TorchTabularClassifier expects a 2D feature matrix.")

            self.model_.eval()
            with torch.no_grad():
                tensor = torch.from_numpy(x_arr.astype(np.float32)).to(self.device_)
                logits = self.model_(tensor)
                pred_idx = torch.argmax(logits, dim=1).detach().cpu().numpy().astype(np.int64)
            return np.asarray([self.classes_[int(idx)] for idx in pred_idx], dtype=object)


def _available_model_names() -> list[str]:
    names = ["logreg", "knn", "svm", "gaussian_nb", "decision_tree", "mlp", "rf"]
    if TORCH_AVAILABLE:
        names.extend(list(DEEP_MODEL_NAMES))
    return names


def _resolve_torch_runtime_device(requested_device: str) -> str:
    wanted = str(requested_device or "auto").strip().lower()
    if wanted == "auto":
        if TORCH_AVAILABLE and torch is not None and torch.cuda.is_available():
            return "cuda"
        return "cpu"
    return wanted


def _detect_nvidia_gpus(timeout_seconds: float = 3.0) -> tuple[bool, list[str], str | None]:
    try:
        completed = subprocess.run(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            capture_output=True,
            text=True,
            timeout=max(0.5, float(timeout_seconds)),
            check=False,
        )
    except FileNotFoundError:
        return False, [], "nvidia-smi not found"
    except Exception as exc:  # noqa: BLE001
        return False, [], f"nvidia-smi probe failed: {exc}"

    if completed.returncode != 0:
        stderr = str(completed.stderr or "").strip()
        message = stderr if stderr else f"nvidia-smi return code {completed.returncode}"
        return False, [], message

    names = [line.strip() for line in str(completed.stdout or "").splitlines() if line.strip()]
    if not names:
        return False, [], "nvidia-smi returned no GPU names"
    return True, names, None


def _model_registry(random_state: int, torch_device: str) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {
        "logreg": {
            "label": "LogisticRegression",
            "estimator": LogisticRegression(
                solver="lbfgs",
                max_iter=8000,
                tol=1e-3,
                class_weight="balanced",
                random_state=random_state,
            ),
            "grid": _product_grid({"C": [0.1, 1.0, 5.0, 10.0]}),
        },
        "svm": {
            "label": "SVM-RBF",
            "estimator": SVC(kernel="rbf", class_weight="balanced"),
            "grid": _product_grid({"C": [0.5, 1.0, 3.0, 10.0], "gamma": ["scale", "auto"]}),
        },
        "gaussian_nb": {
            "label": "GaussianNB",
            "estimator": GaussianNB(),
            "grid": _product_grid({"var_smoothing": [1e-9, 1e-8, 1e-7]}),
        },
        "decision_tree": {
            "label": "DecisionTree",
            "estimator": DecisionTreeClassifier(
                class_weight="balanced",
                random_state=random_state,
            ),
            "grid": _product_grid(
                {
                    "criterion": ["gini", "entropy"],
                    "max_depth": [None, 8, 16, 24],
                    "min_samples_leaf": [1, 2, 4],
                }
            ),
        },
        "knn": {
            "label": "KNN",
            "estimator": KNeighborsClassifier(),
            "grid": _product_grid(
                {"n_neighbors": [3, 5, 9, 13], "weights": ["uniform", "distance"], "p": [1, 2]}
            ),
        },
        "mlp": {
            "label": "MLP",
            "estimator": MLPClassifier(
                max_iter=800,
                early_stopping=False,
                random_state=random_state,
            ),
            "grid": _product_grid(
                {
                    "hidden_layer_sizes": [(64,), (128,), (64, 32)],
                    "alpha": [1e-4, 1e-3],
                    "learning_rate_init": [1e-3, 5e-4],
                }
            ),
        },
        "rf": {
            "label": "RandomForest",
            "estimator": RandomForestClassifier(
                n_estimators=400,
                class_weight="balanced_subsample",
                random_state=random_state,
                n_jobs=-1,
            ),
            "grid": _product_grid(
                {"max_depth": [None, 10, 20], "min_samples_leaf": [1, 2, 4], "max_features": ["sqrt", 0.5]}
            ),
        },
    }
    if TORCH_AVAILABLE:
        registry["lstm1d"] = {
            "label": "Torch-LSTM1D",
            "estimator": TorchTabularClassifier(
                architecture="lstm1d",
                epochs=30,
                batch_size=64,
                lr=1e-3,
                weight_decay=1e-4,
                hidden_dim=96,
                dropout=0.2,
                n_layers=1,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid(
                {
                    "hidden_dim": [64, 96],
                    "n_layers": [1, 2],
                    "lr": [1e-3, 5e-4],
                    "dropout": [0.1, 0.2],
                }
            ),
        }
        registry["bilstm1d"] = {
            "label": "Torch-BiLSTM1D",
            "estimator": TorchTabularClassifier(
                architecture="bilstm1d",
                epochs=36,
                batch_size=64,
                lr=8e-4,
                weight_decay=1e-4,
                hidden_dim=128,
                dropout=0.25,
                n_layers=2,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid(
                {
                    "hidden_dim": [96, 128],
                    "n_layers": [1, 2],
                    "lr": [1e-3, 5e-4],
                    "dropout": [0.2, 0.3],
                }
            ),
        }
        registry["gru1d"] = {
            "label": "Torch-GRU1D",
            "estimator": TorchTabularClassifier(
                architecture="gru1d",
                epochs=30,
                batch_size=64,
                lr=1e-3,
                weight_decay=1e-4,
                hidden_dim=96,
                dropout=0.2,
                n_layers=1,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid(
                {
                    "hidden_dim": [64, 96],
                    "n_layers": [1, 2],
                    "lr": [1e-3, 5e-4],
                    "dropout": [0.1, 0.2],
                }
            ),
        }
        registry["bigru1d"] = {
            "label": "Torch-BiGRU1D",
            "estimator": TorchTabularClassifier(
                architecture="bigru1d",
                epochs=36,
                batch_size=64,
                lr=8e-4,
                weight_decay=1e-4,
                hidden_dim=128,
                dropout=0.25,
                n_layers=2,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid(
                {
                    "hidden_dim": [96, 128],
                    "n_layers": [1, 2],
                    "lr": [1e-3, 5e-4],
                    "dropout": [0.2, 0.3],
                }
            ),
        }
        registry["cnn1d"] = {
            "label": "Torch-CNN1D",
            "estimator": TorchTabularClassifier(
                architecture="cnn1d",
                epochs=30,
                batch_size=64,
                lr=1e-3,
                weight_decay=1e-4,
                hidden_dim=96,
                dropout=0.2,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid({"hidden_dim": [64, 96], "lr": [1e-3, 5e-4], "dropout": [0.1, 0.2]}),
        }
        registry["cnn1d_deep"] = {
            "label": "Torch-CNN1D-Deep",
            "estimator": TorchTabularClassifier(
                architecture="cnn1d",
                epochs=42,
                batch_size=64,
                lr=8e-4,
                weight_decay=2e-4,
                hidden_dim=128,
                dropout=0.25,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid(
                {
                    "hidden_dim": [96, 128, 160],
                    "lr": [1e-3, 5e-4],
                    "dropout": [0.15, 0.25],
                    "weight_decay": [1e-4, 5e-4],
                }
            ),
        }
        registry["transformer"] = {
            "label": "Torch-Transformer",
            "estimator": TorchTabularClassifier(
                architecture="transformer",
                epochs=30,
                batch_size=64,
                lr=1e-3,
                weight_decay=1e-4,
                hidden_dim=64,
                dropout=0.1,
                n_heads=4,
                n_layers=1,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid({"hidden_dim": [32, 64], "n_layers": [1, 2], "lr": [1e-3], "dropout": [0.1]}),
        }
        registry["transformer_xl"] = {
            "label": "Torch-Transformer-XL",
            "estimator": TorchTabularClassifier(
                architecture="transformer",
                epochs=42,
                batch_size=64,
                lr=7e-4,
                weight_decay=2e-4,
                hidden_dim=128,
                dropout=0.15,
                n_heads=8,
                n_layers=2,
                random_state=random_state,
                device=torch_device,
            ),
            "grid": _product_grid(
                {
                    "hidden_dim": [96, 128],
                    "n_heads": [4, 8],
                    "n_layers": [2, 3],
                    "lr": [1e-3, 5e-4],
                    "dropout": [0.1, 0.2],
                }
            ),
        }
    return registry


def _mutual_info_score(
    X: np.ndarray,
    y: np.ndarray,
    *,
    random_state: int,
) -> np.ndarray:
    return mutual_info_classif(X, y, random_state=random_state)


def _feature_selector_registry(random_state: int) -> dict[str, dict[str, Any]]:
    return {
        "none": {
            "label": "NoFeatureSelection",
            "selector": "passthrough",
            "grid": [{}],
        },
        "anova": {
            "label": "ANOVA-SelectPercentile",
            "selector": SelectPercentile(score_func=f_classif),
            "grid": _product_grid({"percentile": [25, 50, 75]}),
        },
        "mutual_info": {
            "label": "MutualInfo-SelectPercentile",
            "selector": SelectPercentile(score_func=partial(_mutual_info_score, random_state=random_state)),
            "grid": _product_grid({"percentile": [25, 50, 75]}),
        },
        "l1": {
            "label": "L1-SelectFromModel",
            "selector": SelectFromModel(
                estimator=LogisticRegression(
                    penalty="l1",
                    solver="saga",
                    class_weight="balanced",
                    max_iter=6000,
                    random_state=random_state,
                )
            ),
            "grid": _product_grid({"threshold": ["mean", "median"]}),
        },
        "tree": {
            "label": "Tree-SelectFromModel",
            "selector": SelectFromModel(
                estimator=ExtraTreesClassifier(
                    n_estimators=300,
                    class_weight="balanced_subsample",
                    random_state=random_state,
                    n_jobs=-1,
                )
            ),
            "grid": _product_grid({"threshold": ["mean", "median"]}),
        },
    }


def _prefix_param_grid(param_grid: list[dict[str, Any]], prefix: str) -> list[dict[str, Any]]:
    if not param_grid:
        return [{}]
    out: list[dict[str, Any]] = []
    for params in param_grid:
        out.append({f"{prefix}__{key}": value for key, value in params.items()})
    return out


def _cross_param_grids(left: list[dict[str, Any]], right: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not left:
        left = [{}]
    if not right:
        right = [{}]
    out: list[dict[str, Any]] = []
    for l_params in left:
        for r_params in right:
            merged = dict(l_params)
            merged.update(r_params)
            out.append(merged)
    return out


def _split_pipeline_params(params: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    model_params: dict[str, Any] = {}
    selector_params: dict[str, Any] = {}
    other_params: dict[str, Any] = {}
    for key, value in params.items():
        if key.startswith("model__"):
            model_params[key[len("model__") :]] = value
        elif key.startswith("selector__"):
            selector_params[key[len("selector__") :]] = value
        else:
            other_params[key] = value
    return model_params, selector_params, other_params


def _sample_param_grid(combos: list[dict[str, Any]], max_count: int, seed: int) -> list[dict[str, Any]]:
    if len(combos) <= max_count:
        return combos
    rng = random.Random(seed)
    picked_idx = sorted(rng.sample(range(len(combos)), max_count))
    return [combos[i] for i in picked_idx]


def _sample_plan_items(items: list[dict[str, Any]], max_count: int | None, seed: int) -> list[dict[str, Any]]:
    if max_count is None or len(items) <= max_count:
        return items
    rng = random.Random(seed)
    picked_idx = sorted(rng.sample(range(len(items)), max_count))
    return [items[i] for i in picked_idx]


def _build_pipeline(
    args: argparse.Namespace,
    estimator: BaseEstimator,
    feature_selector: Any,
) -> Pipeline:
    selector_step = feature_selector if feature_selector != "passthrough" else "passthrough"
    return Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("clip", QuantileClipper(lower_q=args.clip_lower_quantile, upper_q=args.clip_upper_quantile)),
            ("scale", RobustScaler(with_centering=True)),
            ("var", VarianceThreshold(threshold=0.0)),
            ("selector", selector_step),
            ("model", estimator),
        ]
    )


def _metric_bundle(y_true: np.ndarray, y_pred: np.ndarray, labels: list[str]) -> dict[str, Any]:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "weighted_f1": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        "confusion_matrix_labels": labels,
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=labels).tolist(),
    }


def _write_live_confusion_png(
    *,
    metrics: dict[str, Any],
    out_root: Path,
    class_scenario_name: str,
    dataset: str,
    protocol: str,
    split_id: str,
    pipeline_id: str,
    eval_index: int,
    cmap: str,
    dpi: int,
) -> Path:
    labels = [str(x) for x in metrics.get("confusion_matrix_labels", [])]
    counts = np.asarray(metrics.get("confusion_matrix", []), dtype=np.float64)
    if counts.ndim != 2 or counts.shape[0] != counts.shape[1] or counts.shape[0] != len(labels):
        raise ValueError("Confusion matrix shape/labels mismatch for live confusion PNG export.")

    support = counts.sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        norm = np.divide(counts, support[:, None], where=support[:, None] > 0.0)
    norm = np.nan_to_num(norm, nan=0.0, posinf=0.0, neginf=0.0)

    n_classes = max(1, len(labels))
    fig_w = max(6.0, min(16.0, 1.1 * n_classes + 2.0))
    fig_h = max(5.0, min(14.0, 1.0 * n_classes + 2.5))
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    im = ax.imshow(norm, interpolation="nearest", cmap=cmap, vmin=0.0, vmax=1.0)
    ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ax.set(
        xticks=np.arange(len(labels)),
        yticks=np.arange(len(labels)),
        xticklabels=labels,
        yticklabels=labels,
        ylabel="True label",
        xlabel="Predicted label",
        title=(
            f"{dataset} | {protocol} | {pipeline_id}\n"
            f"split={split_id} | scenario={class_scenario_name}"
        ),
    )
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    for i in range(norm.shape[0]):
        for j in range(norm.shape[1]):
            val = float(norm[i, j])
            cnt = int(round(float(counts[i, j])))
            text_color = "white" if val >= 0.55 else "black"
            ax.text(j, i, f"{val:.2f}\n({cnt})", ha="center", va="center", color=text_color, fontsize=8)

    fig.tight_layout()
    out_subdir = (
        out_root
        / _slug(class_scenario_name)
        / _slug(dataset)
        / _slug(protocol)
        / _slug(split_id)
    )
    out_subdir.mkdir(parents=True, exist_ok=True)
    out_path = out_subdir / f"{int(eval_index):06d}__{_slug(pipeline_id)}.png"
    fig.savefig(out_path, dpi=max(72, int(dpi)))
    plt.close(fig)
    return out_path


def _fit_predict(
    estimator: BaseEstimator,
    feature_selector: Any,
    params: dict[str, Any],
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    args: argparse.Namespace,
    warning_counter: Counter[str] | None = None,
) -> np.ndarray | None:
    model = clone(estimator)
    selector = clone(feature_selector) if feature_selector != "passthrough" else "passthrough"
    pipe = _build_pipeline(args, model, selector)
    if params:
        pipe.set_params(**params)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        warnings.filterwarnings("always", category=ConvergenceWarning)
        try:
            pipe.fit(X_train, y_train)
            y_pred = pipe.predict(X_test)
        except Exception as exc:  # noqa: BLE001
            _capture_warnings(caught, warning_counter)
            if warning_counter is not None:
                message = str(exc).strip().splitlines()[0]
                if len(message) > 160:
                    message = message[:157] + "..."
                warning_counter[f"FitError: {type(exc).__name__}: {message}"] += 1
            return None
    _capture_warnings(caught, warning_counter)
    return y_pred


def _inner_score_grouped(
    estimator: BaseEstimator,
    feature_selector: Any,
    params: dict[str, Any],
    X_train: np.ndarray,
    y_train: np.ndarray,
    groups_train: np.ndarray,
    labels: list[str],
    args: argparse.Namespace,
) -> tuple[float, dict[str, int]]:
    warning_counter: Counter[str] = Counter()
    unique_groups = np.unique(groups_train)
    if unique_groups.size < 2:
        return -1.0, {}
    n_splits = min(args.inner_folds, int(unique_groups.size))
    if n_splits < 2:
        return -1.0, {}
    splitter = GroupKFold(n_splits=n_splits)
    fold_scores: list[float] = []
    for inner_train_idx, inner_valid_idx in splitter.split(X_train, y_train, groups=groups_train):
        y_pred = _fit_predict(
            estimator=estimator,
            feature_selector=feature_selector,
            params=params,
            X_train=X_train[inner_train_idx],
            y_train=y_train[inner_train_idx],
            X_test=X_train[inner_valid_idx],
            args=args,
            warning_counter=warning_counter,
        )
        if y_pred is None:
            continue
        metrics = _metric_bundle(y_train[inner_valid_idx], y_pred, labels=labels)
        fold_scores.append(float(metrics["balanced_accuracy"]))
    return (float(mean(fold_scores)) if fold_scores else -1.0), dict(sorted(warning_counter.items()))


def _inner_score_stratified(
    estimator: BaseEstimator,
    feature_selector: Any,
    params: dict[str, Any],
    X_train: np.ndarray,
    y_train: np.ndarray,
    labels: list[str],
    args: argparse.Namespace,
    seed: int,
) -> tuple[float, dict[str, int]]:
    warning_counter: Counter[str] = Counter()
    counts = Counter(y_train.tolist())
    if not counts:
        return -1.0, {}
    min_class = min(counts.values())
    n_splits = min(args.inner_folds, int(min_class))
    if n_splits < 2:
        return -1.0, {}
    splitter = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    fold_scores: list[float] = []
    for inner_train_idx, inner_valid_idx in splitter.split(X_train, y_train):
        y_pred = _fit_predict(
            estimator=estimator,
            feature_selector=feature_selector,
            params=params,
            X_train=X_train[inner_train_idx],
            y_train=y_train[inner_train_idx],
            X_test=X_train[inner_valid_idx],
            args=args,
            warning_counter=warning_counter,
        )
        if y_pred is None:
            continue
        metrics = _metric_bundle(y_train[inner_valid_idx], y_pred, labels=labels)
        fold_scores.append(float(metrics["balanced_accuracy"]))
    return (float(mean(fold_scores)) if fold_scores else -1.0), dict(sorted(warning_counter.items()))


def _choose_best_params(
    estimator: BaseEstimator,
    feature_selector: Any,
    param_grid: list[dict[str, Any]],
    X_train: np.ndarray,
    y_train: np.ndarray,
    labels: list[str],
    args: argparse.Namespace,
    mode: str,
    groups_train: np.ndarray | None,
    seed: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    best_params = param_grid[0] if param_grid else {}
    best_score = -1.0
    tried = 0
    details: list[dict[str, Any]] = []
    warning_counter: Counter[str] = Counter()
    for params in param_grid:
        tried += 1
        if mode == "grouped":
            assert groups_train is not None
            score, warning_counts = _inner_score_grouped(
                estimator=estimator,
                feature_selector=feature_selector,
                params=params,
                X_train=X_train,
                y_train=y_train,
                groups_train=groups_train,
                labels=labels,
                args=args,
            )
        else:
            score, warning_counts = _inner_score_stratified(
                estimator=estimator,
                feature_selector=feature_selector,
                params=params,
                X_train=X_train,
                y_train=y_train,
                labels=labels,
                args=args,
                seed=seed + tried,
            )
        warning_counter.update(warning_counts)
        details.append({"params": params, "inner_balanced_accuracy": score, "warning_counts": warning_counts})
        if score > best_score:
            best_score = score
            best_params = params
    return best_params, {
        "best_inner_balanced_accuracy": best_score,
        "n_param_sets": tried,
        "scores": details,
        "warning_counts": dict(sorted(warning_counter.items())),
    }


def _load_dataset_frame(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False)


def _select_feature_columns(df: pd.DataFrame, target_col: str) -> list[str]:
    feature_cols: list[str] = []
    for col in df.columns:
        if col == target_col:
            continue
        if col in NON_FEATURE_COLUMNS:
            continue
        if col.startswith("preproc_version_"):
            continue
        if col.startswith("baseline_start_s_"):
            continue
        if col.startswith("baseline_end_s_"):
            continue
        if col.startswith("has_"):
            continue
        feature_cols.append(col)
    return feature_cols


def _prepare_dataset(
    dataset_name: str,
    dataset_path: Path,
    target_col: str,
    labels: list[str],
    class_scenario: dict[str, Any],
) -> dict[str, Any]:
    df = _load_dataset_frame(dataset_path)
    if target_col not in df.columns:
        raise ValueError(f"{dataset_name}: missing target column '{target_col}' in {dataset_path}")
    if "participant_id" not in df.columns:
        raise ValueError(f"{dataset_name}: missing participant_id column in {dataset_path}")

    df = df.copy()
    df[target_col] = df[target_col].astype(str).str.strip()
    baseline_label = class_scenario.get("baseline_from_tutorial_label")
    source_label = df[target_col].astype(str).str.strip()
    if baseline_label and "is_tutorial" in df.columns:
        tutorial_mask = df["is_tutorial"].astype(str).str.strip().str.lower() == "true"
        source_label = np.where(tutorial_mask.to_numpy(), str(baseline_label), source_label.to_numpy())
    df["_target_source_label"] = pd.Series(source_label, index=df.index, dtype="string").astype(str)

    rows_before_class_filter = int(df.shape[0])
    manifest_labels_order = list(class_scenario.get("manifest_labels", []))
    full_class_counts = _ordered_counts(df["_target_source_label"].tolist(), preferred_order=manifest_labels_order)

    allowed_original_labels_order = list(class_scenario["allowed_original_labels"])
    allowed_original_labels = set(allowed_original_labels_order)
    merge_map = {str(k): str(v) for k, v in class_scenario["merge_map"].items()}
    final_label_set = set(labels)

    df = df[df["_target_source_label"].isin(allowed_original_labels)].copy()
    rows_after_label_filter = int(df.shape[0])
    class_counts_after_label_filter = _ordered_counts(
        df["_target_source_label"].tolist(),
        preferred_order=allowed_original_labels_order,
    )
    if df.empty:
        raise ValueError(f"{dataset_name}: no rows left after class include/drop filters.")

    mapped = df["_target_source_label"].map(lambda x: str(merge_map.get(x, x)).strip())
    merge_drop_mask = mapped.str.lower().isin(DROP_LABEL_TOKENS) | (mapped == "")
    if bool(merge_drop_mask.any()):
        df = df.loc[~merge_drop_mask].copy()
        mapped = mapped.loc[~merge_drop_mask].copy()

    df["_target_label_effective"] = mapped.values
    df = df[df["_target_label_effective"].isin(final_label_set)].reset_index(drop=True)
    if df.empty:
        raise ValueError(f"{dataset_name}: no rows left after class merge/drop mapping.")

    group_col = "split_group" if "split_group" in df.columns else "participant_id"
    groups = df[group_col].astype(str).to_numpy()
    participants = df["participant_id"].astype(str).to_numpy()
    y = df["_target_label_effective"].astype(str).to_numpy()

    feature_cols = _select_feature_columns(df, target_col=target_col)
    if not feature_cols:
        raise ValueError(f"{dataset_name}: no candidate feature columns.")

    feature_df = df[feature_cols].replace({"n/a": np.nan, "": np.nan})
    for col in feature_cols:
        feature_df[col] = pd.to_numeric(feature_df[col], errors="coerce")
    valid_feature_cols = [col for col in feature_cols if feature_df[col].notna().any()]
    if not valid_feature_cols:
        raise ValueError(f"{dataset_name}: all feature columns are empty/non-numeric after coercion.")

    X = feature_df[valid_feature_cols].to_numpy(dtype=np.float64)
    row_ids = np.arange(df.shape[0], dtype=np.int64)
    trial_ids = df["trial_id"].astype(str).to_numpy() if "trial_id" in df.columns else np.array([""] * df.shape[0])

    return {
        "name": dataset_name,
        "path": str(dataset_path),
        "df": df,
        "X": X,
        "y": y,
        "groups": groups,
        "participants": participants,
        "row_ids": row_ids,
        "trial_ids": trial_ids,
        "feature_columns": valid_feature_cols,
        "class_counts": _ordered_counts(y.tolist(), preferred_order=labels),
        "full_class_counts": full_class_counts,
        "class_counts_after_label_filter": class_counts_after_label_filter,
        "rows_before_class_filter": rows_before_class_filter,
        "rows_after_label_filter": rows_after_label_filter,
        "rows_after_class_mapping": int(df.shape[0]),
    }


def _subset_by_participants(payload: dict[str, Any], participants: list[str]) -> tuple[np.ndarray, np.ndarray]:
    wanted = set(participants)
    participant_col = payload["participants"]
    mask = np.isin(participant_col, list(wanted))
    idx = np.where(mask)[0]
    return idx, mask


def _aggregate_metric_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        feature_selector = str(row.get("feature_selector", "none"))
        pipeline_id = str(row.get("pipeline_id", f"{row['model']}+{feature_selector}"))
        grouped[(row["dataset"], row["protocol"], row["model"], feature_selector, pipeline_id)].append(row)

    out: list[dict[str, Any]] = []
    for (dataset, protocol, model, feature_selector, pipeline_id), items in sorted(grouped.items()):
        acc = [float(x["metrics"]["accuracy"]) for x in items]
        bacc = [float(x["metrics"]["balanced_accuracy"]) for x in items]
        mf1 = [float(x["metrics"]["macro_f1"]) for x in items]
        wf1 = [float(x["metrics"]["weighted_f1"]) for x in items]
        out.append(
            {
                "dataset": dataset,
                "protocol": protocol,
                "model": model,
                "feature_selector": feature_selector,
                "pipeline_id": pipeline_id,
                "n_evaluations": len(items),
                "accuracy_mean": float(mean(acc)),
                "accuracy_std": float(pstdev(acc)) if len(acc) > 1 else 0.0,
                "balanced_accuracy_mean": float(mean(bacc)),
                "balanced_accuracy_std": float(pstdev(bacc)) if len(bacc) > 1 else 0.0,
                "macro_f1_mean": float(mean(mf1)),
                "macro_f1_std": float(pstdev(mf1)) if len(mf1) > 1 else 0.0,
                "weighted_f1_mean": float(mean(wf1)),
                "weighted_f1_std": float(pstdev(wf1)) if len(wf1) > 1 else 0.0,
            }
        )
    return out


def _best_model_by_dataset_protocol(aggregate_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in aggregate_rows:
        grouped[(row["dataset"], row["protocol"])].append(row)
    out: list[dict[str, Any]] = []
    for (dataset, protocol), items in sorted(grouped.items()):
        ranked = sorted(
            items,
            key=lambda x: (x["balanced_accuracy_mean"], x["macro_f1_mean"], -x["balanced_accuracy_std"]),
            reverse=True,
        )
        out.append(
            {
                "dataset": dataset,
                "protocol": protocol,
                "best_model": ranked[0]["model"],
                "best_feature_selector": ranked[0].get("feature_selector", "none"),
                "best_pipeline": ranked[0].get("pipeline_id", ranked[0]["model"]),
                "balanced_accuracy_mean": ranked[0]["balanced_accuracy_mean"],
                "macro_f1_mean": ranked[0]["macro_f1_mean"],
                "n_evaluations": ranked[0]["n_evaluations"],
            }
        )
    return out


def _aggregate_warning_counts(evaluations: list[dict[str, Any]]) -> dict[str, int]:
    warning_counter: Counter[str] = Counter()
    for row in evaluations:
        warning_payload = row.get("warning_counts", {})
        if not isinstance(warning_payload, dict):
            continue
        for section in ("tuning", "outer_fit_predict"):
            section_payload = warning_payload.get(section, {})
            if not isinstance(section_payload, dict):
                continue
            for key, count in section_payload.items():
                warning_counter[str(key)] += int(count)
    return {k: warning_counter[k] for k in sorted(warning_counter, key=lambda x: (-warning_counter[x], x))}


def _protocol_debug_label(protocol: str) -> str:
    mapping = {
        "within_participant": "single_participant",
        "group_holdout": "group",
        "loso": "loso",
        "pooled_stratified": "pooled_mixed",
        "pooled_stratified_holdout": "pooled_mixed",
        "pooled_stratified_one_fold": "pooled_mixed",
    }
    return mapping.get(protocol, protocol)


def _dataset_protocol_coverage(
    aggregate_rows: list[dict[str, Any]],
    datasets: list[str],
    protocols: list[str],
    min_aggregate_rows_per_pair: int,
) -> dict[str, Any]:
    pair_counts: Counter[tuple[str, str]] = Counter()
    for row in aggregate_rows:
        dataset = str(row.get("dataset", ""))
        protocol = str(row.get("protocol", ""))
        if not dataset or not protocol:
            continue
        pair_counts[(dataset, protocol)] += 1

    pairs_summary: list[dict[str, Any]] = []
    missing_pairs: list[dict[str, Any]] = []
    for dataset in datasets:
        for protocol in protocols:
            count = int(pair_counts.get((dataset, protocol), 0))
            entry = {"dataset": dataset, "protocol": protocol, "aggregate_rows": count}
            pairs_summary.append(entry)
            if min_aggregate_rows_per_pair > 0 and count < min_aggregate_rows_per_pair:
                missing_pairs.append(entry)

    return {
        "min_aggregate_rows_per_pair": int(min_aggregate_rows_per_pair),
        "pairs": pairs_summary,
        "missing_pairs": missing_pairs,
    }


def _build_summary_markdown(
    config: dict[str, Any],
    dataset_stats: list[dict[str, Any]],
    aggregate_rows: list[dict[str, Any]],
    best_rows: list[dict[str, Any]],
    warning_counts_total: dict[str, int],
    coverage: dict[str, Any],
    skip_counts: dict[str, int],
    eeg_condition_psd: dict[str, Any] | None,
) -> str:
    lines: list[str] = []
    lines.append("# Stage 6 ML Summary")
    lines.append("")
    lines.append("## Config")
    lines.append(f"- Target: `{config['target']}` (`{config['target_column']}`)")
    lines.append(f"- Protocols: `{', '.join(config['protocols'])}`")
    lines.append(f"- Models: `{', '.join(config['models'])}`")
    lines.append(f"- Feature selectors: `{', '.join(config['feature_selectors'])}`")
    lines.append(f"- Datasets: `{', '.join(config['datasets'])}`")
    lines.append(f"- Inner folds: `{config['inner_folds']}`")
    lines.append(f"- Max param combos/model: `{config['max_param_combos']}`")
    lines.append(f"- Pooled stratified folds: `{config.get('pooled_stratified_folds', 'n/a')}`")
    lines.append(
        f"- Pooled no-folds mode: "
        f"`{config.get('pooled_stratified_no_folds', False)}`"
    )
    lines.append(
        f"- Pooled test size: "
        f"`{config.get('pooled_stratified_test_size', 'n/a')}`"
    )
    lines.append(
        f"- Within-participant no-folds mode: "
        f"`{config.get('within_participant_no_folds', False)}`"
    )
    lines.append(
        f"- Within-participant test size: "
        f"`{config.get('within_participant_test_size', 'n/a')}`"
    )
    lines.append(f"- Torch available: `{config.get('torch_available', False)}`")
    lines.append(
        f"- Torch device requested/effective: "
        f"`{config.get('torch_device_requested', 'auto')}` -> `{config.get('torch_device_effective', 'cpu')}`"
    )
    lines.append(f"- NVIDIA GPU detected: `{config.get('nvidia_gpu_detected', False)}`")
    gpu_names = [str(x) for x in config.get("nvidia_gpu_names", []) if str(x).strip()]
    if gpu_names:
        lines.append(f"- NVIDIA GPU names: `{', '.join(gpu_names)}`")
    lines.append(f"- Live confusion PNGs during training: `{config.get('live_confusion_pngs', False)}`")
    lines.append(f"- EEG condition PSD plots: `{config.get('eeg_condition_psd_plots', False)}`")
    class_cfg = config.get("class_scenario", {})
    lines.append(f"- Class scenario: `{class_cfg.get('name', 'default')}`")
    lines.append(f"- Final labels: `{', '.join(class_cfg.get('final_labels', []))}`")
    lines.append("")
    lines.append("## EEG PSD / Topomap QC")
    if eeg_condition_psd:
        lines.append(f"- Status: `{eeg_condition_psd.get('status', 'unknown')}`")
        manifest_json = str(eeg_condition_psd.get("manifest_json", "") or "").strip()
        if manifest_json:
            lines.append(f"- Manifest: `{manifest_json}`")
        all_participants_png = str(eeg_condition_psd.get("all_participants_png", "") or "").strip()
        if all_participants_png:
            lines.append(f"- All participants PSD PNG: `{all_participants_png}`")
        all_participants_topomap_png = str(eeg_condition_psd.get("all_participants_topomap_png", "") or "").strip()
        if all_participants_topomap_png:
            lines.append(f"- All participants topomap PNG: `{all_participants_topomap_png}`")
        roi_reference_topomap_png = str(eeg_condition_psd.get("roi_reference_topomap_png", "") or "").strip()
        if roi_reference_topomap_png:
            lines.append(f"- EEG ROI reference PNG: `{roi_reference_topomap_png}`")
        if eeg_condition_psd.get("status") == "ok":
            lines.append(
                f"- Participants plotted: `{int(eeg_condition_psd.get('n_participants_plotted', 0))}`"
            )
            label_order_plotted = [str(x) for x in eeg_condition_psd.get("label_order_plotted", []) if str(x).strip()]
            if label_order_plotted:
                lines.append(f"- Conditions plotted: `{', '.join(label_order_plotted)}`")
        reason = str(eeg_condition_psd.get("reason", "") or "").strip()
        if reason:
            lines.append(f"- Note: `{reason}`")
    else:
        lines.append("- Status: disabled")
    lines.append("")
    lines.append("## Dataset Snapshot")
    for ds in dataset_stats:
        lines.append(
            f"- `{ds['dataset']}`: rows={ds['rows']}, features={ds['n_features']}, "
            f"participants={ds['n_participants']}, classes={ds['n_classes']}"
        )
    lines.append("")
    lines.append("## Coverage")
    lines.append(
        f"- Minimum aggregate rows required per dataset+protocol: `{coverage.get('min_aggregate_rows_per_pair', 0)}`"
    )
    missing_pairs = list(coverage.get("missing_pairs", []))
    if missing_pairs:
        lines.append("- Missing pairs:")
        for pair in missing_pairs:
            lines.append(
                f"  - `{pair['dataset']}` + `{pair['protocol']}` "
                f"(aggregate_rows={int(pair.get('aggregate_rows', 0))})"
            )
    else:
        lines.append("- Missing pairs: none")
    lines.append("")
    lines.append("| dataset | protocol | aggregate_rows |")
    lines.append("|---|---|---:|")
    for pair in coverage.get("pairs", []):
        lines.append(
            f"| {pair['dataset']} | {pair['protocol']} | {int(pair.get('aggregate_rows', 0))} |"
        )
    lines.append("")
    lines.append("## Best By Dataset/Protocol")
    if best_rows:
        for row in best_rows:
            lines.append(
                f"- `{row['dataset']}` + `{row['protocol']}` -> `{row.get('best_pipeline', row['best_model'])}` "
                f"(balanced_acc={row['balanced_accuracy_mean']:.4f}, macro_f1={row['macro_f1_mean']:.4f}, "
                f"n={row['n_evaluations']})"
            )
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Aggregates")
    lines.append("| dataset | protocol | model | feature_selector | pipeline_id | n | balanced_acc_mean | macro_f1_mean |")
    lines.append("|---|---|---|---|---|---:|---:|---:|")
    if aggregate_rows:
        for row in aggregate_rows:
            lines.append(
                f"| {row['dataset']} | {row['protocol']} | {row['model']} | {row.get('feature_selector', 'none')} | "
                f"{row.get('pipeline_id', row['model'])} | {row['n_evaluations']} | "
                f"{row['balanced_accuracy_mean']:.4f} | {row['macro_f1_mean']:.4f} |"
            )
    else:
        lines.append("| n/a | n/a | n/a | n/a | n/a | 0 | 0.0000 | 0.0000 |")
    lines.append("")
    lines.append("## Skip Summary")
    if skip_counts:
        for key, count in sorted(skip_counts.items(), key=lambda x: (-x[1], x[0])):
            lines.append(f"- {key}: {count}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Warning Summary")
    if warning_counts_total:
        for key, count in warning_counts_total.items():
            lines.append(f"- {key}: {count}")
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Stage 6 classic ML battery with leakage-safe preprocessing and "
            "multiple evaluation protocols (within-participant, LOSO, grouped holdout, pooled stratified)."
        )
    )
    parser.add_argument("--bids-root", required=True, help="Path to BIDS root.")
    parser.add_argument("--split-manifest", default=None, help="Path to split_manifest.json.")
    parser.add_argument("--datasets", nargs="*", default=None, help="Datasets to evaluate (from split manifest).")
    parser.add_argument(
        "--protocols",
        nargs="*",
        default=None,
        help=(
            "Evaluation protocols: loso group_holdout within_participant "
            "pooled_stratified pooled_stratified_holdout pooled_stratified_one_fold "
            "(default: all)."
        ),
    )
    parser.add_argument(
        "--models",
        nargs="*",
        default=None,
        help=(
            "Models (default: all available): logreg knn svm gaussian_nb decision_tree mlp rf "
            "[lstm1d gru1d cnn1d transformer bilstm1d bigru1d cnn1d_deep transformer_xl if torch installed]."
        ),
    )
    parser.add_argument(
        "--feature-selectors",
        nargs="*",
        default=None,
        help="Feature selectors (default: none): none anova mutual_info l1 tree.",
    )
    parser.add_argument("--inner-folds", type=int, default=4, help="Inner CV folds for hyperparameter tuning.")
    parser.add_argument(
        "--max-param-combos",
        type=int,
        default=12,
        help="Max hyperparameter combinations evaluated per model+selector pipeline per outer split.",
    )
    parser.add_argument(
        "--max-outer-splits-per-protocol",
        type=int,
        default=None,
        help="Optional cap on outer splits per protocol for quick runs.",
    )
    parser.add_argument(
        "--pooled-stratified-folds",
        type=int,
        default=5,
        help=(
            "Number of folds for pooled_stratified protocol "
            "(all participants mixed; row-level stratified CV)."
        ),
    )
    parser.add_argument(
        "--pooled-stratified-no-folds",
        action="store_true",
        help=(
            "Use one stratified holdout split for pooled_stratified "
            "(instead of K-fold CV)."
        ),
    )
    parser.add_argument(
        "--pooled-stratified-test-size",
        type=float,
        default=0.20,
        help=(
            "Test fraction for --pooled-stratified-no-folds "
            "(default: 0.20)."
        ),
    )
    parser.add_argument(
        "--within-participant-no-folds",
        action="store_true",
        help=(
            "Use one stratified holdout split per participant for within_participant "
            "(instead of K-fold CV)."
        ),
    )
    parser.add_argument(
        "--within-participant-test-size",
        type=float,
        default=0.20,
        help=(
            "Test fraction for --within-participant-no-folds "
            "(default: 0.20)."
        ),
    )
    parser.add_argument(
        "--min-aggregate-rows-per-dataset-protocol",
        type=int,
        default=1,
        help=(
            "Minimum aggregate rows required per dataset+protocol pair. "
            "Set to 0 to disable coverage checks."
        ),
    )
    parser.add_argument(
        "--allow-incomplete-coverage",
        action="store_true",
        help="Do not fail if dataset+protocol coverage checks are not met.",
    )
    parser.add_argument("--clip-lower-quantile", type=float, default=0.01)
    parser.add_argument("--clip-upper-quantile", type=float, default=0.99)
    parser.add_argument("--random-seed", type=int, default=42)
    parser.add_argument(
        "--baseline-from-tutorial-label",
        default=None,
        help=(
            "Optional label to assign tutorial rows before class filtering/merging "
            "(for tutorial-as-baseline proxy experiments)."
        ),
    )
    parser.add_argument(
        "--class-scenario-name",
        default="default",
        help="Name for this class scenario (recorded in run metadata).",
    )
    parser.add_argument(
        "--class-include-labels",
        nargs="*",
        default=None,
        help="Optional subset of original labels to keep before merging.",
    )
    parser.add_argument(
        "--class-drop-labels",
        nargs="*",
        default=None,
        help="Optional original labels to omit before merging.",
    )
    parser.add_argument(
        "--class-merge",
        action="append",
        default=None,
        help=(
            "Repeatable label merge mapping. Formats: old->new, old:new, old=new. "
            "Example: --class-merge 0.6-1.5->low --class-merge 1.5-2.4->low"
        ),
    )
    parser.add_argument(
        "--class-merge-json",
        default=None,
        help="Optional JSON file with merge mapping object: {\"old_label\": \"new_label\", ...}.",
    )
    parser.add_argument("--run-tag", default=None, help="Optional model run tag.")
    parser.add_argument("--results-json", default=None, help="Output JSON path (default: reports/ml_results.json).")
    parser.add_argument("--summary-md", default=None, help="Output markdown path (default: reports/ml_summary.md).")
    parser.add_argument(
        "--eeg-condition-psd-plots",
        dest="eeg_condition_psd_plots",
        action="store_true",
        default=True,
        help=(
            "Write scenario-aware EEG power spectrum QC plots by ROI for all participants "
            "and each single participant (default: enabled)."
        ),
    )
    parser.add_argument(
        "--no-eeg-condition-psd-plots",
        dest="eeg_condition_psd_plots",
        action="store_false",
        help="Disable scenario-aware EEG power spectrum QC plots.",
    )
    parser.add_argument(
        "--eeg-condition-psd-dir",
        default=None,
        help="Output root for scenario-aware EEG PSD plots (default: analysis_pipeline/reports/eeg_condition_psd).",
    )
    parser.add_argument(
        "--eeg-condition-psd-fmin",
        type=float,
        default=2.0,
        help="Minimum frequency for EEG condition PSD plots (default: 2.0 Hz).",
    )
    parser.add_argument(
        "--eeg-condition-psd-fmax",
        type=float,
        default=40.0,
        help="Maximum frequency for EEG condition PSD plots (default: 40.0 Hz).",
    )
    parser.add_argument(
        "--live-confusion-pngs",
        dest="live_confusion_pngs",
        action="store_true",
        default=True,
        help="Write a confusion PNG for each evaluated model/split as training runs (default: enabled).",
    )
    parser.add_argument(
        "--no-live-confusion-pngs",
        dest="live_confusion_pngs",
        action="store_false",
        help="Disable per-evaluation live confusion PNG writing.",
    )
    parser.add_argument(
        "--live-confusion-png-dir",
        default=None,
        help="Directory for per-evaluation live confusion PNGs (default: analysis_pipeline/reports/confusion_pngs_live).",
    )
    parser.add_argument(
        "--live-confusion-png-cmap",
        default="Blues",
        help="Matplotlib colormap for live confusion PNGs.",
    )
    parser.add_argument(
        "--live-confusion-png-dpi",
        type=int,
        default=150,
        help="PNG DPI for live confusion PNGs (default: 150).",
    )
    parser.add_argument("--models-root", default=None, help="Model artifact root (default: analysis_pipeline/models).")
    parser.add_argument(
        "--torch-device",
        default="auto",
        help="Torch device for deep models: auto (default), cpu, cuda, cuda:0, etc.",
    )
    args = parser.parse_args()

    if args.inner_folds < 2:
        raise ValueError("--inner-folds must be >= 2.")
    if args.max_param_combos < 1:
        raise ValueError("--max-param-combos must be >= 1.")
    if args.pooled_stratified_folds < 2:
        raise ValueError("--pooled-stratified-folds must be >= 2.")
    if args.pooled_stratified_test_size <= 0 or args.pooled_stratified_test_size >= 1:
        raise ValueError("--pooled-stratified-test-size must be within (0,1).")
    if args.within_participant_test_size <= 0 or args.within_participant_test_size >= 1:
        raise ValueError("--within-participant-test-size must be within (0,1).")
    if args.min_aggregate_rows_per_dataset_protocol < 0:
        raise ValueError("--min-aggregate-rows-per-dataset-protocol must be >= 0.")
    if args.live_confusion_png_dpi < 72:
        raise ValueError("--live-confusion-png-dpi must be >= 72.")
    if args.clip_lower_quantile < 0 or args.clip_lower_quantile >= 1:
        raise ValueError("--clip-lower-quantile must be within [0,1).")
    if args.clip_upper_quantile <= 0 or args.clip_upper_quantile > 1:
        raise ValueError("--clip-upper-quantile must be within (0,1].")
    if args.clip_lower_quantile >= args.clip_upper_quantile:
        raise ValueError("clip lower quantile must be less than clip upper quantile.")
    if args.eeg_condition_psd_fmin < 0:
        raise ValueError("--eeg-condition-psd-fmin must be >= 0.")
    if args.eeg_condition_psd_fmax <= args.eeg_condition_psd_fmin:
        raise ValueError("--eeg-condition-psd-fmax must be greater than --eeg-condition-psd-fmin.")
    args.torch_device = str(args.torch_device or "auto").strip() or "auto"
    if not TORCH_AVAILABLE and args.torch_device.lower() != "auto":
        raise ValueError("PyTorch is not installed, so --torch-device cannot be set.")
    if TORCH_AVAILABLE and args.torch_device.lower().startswith("cuda"):
        if torch is None or not torch.cuda.is_available():
            raise ValueError(f"Requested torch device '{args.torch_device}' but CUDA is not available.")

    bids_root = _resolve_bids_root(args.bids_root)
    if not bids_root.exists():
        raise FileNotFoundError(bids_root)

    split_manifest_path = Path(args.split_manifest).resolve() if args.split_manifest else _default_split_manifest()
    if not split_manifest_path.exists():
        raise FileNotFoundError(split_manifest_path)
    split_manifest = json.loads(split_manifest_path.read_text(encoding="utf-8"))

    target_col = str(split_manifest.get("target_column", "target_label"))
    class_scenario = _build_class_scenario(split_manifest, args)
    labels = list(class_scenario["final_labels"])

    datasets = _coerce_dataset_list(split_manifest, args.datasets)
    protocols = _coerce_protocol_list(args.protocols)
    models = _coerce_model_list(args.models)
    feature_selectors = _coerce_feature_selector_list(args.feature_selectors)
    torch_device_effective = _resolve_torch_runtime_device(args.torch_device)
    nvidia_gpu_detected, nvidia_gpu_names, nvidia_probe_message = _detect_nvidia_gpus()
    registry = _model_registry(random_state=args.random_seed, torch_device=args.torch_device)
    selector_registry = _feature_selector_registry(random_state=args.random_seed)
    stage_started = time.time()

    print("Stage 6 starting.")
    print(f"  Datasets: {', '.join(datasets)}")
    print(f"  Protocols: {', '.join(protocols)}")
    print(f"  Models: {', '.join(models)}")
    print(f"  Feature selectors: {', '.join(feature_selectors)}")
    print(f"  Class scenario: {class_scenario['name']} ({len(labels)} classes)")
    print(f"  Torch available: {TORCH_AVAILABLE}")
    print(f"  NVIDIA GPU detected: {nvidia_gpu_detected}")
    if nvidia_gpu_detected:
        print(f"  NVIDIA GPUs: {', '.join(nvidia_gpu_names)}")
    elif nvidia_probe_message:
        print(f"  NVIDIA probe note: {nvidia_probe_message}")
    if TORCH_AVAILABLE:
        print(f"  Torch device requested: {args.torch_device}")
        print(f"  Torch device effective: {torch_device_effective}")
        if torch_device_effective.startswith("cuda") and torch is not None and torch.cuda.is_available():
            print(f"  CUDA device name: {torch.cuda.get_device_name(0)}")
        elif nvidia_gpu_detected and (torch is None or not torch.cuda.is_available()):
            print(
                "  WARNING: NVIDIA GPU detected but torch.cuda.is_available() is False. "
                "Install a CUDA-enabled PyTorch build to run deep models on GPU."
            )
    elif nvidia_gpu_detected:
        print(
            "  WARNING: NVIDIA GPU detected but PyTorch is unavailable. "
            "Deep models require a CUDA-enabled PyTorch installation."
        )

    results_json = Path(args.results_json).resolve() if args.results_json else _default_results_json()
    summary_md = Path(args.summary_md).resolve() if args.summary_md else _default_summary_md()
    models_root = Path(args.models_root).resolve() if args.models_root else _models_root()
    live_confusion_png_dir = (
        Path(args.live_confusion_png_dir).resolve()
        if args.live_confusion_png_dir
        else _default_live_confusion_png_dir()
    )
    eeg_condition_psd_dir = (
        Path(args.eeg_condition_psd_dir).resolve()
        if args.eeg_condition_psd_dir
        else _default_eeg_condition_psd_dir()
    )

    run_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_tag = args.run_tag.strip() if args.run_tag else "default"
    run_dir = models_root / f"stage6_{run_stamp}_{run_tag}"
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"  Run dir: {run_dir}")
    print(f"  Live confusion PNGs: {bool(args.live_confusion_pngs)}")
    if args.live_confusion_pngs:
        live_confusion_png_dir.mkdir(parents=True, exist_ok=True)
        print(f"  Live confusion PNG dir: {live_confusion_png_dir}")
    print(f"  EEG condition PSD plots: {bool(args.eeg_condition_psd_plots)}")
    if args.eeg_condition_psd_plots:
        print(f"  EEG condition PSD dir: {eeg_condition_psd_dir}")

    dataset_payloads: dict[str, dict[str, Any]] = {}
    dataset_stats: list[dict[str, Any]] = []
    for dataset_idx, dataset_name in enumerate(datasets, start=1):
        print(f"[Dataset {dataset_idx}/{len(datasets)}] Loading '{dataset_name}'...")
        dataset_path = _resolve_dataset_path(
            path_text=str(split_manifest["datasets"][dataset_name]["path"]),
            split_manifest_path=split_manifest_path,
        )
        payload = _prepare_dataset(
            dataset_name=dataset_name,
            dataset_path=dataset_path,
            target_col=target_col,
            labels=labels,
            class_scenario=class_scenario,
        )
        dataset_payloads[dataset_name] = payload
        dataset_stats.append(
            {
                "dataset": dataset_name,
                "path": payload["path"],
                "rows": int(payload["X"].shape[0]),
                "n_features": int(payload["X"].shape[1]),
                "n_participants": int(len(set(payload["participants"].tolist()))),
                "n_classes": int(len(set(payload["y"].tolist()))),
                "class_counts": payload["class_counts"],
                "full_class_counts": payload["full_class_counts"],
                "class_counts_after_label_filter": payload["class_counts_after_label_filter"],
                "rows_before_class_filter": payload["rows_before_class_filter"],
                "rows_after_label_filter": payload["rows_after_label_filter"],
                "rows_after_class_mapping": payload["rows_after_class_mapping"],
            }
        )
        print(
            f"  Loaded '{dataset_name}': rows={payload['X'].shape[0]} "
            f"features={payload['X'].shape[1]} participants={len(set(payload['participants'].tolist()))}"
        )

    eeg_condition_psd: dict[str, Any] | None = None
    if args.eeg_condition_psd_plots:
        epoch_manifest_path: Path | None = None
        epoch_manifest_value = split_manifest.get("epoch_manifest")
        if epoch_manifest_value:
            epoch_manifest_path = _resolve_dataset_path(str(epoch_manifest_value), split_manifest_path)
        eeg_payload = dataset_payloads.get("eeg")
        eeg_condition_psd = build_condition_psd_report(
            eeg_df=(eeg_payload["df"] if eeg_payload is not None else None),
            epoch_manifest_path=epoch_manifest_path,
            out_dir=eeg_condition_psd_dir / _slug(class_scenario["name"]),
            scenario_name=class_scenario["name"],
            label_order=labels,
            fmin=float(args.eeg_condition_psd_fmin),
            fmax=float(args.eeg_condition_psd_fmax),
        )
        print(f"  EEG condition PSD status: {eeg_condition_psd.get('status', 'unknown')}")
        print(f"  EEG condition PSD manifest: {eeg_condition_psd.get('manifest_json', '')}")
        if eeg_condition_psd.get("all_participants_png"):
            print(f"  EEG condition PSD all participants PNG: {eeg_condition_psd['all_participants_png']}")
        if eeg_condition_psd.get("all_participants_topomap_png"):
            print(f"  EEG condition topomap all participants PNG: {eeg_condition_psd['all_participants_topomap_png']}")

    evaluations: list[dict[str, Any]] = []
    skip_counts: Counter[str] = Counter()
    live_confusion_png_count = 0

    global_strategies = split_manifest.get("strategies", {}) or {}
    dataset_strategy_map = split_manifest.get("dataset_strategies", {}) or {}

    dataset_protocol_total = len(datasets) * len(protocols)
    dataset_protocol_idx = 0
    for dataset_name in datasets:
        payload = dataset_payloads[dataset_name]
        X = payload["X"]
        y = payload["y"]
        groups = payload["groups"]
        participants = payload["participants"]
        dataset_strategies = dataset_strategy_map.get(dataset_name, {}) or {}
        strategy_map = {
            "loso": dataset_strategies.get(
                "leave_one_participant_out",
                global_strategies.get("leave_one_participant_out", []),
            ),
            "group_holdout": dataset_strategies.get(
                "group_holdout",
                global_strategies.get("group_holdout", []),
            ),
            "within_participant": dataset_strategies.get(
                "within_participant",
                global_strategies.get("within_participant", []),
            ),
        }

        for protocol in protocols:
            dataset_protocol_idx += 1
            protocol_debug = _protocol_debug_label(protocol)
            print(
                f"[Evaluation {dataset_protocol_idx}/{dataset_protocol_total}] "
                f"dataset={dataset_name} protocol={protocol} "
                f"classification_set={protocol_debug} class_scenario={class_scenario['name']}"
            )
            if protocol in ("loso", "group_holdout"):
                split_plan = _sample_plan_items(
                    items=list(strategy_map.get(protocol, [])),
                    max_count=args.max_outer_splits_per_protocol,
                    seed=args.random_seed + len(dataset_name) + len(protocol),
                )
                print(f"  Planned outer splits: {len(split_plan)}")

                for split_index, split_item in enumerate(split_plan, start=1):
                    train_participants = list(split_item.get("train_participants", []))
                    test_participants = list(split_item.get("test_participants", []))
                    train_idx, _ = _subset_by_participants(payload, train_participants)
                    test_idx, _ = _subset_by_participants(payload, test_participants)
                    if train_idx.size < 10 or test_idx.size < 2:
                        skip_counts[f"{dataset_name}:{protocol}:split_insufficient_rows"] += 1
                        continue

                    y_train = y[train_idx]
                    y_test = y[test_idx]
                    if len(set(y_train.tolist())) < 2:
                        skip_counts[f"{dataset_name}:{protocol}:split_single_train_class"] += 1
                        continue

                    X_train = X[train_idx]
                    X_test = X[test_idx]
                    groups_train = groups[train_idx]
                    split_name = str(split_item.get("split_id", f"{protocol}_{split_index:03d}"))
                    print(
                        f"    Split {split_index}/{len(split_plan)} ({split_name}): "
                        f"train_rows={train_idx.size} test_rows={test_idx.size} "
                        f"model_selectors={len(models)}x{len(feature_selectors)}"
                    )

                    combo_total = len(models) * len(feature_selectors)
                    combo_idx = 0
                    for model_key in models:
                        model_spec = registry[model_key]
                        estimator = model_spec["estimator"]
                        model_label = str(model_spec.get("label", model_key))
                        model_grid = _prefix_param_grid(list(model_spec["grid"]), prefix="model")
                        for selector_key in feature_selectors:
                            combo_idx += 1
                            print(
                                f"      [Train {combo_idx}/{combo_total}] "
                                f"dataset={dataset_name} class_scenario={class_scenario['name']} "
                                f"classification_set={protocol_debug} protocol={protocol} "
                                f"split={split_name} model={model_key} selector={selector_key}"
                            )
                            selector_spec = selector_registry[selector_key]
                            selector = selector_spec["selector"]
                            selector_label = str(selector_spec.get("label", selector_key))
                            selector_grid = _prefix_param_grid(list(selector_spec["grid"]), prefix="selector")
                            all_combos = _cross_param_grids(model_grid, selector_grid)
                            param_grid = _sample_param_grid(
                                combos=all_combos,
                                max_count=args.max_param_combos,
                                seed=(
                                    args.random_seed
                                    + split_index
                                    + len(dataset_name)
                                    + len(model_key)
                                    + len(selector_key)
                                ),
                            )
                            best_params, tune_summary = _choose_best_params(
                                estimator=estimator,
                                feature_selector=selector,
                                param_grid=param_grid,
                                X_train=X_train,
                                y_train=y_train,
                                labels=labels,
                                args=args,
                                mode="grouped",
                                groups_train=groups_train,
                                seed=args.random_seed + split_index,
                            )

                            outer_warning_counter: Counter[str] = Counter()
                            y_pred = _fit_predict(
                                estimator=estimator,
                                feature_selector=selector,
                                params=best_params,
                                X_train=X_train,
                                y_train=y_train,
                                X_test=X_test,
                                args=args,
                                warning_counter=outer_warning_counter,
                            )
                            if y_pred is None:
                                skip_counts[f"{dataset_name}:{protocol}:fit_predict_failed"] += 1
                                continue
                            metrics = _metric_bundle(y_test, y_pred, labels=labels)
                            best_model_params, best_selector_params, best_other_params = _split_pipeline_params(best_params)
                            pipeline_id = f"{model_key}+{selector_key}"
                            eval_row: dict[str, Any] = {
                                "dataset": dataset_name,
                                "protocol": protocol,
                                "model": model_key,
                                "model_label": model_label,
                                "feature_selector": selector_key,
                                "feature_selector_label": selector_label,
                                "pipeline_id": pipeline_id,
                                "pipeline_label": f"{model_label} + {selector_label}",
                                "split_id": split_name,
                                "n_train_rows": int(train_idx.size),
                                "n_test_rows": int(test_idx.size),
                                "n_train_participants": int(len(set(participants[train_idx].tolist()))),
                                "n_test_participants": int(len(set(participants[test_idx].tolist()))),
                                "best_params": best_params,
                                "best_model_params": best_model_params,
                                "best_feature_selector_params": best_selector_params,
                                "best_pipeline_other_params": best_other_params,
                                "tuning": tune_summary,
                                "warning_counts": {
                                    "tuning": tune_summary.get("warning_counts", {}),
                                    "outer_fit_predict": dict(sorted(outer_warning_counter.items())),
                                },
                                "metrics": metrics,
                            }
                            if args.live_confusion_pngs:
                                live_png = _write_live_confusion_png(
                                    metrics=metrics,
                                    out_root=live_confusion_png_dir,
                                    class_scenario_name=class_scenario["name"],
                                    dataset=dataset_name,
                                    protocol=protocol,
                                    split_id=split_name,
                                    pipeline_id=pipeline_id,
                                    eval_index=len(evaluations) + 1,
                                    cmap=str(args.live_confusion_png_cmap),
                                    dpi=int(args.live_confusion_png_dpi),
                                )
                                live_confusion_png_count += 1
                                eval_row["confusion_png_live"] = str(live_png)
                                print(f"        Live confusion PNG: {live_png}")
                            evaluations.append(eval_row)
            elif protocol == "within_participant":
                within_plan = _sample_plan_items(
                    items=list(strategy_map.get("within_participant", [])),
                    max_count=args.max_outer_splits_per_protocol,
                    seed=args.random_seed + len(dataset_name) + 17,
                )
                print(f"  Candidate within-participant entries: {len(within_plan)}")
                for within_item in within_plan:
                    participant_id = str(within_item.get("participant_id", ""))
                    if not participant_id:
                        skip_counts[f"{dataset_name}:{protocol}:missing_participant_id"] += 1
                        continue
                    if not bool(within_item.get("eligible_for_within_participant_cv", False)):
                        skip_counts[f"{dataset_name}:{protocol}:participant_not_eligible"] += 1
                        continue
                    participant_mask = participants == participant_id
                    idx_all = np.where(participant_mask)[0]
                    if idx_all.size < 8:
                        skip_counts[f"{dataset_name}:{protocol}:participant_rows_lt8"] += 1
                        continue
                    y_participant = y[idx_all]
                    counts = Counter(y_participant.tolist())
                    if len(counts) < 2:
                        skip_counts[f"{dataset_name}:{protocol}:participant_single_class"] += 1
                        continue
                    participant_seed = _stable_seed_from_text(participant_id, args.random_seed)
                    if args.within_participant_no_folds:
                        min_class_support = min(counts.values())
                        if min_class_support < 2:
                            skip_counts[f"{dataset_name}:{protocol}:class_support_lt2_no_fold"] += 1
                            continue
                        splitter = StratifiedShuffleSplit(
                            n_splits=1,
                            test_size=float(args.within_participant_test_size),
                            random_state=participant_seed,
                        )
                        split_iter = splitter.split(np.zeros(idx_all.size), y_participant)
                        split_name_prefix = "holdout"
                        print(
                            f"    Participant {participant_id}: holdout_splits=1 "
                            f"test_size={args.within_participant_test_size:.2f} "
                            f"model_selectors={len(models)}x{len(feature_selectors)}"
                        )
                    else:
                        rec_splits = int(within_item.get("recommended_n_splits", 0))
                        if rec_splits < 2:
                            skip_counts[f"{dataset_name}:{protocol}:recommended_splits_lt2"] += 1
                            continue
                        max_splits_by_class = min(counts.values())
                        n_splits = min(rec_splits, int(max_splits_by_class))
                        if n_splits < 2:
                            skip_counts[f"{dataset_name}:{protocol}:folds_lt2_after_class_cap"] += 1
                            continue
                        splitter = StratifiedKFold(
                            n_splits=n_splits,
                            shuffle=True,
                            random_state=participant_seed,
                        )
                        split_iter = splitter.split(np.zeros(idx_all.size), y_participant)
                        split_name_prefix = "fold"
                        print(
                            f"    Participant {participant_id}: folds={n_splits} "
                            f"model_selectors={len(models)}x{len(feature_selectors)}"
                        )

                    for split_idx, (inner_train_pos, inner_test_pos) in enumerate(
                        split_iter,
                        start=1,
                    ):
                        train_idx = idx_all[inner_train_pos]
                        test_idx = idx_all[inner_test_pos]
                        X_train = X[train_idx]
                        y_train = y[train_idx]
                        X_test = X[test_idx]
                        y_test = y[test_idx]
                        if len(set(y_train.tolist())) < 2:
                            skip_counts[f"{dataset_name}:{protocol}:fold_single_train_class"] += 1
                            continue

                        combo_total = len(models) * len(feature_selectors)
                        combo_idx = 0
                        for model_key in models:
                            model_spec = registry[model_key]
                            estimator = model_spec["estimator"]
                            model_label = str(model_spec.get("label", model_key))
                            model_grid = _prefix_param_grid(list(model_spec["grid"]), prefix="model")
                            for selector_key in feature_selectors:
                                combo_idx += 1
                                split_name = f"within_{participant_id}_{split_name_prefix}{split_idx:02d}"
                                print(
                                    f"      [Train {combo_idx}/{combo_total}] "
                                    f"dataset={dataset_name} class_scenario={class_scenario['name']} "
                                    f"classification_set={protocol_debug} protocol={protocol} "
                                    f"split={split_name} model={model_key} selector={selector_key}"
                                )
                                selector_spec = selector_registry[selector_key]
                                selector = selector_spec["selector"]
                                selector_label = str(selector_spec.get("label", selector_key))
                                selector_grid = _prefix_param_grid(list(selector_spec["grid"]), prefix="selector")
                                all_combos = _cross_param_grids(model_grid, selector_grid)
                                param_grid = _sample_param_grid(
                                    combos=all_combos,
                                    max_count=args.max_param_combos,
                                    seed=args.random_seed + split_idx + len(model_key) + len(selector_key),
                                )
                                best_params, tune_summary = _choose_best_params(
                                    estimator=estimator,
                                    feature_selector=selector,
                                    param_grid=param_grid,
                                    X_train=X_train,
                                    y_train=y_train,
                                    labels=labels,
                                    args=args,
                                    mode="stratified",
                                    groups_train=None,
                                    seed=args.random_seed + split_idx,
                                )
                                outer_warning_counter = Counter()
                                y_pred = _fit_predict(
                                    estimator=estimator,
                                    feature_selector=selector,
                                    params=best_params,
                                    X_train=X_train,
                                    y_train=y_train,
                                    X_test=X_test,
                                    args=args,
                                    warning_counter=outer_warning_counter,
                                )
                                if y_pred is None:
                                    skip_counts[f"{dataset_name}:{protocol}:fit_predict_failed"] += 1
                                    continue
                                metrics = _metric_bundle(y_test, y_pred, labels=labels)
                                best_model_params, best_selector_params, best_other_params = _split_pipeline_params(
                                    best_params
                                )
                                pipeline_id = f"{model_key}+{selector_key}"
                                eval_row = {
                                    "dataset": dataset_name,
                                    "protocol": protocol,
                                    "model": model_key,
                                    "model_label": model_label,
                                    "feature_selector": selector_key,
                                    "feature_selector_label": selector_label,
                                    "pipeline_id": pipeline_id,
                                    "pipeline_label": f"{model_label} + {selector_label}",
                                    "split_id": split_name,
                                    "participant_id": participant_id,
                                    "n_train_rows": int(train_idx.size),
                                    "n_test_rows": int(test_idx.size),
                                    "n_train_participants": 1,
                                    "n_test_participants": 1,
                                    "best_params": best_params,
                                    "best_model_params": best_model_params,
                                    "best_feature_selector_params": best_selector_params,
                                    "best_pipeline_other_params": best_other_params,
                                    "tuning": tune_summary,
                                    "warning_counts": {
                                        "tuning": tune_summary.get("warning_counts", {}),
                                        "outer_fit_predict": dict(sorted(outer_warning_counter.items())),
                                    },
                                    "metrics": metrics,
                                }
                                if args.live_confusion_pngs:
                                    live_png = _write_live_confusion_png(
                                        metrics=metrics,
                                        out_root=live_confusion_png_dir,
                                        class_scenario_name=class_scenario["name"],
                                        dataset=dataset_name,
                                        protocol=protocol,
                                        split_id=split_name,
                                        pipeline_id=pipeline_id,
                                        eval_index=len(evaluations) + 1,
                                        cmap=str(args.live_confusion_png_cmap),
                                        dpi=int(args.live_confusion_png_dpi),
                                    )
                                    live_confusion_png_count += 1
                                    eval_row["confusion_png_live"] = str(live_png)
                                    print(f"        Live confusion PNG: {live_png}")
                                evaluations.append(eval_row)
            elif protocol in ("pooled_stratified", "pooled_stratified_holdout", "pooled_stratified_one_fold"):
                counts = Counter(y.tolist())
                if len(counts) < 2:
                    skip_counts[f"{dataset_name}:{protocol}:single_class_dataset"] += 1
                    continue

                n_splits = 1
                split_total = 1
                pooled_seed = _stable_seed_from_text(f"{dataset_name}:{class_scenario['name']}:pooled", args.random_seed)
                protocol_forces_holdout = protocol == "pooled_stratified_holdout"
                protocol_forces_one_fold = protocol == "pooled_stratified_one_fold"
                use_pooled_holdout = bool(args.pooled_stratified_no_folds) or protocol_forces_holdout
                use_single_pooled_fold = protocol_forces_one_fold
                if use_pooled_holdout:
                    min_class_support = min(counts.values())
                    if min_class_support < 2:
                        skip_counts[f"{dataset_name}:{protocol}:class_support_lt2_no_fold"] += 1
                        continue
                    splitter = StratifiedShuffleSplit(
                        n_splits=1,
                        test_size=float(args.pooled_stratified_test_size),
                        random_state=pooled_seed,
                    )
                    split_name_prefix = "pooled_holdout"
                else:
                    min_class_support = min(counts.values())
                    n_splits = min(int(args.pooled_stratified_folds), int(min_class_support))
                    if n_splits < 2:
                        skip_counts[f"{dataset_name}:{protocol}:folds_lt2_after_class_cap"] += 1
                        continue
                    splitter = StratifiedKFold(
                        n_splits=n_splits,
                        shuffle=True,
                        random_state=pooled_seed,
                    )
                    split_name_prefix = "pooled_fold"
                    split_total = n_splits

                fold_plan = [{"fold_index": i + 1} for i in range(n_splits)]
                fold_plan = _sample_plan_items(
                    items=fold_plan,
                    max_count=(1 if use_single_pooled_fold else args.max_outer_splits_per_protocol),
                    seed=args.random_seed + len(dataset_name) + 31,
                )
                fold_indices = [int(item.get("fold_index", 0)) for item in fold_plan if int(item.get("fold_index", 0)) > 0]
                selected_fold_set = set(fold_indices)
                if not selected_fold_set:
                    skip_counts[f"{dataset_name}:{protocol}:no_outer_folds_selected"] += 1
                    continue

                if use_pooled_holdout:
                    print(
                        "  Planned pooled holdout splits: "
                        f"{len(selected_fold_set)} (of {split_total}, test_size={args.pooled_stratified_test_size:.2f})"
                    )
                else:
                    print(f"  Planned pooled stratified folds: {len(selected_fold_set)} (of {split_total})")
                for fold_idx, (train_idx, test_idx) in enumerate(splitter.split(np.zeros(X.shape[0]), y), start=1):
                    if fold_idx not in selected_fold_set:
                        continue

                    if train_idx.size < 10 or test_idx.size < 2:
                        skip_counts[f"{dataset_name}:{protocol}:split_insufficient_rows"] += 1
                        continue

                    y_train = y[train_idx]
                    y_test = y[test_idx]
                    if len(set(y_train.tolist())) < 2:
                        skip_counts[f"{dataset_name}:{protocol}:split_single_train_class"] += 1
                        continue

                    X_train = X[train_idx]
                    X_test = X[test_idx]
                    split_name = f"{split_name_prefix}{fold_idx:02d}"
                    print(
                        f"    Split {fold_idx}/{split_total} ({split_name}): "
                        f"train_rows={train_idx.size} test_rows={test_idx.size} "
                        f"model_selectors={len(models)}x{len(feature_selectors)}"
                    )

                    combo_total = len(models) * len(feature_selectors)
                    combo_idx = 0
                    for model_key in models:
                        model_spec = registry[model_key]
                        estimator = model_spec["estimator"]
                        model_label = str(model_spec.get("label", model_key))
                        model_grid = _prefix_param_grid(list(model_spec["grid"]), prefix="model")
                        for selector_key in feature_selectors:
                            combo_idx += 1
                            print(
                                f"      [Train {combo_idx}/{combo_total}] "
                                f"dataset={dataset_name} class_scenario={class_scenario['name']} "
                                f"classification_set={protocol_debug} protocol={protocol} "
                                f"split={split_name} model={model_key} selector={selector_key}"
                            )
                            selector_spec = selector_registry[selector_key]
                            selector = selector_spec["selector"]
                            selector_label = str(selector_spec.get("label", selector_key))
                            selector_grid = _prefix_param_grid(list(selector_spec["grid"]), prefix="selector")
                            all_combos = _cross_param_grids(model_grid, selector_grid)
                            param_grid = _sample_param_grid(
                                combos=all_combos,
                                max_count=args.max_param_combos,
                                seed=args.random_seed + fold_idx + len(model_key) + len(selector_key),
                            )
                            best_params, tune_summary = _choose_best_params(
                                estimator=estimator,
                                feature_selector=selector,
                                param_grid=param_grid,
                                X_train=X_train,
                                y_train=y_train,
                                labels=labels,
                                args=args,
                                mode="stratified",
                                groups_train=None,
                                seed=args.random_seed + fold_idx,
                            )
                            outer_warning_counter = Counter()
                            y_pred = _fit_predict(
                                estimator=estimator,
                                feature_selector=selector,
                                params=best_params,
                                X_train=X_train,
                                y_train=y_train,
                                X_test=X_test,
                                args=args,
                                warning_counter=outer_warning_counter,
                            )
                            if y_pred is None:
                                skip_counts[f"{dataset_name}:{protocol}:fit_predict_failed"] += 1
                                continue
                            metrics = _metric_bundle(y_test, y_pred, labels=labels)
                            best_model_params, best_selector_params, best_other_params = _split_pipeline_params(
                                best_params
                            )
                            pipeline_id = f"{model_key}+{selector_key}"
                            eval_row = {
                                "dataset": dataset_name,
                                "protocol": protocol,
                                "model": model_key,
                                "model_label": model_label,
                                "feature_selector": selector_key,
                                "feature_selector_label": selector_label,
                                "pipeline_id": pipeline_id,
                                "pipeline_label": f"{model_label} + {selector_label}",
                                "split_id": split_name,
                                "n_train_rows": int(train_idx.size),
                                "n_test_rows": int(test_idx.size),
                                "n_train_participants": int(len(set(participants[train_idx].tolist()))),
                                "n_test_participants": int(len(set(participants[test_idx].tolist()))),
                                "best_params": best_params,
                                "best_model_params": best_model_params,
                                "best_feature_selector_params": best_selector_params,
                                "best_pipeline_other_params": best_other_params,
                                "tuning": tune_summary,
                                "warning_counts": {
                                    "tuning": tune_summary.get("warning_counts", {}),
                                    "outer_fit_predict": dict(sorted(outer_warning_counter.items())),
                                },
                                "metrics": metrics,
                            }
                            if args.live_confusion_pngs:
                                live_png = _write_live_confusion_png(
                                    metrics=metrics,
                                    out_root=live_confusion_png_dir,
                                    class_scenario_name=class_scenario["name"],
                                    dataset=dataset_name,
                                    protocol=protocol,
                                    split_id=split_name,
                                    pipeline_id=pipeline_id,
                                    eval_index=len(evaluations) + 1,
                                    cmap=str(args.live_confusion_png_cmap),
                                    dpi=int(args.live_confusion_png_dpi),
                                )
                                live_confusion_png_count += 1
                                eval_row["confusion_png_live"] = str(live_png)
                                print(f"        Live confusion PNG: {live_png}")
                            evaluations.append(eval_row)

    aggregate_rows = _aggregate_metric_rows(evaluations)
    best_rows = _best_model_by_dataset_protocol(aggregate_rows)
    warning_counts_total = _aggregate_warning_counts(evaluations)
    skip_counts_total = {k: skip_counts[k] for k in sorted(skip_counts, key=lambda x: (-skip_counts[x], x))}
    coverage = _dataset_protocol_coverage(
        aggregate_rows=aggregate_rows,
        datasets=datasets,
        protocols=protocols,
        min_aggregate_rows_per_pair=args.min_aggregate_rows_per_dataset_protocol,
    )

    config = {
        "bids_root": str(bids_root),
        "split_manifest": str(split_manifest_path),
        "target": split_manifest.get("target"),
        "target_column": target_col,
        "class_scenario": class_scenario,
        "datasets": datasets,
        "protocols": protocols,
        "models": models,
        "feature_selectors": feature_selectors,
        "available_models": _available_model_names(),
        "available_feature_selectors": _available_feature_selector_names(),
        "torch_available": TORCH_AVAILABLE,
        "torch_device_requested": args.torch_device,
        "torch_device_effective": torch_device_effective,
        "nvidia_gpu_detected": bool(nvidia_gpu_detected),
        "nvidia_gpu_names": nvidia_gpu_names,
        "nvidia_probe_message": nvidia_probe_message,
        "inner_folds": args.inner_folds,
        "max_param_combos": args.max_param_combos,
        "max_outer_splits_per_protocol": args.max_outer_splits_per_protocol,
        "pooled_stratified_folds": int(args.pooled_stratified_folds),
        "pooled_stratified_no_folds": bool(args.pooled_stratified_no_folds),
        "pooled_stratified_test_size": float(args.pooled_stratified_test_size),
        "within_participant_no_folds": bool(args.within_participant_no_folds),
        "within_participant_test_size": float(args.within_participant_test_size),
        "min_aggregate_rows_per_dataset_protocol": args.min_aggregate_rows_per_dataset_protocol,
        "allow_incomplete_coverage": bool(args.allow_incomplete_coverage),
        "clip_lower_quantile": args.clip_lower_quantile,
        "clip_upper_quantile": args.clip_upper_quantile,
        "live_confusion_pngs": bool(args.live_confusion_pngs),
        "live_confusion_png_dir": str(live_confusion_png_dir),
        "live_confusion_png_cmap": args.live_confusion_png_cmap,
        "live_confusion_png_dpi": int(args.live_confusion_png_dpi),
        "eeg_condition_psd_plots": bool(args.eeg_condition_psd_plots),
        "eeg_condition_psd_dir": str(eeg_condition_psd_dir),
        "eeg_condition_psd_fmin": float(args.eeg_condition_psd_fmin),
        "eeg_condition_psd_fmax": float(args.eeg_condition_psd_fmax),
        "random_seed": args.random_seed,
        "run_dir": str(run_dir),
        "run_tag": run_tag,
        "timestamp_utc": run_stamp,
    }

    results = {
        "config": config,
        "dataset_stats": dataset_stats,
        "evaluations": evaluations,
        "aggregates": aggregate_rows,
        "best_models": best_rows,
        "warning_counts_total": warning_counts_total,
        "skip_counts_total": skip_counts_total,
        "coverage": coverage,
        "eeg_condition_psd": eeg_condition_psd,
        "counts": {
            "n_evaluations": len(evaluations),
            "n_aggregate_rows": len(aggregate_rows),
            "n_live_confusion_pngs": int(live_confusion_png_count),
        },
    }
    results_json.parent.mkdir(parents=True, exist_ok=True)
    results_json.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    summary_text = _build_summary_markdown(
        config=config,
        dataset_stats=dataset_stats,
        aggregate_rows=aggregate_rows,
        best_rows=best_rows,
        warning_counts_total=warning_counts_total,
        coverage=coverage,
        skip_counts=skip_counts_total,
        eeg_condition_psd=eeg_condition_psd,
    )
    summary_md.parent.mkdir(parents=True, exist_ok=True)
    summary_md.write_text(summary_text, encoding="utf-8")

    run_meta = {
        "results_json": str(results_json),
        "summary_md": str(summary_md),
        "n_evaluations": len(evaluations),
        "n_aggregate_rows": len(aggregate_rows),
        "n_live_confusion_pngs": int(live_confusion_png_count),
        "live_confusion_png_dir": str(live_confusion_png_dir),
        "best_models": best_rows,
        "warning_counts_total": warning_counts_total,
        "skip_counts_total": skip_counts_total,
        "coverage": coverage,
        "eeg_condition_psd": eeg_condition_psd,
    }
    (run_dir / "run_meta.json").write_text(json.dumps(run_meta, indent=2) + "\n", encoding="utf-8")
    (run_dir / "run_config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    missing_pairs = list(coverage.get("missing_pairs", []))
    if missing_pairs:
        print("  Coverage gaps detected:")
        for pair in missing_pairs:
            print(
                f"    - dataset={pair['dataset']} protocol={pair['protocol']} "
                f"aggregate_rows={int(pair.get('aggregate_rows', 0))}"
            )
        if not args.allow_incomplete_coverage:
            raise RuntimeError(
                "Stage 6 coverage check failed: missing dataset+protocol aggregate rows. "
                "Use --allow-incomplete-coverage or set --min-aggregate-rows-per-dataset-protocol 0 to bypass."
            )

    print("Stage 6 complete.")
    print(f"  Evaluations: {len(evaluations)}")
    print(f"  Aggregate rows: {len(aggregate_rows)}")
    print(f"  Results JSON: {results_json}")
    print(f"  Summary Markdown: {summary_md}")
    print(f"  Model run dir: {run_dir}")
    print(f"  Class scenario: {class_scenario['name']} ({len(labels)} classes)")
    if eeg_condition_psd is not None:
        print(f"  EEG condition PSD manifest: {eeg_condition_psd.get('manifest_json', '')}")
    if args.live_confusion_pngs:
        print(f"  Live confusion PNGs written: {live_confusion_png_count}")
        print(f"  Live confusion PNG dir: {live_confusion_png_dir}")
    print(
        "  Coverage: "
        f"missing_pairs={len(missing_pairs)} "
        f"(min_aggregate_rows_per_pair={coverage['min_aggregate_rows_per_pair']})"
    )
    print(f"  Elapsed seconds: {time.time() - stage_started:.1f}")
    if warning_counts_total:
        print(f"  Captured warnings: {sum(warning_counts_total.values())}")
    if skip_counts_total:
        print(f"  Skip events: {sum(skip_counts_total.values())}")


if __name__ == "__main__":
    main()
