# Issue #89: Strange Memory Consumption Phenomenon in vLLM

## 基本信息

- **编号**: #89
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/89
- **创建时间**: 2025-02-18T09:46:59Z
- **关闭时间**: 2025-02-21T06:19:02Z
- **更新时间**: 2025-02-21T06:19:02Z
- **提交者**: @fandengdong
- **评论数**: 5

## 标签

bug; question

## 问题描述

Today when I test the inference of Qwen2.5-Math-7B-Instruct on one card (TP=PP=1) it reported the OOM error. 

I'm curously why this happened because the weights of 7B model only occupy 14GB NPU memory, there is 50GB memory left. Then I found that the OOM could be solved when reduce `gpu_memory_utilization` from 0.96 to 0.8. I didn't understand this all even if I set the max_tokens to 1024 in LLM.

We know in the infer mode, the memory is mainly occupied by model weight, activations and KV cache.  Searching on the doc of vllm, I found this:

```bash
        gpu_memory_utilization: The ratio (between 0 and 1) of GPU memory to
            reserve for the model weights, activations, and KV cache. Higher
            values will increase the KV cache size and thus improve the model's
            throughput. However, if the value is too high, it may cause out-of-
            memory (OOM) errors.
```

I was confued when I decrease the `gpu_memory_utilization` the problem solved. So I did some experiments:

- 7B模型，max_tokens = 1K，这里考虑关闭`cpu_offload_gb`参数

  | gpu_memory_utilization | 权重占用显存 | 设置的显存阈值 | 总显存占用 | 
  | --- | --- |--- |--- |
  | 0.2 | 14GB | 12.8GB | OOM | 
  | 0.4 | 14GB | 25.6GB | 36.2GB |
  | 0.6 | 14GB | 38.4GB | 48.3GB |
  | 0.8 | 14GB | 51.2GB | 60.5GB |
  | 0.9 | 14GB | 57.6GB | 63.3GB |
  | 0.95 | 14GB | 60.8GB | OOM |

- 7B模型，**max_tokens = 32K**，这里考虑关闭`cpu_offload_gb`参数

    | gpu_memory_utilization | 权重占用显存 | 设置的显存阈值 | 总显存占用 | 
    | --- | --- |--- |--- |
    | 0.2 | 14GB | 12.8GB | OOM | 
    | 0.4 | 14GB | 25.6GB | 36.2GB |
    | 0.6 | 14GB | 38.4GB | 48.3GB | 
    | 0.8 | 14GB | 51.2GB | 60.6GB | 

So my questions are: 

1.  What actualy does  `gpu_memory_utilization` mean? When I set the value, the real memory occupation usually is higher than the threshold.
2.  What is the additional memory used by vllm that is beyond the `gpu_memory_utilization` threshold ? about 10GB regardless of the `gpu_memory_utilization ` and `max_tokens`.
3.  Why the memory occupation has nothing to do with the `max_tokens` ? Then the `max_tokens` is 32x bigger, the memory is unchanged.
