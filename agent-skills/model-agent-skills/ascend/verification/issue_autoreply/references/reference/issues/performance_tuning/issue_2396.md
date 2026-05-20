# Issue #2396: [Release]: Release checklist for `v0.9.1rc3`

## 基本信息

- **编号**: #2396
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2396
- **创建时间**: 2025-08-15T09:46:14Z
- **关闭时间**: 2025-08-29T06:41:02Z
- **更新时间**: 2025-08-29T06:41:26Z
- **提交者**: @shen-shanshan
- **评论数**: 6

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: `v0.9.1rc3`

**Release Branch**: `v0.9.1-dev`

**Release Date**: `2025/08/20`

**Release Manager**: @shen-shanshan 

### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/2410
- [x] Write the release note PR https://github.com/vllm-project/vllm-ascend/pull/2431
  - [x] Update the feedback issue link in docs/source/faqs.md
  - [x] Add release note to docs/source/user_guide/release_notes.md
  - [x] Update version info in docs/source/community/versioning_policy.md
  - [x] Update contributor info in docs/source/community/contributors.md
  - [x] Update package version in docs/conf.py

### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/pull/2314
- [x] https://github.com/vllm-project/vllm-ascend/pull/2478

### Functional Test

- [x] DeepSeek W8A8 MTP with V1 Scheduler (A3 DP4 TP4) @Potabk 
- [x] In DeepSeek-R1 W8A8 PD disagregated Decode instance, using pure DP, with `lmhead_tensor_parallel_size=8` @zhangxinyuehfad 
- [x] DeepSeek with V1 scheduler (with chunked prefill enabled) @MengqingCao 

```bash
--additional_config={"lmhead_tensor_parallel_size": 8}
```

### Doc Test

- [x] Tutorial is updated.
- [x] User Guide is updated.
- [x] Developer Guide is updated.

### Prepare Artifacts

- [x] Docker image is ready.
- [x] Wheel package is ready.

### Release Step

- [x] Release note PR is merged.
- [x] Post the release on GitHub release page.
- [x] Generate official doc page on https://app.readthedocs.org/dashboard/
- [ ] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [ ] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [ ] Upload 310p wheel to Github release page
- [x] Broadcast the release news (By message, blog , etc)
- [x] Close this issue
