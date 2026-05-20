# Issue #4807: [Release]: Release checklist for v0.11.0

## 基本信息

- **编号**: #4807
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4807
- **创建时间**: 2025-12-09T01:05:45Z
- **关闭时间**: 2025-12-19T01:35:37Z
- **更新时间**: 2025-12-19T01:35:37Z
- **提交者**: @wangxiyuan
- **评论数**: 5

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.11.0
**Release Branch**:  v0.11.0-dev
**Release Date**: 2025.12.16
**Release Manager**:  @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/4808
- [x] Upgrade vllm version to the new version for CI and Dockerfile
- [x] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/4918

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md (Getting Started and Branch section)

  - [x] Update version info in docs/source/community/versioning_policy.md(Release compatibility matrix, Release window and Branch states section)

  - [ ] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/pull/4777
- [x] https://github.com/vllm-project/vllm-ascend/pull/4721
- [x] https://github.com/vllm-project/vllm-ascend/pull/4153


### Functional Test

- [x] Deepseek v3.1/R1 @Potabk 
- [x] Qwen3 Moe/dense @zhangxinyuehfad 
- [x] Qwen3-next @wxsIcey 
- [x] Qwen2.5/3-VL @shen-shanshan 
- [x] Deepseek3.2 @menogrey 
- [x] embeding @MengqingCao 


### Doc Test

- [ ] Tutorial is updated.
- [ ] User Guide is updated.
- [ ] Developer Guide is updated. https://github.com/vllm-project/vllm-ascend/pull/5060


### Prepare Artifacts

- [ ] Docker image is ready.
- [ ] Wheel package is ready.


### Release Step

- [ ] Release note PR is merged.
- [ ] Post the release on GitHub release page.
- [x] Generate official doc page on https://app.readthedocs.org/dashboard/
- [ ] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [ ] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [x] Upload 310p wheel to Github release page
- [ ] Broadcast the release news (By message, blog , etc)
- [ ] Close this issue

