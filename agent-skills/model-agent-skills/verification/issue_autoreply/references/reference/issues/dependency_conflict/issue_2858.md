# Issue #2858: [Bug]: 0.10.1rc1双机部署Qwen3-235B-A22B报错call aclnnMoeDistributeDispatchV2 failed, error code is 561002

## 基本信息

- **编号**: #2858
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2858
- **创建时间**: 2025-09-10T10:22:15Z
- **关闭时间**: 2025-10-15T02:39:45Z
- **更新时间**: 2025-11-05T10:00:05Z
- **提交者**: @wing2791
- **评论数**: 13

## 标签

bug; critical

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
0.10.1rc1官方镜像
```

</details>


### 🐛 Describe the bug

File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in _ca
(V11mWorker TP0 pid=973) ERROR 09-10 09:46:59 [[multiproc_executor.py:596](https://github.com/vllm-project/vllm-ascend/V1lmWorker%20TP0%20pid=973)](V1lmWorker TP0 pid=973) ERROR 09-10 09:46:59 [multiproc_executor.py:596]return self._op(*args, **(kwargs or {))
28 NPu function error: call aclnnMoeDistributeDispatchV2 failed, error code is 561002(V1lmWorker TP0 pid=973) ERROR 09-10 09:46:59 [multiproc_executor.py:596] RuntimeError: npu_moe_distribute_dispatch_v2:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:1
(V11mWorker TP0 pid=973) ERROR 09-10 09:46:59 [multiproc_executor.py:596] [ERROR] 2025-09-10-09:46:59 (PID:973, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(v1lmWorker TP0 pid=973)EERROR 09-10 09:46:599 [multiproc_executor.py:596]EZ9999: Inner Error!
2CheckShapeAndSetTiling][FILE:moe_distribute_dispatch_tiling.cc][[LINE:642](https://github.com/vllm-project/vllm-ascend/V1lmWorker%20TP0%20pid=973)](V1lmWorker TP0 pid=973) ERROR 09-10 09:46:59 [multiproc_executor.Py:596] EZ9999: [PID: 973] 2025-09-10-09:46:59.220.179 batchsize is invalid.[FUNC:MoeDistributeDispatchA
(V11mWorker TP0 pid=973) ERROR 09-10 09:46:59 [multiproc_executor.py:596]TraceBack (most recent call last):
DistributeDispatchA2TilingFuncImpl][FILE:moe_distribute_dispatch_tiling.cc][[LINE:729](https://github.com/vllm-project/vllm-ascend/V11mWorker%20TP0%20pid=973)](V11mWorker TP0 pid=973) ERROR 09-10 09:46:599 [multiproc_executor.py:596]op[MoeDistributeDispatch], MoeDistributeDispatchA2 CheckShapeAndSetTiling Failed[FUNC:Moe
(V11mWorker TP0 pid=973) ERROR 09-10 09:46:59 [[multiproc_executor.py:596](https://github.com/vllm-project/vllm-ascend/V11mWorker%20TP0%20pid=973)](V11mWorker TP0 pid=973) ERROR 09-10 09:46:59 [multiproc_executor.py:596]MoeDistributeDispatch do tiling failed, ret is -1.
Check NnopbaseExecutorDoTiling(executor) failed
(V1lmWorkerTP0pid=973）ERR0R09-1009:46:59
