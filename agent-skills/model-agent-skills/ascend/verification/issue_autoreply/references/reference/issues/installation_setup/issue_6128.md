# Issue #6128: [bugfix][npugraph_ex]fix static kernel uninstall issue

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

The static kernel in torch_npu is uninstalled through Python's atexit mechanism.
However, in vllm-ascend, when inference ends or the service stops, the worker process is terminated. This way, ending the process does not trigger the atexit mechanism, causing the static kernel not to be unloaded.
When using the nougraph_ex backend and enabling the static kernel, we registered a signal handler to explicitly unload the static kernel.
When there are many static kernels, unloading usually takes some time, whereas vllm will directly kill the process after sending a terminate event. Therefore, we choose to handle it by starting a new process.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6128
- **作者**: ChenCangtao
- **创建时间**: 2026-01-22T07:58:53Z
- **关闭时间**: 2026-01-26T07:03:18Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6128)
