# Issue #2191: [Release]: Release checklist for v0.9.1rc2

## 基本信息

- **编号**: #2191
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2191
- **创建时间**: 2025-08-04T04:27:28Z
- **关闭时间**: 2025-09-03T09:15:26Z
- **更新时间**: 2025-09-03T09:15:26Z
- **提交者**: @Yikun
- **评论数**: 5

## 标签

release

## 问题描述

### Release Checklist

**Release Version**: v0.9.1rc2
**Release Branch**: v0.9.1-dev
**Release Date**: 2025.08.05
**Release Manager**: @Yikun 


### Prepare Release Note

- [x] Create a new issue for release feedback: https://github.com/vllm-project/vllm-ascend/issues/1487
- [ ] Write the release note PR: https://github.com/vllm-project/vllm-ascend/pull/2188

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update version info in docs/source/community/versioning_policy.md

~~- [ ] Update contributor info in docs/source/community/contributors.md~~ Contributors will not updated in branch

  - [ ] Update package version in docs/conf.py


### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/pull/2199
- [x] https://github.com/vllm-project/vllm-ascend/pull/2188
- [x] https://github.com/vllm-project/vllm-ascend/pull/2227

### Functional Test
- [x] Accuracy test: https://github.com/vllm-project/vllm-ascend/actions/runs/16722260396?pr=2199
- [x] Qwen3 aclgraph + performance test
       - https://github.com/vllm-project/vllm-ascend/issues/2191#issuecomment-3149471360
- [x] DeepSeek V3 W8A8 DP4 + TP4 + EP @Potabk 
- [x] PD disaggregation @Potabk 
- [x] Qwen3 Moe + Aclgraph @shen-shanshan 
    - [x] Adding known issue: https://github.com/vllm-project/vllm-ascend/issues/2226
- [x] qwen deepseek W4A8 quantization @22dimensions 

### Doc Test

- [x] Tutorial is updated.
- [x] User Guide is updated.
- [x] Developer Guide is updated.

Sync doc on: https://github.com/vllm-project/vllm-ascend/pull/2227

### Prepare Artifacts

- [x] Docker image is ready.
- [x] Wheel package is ready.


### Release Step

- [x] Release note PR is merged.
- [x] Post the release on GitHub release page.
- [x] Generate official doc page on https://app.readthedocs.org/dashboard/
- [x] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [x] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [ ] Upload 310p wheel to Github release page
- [ ] Broadcast the release news (By message, blog , etc)
- [ ] Close this issue

