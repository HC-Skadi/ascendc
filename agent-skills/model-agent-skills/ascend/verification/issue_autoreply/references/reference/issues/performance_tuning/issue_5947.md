# Issue #5947: [Bug]: 双机 A2 800 (64Gx8)  vllm-ascend:v0.13.0rc1 无法拉起 DeepSeek-R1-0528-W8A8 : call aclnnMoeDistributeDispatchV3 failed 561000

## 基本信息

- **编号**: #5947
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5947
- **创建时间**: 2026-01-16T05:45:49Z
- **关闭时间**: 2026-01-20T03:35:49Z
- **更新时间**: 2026-01-23T06:26:05Z
- **提交者**: @shilongx
- **评论数**: 2

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

<details>
<summary>

关键问题：双机 A2 800 (64Gx8)  vllm-ascend:v0.13.0rc1 无法拉起 DeepSeek-R1-0528-W8A8    

关键报错信息：operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-16-04:52:41 (PID:542, Device:3, RankID:-1) ERR00100 PTA call acl api failed.
[PID: 542] 2026-01-16-04:52:41.266.655 Allocation_Failure(EI0007): Failed to allocate resource[qp] with info [aicpu rank:7,localUserrank:7,localIpAddr: 100.97.2.72,deviceLogicId:3,send_cq_depth:32768]. Reason: Memory resources are exhausted.
</summary>

# 1、基本信息
```text
=== 操作系统信息 ===                                  
NAME="openEuler"                                     
VERSION="22.03 LTS"                                                                                       
=== 内核与架构 ===                                                                          
Linux worker-25 5.10.0-60.18.0.50.oe2203.aarch64 #1 SMP Wed Mar 30 02:43:08 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux 

=== CPU 信息 ===                                                                           
Architecture:                    aarch64                                                   
CPU(s):                          192       

=== 华为服务器型号 ===                                                                      
 Product Name          : Atlas 800 9000 A2
```

```text
vllm-ascend:v0.13.0rc1
```
```text
模型参数来源：https://modelscope.cn/models/vllm-ascend/DeepSeek-R1-0528-W8A8
```

# 2、操作记录

## 两个节点机子分别启动容器 
```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.13.0rc1
export NAME=deepseek-r1-0528-w8a8

sudo docker run --rm \
--name $NAME \
--net=host \
--shm-size=1g \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /etc/hccn.conf:/etc/hccn.conf \
-v /usr/bin/hccn_tool:/usr/bin/hccn_tool \
-v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /data/models/DeepSeek-R1-0528-W8A8:/data/models/DeepSeek-R1-0528-W8A8:ro \
-p 18034:8000 \
-d $IMAGE bash -c "tail -f /dev/null"

docker exec -it deepseek-r1-0528-w8a8 bash
```
## 两个节点容器分别执行 vllm 命令

主节点 Node 0
```bash
nic_name="bond0.150"
local_ip="xx.xx.xx.21"

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
export VLLM_USE_MODELSCOPE=True

vllm serve /data/models/DeepSeek-R1-0528-W8A8 \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 8 \
--data-parallel-size-local 2 \
--data-parallel-address $local_ip \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 8 \
--quantization ascend \
--seed 1024 \
--served-model-name deepseek_r1 \
--enable-expert-parallel \
--async-scheduling \
--max-num-seqs 16 \
--max-model-len 16384 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--gpu-memory-utilization 0.92 \
--speculative-config '{"num_speculative_tokens":3,"method":"mtp"}' \
--compilation-config '{"cudagraph_capture_sizes":[4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}'
```
从节点 Node 1
```bash
nic_name="bond0.150"
local_ip="xx.xx.xx.22"
node0_ip="xx.xx.xx.21" # same as the local_IP address in node 0

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
export VLLM_USE_MODELSCOPE=True

vllm serve /data/models/DeepSeek-R1-0528-W8A8 \
--host 0.0.0.0 \
--port 8000 \
--headless \
--data-parallel-size 8 \
--data-parallel-size-local 2 \
--data-parallel-start-rank 2 \
--data-parallel-address $node0_ip \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 8 \
--quantization ascend \
--seed 1024 \
--served-model-name deepseek_r1 \
--enable-expert-parallel \
--async-scheduling \
--max-num-seqs 16 \
--max-model-len 16384 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--gpu-memory-utilization 0.92 \
--speculative-config '{"num_speculative_tokens":3,"method":"mtp"}' \
--compilation-config '{"cudagraph_capture_sizes":[4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}'
```

# 3、日志记录
详见附件


</details>

[Node1日志记录.log](https://github.com/user-attachments/files/24661938/Node1.log)
[Node0日志记录.log](https://github.com/user-attachments/files/24661937/Node0.log)
