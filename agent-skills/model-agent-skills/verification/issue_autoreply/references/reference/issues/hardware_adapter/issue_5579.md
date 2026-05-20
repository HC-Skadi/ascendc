# Issue #5579: [Kernel] Add moe_gating_top_k operator support for Ascend NPU

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

1.replace moe_gating_top_k from torch_npu with custom op
2.enable the  renorm function of moe_gating_top_k in softmax scenerio

### Does this PR introduce _any_ user-facing change?
No

### How was this patch tested?
No need test

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/7157596103666ee7ccb7008acee8bff8a8ff1731


## 基本信息
- **编号**: #5579
- **作者**: ZCG12345
- **创建时间**: 2026-01-04T07:37:53Z
- **关闭时间**: 2026-01-07T13:42:31Z
- **标签**: module:tests, module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5579)
