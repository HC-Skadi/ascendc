# Issue #3143: [Bug]: PD分离，性能测试时有小部分请求卡在D节点上waiting不处理

## 基本信息

- **编号**: #3143
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3143
- **创建时间**: 2025-09-24T07:00:17Z
- **关闭时间**: 2025-10-11T03:06:42Z
- **更新时间**: 2025-10-11T03:06:42Z
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

性能测试时发现最后有一个或多个请求一直没有返回，测试无法结束。

D实例上存在`Running: 0 reqs, Waiting: 1 reqs`。

卡上AICore有负载30%，但客户端侧无返回。服务端无报错。
