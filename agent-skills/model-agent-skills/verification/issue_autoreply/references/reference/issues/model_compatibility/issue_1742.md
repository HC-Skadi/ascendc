# Issue #1742: [Release]: Release checklist for v0.9.2rc1

## 基本信息

- **编号**: #1742
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1742
- **创建时间**: 2025-07-11T07:33:23Z
- **关闭时间**: 2025-07-15T03:56:37Z
- **更新时间**: 2025-07-16T07:14:02Z
- **提交者**: @wangxiyuan
- **评论数**: 8

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: 0.9.2rc1
**Release Branch**:  main
**Release Date**:  2025/07/11
**Release Manager**:  @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/1743
- [x] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/1725

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/pull/1734
- [x] https://github.com/vllm-project/vllm-ascend/pull/1725
- [x] https://github.com/vllm-project/vllm-ascend/pull/1140

### Functional Test

- [x] DeepSeek V3 W8A8 DP4 + TP4 + EP @Potabk 
- [x] PP @MengqingCao 
- [x] Qwen3 Moe + Aclgraph @shen-shanshan 


### Doc Test

- [x] Tutorial is updated.
- [x] User Guide is updated.
- [x] Developer Guide is updated.


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
- [x] Broadcast the release news (By message, blog , etc)
- [x] Close this issue

