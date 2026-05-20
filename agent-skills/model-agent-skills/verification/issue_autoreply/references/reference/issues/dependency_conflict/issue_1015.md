# Issue #1015: [Bug]: v0.8.4rc2 - The inference performance of QwQ-32B-w8a8 is worse than fp16

## 基本信息

- **编号**: #1015
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1015
- **创建时间**: 2025-05-29T11:46:35Z
- **关闭时间**: 2025-07-13T09:39:28Z
- **更新时间**: 2025-07-13T09:39:28Z
- **提交者**: @tingyiz97
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

- version: v0.8.4rc2
- NPU: 910B3


### 🐛 Describe the bug

Server start-up command:
```
VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --model /mnt/models/QwQ-32B-w8a8-v1 -tp 4 --gpu_memory_utilization 0.8 --max_num_seqs 256 --served-model-name QwQ-32B
```

Benchamrk script: https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py

w8a8 benchmarks result:
```
============ Serving Benchmark Result ============
Successful requests:                     10        
Benchmark duration (s):                  487.92    
Total input tokens:                      2087      
Total generated tokens:                  5120      
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         10.49     
Total Token throughput (tok/s):          14.77     
---------------Time to First Token----------------
Mean TTFT (ms):                          160.36    
Median TTFT (ms):                        170.86    
P99 TTFT (ms):                           190.28    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          95.17     
Median TPOT (ms):                        94.71     
P99 TPOT (ms):                           97.40     
---------------Inter-token Latency----------------
Mean ITL (ms):                           94.98     
Median ITL (ms):                         93.93     
P99 ITL (ms):                            119.94    
==================================================
```

fp16 benchmark result;
```
============ Serving Benchmark Result ============
Successful requests:                     10        
Benchmark duration (s):                  408.37    
Total input tokens:                      2087      
Total generated tokens:                  5120      
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         12.54     
Total Token throughput (tok/s):          17.65     
---------------Time to First Token----------------
Mean TTFT (ms):                          134.02    
Median TTFT (ms):                        144.38    
P99 TTFT (ms):                           158.05    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          79.65     
Median TPOT (ms):                        79.62     
P99 TPOT (ms):                           81.44     
---------------Inter-token Latency----------------
Mean ITL (ms):                           79.50     
Median ITL (ms):                         78.30     
P99 ITL (ms):                            105.79    
==================================================
```
