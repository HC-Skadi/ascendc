# Issue #223: [Bug]: openai起服务后对话两次报错MQLLMEngine terminated

## 基本信息

- **编号**: #223
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/223
- **创建时间**: 2025-03-03T08:10:09Z
- **关闭时间**: 2025-04-10T09:18:46Z
- **更新时间**: 2025-04-10T09:18:47Z
- **提交者**: @GenerallyCovetous
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>INFO 03-03 16:06:04 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-03 16:06:04 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-03 16:06:04 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-03 16:06:04 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-03 16:06:04 [__init__.py:44] plugin ascend loaded.
INFO 03-03 16:06:05 [__init__.py:198] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Ubuntu 20.04.5 LTS (aarch64)
GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
Clang version: Could not collect
CMake version: version 3.31.4
Libc version: glibc-2.31

Python version: 3.10.2 (main, Jan  8 2025, 06:13:36) [GCC 9.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.31
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
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
NUMA node(s):                    8
Vendor ID:                       0x48
Model:                           0
Stepping:                        0x1
BogoMIPS:                        200.00
L1d cache:                       12 MiB
L1i cache:                       12 MiB
L2 cache:                        96 MiB
L3 cache:                        192 MiB
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
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs

Versions of relevant libraries:
[pip3] mindietorch==1.0.0+torch2.1.0.abi0
[pip3] numpy==1.26.4
[pip3] pyzmq==26.2.1
[pip3] sentence-transformers==2.2.2
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250226
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0
[pip3] tritonclient==2.51.0
[conda] numpy                     1.23.0                   pypi_0    pypi
[conda] pyzmq                     26.2.0                   pypi_0    pypi
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.1.dev1+ge584b85 (git sha: e584b85
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

VLLM_WORKER_MULTIPROC_METHOD=spawn
PYTORCH_INSTALL_PATH=/usr/local/python3.10.2/lib/python3.10/site-packages/torch
PYTORCH_NPU_INSTALL_PATH=/usr/local/python3.10.2/lib/python3.10/site-packages/torch_npu
LD_LIBRARY_PATH=/usr/local/python3.10.2/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/python3.10.2/lib/python3.10/site-packages/torch_npu/lib:/usr/local/python3.10.2/lib/python3.10/site-packages/torch/lib:/usr/local/Ascend/llm_model/lib:/usr/local/Ascend/mindie/latest/mindie-llm/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-llm/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-torch/lib:/usr/local/Ascend/mindie/latest/mindie-rt/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/python3.10.2/lib:/usr/local/python3.10.2/lib/python3.10/site-packages/torch.libs:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1</summary>

```text
```

</details>


### 🐛 Describe the bug

```python
python -m vllm.entrypoints.openai.api_server  \
       --model=/home/ma-user/work/s00851266/Llama-3.1-8B-Instruct \
       --trust-remote-code \
       --enforce-eager \
       --max-model-len 8192 \
       --enable-prefix-caching \
       --gpu-memory-utilization=0.9 \
       --tensor_parallel 1 \
       --port 8080 \
       --served-model-name="llama31" \
       --block-size 128
```
拉起服务后对话每次只能进行2次, 第三次后必定报错:
```
ERROR 03-03 16:00:46 [engine.py:141]   File "/home/ma-user/work/s00851266/Vllm-Ascend/vllm/vllm-ascend/vllm_ascend/attention.py", line 609, in forward
ERROR 03-03 16:00:46 [engine.py:141]     raise RuntimeError(
ERROR 03-03 16:00:46 [engine.py:141] RuntimeError: Prefix cache and chunked prefill are currently not supported.
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [117911]
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/process.py", line 318, in _bootstrap
    util._exit_function()
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/util.py", line 334, in _exit_function
    _run_finalizers(0)
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/util.py", line 300, in _run_finalizers
    finalizer()
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 54, in wrapper
    return func(cls, *args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 219, in finalize
    cls.global_mgr.finalize()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/utils/multiprocess_util.py", line 84, in finalize
    self.mgr.shutdown()
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/managers.py", line 674, in _finalize_manager
    process.join(timeout=1.0)
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/process.py", line 149, in join
    res = self._popen.wait(timeout)
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/popen_fork.py", line 40, in wait
    if not wait([self.sentinel], timeout):
  File "/usr/local/python3.10.2/lib/python3.10/multiprocessing/connection.py", line 936, in wait
    ready = selector.select(timeout)
  File "/usr/local/python3.10.2/lib/python3.10/selectors.py", line 416, in select
    fd_event_list = self._selector.poll(timeout)
  File "/usr/local/python3.10.2/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 394, in signal_handler
    raise KeyboardInterrupt("MQLLMEngine terminated")
KeyboardInterrupt: MQLLMEngine terminated
```
