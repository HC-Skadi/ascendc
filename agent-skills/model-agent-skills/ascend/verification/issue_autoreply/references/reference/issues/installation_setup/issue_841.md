# Issue #841: [RFC]: P/D Disaggregation Support

## 基本信息

- **编号**: #841
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/841
- **创建时间**: 2025-05-14T02:17:14Z
- **关闭时间**: 2025-10-20T01:42:00Z
- **更新时间**: 2025-10-20T01:42:00Z
- **提交者**: @MengqingCao
- **评论数**: 0

## 标签

RFC

## 问题描述

### Motivation.

P/D Disaggregation plays a very important role in deploying vllm inference services in large-scale clusters. There is already a initial P/D Disaggregation support in vllm-ascend now, and we' ll continue to develop it with more parrallel mechanisms including tp, ep and dp, and graph mode integration, etc.

The related CI for 1p1d, xpyd scenarios will be integrated step by step, with or w/o parrallel mechanisms including tp, ep, dp, etc.

### Proposed Change.

#### P/D Disaggregation

- [ ] P/D Disaggregation in v0 
  - [x] https://github.com/vllm-project/vllm-ascend/pull/432
  - [ ] https://github.com/vllm-project/vllm-ascend/pull/694
  - [ ] https://github.com/vllm-project/vllm-ascend/pull/794
  - [ ] tutorials
    - [x] 1p1d + offline + single machine https://github.com/vllm-project/vllm-ascend/issues/857
- [ ] P/D Disaggregation in v1
  - [x] https://github.com/vllm-project/vllm-ascend/pull/684   issue: https://github.com/vllm-project/vllm-ascend/issues/605
  - [ ] #950 

#### CI Machine Preparation
- [x] https://github.com/vllm-project/vllm-ascend/pull/830

#### UT Integration

Feature coverage matrix
| P/D Disaggregation | tp   | ep   | dp   |
| ------------------ | ---- | ---- | ---- |
| 1p1d/xpyd          |      |      |      |
| 1p1d/xpyd          | √    |      |      |
| 1p1d/xpyd          | √    | √    |      |
| 1p1d/xpyd          | √    | √    | √    |
| 1p1d/xpyd          |      | √    |      |
| 1p1d/xpyd          |      | √    | √    |
| 1p1d/xpyd          |      |      | √    |

- [ ] Basic P/D Disaggregation w/o parrallel mechanisms.
- [ ] Adding the above parrallel mechanisms.
- [ ] Adding graph mode
