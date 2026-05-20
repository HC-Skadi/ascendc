# Issue #1486: [Release]: Release checklist for v0.9.1rc2 on main

## 基本信息

- **编号**: #1486
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1486
- **创建时间**: 2025-06-27T16:19:32Z
- **关闭时间**: 2025-08-04T03:45:42Z
- **更新时间**: 2025-08-04T03:45:42Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

release

## 问题描述

### Release Checklist

**Release Version**: v0.9.1rc2
**Release Branch**: main
**Release Date**: 0628
**Release Manager**: @Yikun 


### Prepare Release Note

- [x] #1487
- [x] Write the release note PR: https://github.com/vllm-project/vllm-ascend/pull/1488
  - [x] Update the feedback issue link in docs/source/faqs.md
  - [x] Add release note to docs/source/user_guide/release_notes.md
  - [x] Update version info in docs/source/community/versioning_policy.md
  - [ ] Update contributor info in docs/source/community/contributors.md
  - [x] Update package version in docs/conf.py

### PR need Merge

- [ ] https://github.com/vllm-project/vllm-ascend/pull/1483
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1421
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1463
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1477
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1478
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1446
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1506
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1529
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1381
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1582

### Functional Test
- [ ] New model
  - [x] Altlas A2 series  2025.06.21
    - [ ] Docker image E2E test
    - [ ] Performance
    - [ ] Accuracy
    - [ ] Doc Turtorial: `Multi-NPU (XXXX 72B)` @shen-shanshan
  
  - [x] Altlas 300I DUO series  @leo-pony
    - [ ] Docker image E2E test
    - [ ] Performance
    - [ ] Accuracy
    - [ ] Doc Turtorial: `Multi-NPU (300I DUO)` 

  - [ ] Quantization @Angazenn 
    - [ ] Performance
    - [ ] Accuracy

- [ ] Accuracy report (auto)
- [ ] Performance for Qwen2 / Qwen3 / Qwen2.5 VL
- [ ] DeepSeek test


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
- [ ] Brodcast the release news (By message, blog , etc)
- [ ] Close this issue

