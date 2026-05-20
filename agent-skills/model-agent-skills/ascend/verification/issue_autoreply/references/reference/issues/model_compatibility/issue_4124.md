# Issue #4124: [Release]: Release checklist for v0.11.1rc1

## 基本信息

- **编号**: #4124
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4124
- **创建时间**: 2025-11-11T13:00:15Z
- **关闭时间**: 2025-12-03T07:31:06Z
- **更新时间**: 2025-12-03T07:31:06Z
- **提交者**: @leo-pony
- **评论数**: 1

## 标签

无

## 问题描述

### Release Checklist

**Release Version**: v0.11.1rc1
**Release Branch**: main
**Release Date**: 
**Release Manager**: @wangxiyuan 


### Prepare Release Note

- [ ] Create a new issue for release feedback
- [ ] Upgrade vllm version to the new version for CI and Dockerfile
- [ ] Write the release note PR.

  - [ ] Update the feedback issue link in docs/source/faqs.md

  - [ ] Add release note to docs/source/user_guide/release_notes.md

  - [ ] Update release version in README.md and README.zh.md

  - [ ] Update version info in docs/source/community/versioning_policy.md

  - [ ] Update contributor info in docs/source/community/contributors.md

  - [ ] Update package version in docs/conf.py


### PR need Merge

- [ ] PR link1


### Functional Test

- [ ] Deepseek v3 + aclgraph [@Meihan-chen](https://github.com/Meihan-chen)

- [ ] pooling model: bge-m3, bge-reranker  [@zhangxinyuehfad](https://github.com/zhangxinyuehfad)

- [ ]  w4a4 quantization [@22dimensions](https://github.com/22dimensions)

- [ ]  deepseek 3.2 [@menogrey](https://github.com/menogrey)
  > NOTE
  > All the following test should be done with enabling `VLLM_ASCEND_ENABLE_MLAPO` and install `custom_op_sfa` only!
  > w8a8 and bf16 should both be tested

  - [ ]  deepseek 3.2 w8a8/bf16 + aclgraph [@Meihan-chen](https://github.com/Meihan-chen)
  - [ ]  deepseek 3.2 w8a8/bf16 + torchair + ascendscheduler [@menogrey](https://github.com/menogrey)
  - [ ]  deepseek 3.2 w8a8/bf16 + torchair + v1scheduler [@menogrey](https://github.com/menogrey)[x] 

- [ ]  qwen3-next [@wxsIcey](https://github.com/wxsIcey)

- [ ] mtp [@wxsIcey](https://github.com/wxsIcey)

- [ ]  mooncake [@Potabk](https://github.com/Potabk)

- [ ]   v1 scheduler  [@gcanlin](https://github.com/gcanlin)

- [ ]  Qwen2-audio [@zhangxinyuehfad](https://github.com/zhangxinyuehfad)

- [ ] Qwen3-VL [@shen-shanshan](https://github.com/shen-shanshan)

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

