# Issue #5229: [Release]: Release checklist for v0.13.0rc1

## 基本信息

- **编号**: #5229
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5229
- **创建时间**: 2025-12-22T03:59:08Z
- **关闭时间**: 2025-12-29T03:40:58Z
- **更新时间**: 2025-12-29T03:40:58Z
- **提交者**: @MengqingCao
- **评论数**: 6

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.13.0rc1
**Release Branch**: main
**Release Date**: 
**Release Manager**: @MengqingCao 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/5333
- [x] Upgrade vllm version to the new version for CI and Dockerfile
- [ ] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/5334

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md (Getting Started and Branch section)

  - [x] Update version info in docs/source/community/versioning_policy.md(Release compatibility matrix, Release window and Branch states section)

  - [ ] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [x] #5272 
- [x] #5270 
- [x] #5308
- [x] #5397 
- [x] #5402
- [x] https://github.com/vllm-project/vllm-ascend/pull/5417

Qwen3-Next related
- [x] #4595
- [x] #5274 
- [x] #5322

DeepSeek related
- [x] #5317

CP related
- [x] #5340 

Doc on cp
- [x] #5358 
- [x] #5343
- [x] #5364 
- [x] #5372 

### Functional Test

We focus on the **accuracy** and **performance**, both require **no regression**, in the core scenarios (_A2/A3 + async_scheduler + full graph/piecewise graph + Disaggregated Prefill + dp + tp + ep + shared expert dp + mtp/eagle3..._) on the following models:
- [x] deepseek v3.2
- [x] deepseek v3/r1 
- [x] Qwen3-Next
- [x] Qwen3-235B



### Doc Test

- [x] Tutorial is updated.
  - [x] Best performance turtorial doc for ds v3.2 #5373
  - [x] Best performance turtorial doc for ds v3/r1 #5383 @GDzhu01 
  - [x] Best performance turtorial doc for Qwen3-235B #5323 @Angazenn 
  - [x] Best performance turtorial doc for Qwen3-Next #5391 @SunnyLee151064 
  - [x] Double check the dsv3.2 doc is updated: https://github.com/vllm-project/vllm-ascend/issues/4969 @Potabk 
- [x] User Guide is updated.
- [x] Developer Guide is updated.


### Prepare Artifacts

- [x] Docker image is ready.
- [ ] Wheel package is ready.


### Release Step

- [x] Release note PR is merged.
- [x] Post the release on GitHub release page.
- [ ] Generate official doc page on https://app.readthedocs.org/dashboard/
- [ ] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [x] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [ ] Upload 310p wheel to Github release page
- [x] Broadcast the release news (By message, blog , etc)
- [x] Close this issue

