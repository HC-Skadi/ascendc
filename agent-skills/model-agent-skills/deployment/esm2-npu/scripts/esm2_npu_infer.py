#!/usr/bin/env python3
"""ESM-2 NPU 基础推理脚本 (README Quick Start 适配)"""
import time
import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
import esm


def main():
    print("=" * 60)
    print("ESM-2 Inference on Ascend NPU")
    print("=" * 60)

    device_name = torch.npu.get_device_name(0)
    print(f"NPU Device: {device_name}")
    print(f"torch version: {torch.__version__}")
    print(f"torch_npu version: {torch_npu.__version__}")

    print("\n[1/4] Loading ESM-2 model (esm2_t33_650M_UR50D)...")
    t0 = time.time()
    model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
    batch_converter = alphabet.get_batch_converter()
    model.eval()
    model = model.cuda()
    load_time = time.time() - t0
    print(f"  Model loaded in {load_time:.2f}s")

    data = [
        ("protein1", "MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG"),
        ("protein2", "KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE"),
        ("protein2 with mask", "KALTARQQEVFDLIRD<mask>ISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE"),
        ("protein3", "K A <mask> I S Q"),
    ]

    print("\n[2/4] Preparing data...")
    batch_labels, batch_strs, batch_tokens = batch_converter(data)
    batch_lens = (batch_tokens != alphabet.padding_idx).sum(1)
    batch_tokens = batch_tokens.cuda()
    print(f"  Batch shape: {batch_tokens.shape}")
    print(f"  Sequences: {len(data)}")

    print("\n[3/4] Running inference...")
    with torch.no_grad():
        _ = model(batch_tokens, repr_layers=[33], return_contacts=True)
    torch.npu.synchronize()

    t0 = time.time()
    num_runs = 5
    for _ in range(num_runs):
        with torch.no_grad():
            results = model(batch_tokens, repr_layers=[33], return_contacts=True)
        torch.npu.synchronize()
    infer_time = (time.time() - t0) / num_runs
    print(f"  Average inference time ({num_runs} runs): {infer_time:.4f}s")

    token_representations = results["representations"][33]

    print("\n[4/4] Results:")
    for i, (tokens_len, (label, seq)) in enumerate(zip(batch_lens, data)):
        rep = token_representations[i, 1 : tokens_len - 1].mean(0)
        print(f"  {label}: seq_len={tokens_len.item()}, embedding_shape={rep.shape}, "
              f"embedding_norm={rep.norm().item():.4f}")

    contacts = results["contacts"]
    print(f"\n  Contact map shape: {contacts.shape}")
    print(f"  Logits shape: {results['logits'].shape}")

    mem_allocated = torch.npu.memory_allocated(0) / 1024**2
    mem_reserved = torch.npu.memory_reserved(0) / 1024**2
    print(f"\n  NPU Memory: allocated={mem_allocated:.1f}MB, reserved={mem_reserved:.1f}MB")
    print(f"  Model load time: {load_time:.2f}s")
    print(f"  Avg inference time: {infer_time:.4f}s")
    print("\nESM-2 NPU inference completed successfully!")


if __name__ == "__main__":
    main()
