# Issue #1680: [Bug]: 0.9.1-dev，关闭 enforce-eager（开启aclgrach）报 llm_datadist 的 link 错误

## 基本信息

- **编号**: #1680
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1680
- **创建时间**: 2025-07-09T01:54:04Z
- **关闭时间**: 2025-10-15T03:43:08Z
- **更新时间**: 2025-10-15T03:43:08Z
- **提交者**: @FieeFlip
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
d1节点：

```text
INFO 07-09 09:47:05 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-09 09:47:05 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-09 09:47:06 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-09 09:47:06 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-09 09:47:06 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-09 09:47:06 [__init__.py:235] Platform plugin ascend is activated
/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/dynamo/torchair/__init__.py:8: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
WARNING 07-09 09:47:10 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.17 (main, Apr 30 2025, 16:00:31) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-2107.6.0.0192.8.oe1.bclinux.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.9.0.1
vLLM Ascend Version: 0.9.0rc2.dev27+gce4bdab.d20250625 (git sha: ce4bdab, date: 20250625)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=5,6
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 93.2        41                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 97.1        42                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```

d2节点：
```text
INFO 07-09 09:51:00 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-09 09:51:00 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-09 09:51:02 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-09 09:51:02 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-09 09:51:02 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-09 09:51:02 [__init__.py:235] Platform plugin ascend is activated
/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/dynamo/torchair/__init__.py:8: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
WARNING 07-09 09:51:06 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.17 (main, Apr 30 2025, 16:00:31) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-2107.6.0.0192.8.oe1.bclinux.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.9.0.1
vLLM Ascend Version: 0.9.0rc2.dev27+gce4bdab.d20250625 (git sha: ce4bdab, date: 20250625)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=6,1
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 102.3       41                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 101.3       43                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```
</details>


### 🐛 Describe the bug

不知为何开启了 acl graph 报错（关闭了enforce-eager），开启 enforce-eager 是正常运行的。
开启了 acl graph 能正常拉起，但是不能推理，报错如下：
2p2d：

p2:
```bash
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:352] LLMDataDistCMgrConnectorWorker: Receive message from cluster 5
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:352] LLMDataDistCMgrConnectorWorker: Receive message from cluster 6
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:630] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.168.58.66_192.168.58.206
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] rank table 
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '1', 'device_ip': '192.168.58.66', 'rank_id': '0'}], 'server_id': '10.222.49.196'}, {'device': [{'device_id': '5', 'device_ip': '192.168.58.206', 'rank_id': '1'}], 'server_id': '10.222.59.36'}]}
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:634] comm name: pd_comm_192.168.58.66_192.168.58.206
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:635] cluster rank info: {3: 0, 5: 1}
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:630] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.168.58.71_192.168.58.207
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] rank table 
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '6', 'device_ip': '192.168.58.71', 'rank_id': '0'}], 'server_id': '10.222.49.196'}, {'device': [{'device_id': '6', 'device_ip': '192.168.58.207', 'rank_id': '1'}], 'server_id': '10.222.59.36'}]}
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:634] comm name: pd_comm_192.168.58.71_192.168.58.207
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:635] cluster rank info: {4: 0, 6: 1}
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:39 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:39 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:40 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:40 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:41 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:41 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:42 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:42 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:43 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=90674) INFO 07-08 18:17:43 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=90674) Exception in thread metadata_agent_listener:
(VllmWorker rank=0 pid=90674) Traceback (most recent call last):
(VllmWorker rank=0 pid=90674)   File "/usr/local/python3.10.17/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
(VllmWorker rank=0 pid=90674)     self.run()
(VllmWorker rank=0 pid=90674)   File "/usr/local/python3.10.17/lib/python3.10/threading.py", line 953, in run
(VllmWorker rank=0 pid=90674)     self._target(*self._args, **self._kwargs)
(VllmWorker rank=0 pid=90674)   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 356, in listen_for_agent_metadata_req
(VllmWorker rank=0 pid=90674)     self.add_remote_agent(decode_msg)
(VllmWorker rank=0 pid=90674)   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 646, in add_remote_agent
(VllmWorker rank=0 pid=90674)     raise RuntimeError(
(VllmWorker rank=0 pid=90674) RuntimeError: LLMDataDistCMgrConnectorWorker: Linking failed, comm id: 1
(VllmWorker rank=1 pid=90675) INFO 07-08 18:17:44 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=90675) Exception in thread metadata_agent_listener:
(VllmWorker rank=1 pid=90675) Traceback (most recent call last):
(VllmWorker rank=1 pid=90675)   File "/usr/local/python3.10.17/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
(VllmWorker rank=1 pid=90675)     self.run()
(VllmWorker rank=1 pid=90675)   File "/usr/local/python3.10.17/lib/python3.10/threading.py", line 953, in run
(VllmWorker rank=1 pid=90675)     self._target(*self._args, **self._kwargs)
(VllmWorker rank=1 pid=90675)   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 356, in listen_for_agent_metadata_req
(VllmWorker rank=1 pid=90675)     self.add_remote_agent(decode_msg)
(VllmWorker rank=1 pid=90675)   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 646, in add_remote_agent
(VllmWorker rank=1 pid=90675)     raise RuntimeError(
(VllmWorker rank=1 pid=90675) RuntimeError: LLMDataDistCMgrConnectorWorker: Linking failed, comm id: 1
```

d1:
```bash
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:687] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id=None, server_id='10.222.49.196', device_id='1', device_ip='192.168.58.66', super_device_id=None, cluster_id=3)
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:630] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.168.58.66_192.168.58.206
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] rank table 
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '1', 'device_ip': '192.168.58.66', 'rank_id': '0'}], 'server_id': '10.222.49.196'}, {'device': [{'device_id': '5', 'device_ip': '192.168.58.206', 'rank_id': '1'}], 'server_id': '10.222.59.36'}]}
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:634] comm name: pd_comm_192.168.58.66_192.168.58.206
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:687] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id=None, server_id='10.222.49.196', device_id='6', device_ip='192.168.58.71', super_device_id=None, cluster_id=4)
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:635] cluster rank info: {3: 0, 5: 1}
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:630] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.168.58.71_192.168.58.207
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] rank table 
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:633] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '6', 'device_ip': '192.168.58.71', 'rank_id': '0'}], 'server_id': '10.222.49.196'}, {'device': [{'device_id': '6', 'device_ip': '192.168.58.207', 'rank_id': '1'}], 'server_id': '10.222.59.36'}]}
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:634] comm name: pd_comm_192.168.58.71_192.168.58.207
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:38 [llmdatadist_c_mgr_connector.py:635] cluster rank info: {4: 0, 6: 1}
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:39 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:39 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:40 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:40 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:41 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:41 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:42 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:42 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:43 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:43 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=106620) INFO 07-08 18:17:44 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=1 pid=106621) INFO 07-08 18:17:44 [llmdatadist_c_mgr_connector.py:650] Checking query_register_mem_status again
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527] WorkerProc hit an exception.
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527] Traceback (most recent call last):
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm/vllm/v1/executor/multiproc_executor.py", line 522, in worker_busy_loop
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     output = func(*args, **kwargs)
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 181, in execute_model
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     return func(*args, **kwargs)
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1288, in execute_model
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     return self.kv_connector_no_forward(scheduler_output)
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1435, in kv_connector_no_forward
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     self.maybe_setup_kv_connector(scheduler_output)
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1459, in maybe_setup_kv_connector
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     kv_connector.start_load_kv(get_forward_context())
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 145, in start_load_kv
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     self.connector_worker.start_load_kv(self._connector_metadata)
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 525, in start_load_kv
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     self._read_blocks(meta.local_block_ids,
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 703, in _read_blocks
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     remote_cluster_id = self.connect_to_remote_agent(
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 688, in connect_to_remote_agent
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     cluster_id = self.add_remote_agent(metadata)
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]   File "/workspace/mnt/cmss-yangqinghao/Projects/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 646, in add_remote_agent
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527]     raise RuntimeError(
(VllmWorker rank=0 pid=106620) ERROR 07-08 18:17:44 [multiproc_executor.py:527] RuntimeError: LLMDataDistCMgrConnectorWorker: Linking failed, comm id: 1
(EngineCore_0 pid=106467) ERROR 07-08 18:17:44 [dump_input.py:69] Dumping input data
```
