# Issue #4115: [RFC]: Encoder separation for Encode-Prefill-Decode Disaggregation

## 基本信息

- **编号**: #4115
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4115
- **创建时间**: 2025-11-11T02:27:49Z
- **关闭时间**: 2025-11-20T08:04:23Z
- **更新时间**: 2025-11-20T08:04:23Z
- **提交者**: @jesse996
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

## Disaggregated Encoder
A disaggregated encoder runs the vision-encoder stage of a multimodal LLM in a process that is separate from the prefill / decoder stage. Deploying these two stages in independent vLLM instances brings three practical benefits:

1. Independent, fine-grained scaling
2. Lower time-to-first-token (TTFT)
3. Cross-process reuse and caching of encoder outputs

### Proposed Change.

## Encoder-side (producer):
 - Within execute_model, when get_ec_transfer().is_producer is True, the runner enters with maybe_get_ec_connector_output(..., encoder_cache=self.encoder_cache): before running the multimodal encoder.
 - The encode pass computes embeddings and writes them into encoder_cache[mm_hash].
 - Immediately after finishing the encode for a given mm_hash, the runner calls maybe_save_ec_to_connector(self.encoder_cache, mm_hash) which invokes ECConnectorBase.save_caches(encoder_cache=..., mm_hash=...).
 - On context exit, wait_for_save() is invoked (if enabled) to ensure the persisted EC is durable/visible to consumers; get_finished(...) is queried to surface completion status back to the scheduler.
## PD-side (consumer):
 - For requests scheduled on PD, the scheduler supplies ec_connector_metadata that lists the mm_hash items needing loads.
 - The runner binds this metadata and calls start_load_caches(encoder_cache=self.encoder_cache) prior to _gather_mm_embeddings, allowing the connector to populate encoder_cache[mm_hash] from the external store.
 - _gather_mm_embeddings then reads the loaded tensors from encoder_cache and returns them as multimodal embeddings for the subsequent decoder input embedding construction.
 - After the forward step, the runner clears metadata; any connector-furnished completion info is recorded into ECConnectorOutput for the scheduler to free resources when safe.

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
