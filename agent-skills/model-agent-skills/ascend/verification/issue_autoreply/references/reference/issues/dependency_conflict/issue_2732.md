# Issue #2732: [Bug]: Server crashes when running benchmark(deepseek-v3.1) with DP 2

## 基本信息

- **编号**: #2732
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2732
- **创建时间**: 2025-09-03T11:09:02Z
- **关闭时间**: 2025-10-17T01:17:27Z
- **更新时间**: 2025-10-17T01:17:27Z
- **提交者**: @realliujiaxu
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Init 224280 task_queue_enable = 1
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.38

Python version: 3.11.6 (main, Jul  1 2025, 21:40:33) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
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
[pip3] pyzmq==27.0.2
[pip3] torch==2.7.1+cpu
[pip3] torch-npu==2.7.1+git382364d
[pip3] transformers==4.56.0
[conda] Could not collect
vLLM Version: 0.10.1.dev102+g57c22e57f (git sha: 57c22e57f)
vLLM Ascend Version: 0.9.2rc2.dev144+g875a86cbe.d20250820 (git sha: 875a86cbe, date: 20250820)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ASCEND_VISIBLE_DEVICES=4,12,0,8,6,14,3,11,5,13,2,10,7,15,1,9
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
| 0     910B2C              | OK            | 89.7        44                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          60333/ 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 93.0        46                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          60333/ 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 99.4        45                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          60354/ 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 95.2        44                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          60373/ 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 99.3        44                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          60353/ 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 100.6       48                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          60332/ 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 91.4        46                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          60352/ 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 96.8        47                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          60332/ 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 94.5        45                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          60355/ 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 94.1        46                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          60352/ 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 93.9        44                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          60352/ 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 92.3        47                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          60352/ 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 98.0        47                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          60352/ 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 97.6        47                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          60352/ 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 92.8        45                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          60353/ 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 101.9       48                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          60332/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 190611        | /usr/bin/python          | 113                     |
| 0       0                 | 191741        | /usr/bin/python          | 113                     |
| 0       0                 | 189446        | /usr/bin/python          | 113                     |
| 0       0                 | 190045        | /usr/bin/python          | 113                     |
| 0       0                 | 191176        | /usr/bin/python          | 113                     |
| 0       0                 | 189430        | /usr/bin/python          | 56540                   |
| 0       0                 | 189489        | /usr/bin/python          | 114                     |
| 0       0                 | 192306        | /usr/bin/python          | 114                     |
+===========================+===============+====================================================+
| 1       0                 | 189446        | /usr/bin/python          | 56999                   |
+===========================+===============+====================================================+
| 2       0                 | 189489        | /usr/bin/python          | 57020                   |
+===========================+===============+====================================================+
| 3       0                 | 190045        | /usr/bin/python          | 57040                   |
+===========================+===============+====================================================+
| 4       0                 | 190611        | /usr/bin/python          | 57020                   |
+===========================+===============+====================================================+
| 5       0                 | 191176        | /usr/bin/python          | 57001                   |
+===========================+===============+====================================================+
| 6       0                 | 191741        | /usr/bin/python          | 57020                   |
+===========================+===============+====================================================+
| 7       0                 | 192306        | /usr/bin/python          | 57000                   |
+===========================+===============+====================================================+
| 8       0                 | 191177        | /usr/bin/python          | 113                     |
| 8       0                 | 192307        | /usr/bin/python          | 113                     |
| 8       0                 | 191742        | /usr/bin/python          | 114                     |
| 8       0                 | 189447        | /usr/bin/python          | 113                     |
| 8       0                 | 190612        | /usr/bin/python          | 113                     |
| 8       0                 | 189431        | /usr/bin/python          | 56580                   |
| 8       0                 | 189490        | /usr/bin/python          | 113                     |
| 8       0                 | 190044        | /usr/bin/python          | 114                     |
+===========================+===============+====================================================+
| 9       0                 | 189447        | /usr/bin/python          | 57021                   |
+===========================+===============+====================================================+
| 10      0                 | 189490        | /usr/bin/python          | 57020                   |
+===========================+===============+====================================================+
| 11      0                 | 190044        | /usr/bin/python          | 57020                   |
+===========================+===============+====================================================+
| 12      0                 | 190612        | /usr/bin/python          | 57020                   |
+===========================+===============+====================================================+
| 13      0                 | 191177        | /usr/bin/python          | 57020                   |
+===========================+===============+====================================================+
| 14      0                 | 191742        | /usr/bin/python          | 57021                   |
+===========================+===============+====================================================+
| 15      0                 | 192307        | /usr/bin/python          | 57000                   |
+===========================+===============+====================================================+

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

1. run server

```bash
rm -rf .torchair_cache

export VLLM_USE_V1=1
export VLLM_VERSION=0.10.1.1
export TASK_QUEUE_ENABLE=0

export ACL_STREAM_TIMEOUT=340000

python -m vllm.entrypoints.openai.api_server --model=/mnt/deepseek/DeepSeek-R1-W8A8-VLLM \
    --quantization ascend \
    --load-format=auto \
    --served-model-name auto \
    --trust-remote-code \
    --distributed-executor-backend=mp \
    --port 8009 \
    -tp=8 \
    -dp=2 \
    --max-num-seqs 32 \
    --max-model-len 32768 \
    --max-num-batched-tokens 32768 \
    --block-size 128 \
    --enable-expert-parallel \
    --additional-config '{"torchair_graph_config":{"enabled":true,"use_cached_graph":true,"graph_batch_sizes":[32],"enable_multistream_mla": true}}' \
    --gpu-memory-utilization 0.96
```

2. run benchmark

```
REQ_RATE=inf
MAX_CON=24
NUM_PROMPT=200


python /vllm/benchmarks/benchmark_serving.py \
--backend openai-chat \
--dataset-name random \
--trust-remote-code \
--model /mnt/deepseek/DeepSeek-R1-W8A8-VLLM \
--served-model-name auto \
--random-input-len 4096 \
--random-output-len 100 \
--num-prompts ${NUM_PROMPT} \
--max-concurrency ${MAX_CON} \
--request-rate ${REQ_RATE} \
--ignore-eos \
--metric-percentiles "50,90,99" \
--base-url http://localhost:8009 \
--endpoint /v1/chat/completions \
--temperature 0.6
```

3. server report error
```
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596] WorkerProc hit an exception.
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596] Traceback (most recent call last):
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/ljx02299116/930/vllm/vllm/v1/executor/multiproc_executor.py", line 591, in worker_busy_loop
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     output = func(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/worker/worker_v1.py", line 205, in execute_model
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return func(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/worker/model_runner_v1.py", line 1639, in execute_model
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     hidden_states = self._generate_process_reqs_hidden_states(
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/torchair/torchair_model_runner.py", line 282, in _generate_process_reqs_hidden_states
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     hidden_states = self.model(
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]                     ^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 1044, in forward
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     hidden_states = self.model(input_ids, positions, kv_caches,
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 890, in forward
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     hidden_states, residual = layer(
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]                               ^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 740, in forward
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     hidden_states = self.self_attn(
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]                     ^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 605, in forward
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     output = self.mla_attn.impl.forward(self.mla_attn,
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/torchair/torchair_mla.py", line 1216, in forward
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     prefill_k_pe, prefill_k_nope = self.exec_kv_prefill(
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]                                    ^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/mnt/deepseek/cloudide/z37xj0b05t1yvqz2/vllm_ascend/torchair/torchair_mla.py", line 964, in exec_kv_prefill
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     _, _, k_pe, k_nope = torch_npu.npu_kv_rmsnorm_rope_cache(
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]   File "/usr/local/lib64/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]     return self._op(*args, **(kwargs or {}))
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596] RuntimeError: npu_kv_rmsnorm_rope_cache:third_party/op-plugin/op_plugin/ops/opapi/KvRmsNormRopeCacheNpuOpApi.cpp:46 NPU function error: call aclnnKvRmsNormRopeCache failed, error code is 561002
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596] [ERROR] 2025-09-03-19:05:48 (PID:191741, Device:6, RankID:-1) ERR00100 PTA call acl api failed.
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596] EZ9999: Inner Error!
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596] EZ9999: [PID: 191741] 2025-09-03-19:05:48.642.164 cos shape is invalid.[FUNC:GetShapeAttrsInfo][FILE:kv_rms_norm_rope_cache_tiling.cpp][LINE:298]
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]         TraceBack (most recent call last):
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]        KvRmsNormRopeCache do tiling failed, ret is -1.
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]        Check NnopbaseExecutorDoTiling(executor) failed
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]        Check NnopbaseExecutorMatchCache(executor) failed
[1;36m(VllmWorker TP6 pid=191741)[0;0m ERROR 09-03 19:05:48 [multiproc_executor.py:596]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed

```


