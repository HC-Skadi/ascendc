# Issue #5276: [Bug]: Prefill and dcode nodes crash during accuracy testing

## 基本信息

- **编号**: #5276
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5276
- **创建时间**: 2025-12-23T05:08:10Z
- **关闭时间**: 2025-12-31T07:50:15Z
- **更新时间**: 2025-12-31T07:50:15Z
- **提交者**: @jianzs
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

```shell
export TORCHDYNAMO_DISABLE=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=1
vllm serve DeepSeek-V3-0324-W8A8-MTP-ROT --port 8100 --trust-remote-code --served-model-name auto --distributed-executor-backend mp --model-loader-extra-config '{"enable_multithread_load":true,"num_threads":8}' --enable-prompt-tokens-details --max-model-len 65535 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.93 --trust-remote-code --enable-prefix-caching --data-parallel-size 2 --tensor-parallel-size 8 --pipeline-parallel-size 1 --enforce-eager --quantization ascend --enable-expert-parallel --async-scheduling --speculative-config '{"num_speculative_tokens":1, "method": "deepseek_mtp"}' --additional-config '{
        "enable_cpu_binding": true
    }' --kv-transfer-config '{
        "kv_connector": "MooncakeConnectorV1",
        "kv_buffer_device": "npu",
        "kv_role": "kv_producer",
        "kv_parallel_size": 2,
        "kv_port": "20002",
        "engine_id": "prefill-0",
        "kv_rank": 0,
        "kv_connector_extra_config": {
            "use_ascend_direct": true,
            "prefill": {
                    "dp_size": 2,
                    "tp_size": 8,
                    "pp_size": 1
             },
             "decode": {
                    "dp_size": 32,
                    "tp_size": 1
             }
        }
    }'
```

```
export TORCHDYNAMO_DISABLE=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=2
vllm serve DeepSeek-V3-0324-W8A8-MTP-ROT --api-server-count 1 --port 8200 --trust-remote-code --served-model-name auto --distributed-executor-backend mp --model-loader-extra-config '{"enable_multithread_load":true,"num_threads":8}' --enable-prompt-tokens-details --max-num-seqs 42 --max-model-len 65536 --max-num-batched-tokens 84 --block-size 128 --gpu-memory-utilization 0.95 --no-enable-prefix-caching --data-parallel-size 32 --data-parallel-size-local 16 --data-parallel-address 33.182.142.47 --data-parallel-rpc-port 14435 --data-parallel-start-rank 0 --tensor-parallel-size 1 --enable-expert-parallel --quantization ascend --async-scheduling --speculative-config '{"num_speculative_tokens":1, "method": "deepseek_mtp"}' --compilation-config '{"cudagraph_capture_sizes":[2,4,8,16,24,32,40,42,48,60,72,84], "cudagraph_mode": "FULL_DECODE_ONLY"}' --additional-config '{"enable_cpu_binding":true,"recompute_scheduler_enable":true,"finegrained_tp_config":{"lmhead_tensor_parallel_size":16}}' --kv-transfer-config '{
        "kv_connector": "MooncakeConnectorV1",
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

prefill log

<img width="3818" height="1796" alt="Image" src="https://github.com/user-attachments/assets/f05a6589-9423-4de3-a47b-a75d74787515" />

decode log

<img width="3840" height="1376" alt="Image" src="https://github.com/user-attachments/assets/8049869b-32c0-47c3-adab-348761655b6d" />
