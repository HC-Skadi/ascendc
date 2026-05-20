# Issue #5748: [Bug]: qwen3 coder  failed to start and get HCCL function error

## 基本信息

- **编号**: #5748
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5748
- **创建时间**: 2026-01-09T02:27:11Z
- **关闭时间**: 2026-01-23T03:12:46Z
- **更新时间**: 2026-01-28T02:13:41Z
- **提交者**: @gao12312
- **评论数**: 9

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

A2+VLLM 0.13.0rc1

NODE0:
```python  
nic_name="eth0"
local_ip="XXXX"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
#export HCCL_CONNECT_TIMEOUT=360
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1024
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1
# export CPU_AFFINITY_CONF=2
# export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
# export VLLM_ASCEND_ENABLE_FUSED_MC2=1  
# export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
# export HCCL_INTRA_PCIE_ENABLE=1
# export HCCL_INTRA_ROCE_ENABLE=0

vllm serve /models/Qwen3-Coder-480B-A35B-Instruct-w8a8 \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 2 \
--data-parallel-size-local 1 \
--data-parallel-address $local_ip \
--data-parallel-rpc-port 13389 \
--seed 1024 \
--served-model-name qwen3_coder \
--enable-expert-parallel  \
--tensor-parallel-size 8 \
--max-num-seqs 16 \
--max-model-len 32768 \
--max-num-batched-tokens 8192 \
--trust-remote-code \
--gpu-memory-utilization 0.9 \
--async-scheduling \
```


NODE1:
```python  
#!/bin/sh

# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip

nic_name="eth0"
local_ip="XXX"
node0_ip="XXX"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name

export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1024
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1

vllm serve /workspace/cache/aiops-sh2/models/Qwen3-Coder-480B-A35B-Instruct-w8a8 \
--host 0.0.0.0 \
--port 8000 \
--headless \
--data-parallel-size 2 \
--data-parallel-size-local 1 \
--data-parallel-start-rank 1 \
--data-parallel-address  $node0_ip \
--data-parallel-rpc-port 13389 \
--seed 1024 \
--tensor-parallel-size 8 \
--served-model-name qwen3-coder \
--quantization ascend  \
--enable-expert-parallel  \
--max-num-seqs 16 \
--max-model-len 32768 \
--max-num-batched-tokens 8192 \
--tool-call-parser qwen3_coder \
--gpu-memory-utilization 0.9 \
```

failed logs:
```python 
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751] WorkerProc failed to start.
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751] Traceback (most recent call last):
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 722, in worker_main
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     worker = WorkerProc(*args, **kwargs)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 562, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.worker.load_model()
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 355, in load_model
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.model_runner.load_model()
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2230, in load_model
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.model = get_model(vllm_config=self.vllm_config)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 132, in get_model
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     return loader.load_model(vllm_config=vllm_config, model_config=model_config)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 49, in load_model
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     model = initialize_model(
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]             ^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 48, in initialize_model
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     return model_class(vllm_config=vllm_config, prefix=prefix)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 658, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.model = Qwen3MoeModel(
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                  ^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 291, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     old_init(self, **kwargs)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 412, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.start_layer, self.end_layer, self.layers = make_layers(
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                                                     ^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 605, in make_layers
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     + [
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]       ^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 606, in <listcomp>
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 414, in <lambda>
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     lambda prefix: Qwen3MoeDecoderLayer(vllm_config=vllm_config, prefix=prefix),
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 352, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.mlp = Qwen3MoeSparseMoeBlock(
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 163, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.experts = FusedMoE(
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                    ^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 255, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     setup_moe_comm_method(self.moe_config)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 44, in setup_moe_comm_method
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     _MoECommMethods[MoECommType.ALLTOALL] = AlltoAllCommImpl(moe_config)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 56, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.token_dispatcher = self._get_token_dispatcher()
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 235, in _get_token_dispatcher
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     return TokenDispatcherWithAll2AllV(
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 465, in __init__
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]     self.moe_all_to_all_group_name = backend.get_hccl_comm_name(local_rank)
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751]                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751] RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:148 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 1
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751] [ERROR] 2026-01-09-10:21:58 (PID:8457, Device:0, RankID:-1) ERR02200 DIST call hccl api failed.
(Worker_DP0_TP0_EP0 pid=8457) ERROR 01-09 10:21:59 [multiproc_executor.py:751] 
(Worker_DP0_TP0_EP0 pid=8457) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_DP0_TP4_EP4 pid=8461) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_DP0_TP1_EP1 pid=8458) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_DP0_TP2_EP2 pid=8459) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_DP0_TP7_EP7 pid=8464) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_DP0_TP6_EP6 pid=8463) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_DP0_TP3_EP3 pid=8460) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_DP0_TP5_EP5 pid=8462) INFO 01-09 10:21:59 [multiproc_executor.py:709] Parent process exited, terminating worker
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866] EngineCore failed to start.
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866] Traceback (most recent call last):
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 853, in run_engine_core
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     super().__init__(
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     super().__init__(
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 102, in __init__
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 97, in __init__
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     super().__init__(vllm_config)
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 101, in __init__
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     self._init_executor()
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 172, in _init_executor
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 660, in wait_for_ready
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866]     raise e from None
(EngineCore_DP0 pid=8041) ERROR 01-09 10:22:03 [core.py:866] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP0 pid=8041) Process EngineCore_DP0:
(EngineCore_DP0 pid=8041) Traceback (most recent call last):
(EngineCore_DP0 pid=8041)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=8041)     self.run()
(EngineCore_DP0 pid=8041)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=8041)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 870, in run_engine_core
(EngineCore_DP0 pid=8041)     raise e
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 853, in run_engine_core
(EngineCore_DP0 pid=8041)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=8041)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
(EngineCore_DP0 pid=8041)     super().__init__(
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP0 pid=8041)     super().__init__(
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 102, in __init__
(EngineCore_DP0 pid=8041)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=8041)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 97, in __init__
(EngineCore_DP0 pid=8041)     super().__init__(vllm_config)
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 101, in __init__
(EngineCore_DP0 pid=8041)     self._init_executor()
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 172, in _init_executor
(EngineCore_DP0 pid=8041)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=8041)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=8041)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 660, in wait_for_ready
(EngineCore_DP0 pid=8041)     raise e from None
(EngineCore_DP0 pid=8041) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(APIServer pid=7658) Traceback (most recent call last):
(APIServer pid=7658)   File "/usr/local/python3.11.13/bin/vllm", line 7, in <module>
(APIServer pid=7658)     sys.exit(main())
(APIServer pid=7658)              ^^^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main
(APIServer pid=7658)     args.dispatch_function(args)
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 60, in cmd
(APIServer pid=7658)     uvloop.run(run_server(args))
(APIServer pid=7658)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
(APIServer pid=7658)     return runner.run(wrapper())
(APIServer pid=7658)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7658)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=7658)     return self._loop.run_until_complete(task)
(APIServer pid=7658)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7658)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=7658)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=7658)     return await main
(APIServer pid=7658)            ^^^^^^^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1398, in run_server
(APIServer pid=7658)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1417, in run_server_worker
(APIServer pid=7658)     async with build_async_engine_client(
(APIServer pid=7658)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=7658)     return await anext(self.gen)
(APIServer pid=7658)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 172, in build_async_engine_client
(APIServer pid=7658)     async with build_async_engine_client_from_engine_args(
(APIServer pid=7658)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=7658)     return await anext(self.gen)
(APIServer pid=7658)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 213, in build_async_engine_client_from_engine_args
(APIServer pid=7658)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=7658)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 215, in from_vllm_config
(APIServer pid=7658)     return cls(
(APIServer pid=7658)            ^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=7658)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=7658)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 120, in make_async_mp_client
(APIServer pid=7658)     return DPLBAsyncMPClient(*client_args)
(APIServer pid=7658)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1192, in __init__
(APIServer pid=7658)     super().__init__(
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1033, in __init__
(APIServer pid=7658)     super().__init__(
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 820, in __init__
(APIServer pid=7658)     super().__init__(
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 477, in __init__
(APIServer pid=7658)     with launch_core_engines(vllm_config, executor_class, log_stats) as (
(APIServer pid=7658)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=7658)     next(self.gen)
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 903, in launch_core_engines
(APIServer pid=7658)     wait_for_engine_startup(
(APIServer pid=7658)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 960, in wait_for_engine_startup
(APIServer pid=7658)     raise RuntimeError(
(APIServer pid=7658) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=7658) [ERROR] 2026-01-09-10:22:06 (PID:7658, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 9 leaked shared_memory objects to clean up at shutdown
```



