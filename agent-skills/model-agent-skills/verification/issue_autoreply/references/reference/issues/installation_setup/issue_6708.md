# Issue #6708: [CI] Refactor to speedup image building and CI Installation

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. Refactor  image workflow using cache-from to speedup builds
![build](https://github.com/user-attachments/assets/02135c12-0069-44f8-a3ec-5c2b4282448a)

Simultaneously refactored all Dockerfiles by placing layers that rarely change before those that change frequently, improving build cache hit rate.

2. Refactor E2E test using vllm-ascend container images, to skip C compile while no C code are changed
![e2e](https://github.com/user-attachments/assets/49f5b166-0df3-41e1-8f71-b3bbbed17cfd)

In this case, the job will only replace the source code of vllm-ascend and install `requirements-dev.txt`, saving about 10min before tests

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/9562912cead1f11e8540fb91306c5cbda66f0007


## 基本信息
- **编号**: #6708
- **作者**: wjunLu
- **创建时间**: 2026-02-11T14:19:46Z
- **关闭时间**: 2026-02-28T01:06:00Z
- **标签**: ci/build, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6708)
