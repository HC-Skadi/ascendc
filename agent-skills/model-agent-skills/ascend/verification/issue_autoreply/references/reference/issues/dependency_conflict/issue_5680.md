# Issue #5680: [Bug]: Ubuntu A2 DeepSeek-V3.2 SingleNode Start Error in docker container

## 基本信息

- **编号**: #5680
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5680
- **创建时间**: 2026-01-07T03:42:57Z
- **关闭时间**: 2026-01-07T03:44:29Z
- **更新时间**: 2026-01-07T03:44:29Z
- **提交者**: @moluzhui
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

According to the [document](https://docs.vllm.ai/projects/ascend/en/latest/installation.html#set-up-using-docker), the operation is carried out by using the docker method. The command is executed in the following way: in the Docker container that is started in this manner, the model startup code also runs within the container.
```bash
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --device /dev/davinci0 \
    --device /dev/davinci1 \
    --device /dev/davinci2 \
    --device /dev/davinci3 \
    --device /dev/davinci4 \
    --device /dev/davinci5 \
    --device /dev/davinci6 \
    --device /dev/davinci7 \
    --device /dev/davinci8 \
    --device /dev/davinci9 \
    --device /dev/davinci10 \
    --device /dev/davinci11 \
    --device /dev/davinci12 \
    --device /dev/davinci13 \
    --device /dev/davinci14 \
    --device /dev/davinci15 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -v /data:/data \
    -it quay.io/ascend/vllm-ascend:v0.13.0rc1 bash
```
<details>
<summary>The output of `python collect_env.py`</summary>
```text
Your output of above commands here
# python3 collect_env.py
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:03:05) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-134-generic-x86_64-with-glibc2.35

CPU:
Architecture:                         x86_64
CPU op-mode(s):                       32-bit, 64-bit
Address sizes:                        46 bits physical, 57 bits virtual
Byte Order:                           Little Endian
CPU(s):                               192
On-line CPU(s) list:                  0-191
Vendor ID:                            GenuineIntel
Model name:                           Intel(R) Xeon(R) Platinum 8468V
CPU family:                           6
Model:                                143
Thread(s) per core:                   2
Core(s) per socket:                   48
Socket(s):                            2
Stepping:                             8
Frequency boost:                      enabled
CPU max MHz:                          2401.0000
CPU min MHz:                          800.0000
BogoMIPS:                             4800.00
Flags:                                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                       VT-x
L1d cache:                            4.5 MiB (96 instances)
L1i cache:                            3 MiB (96 instances)
L2 cache:                             192 MiB (96 instances)
L3 cache:                             195 MiB (2 instances)
NUMA node(s):                         2
NUMA node0 CPU(s):                    0-47,96-143
NUMA node1 CPU(s):                    48-95,144-191
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; RSB filling; PBRSB-eIBRS SW sequence; BHI BHI_DIS_S
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0+cpu
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 89.1        40                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 93.2        40                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3396 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 87.2        40                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 89.2        40                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 87.9        41                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 88.3        41                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 90.5        41                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3409 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 92.1        40                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3407 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 89.2        40                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3408 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 94.8        40                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3407 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 89.6        40                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 93.0        43                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 90.6        42                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 93.8        41                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 87.2        39                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 93.1        41                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3398 / 65536         |
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
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/x86_64-linux
```

</details>


### 🐛 Describe the bug

The code running in the **docker container(quay.io/ascend/vllm-ascend:v0.13.0rc1)** is as follows, the code is based on the V31 [documentation](https://docs.vllm.ai/projects/ascend/en/latest/tutorials/DeepSeek-V3.1.html).
```bash
#!/bin/sh
# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="xxxx"
local_ip="xxxx"

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is install on your machine, you can turn it on.
# export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

# AIV
export HCCL_OP_EXPANSION_MODE="AIV"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

vllm serve /data/models/models/vllm-ascend/DeepSeek-V3___2-W8A8 \
--host 0.0.0.0 \
--port 8015 \
--tensor-parallel-size 16 \
--quantization ascend \
--seed 1024 \
--served-model-name deepseek_v3 \
--enable-expert-parallel \
--async-scheduling \
--max-model-len 16384 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.8 \
--compilation-config '{"cudagraph_capture_sizes":[4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}'
```


DeepSeek-V3.2  failed to start and the error message is as follows

<details>
<summary>The part of error output of `bash start_llm.sh`</summary>
```text
Your output of above commands heren
(Worker_TP3_EP3 pid=13839) (Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     submod_0 = self.submod_0(l_input_ids_, s72, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_bias_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_60_modules_post_attention_layernorm_parameters_bias_ = 
xxxxxxx
l_self_modules_layers_modules_60_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_norm_parameters_weight_ = l_self_modules_norm_parameters_bias_ = None
ERROR 01-07 03:16:09 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^<Too many of this character>
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_compile_backend.py", line 230, in __call__
(EngineCore_DP0 pid=13783) [2026-01-07 03:16:09] ERROR patch_balance_schedule.py:670: EngineCore failed to start.
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self.compiled_graph_for_general_shape(*args)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 2474, in wrapper
(Worker_TP3_EP3 pid=13839) (EngineCore_DP0 pid=13783) Traceback (most recent call last):
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return pytree.tree_unflatten(compiled_fn(*args, **kwargs), spec)
ERROR 01-07 03:16:09 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^<Too many of this character>
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_balance_schedule.py", line 661, in run_engine_core
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_compile_backend.py", line 230, in __call__
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self.compiled_graph_for_general_shape(*args)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)     engine_core = EngineCoreProc(*args, **kwargs)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 2474, in wrapper
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return fn(*args, **kwargs)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return pytree.tree_unflatten(compiled_fn(*args, **kwargs), spec)
(EngineCore_DP0 pid=13783)     super().__init__(
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 1241, in forward
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
(EngineCore_DP0 pid=13783)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return fn(*args, **kwargs)
(EngineCore_DP0 pid=13783)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return compiled_fn(full_args)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 240, in _initialize_kv_caches
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 1241, in forward
(EngineCore_DP0 pid=13783)     available_gpu_memory = self.model_executor.determine_available_memory()
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 384, in runtime_wrapper
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return compiled_fn(full_args)
(EngineCore_DP0 pid=13783)                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     all_outs = call_func_at_runtime_with_args(
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)     return self.collective_rpc("determine_available_memory")
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 384, in runtime_wrapper
(EngineCore_DP0 pid=13783)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 126, in call_func_at_runtime_with_args
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     all_outs = call_func_at_runtime_with_args(
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     out = normalize_as_list(f(args))
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)     return aggregate(get_response())
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]                             ^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 126, in call_func_at_runtime_with_args
(EngineCore_DP0 pid=13783)                      ^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 750, in inner_fn
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     out = normalize_as_list(f(args))
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     outs = compiled_fn(args)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]                             ^^^^^^^
(EngineCore_DP0 pid=13783)     raise RuntimeError(
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 750, in inner_fn
(EngineCore_DP0 pid=13783) RuntimeError: Worker failed with error 'The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnMoeDistributeDispatchV3.
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 556, in wrapper
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     outs = compiled_fn(args)
(EngineCore_DP0 pid=13783) Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return compiled_fn(runtime_args)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783) Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 556, in wrapper
(EngineCore_DP0 pid=13783) [ERROR] 2026-01-07-03:16:09 (PID:13793, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 100, in g
(EngineCore_DP0 pid=13783) ', please check the stack trace above for the root cause
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return compiled_fn(runtime_args)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return f(*args)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 100, in g
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return f(*args)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/_lazy_graph_module.py", line 126, in _lazy_forward
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self(*args, **kwargs)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/_lazy_graph_module.py", line 126, in _lazy_forward
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self(*args, **kwargs)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     raise e
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     raise e
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
[rank2]:[E107 03:16:09.464015675 OpParamMaker.cpp:444] operator():third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-07-03:16:09 (PID:13817, Device:2, RankID:-1) ERR00100 PTA call acl api failed.
EZ9999: Inner Error!
EZ9999[PID: 13817] 2026-01-07-03:16:09.068.221 AclNN_Inner_Error(EZ9999):  Nnopbase fails to invoke the HcclAllocComResourceByTiling function of the hccl module. ret = 4, comm = 0x7efeaee63ec0.
        TraceBack (most recent call last):
       Check nnopbase::NnopBaseHcclWrapper::GetInstance().HcclAllocComResourceByTiling(commHandle, stream, ((NnopbaseTilingData *)executor->args->tilingInfo.tilingData)->GetData(), &contextAddr) failed
       Check NnopbaseGetHcomResource(executor, stream) failed
       Check NnopbaseExecutorGetMc2Num(executor, stream, &argsAddr, &mc2Num) failed
       Check NnopbaseExecutorPrepareParamsExt(executor, stream) failed
       Check NnopbaseRunWithWorkspace(executor, stream, workspace, workspaceSize) failed

Exception raised from operator() at third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x80 (0x7eff901164d0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x65 (0x7eff900b2f69 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1c6d44a (0x7eff696b244a in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x2f1d823 (0x7eff6a962823 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0xc82671 (0x7eff686c7671 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xc83340 (0x7eff686c8340 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xc81357 (0x7eff686c6357 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xdc253 (0x7eff9190f253 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x94ac3 (0x7eff91bdaac3 in /lib/x86_64-linux-gnu/libc.so.6)
frame #9: clone + 0x44 (0x7eff91c6ba74 in /lib/x86_64-linux-gnu/libc.so.6)

[rank10]:[E107 03:16:09.471375691 OpParamMaker.cpp:444] operator():third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-07-03:16:09 (PID:13977, Device:10, RankID:-1) ERR00100 PTA call acl api failed.
EZ9999: Inner Error!
EZ9999[PID: 13977] 2026-01-07-03:16:09.074.597 AclNN_Inner_Error(EZ9999):  Nnopbase fails to invoke the HcclAllocComResourceByTiling function of the hccl module. ret = 4, comm = 0x7f0ac4664ec0.
        TraceBack (most recent call last):
       Check nnopbase::NnopBaseHcclWrapper::GetInstance().HcclAllocComResourceByTiling(commHandle, stream, ((NnopbaseTilingData *)executor->args->tilingInfo.tilingData)->GetData(), &contextAddr) failed
       Check NnopbaseGetHcomResource(executor, stream) failed
       Check NnopbaseExecutorGetMc2Num(executor, stream, &argsAddr, &mc2Num) failed
       Check NnopbaseExecutorPrepareParamsExt(executor, stream) failed
       Check NnopbaseRunWithWorkspace(executor, stream, workspace, workspaceSize) failed

Exception raised from operator() at third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x80 (0x7f0b902d34d0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x65 (0x7f0b9026ff69 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1c6d44a (0x7f0b7f3e044a in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x2f1d823 (0x7f0b80690823 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0xc82671 (0x7f0b7e3f5671 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xc83340 (0x7f0b7e3f6340 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xc81357 (0x7f0b7e3f4357 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xdc253 (0x7f0ba703b253 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x94ac3 (0x7f0ba7306ac3 in /lib/x86_64-linux-gnu/libc.so.6)
frame #9: clone + 0x44 (0x7f0ba7397a74 in /lib/x86_64-linux-gnu/libc.so.6)

[rank1]:[E107 03:16:09.480770244 OpParamMaker.cpp:444] operator():third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-07-03:16:09 (PID:13800, Device:1, RankID:-1) ERR00100 PTA call acl api failed.
EZ9999: Inner Error!
EZ9999[PID: 13800] 2026-01-07-03:16:09.083.955 AclNN_Inner_Error(EZ9999):  Nnopbase fails to invoke the HcclAllocComResourceByTiling function of the hccl module. ret = 4, comm = 0x7f80e5341ec0.
        TraceBack (most recent call last):
       Check nnopbase::NnopBaseHcclWrapper::GetInstance().HcclAllocComResourceByTiling(commHandle, stream, ((NnopbaseTilingData *)executor->args->tilingInfo.tilingData)->GetData(), &contextAddr) failed
       Check NnopbaseGetHcomResource(executor, stream) failed
       Check NnopbaseExecutorGetMc2Num(executor, stream, &argsAddr, &mc2Num) failed
       Check NnopbaseExecutorPrepareParamsExt(executor, stream) failed
       Check NnopbaseRunWithWorkspace(executor, stream, workspace, workspaceSize) failed

Exception raised from operator() at third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x80 (0x7f81b10d34d0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x65 (0x7f81b106ff69 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1c6d44a (0x7f819fb8d44a in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x2f1d823 (0x7f81a0e3d823 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0xc82671 (0x7f819eba2671 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xc83340 (0x7f819eba3340 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xc81357 (0x7f819eba1357 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xdc253 (0x7f81c7de9253 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x94ac3 (0x7f81c80b4ac3 in /lib/x86_64-linux-gnu/libc.so.6)
frame #9: clone + 0x44 (0x7f81c8145a74 in /lib/x86_64-linux-gnu/libc.so.6)

[rank9]:[E107 03:16:09.501417881 OpParamMaker.cpp:444] operator():third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-07-03:16:09 (PID:13959, Device:9, RankID:-1) ERR00100 PTA call acl api failed.
EZ9999: Inner Error!
EZ9999[PID: 13959] 2026-01-07-03:16:09.106.732 AclNN_Inner_Error(EZ9999):  Nnopbase fails to invoke the HcclAllocComResourceByTiling function of the hccl module. ret = 4, comm = 0x7fde719b3ec0.
        TraceBack (most recent call last):
       Check nnopbase::NnopBaseHcclWrapper::GetInstance().HcclAllocComResourceByTiling(commHandle, stream, ((NnopbaseTilingData *)executor->args->tilingInfo.tilingData)->GetData(), &contextAddr) failed
       Check NnopbaseGetHcomResource(executor, stream) failed
       Check NnopbaseExecutorGetMc2Num(executor, stream, &argsAddr, &mc2Num) failed
       Check NnopbaseExecutorPrepareParamsExt(executor, stream) failed
       Check NnopbaseRunWithWorkspace(executor, stream, workspace, workspaceSize) failed

Exception raised from operator() at third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x80 (0x7fdf52b664d0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x65 (0x7fdf52b02f69 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1c6d44a (0x7fdf2c10444a in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x2f1d823 (0x7fdf2d3b4823 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0xc82671 (0x7fdf2b119671 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xc83340 (0x7fdf2b11a340 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xc81357 (0x7fdf2b118357 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xdc253 (0x7fdf54361253 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x94ac3 (0x7fdf5462cac3 in /lib/x86_64-linux-gnu/libc.so.6)
frame #9: clone + 0x44 (0x7fdf546bda74 in /lib/x86_64-linux-gnu/libc.so.6)

[rank7]:[E107 03:16:09.503663725 OpParamMaker.cpp:444] operator():third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-07-03:16:09 (PID:13919, Device:7, RankID:-1) ERR00100 PTA call acl api failed.
EZ9999: Inner Error!
EZ9999[PID: 13919] 2026-01-07-03:16:09.108.336 AclNN_Inner_Error(EZ9999):  Nnopbase fails to invoke the HcclAllocComResourceByTiling function of the hccl module. ret = 4, comm = 0x7f8c94e4fec0.
        TraceBack (most recent call last):
       Check nnopbase::NnopBaseHcclWrapper::GetInstance().HcclAllocComResourceByTiling(commHandle, stream, ((NnopbaseTilingData *)executor->args->tilingInfo.tilingData)->GetData(), &contextAddr) failed
       Check NnopbaseGetHcomResource(executor, stream) failed
       Check NnopbaseExecutorGetMc2Num(executor, stream, &argsAddr, &mc2Num) failed
       Check NnopbaseExecutorPrepareParamsExt(executor, stream) failed
       Check NnopbaseRunWithWorkspace(executor, stream, workspace, workspaceSize) failed

Exception raised from operator() at third_party/op-plugin/op_plugin/ops/opapi/MoeDistributeDispatchV2KernelOpApi.cpp:161 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x80 (0x7f8d60ad34d0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x65 (0x7f8d60a6ff69 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1c6d44a (0x7f8d4fc4244a in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x2f1d823 (0x7f8d50ef2823 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0xc82671 (0x7f8d4ec57671 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xc83340 (0x7f8d4ec58340 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xc81357 (0x7f8d4ec56357 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xdc253 (0x7f8d7789f253 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x94ac3 (0x7f8d77b6aac3 in /lib/x86_64-linux-gnu/libc.so.6)
frame #9: clone + 0x44 (0x7f8d77bfba74 in /lib/x86_64-linux-gnu/libc.so.6)

(Worker_TP3_EP3 pid=13839) ERROR 01-07 03:16:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_TP4_EP4 pid=13857) ERROR 01-07 03:16:09 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=13783) ERROR 01-07 03:16:21 [multiproc_executor.py:231] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
(EngineCore_DP0 pid=13783) Process EngineCore_DP0:
(EngineCore_DP0 pid=13783) Traceback (most recent call last):
(EngineCore_DP0 pid=13783)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=13783)     self.run()
(EngineCore_DP0 pid=13783)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=13783)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_balance_schedule.py", line 674, in run_engine_core
(EngineCore_DP0 pid=13783)     raise e
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_balance_schedule.py", line 661, in run_engine_core
(EngineCore_DP0 pid=13783)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=13783)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP0 pid=13783)     super().__init__(
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP0 pid=13783)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=13783)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 240, in _initialize_kv_caches
(EngineCore_DP0 pid=13783)     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=13783)                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=13783)     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=13783)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP0 pid=13783)     return aggregate(get_response())
(EngineCore_DP0 pid=13783)                      ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=13783)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP0 pid=13783)     raise RuntimeError(
(EngineCore_DP0 pid=13783) RuntimeError: Worker failed with error 'The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnMoeDistributeDispatchV3.
(EngineCore_DP0 pid=13783) Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(EngineCore_DP0 pid=13783) Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(EngineCore_DP0 pid=13783) [ERROR] 2026-01-07-03:16:09 (PID:13793, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=13783) ', please check the stack trace above for the root cause
(APIServer pid=13771) Traceback (most recent call last):
(APIServer pid=13771)   File "/usr/local/python3.11.13/bin/vllm", line 7, in <module>
(APIServer pid=13771)     sys.exit(main())
(APIServer pid=13771)              ^^^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main
(APIServer pid=13771)     args.dispatch_function(args)
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 60, in cmd
(APIServer pid=13771)     uvloop.run(run_server(args))
(APIServer pid=13771)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
(APIServer pid=13771)     return runner.run(wrapper())
(APIServer pid=13771)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=13771)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=13771)     return self._loop.run_until_complete(task)
(APIServer pid=13771)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=13771)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=13771)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=13771)     return await main
(APIServer pid=13771)            ^^^^^^^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1398, in run_server
(APIServer pid=13771)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1417, in run_server_worker
(APIServer pid=13771)     async with build_async_engine_client(
(APIServer pid=13771)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=13771)     return await anext(self.gen)
(APIServer pid=13771)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 172, in build_async_engine_client
(APIServer pid=13771)     async with build_async_engine_client_from_engine_args(
(APIServer pid=13771)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=13771)     return await anext(self.gen)
(APIServer pid=13771)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 213, in build_async_engine_client_from_engine_args
(APIServer pid=13771)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=13771)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 215, in from_vllm_config
(APIServer pid=13771)     return cls(
(APIServer pid=13771)            ^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=13771)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=13771)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 121, in make_async_mp_client
(APIServer pid=13771)     return AsyncMPClient(*client_args)
(APIServer pid=13771)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 820, in __init__
(APIServer pid=13771)     super().__init__(
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 477, in __init__
(APIServer pid=13771)     with launch_core_engines(vllm_config, executor_class, log_stats) as (
(APIServer pid=13771)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=13771)     next(self.gen)
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 903, in launch_core_engines
(APIServer pid=13771)     wait_for_engine_startup(
(APIServer pid=13771)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 960, in wait_for_engine_startup
(APIServer pid=13771)     raise RuntimeError(
(APIServer pid=13771) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=13771) [ERROR] 2026-01-07-03:16:23 (PID:13771, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

</details>

