# Issue #5978: [Lint]Style: Convert `vllm-ascend/` to ruff format(Batch #3)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
**Scope of Changes**:
| File Path |
| :--- |
| `vllm_ascend/attention/mla_v1.py` |
| `vllm_ascend/attention/sfa_v1.py` |
| `vllm_ascend/core/recompute_scheduler.py` |
| `vllm_ascend/core/scheduler_dynamic_batch.py` |
| `vllm_ascend/distributed/device_communicators/npu_communicator.py` |
| `vllm_ascend/distributed/device_communicators/pyhccl.py` |
| `vllm_ascend/distributed/device_communicators/pyhccl_wrapper.py` |

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060


## 基本信息
- **编号**: #5978
- **作者**: MrZ20
- **创建时间**: 2026-01-18T08:24:27Z
- **关闭时间**: 2026-01-24T14:10:18Z
- **标签**: module:core

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5978)
