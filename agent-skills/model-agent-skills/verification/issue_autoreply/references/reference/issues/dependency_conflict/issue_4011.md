# Issue #4011: [Bug]: flashcomm1 report shape error in DP>1

## 基本信息

- **编号**: #4011
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4011
- **创建时间**: 2025-11-05T09:51:43Z
- **关闭时间**: 2025-12-30T10:57:58Z
- **更新时间**: 2025-12-30T10:57:58Z
- **提交者**: @Levi-JQ
- **评论数**: 1

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

OS: openEuler 24.03 (LTS) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.38

Python version: 3.11.6 (main, Sep 23 2025, 18:31:41) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
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
[pip3] torch_npu==2.7.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.1rc3
vLLM Ascend Version: 0.11.0rc1.dev284+g660910ba9 (git sha: 660910ba9)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ASCEND_VISIBLE_DEVICES=0,8,4,12,3,11,2,10,5,13,7,15,6,14,1,9
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ATB_LLM_COMM_BACKEND=hccl
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ATB_LLM_HCCL_ENABLE=1
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/lib64/python3.11/site-packages/vllm_ascend:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
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
| 0     910B2C              | OK            | 95.7        45                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3440 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 94.8        46                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3433 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 92.4        45                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3433 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 94.1        46                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 92.6        47                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3433 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 98.3        47                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 104.6       47                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 92.2        47                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3433 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 94.8        46                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 99.0        47                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3431 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 88.9        45                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 95.2        47                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 97.9        48                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 101.4       48                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 94.9        47                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 100.1       47                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3432 / 65536         |
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
innerversion=V100R001C23SPC001B224
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug
版本：
vllm-ascend：46d5a7768808b450aed6e097bca5523ab322bcb7
vllm：83f478bb19489b41e9d208b47b4bb5a95ac171ac

启动脚本
```shell
export TASK_QUEUE_ENABLE=0
export VLLM_USE_V1=1
export VLLM_VERSION=0.11.1

export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE=AIV
export HCCL_OP_BASE_FFTS_MODE_ENABLE=true
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0

export VLLM_ASCEND_ENABLE_FLASHCOMM1=1


rm -rf ./.torchair_cache/
nohup python -m vllm.entrypoints.openai.api_server \
    --host 0.0.0.0 \
    --model=/mnt/deepseek/model/w8a8-qwen3-235b-a22b/model/ \
    --trust-remote-code \
    --served-model-name auto \
    --distributed-executor-backend=mp \
    --port 8100 \
    -tp=4 \
    -dp=2 \
    --max-num-seqs 24 \
    --max-model-len 32768 \
    --max-num-batched-tokens 32768 \
    --block-size 128 \
    --no-enable-prefix-caching \
    --enable-expert-parallel \
    --enforce-eager \
    --additional-config '{"torchair_graph_config":{"enabled":false,"use_cached_graph":false},"ascend_scheduler_config":{"enabled":false}}' \
    --gpu-memory-utilization 0.90 \
    --enable-prompt-tokens-details \
    --kv-transfer-config \
    '{
        "kv_connector": "MooncakeConnectorV1",
        "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
        "kv_buffer_device": "npu",
        "kv_role": "kv_producer",
        "kv_parallel_size": 2,
        "kv_port": "20002",
        "engine_id": "prefill-0",
        "kv_rank": 0,
        "kv_connector_extra_config": {
             "use_ascend_direct": true,
             "prefill": {
                    "dp_size": 2,
                    "tp_size": 4
             },
             "decode": {
                    "dp_size": 16,
                    "tp_size": 1
             }
        }
    }' &> fc2+fc1.log &
disown
```
报错信息
```shell
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699] RuntimeError: shape '[2, 32768]' is invalid for input of size 16384
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699] Traceback (most recent call last):
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/v1/executor/multiproc_executor.py", line 694, in worker_busy_loop
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     output = func(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 230, in determine_available_memory
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     self.model_runner.profile_run()
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2999, in profile_run
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states = self._dummy_run(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return func(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2962, in _dummy_run
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2765, in _generate_dummy_run_hidden_states
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states = self.model(input_ids=input_ids,
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/models/qwen3_moe.py", line 741, in forward
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states = self.model(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                     ^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/compilation/decorators.py", line 261, in __call__
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self.forward(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/models/qwen3_moe.py", line 460, in forward
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states, residual = layer(positions, hidden_states, residual)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/models/qwen3_moe.py", line 392, in forward
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states = self.mlp(hidden_states)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/models/qwen3_moe.py", line 197, in forward
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     final_hidden_states = self.experts(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                           ^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/custom_op.py", line 46, in forward
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._forward_method(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/custom_op.py", line 81, in forward_oot
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self.forward_native(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2195, in forward_native
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     fused_output = torch.ops.vllm.moe_forward(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._op(*args, **(kwargs or {}))
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2593, in moe_forward
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self.forward_impl(hidden_states, router_logits)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 333, in forward_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states, router_logits, mc2_mask, context_metadata = forward_context.moe_comm_method.prepare(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 92, in prepare
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     hidden_states, router_logits, mc2_mask, context_metadata = self.prepare_finalize.prepare(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/ops/fused_moe/prepare_finalize.py", line 322, in prepare
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._prepare_with_ep_group(hidden_states, router_logits)
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/ops/fused_moe/prepare_finalize.py", line 338, in _prepare_with_ep_group
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     pertoken_scale = torch.ops.vllm.maybe_all_gather_and_maybe_unpad(
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/usr/local/lib64/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     return self._op(*args, **(kwargs or {}))
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]   File "/mnt/deepseek/cloudide/yujinqi/issue/flashcomm2-official/vllm-ascend/vllm_ascend/ops/register_custom_ops.py", line 49, in _maybe_all_gather_and_maybe_unpad_impl
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]     x = x.view(dp_size, forward_context.padded_length, *x.shape[1:])
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699] RuntimeError: shape '[2, 32768]' is invalid for input of size 16384
(Worker_DP1_TP3_EP7 pid=6088) ERROR 2025-11-05 17:47:06.062 [multiproc_executor.py:699]
```
