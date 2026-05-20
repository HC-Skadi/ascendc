# Issue #3141: [Release]: Release checklist for v0.11.0rc1

## 基本信息

- **编号**: #3141
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3141
- **创建时间**: 2025-09-24T03:15:23Z
- **关闭时间**: 2025-10-24T07:01:36Z
- **更新时间**: 2025-10-24T07:01:36Z
- **提交者**: @wangxiyuan
- **评论数**: 5

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.11.0rc1
**Release Branch**:  main
**Release Date**:  during 0924-0928
**Release Manager**:  @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/3222
- [x] Upgrade vllm version to the new version for CI and Dockerfile https://github.com/vllm-project/vllm-ascend/issues/3213
- [ ] Write the release note PR. https://github.com/vllm-project/vllm-ascend/issues/3224

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/pull/3163
- [x] https://github.com/vllm-project/vllm-ascend/pull/3153
- [x] https://github.com/vllm-project/vllm-ascend/pull/3191
- [x] https://github.com/vllm-project/vllm-ascend/pull/3142
- [x] https://github.com/vllm-project/vllm-ascend/pull/3187
- [x] https://github.com/vllm-project/vllm-ascend/pull/3220
- [x] https://github.com/vllm-project/vllm-ascend/pull/3204
- [x] https://github.com/vllm-project/vllm-ascend/pull/3234
- [x] https://github.com/vllm-project/vllm-ascend/pull/3227
- [x] https://github.com/vllm-project/vllm-ascend/pull/3151
- [x] https://github.com/vllm-project/vllm-ascend/pull/3238
- [x] https://github.com/vllm-project/vllm-ascend/pull/3221

### Functional Test

- [x] aclgraph + qwen3 235b @Potabk 
- [x] aclgraph + full graph + qwen3 30b @zhangxinyuehfad 
- [ ] glm4.5 @shen-shanshan 
- [x] Qwen3-next @wxsIcey 
- [x] Qwen3-vl @booker123456 
- [ ] Longcat @zhangxinyuehfad 

### Doc Test

- [ ] Tutorial is updated.
   - [x] qwen3-vl guide @booker123456 https://github.com/vllm-project/vllm-ascend/pull/3227
   - [ ] deepseek v3.2 guide https://github.com/vllm-project/vllm-ascend/pull/3275
- [ ] User Guide is updated.
- [ ] Developer Guide is updated.


### Prepare Artifacts

- [ ] Docker image is ready.
- [ ] Wheel package is ready.


### Release Step

- [ ] Release note PR is merged.
- [ ] Post the release on GitHub release page.
- [ ] Generate official doc page on https://app.readthedocs.org/dashboard/
- [ ] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [ ] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [ ] Upload 310p wheel to Github release page
- [ ] Broadcast the release news (By message, blog , etc)
- [ ] Close this issue

