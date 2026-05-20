# Issue #5559: [New Model]: GLM 4.6

**类型**: Issue

## 问题背景
### The model to consider.

GLM-4.6 部署问题
1、服务器：910B3 64G 4节点 32卡 部署
2、镜像：vllm-ascend:v0.11.0rc2
3、问题
1）模型推理速度慢
2）模型在200K 上下文参数设置无法启动服务，报错 OOM
3）模型在128k 上下文推理时，输入文本大于约8k的时候报错 OOM
4）多次调试--gpu-memory-utilization 从0.8到0.95之间尝试并没有解决问题
服务启动命令如下，需技术支持：
#!/bin/sh
# export VLLM_USE_V1=1

export VLLM_API_KEY="xxxxx"

export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256

nic_name="bond0"
local_ip="xxxxx"
node0_ip="xxxxx"

export VLLM_USE_MODELSCOPE=True
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

export OMP_PROC_BIND=false
export OMP_NUM_THREADS=64 # 100
export HCCL_BUFFSIZE=256

nohup vllm serve /mnt/data1/GLM-4.6 \
        --host 0.0.0.0 \
        --port 11025 \
        --data-parallel-size 4 \
        --data-parallel-size-local 1 \
        --data-parallel-address $node0_ip \
        --data-parallel-rpc-port 13389 \
        --tensor-parallel-si

## 基本信息
- **编号**: #5559
- **作者**: liuainlp
- **创建时间**: 2025-12-31T09:29:20Z
- **关闭时间**: 2026-02-14T01:07:34Z
- **标签**: new model

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5559)
