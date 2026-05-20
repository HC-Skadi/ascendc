#!/usr/bin/env python3

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = ROOT / "cases"
GOLDEN_FILE = ROOT / "golden/prelu_expect.py"

DTYPE_CONFIG = {
    # "float16": {"threshold": [0.001, 0.001], "label": "float16"},
    "float32": {"threshold": [0.0001, 0.0001], "label": "float32"},
    # "bfloat16": {"threshold": [0.008, 0.008], "label": "bfloat16"},
}

SCENARIO = {
    "name": "mixed_sign",
    "x_range": [-10.0, 10.0],
    "weight_range": [-5.0, 5.0],
}

MINIMAL_CASE_MATRIX = [
    # dtype,     shape_tag,             x_shape,     weight_type,   weight_shape, scenario,       note
    ("float16", "2d_scalar_tail",       [1, 17],     "scalar",      [1],          "mixed_sign",   "fp16 scalar direct + tail"),
    ("float16", "pc_inner32_aligned",   [2, 3, 32],  "per_channel", [3],          "mixed_sign",   "Prelu<T> Duplicate branch"),
    ("float32", "scalar_aligned",       [8, 32],     "scalar",      [1],          "mixed_sign",   "fp32 scalar direct"),
    ("float32", "2d_pc_tail",           [2, 33],     "per_channel", [33],         "mixed_sign",   "dim1 channel + SetValue + fp32 tail"),
]

BALANCED_SHAPES = [
    # shape_tag,             x_shape,       weight_type,   weight_shape, note
    ("2d_scalar_short_tail", [1, 17],       "scalar",      [1],          "scalar + DataCopyPad tail"),
    ("2d_scalar_aligned",    [8, 32],       "scalar",      [1],          "scalar aligned"),
    ("2d_scalar_tail",       [8, 3, 33],    "scalar",      [1],          "scalar rank3 tail"),
    ("2d_pc_inner32",        [2, 3, 32],    "per_channel", [3],          "per-channel Duplicate branch"),
    ("3d_pc_inner33_tail",   [2, 3, 33],    "per_channel", [3],          "per-channel unaligned total tail"),
    ("4d_pc_inner35",        [1, 4, 5, 7],  "per_channel", [4],          "rank4 per-channel SetValue branch"),
    ("2d_pc_tail",           [2, 33],       "per_channel", [33],         "dim1 per-channel tail"),
]

STRESS_CASE_MATRIX = [
    # dtype,     shape_tag,              x_shape,         weight_type,   weight_shape, scenario,     note
    ("float16",  "large_pc_inner513",    [32, 16, 513],   "per_channel", [16],         "mixed_sign", "multi-core fp16 per-channel tail"),
    ("float32",  "large_scalar_tail",    [1, 4097],       "scalar",      [1],          "mixed_sign", "multi-core fp32 scalar tail"),
]

LARGE_SHAPES = [
    # shape_tag,                  x_shape,          weight_type,   weight_shape, note
    ("large_2d_scalar_tail",      [8, 4097],        "scalar",      [1],          "large scalar + non-32B tail"),
    ("large_3d_pc_inner512",      [16, 32, 512],    "per_channel", [32],         "large per-channel aligned inner"),
    ("large_4d_pc_inner1089",     [4, 16, 33, 33],  "per_channel", [16],         "large rank4 per-channel unaligned inner"),
]

SCALAR_SHAPES = [
    # shape_tag,                  x_shape,          weight_type, weight_shape, note
    ("scalar_2d_1elem",           [1, 1],           "scalar",    [1],          "minimum valid rank2 scalar"),
    ("scalar_2d_short_tail",      [1, 17],          "scalar",    [1],          "small non-32B tail"),
    ("scalar_2d_one_block",       [1, 16],          "scalar",    [1],          "one 32B block for fp16/bf16"),
    ("scalar_2d_fp32_one_block",  [1, 8],           "scalar",    [1],          "one 32B block for fp32"),
    ("scalar_2d_aligned",         [8, 32],          "scalar",    [1],          "aligned baseline"),
    ("scalar_2d_block_minus1",    [1, 127],         "scalar",    [1],          "below scalar core policy block boundary"),
    ("scalar_2d_block_exact",     [1, 128],         "scalar",    [1],          "exact scalar core policy boundary for fp32"),
    ("scalar_2d_block_plus1",     [1, 129],         "scalar",    [1],          "above scalar core policy boundary with tail"),
    ("scalar_3d_inner31_tail",    [2, 3, 31],       "scalar",    [1],          "rank3 odd inner tail"),
    ("scalar_3d_inner32",         [2, 3, 32],       "scalar",    [1],          "rank3 aligned inner"),
    ("scalar_3d_inner33_tail",    [2, 3, 33],       "scalar",    [1],          "rank3 one element past alignment"),
    ("scalar_4d_inner35_tail",    [1, 4, 5, 7],     "scalar",    [1],          "rank4 unaligned inner"),
    ("scalar_4d_aligned",         [2, 4, 8, 8],     "scalar",    [1],          "rank4 aligned baseline"),
]

SCALAR_LARGE_SHAPES = [
    # shape_tag,                  x_shape,          weight_type, weight_shape, note
    ("scalar_large_2d_4095_tail", [1, 4095],        "scalar",    [1],          "large scalar below aligned block"),
    ("scalar_large_2d_4096",      [1, 4096],        "scalar",    [1],          "large scalar aligned"),
    ("scalar_large_2d_4097_tail", [1, 4097],        "scalar",    [1],          "large scalar non-32B tail"),
    ("scalar_large_batch_tail",   [8, 4097],        "scalar",    [1],          "larger batch non-32B tail"),
    ("scalar_large_3d_aligned",   [16, 32, 128],    "scalar",    [1],          "multi-core rank3 aligned"),
    ("scalar_large_3d_tail",      [16, 32, 129],    "scalar",    [1],          "multi-core rank3 tail"),
    ("scalar_large_4d_aligned",   [4, 16, 32, 32],  "scalar",    [1],          "multi-core rank4 aligned"),
    ("scalar_large_4d_tail",      [4, 16, 33, 33],  "scalar",    [1],          "multi-core rank4 odd inner tail"),
]

CHANNEL_INNER_SHAPES = [
    # shape_tag,                x_shape,         weight_type,   weight_shape, note
    ("pc_c3_inner1024",         [8, 3, 1024],    "per_channel", [3],          "small C, aligned large inner"),
    ("pc_c3_inner4097_tail",    [2, 3, 4097],    "per_channel", [3],          "small C, very large non-32B tail"),
    ("pc_c31_inner512",         [4, 31, 512],    "per_channel", [31],         "C just below 32-core boundary"),
    ("pc_c32_inner512",         [4, 32, 512],    "per_channel", [32],         "C aligned at 32-core boundary"),
    ("pc_c33_inner511_tail",    [4, 33, 511],    "per_channel", [33],         "C just above 32-core boundary with tail"),
    ("pc_c63_inner257_tail",    [2, 63, 257],    "per_channel", [63],         "C just below 64 with odd inner"),
    ("pc_c64_inner257_tail",    [2, 64, 257],    "per_channel", [64],         "C aligned at 64 with odd inner"),
    ("pc_c65_inner255_tail",    [2, 65, 255],    "per_channel", [65],         "C just above 64 with odd inner"),
    ("pc_c127_inner129_tail",   [2, 127, 129],   "per_channel", [127],        "C just below 128 with odd inner"),
    ("pc_c128_inner129_tail",   [2, 128, 129],   "per_channel", [128],        "C aligned at 128 with odd inner"),
    ("pc_c129_inner127_tail",   [2, 129, 127],   "per_channel", [129],        "C just above 128 with odd inner"),
    ("pc_c256_inner64",         [1, 256, 64],    "per_channel", [256],        "large aligned C with small aligned inner"),
    ("pc_c257_inner63_tail",    [1, 257, 63],    "per_channel", [257],        "large irregular C with small inner"),
    ("pc_c512_inner32",         [1, 512, 32],    "per_channel", [512],        "very large aligned C with small aligned inner"),
    ("pc_c511_inner33_tail",    [1, 511, 33],    "per_channel", [511],        "very large irregular C with non-32B inner"),
]

CHANNEL_SCALAR_SHAPES_COMMON = [
    # shape_tag,                    x_shape,         weight_type,   weight_shape, note
    ("pc_c255_inner63_tail",        [1, 255, 63],    "per_channel", [255],        "below large-C sch2 threshold"),
    ("pc_c256_inner63_tail",        [1, 256, 63],    "per_channel", [256],        "large-C sch2 threshold with non-32B inner"),
    ("pc_c257_inner7_tail",         [1, 257, 7],     "per_channel", [257],        "short inner mostly scalar fallback"),
    ("pc_n2_c257_inner63_tail",     [2, 257, 63],    "per_channel", [257],        "batch crossing with non-32B inner"),
    ("pc_n3_c257_inner63_tail",     [3, 257, 63],    "per_channel", [257],        "tile boundary stress with non-32B inner"),
    ("pc_c511_inner33_tail",        [1, 511, 33],    "per_channel", [511],        "large irregular C with non-32B inner"),
    ("pc_c512_inner32",             [1, 512, 32],    "per_channel", [512],        "aligned large-C baseline"),
]

CHANNEL_SCALAR_DTYPE_SHAPES = {
    "float32": [
        ("pc_c257_inner8_aligned",  [1, 257, 8],     "per_channel", [257],        "float32 32B-aligned inner"),
        ("pc_c257_inner9_tail",     [1, 257, 9],     "per_channel", [257],        "float32 one element past 32B alignment"),
    ],
    "float16": [
        ("pc_c257_inner16_aligned", [1, 257, 16],    "per_channel", [257],        "float16 32B-aligned inner"),
        ("pc_c257_inner17_tail",    [1, 257, 17],    "per_channel", [257],        "float16 one element past 32B alignment"),
    ],
}

CHANNEL_SCALAR_LARGE_SHAPES = [
    # shape_tag,                    x_shape,          weight_type,   weight_shape, note
    ("pc_n8_c257_inner63_tail",     [8, 257, 63],     "per_channel", [257],        "larger batch with non-16-aligned C and non-32B inner"),
    ("pc_n8_c511_inner33_tail",     [8, 511, 33],     "per_channel", [511],        "larger batch for current worst irregular C tail"),
    ("pc_n8_c512_inner32",          [8, 512, 32],     "per_channel", [512],        "larger batch aligned C and aligned inner baseline"),
    ("pc_n4_c1023_inner33_tail",    [4, 1023, 33],    "per_channel", [1023],       "very large non-16-aligned C with non-32B inner"),
    ("pc_n4_c1024_inner32",         [4, 1024, 32],    "per_channel", [1024],       "very large aligned C baseline"),
    ("pc_n8_c257_inner65_tail",     [8, 257, 65],     "per_channel", [257],        "inner just outside sch2 small-inner gate"),
    ("pc_n4_c257_inner127_tail",    [4, 257, 127],    "per_channel", [257],        "larger inner outside sch2 small-inner gate"),
    ("pc_n8_c263_inner63_tail",     [8, 263, 63],     "per_channel", [263],        "prime-like non-16-aligned C"),
    ("pc_n8_c271_inner63_tail",     [8, 271, 63],     "per_channel", [271],        "non-16-aligned C near 256"),
    ("pc_n8_c319_inner63_tail",     [8, 319, 63],     "per_channel", [319],        "non-16-aligned C below 320"),
    ("pc_n8_c513_inner31_tail",     [8, 513, 31],     "per_channel", [513],        "non-16-aligned C with short odd inner"),
    ("pc_n8_c527_inner33_tail",     [8, 527, 33],     "per_channel", [527],        "non-16-aligned C above 512"),
]

CASE_SUITES = {
    "minimal": MINIMAL_CASE_MATRIX,
    "balanced": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in BALANCED_SHAPES
    ],
    "stress": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in BALANCED_SHAPES
    ]
    + STRESS_CASE_MATRIX,
    "large": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in LARGE_SHAPES
    ],
    "scalar": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in SCALAR_SHAPES
    ],
    "scalar_large": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in SCALAR_LARGE_SHAPES
    ],
    "channel_inner": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in CHANNEL_INNER_SHAPES
    ],
    "channel_scalar": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in (
            CHANNEL_SCALAR_SHAPES_COMMON + CHANNEL_SCALAR_DTYPE_SHAPES[dtype]
        )
    ],
    "channel_scalar_large": [
        (dtype, shape_tag, shape, weight_type, weight_shape, SCENARIO["name"], note)
        for dtype in DTYPE_CONFIG
        for shape_tag, shape, weight_type, weight_shape, note in CHANNEL_SCALAR_LARGE_SHAPES
    ],
}

CASE_SUITES["scaler"] = CASE_SUITES["scalar"]
CASE_SUITES["scaler_large"] = CASE_SUITES["scalar_large"]


def make_tensor_desc(name, dtype, shape, value_range):
    return {
        "name": name,
        "format": "ND",
        "data_type": dtype,
        "param_type": "required",
        "shape": shape,
        "data_path": "",
        "value_range": value_range,
    }


def make_output_desc(dtype, shape):
    return {
        "name": "y",
        "format": "ND",
        "data_type": dtype,
        "param_type": "required",
        "shape": shape,
        "data_path": "",
        "golden_path": "",
        "err_threshold": DTYPE_CONFIG[dtype]["threshold"],
    }


def make_case(expect_name, input_x_name, dtype, shape_tag, shape, weight_type, weight_shape, scenario_name):
    case_name = f"{DTYPE_CONFIG[dtype]['label']}_{shape_tag}_{scenario_name}_{weight_type}"
    return {
        "case_name": case_name,
        "op_name": "Prelu",
        "case_path": str(ROOT),
        "expect_func": f"{GOLDEN_FILE}:{expect_name}",
        "input_desc": [
            make_tensor_desc(input_x_name, dtype, shape, SCENARIO["x_range"]),
            make_tensor_desc("weight", dtype, weight_shape, SCENARIO["weight_range"]),
        ],
        "output_desc": [make_output_desc(dtype, shape)],
        "attr_desc": [],
    }


def selected_cases():
    suite_value = os.environ.get("CASE_SUITE") or os.environ.get("CASE_SUITES", "balanced")
    suites = [suite.strip() for suite in suite_value.split(",") if suite.strip()]
    invalid_suites = [suite for suite in suites if suite not in CASE_SUITES]
    if invalid_suites:
        raise ValueError(
            f"CASE_SUITE/CASE_SUITES must be a comma-separated list of {sorted(CASE_SUITES)}, "
            f"got invalid suite(s): {invalid_suites!r}"
        )

    dtype_filter = os.environ.get("DTYPE_FILTER", "")
    weight_filter = os.environ.get("WEIGHT_TYPE_FILTER", "")
    tag_filter = os.environ.get("SHAPE_TAG_FILTER", "")

    for suite in suites:
        for dtype, shape_tag, shape, weight_type, weight_shape, scenario_name, _ in CASE_SUITES[suite]:
            if dtype_filter and dtype != dtype_filter:
                continue
            if weight_filter and weight_type != weight_filter:
                continue
            if tag_filter and shape_tag != tag_filter:
                continue
            yield dtype, shape_tag, shape, weight_type, weight_shape, scenario_name


def generate_cases():
    custom_cases = []
    builtin_cases = []
    for dtype, shape_tag, shape, weight_type, weight_shape, scenario_name in selected_cases():
        custom_cases.append(
            make_case("prelu_custom_expect", "x", dtype, shape_tag, shape, weight_type, weight_shape, scenario_name)
        )
        builtin_cases.append(
            make_case(
                "prelu_builtin_expect", "self", dtype, shape_tag, shape, weight_type, weight_shape, scenario_name
            )
        )
    return custom_cases, builtin_cases


def main():
    CASE_DIR.mkdir(parents=True, exist_ok=True)
    custom_cases, builtin_cases = generate_cases()
    (CASE_DIR / "prelu_custom_cases.json").write_text(json.dumps(custom_cases, indent=2) + "\n", encoding="utf-8")
    (CASE_DIR / "prelu_builtin_cases.json").write_text(json.dumps(builtin_cases, indent=2) + "\n", encoding="utf-8")
    print(f"generated custom cases: {len(custom_cases)}")
    print(f"generated builtin cases: {len(builtin_cases)}")


if __name__ == "__main__":
    main()
