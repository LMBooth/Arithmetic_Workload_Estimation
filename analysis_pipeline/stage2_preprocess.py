from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any

import mne
import numpy as np
from mne.preprocessing import ICA
from scipy import signal as sp_signal


@dataclass(frozen=True)
class SubjectPaths:
    subject: str
    eeg_vhdr: Path
    eeg_events: Path
    channels_tsv: Path
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


def _format_float(value: float | None, decimals: int = 6) -> str:
    if value is None:
        return "n/a"
    return f"{value:.{decimals}f}"


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


def _analysis_root() -> Path:
    return Path(__file__).resolve().parent


def _reports_dir() -> Path:
    return _analysis_root() / "reports"


def _derivatives_root() -> Path:
    return _analysis_root() / "derivatives" / "cleaned"


def _read_participants(participants_tsv: Path) -> dict[str, dict[str, str]]:
    if not participants_tsv.exists():
        return {}
    out: dict[str, dict[str, str]] = {}
    with participants_tsv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            subject = (row.get("participant_id") or "").strip()
            if subject:
                out[subject] = row
    return out


def _resolve_subject_paths(subject_dir: Path, task: str) -> SubjectPaths:
    subject = subject_dir.name
    return SubjectPaths(
        subject=subject,
        eeg_vhdr=subject_dir / "eeg" / f"{subject}_task-{task}_eeg.vhdr",
        eeg_events=subject_dir / "eeg" / f"{subject}_task-{task}_events.tsv",
        channels_tsv=subject_dir / "eeg" / f"{subject}_task-{task}_channels.tsv",
        ecg_tsv=subject_dir / "ecg" / f"{subject}_task-{task}_recording-ecg_physio.tsv",
        ecg_json=subject_dir / "ecg" / f"{subject}_task-{task}_recording-ecg_physio.json",
        pupil_tsv=subject_dir / "pupil" / f"{subject}_task-{task}_pupil.tsv",
        pupil_json=subject_dir / "pupil" / f"{subject}_task-{task}_eyetrack.json",
    )


def _load_ecg_series(path: Path) -> tuple[np.ndarray, np.ndarray]:
    times: list[float] = []
    values: list[float] = []
    if not path.exists():
        return np.array([], dtype=np.float64), np.array([], dtype=np.float64)
    with _open_text(path) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) < 2:
                continue
            t = _as_float(row[0])
            x = _as_float(row[1])
            if t is None or x is None:
                continue
            times.append(t)
            values.append(x)
    return np.asarray(times, dtype=np.float64), np.asarray(values, dtype=np.float64)


def _infer_sfreq(times: np.ndarray) -> float | None:
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


def _apply_bandpass(values: np.ndarray, sfreq: float, low_hz: float, high_hz: float) -> np.ndarray:
    nyquist = 0.5 * sfreq
    if nyquist <= low_hz:
        return values.copy()
    high_hz = min(high_hz, 0.95 * nyquist)
    low = low_hz / nyquist
    high = high_hz / nyquist
    b, a = sp_signal.butter(2, [low, high], btype="bandpass")
    return sp_signal.filtfilt(b, a, values)


def _evaluate_peaks(times: np.ndarray, peaks: np.ndarray) -> dict[str, float | int | None]:
    rr = np.diff(times[peaks]) if peaks.size > 1 else np.array([], dtype=np.float64)
    rr = rr[np.isfinite(rr) & (rr > 0)]
    if rr.size == 0:
        return {
            "detected_beats": int(peaks.size),
            "hr_mean_bpm": None,
            "hr_median_bpm": None,
            "hr_valid_ratio": None,
        }
    hr = 60.0 / rr
    valid = (hr >= 35.0) & (hr <= 180.0)
    hr_valid = hr[valid]
    if hr_valid.size == 0:
        return {
            "detected_beats": int(peaks.size),
            "hr_mean_bpm": None,
            "hr_median_bpm": None,
            "hr_valid_ratio": 0.0,
        }
    return {
        "detected_beats": int(peaks.size),
        "hr_mean_bpm": float(np.mean(hr_valid)),
        "hr_median_bpm": float(np.median(hr_valid)),
        "hr_valid_ratio": float(hr_valid.size) / float(hr.size),
    }


def _detect_hr_from_filtered_ecg(times: np.ndarray, filtered: np.ndarray, sfreq: float) -> dict[str, float | int | None]:
    distance = max(1, int(round(0.3 * sfreq)))
    mad = np.median(np.abs(filtered - np.median(filtered)))
    robust_scale = 1.4826 * mad if mad > 0 else float(np.std(filtered))
    fallback = float(np.percentile(np.abs(filtered), 75)) * 0.30
    prominence = max(robust_scale * 1.5, fallback, 1e-9)
    peaks_pos, _ = sp_signal.find_peaks(filtered, distance=distance, prominence=prominence)
    peaks_neg, _ = sp_signal.find_peaks(-filtered, distance=distance, prominence=prominence)
    pos = _evaluate_peaks(times, peaks_pos)
    neg = _evaluate_peaks(times, peaks_neg)
    return pos if (pos["detected_beats"] or 0) >= (neg["detected_beats"] or 0) else neg


def _read_ecg_channel_name(channels_tsv: Path) -> str | None:
    if not channels_tsv.exists():
        return None
    with channels_tsv.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            if (row.get("type") or "").strip().upper() == "ECG":
                name = (row.get("name") or "").strip()
                if name:
                    return name
    return None


def _apply_eeg_alias_and_montage(raw_eeg: mne.io.BaseRaw) -> tuple[dict[str, str], bool]:
    alias = {
        "FP1": "Fp1",
        "FP2": "Fp2",
        "T3": "T7",
        "T4": "T8",
        "T5": "P7",
        "T6": "P8",
    }
    rename_map: dict[str, str] = {}
    for old, new in alias.items():
        if old in raw_eeg.ch_names and new not in raw_eeg.ch_names:
            rename_map[old] = new
    if rename_map:
        raw_eeg.rename_channels(rename_map)
    try:
        raw_eeg.set_montage("standard_1020", on_missing="ignore", verbose="ERROR")
        return rename_map, True
    except Exception:
        return rename_map, False


def _detect_bad_eeg_channels(raw_eeg: mne.io.BaseRaw) -> list[str]:
    data_uv = raw_eeg.get_data() * 1e6
    if data_uv.size == 0:
        return []
    std = np.std(data_uv, axis=1)
    med = float(np.median(std))
    mad = float(np.median(np.abs(std - med)))
    scale = 1.4826 * mad if mad > 0 else float(np.std(std))
    z = np.abs((std - med) / (scale + 1e-9))
    bad_hi = np.where(z > 5.0)[0].tolist()
    bad_flat = np.where(std < 0.5)[0].tolist()
    bad_idx = sorted(set(bad_hi + bad_flat))
    return [raw_eeg.ch_names[i] for i in bad_idx]


def _write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_ecg_clean(
    out_tsv: Path,
    times: np.ndarray,
    raw_vals: np.ndarray,
    broad_vals: np.ndarray,
    peak_vals: np.ndarray,
) -> None:
    out_tsv.parent.mkdir(parents=True, exist_ok=True)
    with out_tsv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(["time", "cardiac_raw", "cardiac_broad", "cardiac_peak"])
        for i in range(times.size):
            writer.writerow(
                [
                    f"{times[i]:.6f}",
                    f"{raw_vals[i]:.9f}",
                    f"{broad_vals[i]:.9f}",
                    f"{peak_vals[i]:.9f}",
                ]
            )


def _interp_signal(time: np.ndarray, values: np.ndarray, valid_mask: np.ndarray) -> np.ndarray:
    out = values.copy()
    out[~valid_mask] = np.nan
    valid_idx = np.where(np.isfinite(out))[0]
    if valid_idx.size < 2:
        return np.full_like(values, np.nan, dtype=np.float64)
    return np.interp(time, time[valid_idx], out[valid_idx])


def _smooth_series(values: np.ndarray, window_samples: int) -> np.ndarray:
    if window_samples <= 1:
        return values
    kernel = np.ones(window_samples, dtype=np.float64) / float(window_samples)
    return np.convolve(values, kernel, mode="same")


def _load_pupil_matrix(pupil_tsv: Path, pupil_json: Path) -> tuple[np.ndarray, dict[str, np.ndarray], dict[str, Any]]:
    sidecar = json.loads(pupil_json.read_text(encoding="utf-8"))
    columns = sidecar.get("Columns")
    if not isinstance(columns, list) or not columns:
        raise ValueError(f"Missing/invalid Columns in {pupil_json}")

    rows: list[list[float]] = []
    with _open_text(pupil_tsv) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) < len(columns):
                continue
            parsed: list[float] = []
            ok = True
            for idx in range(len(columns)):
                v = _as_float(row[idx])
                if v is None:
                    parsed.append(float("nan"))
                else:
                    parsed.append(v)
            if ok:
                rows.append(parsed)
    if not rows:
        raise ValueError(f"No pupil rows parsed from {pupil_tsv}")
    mat = np.asarray(rows, dtype=np.float64)
    series = {str(columns[i]): mat[:, i] for i in range(len(columns))}
    return mat, series, sidecar


def _process_subject(
    paths: SubjectPaths,
    out_root: Path,
    analysis_included: str,
    args: argparse.Namespace,
) -> dict[str, str]:
    notes: list[str] = []
    subject_out = out_root / paths.subject
    eeg_out_dir = subject_out / "eeg"
    ecg_out_dir = subject_out / "ecg"
    pupil_out_dir = subject_out / "pupil"
    eeg_out_dir.mkdir(parents=True, exist_ok=True)
    ecg_out_dir.mkdir(parents=True, exist_ok=True)
    pupil_out_dir.mkdir(parents=True, exist_ok=True)

    log: dict[str, str] = {
        "participant_id": paths.subject,
        "analysis_included": analysis_included,
        "has_eeg": "false",
        "has_ecg": "false",
        "has_pupil": "false",
        "eeg_status": "not_run",
        "eeg_bad_count": "0",
        "eeg_bad_channels": "",
        "eeg_interpolated": "false",
        "eeg_montage_applied": "false",
        "eeg_ica_applied": "false",
        "eeg_ica_excluded_count": "0",
        "eeg_channels_out": "0",
        "eeg_sfreq_hz": "n/a",
        "ecg_status": "not_run",
        "ecg_samples": "0",
        "ecg_sfreq_hz": "n/a",
        "ecg_hr_mean_bpm": "n/a",
        "ecg_hr_median_bpm": "n/a",
        "ecg_hr_valid_ratio": "n/a",
        "pupil_status": "not_run",
        "pupil_samples_in": "0",
        "pupil_samples_out": "0",
        "pupil_masked_pct": "n/a",
        "pupil_target_sfreq_hz": _format_float(args.pupil_target_sfreq, 3),
        "notes": "",
    }

    # EEG
    if paths.eeg_vhdr.exists():
        log["has_eeg"] = "true"
        try:
            raw_full = mne.io.read_raw_brainvision(paths.eeg_vhdr, preload=True, verbose="ERROR")
            ecg_name = _read_ecg_channel_name(paths.channels_tsv)
            if ecg_name and ecg_name in raw_full.ch_names:
                raw_full.set_channel_types({ecg_name: "ecg"}, verbose="ERROR")

            raw_eeg = raw_full.copy().pick("eeg")
            if args.eeg_notch_hz > 0 and args.eeg_notch_hz < (raw_eeg.info["sfreq"] / 2.0):
                raw_eeg.notch_filter(
                    freqs=[args.eeg_notch_hz], picks="eeg", verbose="ERROR"
                )
            raw_eeg.filter(
                l_freq=args.eeg_l_freq,
                h_freq=args.eeg_h_freq,
                picks="eeg",
                verbose="ERROR",
            )
            bads = _detect_bad_eeg_channels(raw_eeg)
            raw_eeg.info["bads"] = bads
            log["eeg_bad_count"] = str(len(bads))
            log["eeg_bad_channels"] = ",".join(bads)

            _, montage_ok = _apply_eeg_alias_and_montage(raw_eeg)
            log["eeg_montage_applied"] = "true" if montage_ok else "false"
            interpolated = False
            if args.eeg_interpolate_bads and bads:
                try:
                    raw_eeg.interpolate_bads(reset_bads=False, verbose="ERROR")
                    interpolated = True
                except Exception:
                    notes.append("EEG interpolation failed; continuing without interpolation.")
            log["eeg_interpolated"] = "true" if interpolated else "false"

            raw_eeg.set_eeg_reference("average", projection=False, verbose="ERROR")

            ica_excluded: list[int] = []
            if args.run_ica:
                try:
                    n_components = min(
                        args.ica_max_components,
                        max(2, raw_eeg.info["nchan"] - 1),
                    )
                    ica = ICA(
                        n_components=n_components,
                        method="fastica",
                        random_state=args.random_state,
                        max_iter="auto",
                    )
                    ica.fit(raw_eeg.copy(), verbose="ERROR")
                    if ecg_name and ecg_name in raw_full.ch_names:
                        ecg_inds, _ = ica.find_bads_ecg(
                            raw_full,
                            ch_name=ecg_name,
                            method="correlation",
                            threshold="auto",
                            verbose="ERROR",
                        )
                        ica_excluded = ecg_inds[: args.ica_max_ecg_components]
                    ica.exclude = ica_excluded
                    if ica_excluded:
                        ica.apply(raw_eeg, verbose="ERROR")
                    log["eeg_ica_applied"] = "true"
                    log["eeg_ica_excluded_count"] = str(len(ica_excluded))
                except Exception:
                    notes.append("EEG ICA failed; continuing without ICA output.")
                    log["eeg_ica_applied"] = "false"

            eeg_out = eeg_out_dir / f"{paths.subject}_task-arithmetic_desc-preproc_eeg_raw.fif"
            raw_eeg.save(eeg_out, overwrite=args.overwrite, verbose="ERROR")
            eeg_meta = {
                "subject": paths.subject,
                "task": "arithmetic",
                "input_vhdr": str(paths.eeg_vhdr),
                "output_fif": str(eeg_out),
                "parameters": {
                    "notch_hz": args.eeg_notch_hz,
                    "bandpass_hz": [args.eeg_l_freq, args.eeg_h_freq],
                    "interpolate_bads": args.eeg_interpolate_bads,
                    "run_ica": args.run_ica,
                    "ica_max_components": args.ica_max_components,
                    "ica_max_ecg_components": args.ica_max_ecg_components,
                },
                "detected_bads": bads,
                "interpolated": interpolated,
                "montage_applied": montage_ok,
                "ica_excluded": ica_excluded,
                "sfreq_hz": float(raw_eeg.info["sfreq"]),
                "n_channels_out": int(raw_eeg.info["nchan"]),
            }
            (eeg_out_dir / f"{paths.subject}_task-arithmetic_desc-preproc_eeg.json").write_text(
                json.dumps(eeg_meta, indent=2) + "\n",
                encoding="utf-8",
            )
            log["eeg_status"] = "ok"
            log["eeg_channels_out"] = str(raw_eeg.info["nchan"])
            log["eeg_sfreq_hz"] = _format_float(float(raw_eeg.info["sfreq"]), 3)
        except Exception as e:
            log["eeg_status"] = "error"
            notes.append(f"EEG error: {e}")
    else:
        notes.append("Missing EEG input files.")

    # ECG
    if paths.ecg_tsv.exists() and paths.ecg_json.exists():
        log["has_ecg"] = "true"
        try:
            times, raw_vals = _load_ecg_series(paths.ecg_tsv)
            sidecar = json.loads(paths.ecg_json.read_text(encoding="utf-8"))
            sfreq = sidecar.get("SamplingFrequency")
            sfreq_val = float(sfreq) if isinstance(sfreq, (int, float)) else _infer_sfreq(times)
            if sfreq_val is None or sfreq_val <= 0:
                raise ValueError("Could not infer ECG sampling frequency.")

            centered = raw_vals - np.median(raw_vals)
            broad = _apply_bandpass(centered, sfreq_val, args.ecg_broad_l_freq, args.ecg_broad_h_freq)
            peak = _apply_bandpass(centered, sfreq_val, args.ecg_peak_l_freq, args.ecg_peak_h_freq)
            hr = _detect_hr_from_filtered_ecg(times, peak, sfreq_val)

            ecg_out_tsv = ecg_out_dir / f"{paths.subject}_task-arithmetic_desc-preproc-ecg.tsv"
            _write_ecg_clean(ecg_out_tsv, times, raw_vals, broad, peak)
            ecg_meta = {
                "subject": paths.subject,
                "task": "arithmetic",
                "input_tsv": str(paths.ecg_tsv),
                "output_tsv": str(ecg_out_tsv),
                "parameters": {
                    "broad_bandpass_hz": [args.ecg_broad_l_freq, args.ecg_broad_h_freq],
                    "peak_bandpass_hz": [args.ecg_peak_l_freq, args.ecg_peak_h_freq],
                },
                "sampling_frequency_hz": sfreq_val,
                "n_samples": int(times.size),
                "hr_summary": hr,
            }
            (ecg_out_dir / f"{paths.subject}_task-arithmetic_desc-preproc-ecg.json").write_text(
                json.dumps(ecg_meta, indent=2) + "\n",
                encoding="utf-8",
            )

            log["ecg_status"] = "ok"
            log["ecg_samples"] = str(int(times.size))
            log["ecg_sfreq_hz"] = _format_float(sfreq_val, 3)
            log["ecg_hr_mean_bpm"] = _format_float(hr["hr_mean_bpm"], 3)
            log["ecg_hr_median_bpm"] = _format_float(hr["hr_median_bpm"], 3)
            log["ecg_hr_valid_ratio"] = _format_float(hr["hr_valid_ratio"], 3)
        except Exception as e:
            log["ecg_status"] = "error"
            notes.append(f"ECG error: {e}")
    else:
        notes.append("Missing ECG input files.")

    # Pupil
    if paths.pupil_tsv.exists() and paths.pupil_json.exists():
        log["has_pupil"] = "true"
        try:
            _, series, sidecar = _load_pupil_matrix(paths.pupil_tsv, paths.pupil_json)
            time = series.get("time")
            if time is None:
                raise ValueError("Missing time column in pupil file.")
            start_time = sidecar.get("StartTime", 0.0)
            start_offset = float(start_time) if isinstance(start_time, (int, float)) else 0.0
            t = time + start_offset

            order = np.argsort(t)
            t = t[order]
            confidence = series.get("confidence")
            pupil_size = series.get("pupil_size")
            x_coord = series.get("x_coordinate")
            y_coord = series.get("y_coordinate")
            if confidence is None or pupil_size is None:
                raise ValueError("Missing confidence or pupil_size columns in pupil file.")
            confidence = confidence[order]
            pupil_size = pupil_size[order]
            x_coord = x_coord[order] if x_coord is not None else np.full_like(t, np.nan)
            y_coord = y_coord[order] if y_coord is not None else np.full_like(t, np.nan)

            unique_t, unique_idx = np.unique(t, return_index=True)
            t = unique_t
            confidence = confidence[unique_idx]
            pupil_size = pupil_size[unique_idx]
            x_coord = x_coord[unique_idx]
            y_coord = y_coord[unique_idx]

            conf_ok = np.isfinite(confidence) & (confidence >= args.pupil_conf_threshold)
            size_ok = np.isfinite(pupil_size) & (pupil_size > 0.0)
            valid = conf_ok & size_ok
            masked_pct = 100.0 * float(np.count_nonzero(~valid)) / float(valid.size)

            pupil_interp = _interp_signal(t, pupil_size, valid)
            x_interp = _interp_signal(t, x_coord, conf_ok & np.isfinite(x_coord))
            y_interp = _interp_signal(t, y_coord, conf_ok & np.isfinite(y_coord))
            conf_interp = _interp_signal(t, confidence, np.isfinite(confidence))

            orig_sfreq = _infer_sfreq(t)
            smooth_window = 1
            if orig_sfreq is not None and orig_sfreq > 0:
                smooth_window = max(1, int(round(args.pupil_smooth_seconds * orig_sfreq)))
            pupil_smooth = _smooth_series(pupil_interp, smooth_window)
            x_smooth = _smooth_series(x_interp, smooth_window)
            y_smooth = _smooth_series(y_interp, smooth_window)
            conf_smooth = _smooth_series(conf_interp, smooth_window)

            t_start = float(t[0])
            t_end = float(t[-1])
            step = 1.0 / float(args.pupil_target_sfreq)
            t_resampled = np.arange(t_start, t_end + (0.5 * step), step)
            pupil_resampled = np.interp(t_resampled, t, pupil_smooth)
            x_resampled = np.interp(t_resampled, t, x_smooth)
            y_resampled = np.interp(t_resampled, t, y_smooth)
            conf_resampled = np.interp(t_resampled, t, conf_smooth)

            pupil_out_tsv = pupil_out_dir / f"{paths.subject}_task-arithmetic_desc-preproc-pupil.tsv"
            with pupil_out_tsv.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f, delimiter="\t", lineterminator="\n")
                writer.writerow(
                    [
                        "time",
                        "pupil_size_clean",
                        "x_coordinate_clean",
                        "y_coordinate_clean",
                        "confidence_clean",
                    ]
                )
                for i in range(t_resampled.size):
                    writer.writerow(
                        [
                            f"{t_resampled[i]:.6f}",
                            f"{pupil_resampled[i]:.9f}",
                            f"{x_resampled[i]:.9f}",
                            f"{y_resampled[i]:.9f}",
                            f"{conf_resampled[i]:.9f}",
                        ]
                    )
            pupil_meta = {
                "subject": paths.subject,
                "task": "arithmetic",
                "input_tsv": str(paths.pupil_tsv),
                "output_tsv": str(pupil_out_tsv),
                "parameters": {
                    "confidence_threshold": args.pupil_conf_threshold,
                    "smoothing_seconds": args.pupil_smooth_seconds,
                    "target_sampling_frequency_hz": args.pupil_target_sfreq,
                },
                "n_samples_in": int(t.size),
                "n_samples_out": int(t_resampled.size),
                "masked_pct": masked_pct,
            }
            (pupil_out_dir / f"{paths.subject}_task-arithmetic_desc-preproc-pupil.json").write_text(
                json.dumps(pupil_meta, indent=2) + "\n",
                encoding="utf-8",
            )

            log["pupil_status"] = "ok"
            log["pupil_samples_in"] = str(int(t.size))
            log["pupil_samples_out"] = str(int(t_resampled.size))
            log["pupil_masked_pct"] = _format_float(masked_pct, 3)
        except Exception as e:
            log["pupil_status"] = "error"
            notes.append(f"Pupil error: {e}")
    else:
        notes.append("Missing pupil input files.")

    log["notes"] = " | ".join(notes)
    return log


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Stage 2 preprocessing for EEG/ECG/pupil. "
            "Writes cleaned derivatives and a subject-level preprocess log."
        )
    )
    parser.add_argument("--bids-root", required=True, help="Path to BIDS root.")
    parser.add_argument("--task", default=None, help="Task name (default: infer from BIDS root).")
    parser.add_argument(
        "--subjects",
        nargs="*",
        default=None,
        help="Optional subset of subject IDs (e.g., sub-001 sub-003).",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs.")

    parser.add_argument("--eeg-notch-hz", type=float, default=50.0)
    parser.add_argument("--eeg-l-freq", type=float, default=1.0)
    parser.add_argument("--eeg-h-freq", type=float, default=40.0)
    parser.add_argument(
        "--eeg-interpolate-bads",
        dest="eeg_interpolate_bads",
        action="store_true",
        default=True,
        help="Interpolate detected bad EEG channels (default: enabled).",
    )
    parser.add_argument(
        "--no-eeg-interpolate-bads",
        dest="eeg_interpolate_bads",
        action="store_false",
        help="Disable EEG bad-channel interpolation.",
    )
    parser.add_argument("--run-ica", action="store_true")
    parser.add_argument("--ica-max-components", type=int, default=15)
    parser.add_argument("--ica-max-ecg-components", type=int, default=2)
    parser.add_argument("--random-state", type=int, default=42)

    parser.add_argument("--ecg-broad-l-freq", type=float, default=0.5)
    parser.add_argument("--ecg-broad-h-freq", type=float, default=40.0)
    parser.add_argument("--ecg-peak-l-freq", type=float, default=5.0)
    parser.add_argument("--ecg-peak-h-freq", type=float, default=25.0)

    parser.add_argument("--pupil-conf-threshold", type=float, default=0.60)
    parser.add_argument("--pupil-smooth-seconds", type=float, default=0.20)
    parser.add_argument("--pupil-target-sfreq", type=float, default=100.0)
    args = parser.parse_args()

    bids_root = _resolve_bids_root(args.bids_root)
    if not bids_root.exists():
        raise FileNotFoundError(bids_root)
    task = args.task or _task_from_bids_root(bids_root)

    participants = _read_participants(bids_root / "participants.tsv")
    out_root = _derivatives_root()
    out_root.mkdir(parents=True, exist_ok=True)
    reports_dir = _reports_dir()
    reports_dir.mkdir(parents=True, exist_ok=True)

    subject_dirs = sorted(path for path in bids_root.glob("sub-*") if path.is_dir())
    if args.subjects:
        wanted = set(args.subjects)
        subject_dirs = [path for path in subject_dirs if path.name in wanted]
    if not subject_dirs:
        raise FileNotFoundError("No matching subject directories found.")

    logs: list[dict[str, str]] = []
    for subject_dir in subject_dirs:
        paths = _resolve_subject_paths(subject_dir, task)
        analysis_included = (
            (participants.get(paths.subject, {}).get("analysis_included") or "n/a")
            .strip()
            .lower()
        )
        if analysis_included not in ("true", "false"):
            analysis_included = "n/a"
        log = _process_subject(paths, out_root, analysis_included, args)
        logs.append(log)
        print(
            f"{paths.subject}: EEG={log['eeg_status']} ECG={log['ecg_status']} "
            f"Pupil={log['pupil_status']}"
        )

    fields = [
        "participant_id",
        "analysis_included",
        "has_eeg",
        "has_ecg",
        "has_pupil",
        "eeg_status",
        "eeg_bad_count",
        "eeg_bad_channels",
        "eeg_interpolated",
        "eeg_montage_applied",
        "eeg_ica_applied",
        "eeg_ica_excluded_count",
        "eeg_channels_out",
        "eeg_sfreq_hz",
        "ecg_status",
        "ecg_samples",
        "ecg_sfreq_hz",
        "ecg_hr_mean_bpm",
        "ecg_hr_median_bpm",
        "ecg_hr_valid_ratio",
        "pupil_status",
        "pupil_samples_in",
        "pupil_samples_out",
        "pupil_masked_pct",
        "pupil_target_sfreq_hz",
        "notes",
    ]
    log_path = reports_dir / "preprocess_log.tsv"
    _write_tsv(log_path, fields, logs)

    summary = {
        "bids_root": str(bids_root),
        "task": task,
        "subjects_processed": len(logs),
        "out_root": str(out_root),
        "preprocess_log_tsv": str(log_path),
        "parameters": {
            "eeg_notch_hz": args.eeg_notch_hz,
            "eeg_bandpass_hz": [args.eeg_l_freq, args.eeg_h_freq],
            "eeg_interpolate_bads": args.eeg_interpolate_bads,
            "run_ica": args.run_ica,
            "ica_max_components": args.ica_max_components,
            "ica_max_ecg_components": args.ica_max_ecg_components,
            "ecg_broad_bandpass_hz": [args.ecg_broad_l_freq, args.ecg_broad_h_freq],
            "ecg_peak_bandpass_hz": [args.ecg_peak_l_freq, args.ecg_peak_h_freq],
            "pupil_conf_threshold": args.pupil_conf_threshold,
            "pupil_smooth_seconds": args.pupil_smooth_seconds,
            "pupil_target_sfreq_hz": args.pupil_target_sfreq,
            "random_state": args.random_state,
        },
        "status_counts": {
            "eeg_ok": sum(1 for row in logs if row["eeg_status"] == "ok"),
            "ecg_ok": sum(1 for row in logs if row["ecg_status"] == "ok"),
            "pupil_ok": sum(1 for row in logs if row["pupil_status"] == "ok"),
            "any_error": sum(
                1
                for row in logs
                if "error" in (row["eeg_status"], row["ecg_status"], row["pupil_status"])
            ),
        },
        "mean_ecg_hr_bpm": (
            mean(
                [
                    float(row["ecg_hr_mean_bpm"])
                    for row in logs
                    if row["ecg_hr_mean_bpm"] != "n/a"
                ]
            )
            if any(row["ecg_hr_mean_bpm"] != "n/a" for row in logs)
            else None
        ),
    }
    summary_path = reports_dir / "preprocess_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote preprocess log: {log_path}")
    print(f"Wrote preprocess summary: {summary_path}")


if __name__ == "__main__":
    main()
