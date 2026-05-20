# Issue #2525: [Release]: Release checklist for v0.10.1rc1

## 基本信息

- **编号**: #2525
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2525
- **创建时间**: 2025-08-25T08:57:41Z
- **关闭时间**: 2025-09-05T01:55:56Z
- **更新时间**: 2025-09-05T01:55:56Z
- **提交者**: @MengqingCao
- **评论数**: 3

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.10.1.1rc1
**Release Branch**: main
**Release Date**: 
**Release Manager**: @MengqingCao 


### Prepare Release Note

- [x] Create a new issue for release feedback https://github.com/vllm-project/vllm-ascend/issues/2630
- [x] Write the release note PR. https://github.com/vllm-project/vllm-ascend/pull/2635

  - [x] Update the feedback issue link in docs/source/faqs.md

  - [x] Add release note to docs/source/user_guide/release_notes.md

  - [x] Update version info in docs/source/community/versioning_policy.md

  - [x] Update contributor info in docs/source/community/contributors.md

  - [x] Update package version in docs/conf.py


### PR need Merge

- [x] [Bugfix]Support Qwen3-MOE on aclgraph mode in sizes capture and add new ut https://github.com/vllm-project/vllm-ascend/pull/2511
- [x] [Fix] Add operations in _dummy_run to maintain synchronization with _process_reqs, resolving a service hang https://github.com/vllm-project/vllm-ascend/pull/2454
- [x] https://github.com/vllm-project/vllm-ascend/issues/2522
- [x] https://github.com/vllm-project/vllm-ascend/pull/2549
- [x] https://github.com/vllm-project/vllm-ascend/pull/2540
- [x] https://github.com/vllm-project/vllm-ascend/pull/2532
- [x] fix the bug with torchair + dp https://github.com/vllm-project/vllm-ascend/pull/2558
- [x] https://github.com/vllm-project/vllm-ascend/pull/2442
- [x] https://github.com/vllm-project/vllm-ascend/pull/2590
- [x] https://github.com/vllm-project/vllm-ascend/pull/2560
- [x] https://github.com/vllm-project/vllm-ascend/pull/2584
- [x] https://github.com/vllm-project/vllm-ascend/pull/2609
- [x] https://github.com/vllm-project/vllm-ascend/pull/2632
- [x] https://github.com/vllm-project/vllm-ascend/pull/2704
- [x] https://github.com/vllm-project/vllm-ascend/pull/2623
- [ ] https://github.com/vllm-project/vllm-ascend/pull/2660
- [x] https://github.com/vllm-project/vllm-ascend/pull/2664
- [x] https://github.com/vllm-project/vllm-ascend/pull/2541
- [x] https://github.com/vllm-project/vllm-ascend/pull/2714

### Functional Test

Bug needs to be fixed: 
- [x] issue on mc2: https://github.com/vllm-project/vllm-ascend/issues/2523 https://github.com/vllm-project/vllm-ascend/pull/2540 @MengqingCao 
- [ ] https://github.com/vllm-project/vllm-ascend/issues/2239 @leo-pony 
- [x] GLM4.5 long seq @shen-shanshan https://github.com/vllm-project/vllm-ascend/pull/2601
- [x] GLM4V @Yikun will track on https://github.com/vllm-project/vllm-ascend/issues/2516
- [ ] DS 400 QPM @Potabk 
No feature regression
- [ ] Qwen3 235B aclgraph @MengqingCao 
- [x] gpt-oss: https://github.com/vllm-project/vllm-ascend/pull/2436 depends on https://github.com/vllm-project/vllm-ascend/pull/2469
- [x] logits preprocessor @Potabk 
- [x] https://github.com/vllm-project/vllm-ascend/issues/2533 @Potabk  online test



### Doc Test

- [x] Tutorial is updated.
- [x] User Guide is updated.
- [x] Developer Guide is updated.


### Prepare Artifacts

- [ ] Docker image is ready.
- [ ] Wheel package is ready.


### Release Step

- [x] Release note PR is merged.
- [x] Post the release on GitHub release page.
- [ ] Generate official doc page on https://app.readthedocs.org/dashboard/
- [x] Wait for the wheel package to be available on https://pypi.org/project/vllm-ascend
- [x] Wait for the docker image to be available on https://quay.io/ascend/vllm-ascend
- [ ] Upload 310p wheel to Github release page
- [ ] Broadcast the release news (By message, blog , etc)
- [ ] Close this issue

