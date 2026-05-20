# Issue #342: [Installation]:

## 基本信息

- **编号**: #342
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/342
- **创建时间**: 2025-03-17T03:47:43Z
- **关闭时间**: 2025-03-17T03:52:29Z
- **更新时间**: 2025-03-17T03:52:29Z
- **提交者**: @yungongzi
- **评论数**: 0

## 标签

installation

## 问题描述

### Your current environment

```text

```


### How you are installing vllm and vllm-ascend

```sh
git clone --depth 1 --branch v0.7.3 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install . --extra-index https://download.pytorch.org/whl/cpu/
```

