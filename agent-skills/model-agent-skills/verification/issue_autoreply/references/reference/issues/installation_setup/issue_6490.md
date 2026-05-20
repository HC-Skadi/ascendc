# Issue #6490: [Feature]:   integrate Qwen3-Asr

**类型**: Issue

## 问题背景
### 🚀 The feature, motivation and pitch

When integrating Qwen3-Asr into vllm-ascend, the following error occurred. We have already converted the model to float16, why is this error still being reported? I don't know where the bfloat16 comes from....

the vllm-ascend is the latest, use the offcie docker images is [v0.14.0rc1.](vllm-ascend:v0.14.0rc1-310p)

clNN_Parameter_Error(EZ1001): Io input dtype or format is not supported, get io input info is x(DT_BFLOAT16, ND) gamma(DT_BFLOAT16, ND) yOut(DT_BFLOAT16, ND) rstdOut(DT_FLOAT, ND) but supported list is:

### Alternatives

_No response_

### Additional context

_No response_

## 基本信息
- **编号**: #6490
- **作者**: lixikun
- **创建时间**: 2026-02-02T12:22:02Z
- **关闭时间**: 2026-02-03T06:20:53Z
- **标签**: feature request

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/6490)
