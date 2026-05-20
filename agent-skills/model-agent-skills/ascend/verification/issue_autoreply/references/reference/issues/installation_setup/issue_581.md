# Issue #581: [Doc]: Could not find a version that satisfies the requirement triton

## 基本信息

- **编号**: #581
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/581
- **创建时间**: 2025-04-19T13:25:53Z
- **关闭时间**: 2025-05-14T05:15:48Z
- **更新时间**: 2025-05-14T05:15:48Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

documentation

## 问题描述

### 📚 The doc issue

Failed to install vllm v0.8.4, installation doc should be fixed

https://vllm-ascend.readthedocs.io/en/latest/installation.html#setup-vllm-and-vllm-ascend

```
# Install vllm-project/vllm from pypi
pip install vllm==0.8.4
```
Raise the issue: 
```
ERROR: Could not find a version that satisfies the requirement triton==3.2.0; platform_machine != "ppc64le" (from vllm) (from versions: none)
ERROR: No matching distribution found for triton==3.2.0; platform_machine != "ppc64le"
```

Below command can works:
```
# Install vLLM
git clone --depth 1 --branch v0.8.4 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install . --extra-index https://download.pytorch.org/whl/cpu/
```

1. We'd better add a CI on upstream CI to protect the vLLM binary installation on aarch64/x86
2. We should also have a CI on vllm-ascend to validate the installation doc

### Suggest a potential alternative/fix

_No response_
