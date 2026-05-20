# Issue #1017: [Doc]: wrong torch version in developer guide - Optimization and Tuning

## 基本信息

- **编号**: #1017
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1017
- **创建时间**: 2025-05-29T13:41:36Z
- **关闭时间**: 2025-06-04T06:07:23Z
- **更新时间**: 2025-06-04T06:07:24Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

documentation

## 问题描述

### 📚 The doc issue

https://vllm-ascend.readthedocs.io/en/v0.7.3-dev/developer_guide/performance/optimization_and_tuning.html#install-optimized-torch-and-torch-npu

```diff
# Download prebuilt packages
- wget https://repo.oepkgs.net/ascend/pytorch/vllm/torch/torch-2.5.1-cp310-cp310-linux_aarch64.whl
- wget https://repo.oepkgs.net/ascend/pytorch/vllm/torch/torch_npu-2.5.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
+ wget https://repo.oepkgs.net/ascend/pytorch/vllm/torch/torch-2.5.1-cp311-cp311-linux_aarch64.whl
+ wget https://repo.oepkgs.net/ascend/pytorch/vllm/torch/torch_npu-2.5.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
```

```diff
- rm -rf /tmp/*
+ rm -rf /workspace/tmp/*
```
### Suggest a potential alternative/fix

_No response_
