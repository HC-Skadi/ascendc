# Issue #776: [Guide][Performance]: vllm-ascend v0.7.3 release performance benchmark

## 基本信息

- **编号**: #776
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/776
- **创建时间**: 2025-05-07T08:27:12Z
- **关闭时间**: 2025-06-15T07:47:34Z
- **更新时间**: 2025-06-15T07:47:34Z
- **提交者**: @Potabk
- **评论数**: 12

## 标签

guide; release

## 问题描述

# How does this result test
Please refer to vllm-ascend [benchmark](https://github.com/vllm-project/vllm-ascend/tree/main/benchmarks)

## Rules

### online serving test
- Input length: randomly sample 200 prompts [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split.json) and [lmarena-ai/vision-arena-bench-v0.1](https://huggingface.co/datasets/lmarena-ai/vision-arena-bench-v0.1/tree/main)(multi-modal) dataset (with fixed random seed).
- Output length: the corresponding output length of these 200 prompts.
- Batch size: dynamically determined by vllm and the arrival pattern of the requests.
- **Average QPS (query per second)**: 1, 4, 16 and inf. QPS = inf means all requests come at once. For other QPS values, the arrival time of each query is determined using a random Poisson process (with fixed random seed).
- Models: Qwen/Qwen2.5-7B-Instruct, Qwen/Qwen2.5-VL-7B-Instruct
- Evaluation metrics: throughput, TTFT (median time to the first token ), ITL (median inter-token latency) TPOT(median time per output token).

### latency test
- Input length: 32 tokens.
- Output length: 128 tokens.
- Batch size: fixed (8).
- Models: Qwen/Qwen2.5-7B-Instruct, Qwen/Qwen2.5-VL-7B-Instruct
- Evaluation metrics: end-to-end latency.

### throughput test
- Input length: randomly sample 200 prompts from [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split.json) and [lmarena-ai/vision-arena-bench-v0.1](https://huggingface.co/datasets/lmarena-ai/vision-arena-bench-v0.1/tree/main)(multi-modal) dataset (with fixed random seed).
- Output length: the corresponding output length of these 200 prompts.
- Batch size: dynamically determined by vllm to achieve maximum throughput.
- Models: Qwen/Qwen2.5-7B-Instruct, Qwen/Qwen2.5-VL-7B-Instruct
- Evaluation metrics: throughput.

### test parameters
<details>
<summary> serving parameters</summary>

```json
[
  {
    "test_name": "serving_qwen2_5vl_7B_tp1",
    "qps_list": [
      1,
      4,
      16,
      "inf"
    ],
    "server_parameters": {
      "model": "Qwen/Qwen2.5-VL-7B-Instruct",
      "tensor_parallel_size": 1,
      "swap_space": 16,
      "disable_log_stats": "",
      "disable_log_requests": "",
      "trust_remote_code": "",
      "max_model_len": 16384
    },
    "client_parameters": {
      "model": "Qwen/Qwen2.5-VL-7B-Instruct",
      "backend": "openai-chat",
      "dataset_name": "hf",
      "hf_split": "train",
      "endpoint": "/v1/chat/completions",
      "dataset_path": "lmarena-ai/vision-arena-bench-v0.1",
      "num_prompts": 200
    }
  },
  {
    "test_name": "serving_qwen2_5_7B_tp1",
    "qps_list": [
      1,
      4,
      16,
      "inf"
    ],
    "server_parameters": {
      "model": "Qwen/Qwen2.5-7B-Instruct",
      "tensor_parallel_size": 1,
      "swap_space": 16,
      "disable_log_stats": "",
      "disable_log_requests": "",
      "load_format": "dummy"
    },
    "client_parameters": {
      "model": "Qwen/Qwen2.5-7B-Instruct",
      "backend": "vllm",
      "dataset_name": "sharegpt",
      "dataset_path": "./ShareGPT_V3_unfiltered_cleaned_split.json",
      "num_prompts": 200
    }
  }
]

```
</details>


<details>
<summary>throughput parameters</summary>

```json
[
  {
    "test_name": "throughput_qwen2_5_7B_tp1",
    "parameters": {
      "model": "Qwen/Qwen2.5-7B-Instruct",
      "tensor_parallel_size": 1,
      "load_format": "dummy",
      "dataset_path": "./ShareGPT_V3_unfiltered_cleaned_split.json",
      "num_prompts": 200,
      "backend": "vllm"
    }
  },
  {
    "test_name": "throughput_qwen2_5vl_7B_tp1",
    "parameters": {
      "model": "Qwen/Qwen2.5-VL-7B-Instruct",
      "tensor_parallel_size": 1,
      "backend": "vllm-chat",
      "dataset_name": "hf",
      "hf_split": "train",
      "max_model_len": 16384,
      "dataset_path": "lmarena-ai/vision-arena-bench-v0.1",
      "num_prompts": 200
    }
  }
]


```

</details>


<details>
<summary>latency parameters</summary>

```json
[
  {
    "test_name": "latency_qwen2_5vl_7B_tp1",
    "parameters": {
      "model": "Qwen/Qwen2.5-VL-7B-Instruct",
      "tensor_parallel_size": 1,
      "max_model_len": 16384,
      "num_iters_warmup": 5,
      "num_iters": 15
    }
  },
  {
    "test_name": "latency_qwen2_5_7B_tp1",
    "parameters": {
      "model": "Qwen/Qwen2.5-7B-Instruct",
      "tensor_parallel_size": 1,
      "load_format": "dummy",
      "max_model_len": 16384,
      "num_iters_warmup": 5,
      "num_iters": 15
    }
  }
]

```

</details>


# vllm-ascend v0.7.3 + MindIE Trubo

## Online serving tests

### Qwen2.5-7B-Instruct
| Test name                        |   Request rate (req/s) |   Tput (req/s) |   Output Tput (tok/s) |   TTFT (ms) |   TPOT (ms) |   ITL (ms) |
|:---------------------------------|-----------------------:|---------------:|----------------------:|------------:|------------:|-----------:|
| serving_qwen2_5_7B_tp1_qps_1     |                      1 |       0.95543  |               213.524 |     69.5214 |     23.351  |    22.5373 |
| serving_qwen2_5_7B_tp1_qps_4     |                      4 |       3.15729  |               705.608 |     72.2935 |     30.3927 |    26.7608 |
| serving_qwen2_5_7B_tp1_qps_16    |                     16 |       5.64525  |              1261.63  |     85.6201 |     55.3979 |    36.701  |
| serving_qwen2_5_7B_tp1_qps_inf   |                    inf |       6.647    |              1485.51  |   3198.48   |     50.8949 |    40.9818 |


### Qwen2.5-VL-7B-Instruct
| Test name                        |   Request rate (req/s) |   Tput (req/s) |   Output Tput (tok/s) |   TTFT (ms) |   TPOT (ms) |   ITL (ms) |
|:---------------------------------|-----------------------:|---------------:|----------------------:|------------:|------------:|-----------:|
| serving_qwen2_5vl_7B_tp1_qps_1   |                      1 |       0.997964 |               109.247 |    374.364  |     30.8042 |    22.887  |
| serving_qwen2_5vl_7B_tp1_qps_4   |                      4 |       3.7565   |               411.938 |    301.918  |     67.4147 |    31.0699 |
| serving_qwen2_5vl_7B_tp1_qps_16  |                     16 |       6.2011   |               673.533 |   8744.6    |    158.046  |    64.3575 |
| serving_qwen2_5vl_7B_tp1_qps_inf |                    inf |       5.11639  |               557.508 |  17186.9    |    195.048  |    64.0484 |

# vllm-ascend v0.7.3

## Online serving

### Qwen2.5-7B-Instruct
| Test name                      |   Request rate (req/s) |   Tput (req/s) |   Output Tput (tok/s) |   TTFT (ms) |   TPOT (ms) |   ITL (ms) |
|:-------------------------------|-----------------------:|---------------:|----------------------:|------------:|------------:|-----------:|
| serving_qwen2_5_7B_tp1_qps_1   |                      1 |       0.922267 |               206.113 |     97.8581 |     36.5128 |    35.3481 |
| serving_qwen2_5_7B_tp1_qps_4   |                      4 |       2.79137  |               623.829 |    104.405  |     48.9373 |    41.9421 |
| serving_qwen2_5_7B_tp1_qps_16  |                     16 |       4.37615  |               978.005 |    114.836  |     75.88   |    51.2339 |
| serving_qwen2_5_7B_tp1_qps_inf |                    inf |       5.06881  |              1132.8   |   2845.75   |     62.8063 |    53.0942 |

### Qwen2.5-VL-7B-Instruct
| Test name                        |   Request rate (req/s) |   Tput (req/s) |   Output Tput (tok/s) |   TTFT (ms) |   TPOT (ms) |   ITL (ms) |
|:---------------------------------|-----------------------:|---------------:|----------------------:|------------:|------------:|-----------:|
| serving_qwen2_5vl_7B_tp1_qps_1   |                      1 |       0.993584 |               109.046 |     345.717 |     40.9481 |    32.1247 |
| serving_qwen2_5vl_7B_tp1_qps_4   |                      4 |       3.66915  |               402.579 |     321.537 |     86.7003 |    42.4031 |
| serving_qwen2_5vl_7B_tp1_qps_16  |                     16 |       6.07012  |               668.412 |    8580.35  |    164.858  |    71.5467 |
| serving_qwen2_5vl_7B_tp1_qps_inf |                    inf |       5.26736  |               579.831 |   14326.2   |    208.966  |    73.1931 |

## Offline tests
### Latency tests


| Test name                |   Mean latency (ms) |   Median latency (ms) |   P99 latency (ms) |
|:-------------------------|--------------------:|----------------------:|-------------------:|
| latency_qwen2_5vl_7B_tp1 |             4128.36 |               4126.04 |            4200.24 |
| latency_qwen2_5_7B_tp1   |             4274.96 |               4284.9  |            4335.71 |

### Throughput tests

| Test name                   |   Num of reqs |   Total num of tokens |   Elapsed time (s) |   Tput (req/s) |   Tput (tok/s) |
|:----------------------------|--------------:|----------------------:|-------------------:|---------------:|---------------:|
| throughput_qwen2_5_7B_tp1   |           200 |                 88257 |            40.8233 |        4.89917 |        2161.93 |
| throughput_qwen2_5vl_7B_tp1 |           200 |                203673 |            69.9566 |        2.85892 |        2911.42 |



# Conclusion
First, we compared the online serving  results with and without mindie_turbo integration

## Qwen2.5-7B-Instruct
| QPS | Metric      | vllm-ascend+ mindie_turbo | vllm-ascend  | Optimization      |
| --- | ----------- | ------- | -------- | --------------- |
| 1   | Tput        | 0.95543 | 0.922267 | +3.60%          |
|     | Output Tput | 213.524 | 206.113  | +3.59%          |
|     | TTFT        | 69.5214 | 97.8581  | +28.98%     |
|     | TPOT        | 23.351  | 36.5128  | +36.05%     |
|     | ITL         | 22.5373 | 35.3481  | +36.24%     |
| 4   | Tput        | 3.15729 | 2.79137  | +13.11%         |
|     | Output Tput | 705.608 | 623.829  | +13.09%         |
|     | TTFT        | 72.2935 | 104.405  | +30.78%     |
|     | TPOT        | 30.3927 | 48.9373  | +37.91%   |
|     | ITL         | 26.7608 | 41.9421  | +36.19%     |
| 16  | Tput        | 5.64525 | 4.37615  | +28.96%         |
|     | Output Tput | 1261.63 | 978.005  | +28.98%         |
|     | TTFT        | 85.6201 | 114.836  | +25.46%     |
|     | TPOT        | 55.3979 | 75.88    | +26.98%    |
|     | ITL         | 36.701  | 51.2339  | +28.37%     |
| inf | Tput        | 6.647   | 5.06881  | +31.12%         |
|     | Output Tput | 1485.51 | 1132.8   | +31.21%         |
|     | TTFT        | 3198.48 | 2845.75  | **-12.41%** |
|     | TPOT        | 50.8949 | 62.8063  | +18.96%     |
|     | ITL         | 40.9818 | 53.0942  | +22.80%     |

## Qwen2.5-VL-7B-Instruct

| QPS | Metric      | vllm-ascend+ mindie_turbo | vllm-ascend     | Optimization      |
| --- | ----------- | -------- | -------- | ------------- |
| 1   | Tput        | 0.997964 | 0.993584 | +0.44%     |
|     | Output Tput | 109.247  | 109.046  | +0.18%      |
|     | TTFT        | 374.364  | 345.717  | -8.27%  |
|     | TPOT        | 30.8042  | 40.9481  |  +24.78% |
|     | ITL         | 22.887   | 32.1247  | +28.74% |
| 4   | Tput        | 3.7565   | 3.66915  | +2.38%     |
|     | Output Tput | 411.938  | 402.579  | +2.33%      |
|     | TTFT        | 301.918  | 321.537  | +6.10%  |
|     | TPOT        | 67.4147  | 86.7003  |  +22.22% |
|     | ITL         | 31.0699  | 42.4031  |  +26.71% |
| 16  | Tput        | 6.2011   | 6.07012  | +2.16%      |
|     | Output Tput | 673.533  | 668.412  | +0.77%      |
|     | TTFT        | 8744.6   | 8580.35  | -1.91% |
|     | TPOT        | 158.046  | 164.858  | +4.14%  |
|     | ITL         | 64.3575  | 71.5467  |  +10.06% |
| inf | Tput        | 5.11639  | 5.26736  | -2.87%  |
|     | Output Tput | 557.508  | 579.831  | -3.85%  |
|     | TTFT        | 17186.9  | 14326.2  |  -20.03% |
|     | TPOT        | 195.048  | 208.966  | +6.63%  |
|     | ITL         | 64.0484  | 73.1931  | +12.50% |
