# Issue #6556: [CI] v0.13.0 Make UT does not compile and run custom kernels examples

**类型**: Pull Request

## 问题背景
<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
1) Update the UT running CANN version to 8.5.0
2) Make UT without compiling custom kernels and without running custom kernels examples, as CANN 8.5.0 needs check Soc-Name during register_kernels while our UT is running without NPU hardware.

### Does this PR introduce _any_ user-facing change?
NA

### How was this patch tested?
Warning Log:
<img width="1647" height="25" alt="image" src="https://github.com/user-attachments/assets/48b56d6f-ecb5-42fc-9195-f25aa9460c4d" />

Tested on my local host without NPU:
<img width="854" height="151" alt="4a7b9f32-43bd-4fa5-beda-0f2e07ce6e9d" src="https://github.com/user-attachments/assets/5babb45c-a20c-4e71-a58d-3398358f2d7f" />


## 基本信息
- **编号**: #6556
- **作者**: leo-pony
- **创建时间**: 2026-02-05T06:50:54Z
- **关闭时间**: 2026-02-05T08:54:37Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6556)
