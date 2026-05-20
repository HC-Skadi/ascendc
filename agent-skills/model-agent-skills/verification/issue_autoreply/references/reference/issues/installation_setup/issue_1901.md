# Issue #1901: [Installation]: 源码安装0.9.2rc1，torch npu版本问题

## 基本信息

- **编号**: #1901
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1901
- **创建时间**: 2025-07-21T04:41:51Z
- **关闭时间**: 2025-07-21T07:02:55Z
- **更新时间**: 2025-12-23T11:44:47Z
- **提交者**: @PiratePai
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

ERROR: Could not find a version that satisfies the requirement torch-npu==2.5.1.post1.dev20250619 (from versions: 2.1.0.post8, 2.1.0.post10, 2.1.0.post12, 2.3.1.post2, 2.3.1.post4, 2.3.1.post6, 2.4.0, 2.4.0.post2, 2.4.0.post4, 2.5.1rc1, 2.5.1, 2.6.0rc1, 2.7.1rc1)
ERROR: No matching distribution found for torch-npu==2.5.1.post1.dev20250619
  error: subprocess-exited-with-error

### How you are installing vllm and vllm-ascend

# Install vLLM
git clone --depth 1 --branch v0.9.2 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install -v -e .
cd ..

# Install vLLM Ascend
git clone  --depth 1 --branch v0.9.2rc1 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -v -e .
cd ..
