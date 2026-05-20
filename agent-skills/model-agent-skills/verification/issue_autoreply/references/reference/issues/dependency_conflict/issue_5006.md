# Issue #5006: [Bug]: vllm-ascend serve Qwen3-235B-A22B model failed. ValueError: Following weights were not initialized from checkpoint

## 基本信息

- **编号**: #5006
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5006
- **创建时间**: 2025-12-15T02:05:24Z
- **关闭时间**: 2025-12-15T09:13:34Z
- **更新时间**: 2025-12-15T09:13:34Z
- **提交者**: @oasis-0927
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc3

package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

I followed the instruction on https://docs.vllm.ai/projects/vllm-ascend-cn/zh-cn/latest/tutorials/Qwen3-235B-A22B.html#multi-node-deployment-with-mp-recommended 
```bash
#!/bin/sh
# Load model from ModelScope to speed up download
export VLLM_USE_MODELSCOPE=true
# To reduce memory fragmentation and avoid out of memory
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="bond0"
local_ip="192.168.0.62"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=1024
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

vllm serve /data/Qwen3-235B-A22B/ \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 2 \
--api-server-count 2 \
--data-parallel-size-local 1 \
--data-parallel-address $local_ip \
--data-parallel-rpc-port 13389 \
--seed 1024 \
--served-model-name qwen3 \
--tensor-parallel-size 8 \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 32768 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--async-scheduling \
--gpu-memory-utilization 0.9 \
```
This command raise the following error:
```bash
ValueError: Following weights were not initialized from checkpoint: {'model.layers.73.mlp.gate.weight', 'model.layers.57.self_attn.qkv_proj.weight', 'model.layers.5.mlp.experts.w13_weight', 'model.layers.5.self_attn.k_norm.weight', 'model.layers.72.post_attention_layernorm.weight', 'model.layers.73.mlp.experts.w2_weight', 'model.layers.56.post_attention_layernorm.weight', 'model.layers.35.mlp.experts.w13_weight', 'model.layers.5.mlp.experts.w2_weight', 'model.layers.5.self_attn.o_proj.weight', 'model.layers.58.self_attn.qkv_proj.weight', 'model.layers.73.self_attn.qkv_proj.weight', 'model.layers.5.self_attn.q_norm.weight', 'model.layers.56.input_layernorm.weight', 'model.layers.57.mlp.gate.weight', 'model.layers.35.mlp.experts.w2_weight', 'model.layers.5.self_attn.qkv_proj.weight', 'model.layers.57.mlp.experts.w13_weight', 'model.layers.4.post_attention_layernorm.weight', 'model.layers.73.self_attn.o_proj.weight', 'model.layers.58.self_attn.q_norm.weight', 'model.layers.57.self_attn.o_proj.weight', 'model.layers.5.mlp.gate.weight', 'model.layers.58.self_attn.k_norm.weight', 'model.layers.57.self_attn.k_norm.weight', 'model.layers.57.mlp.experts.w2_weight', 'model.layers.73.mlp.experts.w13_weight', 'model.layers.73.self_attn.k_norm.weight', 'model.layers.4.input_layernorm.weight', 'model.layers.73.self_attn.q_norm.weight', 'model.layers.57.post_attention_layernorm.weight', 'model.layers.58.mlp.gate.weight', 'model.layers.72.input_layernorm.weight', 'model.layers.57.input_layernorm.weight', 'model.layers.57.self_attn.q_norm.weight', 'model.layers.58.self_attn.o_proj.weight'}
```
The model weights were downloaded from [modelscope](https://www.modelscope.cn/models/Qwen/Qwen3-235B-A22B/files) and  stored on local path.
