# Issue #5661: [Bug]: 高频出现 RuntimeError: ACL stream synchronize failed, error code:507015 问题

## 基本信息

- **编号**: #5661
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5661
- **创建时间**: 2026-01-06T12:09:00Z
- **关闭时间**: 2026-01-07T03:16:42Z
- **更新时间**: 2026-01-19T06:25:18Z
- **提交者**: @chenaoxuan
- **评论数**: 9

## 标签

bug

## 问题描述

### Your current environment

vllm：v0.13.0 commit：72506c98349d6bcd32b4e33eec7b5513453c1502
vllm-ascend：e07938047e4b117258f8cb564a41c472d2b6e4ab
triton-ascend：3.2.0.dev20260105
CANNVERSION=CANN 8.5.0.B100
PTAVERSION=FrameworkPTAdapter 7.2.RC1.B130

推理参数：temperature = 0.6,   top_p = 0.95

### 🐛 Describe the bug

推理一段时间后报错，高频出现（使用triton下频率稍低，非triton下高频出现）：
[rank9]:[W106 19:37:15.186470670 compiler_depend.ts:57] Warning: EZ9999: Inner Error!
EZ9999[PID: 244584] 2026-01-06-19:37:15.407.487 (EZ9999):  The error from device(chipId:4, dieId:1), serial number is 91, there is an exception of fftsplus aivector error, core id is 40, error code = 0, dump info: pc start: 0x1252009f31b4, current: 0x1252009f3574, vec error info: 0xce00000886, mte error info: 0x8f030001da, ifu error info: 0x1202cf8839dc0, ccu error info: 0xdb797c23da535c3, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c241b7b080.[FUNC:PrintCoreInfo][FILE:device_error_core_proc.cc][LINE:347]
        TraceBack (most recent call last):
       The extend info: errcode:(0, 0x1000, 0) errorStr: VEC supports illegal configurations in commands. fixp_error0 info: 0x30001da, fixp_error1 info: 0x8f, fsmId:1, tslot:3, thread:0, ctxid:0, blk:28, sublk:0, subErrType:4.[FUNC:PrintCoreInfo][FILE:device_error_core_proc.cc][LINE:360]
       Kernel task happen error, retCode=0x26, [aicore exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1493]
       rtStreamSynchronize execute failed, reason=[aicore exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 507015[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:148]
 (function copy_between_host_and_device_opapi)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824] WorkerProc hit an exception.
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824] Traceback (most recent call last):
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     output = func(*args, **kwargs)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     return func(*args, **kwargs)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm-ascend/vllm_ascend/worker/worker.py", line 354, in sample_tokens
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     return self.model_runner.sample_tokens(grammar_output)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     return func(*args, **kwargs)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1673, in sample_tokens
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     ) = self._bookkeeping_sync(
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1814, in _bookkeeping_sync
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     valid_sampled_token_ids, cu_num_tokens = RejectionSampler.parse_output(
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm/vllm/v1/sample/rejection_sampler.py", line 223, in parse_output
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     output_token_ids_np = output_token_ids.cpu().numpy()
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]                           ^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824] RuntimeError: ACL stream synchronize failed, error code:507015
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824] Traceback (most recent call last):
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     output = func(*args, **kwargs)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     return func(*args, **kwargs)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm-ascend/vllm_ascend/worker/worker.py", line 354, in sample_tokens
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     return self.model_runner.sample_tokens(grammar_output)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     return func(*args, **kwargs)
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1673, in sample_tokens
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     ) = self._bookkeeping_sync(
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1814, in _bookkeeping_sync
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     valid_sampled_token_ids, cu_num_tokens = RejectionSampler.parse_output(
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]   File "/home/c00943444/latest/vllm/vllm/v1/sample/rejection_sampler.py", line 223, in parse_output
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]     output_token_ids_np = output_token_ids.cpu().numpy()
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824]                           ^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:824] RuntimeError: ACL stream synchronize failed, error code:507015
[0;36m(Worker_DP1_TP1_EP9 pid=244584)[0;0m ERROR 01-06 19:37:15 [multiproc_executor.py:8

