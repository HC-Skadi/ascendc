# Issue #156: [RFC]: Add support for custom ops

## 基本信息

- **编号**: #156
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/156
- **创建时间**: 2025-02-25T03:16:55Z
- **关闭时间**: 2025-04-10T09:15:43Z
- **更新时间**: 2025-04-10T09:15:44Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

feature request

## 问题描述

### Motivation.

Currently:

**vLLM** supports a variety of custom ops by.

- Triton ops: https://github.com/vllm-project/vllm/tree/main/vllm/lora/ops/triton_ops
- Torch native ops: https://github.com/vllm-project/vllm/tree/main/vllm/lora/ops/torch_ops
- Custom ops via torch bindings:
https://github.com/vllm-project/vllm/blob/cdc1fa12eb1ba4795d24e97dcffa2018668a9267/csrc/torch_bindings.cpp#L480
- 3rd party Lib: https://github.com/vllm-project/vllm/blob/cdc1fa12eb1ba4795d24e97dcffa2018668a9267/vllm/attention/backends/flashinfer.py#L12

**vLLM Ascend** current (v0.7.1rc1) supports torch native ops (with torch npu), the whole workflow like: `vllm --> torch --> torch_npu --> atb ---> cann`, but in this way:
1. the devs should have to first implements the ops in atb
2. then exposed to torch_npu
3. upgrade `torch_npu` to latest version as dependency.
4. finally, users can use the ops.

The lengthy version matching and upgrade process discourages developers from implementing the Ascend operator.


### Proposed Change.

This RFC aims to smooth out the complicated process for ops development and make everything clear and simple. It can also help Ascend developers to create ops with better collaboration.

This RFC is going to start with exploring custom ops support via two ways:

1. AscendCL (aclnn)
2. AscendC

We propose to support custom ops via [torch bindings](https://github.com/vllm-project/vllm/blob/cdc1fa12eb1ba4795d24e97dcffa2018668a9267/csrc/torch_bindings.cpp) to archive this goal.

Work items:
- Custom Ops framework for vLLM Ascend 
- A real ops implements with CI passed
- A turtorial to help users understand how to develop the custom ops

### Feedback Period.

now - 2025.03.06

### CC List.

cc @wangxiyuan
cc @ganyi1996ppo 

### Any Other Things.

Ready in 2025 Q1 (vLLM Ascend first release v1.7.3)
