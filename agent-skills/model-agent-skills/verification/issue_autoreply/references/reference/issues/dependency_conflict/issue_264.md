# Issue #264: [Bug]: npu oom when deploy DeepSeek R1

## 基本信息

- **编号**: #264
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/264
- **创建时间**: 2025-03-07T10:00:02Z
- **关闭时间**: 2025-04-09T16:20:19Z
- **更新时间**: 2025-04-10T01:36:29Z
- **提交者**: @gameofdimension
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.31.6
Libc version: glibc-2.35

Python version: 3.10.13 (main, Feb  7 2025, 09:46:40) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.36.0.112.4.oe2203sp1.x86_64-x86_64-with-glibc2.35
Is XNNPACK available: True

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          128
On-line CPU(s) list:             0-127
Vendor ID:                       GenuineIntel
Model name:                      Intel(R) Xeon(R) Platinum 8462Y+
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              32
Socket(s):                       2
Stepping:                        8
CPU max MHz:                     4100.0000
CPU min MHz:                     800.0000
BogoMIPS:                        5600.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves xfd cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req hfi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       3 MiB (64 instances)
L1i cache:                       2 MiB (64 instances)
L2 cache:                        128 MiB (64 instances)
L3 cache:                        120 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-31,64-95
NUMA node1 CPU(s):               32-63,96-127
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled, PBRSB-eIBRS: Vulnerable
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] mindietorch==1.0a71+torch2.1.0.abi0
[pip3] numpy==1.26.4
[pip3] pyzmq==26.2.1
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250226
[pip3] torchaudio==2.5.1+cpu
[pip3] torchvision==0.20.1+cpu
[pip3] transformers==4.49.0
[conda] Could not collect
vLLM Version: 0.7.3.dev254+g7a0f6885
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_VISIBLE_DEVICES=5,10,11,13,4,6,2,7,9,12,1,0,14,15,3,8
ASCEND_RUNTIME_OPTIONS=
ASCEND_SLOG_PRINT_TO_STDOUT=0
ASCEND_GLOBAL_EVENT_ENABLE=0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_GLOBAL_LOG_LEVEL=3
ASCEND_CUSTOM_OPP_PATH=/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/aie_ascendc:/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/customize:
PYTORCH_INSTALL_PATH=/usr/local/python3.10.13/lib/python3.10/site-packages/torch
PYTORCH_NPU_INSTALL_PATH=/usr/local/python3.10.13/lib/python3.10/site-packages/torch_npu
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.10.13/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/python3.10.13/lib/python3.10/site-packages/torch_npu/lib:/usr/local/python3.10.13/lib/python3.10/site-packages/torch/lib:/usr/local/Ascend/llm_models/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/mindie/latest/mindie-llm/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-llm/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-torch/lib:/usr/local/Ascend/mindie/latest/mindie-rt/lib:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/python3.10.13/lib:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
CUDA_HOME=/usr/local/cuda
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc1                 Version: 24.1.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 86.8        35                0    / 0             |
| 0                         | 0000:66:00.0  | 0           0    / 0          59356/ 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 103.1       37                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 94.0        36                0    / 0             |
| 0                         | 0000:52:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 95.1        36                0    / 0             |
| 0                         | 0000:3F:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 91.0        36                0    / 0             |
| 0                         | 0000:E3:00.0  | 0           0    / 0          59346/ 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 104.0       38                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 95.3        36                0    / 0             |
| 0                         | 0000:BD:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 97.5        36                0    / 0             |
| 0                         | 0000:CF:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 103.2       36                0    / 0             |
| 0                         | 0000:65:00.0  | 0           0    / 0          59353/ 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 90.4        36                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          59345/ 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 99.7        36                0    / 0             |
| 0                         | 0000:51:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 90.7        37                0    / 0             |
| 0                         | 0000:3E:00.0  | 0           0    / 0          59345/ 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 88.2        36                0    / 0             |
| 0                         | 0000:E2:00.0  | 0           0    / 0          59345/ 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 98.0        35                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 98.6        35                0    / 0             |
| 0                         | 0000:BE:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 104.2       35                0    / 0             |
| 0                         | 0000:D0:00.0  | 0           0    / 0          59351/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 418635        | vllm                     | 56057                   |
+===========================+===============+====================================================+
| 1       0                 | 418709        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 2       0                 | 418694        | rayNPURayWork            | 56062                   |
+===========================+===============+====================================================+
| 3       0                 | 418711        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 4       0                 | 418705        | rayNPURayWork            | 56057                   |
+===========================+===============+====================================================+
| 5       0                 | 418704        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 6       0                 | 418697        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 7       0                 | 418695        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 8       0                 | 418693        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 9       0                 | 418696        | rayNPURayWork            | 56057                   |
+===========================+===============+====================================================+
| 10      0                 | 418700        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 11      0                 | 418701        | rayNPURayWork            | 56057                   |
+===========================+===============+====================================================+
| 12      0                 | 418710        | rayNPURayWork            | 56057                   |
+===========================+===============+====================================================+
| 13      0                 | 418698        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 14      0                 | 418712        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+
| 15      0                 | 418714        | rayNPURayWork            | 56063                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/x86_64-linux
```

</details>


### 🐛 Describe the bug

#### launch script

```
    export VLLM_HOST_IP=${host_ip}
    export HCCL_CONNECT_TIMEOUT=120
    export HCCL_IF_IP=${host_ip}

    ckpt='/path/to/DeepSeek-R1-bf16/'

    VLLM_TORCH_PROFILER_DIR=/home/vllm_profile/
    export OMP_NUM_THREADS=1
    # export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
    vllm serve "${ckpt}" \
        --trust-remote-code \
        --served-model-name=demo \
        --distributed_executor_backend="ray" \
        --enforce-eager \
        --gpu-memory-utilization=0.9 \
        --tensor_parallel_size=16 \
        --pipeline_parallel_size=2
```

#### stack trace
```
(NPURayWorkerWrapper pid=399586, ip=10.43.132.227) [rank16]:[W307 09:50:42.924197462 MoeInitRoutingKernelNpuOpApi.cpp:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
(NPURayWorkerWrapper pid=399586, ip=10.43.132.227) [W307 09:37:04.246385434 socket.cpp:752] [c10d] The client socket cannot be initialized to connect to [pytorch-r1-mindie-lab-mlp-1969590-worker-0.pytorch-r1-mindie-lab-mlp-1969590.mlp.svc.gd18-llm-002.vip.com]:57189 (errno: 97 - Address family not supported by protocol). [repeated 30x across cluster]
[rank0]:[W307 09:50:44.774227369 MoeInitRoutingKernelNpuOpApi.cpp:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581] Error executing method 'determine_num_available_blocks'. This might cause deadlock in distributed execution.
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581] Traceback (most recent call last):
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return run_method(target, method, args, kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return func(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return func(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 227, in determine_num_available_blocks
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     self.model_runner.profile_run()
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return func(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1355, in profile_run
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     self.execute_model(model_input, kv_caches, intermediate_tensors)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return func(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1135, in execute_model
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     hidden_or_intermediate_states = model_executable(
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self._call_impl(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return forward_call(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 677, in forward
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     hidden_states = self.model(input_ids, positions, kv_caches,
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self.forward(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 633, in forward
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     hidden_states, residual = layer(positions, hidden_states,
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self._call_impl(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return forward_call(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 560, in forward
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     hidden_states = self.mlp(hidden_states)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self._call_impl(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return forward_call(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 162, in forward
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     final_hidden_states = self.experts(
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self._call_impl(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return forward_call(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 586, in forward
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     final_hidden_states = self.quant_method.apply(
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 120, in apply
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self.forward(x=x,
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self._forward_method(*args, **kwargs)
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm_ascend/ops/fused_moe.py", line 181, in forward_oot
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return fused_experts(hidden_states=x,
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/vllm_ascend/ops/fused_moe.py", line 110, in fused_experts
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     expanded_x, expanded_row_idx, expanded_expert_idx = torch_npu.npu_moe_init_routing(
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]   File "/usr/local/python3.10.13/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581]     return self._op(*args, **(kwargs or {}))
(NPURayWorkerWrapper pid=399601, ip=10.43.132.227) ERROR 03-07 09:51:00 worker_base.py:581] RuntimeError: NPU out of memory. Tried to allocate 17.50 GiB (NPU 15; 60.97 GiB total capacity; 53.74 GiB already allocated; 53.74 GiB current active; 5.96 GiB free; 54.36 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
```
