# Issue #3378: [Bug]: use v0.11.0rc0 start Qwen3-VL-235B-A22B-Instruct failed according to the official documentation

## 基本信息

- **编号**: #3378
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3378
- **创建时间**: 2025-10-11T03:46:51Z
- **关闭时间**: 2025-10-14T08:04:10Z
- **更新时间**: 2026-02-17T15:10:48Z
- **提交者**: @nuclearwu
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

command:

node0:
```
#!/bin/sh
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip
MODEL_NAME_OR_PATH=/workspace/cache/grtest-zz/johnjan/modelscope/models/Qwen/Qwen3-VL-235B-A22B-Instruct/
nic_name=""
local_ip=""

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1024

vllm serve $MODEL_NAME_OR_PATH \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 2 \
--api-server-count 2 \
--data-parallel-size-local 1 \
--data-parallel-address $local_ip \
--data-parallel-rpc-port 13389 \
--seed 1024 \
--served-model-name qwen3vl \
--tensor-parallel-size 8 \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 32768 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.8 \
```
node1:
```
#!/bin/sh
MODEL_NAME_OR_PATH=/workspace/cache/grtest-zz/johnjan/modelscope/models/Qwen/Qwen3-VL-235B-A22B-Instruct/
nic_name="eth0"
local_ip=""
node0_ip=""

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1024

vllm serve $MODEL_NAME_OR_PATH \
--host 0.0.0.0 \
--port 8000 \
--headless \
--data-parallel-size 2 \
--data-parallel-size-local 1 \
--data-parallel-start-rank 1 \
--data-parallel-address $node0_ip \
--data-parallel-rpc-port 13389 \
--seed 1024 \
--tensor-parallel-size 8 \
--served-model-name qwen3vl \
--max-num-seqs 16 \
--max-model-len 32768 \
--max-num-batched-tokens 4096 \
--enable-expert-parallel \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.8 \
```


```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

The error message is as follows:
```
(Worker_DP0_TP0_EP0 pid=33724) ERROR 10-11 11:37:35 [multiproc_executor.py:671] RuntimeError: Format of weight in npu_grouped_matmul is FRACTAL_NZ, current CANN version do not support with this format. Please try to update the version of CANN.
(Worker_DP0_TP0_EP0 pid=33724) ERROR 10-11 11:37:35 [multiproc_executor.py:671] [ERROR] 2025-10-11-11:37:35 (PID:33724, Device:0, RankID:-1) ERR01001 OPS invalid parameter
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 695, in run_engine_core
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 965, in __init__
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     super().__init__(vllm_config, local_client, handshake_address,
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     self.model_executor.determine_available_memory())
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 85, in determine_available_memory
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708]     raise RuntimeError(
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708] RuntimeError: Worker failed with error 'Format of weight in npu_grouped_matmul is FRACTAL_NZ, current CANN version do not support with this format. Please try to update the version of CANN.
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:35 [core.py:708] [ERROR] 2025-10-11-11:37:35 (PID:33724, Device:0, RankID:-1) ERR01001 OPS invalid parameter', please check the stack trace above for the root cause
(EngineCore_DP0 pid=32647) ERROR 10-11 11:37:50 [multiproc_executor.py:154] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
(EngineCore_DP0 pid=32647) Process EngineCore_DP0:
(EngineCore_DP0 pid=32647) Traceback (most recent call last):
(EngineCore_DP0 pid=32647)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=32647)     self.run()
(EngineCore_DP0 pid=32647)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=32647)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=32647)     raise e
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 695, in run_engine_core
(EngineCore_DP0 pid=32647)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 965, in __init__
(EngineCore_DP0 pid=32647)     super().__init__(vllm_config, local_client, handshake_address,
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=32647)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=32647)     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
(EngineCore_DP0 pid=32647)     self.model_executor.determine_available_memory())
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 85, in determine_available_memory
(EngineCore_DP0 pid=32647)     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=32647)     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=32647)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=32647)     raise RuntimeError(
(EngineCore_DP0 pid=32647) RuntimeError: Worker failed with error 'Format of weight in npu_grouped_matmul is FRACTAL_NZ, current CANN version do not support with this format. Please try to update the version of CANN.
(EngineCore_DP0 pid=32647) [ERROR] 2025-10-11-11:37:35 (PID:33724, Device:0, RankID:-1) ERR01001 OPS invalid parameter', please check the stack trace above for the root cause
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 54, in cmd
    run_multi_api_server(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 178, in run_multi_api_server
    with launch_core_engines(vllm_config, executor_class, log_stats,
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
    wait_for_engine_startup(
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-10-11-11:37:54 (PID:32188, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
