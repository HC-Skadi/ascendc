# Issue #1309: [RFC]: Support Altlas 300I series

## 基本信息

- **编号**: #1309
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1309
- **创建时间**: 2025-06-20T03:54:30Z
- **关闭时间**: 2025-07-13T15:55:10Z
- **更新时间**: 2025-07-13T15:55:10Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

RFC

## 问题描述

### Motivation.

Support Altlas 310P series

### Proposed Change.

**Stage1: E2E workflow work**
- [x] Support Altlas 310P series: https://github.com/vllm-project/vllm-ascend/pull/914
    - [ ] qwen2.5-7b-instruct
    - [ ] qwen2.5-0.5b
    - [ ] qwen3-0.6B
    - [ ] qwen3-4B
    - [ ] qwen3-8B
- [ ] Enable 310P CI
    - [ ] Enable `linux-arm64-310-static-8` runner
- [ ] Enable e2e test
    - [ ] qwen3-0.6B
    - [ ] qwen2.5-0.5b
- [x] Add 310P dockerfile and image publish 
- [ ] Wheel should also support 310P (Maybe --no-binary?)
- [ ] E2E model test for 310P related models
- [x] Documentation for 310P support

**Stage2: Performance improvement**

### Feedback Period.

_No response_

### CC List.

cc @leo-pony

### Any Other Things.

_No response_
