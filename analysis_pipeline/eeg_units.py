from __future__ import annotations

from typing import Any

import numpy as np


EEG_P95_ABS_SANITY_THRESHOLD_V = 1e-2
MICROVOLT_TO_VOLT = 1e-6


def _center_by_channel(data: np.ndarray) -> np.ndarray:
    arr = np.asarray(data, dtype=np.float64)
    if arr.ndim == 1:
        return arr - np.nanmedian(arr)
    if arr.ndim == 2:
        return arr - np.nanmedian(arr, axis=1, keepdims=True)
    lead_dim = arr.shape[0]
    reshaped = arr.reshape(lead_dim, -1)
    centered = reshaped - np.nanmedian(reshaped, axis=1, keepdims=True)
    return centered.reshape(arr.shape)


def infer_eeg_scale_to_volts(
    data: np.ndarray,
    *,
    p95_abs_sanity_threshold_v: float = EEG_P95_ABS_SANITY_THRESHOLD_V,
) -> dict[str, Any]:
    centered = _center_by_channel(data)
    finite = np.abs(centered[np.isfinite(centered)])
    if finite.size == 0:
        return {
            "input_unit_inferred": "unknown",
            "scale_factor_to_volts": 1.0,
            "scale_applied": False,
            "demeaned_p95_abs_input": None,
            "demeaned_p95_abs_output_volts": None,
        }

    p95_abs_input = float(np.nanpercentile(finite, 95))
    scale_factor = 1.0
    input_unit = "V"
    if p95_abs_input > float(p95_abs_sanity_threshold_v):
        scale_factor = MICROVOLT_TO_VOLT
        input_unit = "uV"

    return {
        "input_unit_inferred": input_unit,
        "scale_factor_to_volts": float(scale_factor),
        "scale_applied": bool(scale_factor != 1.0),
        "demeaned_p95_abs_input": p95_abs_input,
        "demeaned_p95_abs_output_volts": float(p95_abs_input * scale_factor),
    }


def ensure_eeg_data_in_volts(
    data: np.ndarray,
    *,
    p95_abs_sanity_threshold_v: float = EEG_P95_ABS_SANITY_THRESHOLD_V,
) -> tuple[np.ndarray, dict[str, Any]]:
    info = infer_eeg_scale_to_volts(
        data,
        p95_abs_sanity_threshold_v=p95_abs_sanity_threshold_v,
    )
    scale_factor = float(info["scale_factor_to_volts"])
    if scale_factor == 1.0:
        return data, info

    arr = np.asarray(data)
    scaled = (arr.astype(np.float64, copy=False) * scale_factor).astype(arr.dtype, copy=False)
    return scaled, info
