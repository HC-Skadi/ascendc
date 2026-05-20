# Issue #6829: [Installation]: Atlas 800I A2单机运行Qwen3-Next-80B-A3B-Instruct加载失败

## 基本信息

- **编号**: #6829
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6829
- **创建时间**: 2026-02-26T09:02:00Z
- **关闭时间**: 2026-03-02T10:34:42Z
- **更新时间**: 2026-03-02T10:34:42Z
- **提交者**: @ranzhengfeng
- **评论数**: 3

## 标签

installation

## 问题描述

### Your current environment
Docker,镜像quay.io/ascend/vllm-ascend:v0.14.0rc1
### 运行命令：
```
export HCCL_INTRA_ROCE_ENABLE=0
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_P2P_DISABLE=0
export HCCL_P2P_ENABLE=1
export VLLM_HCCL_ENABLE_P2P_CHECK=0
export NCCL_SOCKET_IFNAME=lo
export GLOO_SOCKET_IFNAME=lo
export HCCL_CONNECT_TIMEOUT=3600
# 限制权重并行加载，防止 8 个进程在内存分配上打架
export VLLM_WEIGHT_LOADING_PARALLELISM=1
# 昇腾专用：允许内存分段扩展，减少初次申请超大内存被拒绝的概率
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
# 增加超时阈值，80B 模型解析很慢
export VLLM_RPC_TIMEOUT_MS=600000


vllm serve --served-model-name Qwen3-Next-80B-A3B-Instruct \
  --model /data/models/Qwen3-Next-80B-A3B-Instruct-b \
  --tensor-parallel-size 8 \
  --trust-remote-code \
  --distributed-executor-backend mp \
  --max-model-len 512           \
  --gpu-memory-utilization 0.75   \
  --max-num-batched-tokens 512  \
  --max-num-seqs 64              \
  --block-size 16                 \
  --swap-space 0                  \
  --disable-custom-all-reduce \
  --enforce-eager \
  --port 8002 \
  --host 0.0.0.0 
```
### 运行日志：
```
INFO 02-26 08:38:04 [parallel_state.py:1214] world_size=8 rank=0 local_rank=0 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
INFO 02-26 08:38:04 [parallel_state.py:1214] world_size=8 rank=7 local_rank=7 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
INFO 02-26 08:38:04 [parallel_state.py:1214] world_size=8 rank=3 local_rank=3 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
INFO 02-26 08:38:04 [parallel_state.py:1214] world_size=8 rank=6 local_rank=6 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
INFO 02-26 08:38:04 [parallel_state.py:1214] world_size=8 rank=4 local_rank=4 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
INFO 02-26 08:38:05 [parallel_state.py:1214] world_size=8 rank=5 local_rank=5 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
INFO 02-26 08:38:05 [parallel_state.py:1214] world_size=8 rank=1 local_rank=1 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
INFO 02-26 08:38:05 [parallel_state.py:1214] world_size=8 rank=2 local_rank=2 distributed_init_method=tcp://127.0.0.1:59091 backend=hccl
[Gloo] Rank 0 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 1 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 3 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 4 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 2 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 5 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 6 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 7 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 0 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 1 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 2 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 5 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 3 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 7 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 4 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 6 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 2 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 4 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 1 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 6 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 5 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 3 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 7 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 0 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 2 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 2, EP rank 2
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 6 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 6, EP rank 6
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 5 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 5, EP rank 5
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 1 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 1, EP rank 1
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 3 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 3, EP rank 3
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 7 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 7, EP rank 7
INFO 02-26 08:38:05 [parallel_state.py:1425] rank 4 in world size 8 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 4, EP rank 4
[Gloo] Rank 0 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 4 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 2 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 5 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 1 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 3 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 7 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
[Gloo] Rank 6 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7
(Worker_TP6 pid=117) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP4 pid=115) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP0 pid=111) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP7 pid=118) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP1 pid=112) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP2 pid=113) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP5 pid=116) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP3 pid=114) INFO 02-26 08:38:05 [model_runner_v1.py:2188] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct-b...
(Worker_TP0 pid=111) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP0 pid=111)   return func(*args, **kwargs)
(Worker_TP5 pid=116) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP5 pid=116)   return func(*args, **kwargs)
(Worker_TP6 pid=117) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP6 pid=117)   return func(*args, **kwargs)
(Worker_TP4 pid=115) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP4 pid=115)   return func(*args, **kwargs)
(Worker_TP2 pid=113) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP2 pid=113)   return func(*args, **kwargs)
(Worker_TP1 pid=112) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP1 pid=112)   return func(*args, **kwargs)
(Worker_TP7 pid=118) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP7 pid=118)   return func(*args, **kwargs)
(Worker_TP3 pid=114) /usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_device.py:103: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:253.)
(Worker_TP3 pid=114)   return func(*args, **kwargs)
Loading safetensors checkpoint shards:   0% Completed | 0/41 [00:00<?, ?it/s]
```
---
改为  --tensor-parallel-size 4  --pipeline-parallel-size 2 后，在27%卡住。


