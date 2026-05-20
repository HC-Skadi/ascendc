# Issue #5005: [Bug]: 'GDNAttentionMetadataBuilder' object has no attribute 'aclgraph_support'

## 基本信息

- **编号**: #5005
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5005
- **创建时间**: 2025-12-15T01:47:02Z
- **关闭时间**: 2025-12-15T14:32:44Z
- **更新时间**: 2026-01-20T01:22:49Z
- **提交者**: @RyanOvO
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

**_ENV:_** 
```
vllm-ascend version: 0.11.0rc3
LLM version: Qwen3-Next-80B-A3B-Instruct
Ascend version: 910B4

```

**_deploy shell:_** 
```

ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
vllm serve /home/developer/Qwen3-Next-80B-A3B-Instruct \
  --served-model-name ipt-model\
  --port 1030 \
  --tensor-parallel-size 8 \
  --max-model-len 10240 \
  --gpu-memory-utilization 0.7

```


**_Error：_**
```

(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58] EngineCore failed to start.
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58] Traceback (most recent call last):
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm_ascend/patch/platform/patch_core.py", line 49, in run_engine_core
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/executor/abstract.py", line 75, in initialize_from_config
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]     self.collective_rpc("compile_or_warm_up_model")
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58]     raise RuntimeError(
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:45 [patch_core.py:58] RuntimeError: Worker failed with error ''GDNAttentionMetadataBuilder' object has no attribute 'aclgraph_support'', please check the stack trace above for the root cause
(EngineCore_DP0 pid=290084) ERROR 12-14 12:10:55 [multiproc_executor.py:154] Worker proc VllmWorker-7 died unexpectedly, shutting down executor.
(EngineCore_DP0 pid=290084) Process EngineCore_DP0:
(EngineCore_DP0 pid=290084) Traceback (most recent call last):
(EngineCore_DP0 pid=290084)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=290084)     self.run()
(EngineCore_DP0 pid=290084)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=290084)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm_ascend/patch/platform/patch_core.py", line 62, in run_engine_core
(EngineCore_DP0 pid=290084)     raise e
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm_ascend/patch/platform/patch_core.py", line 49, in run_engine_core
(EngineCore_DP0 pid=290084)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=290084)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=290084)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=290084)     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
(EngineCore_DP0 pid=290084)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/executor/abstract.py", line 75, in initialize_from_config
(EngineCore_DP0 pid=290084)     self.collective_rpc("compile_or_warm_up_model")
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=290084)     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=290084)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=290084)   File "/home/developer/vllm-ascend-0.11.0rc3-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=290084)     raise RuntimeError(
(EngineCore_DP0 pid=290084) RuntimeError: Worker failed with error ''GDNAttentionMetadataBuilder' object has no attribute 'aclgraph_support'', please check the stack trace above for the root cause

```


### 🐛 Describe the bug

Above.
