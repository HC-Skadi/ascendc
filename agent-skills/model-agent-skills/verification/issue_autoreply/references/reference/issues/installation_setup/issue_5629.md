# Issue #5629: [Usage]: 双八卡910B节点部署DeepSeek-V3.1-Terminus-w8a8-mtp-QuaRot报错

**类型**: Issue

## 问题背景
### Your current environment

```
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0

vllm serve /root/.cache/DeepSeek-V3.1-Terminus-w8a8-mtp-QuaRot \
--host 0.0.0.0 \
--port 8004 \
--data-parallel-size 4 \
--data-parallel-size-local 2 \
--data-parallel-address $node0_ip \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--quantization ascend \
--seed 1024 \
--served-model-name DeepSeek-V3.1-Terminus \
--enable-expert-parallel \
--async-scheduling \
--max-num-seqs 64 \
--max-model-len 16384 \
--max-num-batched-tokens 16384 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--speculative-config '

## 基本信息
- **编号**: #5629
- **作者**: StormMapleleaf
- **创建时间**: 2026-01-06T03:32:44Z
- **关闭时间**: 2026-01-06T08:54:58Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5629)
