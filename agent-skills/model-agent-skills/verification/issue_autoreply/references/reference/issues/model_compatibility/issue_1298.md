# Issue #1298: [RFC]: Unit test coverage improvement

## 基本信息

- **编号**: #1298
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1298
- **创建时间**: 2025-06-19T09:09:39Z
- **关闭时间**: 2025-12-08T08:01:26Z
- **更新时间**: 2025-12-08T08:01:26Z
- **提交者**: @MengqingCao
- **评论数**: 42

## 标签

good first issue; help wanted; feature request

## 问题描述

Note: Setup test environment: https://vllm-ascend.readthedocs.io/en/latest/developer_guide/contribution/testing.html

### Motivation

This issue attempt to reduce the gap of unit tests to cover the code. There is a brief architecture of ut in `tests/ut/` already. We need to add more to cover all the code in vllm-ascend, and there are several principles to follow:

1. The overall file tree should be consistent with `vllm_ascend`
2. The file name should be the original file name with a prefix `test_`
3. Use `unittest` framework, make good use of mock
4. The UTs are all running on cpu node, mock the function related to device to host

Please refer to the official doc on [contributing](https://vllm-ascend.readthedocs.io/en/latest/developer_guide/contribution/index.html) and [testing](https://vllm-ascend.readthedocs.io/en/latest/developer_guide/contribution/testing.html) to develop, thanks!
### Unit tests need to add

- [x] |-- test__version.py
- [x] |-- test_ascend_config.py
- [ ] |-- test_attention
- [ ] |   |-- ~~test_attention.py~~ will drop later
- [x] |   |-- test_attention_v1.py https://github.com/vllm-project/vllm-ascend/pull/1529
- [ ] |   `-- test_mla_v1.py @SunnyLee151064
- [ ] |-- compilation
- [ ] |   `-- test_piecewise_backend.py @SunnyLee151064
- [ ] |-- core
- [ ] |   |-- test_schedule_config.py @nuclearwu
- [ ] |   `-- test_scheduler.py @SunnyLee151064
- [ ] |-- device_allocator
- [ ] |   `-- test_camem.py @1024daniel
- [ ] |-- distributed
- [ ] |   |-- test_communicator.py @FieeFlip
- [ ] |   |-- test_device_communicators @Agonixiaoxiao #1601
- [ ] |   |   |-- test_pyhccl.py @SunnyLee151064
- [ ] |   |   `-- test_pyhccl_wrapper.py @SunnyLee151064
- [x] |   |-- kv_transfer @Agonixiaoxiao 
- [x] |   |   |-- test_simple_buffer.py https://github.com/vllm-project/vllm-ascend/pull/1531
- [x] |   |   |-- test_simple_connector.py https://github.com/vllm-project/vllm-ascend/pull/1531
- [x] |   |   |-- test_simple_pipe.py https://github.com/vllm-project/vllm-ascend/pull/1531
- [ ] |   |   `-- test_utils.py @cocacolafan
- [ ] |   |-- test_llmdatadist_connector.py @cocacolafan
- [x] |   `-- test_parallel_state.py   @wangyanhui-cmss https://github.com/vllm-project/vllm-ascend/pull/1460
- [ ] |-- test_envs.py @YuanCheng-coder
- [ ] |-- lora
- [ ] |   `-- punica_wrapper @hongfugui
- [ ] |       `-- test_punica_npu.py @hongfugui
- [ ] |-- models
- [ ] |   |-- test_deepseek_dbo.py
- [ ] |   |-- test_deepseek_mtp.py @Liccol
- [ ] |   |-- test_deepseek_v2.py @ZrBac
- [ ] |   |-- test_qwen2_5_vl.py @Ronald1995
- [ ] |   |-- test_qwen2_5_vl_without_padding.py @Ronald1995
- [ ] |   |-- test_qwen2_vl.py @Ronald1995
- [ ] |   `-- test_qwen3_moe.py @loukong33
- [ ] |-- multistream
- [ ] |   |-- test_base.py @SunnyLee151064
- [ ] |   |-- test_context.py @xingLong-xl
- [ ] |   |-- test_decorator.py @Liccol
- [ ] |   |-- test_layers.py @1024daniel
- [ ] |   |-- test_metadata.py @SunnyLee151064
- [ ] |   `-- test_ms_split.py @SunnyLee151064
- [ ] |-- ops
- [ ] |   |-- test_activation.py @MengqingCao 
- [ ] |   |-- test_attention.py @SunnyLee151064
- [ ] |   |-- test_cache.py @SunnyLee151064
- [ ] |   |-- test_common_fused_moe.py @MengqingCao 
- [x] |   |-- test_expert_load_balancer.py
- [ ] |   |-- test_fused_moe.py @shiyuan680
- [ ] |   |-- test_layernorm.py @MengqingCao 
- [ ] |   |-- test_rotary_embedding.py @MengqingCao 
- [ ] |   `-- test_vocab_parallel_embedding.py @YuanCheng-coder
- [ ] |-- patch
- [ ] |   |-- platform
- [ ] |   |   |-- patch_0_9_2
- [ ] |   |   |-- patch_common
- [ ] |   |   |   `-- test_test_patch_distributed.py @yangqinghao-cmss
- [ ] |   |   `-- patch_main
- [ ] |   `-- worker
- [ ] |       |-- patch_0_9_2
- [ ] |       |-- patch_common
- [ ] |       |   |-- test_patch_distributed.py @Pr0Wh1teGivee
- [ ] |       |   |-- test_patch_eagle.py @Pr0Wh1teGivee
- [ ] |       |   |-- test_patch_minicpm.py @Pr0Wh1teGivee
- [ ] |       |   |-- test_patch_multi_step_worker.py @Pr0Wh1teGivee
- [x] |       |   |-- test_patch_sampler.py 
- [ ] |       |   |-- test_patch_spec_decode_worker.py @Pr0Wh1teGivee
- [ ] |       |   `-- test_patch_utils.py @Pr0Wh1teGivee
- [ ] |       `-- patch_main
- [x] |-- test_platform.py @zhanghw0354 https://github.com/vllm-project/vllm-ascend/pull/1476
- [ ] |-- quantization
- [ ] |   |-- test_func_wrapper.py @xudongLi-cmss
- [x] |   |-- test_quant_config.py @nuclearwu https://github.com/vllm-project/vllm-ascend/pull/1529
- [x] |   |-- test_quantizer.py https://github.com/vllm-project/vllm-ascend/pull/1529
- [x] |   |-- test_w8a8.py https://github.com/vllm-project/vllm-ascend/pull/1529
- [ ] |   `-- test_w8a8_dynamic.py
- [ ] |-- sample
- [ ] |   |-- ops
- [ ] |   `-- test_rejection_sampler.py @momo609
- [x] |-- test_utils.py
- [ ] `-- worker 
- [ ] |-- test_cache_engine.py @machenglong2025
- [ ] |-- ~~test_draft_model_runner.py~~ @wangyanhui-cmss will drop later
- [ ] |-- ~~test_model_runner.py~~ will drop later
- [ ] |-- test_model_runner_v1.py @xudongLi-cmss
- [ ]  |-- test_mtp_proposer_v1.py @machenglong2025
- [ ] |-- ~~test_multi_step_runner.py~~ will drop later
- [ ] |-- ~~test_multi_step_worker.py~~ will drop later
- [x] |-- test_pooling_model_runner.py @wangyanhui-cmss https://github.com/vllm-project/vllm-ascend/pull/1640
- [ ] |-- ~~test_worker.py~~ @zhanghw0354 will drop later
- [ ] `-- test_worker_v1.py @zhanghw0354

