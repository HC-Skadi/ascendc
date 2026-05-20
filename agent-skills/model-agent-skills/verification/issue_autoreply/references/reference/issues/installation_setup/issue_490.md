# Issue #490: [Usage]: 昇腾环境启动vllm服务报错RuntimeError: Engine process failed to start. See stack trace for the root cause.

## 基本信息

- **编号**: #490
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/490
- **创建时间**: 2025-04-09T07:28:10Z
- **关闭时间**: 2025-04-09T16:02:23Z
- **更新时间**: 2025-04-09T16:02:24Z
- **提交者**: @xyh1989
- **评论数**: 1

## 标签

无

## 问题描述

### Your current environment

![Image](https://github.com/user-attachments/assets/28333432-a1e1-4a65-a854-a205f4fa9dca)

![Image](https://github.com/user-attachments/assets/6183e6b9-6265-403f-9e16-a50dd7af75b6)

(vllm-ascend-env) [root@localhost vllm]# python3 collect_env.py 
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: UOS Server 20 (aarch64)
GCC version: (GCC) 12.2.0
Clang version: 12.0.1 (UnionTech 12.0.1-1.uel20.01 e9eaec74682acb8c06121fed4566bb7e7b99bba8)
CMake version: version 3.16.5
Libc version: glibc-2.28

Python version: 3.10.16 (main, Apr  3 2025, 08:58:15) [GCC 7.3.0] (64-bit runtime)
Python platform: Linux-4.19.90-2403.3.0.0270.98.uel20.aarch64-aarch64-with-glibc2.28
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
架构：                              aarch64
CPU 运行模式：                      64-bit
字节序：                            Little Endian
CPU:                                96
在线 CPU 列表：                     0-95
每个核的线程数：                    1
每个座的核数：                      48
座：                                2
NUMA 节点：                         4
厂商 ID：                           HiSilicon
BIOS 厂商 ID：                      Hisilicon
型号：                              0
型号名称：                          Kunpeng-920
BIOS 型号名称：                     Kunpeng 920-4826
步进：                              0x1
CPU 最大 MHz：                      2600.0000
CPU 最小 MHz：                      200.0000
BogoMIPS：                          200.00
L1d 缓存：                          6 MiB
L1i 缓存：                          6 MiB
L2 缓存：                           48 MiB
L3 缓存：                           128 MiB
NUMA 节点0 CPU：                    0-23
NUMA 节点1 CPU：                    24-47
NUMA 节点2 CPU：                    48-71
NUMA 节点3 CPU：                    72-95
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec store bypass:    Vulnerable
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected
标记：                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] transformers==4.51.1
[conda] Could not collect
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.7.3
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/gcc-12.2.0/lib64:
OMP_NUM_THREADS=96
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1



### How would you like to use vllm on ascend

希望能够在昇腾环境下通过VLLM启动DeekSeek模型

