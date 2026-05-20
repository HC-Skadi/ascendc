# Issue #3099: [Bug]: PD分离下首token由D节点返回，TTFT偏高

## 基本信息

- **编号**: #3099
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3099
- **创建时间**: 2025-09-22T09:27:05Z
- **关闭时间**: 2026-01-05T06:10:59Z
- **更新时间**: 2026-01-05T06:10:59Z
- **提交者**: @Mitchellax
- **评论数**: 0

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

在 PD 分离下，PD Proxy 的代码逻辑为：P 节点完成推理后，需等待 D 节点完成一个token 后，由 D 节点将首 token 返回。相比 PD 混部场景，该机制导致 TTFT 天然偏高。

P 节点完成 Prefill 后，首 token 应直接由 P 节点返回，无需等待 D 节点。
