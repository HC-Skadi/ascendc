# Issue #2210: [Release]: Release checklist for v0.10.0rc1

## 基本信息

- **编号**: #2210
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2210
- **创建时间**: 2025-08-05T06:08:59Z
- **关闭时间**: 2025-08-08T06:26:49Z
- **更新时间**: 2025-09-05T02:11:56Z
- **提交者**: @MengqingCao
- **评论数**: 11

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.10.0rc1
**Release Branch**: main
**Release Date**: 
**Release Manager**: MengqingCao


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/2217
- [x] Write the release note PR.

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py -- do me after release


### PR need Merge

- [x] #2183
- [x] #2145
- [x] #2162
- [x] #2242 
- [x] #2209

### Functional Test
- **ALL tests with `VLLM_ASCEND_ENABLE_MATMUL_ALLREDUCE` enabled**
- [ ] Disaggregate prefill @Potabk
  - [ ] deepseek
    - [x] Disaggregate prefill on multi-node + deepseek + torchair graph mode + V1 scheduler + dp + ep + tp
    - [ ] Disaggregate prefill on single-node + deepseek + torchair graph mode + V1 scheduler + dp + ep + tp
    - [x] Disaggregate prefill on multi-node + deepseek + torchair graph mode + AscendScheduler (disabling chunked prefill) + dp + ep + tp
    - [ ] Disaggregate prefill on single-node + deepseek + torchair graph mode + AscendScheduler (disabling chunked prefill) + dp + ep + tp
  - [ ] qwen3 moe
    - [x] Disaggregate prefill on multi-node + qwen3 235B + aclgraph + V1 scheduler + dp + ep + tp
    - [ ] Disaggregate prefill on single-node + qwen3 30B + aclgraph + V1 scheduler + dp + ep + tp

- [x] qwen3 moe + eager mode + all2allv: enabling `VLLM_ASCEND_ENABLE_MOE_ALL2ALL_SEQ` @wangxiyuan 
- [x] deepseek v3 + torchair + all2allv: enabling `VLLM_ASCEND_ENABLE_MOE_ALL2ALL_SEQ` @Potabk 

- [x] Aclgraph + qwen3 moe + dp +tp @MengqingCao https://github.com/vllm-project/vllm-ascend/issues/2210#issuecomment-3154788642
- [x] Eager mode + qwen3 moe + dp +tp @MengqingCao https://github.com/vllm-project/vllm-ascend/issues/2210#issuecomment-3154788642

- [ ] spec decode @shen-shanshan 
  - [ ] deepseek-w8a8 + torchair graph mode+ mtp -- rely on #2145
  - [x] eagle3
  - [x] ngram
- [ ] w8a8 + enabling nz -- performance @MengqingCao 
- [x] deepseek w8a8 dynamic + multi-stream @zhangxinyuehfad https://github.com/vllm-project/vllm-ascend/issues/2210#issuecomment-3154236497
- [x] w4a8 + qwen3-8b @22dimensions  https://github.com/vllm-project/vllm-ascend/issues/2210#issuecomment-3155006315

- [x] numpy > 2.0 with CANN 8.2.1 @MengqingCao -- not work with numpy>2.0 https://github.com/vllm-project/vllm-ascend/issues/2210#issuecomment-3154024216
- [x] lora perf improve @taoxudonghaha 

### Doc Test

- [x] Tutorial is updated.
- [x] User Guide is updated.
- [x] Developer Guide is updated.


### Prepare Artifacts

- [x] Docker image is ready.
  - [x] A3 image check @Potabk 
- [x] Wheel package is ready.


### Release Step

- [x] Release note PR is merged.
- [x] Post the release on GitHub release page.
- [x] Generate official doc page on https://app.readthedocs.org/dashboard/
- [x] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [x] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [ ] Upload 310p wheel to Github release page
- [x] Broadcast the release news (By message, blog , etc)
- [x] Close this issue
- [ ] Update 900-release-checklist.yml
- [x] Pin feedback issue

