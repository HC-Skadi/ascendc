# Issue #6251: [Release]: Release checklist for v

## 基本信息

- **编号**: #6251
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6251
- **创建时间**: 2026-01-26T03:49:22Z
- **关闭时间**: 2026-01-26T09:21:15Z
- **更新时间**: 2026-01-26T09:21:15Z
- **提交者**: @shao-cyber
- **评论数**: 0

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: 
**Release Branch**: 
**Release Date**: 
**Release Manager**: 


### Prepare Release Note

- [ ] Create a new issue for release feedback
- [ ] Upgrade vllm version to the new version for CI and Dockerfile
- [ ] Write the release note PR.

  - [ ] Update the feedback issue link in docs/source/faqs.md

  - [ ] Add release note to docs/source/user_guide/release_notes.md

  - [ ] Update release version in README.md and README.zh.md (Getting Started and Branch section)

  - [ ] Update version info in docs/source/community/versioning_policy.md(Release compatibility matrix, Release window and Branch states section)

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

