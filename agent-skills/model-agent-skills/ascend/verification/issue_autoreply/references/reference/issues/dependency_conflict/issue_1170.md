# Issue #1170: [Bug]:DP Crash, After first request, process is crash, 'DPEngineCoreProc' object has no attribute 'dp_rank'

## 基本信息

- **编号**: #1170
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1170
- **创建时间**: 2025-06-11T07:22:19Z
- **关闭时间**: 2025-06-16T15:09:54Z
- **更新时间**: 2025-06-16T15:09:54Z
- **提交者**: @david6666666
- **评论数**: 1

## 标签

bug; module:dp

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>



### 🐛 Describe the bug

vllm tag v0.9.1  
vllm-ascend main 7bdc606677705d072c1dc45f050a3c3471d6d379 

vllm serve DeepSeek-V2-Lite --trust-remote-code --max-model-len=4096 --gpu-memory-utilization=0.95 --data-parallel-size 2 --data-parallel-size-local 2 --block_size 128 --enforce-eager

vllm commit：https://github.com/vllm-project/vllm/pull/18502
#940 is not correct 

After first request, process is crash . Error:
```
....INFO:     127.0.0.1:51658 - "POST /v1/completions HTTP/1.1" 200 OK
INFO 06-11 11:46:37 [loggers.py:118] Engine 000: Avg prompt throughput: 1.9 tokens/s, Avg generation throughput: 10.3 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 06-11 11:46:37 [loggers.py:118] Engine 001: Avg prompt throughput: 1.5 tokens/s, Avg generation throughput: 10.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(EngineCore_0 pid=2651) ERROR 06-11 11:46:39 [core.py:517] EngineCore encountered a fatal error.
(EngineCore_0 pid=2651) ERROR 06-11 11:46:39 [core.py:517] Traceback (most recent call last):
(EngineCore_0 pid=2651) ERROR 06-11 11:46:39 [core.py:517]   File "/home/dsv3/project/opensource/vllm/vllm/v1/engine/core.py", line 508, in run_engine_core
(EngineCore_1 pid=2655) ERROR 06-11 11:46:39 [core.py:517] EngineCore encountered a fatal error.
(EngineCore_0 pid=2651) ERROR 06-11 11:46:39 [core.py:517]     engine_core.run_busy_loop()
(EngineCore_1 pid=2655) ERROR 06-11 11:46:39 [core.py:517] Traceback (most recent call last):
(EngineCore_0 pid=2651) ERROR 06-11 11:46:39 [core.py:517]   File "/home/dsv3/project/opensource/vllm/vllm/v1/engine/core.py", line 876, in run_busy_loop
(EngineCore_1 pid=2655) ERROR 06-11 11:46:39 [core.py:517]   File "/home/dsv3/project/opensource/vllm/vllm/v1/engine/core.py", line 508, in run_engine_core
(EngineCore_0 pid=2651) ERROR 06-11 11:46:39 [core.py:517]     if self.dp_rank == 0:
(EngineCore_1 pid=2655) ERROR 06-11 11:46:39 [core.py:517]     engine_core.run_busy_loop()
(EngineCore_0 pid=2651) ERROR 06-11 11:46:39 [core.py:517] AttributeError: 'DPEngineCoreProc' object has no attribute 'dp_rank'
(EngineCore_1 pid=2655) ERROR 06-11 11:46:39 [core.py:517]   File "/home/dsv3/project/opensource/vllm/vllm/v1/engine/core.py", line 876, in run_busy_loop
(EngineCore_1 pid=2655) ERROR 06-11 11:46:39 [core.py:517]     if self.dp_rank == 0:
(EngineCore_1 pid=2655) ERROR 06-11 11:46:39 [core.py:517] AttributeError: 'DPEngineCoreProc' object has no attribute 'dp_rank'
ERROR 06-11 11:46:39 [async_llm.py:420] AsyncLLM output_handler failed.
ERROR 06-11 11:46:39 [async_llm.py:420] Traceback (most recent call last):
ERROR 06-11 11:46:39 [async_llm.py:420]   File "/home/dsv3/project/opensource/vllm/vllm/v1/engine/async_llm.py", line 379, in output_handler
ERROR 06-11 11:46:39 [async_llm.py:420]     outputs = await engine_core.get_output_async()
ERROR 06-11 11:46:39 [async_llm.py:420]   File "/home/dsv3/project/opensource/vllm/vllm/v1/engine/core_client.py", line 790, in get_output_async
ERROR 06-11 11:46:39 [async_llm.py:420]     raise self._format_exception(outputs) from None
ERROR 06-11 11:46:39 [async_llm.py:420] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
INFO 06-11 11:46:39 [launcher.py:80] Shutting down FastAPI HTTP server.
/usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
INFO 06-11 11:46:40 [coordinator.py:128] DP Coordinator process exiting
/usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```
