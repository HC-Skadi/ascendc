# Issue #3097: [Bug]: A2 PD分离部署Deepseek-R1-w8a8时，MTP收益不达预期

## 基本信息

- **编号**: #3097
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3097
- **创建时间**: 2025-09-22T09:05:57Z
- **关闭时间**: 2025-09-23T07:34:27Z
- **更新时间**: 2025-09-23T07:34:27Z
- **提交者**: @Mitchellax
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

- OS: Ubuntu 5.16.20-2
- CPU：Intel Xeon Platinum 8480+ (224核 2NUMA)
- NPU: 910B2C x16
- 模型：DS-R1 0528 W8A8 MTP float

2P1D，四机共64卡，使用0.9.1-dev镜像部署。

### 🐛 Describe the bug

固定测试场景：3.5K/1.5K 共1000条数据，Request rate inf，max concurrency 100。

D节点上：
- 开启单算子下发，使用w8a8 MTP权重：P99 TTFT 5.4s，TPS/NPU 9.78；
- 开启图下发，使用w8a8 MTP权重，关闭MTP：P99 TTFT 4.9s，TPS/NPU 38.94；
- 开启图下发，使用float MTP权重，关闭MTP：P99 TTFT 4.8s，TPS/NPU 39.39；
- 开启图下发，使用float MTP权重，开启MTP：P99 TTFT 4.3s，TPS/NPU 42.67；

按照Output token throughput计算：开启MTP从696.50提高到756.48，提升幅度8.61%。

需确认MTP实现是否存在问题，D节点单卡并发很低，MTP提升幅度过小。
