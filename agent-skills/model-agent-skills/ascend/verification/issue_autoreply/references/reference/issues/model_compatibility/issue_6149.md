# Issue #6149: [Release]: Release checklist for v0.14.0rc1

## 基本信息

- **编号**: #6149
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6149
- **创建时间**: 2026-01-22T11:46:39Z
- **关闭时间**: 2026-01-30T01:04:05Z
- **更新时间**: 2026-01-30T01:04:05Z
- **提交者**: @wangxiyuan
- **评论数**: 12

## 标签

无

## 问题描述

### Release Checklist

**Release Version**:  v0.14.0rc1
**Release Branch**:  main
**Release Date**:  2026.01.26
**Release Manager**:  @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/6148
- [x] Upgrade vllm version to the new version for CI and Dockerfile
- [x] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/6225

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md (Getting Started and Branch section)

  - [x] Update version info in docs/source/community/versioning_policy.md(Release compatibility matrix, Release window and Branch states section)

  - [ ] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### Bug need Solve

- [x] https://github.com/vllm-project/vllm-ascend/issues/5399
- [x] https://github.com/vllm-project/vllm-ascend/issues/5748
- [ ] E2E stream and eagle error
- [ ] https://github.com/vllm-project/vllm-ascend/issues/6235
- [x] 310 image build error

### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/pull/6144
- [x] https://github.com/vllm-project/vllm-ascend/pull/6069
- [x] https://github.com/vllm-project/vllm-ascend/pull/6151
- [x] https://github.com/vllm-project/vllm-ascend/pull/6117
- [x] https://github.com/vllm-project/vllm-ascend/pull/6191
- [x] https://github.com/vllm-project/vllm-ascend/pull/6098

### Functional Test

- [x] Qwen3-next
- [x] Qwen3-dense
- [x] Qwen3-moe
- [x] Deepseek-3.2
- [ ] Deepseek-3.1


### Doc Test

- [ ] Tutorial is updated.
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

