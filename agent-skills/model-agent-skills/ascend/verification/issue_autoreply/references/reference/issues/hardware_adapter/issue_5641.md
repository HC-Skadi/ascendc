# Issue #5641: [Feat] Integrate FIA operator in mla_cp._forward_decode

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Replace the npu_multi_head_latent_attention with FIA operator in mla_cp.py _forward_decode.
Adjust mla_attn_dpc_pcp in acl_graph.py
### Does this PR introduce _any_ user-facing change?
no
### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5641
- **作者**: 845473182
- **创建时间**: 2026-01-06T08:05:37Z
- **关闭时间**: 2026-01-22T12:02:31Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5641)
