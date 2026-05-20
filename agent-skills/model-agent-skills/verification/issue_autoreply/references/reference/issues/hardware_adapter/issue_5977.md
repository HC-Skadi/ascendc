# Issue #5977: [Lint]Style: Convert `vllm-ascend/` to ruff format(Batch #2)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
**Scope of Changes**:
| File Path |
| :--- |
| `vllm_ascend/attention/attention_mask.py` |
| `vllm_ascend/attention/attention_v1.py` |
| `vllm_ascend/attention/context_parallel/attention_cp.py` |
| `vllm_ascend/attention/context_parallel/common_cp.py` |
| `vllm_ascend/attention/context_parallel/mla_cp.py` |
| `vllm_ascend/attention/utils.py` |
| `vllm_ascend/batch_invariant.py` |
| `vllm_ascend/device/device_op.py` |
| `vllm_ascend/device_allocator/camem.py` |
| `vllm_ascend/envs.py` |

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060


## 基本信息
- **编号**: #5977
- **作者**: MrZ20
- **创建时间**: 2026-01-18T04:27:26Z
- **关闭时间**: 2026-01-19T00:59:46Z
- **标签**: module:core

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5977)
