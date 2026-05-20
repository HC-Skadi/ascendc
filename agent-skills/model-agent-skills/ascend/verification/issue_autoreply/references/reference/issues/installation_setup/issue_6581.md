# Issue #6581: [BugFix] Add support for rotary_dim parameter when using partial rope in rotary_embedding

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Issue: If a model such as Ling-1T adopts partial rotary position embedding (partial RoPE), but config.json uses the rotary_dim parameter instead of partial_rotary_factor, it will trigger a RuntimeError: The expanded size of the tensor (128) must match the existing size (64) at non-singleton dimension 3.
<img width="1681" height="472" alt="image" src="https://github.com/user-attachments/assets/ba03d7df-ecba-4d6f-9ec1-4dc55f59799e" />

This PR addresses an issue where models using partial rotary position embedding (partial RoPE) with the `rotary_dim` parameter in `config.json` (instead of `partial_rotary_factor`) would encounter a `RuntimeError`.

This change adds support for the `rotary_dim` parameter in `vllm_ascend/ops/rotary_embedding.py` to correctly calculate the `rope_dim`, resolving the tensor size mismatch error.

### Does this PR introduce _any_ user-facing change?

No.

### How was this patch tested?

The patch was tested s

## 基本信息
- **编号**: #6581
- **作者**: GoCHug
- **创建时间**: 2026-02-05T16:12:13Z
- **关闭时间**: 2026-02-09T09:17:52Z
- **标签**: module:ops

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6581)
