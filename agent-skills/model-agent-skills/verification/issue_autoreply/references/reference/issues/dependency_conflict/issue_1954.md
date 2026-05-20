# Issue #1954: [Bug]: After applying the mindie_turbo to the vLLM-Ascend 0.7.3.post1 version, some inference results may lack content.

## 基本信息

- **编号**: #1954
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1954
- **创建时间**: 2025-07-23T04:44:28Z
- **关闭时间**: 2026-01-04T02:11:37Z
- **更新时间**: 2026-01-04T02:11:37Z
- **提交者**: @moxiaohei
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

v0.7.3 post1 image + mindie turbo:

quay.io/ascend/vllm-ascend:v0.7.3.post1-openeuler

pip install mindie_turbo


### 🐛 Describe the bug


```
Qwen3-30B may exhibit some inference results without content under high concurrency (the verification scenario is: 910B3 with 2 cards deployed running 40 concurrent instances on the open-source evaluation set GPQA). 
```
```
The issue was not reproduced after uninstalling mindie_turbo and running under the same scenario.
```
