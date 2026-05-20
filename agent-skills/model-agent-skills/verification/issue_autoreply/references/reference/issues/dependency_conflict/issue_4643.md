# Issue #4643: [Release]: Release checklist for v0.11.0rc3

## 基本信息

- **编号**: #4643
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4643
- **创建时间**: 2025-12-02T12:46:59Z
- **关闭时间**: 2025-12-19T01:35:54Z
- **更新时间**: 2025-12-19T01:35:54Z
- **提交者**: @wangxiyuan
- **评论数**: 0

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.11.0rc3
**Release Branch**: v0.11.0-dev
**Release Date**: 2025-12-02
**Release Manager**: @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/4642
- [ ] Upgrade vllm version to the new version for CI and Dockerfile
- [ ] Write the release note PR.

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [ ] Update contributor info in docs/source/community/contributors.md

  - [ ] Update package version in docs/conf.py


### PR need Merge

- [ ] PR link1
- [ ] PR link2
- [ ] ...


### Functional Test

- [ ] Feature1
- [ ] Bug1
- [ ] ...


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

