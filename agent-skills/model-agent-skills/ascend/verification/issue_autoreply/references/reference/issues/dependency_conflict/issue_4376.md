# Issue #4376: [Bug]: verl train error

## 基本信息

- **编号**: #4376
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4376
- **创建时间**: 2025-11-24T04:02:17Z
- **关闭时间**: 2026-01-07T01:55:02Z
- **更新时间**: 2026-01-07T01:55:02Z
- **提交者**: @shaojun0
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```shell
root@3779acaafa1a:/vllm-workspace/vllm-ascend# python collect_env.py
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.oe2203.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 5250
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
Stepping:                        0x1
Frequency boost:                 disabled
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
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
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.0.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchdata==0.11.0
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc1.dev144+g6975d4662 (git sha: 6975d4662)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETU P_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
VLLM_HOST_IP=10.48.205.240
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
| 0     910B3               | OK            | 98.4        37                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3394 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 89.3        35                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 89.4        36                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 95.8        38                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 94.1        41                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3399 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 90.3        41                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3399 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 94.8        43                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 93.1        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3400 / 65536         |
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

```shell
(WorkerDict pid=51553) ERROR 11-24 03:44:07 [dump_input.py:76]        dtype=torch.bfloat16), field=MultiModalFlatField(slices=[(slice(0, tensor(96), None),)], dim=0)), 'image_grid_thw': MultiModalFieldElem(modality='image', key='image_grid_thw', data=tensor([ 1, 12,  8]), field=MultiModalBatchedField())}, modality='image', identifier='fb5b2b5e08928df0ca4588b576be1f87aa7936912a60debff735da6ab9f1bab6', mm_position=PlaceholderRange(offset=15, length=24, is_embed=None))],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=512, min_tokens=0, logprobs=0, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None),block_ids=([32],),num_computed_tokens=0,lora_request=None,prompt_embeds_shape=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={22: 50, 9: 50, 4: 50, 14: 50, 12: 50, 7: 50, 2: 50, 0: 50, 16: 50, 24: 50, 20: 50, 6: 50, 5: 50, 23: 50, 10: 50, 28: 50, 11: 50, 18: 50, 15: 50, 31: 50, 3: 50, 21: 50, 27: 50, 1: 50, 26: 50, 29: 50, 8: 50, 17: 50, 30: 50, 19: 50, 13: 50, 25: 50}, total_num_scheduled_tokens=1600, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={16: [0], 10: [0], 5: [0], 21: [0], 30: [0], 9: [0], 28: [0], 13: [0], 19: [0], 14: [0], 17: [0], 26: [0], 23: [0], 6: [0], 20: [0], 24: [0], 27: [0], 25: [0], 18: [0], 15: [0], 2: [0], 0: [0], 1: [0], 11: [0], 29: [0], 12: [0], 4: [0], 3: [0], 22: [0], 31: [0], 7: [0], 8: [0]}, num_common_prefix_blocks=[0], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
Error executing job with overrides: []
Traceback (most recent call last):
  File "/data/pyproject/icig-ai/cv/main_ppo.py", line 439, in <module>
    main()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/main.py", line 94, in decorated_main
    _run_hydra(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/_internal/utils.py", line 394, in _run_hydra
    _run_app(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/_internal/utils.py", line 457, in _run_app
    run_and_report(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/_internal/utils.py", line 223, in run_and_report
    raise ex
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/_internal/utils.py", line 220, in run_and_report
    return func()
           ^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/_internal/utils.py", line 458, in <lambda>
    lambda: hydra.run(
            ^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.1 1/site-packages/hydra/_internal/hydra.py", line 132, in run
    _ = ret.return_value
        ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/core/utils.py", line 260, in return_value
    raise self._return_value
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/hydra/core/utils.py", line 186, in run_job
    ret.return_value = task_function(task_cfg)
                       ^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/pyproject/icig-ai/cv/main_ppo.py", line 42, in main
    run_ppo(config)
  File "/data/pyproject/icig-ai/cv/main_ppo.py", line 96, in run_ppo
    ray.get(runner.run.remote(config))
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/worker.py", line 2962, in get
    values, debugger_breakpoint = worker.get_objects(
                                  ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/worker.py", line 1026, in get_objects
    raise value.as_instanceof_cause()
ray.exceptions.RayTaskError(RuntimeError): ray::TaskRunner.run() (pid=41818, ip=172.17.0.3, actor_id=42313d77e8fc88e7ae3a1ec201000000, repr=<main_ppo.TaskRunner object at 0xffff80127ad0>)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/pyproject/icig-ai/cv/main_ppo.py", line 341, in run
    trainer.fit()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/trainer/ppo/ray_trainer.py", line 982, in fit
    val_metrics = self._validate()
                  ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/trainer/ppo/ray_trainer.py", line 589, in _validate
    test_output_gen_batch_padded = self.actor_rollout_wg.generate_sequences(test_gen_batch_padded)
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/single_controller/ray/base.py", line 48, in __call__
    output = ray.get(output)
             ^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^^^
                                  ^^^^^^^^^^^^^^^^^^^
ray.exceptions.RayTaskError(RuntimeError): ray::WorkerDict.actor_rollout_generate_sequences() (pid=51554, ip=172.17.0.3, actor_id=b4e92352defdbb56437d82cf01000000, repr=<verl.single_controller.ray.base.WorkerDict object at 0xffcfab5d0810>)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/single_controller/ray/base.py", line 700, in func
    return getattr(self.worker_dict[key], name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/single_controller/base/decorator.py", line 442, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/utils/transferqueue_utils.py", line 199, in dummy_inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/utils/profiler/profile.py", line 256, in wrapper
    return func(self_instance, *args, **kwargs_inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/workers/fsdp_workers.py", line 930, in generate_sequences
    output = self.rollout.generate_sequences(prompts=prompts)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/utils/profiler/performance.py", line 105, in f
    return self.log(decorated_function, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/utils/profiler/performance.py", line 118, in log
    output = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/verl/workers/rollout/vllm_rollout/vllm_rollout_spmd.py", line 383, in generate_sequences
    outputs = self.inference_engine.generate(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/llm.py", line 401, in generate
    outputs = self._run_engine(use_tqdm=use_tqdm)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/llm.py", line 1600, in _run_engine
    step_outputs = self.llm_engine.step()
                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/llm_engine.py", line 265, in step
    outputs = self.engine_core.get_output()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 248, in get_output
    outputs, _ = self.engine_core.step_fn()
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 284, in step
    model_output = self.execute_model_with_error_logging(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 270, in execute_model_with_error_logging
    raise err
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 261, in execute_model_with_error_logging
    return model_fn(scheduler_output)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 103, in execute_model
    output = self.collective_rpc("execute_model",
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
    return [run_method(self.driver_worker, method, args, kwargs)]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3122, in run_method
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 270, in execute_model
    output = self.model_runner.execute_model(scheduler_output,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2082, in execute_model
    logprobs_lists = logprobs_tensors.tolists() \
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/outputs.py", line 43, in tolists
    self.logprob_token_ids.tolist(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: ACL stream synchronize failed, error code:507035
```
