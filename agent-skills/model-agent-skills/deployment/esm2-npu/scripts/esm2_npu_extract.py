#!/usr/bin/env python3
"""ESM-2 NPU Embedding 批量提取脚本 (extract.py 适配)

用法: 将此文件放到 ESM 仓库根目录后运行。
可修改 sys.argv 中的参数适配不同的模型/FASTA/输出目录。
"""
import sys
import time
import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu

from scripts.extract import create_parser, run

if __name__ == "__main__":
    sys.argv = [
        "extract.py",
        "esm2_t33_650M_UR50D",
        "examples/data/some_proteins.fasta",
        "examples/data/some_proteins_emb_esm2",
        "--repr_layers", "0", "32", "33",
        "--include", "mean", "per_tok",
    ]
    parser = create_parser()
    args = parser.parse_args()
    print("Running extract.py on NPU...")
    t0 = time.time()
    run(args)
    elapsed = time.time() - t0
    print(f"\nExtraction completed in {elapsed:.2f}s")
