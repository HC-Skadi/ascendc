# Issue #3513: [Bug]: vllm:EngineCore process coredump while testing TextVQA dataset for both Qwen3-VL-30B-A3B-Instruct and Qwen2.5-VL-7B-Instruct

## 基本信息

- **编号**: #3513
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3513
- **创建时间**: 2025-10-17T02:18:31Z
- **关闭时间**: 2025-10-17T09:48:56Z
- **更新时间**: 2025-10-20T15:25:47Z
- **提交者**: @leijie-ww
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
[root@4257864fdaf1 workspace]# python collect_env.py
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-98.oe2403sp2)
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.38

Python version: 3.11.13 (main, Aug 29 2025, 04:31:33) [GCC 12.3.1 (openEuler 12.3.1-97.oe2403sp2)] (64-bit runtime)
Python platform: Linux-5.10.0-153.56.0.134.oe2203sp2.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250 To be filled by O.E.M. CPU @ 2.6GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
Stepping:                           0x1
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

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
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 98.7        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 88.1        34                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3394 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 87.7        34                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3411 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 98.7        34                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3411 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 93.4        38                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3412 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 89.4        37                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3409 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 94.8        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3409 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 94.2        39                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          50861/ 65536         |
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
| 7       0                 | 3990573       |                          | 47516                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux

</details>


### 🐛 Describe the bug

when we test TextVQA dataset, VLLM:EngineCore process coredump.

vllm-ascend log:

> (APIServer pid=3478) INFO 10-16 16:27:51 [loggers.py:127] Engine 000: Avg prompt throughput: 393.0 tokens/s, Avg generation throughput: 16.0 tokens/s, Running: 0 reqs, Waiting: 0he usage: 0.0%, Prefix cache hit rate: 47.8%
> (APIServer pid=3478) ERROR 10-16 16:27:53 [core_client.py:564] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.
> (Worker_TP0 pid=3752) INFO 10-16 16:27:53 [multiproc_executor.py:558] Parent process exited, terminating worker
> (Worker_TP1 pid=3753) INFO 10-16 16:27:53 [multiproc_executor.py:558] Parent process exited, terminating worker
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480] AsyncLLM output_handler failed.
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480] Traceback (most recent call last):
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 439, in output_handler
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480]     outputs = await engine_core.get_output_async()
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 846, in get_output_async
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480]     raise self._format_exception(outputs) from None
> (APIServer pid=3478) ERROR 10-16 16:27:53 [async_llm.py:480] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root caus
> (Worker_TP0 pid=3752) INFO 10-16 16:27:53 [multiproc_executor.py:599] WorkerProc shutting down.
> (Worker_TP1 pid=3753) INFO 10-16 16:27:53 [multiproc_executor.py:599] WorkerProc shutting down.
> (APIServer pid=3478) INFO:     Shutting down
> (APIServer pid=3478) INFO:     Waiting for application shutdown.
> (APIServer pid=3478) INFO:     Application shutdown complete.
> (APIServer pid=3478) INFO:     Finished server process [3478]

btw: There is no error in any plog files.

vllm:enginecore stack:

> Core was generated by `VLLM::EngineCore                                                              '.
> Program terminated with signal SIGBUS, Bus error.

> Thread 1 (LWP 3509):
> #0  0x0000ffffb5ec7c88 in ?? () from /opt/data/docker_data/overlay2/6dfeab51319ac475d3ee926d38ac31f7d340d0a14ae3416822725feaa974da8d/merged/lib/aarch64-linux-gnu/libc.so.6
> #1  0x0000ffffb61895c4 in copy_single (self=0xfffcf0e9c7c0, self=0xfffcf0e9c7c0, src=0xffffd1a0fa50, dest=0xffffd1a0faa0) at Objects/memoryobject.c:407
> #2  memory_ass_sub (self=0xfffcf0e9c7c0, key=<optimized out>, value=<optimized out>) at Objects/memoryobject.c:2603
> #3  0x0000ffffb60df4f4 in _PyEval_EvalFrameDefault (tstate=0xffffb656a680 <_PyRuntime+166344>, frame=0xffffb65e9798, throwflag=<optimized out>) at Python/ceval.c:2297
> #4  0x0000ffffb62342ac in _PyEval_EvalFrame (throwflag=0, frame=0xffffb65e9320, tstate=0xffffb656a680 <_PyRuntime+166344>) at ./Include/internal/pycore_ceval.h:73
> #5  _PyEval_Vector (tstate=0xffffb656a680 <_PyRuntime+166344>, func=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=<optimized out>) at Python/ceval.c:6434
> #6  0x0000ffffb613cb60 in _PyVectorcall_Call (kwargs=<optimized out>, tuple=<optimized out>, callable=0xfffd0f0f2c00, func=0xffffb613cc80 <_PyFunction_Vectorcall>, tstate=0xffffb656a680 <_PyRuntime+166344>) at Objects/call.c:257
> #7  _PyObject_Call (tstate=0xffffb656a680 <_PyRuntime+166344>, callable=0xfffd0f0f2c00, args=<optimized out>, kwargs=<optimized out>) at Objects/call.c:328
> #8  0x0000ffffb60e2380 in do_call_core (use_tracing=<optimized out>, kwdict=0xffffb5a7af00, callargs=0xffffb65502e0 <_PyRuntime+58920>, func=0xfffd0f0f2c00, tstate=0xffffb656a680 <_PyRuntime+166344>) at Python/ceval.c:7349
> #9  _PyEval_EvalFrameDefault (tstate=0xffffb656a680 <_PyRuntime+166344>, frame=0xffffb65e92a8, throwflag=<optimized out>) at Python/ceval.c:5376
> #10 0x0000ffffb623411c in _PyEval_EvalFrame (throwflag=0, frame=0xffffb65e9020, tstate=0xffffb656a680 <_PyRuntime+166344>) at ./Include/internal/pycore_ceval.h:73
> #11 _PyEval_Vector (args=0x0, argcount=0, kwnames=0x0, locals=0xffffb5d2fa40, func=0xffffb5d09f80, tstate=0xffffb656a680 <_PyRuntime+166344>) at Python/ceval.c:6434
> #12 PyEval_EvalCode (co=co@entry=0xffffb5cbcc60, globals=globals@entry=0xffffb5d2fa40, locals=locals@entry=0xffffb5d2fa40) at Python/ceval.c:1148
> #13 0x0000ffffb627e8bc in run_eval_code_obj (locals=0xffffb5d2fa40, globals=0xffffb5d2fa40, co=0xffffb5cbcc60, tstate=0xffffb656a680 <_PyRuntime+166344>) at Python/pythonrun.c:1741
> #14 run_mod (mod=mod@entry=0xaaaaec65a8c8, filename=filename@entry=0xffffb65471d8 <_PyRuntime+21792>, globals=globals@entry=0xffffb5d2fa40, locals=locals@entry=0xffffb5d2fa40, flags=flags@entry=0xffffd1a10080, arena=arena@entry=0xffffb5c578b0) at Python/pythonrun.c:1762
> #15 0x0000ffffb628082c in PyRun_StringFlags (str=str@entry=0xffffb5cd2350 "from multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=25, pipe_handle=27)\n", start=start@entry=257, globals=0xffffb5d2fa40, locals=0xffffb5d2fa40, flags=flags@entry=0xffffd1a10080) at Python/pythonrun.c:1632
> #16 0x0000ffffb62808b0 in PyRun_SimpleStringFlags (command=0xffffb5cd2350 "from multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=25, pipe_handle=27)\n", flags=flags@entry=0xffffd1a10080) at Python/pythonrun.c:487
> #17 0x0000ffffb62a12b0 in pymain_run_command (command=<optimized out>) at Modules/main.c:255
> #18 pymain_run_python (exitcode=0xffffd1a10078) at Modules/main.c:596
> #19 Py_RunMain () at Modules/main.c:684
> #20 0x0000ffffb62a1c2c in pymain_main (args=0xffffd1a10188) at Modules/main.c:714
> #21 Py_BytesMain (argc=<optimized out>, argv=<optimized out>) at Modules/main.c:738
> #22 0x0000ffffb5e573fc in ?? () from /opt/data/docker_data/overlay2/6dfeab51319ac475d3ee926d38ac31f7d340d0a14ae3416822725feaa974da8d/merged/lib/aarch64-linux-gnu/libc.so.6
> #23 0x0000ffffb5e574cc in __libc_start_main () from /opt/data/docker_data/overlay2/6dfeab51319ac475d3ee926d38ac31f7d340d0a14ae3416822725feaa974da8d/merged/lib/aarch64-linux-gnu/libc.so.6
> #24 0x0000aaaab8c408b0 in _start ()

<img width="1404" height="124" alt="Image" src="https://github.com/user-attachments/assets/7e18d395-3b85-49dd-9bc2-0bcdeca43517" />

EvalScope benchmark set:

> cat config_30b.yaml
> work_dir: outputs
> eval_backend: VLMEvalKit
> eval_config:
>   model:
>     - type: qwen25vl
>       name: CustomAPIModel
>       api_base: "http://71.10.29.136:8000/v1/chat/completions"
>       key: EMPTY
>       temperature: 0.0
>       img_size: -1
>   data:
>     - TextVQA_VAL
>   verbose: true
>   mode: all
>   limit: 0
>   reuse: false
>   nproc: 1
> debug: true

docker run cmd:

> export IMAGE=quay.io/ascend/vllm-ascend:v0.11.0rc0-openeuler
> docker run --privileged \
> --name test-qwen3-leijie-oe \
> --device /dev/davinci0 \
> --device /dev/davinci1 \
> --device /dev/davinci_manager \
> --device /dev/devmm_svm \
> --device /dev/hisi_hdc \
> -v /usr/local/dcmi:/usr/local/dcmi \
> -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
> -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
> -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
> -v /etc/ascend_install.info:/etc/ascend_install.info \
> -v /home/l00656382/ascend_work/cache:/root/.cache \
> -p 8000:8000 \
> -e VLLM_USE_MODELSCOPE=True \
> -e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 \
> -it $IMAGE /bin/bash

vllm serve cmd:

> vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct \
> --served-model-name qwen3vl \
> --dtype bfloat16 \
> --max_model_len 16384 \
> --max-num-batched-tokens 16384 \
> --tensor-parallel-size 2 \
> --enable_expert_parallel

> vllm serve Qwen/Qwen2.5-VL-7B-Instruct \
> --served-model-name qwen25vl \
> --dtype bfloat16 \
> --max_model_len 16384 \
> --max-num-batched-tokens 16384 \
> --tensor-parallel-size 2


When we run test for InfoVQA, DocVQA dataset, the same error occurs. 
And we guess the problem is not triggered by one specific test case, because when we reproduce the error, it will happen in different test case.

