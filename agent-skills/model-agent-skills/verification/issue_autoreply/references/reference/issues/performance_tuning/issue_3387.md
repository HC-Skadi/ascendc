# Issue #3387: [Test] enable all the skipped test

## 基本信息

- **编号**: #3387
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3387
- **创建时间**: 2025-10-11T09:26:21Z
- **关闭时间**: 2025-12-08T08:00:48Z
- **更新时间**: 2025-12-08T08:00:48Z
- **提交者**: @wangxiyuan
- **评论数**: 3

## 标签

good first issue; help wanted; ci/build

## 问题描述

We notice that a lot of UT and E2E test are skipped, we should reenable them.

E2E:

- [ ] test_fused_moe_allgather_ep.py (Need CANN and PTA upgrade)
- [ ] test_e2e_pangu_with_torchair @Angazenn 
- [x] test_external_launcher.py https://github.com/vllm-project/vllm-ascend/pull/3344 @loukong33 
- [x] test_pipeline_parallel.py @leo-pony 
- [ ] spec decode @wxsIcey 

UT: @zhangxinyuehfad 
- [x] test_platform.py
- [x] test_patch_minicpm.py
- [x] test_scheduler.py
- [x] test_llmdatadist_connector.py
- [x] test_mooncake_connector.py
- [x] test_remote_decode_lifecycle.py
- [x] test_remote_prefill_lifecycle.py
- [x] test_torchair_deepseek_v2.py
- [x] test_utils.py
