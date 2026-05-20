# Issue #4096: [Bug]: vllm-ascend 部署 DeepSeek-V3.2-Exp-W8A8 出现精度问题

## 基本信息

- **编号**: #4096
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4096
- **创建时间**: 2025-11-10T11:31:25Z
- **关闭时间**: 2025-12-18T01:58:11Z
- **更新时间**: 2025-12-18T01:58:12Z
- **提交者**: @Alexander-Qiu
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

# 宿主机环境：
HDK 25.2.T5
操作系统	CuLinux3.0
Ascend CANN版本	8.2.RC1
机器型号	Atlas 800T A3
CPU	Kunpeng 920 3.0G
AI加速芯片	Ascend 910C

# 部署镜像  
docker pull quay.io/ascend/vllm-ascend:v0.11.0rc0-a3-deepseek-v3.2-exp

# 部署指令
参考： https://docs.vllm.ai/projects/ascend/en/latest/tutorials/DeepSeek-V3.2-Exp.html

#!/bin/sh
export VLLM_USE_MODELSCOPE=true
vllm serve vllm-ascend/DeepSeek-V3.2-Exp-W8A8 \
--host 0.0.0.0 \
--port 8000 \
--tensor-parallel-size 16 \
--seed 1024 \
--quantization ascend \
--served-model-name deepseek_v3.2 \
--max-num-seqs 16 \
--max-model-len 17450 \
--max-num-batched-tokens 17450 \
--enable-expert-parallel \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true,"graph_batch_sizes":[16]}}'

### 🐛 Describe the bug

# 问题描述
出现精度问题，提问官方问题 “The capitalof France is” 回答正确

<img width="3188" height="530" alt="Image" src="https://github.com/user-attachments/assets/ba08ba91-2f7e-4666-9a6d-6ced693938bc" />

提问别的问题，例如你是谁等，则出现一定程度胡言乱语问题

<img width="3229" height="864" alt="Image" src="https://github.com/user-attachments/assets/bd1ce096-0050-47e7-83e6-089e8b366952" />
