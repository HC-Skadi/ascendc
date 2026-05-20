# Issue #2859: [Release]: Release checklist for v0.10.2rc1

## 基本信息

- **编号**: #2859
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2859
- **创建时间**: 2025-09-10T12:21:58Z
- **关闭时间**: 2025-09-24T03:09:43Z
- **更新时间**: 2025-09-24T03:09:43Z
- **提交者**: @wangxiyuan
- **评论数**: 7

## 标签

无

## 问题描述

### Release Checklist

**Release Version**:  v0.10.2rc1
**Release Branch**:  main
**Release Date**: 2025/09/10
**Release Manager**: @wangxiyuan 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/2874
- [x] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/2921

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [x] https://github.com/vllm-project/vllm-ascend/issues/2865
- [x] Quantization accuracy problem https://github.com/vllm-project/vllm-ascend/pull/2856 @22dimensions 
- [x] aclgraph quantization support @yiz-liu  https://github.com/vllm-project/vllm-ascend/pull/2841/
- [x] https://github.com/vllm-project/vllm-ascend/pull/2816
- [x] https://github.com/vllm-project/vllm-ascend/pull/2786

- [x] https://github.com/vllm-project/vllm-ascend/issues/2876 accuracy test fix @wxsIcey 
- [x] https://github.com/vllm-project/vllm-ascend/pull/2896
- [x] https://github.com/vllm-project/vllm-ascend/pull/2894
- [x] https://github.com/vllm-project/vllm-ascend/pull/2902
- [ ] https://github.com/vllm-project/vllm-ascend/pull/2875
- [ ] https://github.com/vllm-project/vllm-ascend/issues/2900
- [ ] GLM accuracy problem @shen-shanshan 
   - https://github.com/vllm-project/vllm-ascend/pull/2898
   - https://github.com/vllm-project/vllm-ascend/pull/2897
- [x] Qwen3-next support @MengqingCao @wangxiyuan

Will not be merged:
- [ ] https://github.com/vllm-project/vllm-ascend/pull/2880

### Functional Test

- [x] Qwen3 235B aclgraph test @zhangxinyuehfad 
- [x] Qwen 235B PD DP EP TP @zhangxinyuehfad 
- [x] deepseek v3 + torchair + all2allv @Potabk 
- [x] Async scheduler feature test @Potabk 
- [x] Qwen2.5 VL W8A8 @22dimensions 
- [x] Qwen3 8B + flash comm @Potabk 
- [x] aclgrah w8a8  @Potabk 


### Doc Test

- [x] Tutorial is updated.
- [x] User Guide is updated.
- [ ] Developer Guide is updated.


### Prepare Artifacts

- [ ] Docker image is ready.
- [ ] Wheel package is ready.


### Release Step

- [x] Release note PR is merged.
- [x] Post the release on GitHub release page.
- [x] Generate official doc page on https://app.readthedocs.org/dashboard/
- [x] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [x] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [ ] Upload 310p wheel to Github release page
- [x] Broadcast the release news (By message, blog , etc)
- [x] Close this issue

