# Issue #778: [Bug]: Wrong output tensor shape when running DeepSeek model with V1 engine

## 基本信息

- **编号**: #778
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/778
- **创建时间**: 2025-05-07T08:34:49Z
- **关闭时间**: 2025-08-28T15:26:43Z
- **更新时间**: 2025-08-28T15:26:43Z
- **提交者**: @yiz-liu
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

The environment is unrelated to this issue; therefore, including environment logs is unnecessary.

### 🐛 Describe the bug

</details>
The following error is encountered when running the DeepSeek model:

```
ERROR 05-07 16:27:13 [core.py:402] EngineCore encountered a fatal error.
ERROR 05-07 16:27:13 [core.py:402] Traceback (most recent call last):
ERROR 05-07 16:27:13 [core.py:402]   File "workspace/vllm/vllm/v1/engine/core.py", line 393, in run_engine_core
ERROR 05-07 16:27:13 [core.py:402]     engine_core.run_busy_loop()
ERROR 05-07 16:27:13 [core.py:402]   File "workspace/vllm/vllm/v1/engine/core.py", line 417, in run_busy_loop
ERROR 05-07 16:27:13 [core.py:402]     self._process_engine_step()
ERROR 05-07 16:27:13 [core.py:402]   File "workspace/vllm/vllm/v1/engine/core.py", line 442, in _process_engine_step
ERROR 05-07 16:27:13 [core.py:402]     outputs = self.step_fn()
ERROR 05-07 16:27:13 [core.py:402]               ^^^^^^^^^^^^^^
ERROR 05-07 16:27:13 [core.py:402]   File "workspace/vllm/vllm/v1/engine/core.py", line 205, in step
ERROR 05-07 16:27:13 [core.py:402]     output = self.model_executor.execute_model(scheduler_output)
ERROR 05-07 16:27:13 [core.py:402]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 05-07 16:27:13 [core.py:402]   File "workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 158, in execute_model
ERROR 05-07 16:27:13 [core.py:402]     (output, ) = self.collective_rpc("execute_model",
ERROR 05-07 16:27:13 [core.py:402]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 05-07 16:27:13 [core.py:402]   File "workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 215, in collective_rpc
ERROR 05-07 16:27:13 [core.py:402]     result = get_response(w, dequeue_timeout)
ERROR 05-07 16:27:13 [core.py:402]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 05-07 16:27:13 [core.py:402]   File "workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 202, in get_response
ERROR 05-07 16:27:13 [core.py:402]     raise RuntimeError(
ERROR 05-07 16:27:13 [core.py:402] RuntimeError: Worker failed with error 'call aclnnInplaceCopy failed, detail:EZ1001: [PID: 1123276] 2025-05-07-16:27:13.714.340 128 and 2048 cannot broadcast.
ERROR 05-07 16:27:13 [core.py:402]         TraceBack (most recent call last):
ERROR 05-07 16:27:13 [core.py:402]         the size of tensor self [17,2048] must match the size of tensor src [17,16,128].
```
