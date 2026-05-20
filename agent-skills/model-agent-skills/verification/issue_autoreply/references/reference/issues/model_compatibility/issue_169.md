# Issue #169: [Feature]: 适配swift框架的GRPO训练流程

## 基本信息

- **编号**: #169
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/169
- **创建时间**: 2025-02-26T03:11:54Z
- **关闭时间**: 2025-03-06T03:08:11Z
- **更新时间**: 2025-03-06T03:08:12Z
- **提交者**: @dawnranger
- **评论数**: 1

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch

[swift](https://github.com/modelscope/ms-swift)是一个流行的LLM训练框架，支持对LLM/VLM模型进行GRPO训练。但是我在基于vllm_ascend框架进行GRPO训练的时候，发现训练流程会失败。定位到可能是由于vllm_ascend推理问题导致GRPO的推理部分超时导致。需要进一步进行定位

具体问题参考issue: https://github.com/modelscope/ms-swift/issues/3272


### Additional context

相关issue: https://github.com/modelscope/ms-swift/issues/3241
