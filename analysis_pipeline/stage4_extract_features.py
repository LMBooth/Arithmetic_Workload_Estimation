from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any

import mne
import numpy as np
from scipy import signal as sp_signal


BANDS_HZ: dict[str, tuple[float, float]] = {
    "delta": (1.0, 4.0),
    "theta": (4.0, 8.0),
    "alpha": (8.0, 13.0),
    "beta": (13.0, 30.0),
    "highbeta": (30.0, 40.0),
}


ROI_CHANNELS: dict[str, list[str]] = {
    "frontal": ["Fp1", "Fp2", "F3", "F4", "F7", "F8", "Fz"],
    "central": ["C3", "C4", "Cz"],
    "parietal": ["P3", "P4", "P7", "P8", "Pz"],
    "temporal": ["T7", "T8"],
    "occipital": ["O1", "O2"],
}


@dataclass(frozen=True)
class SubjectBaseline:
    subject: str
    baseline_start_s: float | None
    baseline_end_s: float | None
    eeg_band_abs_by_roi: dict[str, dict[str, float]]
    ecg_hr_mean_bpm: float | None
    ecg_rmssd_ms: float | None
    pupil_mean: float | None
    pupil_peak_dilation: float | None


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _features_dir_default() -> Path:
    return _analysis_root() / "features"


def _cleaned_root_default() -> Path:
    return _analysis_root() / "derivatives" / "cleaned"


def _resolve_bids_root(bids_root_arg: str) -> Path:
    direct = Path(bids_root_arg).expanduser()
    if direct.is_absolute():
        return direct.resolve()

    from_cwd = (Path.cwd() / direct).resolve()
    if from_cwd.exists():
        return from_cwd

    repo_root = Path(__file__).resolve().parent.parent
    return (repo_root / direct).resolve()


def _task_from_bids_root(bids_root: Path) -> str:
    lower_name = bids_root.name.lower()
    if "arithmetic" in lower_name:
        return "arithmetic"
    raise ValueError(f"Could not infer task from BIDS root name: {bids_root}")


def _default_epoch_manifest() -> Path:
    return _reports_dir() / "epoch_manifest.tsv"


def _default_summary_json() -> Path:
    return _reports_dir() / "feature_summary.json"


def _as_float(value: str | None) -> float | None:
    if value is None:
        return None
    text = value.strip()
    if not text or text.lower() == "n/a":
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    if not math.isfinite(number):
        return None
    return number


def _as_int(value: str | None) -> int | None:
    if value is None:
        return None
    text = value.strip()
    if not text or text.lower() == "n/a":
        return None
    try:
        return int(text)
    except ValueError:
        return None


def _format_float(value: float | None, decimals: int = 6) -> str:
    if value is None:
        return "n/a"
    return f"{value:.{decimals}f}"


def _read_tsv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = [{k: (v or "") for k, v in row.items()} for row in reader]
    return rows


def _read_numeric_tsv(path: Path, required_columns: list[str]) -> dict[str, np.ndarray]:
    if not path.exists():
        raise FileNotFoundError(path)
    data: dict[str, list[float]] = {col: [] for col in required_columns}
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if reader.fieldnames is None:
            raise ValueError(f"Missing header in {path}")
        for col in required_columns:
            if col not in reader.fieldnames:
                raise ValueError(f"Missing required column '{col}' in {path}")
        for row in reader:
            parsed: dict[str, float] = {}
            ok = True
            for col in required_columns:
                val = _as_float(row.get(col))
                if val is None:
                    ok = False
                    break
                parsed[col] = val
            if ok:
                for col in required_columns:
                    data[col].append(parsed[col])
    return {k: np.asarray(v, dtype=np.float64) for k, v in data.items()}


def _write_tsv(path: Path, rows: list[dict[str, str]], preferred_prefix: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        fieldnames = preferred_prefix
    else:
        keys = set().union(*(row.keys() for row in rows))
        ordered = [k for k in preferred_prefix if k in keys]
        remaining = sorted(k for k in keys if k not in ordered)
        fieldnames = ordered + remaining

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def _safe_mean(values: np.ndarray) -> float | None:
    if values.size == 0:
        return None
    vals = values[np.isfinite(values)]
    if vals.size == 0:
        return None
    return float(np.mean(vals))


def _safe_median(values: np.ndarray) -> float | None:
    if values.size == 0:
        return None
    vals = values[np.isfinite(values)]
    if vals.size == 0:
        return None
    return float(np.median(vals))


def _safe_std(values: np.ndarray) -> float | None:
    if values.size == 0:
        return None
    vals = values[np.isfinite(values)]
    if vals.size == 0:
        return None
    return float(np.std(vals))


def _safe_min(values: np.ndarray) -> float | None:
    vals = values[np.isfinite(values)]
    if vals.size == 0:
        return None
    return float(np.min(vals))


def _safe_max(values: np.ndarray) -> float | None:
    vals = values[np.isfinite(values)]
    if vals.size == 0:
        return None
    return float(np.max(vals))


def _safe_percentile(values: np.ndarray, q: float) -> float | None:
    vals = values[np.isfinite(values)]
    if vals.size == 0:
        return None
    return float(np.percentile(vals, q))


def _iqr(values: np.ndarray) -> float | None:
    p75 = _safe_percentile(values, 75.0)
    p25 = _safe_percentile(values, 25.0)
    if p75 is None or p25 is None:
        return None
    return p75 - p25


def _normalize_ch_name(name: str) -> str:
    text = name.strip().upper()
    alias = {
        "FP1": "Fp1",
        "FP2": "Fp2",
        "T3": "T7",
        "T4": "T8",
        "T5": "P7",
        "T6": "P8",
        "FZ": "Fz",
        "CZ": "Cz",
        "PZ": "Pz",
        "OZ": "Oz",
    }
    if text in alias:
        return alias[text]
    if len(text) >= 2 and text[0] == "F" and text[1] == "P":
        return "Fp" + text[2:]
    if text.endswith("Z") and len(text) > 1:
        return text[:-1].capitalize() + "z"
    if text and text[0] in ("F", "C", "P", "O", "T"):
        return text[0] + text[1:].lower()
    return name.strip()


def _read_first_started_arithmetic_onset(events_tsv: Path) -> float | None:
    if not events_tsv.exists():
        return None
    onset_values: list[float] = []
    with events_tsv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            trial_type = (row.get("trial_type") or "").strip()
            if trial_type != "started_arithmetic":
                continue
            onset = _as_float(row.get("onset"))
            if onset is not None:
                onset_values.append(onset)
    if not onset_values:
        return None
    return float(min(onset_values))


def _roi_indices(ch_names: list[str]) -> dict[str, np.ndarray]:
    normalized = [_normalize_ch_name(ch) for ch in ch_names]
    by_roi: dict[str, np.ndarray] = {}
    for roi, names in ROI_CHANNELS.items():
        idx = [i for i, n in enumerate(normalized) if n in names]
        by_roi[roi] = np.asarray(idx, dtype=np.int32)
    by_roi["global"] = np.arange(len(ch_names), dtype=np.int32)
    return by_roi


def _band_power(psd: np.ndarray, freqs: np.ndarray, fmin: float, fmax: float) -> np.ndarray:
    mask = (freqs >= fmin) & (freqs < fmax)
    if not np.any(mask):
        return np.zeros(psd.shape[0], dtype=np.float64)
    band = np.trapezoid(psd[:, mask], freqs[mask], axis=1)
    return band.astype(np.float64, copy=False)


def _spectral_entropy(psd_1d: np.ndarray) -> float | None:
    vals = psd_1d[np.isfinite(psd_1d) & (psd_1d > 0)]
    if vals.size < 2:
        return None
    p = vals / np.sum(vals)
    entropy = -np.sum(p * np.log(p))
    norm = np.log(vals.size)
    if norm <= 0:
        return None
    return float(entropy / norm)


def _hjorth_metrics(signal_1d: np.ndarray) -> tuple[float | None, float | None, float | None]:
    x = signal_1d[np.isfinite(signal_1d)]
    if x.size < 3:
        return None, None, None
    dx = np.diff(x)
    ddx = np.diff(dx)
    var_x = float(np.var(x))
    var_dx = float(np.var(dx)) if dx.size > 1 else 0.0
    var_ddx = float(np.var(ddx)) if ddx.size > 1 else 0.0
    if var_x <= 0:
        return None, None, None
    activity = var_x
    mobility = math.sqrt(max(var_dx, 0.0) / var_x) if var_x > 0 else None
    if mobility is None or mobility <= 0:
        return activity, mobility, None
    mobility_dx = math.sqrt(max(var_ddx, 0.0) / var_dx) if var_dx > 0 else None
    complexity = (mobility_dx / mobility) if (mobility_dx is not None and mobility > 0) else None
    return activity, mobility, complexity


def _compute_eeg_roi_features(
    data: np.ndarray,
    sfreq: float,
    ch_names: list[str],
) -> tuple[dict[str, float], dict[str, dict[str, float]]]:
    features: dict[str, float] = {}
    roi_abs: dict[str, dict[str, float]] = {}
    if data.ndim != 2 or data.shape[1] < 10 or sfreq <= 0:
        return features, roi_abs

    n_samples = data.shape[1]
    nperseg = min(n_samples, max(int(round(sfreq * 2.0)), 64))
    freqs, psd = sp_signal.welch(data, fs=sfreq, nperseg=nperseg, axis=1)
    psd = psd.astype(np.float64, copy=False)

    roi_idx = _roi_indices(ch_names)
    total_power = _band_power(psd, freqs, 1.0, 40.0)
    total_power = np.where(total_power <= 0, np.nan, total_power)

    for roi, idx in roi_idx.items():
        if idx.size == 0:
            continue
        roi_psd = psd[idx, :]
        roi_total = np.nanmean(total_power[idx])
        roi_abs[roi] = {}

        for band, (fmin, fmax) in BANDS_HZ.items():
            band_ch = _band_power(roi_psd, freqs, fmin, fmax)
            band_abs = float(np.nanmean(band_ch))
            roi_abs[roi][band] = band_abs
            features[f"eeg_abs_{band}_{roi}"] = band_abs
            if roi_total and math.isfinite(roi_total) and roi_total > 0:
                features[f"eeg_rel_{band}_{roi}"] = band_abs / roi_total

        theta = features.get(f"eeg_rel_theta_{roi}")
        alpha = features.get(f"eeg_rel_alpha_{roi}")
        beta = features.get(f"eeg_rel_beta_{roi}")
        if theta is not None and alpha is not None and alpha > 0:
            features[f"eeg_ratio_theta_alpha_{roi}"] = theta / alpha
        if theta is not None and beta is not None and beta > 0:
            features[f"eeg_ratio_theta_beta_{roi}"] = theta / beta
        if alpha is not None and beta is not None and beta > 0:
            features[f"eeg_ratio_alpha_beta_{roi}"] = alpha / beta

        # Time-domain summary per ROI (average across channels).
        roi_data = data[idx, :]
        var_vals = np.var(roi_data, axis=1)
        rms_vals = np.sqrt(np.mean(roi_data**2, axis=1))
        ll_vals = np.mean(np.abs(np.diff(roi_data, axis=1)), axis=1) if roi_data.shape[1] > 1 else np.array([])
        features[f"eeg_var_{roi}"] = float(np.mean(var_vals))
        features[f"eeg_rms_{roi}"] = float(np.mean(rms_vals))
        if ll_vals.size:
            features[f"eeg_line_length_{roi}"] = float(np.mean(ll_vals))

        hj_activity: list[float] = []
        hj_mobility: list[float] = []
        hj_complexity: list[float] = []
        entropy_vals: list[float] = []
        for chan_i in idx:
            a, m, c = _hjorth_metrics(data[chan_i, :])
            if a is not None:
                hj_activity.append(a)
            if m is not None and math.isfinite(m):
                hj_mobility.append(m)
            if c is not None and math.isfinite(c):
                hj_complexity.append(c)

            # Spectral entropy in 1-40 Hz.
            p = psd[chan_i, :]
            mask = (freqs >= 1.0) & (freqs < 40.0)
            ent = _spectral_entropy(p[mask])
            if ent is not None and math.isfinite(ent):
                entropy_vals.append(ent)

        if hj_activity:
            features[f"eeg_hjorth_activity_{roi}"] = float(np.mean(hj_activity))
        if hj_mobility:
            features[f"eeg_hjorth_mobility_{roi}"] = float(np.mean(hj_mobility))
        if hj_complexity:
            features[f"eeg_hjorth_complexity_{roi}"] = float(np.mean(hj_complexity))
        if entropy_vals:
            features[f"eeg_spectral_entropy_{roi}"] = float(np.mean(entropy_vals))

    # Frontal alpha asymmetry: log(alpha(F4)) - log(alpha(F3)).
    normalized = [_normalize_ch_name(ch) for ch in ch_names]
    idx_f3 = [i for i, name in enumerate(normalized) if name == "F3"]
    idx_f4 = [i for i, name in enumerate(normalized) if name == "F4"]
    if idx_f3 and idx_f4:
        alpha_f3 = _band_power(psd[idx_f3, :], freqs, 8.0, 13.0)
        alpha_f4 = _band_power(psd[idx_f4, :], freqs, 8.0, 13.0)
        f3 = float(np.nanmean(alpha_f3))
        f4 = float(np.nanmean(alpha_f4))
        if f3 > 0 and f4 > 0:
            features["eeg_frontal_alpha_asymmetry_f4_minus_f3"] = float(np.log(f4) - np.log(f3))

    # Frontal midline theta from Fz (absolute + relative).
    idx_fz = [i for i, name in enumerate(normalized) if name == "Fz"]
    if idx_fz:
        theta_fz = _band_power(psd[idx_fz, :], freqs, 4.0, 8.0)
        total_fz = _band_power(psd[idx_fz, :], freqs, 1.0, 40.0)
        theta_abs = float(np.nanmean(theta_fz))
        total_abs = float(np.nanmean(total_fz))
        features["eeg_fz_theta_abs"] = theta_abs
        if total_abs > 0:
            features["eeg_fz_theta_rel"] = theta_abs / total_abs

    return features, roi_abs


def _detect_ecg_peaks(times: np.ndarray, filtered: np.ndarray, sfreq: float) -> np.ndarray:
    if times.size < 3 or filtered.size < 3 or sfreq <= 0:
        return np.array([], dtype=np.int64)
    distance = max(1, int(round(0.3 * sfreq)))
    mad = np.median(np.abs(filtered - np.median(filtered)))
    robust_scale = 1.4826 * mad if mad > 0 else float(np.std(filtered))
    fallback = float(np.percentile(np.abs(filtered), 75)) * 0.30
    prominence = max(robust_scale * 1.5, fallback, 1e-9)
    peaks_pos, _ = sp_signal.find_peaks(filtered, distance=distance, prominence=prominence)
    peaks_neg, _ = sp_signal.find_peaks(-filtered, distance=distance, prominence=prominence)
    return peaks_pos if peaks_pos.size >= peaks_neg.size else peaks_neg


def _compute_ecg_peak_features(times: np.ndarray, peak_sig: np.ndarray) -> dict[str, float | int | str]:
    out: dict[str, float | int | str] = {}
    sfreq = None
    if times.size > 2:
        diffs = np.diff(times)
        diffs = diffs[np.isfinite(diffs) & (diffs > 0)]
        if diffs.size:
            sfreq = 1.0 / float(np.median(diffs))
    if sfreq is None or sfreq <= 0:
        out["ecg_quality_flag"] = "invalid_timebase"
        out["ecg_detected_peak_count"] = 0
        out["ecg_valid_rr_count"] = 0
        out["ecg_rr_coverage_ratio"] = 0.0
        return out

    peaks = _detect_ecg_peaks(times, peak_sig, sfreq)
    out["ecg_detected_peak_count"] = int(peaks.size)
    if peaks.size < 2:
        out["ecg_quality_flag"] = "insufficient_beats"
        out["ecg_valid_rr_count"] = 0
        out["ecg_rr_coverage_ratio"] = 0.0
        return out

    rr = np.diff(times[peaks])
    rr = rr[np.isfinite(rr) & (rr > 0)]
    if rr.size == 0:
        out["ecg_quality_flag"] = "insufficient_beats"
        out["ecg_valid_rr_count"] = 0
        out["ecg_rr_coverage_ratio"] = 0.0
        return out

    hr = 60.0 / rr
    valid = (hr >= 35.0) & (hr <= 180.0)
    rr_valid = rr[valid]
    hr_valid = hr[valid]
    out["ecg_valid_rr_count"] = int(rr_valid.size)
    out["ecg_rr_coverage_ratio"] = float(rr_valid.size) / float(rr.size)

    if rr_valid.size == 0:
        out["ecg_quality_flag"] = "insufficient_beats"
        return out

    rr_ms = rr_valid * 1000.0
    out["ecg_hr_mean_bpm"] = float(np.mean(hr_valid))
    out["ecg_hr_median_bpm"] = float(np.median(hr_valid))
    out["ecg_hr_std_bpm"] = float(np.std(hr_valid))
    out["ecg_hr_min_bpm"] = float(np.min(hr_valid))
    out["ecg_hr_max_bpm"] = float(np.max(hr_valid))

    out["ecg_rr_mean_ms"] = float(np.mean(rr_ms))
    out["ecg_sdnn_ms"] = float(np.std(rr_ms))
    rr_diff_ms = np.diff(rr_ms)
    out["ecg_rmssd_ms"] = float(np.sqrt(np.mean(rr_diff_ms**2))) if rr_diff_ms.size else None
    p75 = np.percentile(rr_ms, 75.0)
    p25 = np.percentile(rr_ms, 25.0)
    out["ecg_rr_iqr_ms"] = float(p75 - p25)
    out["ecg_pnn50_pct"] = float(100.0 * np.mean(np.abs(rr_diff_ms) > 50.0)) if rr_diff_ms.size else None
    out["ecg_rr_cv"] = float(np.std(rr_ms) / np.mean(rr_ms)) if np.mean(rr_ms) > 0 else None
    out["ecg_quality_flag"] = "ok" if int(peaks.size) >= 3 else "insufficient_beats"
    return out


def _compute_pupil_features(
    times: np.ndarray,
    pupil: np.ndarray,
    x: np.ndarray,
    y: np.ndarray,
    conf: np.ndarray,
    low_conf_threshold: float,
) -> dict[str, float | int]:
    out: dict[str, float | int] = {}
    if times.size == 0:
        return out

    finite_mask = (
        np.isfinite(times)
        & np.isfinite(pupil)
        & np.isfinite(x)
        & np.isfinite(y)
        & np.isfinite(conf)
    )
    valid_times = times[finite_mask]
    valid_pupil = pupil[finite_mask]
    valid_x = x[finite_mask]
    valid_y = y[finite_mask]
    valid_conf = conf[finite_mask]

    coverage = float(valid_times.size) / float(times.size) if times.size else 0.0
    out["pupil_valid_coverage_ratio"] = coverage

    if valid_times.size < 2:
        return out

    out["pupil_mean"] = float(np.mean(valid_pupil))
    out["pupil_median"] = float(np.median(valid_pupil))
    out["pupil_std"] = float(np.std(valid_pupil))
    out["pupil_iqr"] = float(np.percentile(valid_pupil, 75.0) - np.percentile(valid_pupil, 25.0))
    out["pupil_min"] = float(np.min(valid_pupil))
    out["pupil_max"] = float(np.max(valid_pupil))
    out["pupil_p10"] = float(np.percentile(valid_pupil, 10.0))
    out["pupil_p90"] = float(np.percentile(valid_pupil, 90.0))

    rel_t = valid_times - float(valid_times[0])
    if np.unique(rel_t).size > 1:
        slope = np.polyfit(rel_t, valid_pupil, 1)[0]
        out["pupil_slope_per_s"] = float(slope)

    duration = float(valid_times[-1] - valid_times[0])
    early_window = min(0.5, 0.10 * max(duration, 0.0))
    early_mask = rel_t <= early_window
    if np.any(early_mask):
        early_ref = float(np.mean(valid_pupil[early_mask]))
    else:
        early_ref = float(valid_pupil[0])
    peak = float(np.max(valid_pupil))
    out["pupil_peak_dilation"] = peak - early_ref

    dt = np.diff(valid_times)
    good_dt = dt > 0
    if np.any(good_dt):
        val_mid = valid_pupil[1:][good_dt]
        ref = np.mean(valid_pupil)
        above = np.maximum(val_mid - ref, 0.0)
        out["pupil_auc_above_mean"] = float(np.sum(above * dt[good_dt]))

        vel = np.diff(valid_pupil)[good_dt] / dt[good_dt]
        out["pupil_vel_mean_abs"] = float(np.mean(np.abs(vel)))
        out["pupil_vel_max_abs"] = float(np.max(np.abs(vel)))

        gaze_steps = np.sqrt(np.diff(valid_x)[good_dt] ** 2 + np.diff(valid_y)[good_dt] ** 2)
        out["gaze_path_length"] = float(np.sum(gaze_steps))

    out["pupil_conf_mean"] = float(np.mean(valid_conf))
    out["pupil_low_conf_ratio"] = float(np.mean(valid_conf < low_conf_threshold))
    out["gaze_x_mean"] = float(np.mean(valid_x))
    out["gaze_x_std"] = float(np.std(valid_x))
    out["gaze_y_mean"] = float(np.mean(valid_y))
    out["gaze_y_std"] = float(np.std(valid_y))

    return out


def _load_cleaned_ecg(subject_root: Path, task: str, subject: str) -> dict[str, np.ndarray] | None:
    path = subject_root / "ecg" / f"{subject}_task-{task}_desc-preproc-ecg.tsv"
    if not path.exists():
        return None
    return _read_numeric_tsv(path, ["time", "cardiac_raw", "cardiac_broad", "cardiac_peak"])


def _load_cleaned_pupil(subject_root: Path, task: str, subject: str) -> dict[str, np.ndarray] | None:
    path = subject_root / "pupil" / f"{subject}_task-{task}_desc-preproc-pupil.tsv"
    if not path.exists():
        return None
    return _read_numeric_tsv(
        path,
        ["time", "pupil_size_clean", "x_coordinate_clean", "y_coordinate_clean", "confidence_clean"],
    )


def _load_cleaned_eeg(subject_root: Path, task: str, subject: str) -> tuple[np.ndarray, float, list[str], np.ndarray] | None:
    path = subject_root / "eeg" / f"{subject}_task-{task}_desc-preproc_eeg_raw.fif"
    if not path.exists():
        return None
    raw = mne.io.read_raw_fif(path, preload=True, verbose="ERROR")
    data = raw.get_data().astype(np.float32, copy=False)
    sfreq = float(raw.info["sfreq"])
    ch_names = list(raw.ch_names)
    times = raw.times.astype(np.float64, copy=False)
    return data, sfreq, ch_names, times


def _baseline_bounds(first_start_s: float | None, baseline_seconds: float) -> tuple[float | None, float | None]:
    if first_start_s is None:
        return None, None
    end_s = first_start_s
    start_s = max(0.0, end_s - baseline_seconds)
    if end_s <= start_s:
        return None, None
    return start_s, end_s


def _compute_subject_baseline(
    bids_root: Path,
    cleaned_root: Path,
    task: str,
    subject: str,
    baseline_seconds: float,
    pupil_low_conf_threshold: float,
) -> SubjectBaseline:
    events_tsv = bids_root / subject / "eeg" / f"{subject}_task-{task}_events.tsv"
    first_start = _read_first_started_arithmetic_onset(events_tsv)
    base_start, base_end = _baseline_bounds(first_start, baseline_seconds)

    eeg_abs: dict[str, dict[str, float]] = {}
    ecg_hr_mean: float | None = None
    ecg_rmssd: float | None = None
    pupil_mean: float | None = None
    pupil_peak: float | None = None

    if base_start is None or base_end is None:
        return SubjectBaseline(
            subject=subject,
            baseline_start_s=None,
            baseline_end_s=None,
            eeg_band_abs_by_roi=eeg_abs,
            ecg_hr_mean_bpm=ecg_hr_mean,
            ecg_rmssd_ms=ecg_rmssd,
            pupil_mean=pupil_mean,
            pupil_peak_dilation=pupil_peak,
        )

    subject_root = cleaned_root / subject

    eeg_payload = _load_cleaned_eeg(subject_root, task, subject)
    if eeg_payload is not None:
        data, sfreq, ch_names, times = eeg_payload
        idx = np.where((times >= base_start) & (times < base_end))[0]
        if idx.size > max(16, int(sfreq)):
            eeg_feats, eeg_roi_abs = _compute_eeg_roi_features(data[:, idx], sfreq, ch_names)
            _ = eeg_feats
            eeg_abs = eeg_roi_abs

    ecg_payload = _load_cleaned_ecg(subject_root, task, subject)
    if ecg_payload is not None:
        t = ecg_payload["time"]
        idx = np.where((t >= base_start) & (t < base_end))[0]
        if idx.size > 10:
            ecg_feats = _compute_ecg_peak_features(t[idx], ecg_payload["cardiac_peak"][idx])
            ecg_hr_mean = (
                float(ecg_feats["ecg_hr_mean_bpm"])
                if "ecg_hr_mean_bpm" in ecg_feats and ecg_feats["ecg_hr_mean_bpm"] is not None
                else None
            )
            ecg_rmssd = (
                float(ecg_feats["ecg_rmssd_ms"])
                if "ecg_rmssd_ms" in ecg_feats and ecg_feats["ecg_rmssd_ms"] is not None
                else None
            )

    pupil_payload = _load_cleaned_pupil(subject_root, task, subject)
    if pupil_payload is not None:
        t = pupil_payload["time"]
        idx = np.where((t >= base_start) & (t < base_end))[0]
        if idx.size > 10:
            pupil_feats = _compute_pupil_features(
                t[idx],
                pupil_payload["pupil_size_clean"][idx],
                pupil_payload["x_coordinate_clean"][idx],
                pupil_payload["y_coordinate_clean"][idx],
                pupil_payload["confidence_clean"][idx],
                low_conf_threshold=pupil_low_conf_threshold,
            )
            if "pupil_mean" in pupil_feats:
                pupil_mean = float(pupil_feats["pupil_mean"])
            if "pupil_peak_dilation" in pupil_feats:
                pupil_peak = float(pupil_feats["pupil_peak_dilation"])

    return SubjectBaseline(
        subject=subject,
        baseline_start_s=base_start,
        baseline_end_s=base_end,
        eeg_band_abs_by_roi=eeg_abs,
        ecg_hr_mean_bpm=ecg_hr_mean,
        ecg_rmssd_ms=ecg_rmssd,
        pupil_mean=pupil_mean,
        pupil_peak_dilation=pupil_peak,
    )


def _row_prefix_from_manifest(row: dict[str, str], preproc_version: str) -> dict[str, str]:
    return {
        "participant_id": row.get("participant_id", ""),
        "trial_id": row.get("trial_id", ""),
        "epoch_id": row.get("epoch_id", ""),
        "block": row.get("block", ""),
        "difficulty_range": row.get("difficulty_range", ""),
        "response_accuracy": row.get("response_accuracy", ""),
        "outcome": row.get("outcome", ""),
        "window": row.get("window_mode", ""),
        "segment_index": row.get("segment_index", ""),
        "is_subwindow": row.get("is_subwindow", ""),
        "epoch_start_s": row.get("epoch_start_s", ""),
        "epoch_end_s": row.get("epoch_end_s", ""),
        "epoch_duration_s": row.get("epoch_duration_s", ""),
        "preproc_version": preproc_version,
    }


def _load_preproc_version(reports_dir: Path) -> str:
    summary_path = reports_dir / "preprocess_summary.json"
    if not summary_path.exists():
        return "stage2_preprocess_unknown"
    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except Exception:
        return "stage2_preprocess_unknown"
    params = payload.get("parameters", {})
    notch = params.get("eeg_notch_hz")
    band = params.get("eeg_bandpass_hz")
    if notch is None or not isinstance(band, list) or len(band) != 2:
        return "stage2_preprocess"
    return f"stage2_preprocess_notch{notch}_bp{band[0]}-{band[1]}"


def _extract_eeg_features_from_epoch(
    row: dict[str, str],
    baseline: SubjectBaseline,
    preproc_version: str,
) -> dict[str, str] | None:
    if row.get("eeg_keep") != "true":
        return None
    path_text = (row.get("eeg_epoch_file") or "").strip()
    if not path_text:
        return None
    path = Path(path_text)
    if not path.exists():
        return None

    payload = np.load(path)
    if "data" not in payload.files or "time" not in payload.files:
        return None

    x = payload["data"]
    t = payload["time"]
    sfreq = None
    if t.size > 2:
        diffs = np.diff(t)
        diffs = diffs[np.isfinite(diffs) & (diffs > 0)]
        if diffs.size:
            sfreq = 1.0 / float(np.median(diffs))
    if sfreq is None or sfreq <= 0:
        return None

    subject = row.get("participant_id", "")
    # Use cleaned fif for channel names.
    ch_names: list[str] = []
    try:
        eeg_meta = path.parents[0] / f"{subject}_task-arithmetic_desc-epochs-eeg_meta.json"
        if eeg_meta.exists():
            meta = json.loads(eeg_meta.read_text(encoding="utf-8"))
            ch_names = [str(c) for c in meta.get("ch_names", [])]
    except Exception:
        ch_names = []
    if len(ch_names) != x.shape[0]:
        ch_names = [f"ch{i:02d}" for i in range(x.shape[0])]

    feat, roi_abs = _compute_eeg_roi_features(x.astype(np.float64), float(sfreq), ch_names)
    out: dict[str, str] = _row_prefix_from_manifest(row, preproc_version)

    for k, v in feat.items():
        out[f"{k}"] = _format_float(v, 9)

    # Baseline deltas for key bands (theta/alpha/beta), by ROI.
    for roi, baseline_bands in baseline.eeg_band_abs_by_roi.items():
        roi_current = roi_abs.get(roi, {})
        for band in ("theta", "alpha", "beta"):
            cur = roi_current.get(band)
            base = baseline_bands.get(band)
            key = f"eeg_abs_{band}_{roi}_delta_base"
            if cur is None or base is None:
                out[key] = "n/a"
            else:
                out[key] = _format_float(cur - base, 9)

    out["baseline_start_s"] = _format_float(baseline.baseline_start_s, 6)
    out["baseline_end_s"] = _format_float(baseline.baseline_end_s, 6)
    return out


def _extract_ecg_features_from_epoch(
    row: dict[str, str],
    baseline: SubjectBaseline,
    preproc_version: str,
) -> dict[str, str] | None:
    if row.get("ecg_keep") != "true":
        return None
    path_text = (row.get("ecg_epoch_file") or "").strip()
    if not path_text:
        return None
    path = Path(path_text)
    if not path.exists():
        return None

    payload = np.load(path)
    required = {"time", "cardiac_peak"}
    if not required.issubset(set(payload.files)):
        return None

    feat = _compute_ecg_peak_features(payload["time"], payload["cardiac_peak"])
    out: dict[str, str] = _row_prefix_from_manifest(row, preproc_version)
    for k, v in feat.items():
        if isinstance(v, str):
            out[k] = v
        elif isinstance(v, int):
            out[k] = str(v)
        elif v is None:
            out[k] = "n/a"
        else:
            out[k] = _format_float(float(v), 9)

    hr_mean = feat.get("ecg_hr_mean_bpm")
    rmssd = feat.get("ecg_rmssd_ms")
    if isinstance(hr_mean, (int, float)) and baseline.ecg_hr_mean_bpm is not None:
        out["ecg_hr_mean_bpm_delta_base"] = _format_float(float(hr_mean) - baseline.ecg_hr_mean_bpm, 9)
    else:
        out["ecg_hr_mean_bpm_delta_base"] = "n/a"
    if isinstance(rmssd, (int, float)) and baseline.ecg_rmssd_ms is not None:
        out["ecg_rmssd_ms_delta_base"] = _format_float(float(rmssd) - baseline.ecg_rmssd_ms, 9)
    else:
        out["ecg_rmssd_ms_delta_base"] = "n/a"

    out["baseline_start_s"] = _format_float(baseline.baseline_start_s, 6)
    out["baseline_end_s"] = _format_float(baseline.baseline_end_s, 6)
    return out


def _extract_pupil_features_from_epoch(
    row: dict[str, str],
    baseline: SubjectBaseline,
    preproc_version: str,
    pupil_low_conf_threshold: float,
) -> dict[str, str] | None:
    if row.get("pupil_keep") != "true":
        return None
    path_text = (row.get("pupil_epoch_file") or "").strip()
    if not path_text:
        return None
    path = Path(path_text)
    if not path.exists():
        return None

    payload = np.load(path)
    required = {"time", "pupil_size_clean", "x_coordinate_clean", "y_coordinate_clean", "confidence_clean"}
    if not required.issubset(set(payload.files)):
        return None

    feat = _compute_pupil_features(
        payload["time"],
        payload["pupil_size_clean"],
        payload["x_coordinate_clean"],
        payload["y_coordinate_clean"],
        payload["confidence_clean"],
        low_conf_threshold=pupil_low_conf_threshold,
    )
    out: dict[str, str] = _row_prefix_from_manifest(row, preproc_version)
    for k, v in feat.items():
        out[k] = _format_float(float(v), 9)

    if "pupil_mean" in feat and baseline.pupil_mean is not None:
        out["pupil_mean_delta_base"] = _format_float(float(feat["pupil_mean"]) - baseline.pupil_mean, 9)
    else:
        out["pupil_mean_delta_base"] = "n/a"
    if "pupil_peak_dilation" in feat and baseline.pupil_peak_dilation is not None:
        out["pupil_peak_dilation_delta_base"] = _format_float(
            float(feat["pupil_peak_dilation"]) - baseline.pupil_peak_dilation,
            9,
        )
    else:
        out["pupil_peak_dilation_delta_base"] = "n/a"

    out["baseline_start_s"] = _format_float(baseline.baseline_start_s, 6)
    out["baseline_end_s"] = _format_float(baseline.baseline_end_s, 6)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Stage 4 feature extraction from Stage 3 epoch outputs. "
            "Writes unimodal feature tables (EEG/ECG/Pupil) and a summary report."
        )
    )
    parser.add_argument("--bids-root", required=True, help="Path to BIDS root.")
    parser.add_argument("--task", default=None, help="Task name (default: infer from BIDS root).")
    parser.add_argument(
        "--epoch-manifest",
        default=None,
        help="Path to epoch manifest TSV (default: analysis_pipeline/reports/epoch_manifest.tsv).",
    )
    parser.add_argument(
        "--cleaned-root",
        default=None,
        help="Path to cleaned derivatives root (default: analysis_pipeline/derivatives/cleaned).",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Output feature directory (default: analysis_pipeline/features).",
    )
    parser.add_argument(
        "--summary-json",
        default=None,
        help="Feature summary output JSON path (default: analysis_pipeline/reports/feature_summary.json).",
    )
    parser.add_argument("--baseline-seconds", type=float, default=60.0)
    parser.add_argument("--pupil-low-conf-threshold", type=float, default=0.60)
    parser.add_argument(
        "--subjects",
        nargs="*",
        default=None,
        help="Optional subset of subject IDs (e.g., sub-001 sub-003).",
    )
    args = parser.parse_args()

    if args.baseline_seconds <= 0:
        raise ValueError("--baseline-seconds must be > 0")
    if args.pupil_low_conf_threshold < 0 or args.pupil_low_conf_threshold > 1:
        raise ValueError("--pupil-low-conf-threshold must be within [0, 1]")

    bids_root = _resolve_bids_root(args.bids_root)
    if not bids_root.exists():
        raise FileNotFoundError(bids_root)
    task = args.task or _task_from_bids_root(bids_root)

    epoch_manifest_path = Path(args.epoch_manifest).resolve() if args.epoch_manifest else _default_epoch_manifest()
    cleaned_root = Path(args.cleaned_root).resolve() if args.cleaned_root else _cleaned_root_default()
    out_dir = Path(args.out_dir).resolve() if args.out_dir else _features_dir_default()
    summary_out = Path(args.summary_json).resolve() if args.summary_json else _default_summary_json()
    reports_dir = _reports_dir()

    manifest_rows = _read_tsv_rows(epoch_manifest_path)
    if not manifest_rows:
        raise ValueError(f"No rows found in epoch manifest: {epoch_manifest_path}")

    wanted = set(args.subjects) if args.subjects else None
    filtered = [
        row
        for row in manifest_rows
        if (not wanted or (row.get("participant_id") or "") in wanted)
    ]
    if not filtered:
        raise ValueError("No epoch rows left after subject filtering.")

    subjects = sorted({row.get("participant_id", "") for row in filtered if row.get("participant_id")})
    preproc_version = _load_preproc_version(reports_dir)

    baseline_cache: dict[str, SubjectBaseline] = {}
    for subject in subjects:
        baseline_cache[subject] = _compute_subject_baseline(
            bids_root=bids_root,
            cleaned_root=cleaned_root,
            task=task,
            subject=subject,
            baseline_seconds=args.baseline_seconds,
            pupil_low_conf_threshold=args.pupil_low_conf_threshold,
        )

    eeg_rows: list[dict[str, str]] = []
    ecg_rows: list[dict[str, str]] = []
    pupil_rows: list[dict[str, str]] = []

    for row in filtered:
        subject = row.get("participant_id", "")
        if not subject or subject not in baseline_cache:
            continue
        baseline = baseline_cache[subject]

        eeg_row = _extract_eeg_features_from_epoch(row, baseline, preproc_version)
        if eeg_row is not None:
            eeg_rows.append(eeg_row)

        ecg_row = _extract_ecg_features_from_epoch(row, baseline, preproc_version)
        if ecg_row is not None:
            ecg_rows.append(ecg_row)

        pupil_row = _extract_pupil_features_from_epoch(
            row,
            baseline,
            preproc_version,
            pupil_low_conf_threshold=args.pupil_low_conf_threshold,
        )
        if pupil_row is not None:
            pupil_rows.append(pupil_row)

    out_dir.mkdir(parents=True, exist_ok=True)
    eeg_out = out_dir / "features_eeg.tsv"
    ecg_out = out_dir / "features_ecg.tsv"
    pupil_out = out_dir / "features_pupil.tsv"

    prefix_cols = [
        "participant_id",
        "trial_id",
        "epoch_id",
        "block",
        "difficulty_range",
        "response_accuracy",
        "outcome",
        "window",
        "segment_index",
        "is_subwindow",
        "epoch_start_s",
        "epoch_end_s",
        "epoch_duration_s",
        "baseline_start_s",
        "baseline_end_s",
        "preproc_version",
    ]
    _write_tsv(eeg_out, eeg_rows, prefix_cols)
    _write_tsv(ecg_out, ecg_rows, prefix_cols)
    _write_tsv(pupil_out, pupil_rows, prefix_cols)

    hr_values = [
        _as_float(row.get("ecg_hr_mean_bpm"))
        for row in ecg_rows
        if _as_float(row.get("ecg_hr_mean_bpm")) is not None
    ]
    pupil_values = [
        _as_float(row.get("pupil_mean"))
        for row in pupil_rows
        if _as_float(row.get("pupil_mean")) is not None
    ]
    hr_arr = np.asarray(hr_values, dtype=np.float64) if hr_values else np.array([], dtype=np.float64)
    pupil_arr = np.asarray(pupil_values, dtype=np.float64) if pupil_values else np.array([], dtype=np.float64)
    summary = {
        "bids_root": str(bids_root),
        "task": task,
        "epoch_manifest": str(epoch_manifest_path),
        "cleaned_root": str(cleaned_root),
        "out_dir": str(out_dir),
        "subjects_processed": len(subjects),
        "manifest_rows_in": len(filtered),
        "rows_out": {
            "eeg": len(eeg_rows),
            "ecg": len(ecg_rows),
            "pupil": len(pupil_rows),
        },
        "preproc_version": preproc_version,
        "baseline_seconds": args.baseline_seconds,
        "pupil_low_conf_threshold": args.pupil_low_conf_threshold,
        "mean_ecg_hr_bpm": mean([x for x in hr_values if x is not None]) if hr_values else None,
        "mean_pupil_size": mean([x for x in pupil_values if x is not None]) if pupil_values else None,
        "ecg_hr_percentiles_bpm": (
            {
                "p10": float(np.percentile(hr_arr, 10.0)),
                "p50": float(np.percentile(hr_arr, 50.0)),
                "p90": float(np.percentile(hr_arr, 90.0)),
            }
            if hr_arr.size
            else None
        ),
        "pupil_mean_percentiles": (
            {
                "p10": float(np.percentile(pupil_arr, 10.0)),
                "p50": float(np.percentile(pupil_arr, 50.0)),
                "p90": float(np.percentile(pupil_arr, 90.0)),
                "p99": float(np.percentile(pupil_arr, 99.0)),
            }
            if pupil_arr.size
            else None
        ),
        "outputs": {
            "features_eeg_tsv": str(eeg_out),
            "features_ecg_tsv": str(ecg_out),
            "features_pupil_tsv": str(pupil_out),
        },
    }
    summary_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote EEG features: {eeg_out}")
    print(f"Wrote ECG features: {ecg_out}")
    print(f"Wrote Pupil features: {pupil_out}")
    print(f"Wrote feature summary: {summary_out}")


if __name__ == "__main__":
    main()
