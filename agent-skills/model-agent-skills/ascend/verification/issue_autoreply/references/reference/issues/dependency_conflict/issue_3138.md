# Issue #3138: [Bug]:  TypeError: get_attn_backend() got multiple values for argument 'use_mla'

## 基本信息

- **编号**: #3138
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3138
- **创建时间**: 2025-09-24T01:29:46Z
- **关闭时间**: 2025-09-24T23:36:52Z
- **更新时间**: 2025-09-24T23:36:52Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/17960411062/job/51082260624

### 🐛 Describe the bug

```
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 695, in run_engine_core
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 965, in __init__
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     super().__init__(vllm_config, local_client, handshake_address,
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 54, in _init_executor
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     self.collective_rpc("init_device")
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils/__init__.py", line 3042, in run_method
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     return func(*args, **kwargs)
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/worker/worker_base.py", line 259, in init_device
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     self.worker.init_device()  # type: ignore
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 176, in init_device
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     self.model_runner = NPUModelRunner(self.vllm_config, device)
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 308, in __init__
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]     self.attn_backend = get_attn_backend(
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708]                         ^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3491) ERROR 09-23 22:24:13 [core.py:708] TypeError: get_attn_backend() got multiple values for argument 'use_mla'
```
