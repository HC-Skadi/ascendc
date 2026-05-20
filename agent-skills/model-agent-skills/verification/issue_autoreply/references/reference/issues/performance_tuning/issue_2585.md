# Issue #2585: [Release]: Release checklist for v0.9.1

## 基本信息

- **编号**: #2585
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2585
- **创建时间**: 2025-08-28T01:35:18Z
- **关闭时间**: 2025-09-11T10:45:16Z
- **更新时间**: 2025-09-11T10:45:16Z
- **提交者**: @wangxiyuan
- **评论数**: 13

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.9.1
**Release Branch**:  v0.9.1-dev
**Release Date**: 2025/08/30
**Release Manager**:  @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/2643
- [x] Write the release note PR. #2646 （should backport to 0.9.1-dev branch then）

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

we should make sure all 0.9.1-dev related PR is done. https://github.com/vllm-project/vllm-ascend/pulls?page=1&q=is%3Apr+is%3Aopen+base%3Av0.9.1-dev

Merge/Close/Keep as it is(should leave the reason here)

TO be merge:
- [x] https://github.com/vllm-project/vllm-ascend/pull/2595
- [x] #2648 
- [x] #2647 
- [x] #2645
- [x] https://github.com/vllm-project/vllm-ascend/pull/2659
- [x] https://github.com/vllm-project/vllm-ascend/pull/2665
- [x] https://github.com/vllm-project/vllm-ascend/pull/2657

Fix in post1 release later:
- [ ] https://github.com/vllm-project/vllm-ascend/pull/2656
- [ ] https://github.com/vllm-project/vllm-ascend/pull/2654

### Functional Test

we should make sure 0.9.1 is well tested. The core function is:

- [x] PD disaggreagate with LLMDatadist @Potabk 
- [x] aclgraph @MengqingCao 
- [x] spec decode @wxsIcey Ngram, MTP works. Eagle doesn't work.
- [x] guided decode @shen-shanshan 
- [x] quantization @22dimensions 
- [x] vlm @zhangxinyuehfad 
- [x] rlhf @leo-pony 
- [x] loar @wxsIcey 
- [x] ascend scheduler @wxsIcey 


### Doc Test

- [x] Tutorial is updated.
- [x] User Guide is updated.
- [x] Developer Guide is updated.
- [x] Check V1 env in 0.9.1-dev branch


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

