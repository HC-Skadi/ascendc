# Issue #1982: [Doc]: Run "bash format.sh ci" according contribution guide in local machine failed

## 基本信息

- **编号**: #1982
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1982
- **创建时间**: 2025-07-24T04:12:47Z
- **关闭时间**: 2025-08-01T07:36:38Z
- **更新时间**: 2025-08-01T07:36:38Z
- **提交者**: @leo-pony
- **评论数**: 0

## 标签

documentation

## 问题描述

### 📚 The doc issue

Part error information as following:
running mypy on vllm_ascend
vllm_ascend/ascend_config.py:18: error: Cannot find implementation or library stub for module named "vllm.logger"  [import-not-found]
vllm_ascend/sample/rejection_sampler.py:6: error: Cannot find implementation or library stub for module named "vllm.v1.sample.rejection_sampler"  [import-not-found]
vllm_ascend/sample/rejection_sampler.py:6: error: Cannot find implementation or library stub for module named "vllm.v1.sample"  [import-not-found]
vllm_ascend/sample/rejection_sampler.py:6: error: Cannot find implementation or library stub for module named "vllm.v1"  [import-not-found]
vllm_ascend/sample/rejection_sampler.py:6: error: Cannot find implementation or library stub for module named "vllm"  [import-not-found]
vllm_ascend/sample/rejection_sampler.py:7: error: Cannot find implementation or library stub for module named "vllm.logger"  [import-not-found]
vllm_ascend/sample/rejection_sampler.py:8: error: Cannot find implementation or library stub for module named "vllm.v1.sample.metadata"  [import-not-found]
vllm_ascend/sample/rejection_sampler.py:11: error: Cannot find implementation or library stub for module named "vllm.v1.spec_decode.metadata"  [import-not-found]
vllm_ascend/quantization/func_wrapper.py:22: error: Cannot find implementation or library stub for module named "vllm.logger"  [import-not-found]
vllm_ascend/quantization/func_wrapper.py:23: error: Cannot find implementation or library stub for module named "vllm.model_executor.layers.layernorm"  [import-not-found]
vllm_ascend/quantization/func_wrapper.py:24: error: Cannot find implementation or library stub for module named "vllm.model_executor.layers.linear"  [import-not-found]
vllm_ascend/patch/worker/patch_common/patch_utils.py:5: error: Cannot find implementation or library stub for module named "vllm"  [import-not-found]
vllm_ascend/patch/worker/patch_common/patch_utils.py:6: error: Cannot find implementation or library stub for module named "vllm.utils"  [import-not-found]
vllm_ascend/patch/worker/patch_common/patch_minicpm.py:19: error: Cannot find implementation or library stub for module named "vllm.model_executor.models.minicpm"  [import-not-found]
vllm_ascend/patch/worker/patch_common/patch_distributed.py:21: error: Cannot find implementation or library stub for module named "vllm"  [import-not-found]
vllm_ascend/patch/worker/patch_common/patch_distributed.py:22: error: Cannot find implementation or library stub for module named "vllm.distributed.parallel_state"  [import-not-found]
vllm_ascend/ops/vocab_parallel_embedding.py:21: error: Cannot find implementation or library stub for module named "vllm.distributed"  [import-not-found]
vllm_ascend/ops/vocab_parallel_embedding.py:22: error: Cannot find implementation or library stub for module named "vllm.model_executor.layers.vocab_parallel_embedding"  [import-not-found]
vllm_ascend/ops/attention.py:21: error: Cannot find implementation or library stub for module named "vllm.model_executor.layers.linear"  [import-not-found]
vllm_ascend/models/qwen3_moe.py:19: error: Cannot find implementation or library stub for module named "vllm.model_executor.models.qwen3_moe"  [import-not-found]
vllm_ascend/lora/punica_wrapper/punica_npu.py:6: error: Cannot find implementation or library stub for module named "vllm.lora.ops.torch_ops"  [import-not-found]
vllm_ascend/lora/punica_wrapper/punica_npu.py:9: error: Cannot find implementation or library stub for module named "vllm.lora.punica_wrapper.punica_base"  [import-not-found]
vllm_ascend/distributed/communicator.py:21: error: Cannot find implementation or library stub for module named "vllm.distributed.device_communicators.base_device_communicator"  [import-not-found]
vllm_ascend/distributed/communication_op.py:19: error: Cannot find implementation or library stub for module named "vllm.distributed.parallel_state"  [import-not-found]
vllm_ascend/distributed/__init__.py:18: error: Cannot find implementation or library stub for module named "vllm.distributed.kv_transfer.kv_connector.factory"  [import-not-found]

### Suggest a potential alternative/fix

_No response_
