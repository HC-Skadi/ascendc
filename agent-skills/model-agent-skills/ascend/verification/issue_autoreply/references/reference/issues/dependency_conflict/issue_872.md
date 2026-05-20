# Issue #872: [Bug]: InputBatch.__init__() got an unexpected keyword argument 'max_num_blocks_per_req'

## 基本信息

- **编号**: #872
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/872
- **创建时间**: 2025-05-15T10:55:01Z
- **关闭时间**: 2025-05-16T04:14:57Z
- **更新时间**: 2025-05-16T04:14:57Z
- **提交者**: @MengqingCao
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

```bash
WARNING 05-15 10:50:27 [utils.py:2618] Methods add_lora,cache_config,determine_available_memory,determine_num_available_blocks,device_config,get_cache_block_size_bytes,list_loras,load_config,pin_lora,remove_lora,scheduler_config not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xfffd1f6a1150>
INFO 05-15 10:50:29 [parallel_state.py:1079] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
ERROR 05-15 10:50:29 [core.py:489] EngineCore failed to start.
ERROR 05-15 10:50:29 [core.py:489] Traceback (most recent call last):
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 480, in run_engine_core
ERROR 05-15 10:50:29 [core.py:489]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 379, in __init__
ERROR 05-15 10:50:29 [core.py:489]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 67, in __init__
ERROR 05-15 10:50:29 [core.py:489]     self.model_executor = executor_class(vllm_config)
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 05-15 10:50:29 [core.py:489]     self._init_executor()
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/executor/uniproc_executor.py", line 46, in _init_executor
ERROR 05-15 10:50:29 [core.py:489]     self.collective_rpc("init_device")
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 05-15 10:50:29 [core.py:489]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/utils.py", line 2552, in run_method
ERROR 05-15 10:50:29 [core.py:489]     return func(*args, **kwargs)
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-cpu/vllm/vllm/worker/worker_base.py", line 604, in init_device
ERROR 05-15 10:50:29 [core.py:489]     self.worker.init_device()  # type: ignore
ERROR 05-15 10:50:29 [core.py:489]   File "/home/cmq/code/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 114, in init_device
ERROR 05-15 10:50:29 [core.py:489]     self.model_runner = NPUModelRunner(self.vllm_config, self.device)
ERROR 05-15 10:50:29 [core.py:489]   File "/home/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 209, in __init__
ERROR 05-15 10:50:29 [core.py:489]     self.input_batch = InputBatch(
ERROR 05-15 10:50:29 [core.py:489] TypeError: InputBatch.__init__() got an unexpected keyword argument 'max_num_blocks_per_req'
```
