# Issue #3431: [CI]: Fix doctest ci for main release

## 基本信息

- **编号**: #3431
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3431
- **创建时间**: 2025-10-14T00:22:06Z
- **关闭时间**: 2025-11-13T01:19:28Z
- **更新时间**: 2025-11-13T01:19:28Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

documentation

## 问题描述

### 📚 The doc issue

we should change this:

https://github.com/vllm-project/vllm-ascend/blob/4f6d60eb067996fbf08b95f797916d978bf98f19/tests/e2e/doctests/002-pip-binary-installation-test.sh#L49

to

```
# Install vLLM
git clone --depth 1 --branch v0.11.0rc3 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install -v -e .
cd ..
```

First fix this and doc, and recover this once v0.11.1rc1 release

### Suggest a potential alternative/fix

_No response_
