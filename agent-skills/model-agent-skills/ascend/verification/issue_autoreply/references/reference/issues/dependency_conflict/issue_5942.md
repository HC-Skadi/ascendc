# Issue #5942: [Bug]: 在双机800I A2上，使用vllm-ascend v0.13.0rc1拉起 DSv3.2-w8a8模型，DP4 TP4 一直卡住拉不起来（DP2 TP8可以拉起来）

## 基本信息

- **编号**: #5942
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5942
- **创建时间**: 2026-01-16T02:30:52Z
- **关闭时间**: 2026-01-20T02:32:11Z
- **更新时间**: 2026-01-20T02:32:11Z
- **提交者**: @sjm0522
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

服务器：Atlas800IA2 *2 （双机混部16卡）
模型：DSv3.2-w8a8
vllm-ascend：直接使用镜像vllm-ascend v0.13.0rc1（在镜像中安装了triton-ascend==3.2.0.dev2025110717）

### 🐛 Describe the bug

<details>
<summary>The output of `python collect_env.py`</summary>

在双机800I A2上   使用vllm-ascend v0.13.0rc1  拉起 DSv3.2-w8a8模型     配置参数--max-num-seqs 2 \
--max-model-len 40000 \
--max-num-batched-tokens 4096 \    
DP4 TP4 拉不起来  一直卡在下图（DP2 TP8可以拉起来）

<img width="1705" height="732" alt="Image" src="https://github.com/user-attachments/assets/7d75362e-9d43-4024-9f62-a92331a811af" />

和DP2TP8比对，正常接下应该是如下图打印的红框中的日志

<img width="1678" height="761" alt="Image" src="https://github.com/user-attachments/assets/640e5034-cb2e-4565-9249-fa3f58b7e2f5" />

对比DP2 TP8发现DP4TP4的后台进程一直没有下图红框中的进程
<img width="1683" height="894" alt="Image" src="https://github.com/user-attachments/assets/cef0f5e5-2b7d-42b4-9c0c-81d0fb941409" />

实际操作步骤
1、拉取vllm-ascend v0.13.0rc1镜像（并在镜像中安装了triton-ascend==3.2.0.dev2025110717）
2、配置双机NPU卡的网络环境
3、配置node0、node1的脚本，如下
node0配置：
#!/bin/sh
nic_name="enp61s0f0"
local_ip="x.x.x.2"
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=200
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=0
export HCCL_CONNECT_TIMEOUT=120
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTTRA_ROCE_ENABLE=0
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/lib64:$LD_LIBRARY_PATH
export VLLM_NIXL_ABORT_REQUEST_TIMEOUT=300000
export ASCEND_AGGREGATE_ENABLE=1
export ASCEND_TRANSPORT_PRINT=1
vllm serve /home/openlab/deepseek/DeepSeek-V3.2-w8a8-vllm-ascend/ \
--host x.x.x.2 \
--port 8000 \
--data-parallel-size 4 \
--data-parallel-size-local 1 \
--data-parallel-address $local_ip \
--data-parallel-rpc-port 18839 \
--tensor-parallel-size 4 \
--enable-expert-parallel \
--seed 1024 \
--served-model-name deepseek_v3.2 \
--max-num-seqs 2 \
--max-model-len 40000 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--quantization ascend \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--compilation-config '{"cudagraph_capture_sizes":[1,2,4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}' \
--speculative-config '{"num_speculative_tokens": 2, "method":"deepseek_mtp"}' \
--tokenizer-mode deepseek_v32 \
--reasoning-parser deepseek_v3


node1配置：
#!/bin/sh
nic_name="enp61s0f0"
local_ip="x.x.x.5"
node0_ip="x.x.x.2"
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=200
export HCCL_OP_EXPANSION_MODE="AIV"
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=0
export HCCL_CONNECT_TIMEOUT=120
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTTRA_ROCE_ENABLE=0
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/lib64:$LD_LIBRARY_PATH
export VLLM_NIXL_ABORT_REQUEST_TIMEOUT=300000
export ASCEND_AGGREGATE_ENABLE=1
export ASCEND_TRANSPORT_PRINT=1
vllm serve /home/openlab/deepseek/DeepSeek-V3.2-w8a8-vllm-ascend/ \
--host x.x.x.5 \
--port 8000 \
--headless \
--data-parallel-size 4 \
--data-parallel-size-local 1 \
--data-parallel-start-rank 1 \
--data-parallel-address $node0_ip \
--data-parallel-rpc-port 18839 \
--tensor-parallel-size 4 \
--enable-expert-parallel \
--seed 1024 \
--served-model-name deepseek_v3.2 \
--max-num-seqs 2 \
--max-model-len 40000 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--quantization ascend \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--compilation-config '{"cudagraph_capture_sizes":[1,2,4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}' \
--speculative-config '{"num_speculative_tokens": 2, "method":"deepseek_mtp"}' \
--tokenizer-mode deepseek_v32 \
--reasoning-parser deepseek_v3

4、启动后一直卡住，日志如下
INFO 01-16 11:00:42 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-16 11:00:42 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-16 11:00:42 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-16 11:00:42 [__init__.py:217] Platform plugin ascend is activated
INFO 01-16 11:00:49 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
(APIServer pid=31411) INFO 01-16 11:00:49 [api_server.py:1351] vLLM API server version 0.13.0
(APIServer pid=31411) INFO 01-16 11:00:49 [utils.py:253] non-default args: {'model_tag': '/home/openlab/deepseek/DeepSeek-V3.2-w8a8-vllm-ascend/', 'host': 'x.x.x.2', 'model': '/home/openlab/deepseek/DeepSeek-V3.2-w8a8-vllm-ascend/', 'tokenizer_mode': 'deepseek_v32', 'trust_remote_code': True, 'seed': 1024, 'max_model_len': 40000, 'quantization': 'ascend', 'served_model_name': ['deepseek_v3.2'], 'reasoning_parser': 'deepseek_v3', 'tensor_parallel_size': 4, 'data_parallel_size': 4, 'data_parallel_size_local': 1, 'data_parallel_address': '194.0.65.2', 'data_parallel_rpc_port': 18839, 'enable_expert_parallel': True, 'gpu_memory_utilization': 0.92, 'enable_prefix_caching': False, 'max_num_batched_tokens': 4096, 'max_num_seqs': 2, 'speculative_config': {'num_speculative_tokens': 2, 'method': 'deepseek_mtp'}, 'compilation_config': {'level': None, 'mode': None, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'vllm_ascend.compilation.compiler_interface.AscendCompiler', 'custom_ops': [], 'splitting_ops': None, 'compile_mm_encoder': False, 'compile_sizes': None, 'compile_ranges_split_points': None, 'inductor_compile_config': {'enable_auto_functionalized_v2': False}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL_DECODE_ONLY: (2, 0)>, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': [1, 2, 4, 16, 32, 48, 64], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': None, 'pass_config': {}, 'max_cudagraph_capture_size': None, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False}, 'local_cache_dir': None}}
(APIServer pid=31411) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=31411) You are using a model of type deepseek_v32 to instantiate a model of type deepseek_v3. This is not supported for all configurations of models and can yield errors.
(APIServer pid=31411) INFO 01-16 11:00:49 [model.py:514] Resolved architecture: DeepseekV32ForCausalLM
(APIServer pid=31411) INFO 01-16 11:00:49 [model.py:1661] Using max model len 40000
(APIServer pid=31411) WARNING 01-16 11:00:50 [speculative.py:245] method `deepseek_mtp` is deprecated and replaced with mtp.
(APIServer pid=31411) You are using a model of type deepseek_v32 to instantiate a model of type deepseek_v3. This is not supported for all configurations of models and can yield errors.
(APIServer pid=31411) INFO 01-16 11:00:50 [model.py:514] Resolved architecture: DeepSeekMTPModel
(APIServer pid=31411) INFO 01-16 11:00:50 [model.py:1661] Using max model len 163840
(APIServer pid=31411) WARNING 01-16 11:00:50 [speculative.py:363] Enabling num_speculative_tokens > 1 will runmultiple times of forward on same MTP layer,which may result in lower acceptance rate
(APIServer pid=31411) INFO 01-16 11:00:50 [scheduler.py:230] Chunked prefill is enabled with max_num_batched_tokens=4096.
(APIServer pid=31411) INFO 01-16 11:00:50 [platform.py:252] FULL_DECODE_ONLY compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             **********************************************************************************
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * WARNING: You have enabled the *full graph* feature.
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * This is an early experimental stage and may involve various unknown issues.
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * A known problem is that capturing too many batch sizes can lead to OOM
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * (Out of Memory) errors or inference hangs. If you encounter such issues,
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * consider reducing `gpu_memory_utilization` or manually specifying a smaller
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * batch size for graph capture.
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * For more details, please refer to:
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             * https://docs.vllm.ai/en/stable/configuration/conserving_memory.html#reduce-cuda-graphs
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]             **********************************************************************************
(APIServer pid=31411) WARNING 01-16 11:00:50 [platform.py:269]
(APIServer pid=31411) INFO 01-16 11:00:50 [utils.py:821] Started DP Coordinator process (PID: 31552)
INFO 01-16 11:00:57 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-16 11:00:57 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-16 11:00:57 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-16 11:00:57 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-16 11:00:57 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-16 11:00:57 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-16 11:00:57 [__init__.py:217] Platform plugin ascend is activated
INFO 01-16 11:00:57 [__init__.py:217] Platform plugin ascend is activated

</details>

