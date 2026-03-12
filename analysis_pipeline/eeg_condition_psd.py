from __future__ import annotations

import json
import math
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from mne.channels.layout import _find_topomap_coords
from mne.viz.topomap import _draw_outlines, _make_head_outlines
import mne
import numpy as np
import pandas as pd
from eeg_units import ensure_eeg_data_in_volts

from stage4_extract_features import BANDS_HZ, ROI_CHANNELS, _roi_indices

mne.set_log_level("ERROR")


ROI_PLOT_ORDER = [
    "frontal",
    "central",
    "parietal",
    "temporal",
    "occipital",
]

TOPO_BAND_ORDER = ["theta", "alpha", "beta", "highbeta"]
TOPO_CMAP = "RdBu_r"
TOPO_VLIM_PERCENTILE = 95.0
ROI_REFERENCE_COLORS = {
    "frontal": "#d1495b",
    "central": "#edae49",
    "parietal": "#66a182",
    "temporal": "#00798c",
    "occipital": "#5f0f40",
}
TOPO_PLOT_SPHERE = (0.0, 0.0, 0.0, 0.095)
TOPO_DISPLAY_Y_OFFSET = -0.02
ROI_REFERENCE_LABEL_Y_SHIFT = -0.018


def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    text = str(value).strip()
    if not text or text.lower() == "n/a":
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


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


def _resolve_existing_path(path_text: str) -> Path:
    direct = Path(path_text).expanduser()
    if direct.exists():
        return direct.resolve()
    translated_wsl = _translate_wsl_path(path_text)
    if translated_wsl is not None and translated_wsl.exists():
        return translated_wsl.resolve()
    translated_windows = _translate_windows_drive_path(path_text)
    if translated_windows is not None and translated_windows.exists():
        return translated_windows.resolve()
    return direct.resolve()


def _load_epoch_lookup(epoch_manifest_path: Path) -> dict[tuple[str, str], Path]:
    manifest = pd.read_csv(epoch_manifest_path, sep="\t", dtype=str, keep_default_na=False)
    required = {"participant_id", "epoch_id", "eeg_keep", "eeg_epoch_file"}
    missing = sorted(required - set(manifest.columns))
    if missing:
        raise ValueError(
            f"Epoch manifest missing required EEG columns: {', '.join(missing)} ({epoch_manifest_path})"
        )

    lookup: dict[tuple[str, str], Path] = {}
    for _, row in manifest.iterrows():
        participant = str(row.get("participant_id", "")).strip()
        epoch_id = str(row.get("epoch_id", "")).strip()
        keep = str(row.get("eeg_keep", "")).strip().lower()
        epoch_file_text = str(row.get("eeg_epoch_file", "")).strip()
        if not participant or not epoch_id or keep != "true" or not epoch_file_text:
            continue
        epoch_file = _resolve_existing_path(epoch_file_text)
        if not epoch_file.exists():
            continue
        lookup[(participant, epoch_id)] = epoch_file
    return lookup


def _load_subject_ch_names(participant: str, epoch_file: Path) -> list[str]:
    meta_candidates = sorted(epoch_file.parent.glob(f"{participant}_task-*_desc-epochs-eeg_meta.json"))
    if not meta_candidates:
        raise FileNotFoundError(f"Missing EEG meta JSON for {participant} near {epoch_file}")
    payload = json.loads(meta_candidates[0].read_text(encoding="utf-8"))
    ch_names = [str(name).strip() for name in payload.get("ch_names", []) if str(name).strip()]
    if not ch_names:
        raise ValueError(f"Missing ch_names in {meta_candidates[0]}")
    return ch_names


def _make_eeg_info(ch_names: list[str], sfreq: float) -> mne.Info:
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=["eeg"] * len(ch_names))
    info.set_montage("standard_1020", on_missing="ignore")
    return info


def _build_group_title(
    scope_label: str,
    scenario_name: str,
    condition_epoch_counts: dict[str, int],
    condition_participant_counts: dict[str, int] | None,
    plot_label: str = "EEG Power Spectrum by Condition",
) -> tuple[str, str]:
    title = f"{plot_label} | {scope_label}"
    subtitle_bits = [f"scenario={scenario_name}"]
    for label in condition_epoch_counts:
        bit = f"{label}: n_epochs={condition_epoch_counts[label]}"
        if condition_participant_counts is not None and label in condition_participant_counts:
            bit += f", n_participants={condition_participant_counts[label]}"
        subtitle_bits.append(bit)
    return title, " | ".join(subtitle_bits)


def _plot_condition_spectra(
    *,
    roi_spectra_by_condition: dict[str, dict[str, np.ndarray]],
    freqs: np.ndarray,
    condition_order: list[str],
    out_path: Path,
    title: str,
    subtitle: str,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    n_cols = min(3, max(len(ROI_PLOT_ORDER), 1))
    n_rows = max(1, math.ceil(len(ROI_PLOT_ORDER) / float(n_cols)))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5.2 * n_cols, 4.2 * n_rows))
    axes_arr = np.asarray(axes, dtype=object)
    if axes_arr.ndim == 0:
        axes_arr = axes_arr.reshape(1, 1)
    elif axes_arr.ndim == 1:
        if n_rows == 1:
            axes_arr = axes_arr.reshape(1, n_cols)
        else:
            axes_arr = axes_arr.reshape(n_rows, n_cols)
    axes_flat = list(axes_arr.ravel())
    colors = plt.get_cmap("tab10")(np.linspace(0.0, 1.0, max(len(condition_order), 1)))
    legend_handles = [Line2D([0], [0], color=colors[idx], lw=2, label=label) for idx, label in enumerate(condition_order)]

    for ax, roi in zip(axes_flat, ROI_PLOT_ORDER):
        plotted = False
        roi_payload = roi_spectra_by_condition.get(roi, {})
        for idx, condition in enumerate(condition_order):
            spectrum_1d = roi_payload.get(condition)
            if spectrum_1d is None:
                continue
            color = tuple(float(value) for value in colors[idx])
            info = mne.create_info(ch_names=[condition], sfreq=1.0, ch_types=["eeg"])
            spectrum = mne.time_frequency.SpectrumArray(
                data=np.asarray([spectrum_1d], dtype=np.float64),
                info=info,
                freqs=freqs.astype(np.float64, copy=False),
            )
            spectrum.plot(
                average=False,
                dB=True,
                amplitude=False,
                xscale="linear",
                ci=None,
                spatial_colors=False,
                color=color,
                axes=ax,
                show=False,
            )
            plotted = True
        ax.set_title(roi.capitalize())
        if not plotted:
            ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
            ax.set_axis_off()

    for ax in axes_flat[len(ROI_PLOT_ORDER) :]:
        ax.set_axis_off()

    fig.subplots_adjust(left=0.07, right=0.99, top=0.90, bottom=0.12, wspace=0.18, hspace=0.14)
    fig.suptitle(title, fontsize=14, y=0.985)
    if legend_handles:
        fig.legend(
            handles=legend_handles,
            loc="upper center",
            bbox_to_anchor=(0.5, 0.962),
            ncol=min(len(legend_handles), 4),
            frameon=False,
        )
    fig.text(
        0.5,
        0.03,
        textwrap.fill(subtitle, width=150, break_long_words=False, break_on_hyphens=False),
        ha="center",
        va="bottom",
        fontsize=8,
    )
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _freqs_match(freqs_a: np.ndarray, freqs_b: np.ndarray) -> bool:
    return freqs_a.shape == freqs_b.shape and np.allclose(freqs_a, freqs_b, rtol=0.0, atol=1e-8)


def _interp_channel_spectra(
    channel_spectra: np.ndarray,
    source_freqs: np.ndarray,
    target_freqs: np.ndarray,
) -> np.ndarray:
    return np.vstack(
        [
            np.interp(target_freqs, source_freqs, row, left=np.nan, right=np.nan)
            for row in channel_spectra.astype(np.float64, copy=False)
        ]
    )


def _align_channel_spectra(
    channel_spectra: np.ndarray,
    source_ch_names: list[str],
    target_ch_names: list[str],
) -> np.ndarray:
    aligned = np.full((len(target_ch_names), channel_spectra.shape[1]), np.nan, dtype=np.float64)
    source_lookup = {name: idx for idx, name in enumerate(source_ch_names)}
    for target_idx, ch_name in enumerate(target_ch_names):
        source_idx = source_lookup.get(ch_name)
        if source_idx is None:
            continue
        aligned[target_idx] = channel_spectra[source_idx]
    return aligned


def _topomap_picks(info: mne.Info) -> np.ndarray:
    picks: list[int] = []
    for idx, ch in enumerate(info["chs"]):
        loc = np.asarray(ch.get("loc", np.zeros(12)), dtype=np.float64)[:3]
        if np.allclose(loc, 0.0) or not np.all(np.isfinite(loc)):
            continue
        picks.append(idx)
    return np.asarray(picks, dtype=int)


def _topomap_display_pos(info: mne.Info) -> np.ndarray:
    pos = _find_topomap_coords(
        info,
        picks=np.arange(len(info.ch_names), dtype=int),
        sphere=TOPO_PLOT_SPHERE,
    ).astype(np.float64, copy=True)
    # Standard 10-20 montage plots sit slightly too anterior with MNE's default head outline.
    pos[:, 1] += TOPO_DISPLAY_Y_OFFSET
    return pos


def _save_note_figure(
    *,
    out_path: Path,
    title: str,
    subtitle: str,
    note: str,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 4.5), constrained_layout=True)
    ax.text(0.5, 0.5, note, ha="center", va="center", fontsize=11, transform=ax.transAxes)
    ax.set_axis_off()
    fig.suptitle(title, fontsize=14)
    fig.text(0.5, 0.03, subtitle, ha="center", fontsize=9)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _band_channel_values_db(
    channel_spectra: np.ndarray,
    freqs: np.ndarray,
    band_name: str,
    *,
    center: bool = False,
) -> np.ndarray:
    fmin, fmax = BANDS_HZ[band_name]
    mask = (freqs >= fmin) & (freqs < fmax)
    if not np.any(mask):
        return np.full(channel_spectra.shape[0], np.nan, dtype=np.float64)
    band_vals = np.mean(channel_spectra[:, mask], axis=1)
    band_vals_db = 10.0 * np.log10(np.maximum(band_vals.astype(np.float64, copy=False), 1e-20))
    if center:
        finite = band_vals_db[np.isfinite(band_vals_db)]
        if finite.size:
            band_vals_db = band_vals_db - float(np.nanmean(finite))
    return band_vals_db


def _plot_roi_reference_topomap(
    *,
    info: mne.Info,
    out_path: Path,
    title: str,
    subtitle: str,
) -> None:
    picks = _topomap_picks(info)
    if picks.size < 3:
        _save_note_figure(
            out_path=out_path,
            title=title,
            subtitle=subtitle,
            note="Insufficient positioned EEG channels for ROI reference rendering.",
        )
        return

    info = mne.pick_info(info.copy(), sel=picks)
    roi_by_channel = {channel: roi for roi, channels in ROI_CHANNELS.items() for channel in channels}
    valid_indices: list[int] = []
    region_values: list[float] = []
    missing_channels: list[str] = []
    for idx, ch_name in enumerate(info.ch_names):
        roi_name = roi_by_channel.get(ch_name)
        if roi_name is None or roi_name not in ROI_PLOT_ORDER:
            missing_channels.append(ch_name)
            continue
        valid_indices.append(idx)
        region_values.append(float(ROI_PLOT_ORDER.index(roi_name) + 1))

    if len(valid_indices) < 3:
        _save_note_figure(
            out_path=out_path,
            title=title,
            subtitle=subtitle,
            note="Insufficient ROI-mapped EEG channels for ROI reference rendering.",
        )
        return

    info = mne.pick_info(info.copy(), sel=np.asarray(valid_indices, dtype=int))
    pos = _topomap_display_pos(info)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(9.6, 5.8), constrained_layout=True)
    grid = fig.add_gridspec(1, 2, width_ratios=[1.25, 1.0])
    ax_head = fig.add_subplot(grid[0, 0])
    ax_legend = fig.add_subplot(grid[0, 1])

    sphere = np.asarray(TOPO_PLOT_SPHERE, dtype=np.float64)
    outlines = _make_head_outlines(
        sphere=sphere,
        pos=pos,
        outlines="head",
        clip_origin=tuple(float(value) for value in sphere[:2]),
    )
    mask_x, mask_y = outlines["mask_pos"]
    ax_head.fill(mask_x, mask_y, color="#f3f4f6", zorder=0)
    _draw_outlines(ax_head, outlines)
    ax_head.set_aspect("equal")
    ax_head.set_xlim(float(np.min(mask_x)) - 0.02, float(np.max(mask_x)) + 0.02)
    ax_head.set_ylim(float(np.min(mask_y)) - 0.04, float(np.max(mask_y)) + 0.02)
    ax_head.set_axis_off()
    ax_head.set_title("Electrode ROI Reference", fontsize=11)
    for idx, (x_pos, y_pos) in enumerate(pos):
        channel_name = info.ch_names[idx]
        roi_name = roi_by_channel[channel_name]
        if y_pos > 0.7:
            text_offset = -0.07
            text_va = "top"
        elif y_pos > 0.5:
            text_offset = -0.04
            text_va = "top"
        else:
            text_offset = 0.035
            text_va = "bottom"
        ax_head.scatter(
            x_pos,
            y_pos,
            s=68,
            facecolor=ROI_REFERENCE_COLORS[roi_name],
            edgecolor="black",
            linewidth=0.6,
            zorder=3,
        )
        ax_head.text(
            x_pos,
            y_pos + text_offset + ROI_REFERENCE_LABEL_Y_SHIFT,
            channel_name,
            fontsize=7.5,
            ha="center",
            va=text_va,
            color="black",
            zorder=4,
        )

    ax_legend.set_axis_off()
    ax_legend.set_xlim(0.0, 1.0)
    ax_legend.set_ylim(0.0, 1.0)
    ax_legend.text(0.0, 0.98, "Region key", fontsize=12, fontweight="bold", va="top")
    y_pos = 0.88
    for roi_name in ROI_PLOT_ORDER:
        channels_present = [ch for ch in ROI_CHANNELS.get(roi_name, []) if ch in info.ch_names]
        if not channels_present:
            continue
        ax_legend.scatter(
            0.03,
            y_pos - 0.008,
            s=110,
            color=ROI_REFERENCE_COLORS[roi_name],
            edgecolors="black",
            linewidths=0.6,
            clip_on=False,
        )
        channel_text = textwrap.fill(
            ", ".join(channels_present),
            width=28,
            break_long_words=False,
            break_on_hyphens=False,
        )
        ax_legend.text(
            0.08,
            y_pos,
            f"{roi_name.capitalize()}: {channel_text}",
            fontsize=10,
            va="top",
            linespacing=1.3,
        )
        y_pos -= 0.17

    if missing_channels:
        missing_text = textwrap.fill(
            ", ".join(missing_channels),
            width=28,
            break_long_words=False,
            break_on_hyphens=False,
        )
        ax_legend.text(0.0, 0.05, f"Unassigned channels: {missing_text}", fontsize=9, va="bottom")

    fig.suptitle(title, fontsize=14)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _plot_condition_topomaps(
    *,
    channel_spectra_by_condition: dict[str, np.ndarray],
    freqs: np.ndarray,
    info: mne.Info,
    condition_order: list[str],
    out_path: Path,
    title: str,
    subtitle: str,
) -> None:
    bands_present = [band for band in TOPO_BAND_ORDER if band in BANDS_HZ]
    if not condition_order or not bands_present:
        return
    picks = _topomap_picks(info)
    if picks.size < 3:
        _save_note_figure(
            out_path=out_path,
            title=title,
            subtitle=subtitle,
            note="Insufficient positioned EEG channels for topomap rendering.",
        )
        return
    info = mne.pick_info(info.copy(), sel=picks)
    pos = _topomap_display_pos(info)
    channel_spectra_by_condition = {
        condition: spectra[picks].astype(np.float64, copy=False)
        for condition, spectra in channel_spectra_by_condition.items()
        if spectra.shape[0] >= int(np.max(picks)) + 1
    }
    if not channel_spectra_by_condition:
        _save_note_figure(
            out_path=out_path,
            title=title,
            subtitle=subtitle,
            note="No channel spectra available for topomap rendering.",
        )
        return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    n_rows = len(condition_order)
    n_cols = len(bands_present)
    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(3.0 * n_cols, 2.8 * max(n_rows, 1)),
        constrained_layout=True,
    )
    axes_arr = np.asarray(axes, dtype=object)
    if axes_arr.ndim == 0:
        axes_arr = axes_arr.reshape(1, 1)
    elif axes_arr.ndim == 1:
        if n_rows == 1:
            axes_arr = axes_arr.reshape(1, n_cols)
        else:
            axes_arr = axes_arr.reshape(n_rows, 1)

    band_vlims: dict[str, tuple[float, float]] = {}
    band_values_by_condition: dict[str, dict[str, np.ndarray]] = {}
    for band_name in bands_present:
        values_all: list[np.ndarray] = []
        for condition in condition_order:
            channel_spectra = channel_spectra_by_condition.get(condition)
            if channel_spectra is None:
                continue
            band_values = _band_channel_values_db(channel_spectra, freqs, band_name, center=True)
            band_values_by_condition.setdefault(condition, {})[band_name] = band_values
            values_all.append(band_values)
        if values_all:
            stacked = np.concatenate(values_all)
            finite = stacked[np.isfinite(stacked)]
            if finite.size:
                vmax = float(np.nanpercentile(np.abs(finite), TOPO_VLIM_PERCENTILE))
                if not math.isfinite(vmax) or math.isclose(vmax, 0.0, rel_tol=0.0, abs_tol=1e-12):
                    vmax = 1.0
                band_vlims[band_name] = (-vmax, vmax)
                continue
        band_vlims[band_name] = (-1.0, 1.0)

    for row_idx, condition in enumerate(condition_order):
        for col_idx, band_name in enumerate(bands_present):
            ax = axes_arr[row_idx, col_idx]
            band_values = band_values_by_condition.get(condition, {}).get(band_name)
            if band_values is None:
                ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
                ax.set_axis_off()
                continue
            band_label = f"{band_name} ({BANDS_HZ[band_name][0]:.0f}-{BANDS_HZ[band_name][1]:.0f} Hz)"
            mne.viz.plot_topomap(
                band_values.astype(np.float64, copy=False),
                pos,
                axes=ax,
                show=False,
                cmap=TOPO_CMAP,
                vlim=band_vlims[band_name],
                contours=0,
                sensors=True,
                sphere=TOPO_PLOT_SPHERE,
            )
            ax.set_title(band_label if row_idx == 0 else "", fontsize=10)
            if col_idx == 0:
                ax.set_ylabel(condition, fontsize=10)

    for col_idx, band_name in enumerate(bands_present):
        vmin, vmax = band_vlims[band_name]
        sm = ScalarMappable(norm=Normalize(vmin=vmin, vmax=vmax), cmap=TOPO_CMAP)
        sm.set_array([])
        colorbar = fig.colorbar(sm, ax=axes_arr[:, col_idx].tolist(), shrink=0.75, pad=0.02)
        colorbar.set_label("dB vs condition mean", fontsize=8)

    fig.suptitle(title, fontsize=14)
    fig.text(0.5, 0.02, subtitle, ha="center", fontsize=9)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def build_condition_psd_report(
    *,
    eeg_df: pd.DataFrame | None,
    epoch_manifest_path: Path | None,
    out_dir: Path,
    scenario_name: str,
    label_order: list[str],
    fmin: float = 2.0,
    fmax: float = 40.0,
) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    summary: dict[str, Any] = {
        "status": "skipped",
        "scenario_name": scenario_name,
        "epoch_manifest_path": str(epoch_manifest_path) if epoch_manifest_path is not None else None,
        "out_dir": str(out_dir),
        "manifest_json": str(manifest_path),
        "all_participants_png": None,
        "all_participants_topomap_png": None,
        "roi_reference_topomap_png": None,
        "single_participant_pngs": {},
        "single_participant_topomap_pngs": {},
        "roi_channels": {
            roi: [channel for channel in ROI_CHANNELS.get(roi, [])]
            for roi in ROI_PLOT_ORDER
            if roi in ROI_CHANNELS
        },
        "roi_names": list(ROI_PLOT_ORDER),
        "topomap_band_order": [band for band in TOPO_BAND_ORDER if band in BANDS_HZ],
        "label_order_requested": list(label_order),
        "label_order_plotted": [],
        "condition_epoch_counts_all_participants": {},
        "condition_participant_counts_all_participants": {},
        "participant_condition_epoch_counts": {},
        "participants_plotted": [],
        "n_participants_plotted": 0,
        "fmin": float(fmin),
        "fmax": float(fmax),
    }

    if eeg_df is None:
        summary["reason"] = "eeg_dataset_not_selected"
        manifest_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        return summary
    if eeg_df.empty:
        summary["reason"] = "eeg_dataset_empty_after_class_mapping"
        manifest_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        return summary
    if epoch_manifest_path is None or not epoch_manifest_path.exists():
        summary["reason"] = "epoch_manifest_missing"
        manifest_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        return summary

    epoch_lookup = _load_epoch_lookup(epoch_manifest_path)
    row_records: dict[str, dict[str, list[Path]]] = defaultdict(lambda: defaultdict(list))
    missing_epoch_keys: list[dict[str, str]] = []
    seen_keys: set[tuple[str, str]] = set()
    for _, row in eeg_df.iterrows():
        participant = str(row.get("participant_id", "")).strip()
        epoch_id = str(row.get("epoch_id", "")).strip()
        condition = str(row.get("_target_label_effective", "")).strip()
        if not participant or not epoch_id or not condition:
            continue
        row_key = (participant, epoch_id)
        if row_key in seen_keys:
            continue
        seen_keys.add(row_key)
        epoch_file = epoch_lookup.get(row_key)
        if epoch_file is None:
            missing_epoch_keys.append({"participant_id": participant, "epoch_id": epoch_id})
            continue
        row_records[participant][condition].append(epoch_file)

    summary["missing_epoch_keys"] = missing_epoch_keys
    if not row_records:
        summary["reason"] = "no_epoch_files_matched_filtered_eeg_rows"
        manifest_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        return summary

    aggregate_roi_spectra: dict[str, dict[str, list[np.ndarray]]] = {
        roi: defaultdict(list) for roi in ROI_PLOT_ORDER
    }
    aggregate_channel_spectra: dict[str, list[np.ndarray]] = defaultdict(list)
    freqs_ref: np.ndarray | None = None
    group_ch_names_ref: list[str] | None = None
    group_info_ref: mne.Info | None = None
    all_condition_epoch_counts: dict[str, int] = defaultdict(int)
    all_condition_participant_counts: dict[str, int] = defaultdict(int)
    single_participant_pngs: dict[str, str] = {}
    single_participant_topomap_pngs: dict[str, str] = {}
    roi_reference_topomap_png: str | None = None
    participant_condition_epoch_counts: dict[str, dict[str, int]] = {}
    plotted_participants: list[str] = []

    for participant in sorted(row_records):
        condition_paths = row_records[participant]
        participant_data: list[np.ndarray] = []
        participant_labels: list[str] = []
        participant_epoch_counts: dict[str, int] = {}
        first_epoch_file: Path | None = None
        first_times: np.ndarray | None = None

        for condition in label_order:
            paths = condition_paths.get(condition, [])
            if not paths:
                continue
            participant_epoch_counts[condition] = len(paths)
            all_condition_epoch_counts[condition] += len(paths)
            all_condition_participant_counts[condition] += 1
            for epoch_file in paths:
                payload = np.load(epoch_file)
                if "data" not in payload.files or "time" not in payload.files:
                    continue
                data_raw = np.asarray(payload["data"], dtype=np.float64)
                data, _ = ensure_eeg_data_in_volts(data_raw)
                times = np.asarray(payload["time"], dtype=np.float64)
                if data.ndim != 2 or times.ndim != 1 or data.shape[1] != times.size:
                    continue
                if first_epoch_file is None:
                    first_epoch_file = epoch_file
                    first_times = times
                participant_data.append(data)
                participant_labels.append(condition)

        if first_epoch_file is None or first_times is None or not participant_data:
            continue

        sfreq = _infer_sfreq(first_times)
        if sfreq is None or sfreq <= 0:
            raise ValueError(f"Could not infer EEG sampling frequency for {participant}")
        ch_names = _load_subject_ch_names(participant, first_epoch_file)
        if any(arr.shape != participant_data[0].shape for arr in participant_data):
            raise ValueError(f"Inconsistent EEG epoch shapes for {participant}")
        if participant_data[0].shape[0] != len(ch_names):
            raise ValueError(f"EEG channel count mismatch for {participant}")

        info = _make_eeg_info(ch_names=ch_names, sfreq=sfreq)
        if group_ch_names_ref is None:
            group_ch_names_ref = list(ch_names)
            group_info_ref = _make_eeg_info(ch_names=group_ch_names_ref, sfreq=sfreq)
        epochs = mne.EpochsArray(np.stack(participant_data, axis=0), info, tmin=0.0, verbose="ERROR")
        spectrum = epochs.compute_psd(method="multitaper", fmin=fmin, fmax=fmax, verbose="ERROR")
        freqs = spectrum.freqs.astype(np.float64, copy=False)
        if freqs_ref is None:
            freqs_ref = freqs

        psd = spectrum.get_data()
        roi_idx = _roi_indices(ch_names)
        participant_roi_spectra: dict[str, dict[str, np.ndarray]] = {roi: {} for roi in ROI_PLOT_ORDER}
        participant_channel_spectra: dict[str, np.ndarray] = {}
        label_array = np.asarray(participant_labels, dtype=object)
        plotted_labels: list[str] = []
        for condition in label_order:
            cond_mask = label_array == condition
            if not bool(np.any(cond_mask)):
                continue
            plotted_labels.append(condition)
            condition_channel_mean = np.mean(psd[cond_mask], axis=0).astype(np.float64, copy=False)
            participant_channel_spectra[condition] = condition_channel_mean
            group_channel_mean = condition_channel_mean
            if group_ch_names_ref is not None and ch_names != group_ch_names_ref:
                group_channel_mean = _align_channel_spectra(
                    channel_spectra=group_channel_mean,
                    source_ch_names=ch_names,
                    target_ch_names=group_ch_names_ref,
                )
            if freqs_ref is not None and not _freqs_match(freqs_ref, freqs):
                group_channel_mean = _interp_channel_spectra(
                    channel_spectra=group_channel_mean,
                    source_freqs=freqs,
                    target_freqs=freqs_ref,
                )
            aggregate_channel_spectra[condition].append(group_channel_mean)
            for roi in ROI_PLOT_ORDER:
                idx = roi_idx.get(roi)
                if idx is None or idx.size == 0:
                    continue
                roi_psd = psd[cond_mask][:, idx, :]
                roi_mean = np.mean(roi_psd, axis=(0, 1))
                roi_mean = roi_mean.astype(np.float64, copy=False)
                participant_roi_spectra[roi][condition] = roi_mean
                if freqs_ref is None or _freqs_match(freqs_ref, freqs):
                    aggregate_roi_spectra[roi][condition].append(roi_mean)
                else:
                    aggregate_roi_spectra[roi][condition].append(
                        np.interp(freqs_ref, freqs, roi_mean, left=np.nan, right=np.nan)
                    )

        if not plotted_labels:
            continue

        plotted_participants.append(participant)
        participant_condition_epoch_counts[participant] = participant_epoch_counts
        participant_title, participant_subtitle = _build_group_title(
            scope_label=participant,
            scenario_name=scenario_name,
            condition_epoch_counts={label: participant_epoch_counts[label] for label in plotted_labels},
            condition_participant_counts=None,
        )
        participant_png = out_dir / "single_participants" / f"{participant}_eeg_condition_psd.png"
        _plot_condition_spectra(
            roi_spectra_by_condition=participant_roi_spectra,
            freqs=freqs,
            condition_order=plotted_labels,
            out_path=participant_png,
            title=participant_title,
            subtitle=participant_subtitle,
        )
        single_participant_pngs[participant] = str(participant_png)
        participant_topomap_title, participant_topomap_subtitle = _build_group_title(
            scope_label=participant,
            scenario_name=scenario_name,
            condition_epoch_counts={label: participant_epoch_counts[label] for label in plotted_labels},
            condition_participant_counts=None,
            plot_label="EEG Band Power Topomaps by Condition",
        )
        participant_topomap_png = out_dir / "single_participants" / f"{participant}_eeg_condition_topomap.png"
        _plot_condition_topomaps(
            channel_spectra_by_condition=participant_channel_spectra,
            freqs=freqs,
            info=info,
            condition_order=plotted_labels,
            out_path=participant_topomap_png,
            title=participant_topomap_title,
            subtitle=participant_topomap_subtitle,
        )
        single_participant_topomap_pngs[participant] = str(participant_topomap_png)

    if group_info_ref is not None:
        roi_reference_title = "EEG Electrode ROI Reference | All participants"
        roi_reference_subtitle = f"scenario={scenario_name} | reference only, no PSD values"
        roi_reference_path = out_dir / "eeg_roi_reference_topomap.png"
        _plot_roi_reference_topomap(
            info=group_info_ref,
            out_path=roi_reference_path,
            title=roi_reference_title,
            subtitle=roi_reference_subtitle,
        )
        roi_reference_topomap_png = str(roi_reference_path)

    if freqs_ref is None or not plotted_participants:
        summary["reason"] = "no_participant_level_psd_plots_generated"
        summary["roi_reference_topomap_png"] = roi_reference_topomap_png
        summary["single_participant_pngs"] = single_participant_pngs
        summary["single_participant_topomap_pngs"] = single_participant_topomap_pngs
        summary["participant_condition_epoch_counts"] = participant_condition_epoch_counts
        manifest_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        return summary

    plotted_label_order = [
        label for label in label_order if any(len(aggregate_roi_spectra[roi].get(label, [])) > 0 for roi in ROI_PLOT_ORDER)
    ]
    all_roi_spectra: dict[str, dict[str, np.ndarray]] = {roi: {} for roi in ROI_PLOT_ORDER}
    all_channel_spectra: dict[str, np.ndarray] = {}
    for roi in ROI_PLOT_ORDER:
        for label in plotted_label_order:
            spectra = aggregate_roi_spectra[roi].get(label, [])
            if not spectra:
                continue
            all_roi_spectra[roi][label] = np.nanmean(np.stack(spectra, axis=0), axis=0).astype(np.float64, copy=False)
    for label in plotted_label_order:
        spectra = aggregate_channel_spectra.get(label, [])
        if not spectra:
            continue
        all_channel_spectra[label] = np.nanmean(np.stack(spectra, axis=0), axis=0).astype(np.float64, copy=False)

    group_title, group_subtitle = _build_group_title(
        scope_label="All participants",
        scenario_name=scenario_name,
        condition_epoch_counts={label: int(all_condition_epoch_counts[label]) for label in plotted_label_order},
        condition_participant_counts={label: int(all_condition_participant_counts[label]) for label in plotted_label_order},
    )
    all_participants_png = out_dir / "all_participants_eeg_condition_psd.png"
    _plot_condition_spectra(
        roi_spectra_by_condition=all_roi_spectra,
        freqs=freqs_ref,
        condition_order=plotted_label_order,
        out_path=all_participants_png,
        title=group_title,
        subtitle=group_subtitle,
    )
    all_participants_topomap_png: str | None = None
    if group_info_ref is not None and all_channel_spectra:
        group_topomap_title, group_topomap_subtitle = _build_group_title(
            scope_label="All participants",
            scenario_name=scenario_name,
            condition_epoch_counts={label: int(all_condition_epoch_counts[label]) for label in plotted_label_order},
            condition_participant_counts={
                label: int(all_condition_participant_counts[label]) for label in plotted_label_order
            },
            plot_label="EEG Band Power Topomaps by Condition",
        )
        topomap_path = out_dir / "all_participants_eeg_condition_topomap.png"
        _plot_condition_topomaps(
            channel_spectra_by_condition=all_channel_spectra,
            freqs=freqs_ref,
            info=group_info_ref,
            condition_order=plotted_label_order,
            out_path=topomap_path,
            title=group_topomap_title,
            subtitle=group_topomap_subtitle,
        )
        all_participants_topomap_png = str(topomap_path)

    summary.update(
        {
            "status": "ok",
            "reason": None,
            "all_participants_png": str(all_participants_png),
            "all_participants_topomap_png": all_participants_topomap_png,
            "roi_reference_topomap_png": roi_reference_topomap_png,
            "single_participant_pngs": single_participant_pngs,
            "single_participant_topomap_pngs": single_participant_topomap_pngs,
            "label_order_plotted": plotted_label_order,
            "condition_epoch_counts_all_participants": {
                label: int(all_condition_epoch_counts[label]) for label in plotted_label_order
            },
            "condition_participant_counts_all_participants": {
                label: int(all_condition_participant_counts[label]) for label in plotted_label_order
            },
            "participant_condition_epoch_counts": participant_condition_epoch_counts,
            "participants_plotted": plotted_participants,
            "n_participants_plotted": len(plotted_participants),
        }
    )
    manifest_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary
