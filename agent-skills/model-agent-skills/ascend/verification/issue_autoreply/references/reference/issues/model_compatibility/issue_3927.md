# Issue #3927: [Release]: Release checklist for v0.11.0rc1

## 基本信息

- **编号**: #3927
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3927
- **创建时间**: 2025-10-31T06:41:12Z
- **关闭时间**: 2025-11-11T01:58:47Z
- **更新时间**: 2025-11-11T01:58:48Z
- **提交者**: @wangxiyuan
- **评论数**: 16

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.11.0rc1
**Release Branch**: v0.11.0-dev
**Release Date**: 2025/11/04
**Release Manager**:  @wangxiyuan 


### Prepare Release Note

- [ ] Create a new issue for release feedback
- [ ] ~~Upgrade vllm version to the new version for CI and Dockerfile~~
- [ ] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/3931

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update release version in README.md and README.zh.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [ ] https://github.com/vllm-project/vllm-ascend/pulls?q=is%3Apr+is%3Aopen+base%3Av0.11.0-dev


### Functional Test

- [x] Deepseek v3 + aclgraph @Meihan-chen  
- [x] pooling model: bge-m3, bge-reranker  @zhangxinyuehfad 
- [x] w4a4 quantization @22dimensions 
- [x] deepseek 3.2 @menogrey
    
    > NOTE
    > All the following test should be done with enabling `VLLM_ASCEND_ENABLE_MLAPO` and install `custom_op_sfa` only!
    > w8a8 and bf16 should both be tested
    - [ ] deepseek 3.2 w8a8/bf16 + aclgraph @Meihan-chen 
    - [x] deepseek 3.2 w8a8/bf16 + torchair + ascendscheduler @menogrey 
    - [x] deepseek 3.2 w8a8/bf16 + torchair + v1scheduler @menogrey 
 
- [x] qwen3-next @wxsIcey 
- [x] mtp @wxsIcey 
- [x] mooncake @Potabk 
- [x] v1 scheduler  @gcanlin 
- [ ] Qwen2-audio @zhangxinyuehfad 
- [x] Qwen3-VL @shen-shanshan 

### Doc Test

- [ ] Tutorial is updated.
- [ ] User Guide is updated.
- [ ] Developer Guide is updated.


### Prepare Artifacts

- [x] Docker image is ready.
- [x] Wheel package is ready.


### Release Step

- [x] Release note PR is merged.
- [x] Post the release on GitHub release page.
- [x] Generate official doc page on https://app.readthedocs.org/dashboard/
- [x] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [x] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [x] Upload 310p wheel to Github release page
- [ ] Broadcast the release news (By message, blog , etc)
- [x] Close this issue

