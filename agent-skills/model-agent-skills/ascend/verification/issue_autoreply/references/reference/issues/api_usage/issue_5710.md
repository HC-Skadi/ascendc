# Issue #5710: [Bug]: vllm-ascend 0.11.0 does not compatible with vllm 0.11.0 for mismatch of pytorch version

## 基本信息

- **编号**: #5710
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5710
- **创建时间**: 2026-01-08T03:17:47Z
- **关闭时间**: 2026-01-16T08:11:20Z
- **更新时间**: 2026-01-16T08:11:20Z
- **提交者**: @iambowen
- **评论数**: 8

## 标签

question

## 问题描述

### Your current environment

Ascend-NPU  910B Single card , within docker runtime.

### 🐛 Describe the bug

<details>
when installing vllm & vllm-ascend with version 0.11.0, it comes up with following error:
<img width="1719" height="392" alt="Image" src="https://github.com/user-attachments/assets/e554fe3e-bf31-4ff6-b07f-d0c1e9c2e690" />

The failure is clear, my question is whether vllm-ascend has the same release version of vllm, if so ,why not put the same vllm version in requirements and remove torch dependency, if not so, what's the corresponding vllm version for vllm-ascend 0.11.0?


</details>

