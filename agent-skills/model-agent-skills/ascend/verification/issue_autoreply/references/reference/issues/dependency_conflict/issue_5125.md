# Issue #5125: [Bug]: 昇腾910B部署模型后，测试时出现精度下降问题

## 基本信息

- **编号**: #5125
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5125
- **创建时间**: 2025-12-17T07:36:51Z
- **关闭时间**: 2025-12-25T01:56:04Z
- **更新时间**: 2025-12-25T01:56:04Z
- **提交者**: @ZhihuaH
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

vllm-ascend:v0.11.0
ascendai/cann:8.3.rc2-910b-ubuntu22.04-py3.11

### 🐛 Describe the bug

vllm serve model_path --tensor-parallel-size 4

大家可以使用任意数据进行测试，均会出现准确度下降的情况。
相较于Transformers离线推理，准确率下降了接近5倍。

如果采用英伟达的卡进行部署，那么准确率没有问题。
