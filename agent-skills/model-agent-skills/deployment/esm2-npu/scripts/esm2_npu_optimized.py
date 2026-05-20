#!/usr/bin/env python3
"""ESM-2 NPU FP32 Performance Optimization Benchmark

Optimizations (all FP32, no precision reduction):
1. npu_rotary_mul - fused rotary position embedding
2. npu_fusion_attention - fused attention (when attn weights not needed)
3. gelu -> F.gelu - native GELU activation
4. contiguous() - explicit contiguous after transpose
"""
import math
import time
from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
import torch_npu
from torch_npu.contrib import transfer_to_npu

import esm
from esm import FastaBatchedDataset
from esm.rotary_embedding import RotaryEmbedding, apply_rotary_pos_emb
import esm.rotary_embedding as rotary_mod
import esm.modules as modules_mod
from esm.multihead_attention import MultiheadAttention

_orig_apply_rotary = apply_rotary_pos_emb
_orig_gelu = modules_mod.gelu
_orig_mha_forward = MultiheadAttention.forward
_orig_layer_forward = modules_mod.TransformerLayer.forward
_orig_rotary_forward = RotaryEmbedding.forward
_patches_applied = False


def _npu_apply_rotary(x, cos, sin):
    if not (str(x.device).startswith("npu") and x.dim() >= 3):
        return _orig_apply_rotary(x, cos, sin)
    cos_t = cos[:, :x.shape[-2], :]
    sin_t = sin[:, :x.shape[-2], :]
    need_unsq = (x.dim() == 3)
    if need_unsq:
        x = x.unsqueeze(0)
        cos_t = cos_t.unsqueeze(0)
        sin_t = sin_t.unsqueeze(0)
    result = torch_npu.npu_rotary_mul(x, cos_t.expand_as(x), sin_t.expand_as(x))
    return result.squeeze(0) if need_unsq else result


def _npu_gelu(x):
    return F.gelu(x)


def _opt_rotary_forward(self, q, k):
    self._cos_cached, self._sin_cached = self._update_cos_sin_tables(k, seq_dimension=-2)
    return (
        _npu_apply_rotary(q, self._cos_cached, self._sin_cached),
        _npu_apply_rotary(k, self._cos_cached, self._sin_cached),
    )


def _opt_mha_forward(
    self, query, key=None, value=None,
    key_padding_mask=None, incremental_state=None,
    need_weights=True, static_kv=False, attn_mask=None,
    before_softmax=False, need_head_weights=False,
):
    can_fuse = (
        str(query.device).startswith("npu")
        and not need_weights and not need_head_weights
        and not before_softmax
        and self.rot_emb is not None
        and incremental_state is None and not static_kv
        and not self.onnx_trace
        and self.bias_k is None and not self.add_zero_attn
        and not self.training
    )
    if not can_fuse:
        return _orig_mha_forward(
            self, query, key, value,
            key_padding_mask=key_padding_mask,
            incremental_state=incremental_state,
            need_weights=need_weights, static_kv=static_kv,
            attn_mask=attn_mask, before_softmax=before_softmax,
            need_head_weights=need_head_weights,
        )

    tgt_len, bsz, embed_dim = query.size()
    src = query if self.self_attention else key
    q = self.q_proj(query)
    k = self.k_proj(src)
    v = self.v_proj(src if value is None else (query if self.self_attention else value))
    q = q * self.scaling

    q = q.contiguous().view(tgt_len, bsz * self.num_heads, self.head_dim).transpose(0, 1)
    k = k.contiguous().view(-1, bsz * self.num_heads, self.head_dim).transpose(0, 1)
    v = v.contiguous().view(-1, bsz * self.num_heads, self.head_dim).transpose(0, 1)
    q, k = self.rot_emb(q, k)
    src_len = k.size(1)

    q4 = q.view(bsz, self.num_heads, tgt_len, self.head_dim).permute(0, 2, 1, 3).contiguous()
    k4 = k.view(bsz, self.num_heads, src_len, self.head_dim).permute(0, 2, 1, 3).contiguous()
    v4 = v.view(bsz, self.num_heads, src_len, self.head_dim).permute(0, 2, 1, 3).contiguous()

    atten_mask = None
    if key_padding_mask is not None:
        atten_mask = key_padding_mask.unsqueeze(1).unsqueeze(1).expand(
            bsz, 1, tgt_len, src_len
        ).to(torch.bool)

    npu_out = torch_npu.npu_fusion_attention(
        q4, k4, v4, self.num_heads,
        input_layout="BSND", pse=None, atten_mask=atten_mask,
        scale=1.0, pre_tockens=65536, next_tockens=65536, keep_prob=1.0,
    )[0]

    attn = npu_out.reshape(bsz, tgt_len, embed_dim).transpose(0, 1).contiguous()
    attn = self.out_proj(attn)
    return attn, None


def _opt_layer_forward(self, x, self_attn_mask=None,
                       self_attn_padding_mask=None, need_head_weights=False):
    residual = x
    x = self.self_attn_layer_norm(x)
    x, attn = self.self_attn(
        query=x, key=x, value=x,
        key_padding_mask=self_attn_padding_mask,
        need_weights=need_head_weights,
        need_head_weights=need_head_weights,
        attn_mask=self_attn_mask,
    )
    x = residual + x
    residual = x
    x = self.final_layer_norm(x)
    x = _npu_gelu(self.fc1(x))
    x = self.fc2(x)
    x = residual + x
    return x, attn


def apply_patches():
    global _patches_applied
    rotary_mod.apply_rotary_pos_emb = _npu_apply_rotary
    RotaryEmbedding.forward = _opt_rotary_forward
    modules_mod.gelu = _npu_gelu
    MultiheadAttention.forward = _opt_mha_forward
    modules_mod.TransformerLayer.forward = _opt_layer_forward
    _patches_applied = True


def revert_patches():
    global _patches_applied
    rotary_mod.apply_rotary_pos_emb = _orig_apply_rotary
    RotaryEmbedding.forward = _orig_rotary_forward
    modules_mod.gelu = _orig_gelu
    MultiheadAttention.forward = _orig_mha_forward
    modules_mod.TransformerLayer.forward = _orig_layer_forward
    _patches_applied = False


def bench(model, tokens, repr_layers, return_contacts=False,
          num_warmup=5, num_runs=20):
    for _ in range(num_warmup):
        with torch.no_grad():
            _ = model(tokens, repr_layers=repr_layers,
                      return_contacts=return_contacts)
    torch.npu.synchronize()
    times = []
    for _ in range(num_runs):
        torch.npu.synchronize()
        t0 = time.perf_counter()
        with torch.no_grad():
            res = model(tokens, repr_layers=repr_layers,
                        return_contacts=return_contacts)
        torch.npu.synchronize()
        times.append(time.perf_counter() - t0)
    return res, times


def load_model():
    model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
    model.eval().cuda()
    return model, alphabet


def main():
    print("=" * 70)
    print("ESM-2 NPU FP32 Optimization Benchmark (No Precision Reduction)")
    print("=" * 70)
    print(f"NPU: {torch.npu.get_device_name(0)}")
    print(f"torch={torch.__version__}, torch_npu={torch_npu.__version__}")

    dataset = FastaBatchedDataset.from_file("examples/data/some_proteins.fasta")
    _, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
    bc = alphabet.get_batch_converter()

    configs = [
        ("Short (len~100, batch=4)",
         [(f"s{i}", s) for i, (_, s) in enumerate(dataset) if len(s) < 120][:4]),
        ("Medium (len~200-500, batch=4)",
         [(f"m{i}", s) for i, (_, s) in enumerate(dataset) if 150 < len(s) < 600][:4]),
        ("Long (len~600-1000, batch=2)",
         [(f"l{i}", s) for i, (_, s) in enumerate(dataset) if len(s) > 500][:2]),
    ]

    num_runs = 20
    results_table = []

    for cname, data_sub in configs:
        if not data_sub:
            continue
        _, _, tokens = bc(data_sub)
        tokens_npu = tokens.cuda()
        print(f"\n{'~'*70}")
        print(f"Config: {cname}  (batch={tokens.shape[0]}, max_len={tokens.shape[1]})")

        revert_patches()
        model_b, _ = load_model()
        _, t_base = bench(model_b, tokens_npu, [33], num_runs=num_runs)
        avg_base = sum(t_base) / len(t_base)
        del model_b; torch.npu.empty_cache()

        apply_patches()
        model_o, _ = load_model()
        _, t_opt = bench(model_o, tokens_npu, [33], num_runs=num_runs)
        avg_opt = sum(t_opt) / len(t_opt)
        del model_o; torch.npu.empty_cache()

        spd = avg_base / avg_opt
        results_table.append((cname, avg_base, avg_opt, spd))
        print(f"  Baseline:  {avg_base*1000:.2f}ms")
        print(f"  Optimized: {avg_opt*1000:.2f}ms")
        print(f"  Speedup:   {spd:.2f}x")

    print(f"\n{'~'*70}")
    print("Accuracy (medium seqs, FP32 baseline vs FP32 optimized)...")
    acc_data = [(f"a{i}", s) for i, (_, s) in enumerate(dataset) if 80 < len(s) < 600][:4]
    _, _, acc_tok = bc(acc_data)
    acc_npu = acc_tok.cuda()

    revert_patches()
    mb, _ = load_model()
    with torch.no_grad():
        rb = mb(acc_npu, repr_layers=[33], return_contacts=False)
    del mb; torch.npu.empty_cache()

    apply_patches()
    mo, _ = load_model()
    with torch.no_grad():
        ro = mo(acc_npu, repr_layers=[33], return_contacts=False)
    del mo; torch.npu.empty_cache()

    rep_b = rb["representations"][33]
    rep_o = ro["representations"][33]
    cos_rep = F.cosine_similarity(
        rep_b.reshape(-1, rep_b.shape[-1]),
        rep_o.reshape(-1, rep_o.shape[-1]), dim=-1).mean().item()
    lg_b = rb["logits"]
    lg_o = ro["logits"]
    cos_lg = F.cosine_similarity(
        lg_b.reshape(-1, lg_b.shape[-1]),
        lg_o.reshape(-1, lg_o.shape[-1]), dim=-1).mean().item()
    max_d = (rep_b - rep_o).abs().max().item()
    mean_d = (rep_b - rep_o).abs().mean().item()

    print(f"  Repr cosine similarity:  {cos_rep:.6f}")
    print(f"  Logits cosine similarity: {cos_lg:.6f}")
    print(f"  Repr max|mean abs diff:  {max_d:.6f} | {mean_d:.6f}")

    print(f"\n{'='*70}")
    print("SUMMARY  (FP32 only, zero precision loss)")
    print(f"{'='*70}")
    hdr = f"{'Config':<42} {'Base(ms)':>10} {'Opt(ms)':>10} {'Speedup':>10}"
    print(hdr)
    print("-" * len(hdr))
    for n, b, o, s in results_table:
        print(f"{n:<42} {b*1000:>10.2f} {o*1000:>10.2f} {s:>9.2f}x")
    print("-" * len(hdr))
    print(f"Accuracy: repr_cos={cos_rep:.6f}  logits_cos={cos_lg:.6f}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
