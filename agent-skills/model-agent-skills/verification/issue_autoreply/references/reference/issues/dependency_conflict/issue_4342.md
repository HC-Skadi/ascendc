# Issue #4342: [Release]: Release checklist for v0.11.0rc2

## 基本信息

- **编号**: #4342
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4342
- **创建时间**: 2025-11-21T08:55:24Z
- **关闭时间**: 2025-12-02T12:46:22Z
- **更新时间**: 2025-12-02T12:46:22Z
- **提交者**: @wangxiyuan
- **评论数**: 0

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.11.0rc2
**Release Branch**:  0.11.0-dev
**Release Date**: 2025.11.21
**Release Manager**:  @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/4343
- [x] Upgrade vllm version to the new version for CI and Dockerfile
- [x] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/4348

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/pull/4334
- [x] https://github.com/vllm-project/vllm-ascend/pull/4332
- [x] https://github.com/vllm-project/vllm-ascend/pull/4341
- [x] https://github.com/vllm-project/vllm-ascend/pull/4352

### Functional Test
Only bug fix release, no need for full test.

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

