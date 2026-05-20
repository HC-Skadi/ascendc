# Issue #632: [Usage]: 容器中获取不到NPU信息

## 基本信息

- **编号**: #632
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/632
- **创建时间**: 2025-04-23T09:27:04Z
- **关闭时间**: 2025-04-24T15:00:55Z
- **更新时间**: 2025-04-24T15:00:55Z
- **提交者**: @padluo
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

```text
root@NPU:/workspace# npu-smi info
DrvMngGetConsoleLogLevel failed. (g_conLogLevel=3)
dcmi model initialized failed, because the device is used. ret is -8020
root@NPU:/workspace# cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
root@NPU:/workspace# python collect_env.py
DrvMngGetConsoleLogLevel failed. (g_conLogLevel=3)
[EVENT] PROFILING(846,python):2025-04-23-09:25:06.507.208 [msprof_callback_impl.cpp:336] >>> (tid:846) Started to register profiling ctrl callback.
[EVENT] PROFILING(846,python):2025-04-23-09:25:06.507.476 [msprof_callback_impl.cpp:343] >>> (tid:846) Started to register profiling hash id callback.
[INFO] PROFILING(846,python):2025-04-23-09:25:06.507.547 [prof_atls_plugin.cpp:117] (tid:846) RegisterProfileCallback, callback type is 7
[EVENT] PROFILING(846,python):2025-04-23-09:25:06.507.605 [msprof_callback_impl.cpp:350] >>> (tid:846) Started to register profiling enable host freq callback.
[INFO] PROFILING(846,python):2025-04-23-09:25:06.507.660 [prof_atls_plugin.cpp:117] (tid:846) RegisterProfileCallback, callback type is 8
[ERROR] ATRACE(846,python):2025-04-23-09:25:06.552.773 [trace_driver_api.c:56](tid:846) get platform info failed, drvErr=87.
[INFO] RUNTIME(846,python):2025-04-23-09:25:06.556.128 [task_fail_callback_manager.cc:52] 846 TaskFailCallBackManager: Constructor.
[INFO] HCCL(846,python):2025-04-23-09:25:06.632.232 [adapter_rts.cc:2646][846][adapter_rts.cc][CallBackInitRts] g_deviceType [6] g_deviceLogicId [-1] g_devicePhyId [-1]
[ERROR] RUNTIME(846,python):2025-04-23-09:25:08.236.015 [runtime.cc:1879]846 CheckHaveDevice:Call halGetDeviceInfo failed: drvRet=87, module type=0, info type=1.
[INFO] PROFILING(846,python):2025-04-23-09:25:08.236.221 [prof_atls_plugin.cpp:210] (tid:846) Module[7] register callback of ctrl handle.
[ERROR] RUNTIME(846,python):2025-04-23-09:25:08.279.862 [driver.cc:65]846 GetDeviceCount:Call drvGetDevNum, drvRetCode=87.
[ERROR] RUNTIME(846,python):2025-04-23-09:25:08.279.940 [api_c_device.cc:23]846 rtGetDeviceCount:ErrCode=507899, desc=[driver error:internal error], InnerCode=0x7020010
[ERROR] RUNTIME(846,python):2025-04-23-09:25:08.280.000 [error_message_manage.cc:53]846 FuncErrorReason:report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(846,python):2025-04-23-09:25:08.280.059 [error_message_manage.cc:53]846 FuncErrorReason:rtGetDeviceCount execute failed, reason=[driver error:internal error]
[ERROR] ASCENDCL(846,python):2025-04-23-09:25:08.280.151 [device.cpp:342]846 aclrtGetDeviceCount: get device count failed, runtime result = 507899.
[ERROR] APP(846,python):2025-04-23-09:25:08.280.260 [log_inner.cpp:76]846 build/CMakeFiles/torch_npu.dir/compiler_depend.ts:device_count:25: "[PTA]:"get device count of NPU failed""
INFO 04-23 09:25:10 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-23 09:25:10 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-23 09:25:10 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-23 09:25:10 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-23 09:25:10 [__init__.py:44] plugin ascend loaded.
INFO 04-23 09:25:10 [__init__.py:230] Platform plugin ascend is activated
[ERROR] TBE(846,python):2025-04-23-09:25:10.410.660 [ascendc_runtime.cpp:228]  846 AscendCheckSoCVersion:cur soc version unknowsoctype not found.
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-2102.2.0.0066.ctl2.aarch64-aarch64-with-glibc2.35
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

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
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
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
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.8.4
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1

[INFO] RUNTIME(846,python):2025-04-23-09:25:14.506.826 [task_fail_callback_manager.cc:57] 846 ~TaskFailCallBackManager: Destructor.
[INFO] RUNTIME(846,python):2025-04-23-09:25:14.510.814 [runtime.cc:2033] 846 ~Runtime: deconstruct runtime
[INFO] RUNTIME(846,python):2025-04-23-09:25:14.511.238 [runtime.cc:2040] 846 ~Runtime: wait monitor success, use=0.

```


### How would you like to use vllm on ascend

容器启动命令如下，容器中获取不到NPU信息。
# Update the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.8.4rc1
docker run --rm \
--name vllm-ascend \
--device /dev/davinci0 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash

