# Issue #5805: [Bug]: 使用qwen3_235B模型跑pd分离，p节点和d节点同时开启时pcp=2,p节点的tp=8,d节点的tp=2,mooncake_connector出现越界的错误

## 基本信息

- **编号**: #5805
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5805
- **创建时间**: 2026-01-12T08:45:02Z
- **关闭时间**: 2026-01-12T11:18:48Z
- **更新时间**: 2026-01-12T11:18:48Z
- **提交者**: @knight0528
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

日志
(Worker
_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824] WorkerProc hit an exception.
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 369, in execute_model
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/worker.py", line 338, in execute_model
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     output = self.model_runner.execute_model(scheduler_output,
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib64/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1355, in execute_model
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     return self.kv_connector_no_forward(scheduler_output,
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib/python3.11/site-packages/vllm/v1/worker/kv_connector_model_runner_mixin.py", line 84, in kv_connector_no_forward
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     with (
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/lib64/python3.11/contextlib.py", line 137, in __enter__
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     return next(self.gen)
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib/python3.11/site-packages/vllm/v1/worker/kv_connector_model_runner_mixin.py", line 128, in _get_kv_connector_output
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     kv_connector.start_load_kv(get_forward_context())
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/distributed/mooncake_connector.py", line 770, in start_load_kv
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     self.connector_worker.start_load_kv(self._connector_metadata)
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/distributed/mooncake_connector.py", line 1328, in start_load_kv
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     remote_handshake_port_list[pcp_dcp_rank][i],
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824]     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
(Worker_DP0_PCP1_TP1_EP3 pid=1041) ERROR 2026-01-12 16:28:02.921 [multiproc_executor.py:824] IndexError: list index out of range
