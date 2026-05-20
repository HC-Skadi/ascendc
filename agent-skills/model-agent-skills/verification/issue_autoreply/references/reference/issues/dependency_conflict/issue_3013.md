# Issue #3013: [Release]: Release checklist for v0.10.3rc1

## 基本信息

- **编号**: #3013
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3013
- **创建时间**: 2025-09-18T09:15:33Z
- **关闭时间**: 2025-09-28T02:36:41Z
- **更新时间**: 2025-09-28T02:36:42Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.11.0rc1
**Release Branch**: main
**Release Date**: 20250923
**Release Manager**: 


### Prepare Release Note

- [ ] Create a new issue for release feedback
- [ ] Write the release note PR.

  - [ ] Update the feedback issue link in docs/source/faqs.md

  - [ ] Add release note to docs/source/user_guide/release_notes.md

  - [ ] Update release version in README.md and README.zh.md

  - [ ] Update version info in docs/source/community/versioning_policy.md

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

