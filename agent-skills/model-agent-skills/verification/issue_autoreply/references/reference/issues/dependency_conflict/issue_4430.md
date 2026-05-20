# Issue #4430: [Bug]: [v0.11.0-dev] qwen2.5-vl-72b reports a shape ERROR during the _prepare_inputs phase under high concurrency.

## 基本信息

- **编号**: #4430
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4430
- **创建时间**: 2025-11-25T08:11:53Z
- **关闭时间**: 2025-12-22T11:10:57Z
- **更新时间**: 2025-12-22T11:10:57Z
- **提交者**: @Levi-JQ
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Init 11803 task_queue_enable = 1
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.38

Python version: 3.11.6 (main, Oct 29 2025, 18:39:28) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
Python platform: Linux-5.10.112-100.alios7.x86_64-x86_64-with-glibc2.38

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
Model name:                      Intel(R) Xeon(R) Platinum 8468
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              48
Socket(s):                       2
Stepping:                        8
BogoMIPS:                        4200.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm uintr md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       4.5 MiB (96 instances)
L1i cache:                       3 MiB (96 instances)
L2 cache:                        192 MiB (96 instances)
L3 cache:                        210 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-47,96-143
NUMA node1 CPU(s):               48-95,144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] flake8==7.3.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1+gitb649cc2
[pip3] torchvision==0.16.0
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.1.dev26+g745ef2584 (git sha: 745ef2584)
vLLM Ascend Version: 0.11.0rc1.dev230+g37912fdb1 (git sha: 37912fdb1)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ASCEND_VISIBLE_DEVICES=5,13,0,8,1,9,7,15,4,12,3,11,6,14,2,10
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ATB_LLM_COMM_BACKEND=hccl
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ATB_LLM_HCCL_ENABLE=1
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/lib64/python3.11/site-packages/vllm_ascend:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_LOGGING_CONFIG_PATH=/home/admin/vllm/logging_config.json
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1               Version: 25.0.rc1.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 91.5        44                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3446 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 94.7        46                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 96.1        46                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 89.9        44                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3435 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 93.3        45                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 96.5        46                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3435 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 87.8        46                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 90.8        44                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3435 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 91.5        44                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3430 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 99.7        45                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3437 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 88.8        44                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 93.3        45                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3437 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 90.2        44                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3437 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 96.3        45                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 91.0        44                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 97.5        45                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3436 / 65536         |
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
| No running processes found in NPU 8                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 9                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 10                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 11                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 12                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 13                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 14                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 15                                                           |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC001B235
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug

server log:
```shell
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671] WorkerProc hit an exception.
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671] Traceback (most recent call last):
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]     output = func(*args, **kwargs)
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 308, in execute_model
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]   File "/usr/local/lib64/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]     return func(*args, **kwargs)
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1924, in execute_model
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1426, in _prepare_inputs
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]     logits_indices = torch.from_numpy(cu_num_tokens - 1).to(
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnIndexPutImpl.
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP5 pid=7129) ERROR 2025-11-25 15:18:55.343 [multiproc_executor.py:671] [ERROR] 2025-11-25-15:18:55 (PID:7129, Device:5, RankID:-1) ERR00100 PTA call acl api failed.
```

plog:
```shell
plog-2950_20251125150202583.log:1:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.389.956 [broadcast_to.cc:102][OP_PROTO][InferShape4BroadcastTo][3373] OpName:[BroadcastTo] "[5041, 8192] can not broadcast to [5042, 8192]"
plog-2950_20251125150202583.log:2:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.390.004 [op_executor.cpp:119][NNOP][InferShape][3373] errno[561000] OpName:[aclnnIndexPutImpl_5225123] infer shape fail, [4294967295]
plog-2950_20251125150202583.log:3:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.390.038 [op_executor.cpp:80][NNOP][InferShape][3373] errno[561000] OpName:[aclnnIndexPutImpl_5225123] Infer Shape failed.
plog-2950_20251125150202583.log:4:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.171 [fusion.cc:79][OP_PROTO][AddShape][3373] OpName:[Fusion] "input shapes [5041] cannot broadcast to shape [5042]"
plog-2950_20251125150202583.log:5:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.184 [broadcast_v3.cc:1686][OP_PROTO][CompletedShapes][3373] OpName:[BroadcastTo] "add input shapes failed"
plog-2950_20251125150202583.log:6:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.189 [auto_tiling_rt2.cc:109][OP_PROTO][AutoTilingRun][3373] OpName:[BroadcastTo] "Autotiling func failed"
plog-2950_20251125150202583.log:7:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.193 [broadcastto.cc:114][OP_PROTO][Tiling4BroadcastTo][3373] OpName:[BroadcastTo] "call DoTiling failed"
plog-2950_20251125150202583.log:8:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.199 [kernel_workspace.cpp:158][NNOP][Tiling][3373] errno[561000] OpName:[aclnnIndexPutImpl_5225123_BroadcastToAiCore] Tiling failed
plog-2950_20251125150202583.log:9:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.207 [op_executor.cpp:615][NNOP][Launch][3373] errno[561103] OpName:[aclnnIndexPutImpl_5225123_BroadcastToAiCore] Tiling Failed.
plog-2950_20251125150202583.log:10:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.212 [op_executor.cpp:70][NNOP][Run][3373] errno[561103] OpName:[aclnnIndexPutImpl_5225123_BroadcastToAiCore] Kernel Run failed. opType: 32, BroadcastTo
plog-2950_20251125150202583.log:11:[ERROR] OP(2950,ker_TP2):2025-11-25-15:02:02.392.217 [op_executor.cpp:837][NNOP][Run][3373] errno[561103] OpName:[aclnnIndexPutImpl_5225123_BroadcastToAiCore] launch failed for BroadcastTo, errno:561103.
plog-2950_20251125150202583.log:12:[ERROR] APP(2950,ker_TP2):2025-11-25-15:02:02.407.487 [log_inner.cpp:77]3373 torch_npu/csrc/framework/OpParamMaker.cpp:ExecFuncOpApi:448: "[PTA]:"Custom hand error:operator():third_party/op-plugin/op_plugin/ops/opapi/IndexPutKernelNpuOpApi.cpp:73 NPU function error: call aclnnIndexPutImpl failed, error code is 561103
```
