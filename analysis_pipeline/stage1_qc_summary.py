from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median
from typing import Any, Callable

import matplotlib
import numpy as np
from scipy import signal as sp_signal

matplotlib.use("Agg")
import matplotlib.pyplot as plt


CUE_TRIAL_RE = re.compile(r"^\d+_\d+_\d+_\d+$")


@dataclass(frozen=True)
class SubjectPaths:
    subject: str
    eeg_vhdr: Path
    eeg_json: Path
    events_tsv: Path
    ecg_tsv: Path
    ecg_json: Path
    pupil_tsv: Path
    pupil_json: Path


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
    number = _as_float(value)
    if number is None:
        return None
    if float(number).is_integer():
        return int(number)
    return None


def _format_float(value: float | None, decimals: int = 6) -> str:
    if value is None:
        return "n/a"
    return f"{value:.{decimals}f}"


def _bool_text(value: bool) -> str:
    return "true" if value else "false"


def _ordered_unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        text = str(item).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _effective_inclusion_flag(analysis_included: str, rejected: bool) -> str:
    if analysis_included == "false":
        return "false"
    if rejected:
        return "false"
    return analysis_included


def _safe_percent(numerator: float, denominator: float) -> float | None:
    if denominator <= 0:
        return None
    return 100.0 * float(numerator) / float(denominator)


def _open_text(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8", newline="")
    return path.open("r", encoding="utf-8", newline="")


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


def _default_trial_table_path(bids_root: Path) -> Path:
    return (
        Path(__file__).resolve().parent
        / "reports"
        / f"trial_table_{bids_root.name}.tsv"
    )


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _default_participant_bids_sample_drop_summary_csv_path() -> Path:
    return _reports_dir() / "participant_bids_sample_drop_summary.csv"


def _read_participants(participants_tsv: Path) -> dict[str, dict[str, str]]:
    if not participants_tsv.exists():
        return {}
    out: dict[str, dict[str, str]] = {}
    with participants_tsv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            subject = (row.get("participant_id") or "").strip()
            if not subject:
                continue
            out[subject] = row
    return out


def _resolve_subject_paths(subject_dir: Path, task: str) -> SubjectPaths:
    subject = subject_dir.name
    return SubjectPaths(
        subject=subject,
        eeg_vhdr=subject_dir / "eeg" / f"{subject}_task-{task}_eeg.vhdr",
        eeg_json=subject_dir / "eeg" / f"{subject}_task-{task}_eeg.json",
        events_tsv=subject_dir / "eeg" / f"{subject}_task-{task}_events.tsv",
        ecg_tsv=subject_dir / "ecg" / f"{subject}_task-{task}_recording-ecg_physio.tsv",
        ecg_json=subject_dir / "ecg" / f"{subject}_task-{task}_recording-ecg_physio.json",
        pupil_tsv=subject_dir / "pupil" / f"{subject}_task-{task}_pupil.tsv",
        pupil_json=subject_dir / "pupil" / f"{subject}_task-{task}_eyetrack.json",
    )


def _count_table_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        try:
            next(reader)
        except StopIteration:
            return 0
        return sum(1 for _ in reader)


def _summarize_eeg_recording(paths: SubjectPaths) -> dict[str, float | int | None]:
    out: dict[str, float | int | None] = {
        "eeg_samples": None,
        "eeg_sampling_frequency_hz": None,
        "eeg_duration_s": None,
    }
    if not paths.eeg_vhdr.exists():
        return out
    eeg_binary = paths.eeg_vhdr.with_suffix(".eeg")
    if not eeg_binary.exists():
        return out
    file_size = eeg_binary.stat().st_size

    n_channels: int | None = None
    sfreq: float | None = None
    if paths.eeg_json.exists():
        meta = json.loads(paths.eeg_json.read_text(encoding="utf-8"))
        sfreq_raw = meta.get("SamplingFrequency")
        if isinstance(sfreq_raw, (int, float)):
            sfreq = float(sfreq_raw)
        count_keys = [
            "EEGChannelCount",
            "ECGChannelCount",
            "EOGChannelCount",
            "EMGChannelCount",
            "MISCChannelCount",
            "TriggerChannelCount",
        ]
        n_channels_tmp = 0
        for key in count_keys:
            value = meta.get(key)
            if isinstance(value, int):
                n_channels_tmp += value
        if n_channels_tmp > 0:
            n_channels = n_channels_tmp

    if n_channels is None:
        with paths.eeg_vhdr.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line.startswith("NumberOfChannels="):
                    n_channels = int(line.split("=", 1)[1].strip())
                if line.startswith("SamplingInterval=") and sfreq is None:
                    interval_us = float(line.split("=", 1)[1].strip())
                    if interval_us > 0:
                        sfreq = 1_000_000.0 / interval_us
                if n_channels is not None and sfreq is not None:
                    break

    if n_channels is None or sfreq is None or sfreq <= 0:
        return out

    samples = file_size / (n_channels * 4.0)
    if not math.isfinite(samples) or samples <= 0:
        return out
    out["eeg_samples"] = int(round(samples))
    out["eeg_sampling_frequency_hz"] = float(sfreq)
    out["eeg_duration_s"] = float(samples / sfreq)
    return out


def _load_ecg_series(ecg_tsv: Path) -> tuple[np.ndarray, np.ndarray]:
    times: list[float] = []
    signal_values: list[float] = []
    if not ecg_tsv.exists():
        return np.array([], dtype=np.float64), np.array([], dtype=np.float64)

    with _open_text(ecg_tsv) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) < 2:
                continue
            time_value = _as_float(row[0])
            ecg_value = _as_float(row[1])
            if time_value is None or ecg_value is None:
                continue
            times.append(time_value)
            signal_values.append(ecg_value)
    return np.asarray(times, dtype=np.float64), np.asarray(signal_values, dtype=np.float64)


def _infer_sampling_frequency(times: np.ndarray) -> float | None:
    if times.size < 3:
        return None
    diffs = np.diff(times)
    diffs = diffs[np.isfinite(diffs) & (diffs > 0)]
    if diffs.size == 0:
        return None
    dt = float(np.median(diffs))
    if dt <= 0:
        return None
    return 1.0 / dt


def _detect_ecg_peaks(
    times: np.ndarray,
    signal_values: np.ndarray,
    sfreq: float,
) -> tuple[np.ndarray, str | None]:
    centered = signal_values - np.median(signal_values)
    nyquist = 0.5 * sfreq
    low_hz = 5.0
    high_hz = 25.0
    if nyquist <= low_hz:
        return np.array([], dtype=int), "Sampling rate too low for ECG band-pass peak detection."
    high_hz = min(high_hz, 0.95 * nyquist)
    low = low_hz / nyquist
    high = high_hz / nyquist

    try:
        b, a = sp_signal.butter(2, [low, high], btype="bandpass")
        filtered = sp_signal.filtfilt(b, a, centered)
    except Exception:
        return np.array([], dtype=int), "Band-pass filtering failed."

    distance = max(1, int(round(0.3 * sfreq)))
    mad = np.median(np.abs(filtered - np.median(filtered)))
    robust_scale = 1.4826 * mad if mad > 0 else float(np.std(filtered))
    fallback_scale = float(np.percentile(np.abs(filtered), 75)) * 0.30
    prominence = max(robust_scale * 1.5, fallback_scale, 1e-9)

    peaks_pos, _ = sp_signal.find_peaks(filtered, distance=distance, prominence=prominence)
    peaks_neg, _ = sp_signal.find_peaks(-filtered, distance=distance, prominence=prominence)
    pos_eval = _evaluate_peaks(times, peaks_pos)
    neg_eval = _evaluate_peaks(times, peaks_neg)
    use_pos = (pos_eval["n_rr_valid"] or 0) >= (neg_eval["n_rr_valid"] or 0)
    chosen_peaks = peaks_pos if use_pos else peaks_neg
    return chosen_peaks, None


def _hr_series_from_peaks(
    times: np.ndarray,
    peaks: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if peaks.size < 2:
        return np.array([], dtype=np.float64), np.array([], dtype=np.float64)
    beat_times = times[peaks]
    rr = np.diff(beat_times)
    rr = rr[np.isfinite(rr) & (rr > 0)]
    if rr.size == 0:
        return np.array([], dtype=np.float64), np.array([], dtype=np.float64)
    hr = 60.0 / rr
    hr_time = beat_times[:-1] + (rr / 2.0)
    valid = np.isfinite(hr) & np.isfinite(hr_time) & (hr >= 35.0) & (hr <= 180.0)
    return hr_time[valid], hr[valid]


def _evaluate_peaks(times: np.ndarray, peaks: np.ndarray) -> dict[str, float | int | None]:
    rr = np.diff(times[peaks]) if peaks.size > 1 else np.array([], dtype=np.float64)
    rr = rr[np.isfinite(rr) & (rr > 0)]
    if rr.size == 0:
        return {
            "detected_beats": int(peaks.size),
            "hr_mean_bpm": None,
            "hr_median_bpm": None,
            "hr_p05_bpm": None,
            "hr_p95_bpm": None,
            "hr_out_of_range_pct": None,
            "hr_valid_ratio": None,
            "n_rr_valid": 0,
        }
    hr_all = 60.0 / rr
    valid_mask = (hr_all >= 35.0) & (hr_all <= 180.0)
    hr_valid = hr_all[valid_mask]
    hr_out = 100.0 * float(np.count_nonzero(~valid_mask)) / float(hr_all.size)
    if hr_valid.size == 0:
        return {
            "detected_beats": int(peaks.size),
            "hr_mean_bpm": None,
            "hr_median_bpm": None,
            "hr_p05_bpm": None,
            "hr_p95_bpm": None,
            "hr_out_of_range_pct": hr_out,
            "hr_valid_ratio": 0.0,
            "n_rr_valid": 0,
        }
    return {
        "detected_beats": int(peaks.size),
        "hr_mean_bpm": float(np.mean(hr_valid)),
        "hr_median_bpm": float(np.median(hr_valid)),
        "hr_p05_bpm": float(np.percentile(hr_valid, 5)),
        "hr_p95_bpm": float(np.percentile(hr_valid, 95)),
        "hr_out_of_range_pct": hr_out,
        "hr_valid_ratio": float(hr_valid.size) / float(hr_all.size),
        "n_rr_valid": int(hr_valid.size),
    }


def _summarize_ecg_quality(
    ecg_tsv: Path,
    ecg_json: Path,
) -> tuple[dict[str, float | int | str | None], np.ndarray, np.ndarray]:
    out: dict[str, float | int | str | None] = {
        "ecg_samples": 0,
        "ecg_sampling_frequency_hz": None,
        "ecg_duration_s": None,
        "ecg_signal_std": None,
        "ecg_signal_p1_p99_range": None,
        "ecg_detected_beats": None,
        "hr_mean_bpm": None,
        "hr_median_bpm": None,
        "hr_p05_bpm": None,
        "hr_p95_bpm": None,
        "hr_out_of_range_pct": None,
        "hr_valid_ratio": None,
        "ecg_quality_flag": "fail",
        "ecg_quality_note": "Missing ECG files.",
    }
    empty_hr = np.array([], dtype=np.float64)
    if not ecg_tsv.exists() or not ecg_json.exists():
        return out, empty_hr, empty_hr

    times, signal_values = _load_ecg_series(ecg_tsv)
    out["ecg_samples"] = int(signal_values.size)
    if signal_values.size < 100:
        out["ecg_quality_note"] = "Too few ECG samples."
        return out, empty_hr, empty_hr

    sidecar = json.loads(ecg_json.read_text(encoding="utf-8"))
    sfreq_raw = sidecar.get("SamplingFrequency")
    sfreq: float | None = float(sfreq_raw) if isinstance(sfreq_raw, (int, float)) else None
    if sfreq is None or sfreq <= 0:
        sfreq = _infer_sampling_frequency(times)
    out["ecg_sampling_frequency_hz"] = sfreq

    duration_s = float(times[-1] - times[0]) if times.size > 1 else None
    out["ecg_duration_s"] = duration_s
    out["ecg_signal_std"] = float(np.std(signal_values))
    p1 = float(np.percentile(signal_values, 1))
    p99 = float(np.percentile(signal_values, 99))
    out["ecg_signal_p1_p99_range"] = p99 - p1

    if sfreq is None or sfreq <= 0:
        out["ecg_quality_note"] = "Could not infer ECG sampling frequency."
        return out, empty_hr, empty_hr
    if duration_s is None or duration_s < 30.0:
        out["ecg_quality_note"] = "ECG duration too short for HR quality check."
        return out, empty_hr, empty_hr
    if out["ecg_signal_p1_p99_range"] is not None and out["ecg_signal_p1_p99_range"] < 100.0:
        out["ecg_quality_note"] = "ECG dynamic range is very low (possible flat/no signal)."
        return out, empty_hr, empty_hr

    peaks, peak_error = _detect_ecg_peaks(times, signal_values, sfreq)
    if peak_error is not None:
        out["ecg_quality_note"] = peak_error
        return out, empty_hr, empty_hr
    chosen = _evaluate_peaks(times, peaks)
    hr_times, hr_values = _hr_series_from_peaks(times, peaks)

    out["ecg_detected_beats"] = chosen["detected_beats"]
    out["hr_mean_bpm"] = chosen["hr_mean_bpm"]
    out["hr_median_bpm"] = chosen["hr_median_bpm"]
    out["hr_p05_bpm"] = chosen["hr_p05_bpm"]
    out["hr_p95_bpm"] = chosen["hr_p95_bpm"]
    out["hr_out_of_range_pct"] = chosen["hr_out_of_range_pct"]
    out["hr_valid_ratio"] = chosen["hr_valid_ratio"]

    n_rr_valid = int(chosen["n_rr_valid"] or 0)
    hr_mean = chosen["hr_mean_bpm"]
    valid_ratio = chosen["hr_valid_ratio"]
    if n_rr_valid < 100 or hr_mean is None:
        out["ecg_quality_flag"] = "fail"
        out["ecg_quality_note"] = "Too few valid RR intervals; heartbeat detection unstable."
        return out, hr_times, hr_values

    if hr_mean < 35.0 or hr_mean > 180.0:
        out["ecg_quality_flag"] = "fail"
        out["ecg_quality_note"] = f"Mean HR out of physiological range ({hr_mean:.1f} bpm)."
        return out, hr_times, hr_values

    if valid_ratio is not None and valid_ratio < 0.70:
        out["ecg_quality_flag"] = "warn"
        out["ecg_quality_note"] = f"Low valid RR ratio ({valid_ratio:.2f}); noisy/partial ECG likely."
        return out, hr_times, hr_values

    if hr_mean < 40.0 or hr_mean > 160.0:
        out["ecg_quality_flag"] = "warn"
        out["ecg_quality_note"] = f"Mean HR is outside broad expected range ({hr_mean:.1f} bpm)."
        return out, hr_times, hr_values

    out["ecg_quality_flag"] = "pass"
    out["ecg_quality_note"] = "ECG heartbeat detection and HR range look acceptable."
    return out, hr_times, hr_values


def _read_marker_onsets(events_tsv: Path) -> dict[str, list[float]]:
    out: dict[str, list[float]] = {
        "started_tutorial_artihmetic": [],
        "finished_tutorial_arithmetic": [],
        "started_arithmetic": [],
        "finished_arithmetic": [],
    }
    if not events_tsv.exists():
        return out

    with events_tsv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            tt = (row.get("trial_type") or "").strip()
            onset = _as_float(row.get("onset"))
            if onset is None:
                continue
            if tt in out:
                out[tt].append(onset)
    return out


def _window_hr_stats(
    hr_times: np.ndarray,
    hr_values: np.ndarray,
    start_s: float | None,
    end_s: float | None,
) -> dict[str, float | int | None]:
    if start_s is None or end_s is None or end_s <= start_s:
        return {
            "start_s": start_s,
            "end_s": end_s,
            "n_rr": 0,
            "mean_bpm": None,
            "median_bpm": None,
            "p05_bpm": None,
            "p95_bpm": None,
        }
    if hr_times.size == 0 or hr_values.size == 0:
        return {
            "start_s": start_s,
            "end_s": end_s,
            "n_rr": 0,
            "mean_bpm": None,
            "median_bpm": None,
            "p05_bpm": None,
            "p95_bpm": None,
        }
    mask = (hr_times >= start_s) & (hr_times < end_s)
    vals = hr_values[mask]
    if vals.size == 0:
        return {
            "start_s": start_s,
            "end_s": end_s,
            "n_rr": 0,
            "mean_bpm": None,
            "median_bpm": None,
            "p05_bpm": None,
            "p95_bpm": None,
        }
    return {
        "start_s": start_s,
        "end_s": end_s,
        "n_rr": int(vals.size),
        "mean_bpm": float(np.mean(vals)),
        "median_bpm": float(np.median(vals)),
        "p05_bpm": float(np.percentile(vals, 5)),
        "p95_bpm": float(np.percentile(vals, 95)),
    }


def _read_events_summary(events_tsv: Path) -> dict[str, int]:
    out = {
        "cue_markers": 0,
        "outcome_markers": 0,
        "dropped_events": 0,
        "dropped_samples_total": 0,
        "started_arithmetic_markers": 0,
        "finished_arithmetic_markers": 0,
        "started_tutorial_markers": 0,
        "finished_tutorial_markers": 0,
    }
    if not events_tsv.exists():
        return out

    with events_tsv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            trial_type = (row.get("trial_type") or "").strip()
            if CUE_TRIAL_RE.match(trial_type):
                out["cue_markers"] += 1
            difficulty_range = (row.get("difficulty_range") or "").strip()
            outcome = (row.get("outcome") or "").strip()
            response_accuracy = (row.get("response_accuracy") or "").strip()
            if (
                difficulty_range
                and difficulty_range.lower() != "n/a"
                and outcome in ("Correct", "Wrong")
                and response_accuracy in ("0", "1")
            ):
                out["outcome_markers"] += 1

            if trial_type == "dropped_samples":
                out["dropped_events"] += 1
                dropped_count = _as_int(row.get("dropped_samples"))
                if dropped_count is not None:
                    out["dropped_samples_total"] += dropped_count
            elif trial_type == "started_arithmetic":
                out["started_arithmetic_markers"] += 1
            elif trial_type == "finished_arithmetic":
                out["finished_arithmetic_markers"] += 1
            elif trial_type == "started_tutorial_artihmetic":
                out["started_tutorial_markers"] += 1
            elif trial_type == "finished_tutorial_arithmetic":
                out["finished_tutorial_markers"] += 1
    return out


def _read_trial_table(trial_table_path: Path) -> list[dict[str, str]]:
    if not trial_table_path.exists():
        raise FileNotFoundError(
            f"Trial table not found: {trial_table_path}. "
            "Run analysis_pipeline/build_trial_table.py first."
        )
    with trial_table_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def _summarize_pupil_quality(pupil_tsv: Path, pupil_json: Path) -> dict[str, float | int | None]:
    out: dict[str, float | int | None] = {
        "pupil_samples": 0,
        "pupil_mean_confidence": None,
        "pupil_pct_conf_lt_0_8": None,
        "pupil_pct_conf_lt_0_6": None,
        "pupil_pct_missing_confidence": None,
        "pupil_pct_nonpositive_size": None,
    }
    if not pupil_tsv.exists() or not pupil_json.exists():
        return out

    sidecar = json.loads(pupil_json.read_text(encoding="utf-8"))
    columns = sidecar.get("Columns")
    if not isinstance(columns, list):
        return out
    col_idx = {str(name): idx for idx, name in enumerate(columns)}
    conf_idx = col_idx.get("confidence")
    size_idx = col_idx.get("pupil_size")

    n = 0
    conf_values: list[float] = []
    conf_missing = 0
    conf_lt_08 = 0
    conf_lt_06 = 0
    size_nonpositive = 0

    with _open_text(pupil_tsv) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if not row:
                continue
            n += 1
            if conf_idx is not None and conf_idx < len(row):
                conf = _as_float(row[conf_idx])
                if conf is None:
                    conf_missing += 1
                else:
                    conf_values.append(conf)
                    if conf < 0.8:
                        conf_lt_08 += 1
                    if conf < 0.6:
                        conf_lt_06 += 1
            else:
                conf_missing += 1

            if size_idx is not None and size_idx < len(row):
                size = _as_float(row[size_idx])
                if size is not None and size <= 0:
                    size_nonpositive += 1

    if n == 0:
        return out

    out["pupil_samples"] = n
    out["pupil_mean_confidence"] = mean(conf_values) if conf_values else None
    out["pupil_pct_conf_lt_0_8"] = 100.0 * conf_lt_08 / n
    out["pupil_pct_conf_lt_0_6"] = 100.0 * conf_lt_06 / n
    out["pupil_pct_missing_confidence"] = 100.0 * conf_missing / n
    out["pupil_pct_nonpositive_size"] = 100.0 * size_nonpositive / n
    return out


def _subject_rows_to_table_rows(
    subject_rows: list[dict[str, Any]],
) -> list[dict[str, str]]:
    fields = [
        "participant_id",
        "analysis_included",
        "has_eeg",
        "has_ecg",
        "has_pupil",
        "eeg_duration_s",
        "ecg_samples",
        "ecg_sampling_frequency_hz",
        "ecg_duration_s",
        "ecg_signal_std",
        "ecg_signal_p1_p99_range",
        "ecg_detected_beats",
        "hr_mean_bpm",
        "hr_median_bpm",
        "hr_p05_bpm",
        "hr_p95_bpm",
        "hr_out_of_range_pct",
        "hr_valid_ratio",
        "ecg_quality_flag",
        "ecg_quality_note",
        "baseline_window_start_s",
        "baseline_window_end_s",
        "baseline_hr_n_rr",
        "baseline_hr_mean_bpm",
        "baseline_hr_median_bpm",
        "baseline_hr_p05_bpm",
        "baseline_hr_p95_bpm",
        "task_window_start_s",
        "task_window_end_s",
        "task_hr_n_rr",
        "task_hr_mean_bpm",
        "task_hr_median_bpm",
        "task_hr_p05_bpm",
        "task_hr_p95_bpm",
        "task_minus_baseline_hr_mean_bpm",
        "pupil_samples",
        "events_rows",
        "trial_rows_total",
        "trial_rows_main",
        "trial_rows_tutorial",
        "event_cue_markers",
        "event_outcome_markers",
        "started_arithmetic_markers",
        "finished_arithmetic_markers",
        "dropped_samples_total_events",
        "dropped_samples_main_trials",
        "dropped_samples_main_trials_per_trial_mean",
        "dropped_samples_main_trials_per_trial_p95",
        "dropped_samples_main_trials_mean_threshold",
        "dropped_samples_main_trials_p95_threshold",
        "dropped_samples_main_trials_mean_exceeds_threshold",
        "dropped_samples_main_trials_p95_exceeds_threshold",
        "dropped_samples_main_trials_mean_threshold_eeg",
        "dropped_samples_main_trials_p95_threshold_eeg",
        "dropped_samples_main_trials_mean_exceeds_threshold_eeg",
        "dropped_samples_main_trials_p95_exceeds_threshold_eeg",
        "dropped_samples_main_trials_mean_threshold_ecg",
        "dropped_samples_main_trials_p95_threshold_ecg",
        "dropped_samples_main_trials_mean_exceeds_threshold_ecg",
        "dropped_samples_main_trials_p95_exceeds_threshold_ecg",
        "response_time_main_mean_s",
        "response_time_main_median_s",
        "response_time_main_p95_s",
        "pupil_mean_confidence",
        "pupil_pct_conf_lt_0_8",
        "pupil_pct_conf_lt_0_6",
        "pupil_pct_missing_confidence",
        "pupil_pct_nonpositive_size",
        "anomaly_count",
        "anomalies",
        "qc_flagged",
        "qc_rejected",
        "qc_rejected_any_modality",
        "qc_rejected_all_modalities",
        "qc_rejected_eeg",
        "qc_rejected_ecg",
        "qc_rejected_pupil",
        "qc_reason_count",
        "qc_rejection_reasons",
        "qc_reason_count_eeg",
        "qc_reason_count_ecg",
        "qc_reason_count_pupil",
        "qc_rejection_reasons_eeg",
        "qc_rejection_reasons_ecg",
        "qc_rejection_reasons_pupil",
        "analysis_included_effective",
        "analysis_included_effective_eeg",
        "analysis_included_effective_ecg",
        "analysis_included_effective_pupil",
    ]
    out: list[dict[str, str]] = []
    for row in subject_rows:
        out.append(
            {
                "participant_id": row["participant_id"],
                "analysis_included": row["analysis_included"],
                "has_eeg": "true" if row["has_eeg"] else "false",
                "has_ecg": "true" if row["has_ecg"] else "false",
                "has_pupil": "true" if row["has_pupil"] else "false",
                "eeg_duration_s": _format_float(row["eeg_duration_s"], 3),
                "ecg_samples": str(row["ecg_samples"]),
                "ecg_sampling_frequency_hz": _format_float(row["ecg_sampling_frequency_hz"], 3),
                "ecg_duration_s": _format_float(row["ecg_duration_s"], 3),
                "ecg_signal_std": _format_float(row["ecg_signal_std"], 3),
                "ecg_signal_p1_p99_range": _format_float(row["ecg_signal_p1_p99_range"], 3),
                "ecg_detected_beats": "n/a"
                if row["ecg_detected_beats"] is None
                else str(row["ecg_detected_beats"]),
                "hr_mean_bpm": _format_float(row["hr_mean_bpm"], 3),
                "hr_median_bpm": _format_float(row["hr_median_bpm"], 3),
                "hr_p05_bpm": _format_float(row["hr_p05_bpm"], 3),
                "hr_p95_bpm": _format_float(row["hr_p95_bpm"], 3),
                "hr_out_of_range_pct": _format_float(row["hr_out_of_range_pct"], 2),
                "hr_valid_ratio": _format_float(row["hr_valid_ratio"], 3),
                "ecg_quality_flag": row["ecg_quality_flag"],
                "ecg_quality_note": row["ecg_quality_note"],
                "baseline_window_start_s": _format_float(row["baseline_window_start_s"], 3),
                "baseline_window_end_s": _format_float(row["baseline_window_end_s"], 3),
                "baseline_hr_n_rr": str(row["baseline_hr_n_rr"]),
                "baseline_hr_mean_bpm": _format_float(row["baseline_hr_mean_bpm"], 3),
                "baseline_hr_median_bpm": _format_float(row["baseline_hr_median_bpm"], 3),
                "baseline_hr_p05_bpm": _format_float(row["baseline_hr_p05_bpm"], 3),
                "baseline_hr_p95_bpm": _format_float(row["baseline_hr_p95_bpm"], 3),
                "task_window_start_s": _format_float(row["task_window_start_s"], 3),
                "task_window_end_s": _format_float(row["task_window_end_s"], 3),
                "task_hr_n_rr": str(row["task_hr_n_rr"]),
                "task_hr_mean_bpm": _format_float(row["task_hr_mean_bpm"], 3),
                "task_hr_median_bpm": _format_float(row["task_hr_median_bpm"], 3),
                "task_hr_p05_bpm": _format_float(row["task_hr_p05_bpm"], 3),
                "task_hr_p95_bpm": _format_float(row["task_hr_p95_bpm"], 3),
                "task_minus_baseline_hr_mean_bpm": _format_float(
                    row["task_minus_baseline_hr_mean_bpm"], 3
                ),
                "pupil_samples": str(row["pupil_samples"]),
                "events_rows": str(row["events_rows"]),
                "trial_rows_total": str(row["trial_rows_total"]),
                "trial_rows_main": str(row["trial_rows_main"]),
                "trial_rows_tutorial": str(row["trial_rows_tutorial"]),
                "event_cue_markers": str(row["event_cue_markers"]),
                "event_outcome_markers": str(row["event_outcome_markers"]),
                "started_arithmetic_markers": str(row["started_arithmetic_markers"]),
                "finished_arithmetic_markers": str(row["finished_arithmetic_markers"]),
                "dropped_samples_total_events": str(row["dropped_samples_total_events"]),
                "dropped_samples_main_trials": str(row["dropped_samples_main_trials"]),
                "dropped_samples_main_trials_per_trial_mean": _format_float(
                    row["dropped_samples_main_trials_per_trial_mean"], 3
                ),
                "dropped_samples_main_trials_per_trial_p95": _format_float(
                    row["dropped_samples_main_trials_per_trial_p95"], 3
                ),
                "dropped_samples_main_trials_mean_threshold": _format_float(
                    row["dropped_samples_main_trials_mean_threshold"], 3
                ),
                "dropped_samples_main_trials_p95_threshold": _format_float(
                    row["dropped_samples_main_trials_p95_threshold"], 3
                ),
                "dropped_samples_main_trials_mean_exceeds_threshold": "true"
                if row["dropped_samples_main_trials_mean_exceeds_threshold"]
                else "false",
                "dropped_samples_main_trials_p95_exceeds_threshold": "true"
                if row["dropped_samples_main_trials_p95_exceeds_threshold"]
                else "false",
                "dropped_samples_main_trials_mean_threshold_eeg": _format_float(
                    row["dropped_samples_main_trials_mean_threshold_eeg"], 3
                ),
                "dropped_samples_main_trials_p95_threshold_eeg": _format_float(
                    row["dropped_samples_main_trials_p95_threshold_eeg"], 3
                ),
                "dropped_samples_main_trials_mean_exceeds_threshold_eeg": "true"
                if row["dropped_samples_main_trials_mean_exceeds_threshold_eeg"]
                else "false",
                "dropped_samples_main_trials_p95_exceeds_threshold_eeg": "true"
                if row["dropped_samples_main_trials_p95_exceeds_threshold_eeg"]
                else "false",
                "dropped_samples_main_trials_mean_threshold_ecg": _format_float(
                    row["dropped_samples_main_trials_mean_threshold_ecg"], 3
                ),
                "dropped_samples_main_trials_p95_threshold_ecg": _format_float(
                    row["dropped_samples_main_trials_p95_threshold_ecg"], 3
                ),
                "dropped_samples_main_trials_mean_exceeds_threshold_ecg": "true"
                if row["dropped_samples_main_trials_mean_exceeds_threshold_ecg"]
                else "false",
                "dropped_samples_main_trials_p95_exceeds_threshold_ecg": "true"
                if row["dropped_samples_main_trials_p95_exceeds_threshold_ecg"]
                else "false",
                "response_time_main_mean_s": _format_float(row["response_time_main_mean_s"], 3),
                "response_time_main_median_s": _format_float(row["response_time_main_median_s"], 3),
                "response_time_main_p95_s": _format_float(row["response_time_main_p95_s"], 3),
                "pupil_mean_confidence": _format_float(row["pupil_mean_confidence"], 4),
                "pupil_pct_conf_lt_0_8": _format_float(row["pupil_pct_conf_lt_0_8"], 2),
                "pupil_pct_conf_lt_0_6": _format_float(row["pupil_pct_conf_lt_0_6"], 2),
                "pupil_pct_missing_confidence": _format_float(row["pupil_pct_missing_confidence"], 2),
                "pupil_pct_nonpositive_size": _format_float(row["pupil_pct_nonpositive_size"], 2),
                "anomaly_count": str(len(row["anomalies"])),
                "anomalies": " | ".join(row["anomalies"]),
                "qc_flagged": _bool_text(row["qc_flagged"]),
                "qc_rejected": _bool_text(row["qc_rejected"]),
                "qc_rejected_any_modality": _bool_text(row["qc_rejected_any_modality"]),
                "qc_rejected_all_modalities": _bool_text(row["qc_rejected_all_modalities"]),
                "qc_rejected_eeg": _bool_text(row["qc_rejected_eeg"]),
                "qc_rejected_ecg": _bool_text(row["qc_rejected_ecg"]),
                "qc_rejected_pupil": _bool_text(row["qc_rejected_pupil"]),
                "qc_reason_count": str(row["qc_reason_count"]),
                "qc_rejection_reasons": " | ".join(row["qc_rejection_reasons"]),
                "qc_reason_count_eeg": str(row["qc_reason_count_eeg"]),
                "qc_reason_count_ecg": str(row["qc_reason_count_ecg"]),
                "qc_reason_count_pupil": str(row["qc_reason_count_pupil"]),
                "qc_rejection_reasons_eeg": " | ".join(row["qc_rejection_reasons_eeg"]),
                "qc_rejection_reasons_ecg": " | ".join(row["qc_rejection_reasons_ecg"]),
                "qc_rejection_reasons_pupil": " | ".join(row["qc_rejection_reasons_pupil"]),
                "analysis_included_effective": row["analysis_included_effective"],
                "analysis_included_effective_eeg": row["analysis_included_effective_eeg"],
                "analysis_included_effective_ecg": row["analysis_included_effective_ecg"],
                "analysis_included_effective_pupil": row["analysis_included_effective_pupil"],
            }
        )
    return out


def _subject_rows_to_bids_sample_drop_summary_rows(
    subject_rows: list[dict[str, Any]],
) -> list[dict[str, str]]:
    fields = [
        "participant_id",
        "analysis_included",
        "has_eeg",
        "eeg_sampling_frequency_hz",
        "eeg_recorded_samples",
        "eeg_recorded_duration_s",
        "eeg_dropped_samples_total_events",
        "eeg_total_samples_including_drops",
        "eeg_dropped_sample_percent",
        "has_ecg",
        "ecg_sampling_frequency_hz",
        "ecg_recorded_samples",
        "ecg_recorded_duration_s",
        "ecg_dropped_samples_total_events",
        "ecg_total_samples_including_drops",
        "ecg_dropped_sample_percent",
        "has_pupil",
        "pupil_recorded_samples",
        "events_rows",
        "trial_rows_total",
        "trial_rows_main",
        "trial_rows_tutorial",
        "dropped_samples_total_events",
        "dropped_samples_main_trials",
    ]
    out: list[dict[str, str]] = []
    for row in subject_rows:
        dropped_total = int(row["dropped_samples_total_events"] or 0)
        eeg_recorded_samples = int(row.get("eeg_samples") or 0)
        ecg_recorded_samples = int(row["ecg_samples"] or 0)
        pupil_recorded_samples = int(row["pupil_samples"] or 0)
        eeg_total_with_drops = eeg_recorded_samples + dropped_total if eeg_recorded_samples > 0 else 0
        ecg_total_with_drops = ecg_recorded_samples + dropped_total if ecg_recorded_samples > 0 else 0
        out.append(
            {
                "participant_id": row["participant_id"],
                "analysis_included": row["analysis_included"],
                "has_eeg": "true" if row["has_eeg"] else "false",
                "eeg_sampling_frequency_hz": _format_float(row.get("eeg_sampling_frequency_hz"), 3),
                "eeg_recorded_samples": str(eeg_recorded_samples),
                "eeg_recorded_duration_s": _format_float(row.get("eeg_duration_s"), 3),
                "eeg_dropped_samples_total_events": str(dropped_total if eeg_recorded_samples > 0 else 0),
                "eeg_total_samples_including_drops": str(eeg_total_with_drops),
                "eeg_dropped_sample_percent": _format_float(
                    _safe_percent(float(dropped_total), float(eeg_total_with_drops)),
                    3,
                ),
                "has_ecg": "true" if row["has_ecg"] else "false",
                "ecg_sampling_frequency_hz": _format_float(row["ecg_sampling_frequency_hz"], 3),
                "ecg_recorded_samples": str(ecg_recorded_samples),
                "ecg_recorded_duration_s": _format_float(row["ecg_duration_s"], 3),
                "ecg_dropped_samples_total_events": str(dropped_total if ecg_recorded_samples > 0 else 0),
                "ecg_total_samples_including_drops": str(ecg_total_with_drops),
                "ecg_dropped_sample_percent": _format_float(
                    _safe_percent(float(dropped_total), float(ecg_total_with_drops)),
                    3,
                ),
                "has_pupil": "true" if row["has_pupil"] else "false",
                "pupil_recorded_samples": str(pupil_recorded_samples),
                "events_rows": str(row["events_rows"]),
                "trial_rows_total": str(row["trial_rows_total"]),
                "trial_rows_main": str(row["trial_rows_main"]),
                "trial_rows_tutorial": str(row["trial_rows_tutorial"]),
                "dropped_samples_total_events": str(dropped_total),
                "dropped_samples_main_trials": str(row["dropped_samples_main_trials"]),
            }
        )
    return out


def _percentile(values: list[float], pct: float) -> float | None:
    if not values:
        return None
    sorted_values = sorted(values)
    idx = int(round((len(sorted_values) - 1) * pct))
    idx = max(0, min(idx, len(sorted_values) - 1))
    return sorted_values[idx]


def _write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        with path.open("w", encoding="utf-8", newline="") as f:
            f.write("")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        with path.open("w", encoding="utf-8", newline="") as f:
            f.write("")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=list(rows[0].keys()), delimiter=",", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def _subject_rows_in_order(
    subject_rows: list[dict[str, Any]],
    predicate: Callable[[dict[str, Any]], bool] | None = None,
) -> list[dict[str, Any]]:
    if predicate is None:
        return list(subject_rows)
    return [row for row in subject_rows if predicate(row)]


def _plot_dropped_samples(subject_rows: list[dict[str, Any]], fig_dir: Path) -> Path:
    fig_dir.mkdir(parents=True, exist_ok=True)
    ordered_rows = _subject_rows_in_order(subject_rows)
    labels = [row["participant_id"] for row in ordered_rows]
    values = [row["dropped_samples_main_trials"] for row in ordered_rows]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, values, color="#2F6C8F")
    ax.set_title("Dropped Samples in Main Trials by Subject")
    ax.set_ylabel("Dropped samples (sum across main trials)")
    ax.set_xlabel("Subject")
    ax.tick_params(axis="x", rotation=60)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()

    out_path = fig_dir / "dropped_samples_main_per_subject.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _plot_dropped_sample_flags_by_modality(
    subject_rows: list[dict[str, Any]],
    fig_dir: Path,
) -> Path:
    fig_dir.mkdir(parents=True, exist_ok=True)
    n_subjects = len(subject_rows)
    eeg_flagged = [
        row["participant_id"]
        for row in subject_rows
        if row["dropped_samples_main_trials_mean_exceeds_threshold_eeg"]
        or row["dropped_samples_main_trials_p95_exceeds_threshold_eeg"]
    ]
    ecg_flagged = [
        row["participant_id"]
        for row in subject_rows
        if row["dropped_samples_main_trials_mean_exceeds_threshold_ecg"]
        or row["dropped_samples_main_trials_p95_exceeds_threshold_ecg"]
    ]

    panels = [
        ("EEG", eeg_flagged, "#2F6C8F"),
        ("ECG", ecg_flagged, "#B15B5B"),
    ]
    max_lines = max(1, len(eeg_flagged), len(ecg_flagged))
    fig, axes = plt.subplots(1, 2, figsize=(10, max(3.8, 1.4 + 0.33 * max_lines)))
    fig.suptitle("Subjects Flagged by Missing-Sample Thresholds")

    for ax, (label, subjects, color) in zip(axes, panels):
        ax.axis("off")
        ax.set_title(f"{label}: {len(subjects)}/{n_subjects}")
        text = "\n".join(subjects) if subjects else "None"
        ax.text(
            0.03,
            0.97,
            text,
            ha="left",
            va="top",
            fontsize=10,
            family="monospace",
            color=color,
            transform=ax.transAxes,
        )
    fig.tight_layout(rect=[0.0, 0.0, 1.0, 0.95])

    out_path = fig_dir / "dropped_samples_flagged_subjects_eeg_ecg.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _plot_pupil_confidence(subject_rows: list[dict[str, Any]], fig_dir: Path) -> Path:
    fig_dir.mkdir(parents=True, exist_ok=True)
    ordered_rows = _subject_rows_in_order(
        subject_rows,
        predicate=lambda row: row["pupil_mean_confidence"] is not None,
    )
    labels = [row["participant_id"] for row in ordered_rows]
    values = [row["pupil_mean_confidence"] for row in ordered_rows]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, values, color="#4E8B31")
    ax.axhline(0.8, color="#B33A3A", linestyle="--", linewidth=1, label="0.8 threshold")
    ax.axhline(0.6, color="#D77A1F", linestyle="--", linewidth=1, label="0.6 threshold")
    ax.set_title("Mean Pupil Confidence by Subject")
    ax.set_ylabel("Mean confidence")
    ax.set_xlabel("Subject")
    ax.set_ylim(0.0, 1.0)
    ax.tick_params(axis="x", rotation=60)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="lower right")
    fig.tight_layout()

    out_path = fig_dir / "pupil_mean_confidence_per_subject.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _plot_hr_mean(subject_rows: list[dict[str, Any]], fig_dir: Path) -> Path:
    fig_dir.mkdir(parents=True, exist_ok=True)
    ordered_rows = _subject_rows_in_order(
        subject_rows,
        predicate=lambda row: row["hr_mean_bpm"] is not None,
    )
    labels = [row["participant_id"] for row in ordered_rows]
    values = [row["hr_mean_bpm"] for row in ordered_rows]
    colors = [
        "#2F6C8F" if row["ecg_quality_flag"] == "pass" else "#B33A3A"
        for row in ordered_rows
    ]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, values, color=colors)
    ax.axhline(40, color="#555555", linestyle="--", linewidth=1, label="40 bpm")
    ax.axhline(100, color="#555555", linestyle="--", linewidth=1, label="100 bpm")
    ax.set_title("Mean Heart Rate by Subject")
    ax.set_ylabel("Mean HR (bpm)")
    ax.set_xlabel("Subject")
    ax.tick_params(axis="x", rotation=60)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper right")
    fig.tight_layout()

    out_path = fig_dir / "ecg_mean_hr_per_subject.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _plot_hr_baseline_vs_task(subject_rows: list[dict[str, Any]], fig_dir: Path) -> Path:
    fig_dir.mkdir(parents=True, exist_ok=True)
    ordered_rows = _subject_rows_in_order(
        subject_rows,
        predicate=lambda row: row["baseline_hr_mean_bpm"] is not None
        and row["task_hr_mean_bpm"] is not None,
    )
    labels = [row["participant_id"] for row in ordered_rows]
    baseline = [row["baseline_hr_mean_bpm"] for row in ordered_rows]
    task = [row["task_hr_mean_bpm"] for row in ordered_rows]

    x = np.arange(len(labels))
    width = 0.42
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.bar(x - width / 2, baseline, width, label="Baseline minute", color="#5B7DB1")
    ax.bar(x + width / 2, task, width, label="Task window", color="#B15B5B")
    ax.set_title("Baseline vs Task Mean Heart Rate by Subject")
    ax.set_ylabel("Mean HR (bpm)")
    ax.set_xlabel("Subject")
    ax.set_xticks(x, labels=labels, rotation=60)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper right")
    fig.tight_layout()

    out_path = fig_dir / "ecg_baseline_vs_task_hr_per_subject.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def _plot_modality_coverage(subject_rows: list[dict[str, Any]], fig_dir: Path) -> Path:
    fig_dir.mkdir(parents=True, exist_ok=True)
    ordered_rows = _subject_rows_in_order(subject_rows)
    labels = [row["participant_id"] for row in ordered_rows]
    matrix = [
        [1 if row["has_eeg"] else 0 for row in ordered_rows],
        [1 if row["has_ecg"] else 0 for row in ordered_rows],
        [1 if row["has_pupil"] else 0 for row in ordered_rows],
    ]

    fig, ax = plt.subplots(figsize=(10, 3))
    im = ax.imshow(matrix, aspect="auto", cmap="Greens", vmin=0, vmax=1)
    ax.set_title("Modality Coverage by Subject")
    ax.set_yticks([0, 1, 2], labels=["EEG", "ECG", "Pupil"])
    ax.set_xticks(range(len(labels)), labels=labels, rotation=60)
    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Present (1) / Missing (0)")
    fig.tight_layout()

    out_path = fig_dir / "modality_coverage_heatmap.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Stage 1 QC summary for arithmetic BIDS data. "
            "Builds per-subject QC table, dataset summary JSON, and quick QC figures."
        )
    )
    parser.add_argument("--bids-root", required=True, help="Path to BIDS root.")
    parser.add_argument(
        "--task",
        default=None,
        help="Task name. Defaults to inferring from BIDS root name.",
    )
    parser.add_argument(
        "--trial-table",
        default=None,
        help=(
            "Path to trial table TSV. Defaults to "
            "analysis_pipeline/reports/trial_table_<bids_root_name>.tsv."
        ),
    )
    parser.add_argument(
        "--out-subject-table",
        default=None,
        help="Output subject-level QC TSV. Default: analysis_pipeline/reports/qc_subject_table.tsv",
    )
    parser.add_argument(
        "--out-summary-json",
        default=None,
        help="Output dataset QC summary JSON. Default: analysis_pipeline/reports/qc_dataset_summary.json",
    )
    parser.add_argument(
        "--participant-bids-sample-drop-summary-csv",
        default=None,
        help=(
            "Output compact per-participant raw-BIDS sample/drop summary CSV. "
            "Default: analysis_pipeline/reports/participant_bids_sample_drop_summary.csv"
        ),
    )
    parser.add_argument(
        "--fig-dir",
        default=None,
        help="Output directory for quick QC figures. Default: analysis_pipeline/reports/figures",
    )
    parser.add_argument(
        "--max-dropped-samples-main-trial-mean",
        type=float,
        default=None,
        help=(
            "Optional Stage 1 EEG dropped-sample proxy threshold: "
            "flag anomaly when subject mean dropped_samples_trial across main trials exceeds this value."
        ),
    )
    parser.add_argument(
        "--max-dropped-samples-main-trial-p95",
        type=float,
        default=None,
        help=(
            "Optional Stage 1 EEG dropped-sample proxy threshold: "
            "flag anomaly when subject p95 dropped_samples_trial across main trials exceeds this value."
        ),
    )
    parser.add_argument(
        "--max-dropped-samples-main-trial-mean-ecg",
        type=float,
        default=None,
        help=(
            "Optional Stage 1 ECG dropped-sample proxy threshold: "
            "flag anomaly when subject mean dropped_samples_trial across main trials exceeds this value."
        ),
    )
    parser.add_argument(
        "--max-dropped-samples-main-trial-p95-ecg",
        type=float,
        default=None,
        help=(
            "Optional Stage 1 ECG dropped-sample proxy threshold: "
            "flag anomaly when subject p95 dropped_samples_trial across main trials exceeds this value."
        ),
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Mark subjects with any QC anomalies as rejected in outputs and continue so "
            "downstream stages can analyze only the carried-forward set."
        ),
    )
    args = parser.parse_args()

    bids_root = _resolve_bids_root(args.bids_root)
    if not bids_root.exists():
        raise FileNotFoundError(bids_root)
    task = args.task or _task_from_bids_root(bids_root)
    if (
        args.max_dropped_samples_main_trial_mean is not None
        and args.max_dropped_samples_main_trial_mean < 0
    ):
        raise ValueError("--max-dropped-samples-main-trial-mean must be >= 0.")
    if (
        args.max_dropped_samples_main_trial_p95 is not None
        and args.max_dropped_samples_main_trial_p95 < 0
    ):
        raise ValueError("--max-dropped-samples-main-trial-p95 must be >= 0.")
    if (
        args.max_dropped_samples_main_trial_mean_ecg is not None
        and args.max_dropped_samples_main_trial_mean_ecg < 0
    ):
        raise ValueError("--max-dropped-samples-main-trial-mean-ecg must be >= 0.")
    if (
        args.max_dropped_samples_main_trial_p95_ecg is not None
        and args.max_dropped_samples_main_trial_p95_ecg < 0
    ):
        raise ValueError("--max-dropped-samples-main-trial-p95-ecg must be >= 0.")

    reports_dir = _reports_dir()
    subject_table_path = (
        Path(args.out_subject_table).resolve()
        if args.out_subject_table
        else reports_dir / "qc_subject_table.tsv"
    )
    summary_json_path = (
        Path(args.out_summary_json).resolve()
        if args.out_summary_json
        else reports_dir / "qc_dataset_summary.json"
    )
    participant_bids_sample_drop_summary_csv_path = (
        Path(args.participant_bids_sample_drop_summary_csv).resolve()
        if args.participant_bids_sample_drop_summary_csv
        else _default_participant_bids_sample_drop_summary_csv_path()
    )
    fig_dir = (
        Path(args.fig_dir).resolve() if args.fig_dir else reports_dir / "figures"
    )
    trial_table_path = (
        Path(args.trial_table).resolve()
        if args.trial_table
        else _default_trial_table_path(bids_root)
    )

    participants = _read_participants(bids_root / "participants.tsv")
    trial_rows = _read_trial_table(trial_table_path)
    trials_by_subject: dict[str, list[dict[str, str]]] = {}
    for row in trial_rows:
        subject = (row.get("participant_id") or "").strip()
        if not subject:
            continue
        trials_by_subject.setdefault(subject, []).append(row)

    subject_dirs = sorted(path for path in bids_root.glob("sub-*") if path.is_dir())
    if not subject_dirs:
        raise FileNotFoundError(f"No subject directories found in {bids_root}")
    print(
        f"Stage 1 starting. task={task} subjects={len(subject_dirs)} "
        f"trial_rows={len(trial_rows)}"
    )

    subject_rows: list[dict[str, Any]] = []
    all_anomalies: list[str] = []
    for subject_idx, subject_dir in enumerate(subject_dirs, start=1):
        paths = _resolve_subject_paths(subject_dir, task)
        subject = paths.subject
        print(f"[Subject {subject_idx}/{len(subject_dirs)}] {subject}")
        analysis_included = (
            (participants.get(subject, {}).get("analysis_included") or "n/a").strip().lower()
        )
        if analysis_included not in ("true", "false"):
            analysis_included = "n/a"

        has_events = paths.events_tsv.exists()
        has_eeg_recording = paths.eeg_vhdr.exists()
        has_ecg_sidecar = paths.ecg_json.exists()
        has_pupil_sidecar = paths.pupil_json.exists()
        has_eeg = has_eeg_recording and has_events
        has_ecg = paths.ecg_tsv.exists()
        has_pupil = paths.pupil_tsv.exists() and has_pupil_sidecar

        events_summary = _read_events_summary(paths.events_tsv)
        marker_onsets = _read_marker_onsets(paths.events_tsv)
        events_rows = _count_table_rows(paths.events_tsv)
        ecg_quality, hr_times, hr_values = _summarize_ecg_quality(paths.ecg_tsv, paths.ecg_json)
        eeg_summary = _summarize_eeg_recording(paths)
        pupil_quality = _summarize_pupil_quality(paths.pupil_tsv, paths.pupil_json)
        subject_trials = trials_by_subject.get(subject, [])

        main_trial_rows = [row for row in subject_trials if row.get("block") == "main"]
        tutorial_trial_rows = [row for row in subject_trials if row.get("block") == "tutorial"]
        dropped_main = [
            _as_float(row.get("dropped_samples_trial"))
            for row in main_trial_rows
            if _as_float(row.get("dropped_samples_trial")) is not None
        ]
        dropped_main_mean = mean(dropped_main) if dropped_main else None
        dropped_main_p95 = _percentile(dropped_main, 0.95)
        rt_main = [
            _as_float(row.get("response_time_s"))
            for row in main_trial_rows
            if _as_float(row.get("response_time_s")) is not None
        ]

        baseline_start_s = (
            marker_onsets["started_tutorial_artihmetic"][0]
            if marker_onsets["started_tutorial_artihmetic"]
            else None
        )
        baseline_end_s = baseline_start_s + 60.0 if baseline_start_s is not None else None

        task_start_candidates = [
            _as_float(row.get("calc_start_s"))
            for row in main_trial_rows
            if _as_float(row.get("calc_start_s")) is not None
        ]
        task_end_candidates = [
            _as_float(row.get("answer_end_s"))
            for row in main_trial_rows
            if _as_float(row.get("answer_end_s")) is not None
        ]
        if task_start_candidates and task_end_candidates:
            task_start_s = min(task_start_candidates)
            task_end_s = max(task_end_candidates)
        else:
            starts = marker_onsets["started_arithmetic"]
            ends = marker_onsets["finished_arithmetic"]
            task_start_s = starts[0] if starts else None
            task_end_s = ends[0] if ends else None

        baseline_hr = _window_hr_stats(hr_times, hr_values, baseline_start_s, baseline_end_s)
        task_hr = _window_hr_stats(hr_times, hr_values, task_start_s, task_end_s)
        hr_delta = None
        if baseline_hr["mean_bpm"] is not None and task_hr["mean_bpm"] is not None:
            hr_delta = float(task_hr["mean_bpm"] - baseline_hr["mean_bpm"])

        global_qc_reasons: list[str] = []
        eeg_qc_reasons_local: list[str] = []
        ecg_qc_reasons_local: list[str] = []
        pupil_qc_reasons_local: list[str] = []

        if not has_events:
            global_qc_reasons.append("Missing events TSV.")
        if not has_eeg_recording:
            eeg_qc_reasons_local.append("Missing EEG recording file.")
        if not has_ecg or not has_ecg_sidecar:
            ecg_qc_reasons_local.append("Missing ECG physio TSV/JSON.")
        elif ecg_quality["ecg_quality_flag"] in ("warn", "fail"):
            ecg_qc_reasons_local.append(
                f"ECG {ecg_quality['ecg_quality_flag']}: {ecg_quality['ecg_quality_note']}"
            )
        if not has_pupil or not has_pupil_sidecar:
            pupil_qc_reasons_local.append("Missing pupil TSV/JSON.")

        if len(subject_trials) != 70:
            global_qc_reasons.append(f"Expected 70 trial rows, got {len(subject_trials)}.")
        if len(main_trial_rows) != 63:
            global_qc_reasons.append(f"Expected 63 main trial rows, got {len(main_trial_rows)}.")
        if len(tutorial_trial_rows) != 7:
            global_qc_reasons.append(f"Expected 7 tutorial trial rows, got {len(tutorial_trial_rows)}.")

        if events_summary["cue_markers"] != 70:
            global_qc_reasons.append(f"Expected 70 cue markers, got {events_summary['cue_markers']}.")
        if events_summary["outcome_markers"] != 70:
            global_qc_reasons.append(f"Expected 70 outcome markers, got {events_summary['outcome_markers']}.")
        if events_summary["started_arithmetic_markers"] != 1:
            global_qc_reasons.append(
                "Unexpected started_arithmetic marker count: "
                f"{events_summary['started_arithmetic_markers']}."
            )
        if events_summary["finished_arithmetic_markers"] != 1:
            global_qc_reasons.append(
                "Unexpected finished_arithmetic marker count: "
                f"{events_summary['finished_arithmetic_markers']}."
            )

        if pupil_quality["pupil_mean_confidence"] is not None and pupil_quality["pupil_mean_confidence"] < 0.6:
            pupil_qc_reasons_local.append(
                f"Low pupil mean confidence ({pupil_quality['pupil_mean_confidence']:.3f})."
            )
        dropped_mean_exceeds_eeg = False
        dropped_p95_exceeds_eeg = False
        dropped_mean_exceeds_ecg = False
        dropped_p95_exceeds_ecg = False
        if args.max_dropped_samples_main_trial_mean is not None:
            if dropped_main_mean is None:
                eeg_qc_reasons_local.append(
                    "No dropped_samples_trial values available for mean-threshold EEG dropped-sample check."
                )
            elif dropped_main_mean > args.max_dropped_samples_main_trial_mean:
                dropped_mean_exceeds_eeg = True
                eeg_qc_reasons_local.append(
                    "High mean dropped samples in main trials "
                    f"({dropped_main_mean:.3f} > {args.max_dropped_samples_main_trial_mean:.3f})."
                )
        if args.max_dropped_samples_main_trial_p95 is not None:
            if dropped_main_p95 is None:
                eeg_qc_reasons_local.append(
                    "No dropped_samples_trial values available for p95-threshold EEG dropped-sample check."
                )
            elif dropped_main_p95 > args.max_dropped_samples_main_trial_p95:
                dropped_p95_exceeds_eeg = True
                eeg_qc_reasons_local.append(
                    "High p95 dropped samples in main trials "
                    f"({dropped_main_p95:.3f} > {args.max_dropped_samples_main_trial_p95:.3f})."
                )
        if args.max_dropped_samples_main_trial_mean_ecg is not None:
            if dropped_main_mean is None:
                ecg_qc_reasons_local.append(
                    "No dropped_samples_trial values available for mean-threshold ECG dropped-sample check."
                )
            elif dropped_main_mean > args.max_dropped_samples_main_trial_mean_ecg:
                dropped_mean_exceeds_ecg = True
                ecg_qc_reasons_local.append(
                    "High mean dropped samples in main trials for ECG "
                    f"({dropped_main_mean:.3f} > {args.max_dropped_samples_main_trial_mean_ecg:.3f})."
                )
        if args.max_dropped_samples_main_trial_p95_ecg is not None:
            if dropped_main_p95 is None:
                ecg_qc_reasons_local.append(
                    "No dropped_samples_trial values available for p95-threshold ECG dropped-sample check."
                )
            elif dropped_main_p95 > args.max_dropped_samples_main_trial_p95_ecg:
                dropped_p95_exceeds_ecg = True
                ecg_qc_reasons_local.append(
                    "High p95 dropped samples in main trials for ECG "
                    f"({dropped_main_p95:.3f} > {args.max_dropped_samples_main_trial_p95_ecg:.3f})."
                )

        eeg_qc_reasons = _ordered_unique(global_qc_reasons + eeg_qc_reasons_local)
        ecg_qc_reasons = _ordered_unique(global_qc_reasons + ecg_qc_reasons_local)
        pupil_qc_reasons = _ordered_unique(global_qc_reasons + pupil_qc_reasons_local)
        anomalies = _ordered_unique(
            global_qc_reasons + eeg_qc_reasons_local + ecg_qc_reasons_local + pupil_qc_reasons_local
        )

        qc_flagged = bool(anomalies)
        qc_rejected_eeg = bool(args.strict and eeg_qc_reasons and analysis_included != "false")
        qc_rejected_ecg = bool(args.strict and ecg_qc_reasons and analysis_included != "false")
        qc_rejected_pupil = bool(args.strict and pupil_qc_reasons and analysis_included != "false")
        qc_rejected_any_modality = bool(
            qc_rejected_eeg or qc_rejected_ecg or qc_rejected_pupil
        )
        qc_rejected_all_modalities = bool(
            qc_rejected_eeg and qc_rejected_ecg and qc_rejected_pupil
        )
        qc_rejected = qc_rejected_all_modalities

        analysis_included_effective_eeg = _effective_inclusion_flag(
            analysis_included, qc_rejected_eeg
        )
        analysis_included_effective_ecg = _effective_inclusion_flag(
            analysis_included, qc_rejected_ecg
        )
        analysis_included_effective_pupil = _effective_inclusion_flag(
            analysis_included, qc_rejected_pupil
        )
        if analysis_included == "false":
            analysis_included_effective = "false"
        elif (
            analysis_included_effective_eeg == "true"
            or analysis_included_effective_ecg == "true"
            or analysis_included_effective_pupil == "true"
        ):
            analysis_included_effective = "true"
        else:
            analysis_included_effective = "false"

        subject_row: dict[str, Any] = {
            "participant_id": subject,
            "analysis_included": analysis_included,
            "analysis_included_effective": analysis_included_effective,
            "analysis_included_effective_eeg": analysis_included_effective_eeg,
            "analysis_included_effective_ecg": analysis_included_effective_ecg,
            "analysis_included_effective_pupil": analysis_included_effective_pupil,
            "has_eeg": has_eeg,
            "has_ecg": has_ecg,
            "has_pupil": has_pupil,
            "eeg_samples": int(eeg_summary["eeg_samples"] or 0),
            "eeg_sampling_frequency_hz": eeg_summary["eeg_sampling_frequency_hz"],
            "eeg_duration_s": eeg_summary["eeg_duration_s"],
            "ecg_samples": int(ecg_quality["ecg_samples"] or 0),
            "ecg_sampling_frequency_hz": ecg_quality["ecg_sampling_frequency_hz"],
            "ecg_duration_s": ecg_quality["ecg_duration_s"],
            "ecg_signal_std": ecg_quality["ecg_signal_std"],
            "ecg_signal_p1_p99_range": ecg_quality["ecg_signal_p1_p99_range"],
            "ecg_detected_beats": ecg_quality["ecg_detected_beats"],
            "hr_mean_bpm": ecg_quality["hr_mean_bpm"],
            "hr_median_bpm": ecg_quality["hr_median_bpm"],
            "hr_p05_bpm": ecg_quality["hr_p05_bpm"],
            "hr_p95_bpm": ecg_quality["hr_p95_bpm"],
            "hr_out_of_range_pct": ecg_quality["hr_out_of_range_pct"],
            "hr_valid_ratio": ecg_quality["hr_valid_ratio"],
            "ecg_quality_flag": str(ecg_quality["ecg_quality_flag"]),
            "ecg_quality_note": str(ecg_quality["ecg_quality_note"]),
            "baseline_window_start_s": baseline_hr["start_s"],
            "baseline_window_end_s": baseline_hr["end_s"],
            "baseline_hr_n_rr": baseline_hr["n_rr"],
            "baseline_hr_mean_bpm": baseline_hr["mean_bpm"],
            "baseline_hr_median_bpm": baseline_hr["median_bpm"],
            "baseline_hr_p05_bpm": baseline_hr["p05_bpm"],
            "baseline_hr_p95_bpm": baseline_hr["p95_bpm"],
            "task_window_start_s": task_hr["start_s"],
            "task_window_end_s": task_hr["end_s"],
            "task_hr_n_rr": task_hr["n_rr"],
            "task_hr_mean_bpm": task_hr["mean_bpm"],
            "task_hr_median_bpm": task_hr["median_bpm"],
            "task_hr_p05_bpm": task_hr["p05_bpm"],
            "task_hr_p95_bpm": task_hr["p95_bpm"],
            "task_minus_baseline_hr_mean_bpm": hr_delta,
            "pupil_samples": int(pupil_quality["pupil_samples"] or 0),
            "events_rows": events_rows,
            "trial_rows_total": len(subject_trials),
            "trial_rows_main": len(main_trial_rows),
            "trial_rows_tutorial": len(tutorial_trial_rows),
            "event_cue_markers": events_summary["cue_markers"],
            "event_outcome_markers": events_summary["outcome_markers"],
            "started_arithmetic_markers": events_summary["started_arithmetic_markers"],
            "finished_arithmetic_markers": events_summary["finished_arithmetic_markers"],
            "dropped_samples_total_events": events_summary["dropped_samples_total"],
            "dropped_samples_main_trials": int(sum(dropped_main)) if dropped_main else 0,
            "dropped_samples_main_trials_per_trial_mean": dropped_main_mean,
            "dropped_samples_main_trials_per_trial_p95": dropped_main_p95,
            "dropped_samples_main_trials_mean_threshold": args.max_dropped_samples_main_trial_mean,
            "dropped_samples_main_trials_p95_threshold": args.max_dropped_samples_main_trial_p95,
            "dropped_samples_main_trials_mean_exceeds_threshold": dropped_mean_exceeds_eeg,
            "dropped_samples_main_trials_p95_exceeds_threshold": dropped_p95_exceeds_eeg,
            "dropped_samples_main_trials_mean_threshold_eeg": args.max_dropped_samples_main_trial_mean,
            "dropped_samples_main_trials_p95_threshold_eeg": args.max_dropped_samples_main_trial_p95,
            "dropped_samples_main_trials_mean_exceeds_threshold_eeg": dropped_mean_exceeds_eeg,
            "dropped_samples_main_trials_p95_exceeds_threshold_eeg": dropped_p95_exceeds_eeg,
            "dropped_samples_main_trials_mean_threshold_ecg": args.max_dropped_samples_main_trial_mean_ecg,
            "dropped_samples_main_trials_p95_threshold_ecg": args.max_dropped_samples_main_trial_p95_ecg,
            "dropped_samples_main_trials_mean_exceeds_threshold_ecg": dropped_mean_exceeds_ecg,
            "dropped_samples_main_trials_p95_exceeds_threshold_ecg": dropped_p95_exceeds_ecg,
            "response_time_main_mean_s": mean(rt_main) if rt_main else None,
            "response_time_main_median_s": median(rt_main) if rt_main else None,
            "response_time_main_p95_s": _percentile(rt_main, 0.95),
            "pupil_mean_confidence": pupil_quality["pupil_mean_confidence"],
            "pupil_pct_conf_lt_0_8": pupil_quality["pupil_pct_conf_lt_0_8"],
            "pupil_pct_conf_lt_0_6": pupil_quality["pupil_pct_conf_lt_0_6"],
            "pupil_pct_missing_confidence": pupil_quality["pupil_pct_missing_confidence"],
            "pupil_pct_nonpositive_size": pupil_quality["pupil_pct_nonpositive_size"],
            "qc_flagged": qc_flagged,
            "qc_rejected": qc_rejected,
            "qc_rejected_any_modality": qc_rejected_any_modality,
            "qc_rejected_all_modalities": qc_rejected_all_modalities,
            "qc_rejected_eeg": qc_rejected_eeg,
            "qc_rejected_ecg": qc_rejected_ecg,
            "qc_rejected_pupil": qc_rejected_pupil,
            "qc_reason_count": len(anomalies),
            "qc_rejection_reasons": list(anomalies),
            "qc_reason_count_eeg": len(eeg_qc_reasons),
            "qc_reason_count_ecg": len(ecg_qc_reasons),
            "qc_reason_count_pupil": len(pupil_qc_reasons),
            "qc_rejection_reasons_eeg": list(eeg_qc_reasons),
            "qc_rejection_reasons_ecg": list(ecg_qc_reasons),
            "qc_rejection_reasons_pupil": list(pupil_qc_reasons),
            "anomalies": anomalies,
        }
        subject_rows.append(subject_row)
        for anomaly in anomalies:
            all_anomalies.append(f"{subject}: {anomaly}")

    subject_rows.sort(key=lambda row: row["participant_id"])
    subject_table_rows = _subject_rows_to_table_rows(subject_rows)
    _write_tsv(subject_table_path, subject_table_rows)
    participant_bids_sample_drop_summary_rows = _subject_rows_to_bids_sample_drop_summary_rows(
        subject_rows
    )
    _write_csv(
        participant_bids_sample_drop_summary_csv_path,
        participant_bids_sample_drop_summary_rows,
    )

    included_rows = [row for row in subject_rows if row["analysis_included"] == "true"]
    carried_forward_rows = [
        row for row in subject_rows if row["analysis_included_effective"] == "true"
    ]
    flagged_rows = [row for row in subject_rows if row["qc_flagged"]]
    rejected_rows = [row for row in subject_rows if row["qc_rejected"]]
    rejected_rows_any_modality = [
        row for row in subject_rows if row["qc_rejected_any_modality"]
    ]
    carried_forward_rows_by_modality = {
        "eeg": [
            row for row in subject_rows if row["analysis_included_effective_eeg"] == "true"
        ],
        "ecg": [
            row for row in subject_rows if row["analysis_included_effective_ecg"] == "true"
        ],
        "pupil": [
            row for row in subject_rows if row["analysis_included_effective_pupil"] == "true"
        ],
    }
    rejected_rows_by_modality = {
        "eeg": [row for row in subject_rows if row["qc_rejected_eeg"]],
        "ecg": [row for row in subject_rows if row["qc_rejected_ecg"]],
        "pupil": [row for row in subject_rows if row["qc_rejected_pupil"]],
    }
    modality_coverage = {
        "n_subjects": len(subject_rows),
        "n_with_eeg": sum(1 for row in subject_rows if row["has_eeg"]),
        "n_with_ecg": sum(1 for row in subject_rows if row["has_ecg"]),
        "n_with_pupil": sum(1 for row in subject_rows if row["has_pupil"]),
        "n_with_all_modalities": sum(
            1 for row in subject_rows if row["has_eeg"] and row["has_ecg"] and row["has_pupil"]
        ),
    }

    dropped_main_all = [
        row["dropped_samples_main_trials_per_trial_mean"]
        for row in subject_rows
        if row["dropped_samples_main_trials_per_trial_mean"] is not None
    ]
    pupil_conf_all = [
        row["pupil_mean_confidence"]
        for row in subject_rows
        if row["pupil_mean_confidence"] is not None
    ]
    hr_mean_all = [
        row["hr_mean_bpm"]
        for row in subject_rows
        if row["hr_mean_bpm"] is not None
    ]
    baseline_hr_all = [
        row["baseline_hr_mean_bpm"]
        for row in subject_rows
        if row["baseline_hr_mean_bpm"] is not None
    ]
    task_hr_all = [
        row["task_hr_mean_bpm"]
        for row in subject_rows
        if row["task_hr_mean_bpm"] is not None
    ]
    delta_hr_all = [
        row["task_minus_baseline_hr_mean_bpm"]
        for row in subject_rows
        if row["task_minus_baseline_hr_mean_bpm"] is not None
    ]

    figure_paths = {
        "dropped_samples_main_per_subject": str(_plot_dropped_samples(subject_rows, fig_dir)),
        "dropped_samples_flagged_subjects_eeg_ecg": str(
            _plot_dropped_sample_flags_by_modality(subject_rows, fig_dir)
        ),
        "pupil_mean_confidence_per_subject": str(_plot_pupil_confidence(subject_rows, fig_dir)),
        "ecg_mean_hr_per_subject": str(_plot_hr_mean(subject_rows, fig_dir)),
        "ecg_baseline_vs_task_hr_per_subject": str(_plot_hr_baseline_vs_task(subject_rows, fig_dir)),
        "modality_coverage_heatmap": str(_plot_modality_coverage(subject_rows, fig_dir)),
    }

    summary: dict[str, Any] = {
        "bids_root": str(bids_root),
        "task": task,
        "trial_table_path": str(trial_table_path),
        "subject_table_path": str(subject_table_path),
        "participant_bids_sample_drop_summary_csv": str(
            participant_bids_sample_drop_summary_csv_path
        ),
        "fig_dir": str(fig_dir),
        "strict_mode": bool(args.strict),
        "qc_decision_policy": "modality_reject_continue" if args.strict else "flag_only",
        "modality_coverage": modality_coverage,
        "analysis_included_subjects": len(included_rows),
        "analysis_included_subjects_after_qc": len(carried_forward_rows),
        "analysis_included_subjects_after_qc_by_modality": {
            modality: len(rows)
            for modality, rows in carried_forward_rows_by_modality.items()
        },
        "subjects_flagged_by_any_qc_anomaly": [row["participant_id"] for row in flagged_rows],
        "subjects_rejected_after_qc": [row["participant_id"] for row in rejected_rows],
        "subjects_rejected_after_qc_any_modality": [
            row["participant_id"] for row in rejected_rows_any_modality
        ],
        "subjects_rejected_after_qc_all_modalities": [
            row["participant_id"] for row in rejected_rows
        ],
        "subjects_rejected_after_qc_by_modality": {
            modality: [row["participant_id"] for row in rows]
            for modality, rows in rejected_rows_by_modality.items()
        },
        "subjects_carried_forward_after_qc": [
            row["participant_id"] for row in carried_forward_rows
        ],
        "subjects_carried_forward_after_qc_by_modality": {
            modality: [row["participant_id"] for row in rows]
            for modality, rows in carried_forward_rows_by_modality.items()
        },
        "qc_reasons_by_subject": {
            row["participant_id"]: list(row["qc_rejection_reasons"])
            for row in subject_rows
            if row["qc_rejection_reasons"]
        },
        "rejection_reasons_by_subject": {
            row["participant_id"]: list(row["qc_rejection_reasons"])
            for row in rejected_rows
        },
        "rejection_reasons_by_subject_any_modality": {
            row["participant_id"]: list(row["qc_rejection_reasons"])
            for row in rejected_rows_any_modality
        },
        "rejection_reasons_by_subject_by_modality": {
            "eeg": {
                row["participant_id"]: list(row["qc_rejection_reasons_eeg"])
                for row in rejected_rows_by_modality["eeg"]
            },
            "ecg": {
                row["participant_id"]: list(row["qc_rejection_reasons_ecg"])
                for row in rejected_rows_by_modality["ecg"]
            },
            "pupil": {
                row["participant_id"]: list(row["qc_rejection_reasons_pupil"])
                for row in rejected_rows_by_modality["pupil"]
            },
        },
        "trial_rows_total": len(trial_rows),
        "trial_rows_main": sum(1 for row in trial_rows if row.get("block") == "main"),
        "trial_rows_tutorial": sum(1 for row in trial_rows if row.get("block") == "tutorial"),
        "dropped_samples_main_per_trial_mean_distribution": {
            "mean": mean(dropped_main_all) if dropped_main_all else None,
            "median": median(dropped_main_all) if dropped_main_all else None,
            "p95": _percentile(dropped_main_all, 0.95),
        },
        "eeg_dropped_samples_thresholds": {
            "max_dropped_samples_main_trial_mean": args.max_dropped_samples_main_trial_mean,
            "max_dropped_samples_main_trial_p95": args.max_dropped_samples_main_trial_p95,
        },
        "ecg_dropped_samples_thresholds": {
            "max_dropped_samples_main_trial_mean": args.max_dropped_samples_main_trial_mean_ecg,
            "max_dropped_samples_main_trial_p95": args.max_dropped_samples_main_trial_p95_ecg,
        },
        "subjects_exceeding_eeg_dropped_samples_main_trial_mean_threshold": [
            row["participant_id"]
            for row in subject_rows
            if row["dropped_samples_main_trials_mean_exceeds_threshold_eeg"]
        ],
        "subjects_exceeding_eeg_dropped_samples_main_trial_p95_threshold": [
            row["participant_id"]
            for row in subject_rows
            if row["dropped_samples_main_trials_p95_exceeds_threshold_eeg"]
        ],
        "subjects_exceeding_ecg_dropped_samples_main_trial_mean_threshold": [
            row["participant_id"]
            for row in subject_rows
            if row["dropped_samples_main_trials_mean_exceeds_threshold_ecg"]
        ],
        "subjects_exceeding_ecg_dropped_samples_main_trial_p95_threshold": [
            row["participant_id"]
            for row in subject_rows
            if row["dropped_samples_main_trials_p95_exceeds_threshold_ecg"]
        ],
        "subjects_flagged_by_dropped_samples_thresholds": {
            "eeg": [
                row["participant_id"]
                for row in subject_rows
                if row["dropped_samples_main_trials_mean_exceeds_threshold_eeg"]
                or row["dropped_samples_main_trials_p95_exceeds_threshold_eeg"]
            ],
            "ecg": [
                row["participant_id"]
                for row in subject_rows
                if row["dropped_samples_main_trials_mean_exceeds_threshold_ecg"]
                or row["dropped_samples_main_trials_p95_exceeds_threshold_ecg"]
            ],
        },
        "pupil_mean_confidence_distribution": {
            "mean": mean(pupil_conf_all) if pupil_conf_all else None,
            "median": median(pupil_conf_all) if pupil_conf_all else None,
            "p10": _percentile(pupil_conf_all, 0.10),
        },
        "ecg_hr_mean_distribution_bpm": {
            "mean": mean(hr_mean_all) if hr_mean_all else None,
            "median": median(hr_mean_all) if hr_mean_all else None,
            "p05": _percentile(hr_mean_all, 0.05),
            "p95": _percentile(hr_mean_all, 0.95),
        },
        "ecg_baseline_hr_mean_distribution_bpm": {
            "mean": mean(baseline_hr_all) if baseline_hr_all else None,
            "median": median(baseline_hr_all) if baseline_hr_all else None,
            "p05": _percentile(baseline_hr_all, 0.05),
            "p95": _percentile(baseline_hr_all, 0.95),
        },
        "ecg_task_hr_mean_distribution_bpm": {
            "mean": mean(task_hr_all) if task_hr_all else None,
            "median": median(task_hr_all) if task_hr_all else None,
            "p05": _percentile(task_hr_all, 0.05),
            "p95": _percentile(task_hr_all, 0.95),
        },
        "ecg_task_minus_baseline_hr_mean_distribution_bpm": {
            "mean": mean(delta_hr_all) if delta_hr_all else None,
            "median": median(delta_hr_all) if delta_hr_all else None,
            "p05": _percentile(delta_hr_all, 0.05),
            "p95": _percentile(delta_hr_all, 0.95),
        },
        "subjects_with_ecg_quality_fail": [
            row["participant_id"]
            for row in subject_rows
            if row["ecg_quality_flag"] == "fail"
        ],
        "subjects_with_ecg_quality_warn": [
            row["participant_id"]
            for row in subject_rows
            if row["ecg_quality_flag"] == "warn"
        ],
        "subjects_with_low_pupil_confidence_lt_0_6": [
            row["participant_id"]
            for row in subject_rows
            if row["pupil_mean_confidence"] is not None and row["pupil_mean_confidence"] < 0.6
        ],
        "anomaly_count": len(all_anomalies),
        "anomalies": all_anomalies,
        "figure_paths": figure_paths,
    }
    summary_json_path.parent.mkdir(parents=True, exist_ok=True)
    summary_json_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote subject QC table: {subject_table_path}")
    print(f"Wrote dataset QC summary: {summary_json_path}")
    print(f"Wrote figures under: {fig_dir}")
    print(f"Subjects processed: {len(subject_rows)}")
    print(f"Anomalies: {len(all_anomalies)}")
    print(
        "Stage 1 QC decision summary: "
        f"flagged={len(flagged_rows)} "
        f"rejected_any={len(rejected_rows_any_modality)} "
        f"rejected_all={len(rejected_rows)} "
        f"carried_forward_union={len(carried_forward_rows)} "
        f"carried_forward_eeg={len(carried_forward_rows_by_modality['eeg'])} "
        f"carried_forward_ecg={len(carried_forward_rows_by_modality['ecg'])} "
        f"carried_forward_pupil={len(carried_forward_rows_by_modality['pupil'])}"
    )
    if all_anomalies:
        for line in all_anomalies:
            print(f"  - {line}")
    if args.strict and rejected_rows_any_modality:
        rejected_ids = ", ".join(row["participant_id"] for row in rejected_rows_any_modality)
        print(
            "Strict Stage 1 QC mode marked modality-specific subject rejections and expects "
            "downstream stages to continue with the carried-forward union: "
            f"{rejected_ids}"
        )


if __name__ == "__main__":
    main()
