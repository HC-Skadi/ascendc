# Issue #868: [Misc]: Why not `AscendMLAImpl` just inherit `MLACommonImpl` for common functions?

## 基本信息

- **编号**: #868
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/868
- **创建时间**: 2025-05-15T07:33:10Z
- **关闭时间**: 2025-07-13T09:06:46Z
- **更新时间**: 2025-07-13T09:06:46Z
- **提交者**: @learning-chip
- **评论数**: 2

## 标签

question

## 问题描述

`class AscendMLAImpl` inherits the abstract `MLAAttentionImpl`: 
https://github.com/vllm-project/vllm-ascend/blob/v0.8.5rc1/vllm_ascend/attention/mla_v1.py#L263

However most functions like `_v_up_proj_and_o_proj` and `_q_proj_and_k_up_proj` are already defined in `MLACommonImpl`, and they look identical to the re-definition in `AscendMLAImpl`:
https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/attention/backends/mla/common.py#L1009

For example, `TritonMLAImpl` just reuses those common functions, but overwrites `_forward_decode`:
https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/attention/backends/triton_mla.py#L26

`AscendMLAImpl` can also just inherits `MLACommonImpl` and overwrite `_forward_prefill` and `_forward_decode` to use NPU operators?

