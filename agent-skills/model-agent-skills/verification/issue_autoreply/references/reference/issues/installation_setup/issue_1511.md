# Issue #1511: [Doc]: torch_npu import and calls statistics

## 基本信息

- **编号**: #1511
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1511
- **创建时间**: 2025-06-29T15:46:26Z
- **关闭时间**: 2026-03-01T14:23:10Z
- **更新时间**: 2026-03-01T14:23:10Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

documentation

## 问题描述

|    | method                          | version   | path                                                                                                                                                                                                                   |
|---:|:--------------------------------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | _npu_flash_attention            | 2.5.1     | [vllm_ascend/attention/attention.py#L893](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L893)                                           |
|    |                                 |           | [vllm_ascend/attention/attention.py#L1251](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L1251)                                         |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L344](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L344)                                     |
|    |                                 |           | [vllm_ascend/attention/mla_v1.py#L825](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L825)                                                 |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L379](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L379)                                               |
|  1 | _npu_flash_attention_qlens      | 2.5.1     | [vllm_ascend/attention/attention.py#L919](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L919)                                           |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L358](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L358)                                     |
|  2 | _npu_flash_attention_unpad      | 2.5.1     | [vllm_ascend/models/qwen2_5_vl_without_padding.py#L93](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_5_vl_without_padding.py#L93)                 |
|    |                                 |           | [vllm_ascend/models/qwen2_vl.py#L101](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_vl.py#L101)                                                   |
|    |                                 |           | [vllm_ascend/models/qwen2_5_vl.py#L113](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_5_vl.py#L113)                                               |
|  3 | _npu_paged_attention            | 2.5.1     | [vllm_ascend/attention/attention.py#L966](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L966)                                           |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L375](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L375)                                     |
|  4 | _npu_paged_attention_mla        | 2.5.1     | [vllm_ascend/attention/attention.py#L1312](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L1312)                                         |
|    |                                 |           | [vllm_ascend/attention/mla_v1.py#L1008](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L1008)                                               |
|  5 | _npu_paged_attention_splitfuse  | 2.5.1     | [vllm_ascend/attention/attention.py#L941](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L941)                                           |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L416](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L416)                                     |
|  6 | _npu_quant_rms_norm             | 2.5.1     | [vllm_ascend/quantization/func_wrapper.py#L50](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/func_wrapper.py#L50)                                 |
|    |                                 |           | [vllm_ascend/quantization/func_wrapper.py#L59](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/func_wrapper.py#L59)                                 |
|  7 | _npu_reshape_and_cache          | 2.5.1     | [vllm_ascend/attention/attention.py#L837](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L837)                                           |
|    |                                 |           | [vllm_ascend/attention/attention.py#L1222](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L1222)                                         |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L320](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L320)                                     |
|    |                                 |           | [vllm_ascend/attention/mla_v1.py#L1158](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L1158)                                               |
|    |                                 |           | [vllm_ascend/distributed/llmdatadist_connector.py#L440](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/llmdatadist_connector.py#L440)               |
|    |                                 |           | [vllm_ascend/distributed/kv_transfer/simple_connector.py#L317](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/kv_transfer/simple_connector.py#L317) |
|  8 | _npu_reshape_and_cache_siso     | 2.5.1     | [vllm_ascend/attention/mla_v1.py#L1170](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L1170)                                               |
|    |                                 |           | [vllm_ascend/distributed/kv_transfer/simple_connector.py#L309](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/kv_transfer/simple_connector.py#L309) |
|  9 | _npu_rotary_embedding           | 2.5.1     | [vllm_ascend/ops/rotary_embedding.py#L69](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/rotary_embedding.py#L69)                                           |
| 10 | npu()                           | 2.5.1     | [vllm_ascend/distributed/llmdatadist_connector.py#L259](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/llmdatadist_connector.py#L259)               |
|    |                                 |           | [vllm_ascend/distributed/kv_transfer/simple_pipe.py#L178](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/kv_transfer/simple_pipe.py#L178)           |
|    |                                 |           | [vllm_ascend/distributed/kv_transfer/simple_connector.py#L357](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/kv_transfer/simple_connector.py#L357) |
|    |                                 |           | [vllm_ascend/worker/multi_step_worker.py#L122](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/worker/multi_step_worker.py#L122)                                 |
| 11 | npu_add_rms_norm                | 2.5.1     | [vllm_ascend/ops/layernorm.py#L41](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/layernorm.py#L41)                                                         |
| 12 | npu_dequant_swiglu_quant        | 2.5.1     | [vllm_ascend/models/deepseek_v2.py#L96](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/deepseek_v2.py#L96)                                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L409](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L409)                               |
| 13 | npu_dynamic_quant               | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L67](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L67)                                 |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L89](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L89)                                 |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L373](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L373)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L596](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L596)                               |
| 14 | npu_fast_gelu                   | 2.5.1     | [vllm_ascend/ops/activation.py#L37](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/activation.py#L37)                                                       |
| 15 | npu_format_cast                 | 2.5.1     | [vllm_ascend/attention/attention.py#L664](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L664)                                           |
|    |                                 |           | [vllm_ascend/attention/attention.py#L891](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention.py#L891)                                           |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L192](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L192)                                     |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L196](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L196)                                     |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L341](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L341)                                     |
|    |                                 |           | [vllm_ascend/attention/attention_v1.py#L413](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/attention_v1.py#L413)                                     |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L621](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L621)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L118](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L118)                                               |
|    |                                 |           | [vllm_ascend/worker/worker.py#L353](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/worker/worker.py#L353)                                                       |
|    |                                 |           | [vllm_ascend/worker/worker.py#L357](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/worker/worker.py#L357)                                                       |
|    |                                 |           | [vllm_ascend/worker/worker.py#L360](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/worker/worker.py#L360)                                                       |
|    |                                 |           | [vllm_ascend/worker/model_runner_v1.py#L1962](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/worker/model_runner_v1.py#L1962)                                   |
|    |                                 |           | [vllm_ascend/worker/model_runner_v1.py#L1964](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/worker/model_runner_v1.py#L1964)                                   |
|    |                                 |           | [vllm_ascend/worker/model_runner_v1.py#L1973](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/worker/model_runner_v1.py#L1973)                                   |
| 16 | npu_format_cast_                | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L820](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L820)                               |
| 17 | npu_fused_infer_attention_score | 2.5.1     | [vllm_ascend/attention/mla_v1.py#L989](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L989)                                                 |
| 18 | npu_grouped_matmul              | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L76](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L76)                                 |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L93](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L93)                                 |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L399](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L399)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L508](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L508)                                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L531](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L531)                                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L171](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L171)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L186](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L186)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L263](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L263)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L276](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L276)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L366](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L366)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L380](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L380)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L607](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L607)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L624](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L624)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L754](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L754)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L768](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L768)                                                       |
| 19 | npu_incre_flash_attention       | 2.5.1     | [vllm_ascend/quantization/w8a8.py#L406](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L406)                                               |
| 20 | npu_interleave_rope             | 2.5.1     | [vllm_ascend/attention/mla_v1.py#L929](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L929)                                                 |
| 21 | npu_kv_rmsnorm_rope_cache       | 2.5.1     | [vllm_ascend/attention/mla_v1.py#L877](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L877)                                                 |
|    |                                 |           | [vllm_ascend/attention/mla_v1.py#L906](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/attention/mla_v1.py#L906)                                                 |
| 22 | npu_moe_compute_expert_tokens   | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L302](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L302)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L508](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L508)                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L361](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L361)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L749](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L749)                                                       |
| 23 | npu_moe_distribute_combine      | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L210](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L210)                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L222](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L222)                                                       |
| 24 | npu_moe_distribute_dispatch     | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L161](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L161)                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L157](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L157)                                                       |
| 25 | npu_moe_finalize_routing        | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L324](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L324)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L336](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L336)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L538](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L538)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L543](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L543)                                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L398](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L398)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L410](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L410)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L536](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L536)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L802](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L802)                                                       |
| 26 | npu_moe_gating_top_k            | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L720](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L720)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L224](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L224)                                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L994](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L994)                                                       |
| 27 | npu_moe_init_routing            | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L256](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L256)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L296](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L296)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8_dynamic.py#L502](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L502)                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L316](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L316)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L355](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L355)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L451](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L451)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L743](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L743)                                                       |
| 28 | npu_moe_init_routing_v2         | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L375](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L375)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L479](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L479)                                               |
| 29 | npu_quant_matmul                | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L606](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L606)                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L99](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L99)                                                 |
| 30 | npu_quantize                    | 2.5.1     | [vllm_ascend/quantization/w8a8.py#L33](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L33)                                                 |
| 31 | npu_rms_norm                    | 2.5.1     | [vllm_ascend/ops/layernorm.py#L38](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/layernorm.py#L38)                                                         |
|    |                                 |           | [vllm_ascend/ops/layernorm.py#L45](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/layernorm.py#L45)                                                         |
| 32 | npu_rotary_mul                  | 2.5.1     | [vllm_ascend/models/qwen2_5_vl_without_padding.py#L82](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_5_vl_without_padding.py#L82)                 |
|    |                                 |           | [vllm_ascend/models/qwen2_5_vl_without_padding.py#L83](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_5_vl_without_padding.py#L83)                 |
|    |                                 |           | [vllm_ascend/models/qwen2_vl.py#L91](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_vl.py#L91)                                                     |
|    |                                 |           | [vllm_ascend/models/qwen2_vl.py#L92](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_vl.py#L92)                                                     |
|    |                                 |           | [vllm_ascend/models/qwen2_5_vl.py#L102](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_5_vl.py#L102)                                               |
|    |                                 |           | [vllm_ascend/models/qwen2_5_vl.py#L103](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/models/qwen2_5_vl.py#L103)                                               |
| 33 | npu_scatter_nd_update_          | 2.5.1     | [vllm_ascend/quantization/w8a8.py#L371](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L371)                                               |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L372](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L372)                                               |
| 34 | npu_swiglu                      | 2.5.1     | [vllm_ascend/quantization/w8a8_dynamic.py#L88](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8_dynamic.py#L88)                                 |
|    |                                 |           | [vllm_ascend/quantization/w8a8.py#L518](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/quantization/w8a8.py#L518)                                               |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L183](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L183)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L273](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L273)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L377](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L377)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L620](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L620)                                                       |
|    |                                 |           | [vllm_ascend/ops/fused_moe.py#L765](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/fused_moe.py#L765)                                                       |
|    |                                 |           | [vllm_ascend/ops/activation.py#L30](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/ops/activation.py#L30)                                                       |
| 35 | npu_top_k_top_p                 | 2.5.1     | [vllm_ascend/patch/worker/patch_common/patch_sampler.py#L57](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/patch/worker/patch_common/patch_sampler.py#L57)     |
| 36 | scatter_update_                 | 2.5.1     | [vllm_ascend/distributed/llmdatadist_connector.py#L279](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/llmdatadist_connector.py#L279)               |
|    |                                 |           | [vllm_ascend/distributed/llmdatadist_connector.py#L284](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/llmdatadist_connector.py#L284)               |
|    |                                 |           | [vllm_ascend/distributed/llmdatadist_connector.py#L289](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/llmdatadist_connector.py#L289)               |
|    |                                 |           | [vllm_ascend/distributed/llmdatadist_connector.py#L297](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/llmdatadist_connector.py#L297)               |
|    |                                 |           | [vllm_ascend/distributed/kv_transfer/simple_pipe.py#L181](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/kv_transfer/simple_pipe.py#L181)           |
|    |                                 |           | [vllm_ascend/distributed/kv_transfer/simple_connector.py#L360](https://github.com/vllm-project/vllm-ascend/blob/b308a7a25897b88d4a23a9e3d583f4ec6de256ac/vllm_ascend/distributed/kv_transfer/simple_connector.py#L360) |

Code:

<details>

```python

import ast
import os
import subprocess
import sys

import pandas as pd

NPU_VERSION_DICT = {
	'_npu_flash_attention': '2.5.1',
	'_npu_flash_attention_qlens': '2.5.1',
	'_npu_flash_attention_unpad': '2.5.1',
	'_npu_paged_attention': '2.5.1',
	'_npu_paged_attention_mla': '2.5.1',
	'_npu_paged_attention_splitfuse': '2.5.1',
	'_npu_quant_rms_norm': '2.5.1',
	'_npu_reshape_and_cache': '2.5.1',
	'_npu_reshape_and_cache_siso': '2.5.1',
	'_npu_rotary_embedding': '2.5.1',
	'npu()': '2.5.1',
	'npu_add_rms_norm': '2.5.1',
	'npu_dequant_swiglu_quant': '2.5.1',
	'npu_dynamic_quant': '2.5.1',
	'npu_fast_gelu': '2.5.1',
	'npu_format_cast': '2.5.1',
	'npu_format_cast_': '2.5.1',
	'npu_fused_infer_attention_score': '2.5.1',
	'npu_grouped_matmul': '2.5.1',
	'npu_incre_flash_attention': '2.5.1',
	'npu_interleave_rope': '2.5.1',
	'npu_kv_rmsnorm_rope_cache': '2.5.1',
	'npu_moe_compute_expert_tokens': '2.5.1',
	'npu_moe_distribute_combine': '2.5.1',
	'npu_moe_distribute_dispatch': '2.5.1',
	'npu_moe_finalize_routing': '2.5.1',
	'npu_moe_gating_top_k': '2.5.1',
	'npu_moe_init_routing': '2.5.1',
	'npu_moe_init_routing_v2': '2.5.1',
	'npu_quant_matmul': '2.5.1',
	'npu_quantize': '2.5.1',
	'npu_rms_norm': '2.5.1',
	'npu_rotary_mul': '2.5.1',
	'npu_scatter_nd_update_': '2.5.1',
	'npu_swiglu': '2.5.1',
	'npu_top_k_top_p': '2.5.1',
	'scatter_update_': '2.5.1'
}

class TorchNpuScanner(ast.NodeVisitor):
    def __init__(self):
        self.results = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):

            #  torch_npu.xxx()
            if (isinstance(node.func.value, ast.Name) and 
                node.func.value.id == 'torch_npu'):
                self.results.append({
                    'type': 'api_call',
                    'lineno': node.lineno,
                    'method': node.func.attr
                })
            # Detect tensor.npu()
            elif node.func.attr == 'npu':
                self.results.append({
                    'type': 'tensor_conversion',
                    'lineno': node.lineno,
                    'method': "npu()"
                })


def scan_python_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read())
            scanner = TorchNpuScanner()
            scanner.visit(tree)
            return scanner.results
        except Exception as e:
            print(f"Parse error {filepath} : {e}")
            return []

def scan_directory(root_dir):
    results = {}
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                findings = scan_python_file(full_path)
                if findings:
                    results[full_path] = findings
    return results

def line2link(hash="", path="", lineno=None):
    link = "https://github.com/vllm-project/vllm-ascend/blob/"
    return f"{link}{hash}/{path}#L{lineno}"

def json_to_table(scan_results):
    table_data = []
    hash = get_current_commit()
    for filepath, findings in scan_results.items():
        for item in findings:
            link = line2link(hash, filepath, item['lineno'])
            method = item.get('method', 'N/A')
            row = {
                'path': f"[{filepath}#L{item['lineno']}]({link})",
                'type': item['type'],
                'method': method,
                'version': NPU_VERSION_DICT.get(method, "unknown")
            }
            table_data.append(row)
    df = pd.DataFrame(table_data)
    return df[['path', 'type', 'method', 'version']]

def get_current_commit():
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                          stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

if __name__ == "__main__":
    scan_results = scan_directory(sys.argv[1])
    df = json_to_table(scan_results)
    print(df.groupby(['method', 'version'])['path'].agg(lambda x: '\n'.join(x)).reset_index().to_markdown())

```

</details>
