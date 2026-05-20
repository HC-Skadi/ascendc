# Issue #971: [Bug]: When moe ep=16 etp=1, the result is normal. When moe ep=1 etp=16, the result is abnormal.

## 基本信息

- **编号**: #971
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/971
- **创建时间**: 2025-05-27T08:00:37Z
- **关闭时间**: 2025-06-15T07:23:21Z
- **更新时间**: 2025-06-15T07:23:21Z
- **提交者**: @ttanzhiqiang
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

<details>
nohup python -m vllm.entrypoints.openai.api_server --model=/mnt/deepseek/DeepSeek-R1-W8A8-VLLM \
 --trust-remote-code \
 --distributed-executor-backend=mp \
 -tp=16 \
 -dp=1 \
 --port 8006 \
 --max-num-seqs 24 \
 --max-model-len 32768 \
 --max-num-batched-tokens 32768 \
 --block-size 128 \
 --enable-expert-parallel \
 --compilation_config 0 \
 --gpu-memory-utilization 0.96 \
 --additional-config '{"expert_tensor_parallel_size":1, "ascend_scheduler_config":{}}' &> run.log &

<img width="1709" alt="Image" src="https://github.com/user-attachments/assets/75e02395-cadf-4ebd-a832-9396e50da4f9" />


nohup python -m vllm.entrypoints.openai.api_server --model=/mnt/deepseek/DeepSeek-R1-W8A8-VLLM \
 --trust-remote-code \
 --distributed-executor-backend=mp \
 -tp=16 \
 -dp=1 \
 --port 8006 \
 --max-num-seqs 24 \
 --max-model-len 32768 \
 --max-num-batched-tokens 32768 \
 --block-size 128 \
 --enable-expert-parallel \
 --compilation_config 0 \
 --gpu-memory-utilization 0.96 \
 --additional-config '{"expert_tensor_parallel_size":16, "ascend_scheduler_config":{}}' &> run.log &

<img width="1710" alt="Image" src="https://github.com/user-attachments/assets/db827e65-b39b-4b98-82b3-3f43b238a6e6" />

The principle of the problem：In the case of etp16 there is no parallel processing
<img width="1550" alt="Image" src="https://github.com/user-attachments/assets/a609ff3b-e231-431b-b66f-907ea53c9b78" />



</details>


### 🐛 Describe the bug

nohup python -m vllm.entrypoints.openai.api_server --model=/mnt/deepseek/DeepSeek-R1-W8A8-VLLM \
 --trust-remote-code \
 --distributed-executor-backend=mp \
 -tp=16 \
 -dp=1 \
 --port 8006 \
 --max-num-seqs 24 \
 --max-model-len 32768 \
 --max-num-batched-tokens 32768 \
 --block-size 128 \
 --enable-expert-parallel \
 --compilation_config 0 \
 --gpu-memory-utilization 0.96 \
 --additional-config '{"expert_tensor_parallel_size":16, "ascend_scheduler_config":{}}' &> run.log &
