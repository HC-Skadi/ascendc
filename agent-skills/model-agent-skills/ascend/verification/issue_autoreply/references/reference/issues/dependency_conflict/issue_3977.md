# Issue #3977: [Bug]:

## 基本信息

- **编号**: #3977
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3977
- **创建时间**: 2025-11-04T11:29:21Z
- **关闭时间**: 2025-11-04T11:31:39Z
- **更新时间**: 2025-11-04T11:31:39Z
- **提交者**: @HemiFate
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

驱动：npu-smi 25.2.1 
cann：8.2.RC1
python：Python 3.10.19
ray： 2.47.1
vllm：0.11.0
vllm-ascend：0.11.0rc0

### 🐛 Describe the bug

DP启动脚本：
node0:
#!/bin/sh
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="eth0"
local_ip="172.27.255.238"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
unset VLLM_USE_V1
export HCCL_BUFFSIZE=1024

nohup vllm serve /model/Qwen3-235B-A22B-Instruct-2507/ \
    --host 0.0.0.0 \
    --port 8000 \
    --data-parallel-size 2 \
    --api-server-count 2 \
    --data-parallel-size-local 1 \
    --data-parallel-address $local_ip \
    --data-parallel-rpc-port 13309 \
    --seed 1024 \
    --served-model-name qwen3 \
    --tensor-parallel-size 8 \
    --enable-expert-parallel \
    --max-num-seqs 8 \
    --max-model-len 32768 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.9 \
    >/model/logs/vllm_node0.log 2>&1 &

node1:
#!/bin/sh

# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="eth0"
local_ip="172.26.142.18"

# The value of node0_ip must be consistent with the value of local_ip set in node0 (master node)
node0_ip="172.27.255.238"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
unset VLLM_USE_V1
export HCCL_BUFFSIZE=1024

nohup vllm serve /model/Qwen3-235B-A22B-Instruct-2507/ \
    --host 0.0.0.0 \
    --port 8000 \
    --headless \
    --data-parallel-size 2 \
    --data-parallel-size-local 1 \
    --data-parallel-start-rank 1 \
    --data-parallel-address $node0_ip \
    --data-parallel-rpc-port 13309 \
    --seed 1024 \
    --tensor-parallel-size 8 \
    --served-model-name qwen3 \
    --max-num-seqs 8 \
    --max-model-len 32768 \
    --enable-expert-parallel \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.9 \
    >/model/logs/vllm_node1.log 2>&1 &


加载报错：

[1;36m(EngineCore_DP0 pid=25527)[0;0m INFO 11-04 18:54:33 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
[1;36m(EngineCore_DP0 pid=25527)[0;0m INFO 11-04 18:55:33 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
[1;36m(EngineCore_DP0 pid=25527)[0;0m INFO 11-04 18:56:33 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
[1;36m(EngineCore_DP0 pid=25527)[0;0m INFO 11-04 18:57:33 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
[1;36m(EngineCore_DP0 pid=25527)[0;0m INFO 11-04 18:58:33 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
[1;36m(EngineCore_DP0 pid=25527)[0;0m INFO 11-04 18:59:33 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
[1;36m(EngineCore_DP0 pid=25527)[0;0m INFO 11-04 19:00:33 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
[1;36m(ApiServer_0 pid=25528)[0;0m Process ApiServer_0:
[1;36m(ApiServer_0 pid=25528)[0;0m Traceback (most recent call last):
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
[1;36m(ApiServer_0 pid=25528)[0;0m     self.run()
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/multiprocessing/process.py", line 108, in run
[1;36m(ApiServer_0 pid=25528)[0;0m     self._target(*self._args, **self._kwargs)
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 230, in run_api_server_worker_proc
[1;36m(ApiServer_0 pid=25528)[0;0m     uvloop.run(
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/uvloop/__init__.py", line 69, in run
[1;36m(ApiServer_0 pid=25528)[0;0m     return loop.run_until_complete(wrapper())
[1;36m(ApiServer_0 pid=25528)[0;0m   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/uvloop/__init__.py", line 48, in wrapper
[1;36m(ApiServer_0 pid=25528)[0;0m     return await main
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
[1;36m(ApiServer_0 pid=25528)[0;0m     async with build_async_engine_client(
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/contextlib.py", line 199, in __aenter__
[1;36m(ApiServer_0 pid=25528)[0;0m     return await anext(self.gen)
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
[1;36m(ApiServer_0 pid=25528)[0;0m     async with build_async_engine_client_from_engine_args(
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/contextlib.py", line 199, in __aenter__
[1;36m(ApiServer_0 pid=25528)[0;0m     return await anext(self.gen)
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
[1;36m(ApiServer_0 pid=25528)[0;0m     async_llm = AsyncLLM.from_vllm_config(
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/utils/__init__.py", line 1572, in inner
[1;36m(ApiServer_0 pid=25528)[0;0m     return fn(*args, **kwargs)
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
[1;36m(ApiServer_0 pid=25528)[0;0m     return cls(
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/v1/engine/async_llm.py", line 134, in __init__
[1;36m(ApiServer_0 pid=25528)[0;0m     self.engine_core = EngineCoreClient.make_async_mp_client(
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 101, in make_async_mp_client
[1;36m(ApiServer_0 pid=25528)[0;0m     return DPLBAsyncMPClient(*client_args)
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 1125, in __init__
[1;36m(ApiServer_0 pid=25528)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 975, in __init__
[1;36m(ApiServer_0 pid=25528)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 769, in __init__
[1;36m(ApiServer_0 pid=25528)[0;0m     super().__init__(
[1;36m(ApiServer_0 pid=25528)[0;0m   File "/root/.local/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 496, in __init__
[1;36m(ApiServer_0 pid=25528)[0;0m     raise TimeoutError("Timed out waiting for engines to send"
[1;36m(ApiServer_0 pid=25528)[0;0m TimeoutError: Timed out waiting for engines to sendinitial message on input socket.

ray 启动脚本：
export HCCL_IF_IP=172.25.173.239
export GLOO_SOCKET_IFNAME=eth0
export TP_SOCKET_IFNAME=eth0
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ray start --head

export HCCL_IF_IP=172.25.230.54
export GLOO_SOCKET_IFNAME=eth0
export TP_SOCKET_IFNAME=eth0
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ray start --address='172.25.173.239:6379' --node-ip-address=172.25.230.54


nohup vllm serve /model/Qwen3-235B-A22B-Instruct-2507/ \
  --distributed-executor-backend ray \
  --tensor-parallel-size 2 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --no-enable-prefix-caching \
  --seed 1024 \
  --max-num-seqs 4 \
  --enforce-eager \
  --served-model-name qwen \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  > /model/logs/vllm_tp2_ep8.log 2>&1 &

加载报错：
[1;36m(EngineCore_DP0 pid=846)[0;0m INFO 11-04 18:50:23 [ray_env.py:63] RAY_NON_CARRY_OVER_ENV_VARS from config: set()
[1;36m(EngineCore_DP0 pid=846)[0;0m INFO 11-04 18:50:23 [ray_env.py:65] Copying the following environment variables to workers: ['VLLM_USE_RAY_COMPILED_DAG', 'VLLM_WORKER_MULTIPROC_METHOD', 'VLLM_USE_RAY_SPMD_WORKER', 'LD_LIBRARY_PATH', 'VLLM_USE_V1', 'VLLM_ALL2ALL_BACKEND']
[1;36m(EngineCore_DP0 pid=846)[0;0m INFO 11-04 18:50:23 [ray_env.py:68] If certain env vars should NOT be copied, add them to /root/.config/vllm/ray_non_carry_over_env_vars.json file
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1021)[0m Exception in thread Thread-1:
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1021)[0m Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1021)[0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(pid=1020)[0m /root/.local/lib/python3.10/site-packages/torch_npu/dynamo/torchair/__init__.py:8: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.[32m [repeated 7x across cluster][0m
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(pid=1020)[0m   import pkg_resources[32m [repeated 7x across cluster][0m
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m     self.run()
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/utils/multiprocess_util.py", line 91, in run
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m     key, func, args, kwargs = self.task_q.get(timeout=TIMEOUT)
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m   File "<string>", line 2, in get
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m     kind, result = conn.recv()
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/multiprocessing/connection.py", line 250, in recv
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m     buf = self._recv_bytes()
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m     buf = self._recv(4)
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m   File "/root/.local/conda/envs/vllm_0.11.0/lib/python3.10/multiprocessing/connection.py", line 379, in _recv
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m     chunk = read(handle, remaining)
[1;36m(EngineCore_DP0 pid=846)[0;0m [36m(RayWorkerWrapper pid=1027)[0m ConnectionResetError: [Errno 104] Connection reset by peer
