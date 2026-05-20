# Issue #3529: [Bug]: cannot start model with Multi-Node-Ray EP+PP2*TP8 (RuntimeError: ACL stream synchronize failed, error code:507014)

## 基本信息

- **编号**: #3529
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3529
- **创建时间**: 2025-10-18T08:46:53Z
- **关闭时间**: 2025-12-15T09:33:35Z
- **更新时间**: 2025-12-16T08:03:17Z
- **提交者**: @ChrisKimZHT
- **评论数**: 10

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...    
PyTorch version: 2.7.1+cpu                                   
Is debug build: False                                      
                                                                               
OS: Ubuntu 22.04.5 LTS (aarch64)                           
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0                                                                                                                                                                                                                                                                           
Clang version: Could not collect                                                                                                                                                                                                                                                                                             
CMake version: version 4.1.0                                                                                                                                                                                                                                                                                                 
Libc version: glibc-2.35                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                             
Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)                                                                                                                                                                                                                                          
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.35

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
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.0
[conda] Could not collect
vLLM Version: 0.11.0rc3
vLLM Ascend Version: 0.11.0rc0

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0                                              
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:                                                                                                                                   
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest                                                                                                     
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1           
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
| 0     910B4               | OK            | 86.0        40                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2849 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 94.0        41                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2843 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 88.6        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2841 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 89.0        41                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2842 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 91.2        41                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2841 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 91.9        44                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2849 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 94.5        41                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2843 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 88.1        44                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2841 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
                                                                                                                                                              
CANN:                                                                                                                                                         
package_name=Ascend-cann-toolkit                                                                                                                              
version=8.2.RC1                                                                                                                                               
innerversion=V100R001C22SPC001B231                                                                                                                            
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64                                                                                                                                                  
os=linux                                                                                                                                                      
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux
```

</details>

complete error log: [error.log](https://github.com/user-attachments/files/22983226/error.log)

docker image: `quay.io/ascend/vllm-ascend:v0.11.0rc0` (manual update transformers to 4.57.0)

docker command:

```bash
docker run --rm \
    --name vllm-ascend-env \
    --net=host \
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
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -v /data:/data \
    -it quay.io/ascend/vllm-ascend:v0.11.0rc0 bash
```

ray command:

```bash
# Head node
export HCCL_IF_IP=192.168.0.147
export GLOO_SOCKET_IFNAME=enp67s0f5
export TP_SOCKET_IFNAME=enp67s0f5
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ray start --head

# Worker node
export HCCL_IF_IP=192.168.0.35
export GLOO_SOCKET_IFNAME=enp67s0f5
export TP_SOCKET_IFNAME=enp67s0f5
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ray start --address='192.168.0.147:6379' --node-ip-address=192.168.0.35
```

vllm command:

```bash
# pp2*tp8
vllm serve /data/Qwen3-VL-30B-A3B-Instruct \
  --served-model-name qwen3-vl \
  --disable-uvicorn-access-log \
  --disable-log-requests \
  --distributed-executor-backend ray \
  --pipeline-parallel-size 2 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --max-model-len 32768  \
  --gpu-memory-utilization 0.9
```

### 🐛 Describe the bug

TP16 work fine in my environment, but EP+PP2*TP8 not working with error `RuntimeError: ACL stream synchronize failed, error code:507014`.

TP16 vllm command:

```
vllm serve /data/Qwen3-VL-30B-A3B-Instruct \
  --served-model-name qwen3-vl \
  --disable-uvicorn-access-log \
  --disable-log-requests \
  --distributed-executor-backend ray \
  --tensor-parallel-size 16 \
  --enable-expert-parallel \
  --max-model-len 32768  \
  --gpu-memory-utilization 0.9
```
