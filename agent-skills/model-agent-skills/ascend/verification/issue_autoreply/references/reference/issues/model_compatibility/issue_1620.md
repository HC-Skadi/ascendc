# Issue #1620: [Feature]: Enable V1 by default and cleanup V0 code

## 基本信息

- **编号**: #1620
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1620
- **创建时间**: 2025-07-03T16:56:04Z
- **关闭时间**: 2025-12-23T12:47:16Z
- **更新时间**: 2025-12-23T12:47:16Z
- **提交者**: @Yikun
- **评论数**: 4

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch
After 0.9.2rc1, v0 code will be removed from vllm-ascend. This issue list the todo list.

## Prepare
- [x] Enable V1 by default follow: https://github.com/vllm-project/vllm/pull/19792/commits/5a7f6a7f45f5e7d2b403c5df7050109b05bc6518
- [x] Release v0.9.2rc1
## todo list
- [x] Cleanup all docs and test related to V0 https://github.com/vllm-project/vllm-ascend/pull/1733
- [x] Cleanup VLLM_USE_V1 in function code https://github.com/vllm-project/vllm-ascend/pull/1764
- [x] Cleanup all benchmark, accuracy test, long-term test, pd test, doc test  CI V0 code #1805  
- [ ] Cleanup all code related to V0 in function code @shen-shanshan 
   - [x] Cleanup v0 worker #1821
   - [x] Cleanup v0 model_runner #1823
   - [x] Cleanup multi step worker #1809 
   - [x] Cleanup multi step model_runner #1820
   - [x] Cleanup draft_model_runner #1810 
   - [x] Cleanup  pooling_model_runner #1824
   - [x] Cleanup v0 attention #1835 
   - [x] Cleanup v0 patch
   - [x] Cleanup V0 PD code https://github.com/vllm-project/vllm-ascend/pull/2047
   - [x] Cleanup V0 custom ops #1871
   - [ ] Rename all v1 file, for example rename `worker_v1` to `worker`.
   - [ ] Rename related code following vllm, for example `prompt_adapter`
      - #1878
      - https://github.com/orgs/vllm-project/projects/25
### Alternatives

_No response_

### Additional context

_No response_
