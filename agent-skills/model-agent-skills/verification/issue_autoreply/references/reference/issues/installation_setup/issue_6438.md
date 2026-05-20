# Issue #6438: [Upgrade] Upgrade Mooncake to v0.3.8.post1

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
- Update MOONCAKE_TAG to v0.3.8.post1 in all Dockerfiles
- Update mooncake version in documentation tutorials
- Upgrade yalantinglibs from 0.5.5 to 0.5.6 in mooncake_installer.sh
- Add missing dependencies to mooncake_installer.sh:
  - apt-get: unzip, liburing-dev, libjemalloc-dev
  - yum: unzip, liburing-devel, jemalloc-devel


The prompt I was used:
> - Please help me ugprade mooncake version to 0.3.8.post1 include Dockerfile/docs and mooncake_installer.sh?
> - Please double check the deps in installer.sh, you can reference https://github.com/kvcache-ai/Mooncake/blob/v0.3.8.post1/dependencies.sh
> - unzip / liburing-dev / libjemalloc-dev doesn't be include in yum install section
> - commit the mooncake upgrade changes
> - add a condition to prevent pushing images when triggered by pull requests

### Does this PR introduce _any_ user-facing change?
Yes, docker image use the 

### How was this patch tested?

- vLLM version: v

## 基本信息
- **编号**: #6438
- **作者**: Yikun
- **创建时间**: 2026-01-30T10:33:10Z
- **关闭时间**: 2026-02-09T16:01:02Z
- **标签**: documentation, module:tools, ready, ready-for-test, merge-conflicts

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6438)
