# Issue #1147: [RFC]: Refactoring AscendFusedMoE

## 基本信息

- **编号**: #1147
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1147
- **创建时间**: 2025-06-10T02:38:22Z
- **关闭时间**: 2025-06-17T09:49:04Z
- **更新时间**: 2025-06-17T09:49:04Z
- **提交者**: @zzzzwwjj
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

This RFC proposes optimize AscendFusedMoE‘s implemention, change branch's condition, simplfy code and make it easier to maintain and develop.

### Current problem
1. Chaotic branch conditions
Currently there are three implementation for AscendFusedMoE: all_gather, all2all and mc2, and different implementation need to be matched with different communication-op. Some communication operators still have usage restrictions.
2. Relative code locations are not together
Some codes of fused_moe are in deepseek_v2.py, some are in fused_moe.py & w8a8_dynamic.py.
3. The optimal performance scenarios for A2 and A3 are different, and it has not been considered yet.

### Proposed Change.

1. Integrate branch conditions
We will implement a global function to choose AscendFusedMoE’s implemention, based on ep_size, with_prefill and soc_version.
2. Move all codes of fused_moe to fused_moe.py

### Feedback Period.

_No response_

### CC List.

@Yikun @wangxiyuan @ganyi1996ppo @jianzs 

### Any Other Things.

Recently I will push some PRs to resolve this issue.
