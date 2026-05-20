# Issue #832: [Bug]: install mindie turbo fail to start DS-W8A8

## 基本信息

- **编号**: #832
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/832
- **创建时间**: 2025-05-13T09:48:38Z
- **关闭时间**: 2025-11-12T07:43:52Z
- **更新时间**: 2025-11-12T07:43:52Z
- **提交者**: @FrankMinions
- **评论数**: 3

## 标签

bug; module:mindie-turbo

## 问题描述

### Your current environment
image: quay.io/ascend/vllm-ascend:v0.7.3
device: 2 nodes 910B1

<details>
<summary>The output of `vllm serve /opt/ml/model/infer/input --tensor-parallel-size 16 --trust-remote-code --distributed_executor_backend ray --max-model-len 32768 --enforce-eager --gpu-memory-utilization 0.9 --additional-config '{"ascend_scheduler_config": {"enable_chunked_prefill": true}}'`</summary>

```text
ERROR 05-13 09:39:22 core.py:291]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 558, in forward
ERROR 05-13 09:39:22 core.py:291]     hidden_states, residual = self.post_attention_layernorm(
ERROR 05-13 09:39:22 core.py:291]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 05-13 09:39:22 core.py:291]     return self._call_impl(*args, **kwargs)
ERROR 05-13 09:39:22 core.py:291]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 05-13 09:39:22 core.py:291]     return forward_call(*args, **kwargs)
ERROR 05-13 09:39:22 core.py:291]   File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 25, in forward
ERROR 05-13 09:39:22 core.py:291]     return self._forward_method(*args, **kwargs)
ERROR 05-13 09:39:22 core.py:291]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/quantize.py", line 62, in _rmsnorm_forward_oot
ERROR 05-13 09:39:22 core.py:291]     x, residual = func(self, x, residual)
ERROR 05-13 09:39:22 core.py:291]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/layernorm.py", line 34, in rms_norm_mki_forward_oot
ERROR 05-13 09:39:22 core.py:291]     x, _, residual = torch_npu.npu_add_rms_norm(x, residual, self.weight,
ERROR 05-13 09:39:22 core.py:291]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 05-13 09:39:22 core.py:291]     return self._op(*args, **(kwargs or {}))
ERROR 05-13 09:39:22 core.py:291] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is lccl_allreduce.
ERROR 05-13 09:39:22 core.py:291] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
ERROR 05-13 09:39:22 core.py:291] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
ERROR 05-13 09:39:22 core.py:291] [ERROR] 2025-05-13-09:39:22 (PID:1850, Device:5, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 05-13 09:39:22 core.py:291] EE1001: [PID: 1850] 2025-05-13-09:39:22.216.023 The argument is invalid.Reason: Memory async failed, src loc type=1, dst loc type=1, kind=1 is invalid!
ERROR 05-13 09:39:22 core.py:291]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
ERROR 05-13 09:39:22 core.py:291]         TraceBack (most recent call last):
ERROR 05-13 09:39:22 core.py:291]         Memory async failed, check kind and loc, retCode=0x7110001[FUNC:MemcpyAsyncCkeckLocation][FILE:api_error.cc][LINE:1793]
ERROR 05-13 09:39:22 core.py:291]         MemcpyAsync check src or dst location failed, stream_id=2.[FUNC:MemcpyAsync][FILE:api_error.cc][LINE:1504]
ERROR 05-13 09:39:22 core.py:291]         The argument is invalid.Reason: rtMemcpyAsync execute failed, reason=[invalid value]
ERROR 05-13 09:39:22 core.py:291]         [Call][Rts]call rts api [rtMemcpyAsync] failed, retCode is 107000[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 05-13 09:39:22 core.py:291] 
CRITICAL 05-13 09:39:22 core_client.py:191] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
INFO 05-13 09:39:22 ray_distributed_executor.py:104] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
```

</details>


### 🐛 Describe the bug

install mindie turbo fail to start DS-W8A8
