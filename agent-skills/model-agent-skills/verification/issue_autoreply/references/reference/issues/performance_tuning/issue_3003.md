# Issue #3003: [RFC]: Support MTP Graph Mode for DeepSeek (Torchair/AclGraph)

## 基本信息

- **编号**: #3003
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3003
- **创建时间**: 2025-09-18T04:07:22Z
- **关闭时间**: 2025-12-11T07:54:17Z
- **更新时间**: 2025-12-11T07:54:18Z
- **提交者**: @JC-ut0
- **评论数**: 0

## 标签

RFC

## 问题描述

### Motivation.

Currently, vLLM-Ascend supports only MTP=1, which improves throughput to some extent. However, hostbound becomes a bottleneck in high-throughput or low-latency scenarios.

Supporting MTP Graph Mode decreases hostbound in the decoding phase, reducing iteration overhead, improving latency, and significantly boosting throughput. This enhancement will maximize hardware utilization, and meet real-world deployment needs.

### Proposed Change.

In the original design, the attention operator was unable to process multiple tokens during the decode phase. We have introduced `npu_fused_infer_attention_score` operator with `TND` layout that supports processing no more than 16 tokens per request during the decode phase. More importantly, this operator supports torchair graph mode, so we need design a padding strategy for this. 

The main changes include:
`npu_fused_infer_attention_score` :  
1) [eager/Torchair] use TND layout to be able handle multiple tokens per request in decoding phase.
2) [eager/Torchair] each request can only handle less than 16 tokens in TND layout.
3) [eager/Torchair] npu_fused_infer_attention_score constraint requires the last element of `actual_seq_lengths` must equal to batch_size(num_tokens).
4) [Torchair] The lengths of the queries `actual_seq_lengths` must be padded to the same leagth in each iteration depending on the graph size.
https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/apilist/ptaoplist_000144.html

Notice that, we did not design a padding strategy for aclgraph, since we use pieceswise aclgraph to skip the attention part.

Torchair online Example:
```
python -m vllm.entrypoints.openai.api_server \
 --model="/home/data/DeepSeek-R1_w8a8/" \
 --trust-remote-code \
 --max-model-len 36000 \
 --max-num-batched-tokens 2048 \
 --tensor-parallel-size 4 \
 --data_parallel_size 4 \
 --max-num-seqs 16 \
 --no-enable-prefix-caching \
 --enable_expert_parallel \
 --served-model-name deepseekr1 \
 --speculative-config '{"num_speculative_tokens": 1, "method":"deepseek_mtp"}' \
 --quantization ascend \
 --host 0.0.0.0 \
 --port 1234 \
 --additional-config '{"ascend_scheduler_config":{"enabled":false},"torchair_graph_config":{"enabled":true,"graph_batch_sizes":[16]},"enable_weight_nz_layout":true,"chunked_prefill_for_mla":true}' \
 --gpu_memory_utilization 0.90 
```

Aclgraph online Example:
```
vllm serve \
 --model="/home/data/DeepSeek-R1_w8a8/" \
 --trust-remote-code \
 --max-model-len 1024 \
 --max-num-batched-tokens 1024 \
 --tensor-parallel-size 4 \
 --data_parallel_size 4 \
 --no-enable-prefix-caching \
 --enable_expert_parallel \
 --served-model-name deepseekr1 \
 --quantization ascend \
 --host 0.0.0.0 \
 --port 1234 \
 --max-num-seqs 16 \
 --speculative-config '{"num_speculative_tokens": 1, "method":"deepseek_mtp"}' \
 --compilation-config '{"cudagraph_capture_sizes":[1,4,8]}' \
 --additional-config '{"ascend_scheduler_config":{"enabled":true}, "enable_shared_expert_dp":false}' \
 --gpu_memory_utilization 0.90 
```




Integration: Align backend execution with the existing vLLM interface, which already supports MTP configuration.

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.
Torchair Support: 
https://github.com/vllm-project/vllm-ascend/pull/2145
https://github.com/vllm-project/vllm-ascend/pull/2951
Aclgraph Support:
https://github.com/vllm-project/vllm-ascend/pull/2932

_No response_
