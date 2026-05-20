# Issue #3389: [Bug]: qwen3 vl acl graph compiled failed

## 基本信息

- **编号**: #3389
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3389
- **创建时间**: 2025-10-11T11:42:52Z
- **关闭时间**: 2025-10-13T12:01:09Z
- **更新时间**: 2025-11-14T03:54:51Z
- **提交者**: @JasonHe-WQ
- **评论数**: 5

## 标签

bug; module:multimodal

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

using image `vllm-ascend:v0.11.0rc0`


```text
root@qwen3-vl-ascend-695866b8f5-69bqs:/vllm-workspace/vllm-ascend# python ./collect_env.py 
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35



Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1+cpu
[pip3] transformers==4.57.0.dev0
[conda] Could not collect
vLLM Version: 0.11.0rc3
vLLM Ascend Version: 0.11.0rc0

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=10,7,6,14,4,9,1,2,13,12,0,3,15,5,11,8
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug

command
```shell
vllm serve /mnt/hw910test-jfs/models/qwen/Qwen3-VL-235B-A22B-Instruct --served-model-name qwen3vl --port 8080 --max-model-len 40960 --max-num-seqs 256 --tensor-parallel-size 16 --gpu-memory-utilization 0.85 --reasoning-parser qwen3 
```

log


```plaintext
(EngineCore_DP0 pid=15471) INFO 10-11 11:30:28 [kv_cache_utils.py:1091] Maximum concurrency for 40,960 tokens per request: 11.90x
(Worker_TP0 pid=15607) INFO 10-11 11:30:28 [model_runner_v1.py:3502] Starting to capture ACL graphs for cases: [512, 408, 304, 192, 88, 1], mode: PIECEWISE, uniform_decode: False
Capturing ACL graphs (mixed prefill-decode, PIECEWISE):   0%|                                                                                                                                              | 0/6 [00:00<?, ?it/s][rank2]:[W1011 11:30:29.389598994 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank14]:[W1011 11:30:29.395223968 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank1]:[W1011 11:30:29.400332646 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank3]:[W1011 11:30:29.407211469 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank5]:[W1011 11:30:29.411050034 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank6]:[W1011 11:30:29.419998949 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank9]:[W1011 11:30:29.422638646 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank7]:[W1011 11:30:29.427645310 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank0]:[W1011 11:30:29.429008297 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank10]:[W1011 11:30:29.429076058 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank4]:[W1011 11:30:29.458632989 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank8]:[W1011 11:30:29.469684689 NPUGraph.cpp:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
(EngineCore_DP0 pid=15471) INFO 10-11 11:31:28 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP0 pid=15471) INFO 10-11 11:32:28 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] ACLgraph sizes capture fail: RuntimeError:
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] ACLgraph has insufficient available streams to capture the configured number of sizes. Please verify both the availability of adequate streams and the appropriateness of the configured size count.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Recommended solutions:
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 1. Manually configure the compilation_config parameter with a reduced set of sizes: '{"cudagraph_capture_sizes":[size1, size2, size3, ...]}'.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 2. Utilize ACLgraph's full graph mode as an alternative to the piece-wise approach.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] [ERROR] 2025-10-11-11:32:59 (PID:15618, Device:11, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] EI0006: [PID: 15618] 2025-10-11-11:32:29.335.888 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         TraceBack (most recent call last):
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[14]-remoteUserrank[14]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[8]-remoteUserrank[8]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[10]-remoteUserrank[10]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[9]-remoteUserrank[9]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] ACLgraph sizes capture fail: RuntimeError:
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] ACLgraph has insufficient available streams to capture the configured number of sizes. Please verify both the availability of adequate streams and the appropriateness of the configured size count.
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Recommended solutions:
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 1. Manually configure the compilation_config parameter with a reduced set of sizes: '{"cudagraph_capture_sizes":[size1, size2, size3, ...]}'.
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 2. Utilize ACLgraph's full graph mode as an alternative to the piece-wise approach.
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] [ERROR] 2025-10-11-11:32:59 (PID:15619, Device:12, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] EI0006: [PID: 15619] 2025-10-11-11:32:29.342.650 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         TraceBack (most recent call last):
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[12]-localUserrank[12]-localIpAddr[100.100.164.12], dst_rank[8]-remoteUserrank[8]-remote_ip_addr[100.100.164.12]
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[12]-localUserrank[12]-localIpAddr[100.100.164.12], dst_rank[10]-remoteUserrank[10]-remote_ip_addr[100.100.164.12]
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[12]-localUserrank[12]-localIpAddr[100.100.164.12], dst_rank[14]-remoteUserrank[14]-remote_ip_addr[100.100.164.12]
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[12]-localUserrank[12]-localIpAddr[100.100.164.12], dst_rank[9]-remoteUserrank[9]-remote_ip_addr[100.100.164.12]
(Worker_TP12 pid=15619) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] ACLgraph sizes capture fail: RuntimeError:
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] ACLgraph has insufficient available streams to capture the configured number of sizes. Please verify both the availability of adequate streams and the appropriateness of the configured size count.
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Recommended solutions:
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 1. Manually configure the compilation_config parameter with a reduced set of sizes: '{"cudagraph_capture_sizes":[size1, size2, size3, ...]}'.
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 2. Utilize ACLgraph's full graph mode as an alternative to the piece-wise approach.
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] [ERROR] 2025-10-11-11:32:59 (PID:15622, Device:15, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] EI0006: [PID: 15622] 2025-10-11-11:32:29.347.816 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         TraceBack (most recent call last):
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[15]-localUserrank[15]-localIpAddr[100.100.164.12], dst_rank[9]-remoteUserrank[9]-remote_ip_addr[100.100.164.12]
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[15]-localUserrank[15]-localIpAddr[100.100.164.12], dst_rank[10]-remoteUserrank[10]-remote_ip_addr[100.100.164.12]
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[15]-localUserrank[15]-localIpAddr[100.100.164.12], dst_rank[8]-remoteUserrank[8]-remote_ip_addr[100.100.164.12]
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[15]-localUserrank[15]-localIpAddr[100.100.164.12], dst_rank[14]-remoteUserrank[14]-remote_ip_addr[100.100.164.12]
(Worker_TP15 pid=15622) ERROR 10-11 11:32:59 [model_runner_v1.py:3556] 
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] WorkerProc hit an exception.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] Traceback (most recent call last):
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     output = func(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 307, in compile_or_warm_up_model
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self.model_runner.capture_model()
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3596, in capture_model
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self._capture_model()
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3551, in _capture_model
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self._capture_aclgraphs(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3525, in _capture_aclgraphs
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self._dummy_run(num_tokens,
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return func(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2475, in _dummy_run
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2320, in _generate_dummy_run_hidden_states
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 1577, in forward
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     hidden_states = self.language_model.model(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 317, in __call__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     model_output = self.forward(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl_moe.py", line 82, in forward
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     def forward(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return fn(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     raise e
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "<eval_with_key>.190", line 676, in forward
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     submod_2 = self.submod_2(getitem_3, s0, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_, l_inputs_embeds_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s2);  getitem_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_ = l_inputs_embeds_ = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_ = l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_ = None
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 153, in __call__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     with torch.npu.graph(aclgraph, pool=self.graph_pool):
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/graphs.py", line 315, in __exit__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self.npu_graph.capture_end()
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/graphs.py", line 221, in capture_end
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     super().capture_end()
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] [ERROR] 2025-10-11-11:32:59 (PID:15618, Device:11, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] EI0006: [PID: 15618] 2025-10-11-11:32:29.335.888 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]         Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]         TraceBack (most recent call last):
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[14]-remoteUserrank[14]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[8]-remoteUserrank[8]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[10]-remoteUserrank[10]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[11]-localUserrank[11]-localIpAddr[100.100.164.12], dst_rank[9]-remoteUserrank[9]-remote_ip_addr[100.100.164.12]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] 
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671] Traceback (most recent call last):
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     output = func(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 307, in compile_or_warm_up_model
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self.model_runner.capture_model()
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3596, in capture_model
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self._capture_model()
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3551, in _capture_model
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self._capture_aclgraphs(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3525, in _capture_aclgraphs
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     self._dummy_run(num_tokens,
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return func(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2475, in _dummy_run
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2320, in _generate_dummy_run_hidden_states
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 1577, in forward
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     hidden_states = self.language_model.model(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 317, in __call__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     model_output = self.forward(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl_moe.py", line 82, in forward
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     def forward(
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return fn(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     raise e
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]   File "<eval_with_key>.190", line 676, in forward
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]     submod_2 = self.submod_2(getitem_3, s0, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_, l_inputs_embeds_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s2);  getitem_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_ = l_inputs_embeds_ = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_ = l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_ = None
(Worker_TP11 pid=15618) ERROR 10-11 11:32:59 [multiproc_executor.py:671]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
