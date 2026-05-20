# Issue #2173: [RFC]: Support multi-node serving in CI

## 基本信息

- **编号**: #2173
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2173
- **创建时间**: 2025-08-01T09:28:42Z
- **关闭时间**: 2025-12-31T02:33:56Z
- **更新时间**: 2025-12-31T02:33:56Z
- **提交者**: @pkking
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

Currently, all CI [workflows](https://github.com/vllm-project/vllm-ascend/tree/main/.github/workflows) run on a single Ascend server node, which limits the maximum available NPU count to 8 cards. 

But its impossible to test `multi-node` scenarios witch maybe more close to real world use case. 

This RFC aims to provide a solution that enables community developers to write test cases for multi-node vllm serving deployments.

### Proposed Change.

Since the community CI runs on a kubernetes cluster, there are many out-of-box `multi-node serving` solution, for example [lws](https://lws.sigs.k8s.io/) and in [vllm project](https://github.com/vllm-project/vllm) there's also [an example](https://docs.vllm.ai/en/stable/deployment/frameworks/lws.html) for reference, the straightforward idea is to build by [lws](https://lws.sigs.k8s.io/) directly, here's a general plan:
1. add a new workflow, which contains two jobs:
    1. job1: create a new lws instance which expose a vllm service with multi pods on seperatly node
    2. job2: wait the lws service is ready, then run the tests, job must cleanup the resource when tests finished
2. add some guides to help developer how to setup more `multi-node` style test cases

since `multi-node serving` may be time and NPU comsuming, It's best not to triggered by a PR

### Feedback Period.

Maybe one week

### CC List.

@Yikun @wangxiyuan @Potabk @MengqingCao 

### Any Other Things.

_No response_
