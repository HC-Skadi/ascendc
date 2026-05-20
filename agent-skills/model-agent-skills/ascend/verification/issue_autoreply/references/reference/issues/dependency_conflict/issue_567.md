# Issue #567: [Bug]: TYPE_CHECK doesn't work

## 基本信息

- **编号**: #567
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/567
- **创建时间**: 2025-04-18T04:23:38Z
- **关闭时间**: 2025-07-29T03:50:15Z
- **更新时间**: 2025-07-29T03:50:15Z
- **提交者**: @wangxiyuan
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

vllm-ascend main branch

### 🐛 Describe the bug

The mypy check since doesn't work with TYPE_CHECK, for example, take a look at this code
https://github.com/vllm-project/vllm-ascend/blob/66a0837963ff5dd6734907083ca3cf57e6bb223b/vllm_ascend/attention/attention.py#L41

if add TYPE_CHECK here, mypy check will raise error. So the PR https://github.com/vllm-project/vllm-ascend/pull/563  removed this check.

we should find a solution to fix the problem: enable TYPE_CHECK and let mypy happy
