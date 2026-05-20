# Issue #4982: [Release]: Release checklist for v0.12.0rc1

## 基本信息

- **编号**: #4982
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4982
- **创建时间**: 2025-12-13T10:02:05Z
- **关闭时间**: 2025-12-14T01:39:07Z
- **更新时间**: 2025-12-14T01:39:07Z
- **提交者**: @wangxiyuan
- **评论数**: 3

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.12.0rc1
**Release Branch**: main
**Release Date**: 12.13
**Release Manager**: @wangxiyuan 


### Prepare Release Note

- [ ] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/4984
- [ ] Upgrade vllm version to the new version for CI and Dockerfile
- [ ] Write the release note PR.

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [ ] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md (Getting Started and Branch section)

  - [x] Update version info in docs/source/community/versioning_policy.md(Release compatibility matrix, Release window and Branch states section)

  - [ ] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

All is merged


### Functional Test

deepseek\qwen test well


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

