# Issue #3029: [Bug]: quay.io/ascend/vllm-ascend:v0.10.2rc1 镜像 Qwen3-Next 模型推理服务启动失败

## 基本信息

- **编号**: #3029
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3029
- **创建时间**: 2025-09-19T05:02:24Z
- **关闭时间**: 2025-11-11T06:17:49Z
- **更新时间**: 2025-11-11T06:24:05Z
- **提交者**: @Zbaoli
- **评论数**: 6

## 标签

bug; qwen3-next

## 问题描述

### Your current environment

<details>
<summary>在quay.io/ascend/vllm-ascend:v0.10.2rc1 镜像内运行 `python collect_env.py` 的输出</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-89.11.v2401.ky10.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
Frequency boost:                    disabled
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
[pip3] transformers==4.56.1
[conda] Could not collect
vLLM Version: 0.10.2
vLLM Ascend Version: 0.10.2rc1

ENV Variables:
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/
ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskerne
l:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_a
bi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/asc
end-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnen
gine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/ex
amples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend
/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/o
p_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| 0     910B4-1             | OK            | 94.5        40                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 1     910B4-1             | OK            | 93.7        42                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 2     910B4-1             | OK            | 91.9        40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 3     910B4-1             | OK            | 91.6        34                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 4     910B4-1             | OK            | 98.1        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3384 / 65536         |
+===========================+===============+====================================================+
| 5     910B4-1             | OK            | 90.3        45                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 6     910B4-1             | OK            | 92.9        44                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 7     910B4-1             | OK            | 90.9        41                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3381 / 65536         |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

运行命令 vllm serve --tensor-parallel-size 8 Qwen3-Next-80B-A3B-Instruct/ 报错：
```
NFO 09-19 05:00:56 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-19 05:00:56 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-19 05:00:56 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-19 05:00:56 [__init__.py:207] Platform plugin ascend is activated
WARNING 09-19 05:00:59 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-19 05:00:59 [registry.py:483] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 09-19 05:00:59 [registry.py:483] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForC$
nditionalGeneration.
WARNING 09-19 05:00:59 [registry.py:483] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_$
_VLForConditionalGeneration.
WARNING 09-19 05:00:59 [registry.py:483] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausa$
LM.
WARNING 09-19 05:00:59 [registry.py:483] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausa$
LM.
WARNING 09-19 05:00:59 [registry.py:483] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 09-19 05:00:59 [registry.py:483] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
WARNING 09-19 05:00:59 [registry.py:483] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:Qwen3NextForCausalLM.
INFO 09-19 05:00:59 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(APIServer pid=390) INFO 09-19 05:01:00 [api_server.py:1896] vLLM API server version 0.10.2
(APIServer pid=390) INFO 09-19 05:01:00 [utils.py:328] non-default args: {'model_tag': 'Qwen3-Next-80B-A3B-Instruct/', 'model': 'Qwen3-Next-80B-A3B-Instruct/', 'tensor_parallel_size': 8}
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] Error in inspecting model architecture 'Qwen3NextForCausalLM'
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] Traceback (most recent call last):
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 867, in _run_in_subprocess
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     returned.check_returncode()
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/usr/local/python3.11.13/lib/python3.11/subprocess.py", line 502, in check_returncode
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     raise CalledProcessError(self.returncode, self.args, self.stdout,
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] subprocess.CalledProcessError: Command '['/usr/local/python3.11.13/bin/python3', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit
 status 1.
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] The above exception was the direct cause of the following exception:
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] Traceback (most recent call last):
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 447, in _try_inspect_model_cls
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     return model.inspect_model_cls()
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 418, in inspect_model_cls
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     return _run_in_subprocess(
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 870, in _run_in_subprocess
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     raise RuntimeError(f"Error raised in subprocess:\n"
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] RuntimeError: Error raised in subprocess:
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] <frozen runpy>:128: RuntimeWarning: 'vllm.model_executor.models.registry' found in sys.modules after import of package 'vllm.model_executor.models',
but prior to execution of 'vllm.model_executor.models.registry'; this may result in unpredictable behaviour
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] Traceback (most recent call last):
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 891, in <module>
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     _run()
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 884, in _run
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     result = fn()
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]              ^^^^
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 419, in <lambda>
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     lambda: _ModelInfo.from_model_cls(self.load_model_cls()))
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]                                       ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 422, in load_model_cls
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     mod = importlib.import_module(self.module_name)
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/usr/local/python3.11.13/lib/python3.11/importlib/__init__.py", line 126, in import_module
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     return _bootstrap._gcd_import(name[level:], package, level)
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 65, in <module>
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     from vllm_ascend.ops.casual_conv1d import (causal_conv1d_fn,
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/casual_conv1d.py", line 14, in <module>
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]     import triton
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449] ModuleNotFoundError: No module named 'triton'
(APIServer pid=390) ERROR 09-19 05:01:11 [registry.py:449]
(APIServer pid=390) Traceback (most recent call last):
(APIServer pid=390)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=390)     sys.exit(main())
(APIServer pid=390)              ^^^^^^
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=390)     args.dispatch_function(args)
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 50, in cmd
(APIServer pid=390)     uvloop.run(run_server(args))
(APIServer pid=390)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=390)     return runner.run(wrapper())
(APIServer pid=390)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=390)     return self._loop.run_until_complete(task)
(APIServer pid=390)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=390)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=390)     return await main
(APIServer pid=390)            ^^^^^^^^^^
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1941, in run_server
(APIServer pid=390)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1961, in run_server_worker
(APIServer pid=390)     async with build_async_engine_client(
(APIServer pid=390)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=390)     return await anext(self.gen)
(APIServer pid=390)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 179, in build_async_engine_client
(APIServer pid=390)     async with build_async_engine_client_from_engine_args(
(APIServer pid=390)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=390)     return await anext(self.gen)
(APIServer pid=390)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 205, in build_async_engine_client_from_engine_args
(APIServer pid=390)     vllm_config = engine_args.create_engine_config(usage_context=usage_context)
(APIServer pid=390)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1119, in create_engine_config
(APIServer pid=390)     model_config = self.create_model_config()
(APIServer pid=390)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=390)   File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 963, in create_model_config
(APIServer pid=390)     return ModelConfig(
(APIServer pid=390)            ^^^^^^^^^^^^
(APIServer pid=390)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__
(APIServer pid=390)     s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
(APIServer pid=390) pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig
(APIServer pid=390)   Value error, Model architectures ['Qwen3NextForCausalLM'] failed to be inspected. Please check the logs for more details. [type=value_error, input_value=ArgsKwargs((), {'model': ...roces
sor_plugin': None}), input_type=ArgsKwargs]
(APIServer pid=390)     For further information visit https://errors.pydantic.dev/2.11/v/value_error
(APIServer pid=390) [ERROR] 2025-09-19-05:01:11 (PID:390, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
