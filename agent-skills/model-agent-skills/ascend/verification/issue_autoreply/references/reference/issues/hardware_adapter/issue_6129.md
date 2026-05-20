# Issue #6129: [Lint]Style: Convert `vllm-ascend/` to ruff format(Batch #8)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
**Scope of Changes**:
| File Path |
| :--- |
| vllm_ascend/ops/\_\_init\_\_.py |
| vllm_ascend/ops/activation.py |
| vllm_ascend/ops/flashcomm2_oshard_manager.py |
| vllm_ascend/ops/layernorm.py |
| vllm_ascend/ops/mla.py |
| vllm_ascend/ops/mm_encoder_attention.py |
| vllm_ascend/ops/register_custom_ops.py |
| vllm_ascend/ops/vocab_parallel_embedding.py |
| vllm_ascend/ops/weight_prefetch.py |
| vllm_ascend/spec_decode/\_\_init\_\_.py |
| vllm_ascend/spec_decode/eagle_proposer.py |
| vllm_ascend/spec_decode/interface.py |
| vllm_ascend/spec_decode/mtp_proposer.py |
| vllm_ascend/spec_decode/ngram_proposer.py |
| vllm_ascend/spec_decode/suffix_proposer.py |

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6129
- **作者**: MrZ20
- **创建时间**: 2026-01-22T08:02:27Z
- **关闭时间**: 2026-02-06T07:25:08Z
- **标签**: module:ops

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6129)
