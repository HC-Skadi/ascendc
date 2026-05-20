# Issue #100: ImportError when using v0.7.1-dev branch (36e9d6e) - Circular import in register function

## 基本信息

- **编号**: #100
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/100
- **创建时间**: 2025-02-19T07:03:53Z
- **关闭时间**: 2025-02-19T08:00:37Z
- **更新时间**: 2025-02-19T08:00:37Z
- **提交者**: @ApsarasX
- **评论数**: 3

## 标签

无

## 问题描述

I encountered an ImportError when switching from the main branch to the v0.7.1-dev branch (commit 36e9d6e). The error occurs specifically when trying to import AscendQuantConfig in register function.

**Steps to Reproduce:**

1. Checkout to v0.7.1-dev branch: git checkout 36e9d6e
2. Attempt to launch model using vLLM
3. Observe ImportError

**Expected Behavior:**
Successful model initialization without import errors, consistent with main branch behavior.

**Actual Behavior:**
Received error:
```
ImportError: cannot import name 'AscendQuantConfig' from partially initialized module 'vllm_ascend.quantization.quant_config' (most likely due to a circular import)
```
