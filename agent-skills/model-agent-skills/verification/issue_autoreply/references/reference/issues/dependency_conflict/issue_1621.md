# Issue #1621: Significant inference speed difference between vllm-ascend and MindIE

## 基本信息

- **编号**: #1621
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1621
- **创建时间**: 2025-07-04T02:24:49Z
- **关闭时间**: 2025-07-15T02:08:16Z
- **更新时间**: 2025-07-15T02:08:17Z
- **提交者**: @Fly-Pluche
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

Environment: Two machines, each with 8 * Ascend910B-64GB GPUs.

MindIE image: mindie_2.0.T18.B010-800I-A2-py3.11-openeuler24.03-lts-aarch64

Vllm-ascend image: 0.8.5rc1-torch_npu2.5.1-cann8.1.rc1-python3.10-oe2203lts

Model weights: DeepSeek-V3-0324-w8a8-modelers (https://modelers.cn/models/Modelers_Park/DeepSeek-V3-0324-w8a8/tree/main)


### Describe the problem

When testing inference speeds using different inference frameworks. 

Inference speeds observed:
vllm-ascend: Approximately 1.4 Tokens/s
MindIE: Approximately 14 Tokens/s
