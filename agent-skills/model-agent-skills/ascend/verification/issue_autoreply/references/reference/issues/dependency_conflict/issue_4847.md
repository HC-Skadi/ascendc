# Issue #4847: [Bug]: Qwen3-Coder-480B-A35B-Instruct-w8a8-QuaRot双节点运行报错

## 基本信息

- **编号**: #4847
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4847
- **创建时间**: 2025-12-09T14:58:24Z
- **关闭时间**: 2025-12-31T06:34:37Z
- **更新时间**: 2025-12-31T06:34:37Z
- **提交者**: @puchine
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>容器配置</summary>

```text
起容器的命令：
docker run -itd --net=host --privileged \
--name suys_vllm \
--shm-size=500g \
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
-v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
-v /usr/local/sbin/npu-smi:/usr/local/sbin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /data/Qwen3-Coder-480B-A35B-Instruct-w8a8-QuaRot/:/data/Qwen3-Coder-480B-A35B-Instruct-w8a8-QuaRot/ \
quay.io/ascend/vllm-ascend:v0.11.0rc2 bash

Node0配置：

#!/bin/sh

nic_name="bond0"
local_ip="192.168.0.125"

export VLLM_USE_MODELSCOPE=True
export HCCL_IF_IP=192.168.0.125
export GLOO_SOCKET_IFNAME=bond0
export TP_SOCKET_IFNAME=bond0
export HCCL_SOCKET_IFNAME=bond0
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export HCCL_BUFFSIZE=1024

Node0运行命令：
vllm serve /data/Qwen3-Coder-480B-A35B-Instruct-w8a8-QuaRot \
--host 0.0.0.0 \
--port 8004 \
--data-parallel-size 4 \
--data-parallel-size-local 2 \
--data-parallel-address 192.168.0.125 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--seed 1024 \
--served-model-name qwen3 \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 8192 \
--quantization ascend \
--max-num-batched-tokens 8192 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.95 \
--additional-config '{"torchair_graph_config":{"enabled":true}}'

Node1配置：
#!/bin/sh

nic_name="bond0"
local_ip="192.168.0.100"

node0_ip="192.168.0.125"

export VLLM_USE_MODELSCOPE=True
export HCCL_IF_IP=192.168.0.100
export GLOO_SOCKET_IFNAME=bond0
export TP_SOCKET_IFNAME=bond0
export HCCL_SOCKET_IFNAME=bond0
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export HCCL_BUFFSIZE=1024

Node1运行命令：
vllm serve /data/Qwen3-Coder-480B-A35B-Instruct-w8a8-QuaRot \
--host 0.0.0.0 \
--port 8004 \
--headless \
--data-parallel-size 4 \
--data-parallel-size-local 2 \
--data-parallel-start-rank 2 \
--data-parallel-address 192.168.0.125 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--seed 1024 \
--quantization ascend \
--served-model-name qwen3 \
--max-num-seqs 16 \
--max-model-len 8192 \
--max-num-batched-tokens 8192 \
--enable-expert-parallel \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.95 \
--additional-config '{"torchair_graph_config":{"enabled":true}}'
```


</details>


### 🐛 Describe the bug

完整报错信息见附件，
不清楚究竟是并行出了差错还是该模型有其他的问题

<img width="1161" height="658" alt="Image" src="https://github.com/user-attachments/assets/1cfa12ed-731c-48af-8fdd-0dd9b3158831" />

<img width="1150" height="648" alt="Image" src="https://github.com/user-attachments/assets/544ea86b-5b51-4260-9e85-780d7b8733f9" />

[vllm.log](https://github.com/user-attachments/files/24057755/vllm.log)
