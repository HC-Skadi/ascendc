# Issue #3289: [MISC]: qwen 3 vl init failed

## 基本信息

- **编号**: #3289
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3289
- **创建时间**: 2025-09-30T04:59:00Z
- **关闭时间**: 2025-09-30T09:33:19Z
- **更新时间**: 2025-10-01T18:18:37Z
- **提交者**: @JasonHe-WQ
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
root@qwen3-vl-ascend-55664d85cf-hj9tn:~# python ./collect.py 
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:28:35) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-89-generic-x86_64-with-glibc2.35

CPU:
Architecture:                       x86_64
CPU op-mode(s):                     32-bit, 64-bit
Address sizes:                      46 bits physical, 57 bits virtual
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          GenuineIntel
Model name:                         Intel(R) Xeon(R) Platinum 8468
CPU family:                         6
Model:                              143
Thread(s) per core:                 2
Core(s) per socket:                 48
Socket(s):                          2
Stepping:                           8
BogoMIPS:                           4200.00
Flags:                              fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                     VT-x
L1d cache:                          4.5 MiB (96 instances)
L1i cache:                          3 MiB (96 instances)
L2 cache:                           192 MiB (96 instances)
L3 cache:                           210 MiB (2 instances)
NUMA node(s):                       2
NUMA node0 CPU(s):                  0-47,96-143
NUMA node1 CPU(s):                  48-95,144-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:           Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:           Mitigation; Enhanced IBRS, IBPB conditional, RSB filling, PBRSB-eIBRS SW sequence
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1+cpu
[pip3] transformers==4.57.0.dev0
[conda] Could not collect
vLLM Version: 0.11.0rc3
vLLM Ascend Version: 0.11.0rc0

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=4,9,2,1,7,10,12,11,6,15,5,13,14,3,0,8
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.2               Version: 25.0.rc1.2.sph001                                    |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 87.1        37                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3415 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 92.5        39                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3404 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 89.7        36                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3402 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 91.7        38                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3404 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 87.3        36                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3407 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 92.2        37                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3402 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 86.0        37                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3402 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 88.6        37                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 91.2        37                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 94.0        37                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 86.6        37                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 89.1        40                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 92.3        37                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3406 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 91.4        38                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 86.2        36                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 88.6        37                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3401 / 65536         |
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
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug
when i tried to use qwen3 vl model, the engine was abnormal and failed to start
first, i encounter some errors about transformer package
```plaintext
(APIServer pid=83) INFO 09-30 04:54:52 [utils.py:233] non-default args: {'model_tag': '/mnt/hw910test-jfs/models/qwen/Qwen3-VL-235B-A22B-Instruct', 'host': '0.0.0.0', 'model': '/mnt/hw910test-jfs/models/qwen/Qwen3-VL-235B-A22B-Instruct', 'trust_remote_code': True, 'seed': 1024, 'max_model_len': 32768, 'served_model_name': ['qwen3vl'], 'tensor_parallel_size': 16, 'gpu_memory_utilization': 0.8, 'max_num_batched_tokens': 4096, 'max_num_seqs': 16}
(APIServer pid=83) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=83) Traceback (most recent call last):
(APIServer pid=83)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=83)     sys.exit(main())
(APIServer pid=83)              ^^^^^^
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=83)     args.dispatch_function(args)
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=83)     uvloop.run(run_server(args))
(APIServer pid=83)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=83)     return runner.run(wrapper())
(APIServer pid=83)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=83)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=83)     return self._loop.run_until_complete(task)
(APIServer pid=83)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=83)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=83)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=83)     return await main
(APIServer pid=83)            ^^^^^^^^^^
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=83)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=83)     async with build_async_engine_client(
(APIServer pid=83)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=83)     return await anext(self.gen)
(APIServer pid=83)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=83)     async with build_async_engine_client_from_engine_args(
(APIServer pid=83)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=83)     return await anext(self.gen)
(APIServer pid=83)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 206, in build_async_engine_client_from_engine_args
(APIServer pid=83)     vllm_config = engine_args.create_engine_config(usage_context=usage_context)
(APIServer pid=83)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1142, in create_engine_config
(APIServer pid=83)     model_config = self.create_model_config()
(APIServer pid=83)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=83)   File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 994, in create_model_config
(APIServer pid=83)     return ModelConfig(
(APIServer pid=83)            ^^^^^^^^^^^^
(APIServer pid=83)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__
(APIServer pid=83)     s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
(APIServer pid=83) pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig
(APIServer pid=83)   Value error, The checkpoint you are trying to load has model type `qwen3_vl_moe` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.
(APIServer pid=83) 
(APIServer pid=83) You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git` [type=value_error, input_value=ArgsKwargs((), {'model': ...rocessor_plugin': None}), input_type=ArgsKwargs]
(APIServer pid=83)     For further information visit https://errors.pydantic.dev/2.11/v/value_error
(APIServer pid=83) [ERROR] 2025-09-30-04:54:52 (PID:83, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

i tried to solve this by upgrading transformers package
```
pip install git+https://github.com/huggingface/transformers.git
```




and problems still occurs by using latest image `quay.io/ascend/vllm-ascend:v0.11.0rc0`


command
```plaintext
vllm serve /mnt/hw910test-jfs/models/qwen/Qwen3-VL-235B-A22B-Instruct \
--host 0.0.0.0 \
--port 8000 \
--seed 1024 \
--served-model-name qwen3vl \
--tensor-parallel-size 16 \
--max-num-seqs 16 \
--max-model-len 32768 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--gpu-memory-utilization 0.8 
```



Log
```plaintext
INFO 09-30 04:44:36 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:36 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:36 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:36 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:36 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:36 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:36 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:36 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:37 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:37 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:37 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:37 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:37 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:37 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:37 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:37 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:37 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:37 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:37 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:37 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:37 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:37 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:37 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:37 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:37 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:37 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:37 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:37 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:38 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:38 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:38 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:38 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:38 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:38 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:38 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:38 [__init__.py:207] Platform plugin ascend is activated
WARNING 09-30 04:44:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-30 04:44:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:38 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:38 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:38 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:38 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:39 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:39 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:39 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:39 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:39 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:39 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:39 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:39 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:39 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:39 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:39 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:39 [__init__.py:207] Platform plugin ascend is activated
WARNING 09-30 04:44:39 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:39 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:39 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:39 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:39 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:39 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:39 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:39 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:39 [__init__.py:207] Platform plugin ascend is activated
INFO 09-30 04:44:39 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-30 04:44:39 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-30 04:44:39 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-30 04:44:39 [__init__.py:207] Platform plugin ascend is activated
WARNING 09-30 04:44:40 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-30 04:44:40 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:40 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_d65a7ae2'), local_subscribe_addr='ipc:///tmp/e1c3190c-84f5-4da9-88c3-2a0589db6ed6', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:40 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_277afdfc'), local_subscribe_addr='ipc:///tmp/0579fa85-aff8-49e2-99db-8ed75d7d4b96', remote_subscribe_addr=None, remote_addr_ipv6=False)
WARNING 09-30 04:44:40 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:41 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_47ad725c'), local_subscribe_addr='ipc:///tmp/51c0fc07-6c56-42e4-8cde-b163a446f280', remote_subscribe_addr=None, remote_addr_ipv6=False)
WARNING 09-30 04:44:41 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:41 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_ffff0fea'), local_subscribe_addr='ipc:///tmp/e336ee0a-15fb-4a27-98b8-662cac5b070b', remote_subscribe_addr=None, remote_addr_ipv6=False)
WARNING 09-30 04:44:42 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-30 04:44:42 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:42 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_5cadeaec'), local_subscribe_addr='ipc:///tmp/fae2b8d5-6fbb-4f95-a88d-26f309747d47', remote_subscribe_addr=None, remote_addr_ipv6=False)
WARNING 09-30 04:44:42 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-30 04:44:42 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:43 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_49d4311c'), local_subscribe_addr='ipc:///tmp/0b90d437-4bbf-4a0d-98bd-ccfdb7529a7f', remote_subscribe_addr=None, remote_addr_ipv6=False)
WARNING 09-30 04:44:43 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-30 04:44:44 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-30 04:44:44 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:44 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_ba050a55'), local_subscribe_addr='ipc:///tmp/925eaea9-1801-4410-8451-ee96341640af', remote_subscribe_addr=None, remote_addr_ipv6=False)
WARNING 09-30 04:44:44 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:45 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_ede292b4'), local_subscribe_addr='ipc:///tmp/4753911d-ad73-4691-aecb-571245d91e37', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:45 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_348a0d06'), local_subscribe_addr='ipc:///tmp/c604d01a-f583-49fd-b908-1081b683eb95', remote_subscribe_addr=None, remote_addr_ipv6=False)
WARNING 09-30 04:44:45 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-30 04:44:45 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_d6cdfdd8'), local_subscribe_addr='ipc:///tmp/42a485a9-597c-4440-9a93-9a8de9943b0b', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:47 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_c3fd185b'), local_subscribe_addr='ipc:///tmp/33eb6a71-6593-46d9-9645-a221c0af13f7', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:47 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_28016637'), local_subscribe_addr='ipc:///tmp/fb100743-53a9-46f3-a022-b0833c3f2fd8', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:48 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_92963ffc'), local_subscribe_addr='ipc:///tmp/352b450f-3478-4705-99f5-bfc15c1dc4e6', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:48 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_47cb7a9a'), local_subscribe_addr='ipc:///tmp/b59c8f73-7af4-411e-a93c-37a1708d983c', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:48 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_35b66b32'), local_subscribe_addr='ipc:///tmp/d3fda1e2-f3a3-49cc-952b-b53386882630', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:48 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_6bfe109d'), local_subscribe_addr='ipc:///tmp/96d1b4e1-313b-4827-ac32-02fae09e56a6', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:49 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], buffer_handle=(15, 4194304, 6, 'psm_1098f2e4'), local_subscribe_addr='ipc:///tmp/40c79b5a-4b75-4546-9751-a7d03240fff6', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 0 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 10 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 10, EP rank 10
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 2 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 1 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 13 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 13, EP rank 13
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 3 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 4 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 4, EP rank 4
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 5 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 5, EP rank 5
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 15 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 15, EP rank 15
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 6 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 6, EP rank 6
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 7 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 7, EP rank 7
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 8 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 8, EP rank 8
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 11 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 11, EP rank 11
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 9 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 9, EP rank 9
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 12 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 12, EP rank 12
INFO 09-30 04:44:49 [parallel_state.py:1208] rank 14 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 14, EP rank 14
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 09-30 04:44:51 [multiproc_executor.py:558] Parent process exited, terminating worker
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708]     raise e from None
(EngineCore_DP0 pid=16449) ERROR 09-30 04:44:55 [core.py:708] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(EngineCore_DP0 pid=16449) Process EngineCore_DP0:
(EngineCore_DP0 pid=16449) Traceback (most recent call last):
(EngineCore_DP0 pid=16449)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=16449)     self.run()
(EngineCore_DP0 pid=16449)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=16449)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=16449)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=16449)     raise e
(EngineCore_DP0 pid=16449)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=16449)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=16449)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16449)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=16449)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=16449)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=16449)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=16449)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16449)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=16449)     self._init_executor()
(EngineCore_DP0 pid=16449)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=16449)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=16449)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16449)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=16449)     raise e from None
(EngineCore_DP0 pid=16449) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(APIServer pid=16178) Traceback (most recent call last):
(APIServer pid=16178)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=16178)     sys.exit(main())
(APIServer pid=16178)              ^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=16178)     args.dispatch_function(args)
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=16178)     uvloop.run(run_server(args))
(APIServer pid=16178)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=16178)     return runner.run(wrapper())
(APIServer pid=16178)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=16178)     return self._loop.run_until_complete(task)
(APIServer pid=16178)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=16178)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=16178)     return await main
(APIServer pid=16178)            ^^^^^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=16178)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=16178)     async with build_async_engine_client(
(APIServer pid=16178)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=16178)     return await anext(self.gen)
(APIServer pid=16178)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=16178)     async with build_async_engine_client_from_engine_args(
(APIServer pid=16178)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=16178)     return await anext(self.gen)
(APIServer pid=16178)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=16178)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=16178)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1571, in inner
(APIServer pid=16178)     return fn(*args, **kwargs)
(APIServer pid=16178)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=16178)     return cls(
(APIServer pid=16178)            ^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=16178)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=16178)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=16178)     return AsyncMPClient(*client_args)
(APIServer pid=16178)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=16178)     super().__init__(
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=16178)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=16178)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=16178)     next(self.gen)
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
(APIServer pid=16178)     wait_for_engine_startup(
(APIServer pid=16178)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
(APIServer pid=16178)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=16178) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=16178) [ERROR] 2025-09-30-04:44:57 (PID:16178, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
root@qwen3-vl-ascend-55664d85cf-hj9tn:~# /usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 60 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 3 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```

and enlarge memory to 1000 Gi may help to fix the second problem
