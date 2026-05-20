# Issue #4986: [Bug]: Server hangs when running FULL_DECODE_ONLY mode  and enabling MTP with DeepSeek V3.1

## 基本信息

- **编号**: #4986
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4986
- **创建时间**: 2025-12-13T10:35:28Z
- **关闭时间**: 2025-12-17T01:20:45Z
- **更新时间**: 2025-12-17T01:20:45Z
- **提交者**: @jianzs
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

``

### 🐛 Describe the bug

```
vllm serve /path/to/model --api-server-count 4 --port 8200 --trust-remote-code --served-model-name auto --distributed-executor-backend mp --model-loader-extra-config '{"enable_multithread_load":true,"num_threads":8}' --enable-prompt-tokens-details --max-num-seqs 42 --max-model-len 131072 --max-num-batched-tokens 84 --block-size 128 --gpu-memory-utilization 0.90 --no-enable-prefix-caching --data-parallel-size 32 --data-parallel-size-local 16 --data-parallel-address 33.182.142.47 --data-parallel-rpc-port 14435 --data-parallel-start-rank 0 --tensor-parallel-size 1 --enable-expert-parallel --quantization ascend --speculative-config '{"num_speculative_tokens":1, "method": "deepseek_mtp"}' --compilation-config '{"cudagraph_capture_sizes":[2,4,8,16,24,32,40,42], "cudagraph_mode": "FULL_DECODE_ONLY"}' --additional-config '{"enable_cpu_binding":true,"enable_kv_nz":true,"multistream_overlap_shared_expert":true,"finegrained_tp_config":{"embedding_tensor_parallel_size":8,"lmhead_tensor_parallel_size":8}}' --kv-transfer-config '{
        "kv_connector": "MooncakeConnector",
        "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
        "kv_buffer_device": "npu",
        "kv_role": "kv_consumer",
        "kv_parallel_size": 2,
        "kv_port": "20002",
        "engine_id": "decode-0",
        "kv_rank": 1,
        "kv_connector_extra_config": {
            "use_ascend_direct": true,
            "prefill": {
                    "dp_size": 2,
                    "tp_size": 8,
                    "pp_size": 1,
                    "pp_layer_partition": null
             },
             "decode": {
                    "dp_size": 32,
                    "tp_size": 1
             }
        }
    }'
```

In the prefill-decode disaggregation scenario, the decode engine freezes when it receives requests.

The plog shows:

<img width="3818" height="1418" alt="Image" src="https://github.com/user-attachments/assets/5f4cda6c-7a76-4231-b213-571aa00d2afc" />
