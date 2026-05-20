# Issue #278: [CI]: Cleanup lock if job failaure

## 基本信息

- **编号**: #278
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/278
- **创建时间**: 2025-03-08T10:49:29Z
- **关闭时间**: 2025-04-09T16:37:30Z
- **更新时间**: 2025-04-09T16:37:31Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

ci/build

## 问题描述

### Anything you want to discuss about vllm on ascend.

https://github.com/vllm-project/vllm-ascend/actions/runs/13735695396/job/38419168376

We perhaps want to remove the lock after job failure, maybe:
https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/running-scripts-before-or-after-a-job

Workaround:
```
ssh root@ascend-ci-arm64
rm -f /tmp/dispatch.lock
```
