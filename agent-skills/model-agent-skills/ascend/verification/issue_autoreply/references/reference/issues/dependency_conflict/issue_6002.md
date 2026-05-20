# Issue #6002: [Bug]:aclgraph图捕获模式不支持

## 基本信息

- **编号**: #6002
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6002
- **创建时间**: 2026-01-19T08:06:47Z
- **关闭时间**: 2026-01-20T02:11:04Z
- **更新时间**: 2026-01-20T02:11:04Z
- **提交者**: @Mitchellax
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

A2 双机十六卡混部，在开启图模式后**某些情况**下，会在aclgraph replaying时报错退出。HDK版本25.2.3，使用镜像部署服务。

### 🐛 Describe the bug

目前能观察到的情况是：开启图下发异常，单算子服务正常；均在显存比较紧张时出现问题；在plog中均存在`MemCopySync:Memory copy sync failed`、`rtMemcpy:ErrCode=107030, desc=[the current capture mode does not support this operation]`。

能够确认的是：捕获模式在aclgraph下不支持，调用接口的地方（框架侧）需要切换模式。参考[CANN - aclmdlRICaptureThreadExchangeMode](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/appdevgapi/aclcppdevg_03_1788.html)，对应PTA接口不明。

稳定复现的场景有：

##### 场景1

vllm-ascend 0.11.0镜像，DSV3.1 w8a8模型：

主节点：

```bash
export HCCL_OP_EXPANSION_MODE="AIV"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0

vllm serve /data1/DeepSeek-V3.1-w8a8-function_call/ \
    --host 0.0.0.0 \
    --port 1025 \
    --data-parallel-size 4 \
    --data-parallel-size-local 2 \
    --data-parallel-start-rank 0 \
    --data-parallel-address $master_ip \
    --data-parallel-rpc-port 13389 \
    --tensor-parallel-size 4 \
    --quantization ascend \
    --seed 1024 \
    --served-model-name deepseek \
    --enable-expert-parallel \
    --max-num-seqs 20 \
    --max-model-len 8192 \
    --max-num-batched-tokens 4096 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.9 \
    --speculative-config '{"num_speculative_tokens": 1, "method":"deepseek_mtp"}' \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --additional-config \
    '{"ascend_scheduler_config":{"enabled":false},"torchair_graph_config":{"enabled":false}}'
```

从节点：

```bash
export HCCL_OP_EXPANSION_MODE="AIV"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0

vllm serve /data1/DeepSeek-V3.1-w8a8-function_call/ \
    --host 0.0.0.0 \
    --port 1025 \
    --headless \
    --data-parallel-size 4 \
    --data-parallel-size-local 2 \
    --data-parallel-start-rank 2 \
    --data-parallel-address $master_ip \
    --data-parallel-rpc-port 13389 \
    --tensor-parallel-size 4 \
    --quantization ascend \
    --seed 1024 \
    --served-model-name deepseek \
    --enable-expert-parallel \
    --max-num-seqs 20 \
    --max-model-len 8192 \
    --max-num-batched-tokens 4096 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.9 \
    --speculative-config '{"num_speculative_tokens": 1, "method":"deepseek_mtp"}' \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --additional-config \
    '{"ascend_scheduler_config":{"enabled":false},"torchair_graph_config":{"enabled":false}}'
```

此场景下，接受请求立即报错退出。

##### 场景2

vllm-ascend 0.13.0RC1镜像，DSV3.2 w8a8模型，没有开启MTP：

主节点：

```bash
export HCCL_OP_EXPANSION_MODE="AIV"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=200
export VLLM_ASCEND_ENABLE_MLAPO=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_FLASHCOMM1=0
export HCCL_CONNECT_TIMEOUT=120
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTTRA_ROCE_ENABLE=0
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/lib64:$LD_LIBRARY_PATH

vllm serve /data/DeepSeek-V3.2-W8A8 \
--host 0.0.0.0 \
--port 8077 \
--data-parallel-size 2 \
--data-parallel-size-local 1 \
--data-parallel-address 10.238.58.157 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 8 \
--quantization ascend \
--seed 1024 \
--served-model-name deepseekv3_2 \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 32000 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes":[3,6,9,12,15]}'
```

从节点：

```bash
export HCCL_OP_EXPANSION_MODE="AIV"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=200
export VLLM_ASCEND_ENABLE_MLAPO=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_FLASHCOMM1=0
export HCCL_CONNECT_TIMEOUT=120
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTTRA_ROCE_ENABLE=0
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/lib64:$LD_LIBRARY_PATH

vllm serve /data/DeepSeek-V3.2-W8A8 \
--host 0.0.0.0 \
--port 8077 \
--headless \
--data-parallel-size 2 \
--data-parallel-size-local 1 \
--data-parallel-start-rank 1 \
--data-parallel-address 10.238.58.157 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 8 \
--quantization ascend \
--seed 1024 \
--served-model-name deepseekv3_2 \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 32000 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes":[3,6,9,12,15]}'
```

服务拉起后，使用4000/2的6条请求预热模型，在第4条请求后报错退出。
