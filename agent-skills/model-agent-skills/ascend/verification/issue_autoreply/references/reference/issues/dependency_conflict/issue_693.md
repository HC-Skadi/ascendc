# Issue #693: [Bug]: rope bug when running llama4 warm up

## 基本信息

- **编号**: #693
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/693
- **创建时间**: 2025-04-28T03:18:59Z
- **关闭时间**: 2025-05-16T02:19:23Z
- **更新时间**: 2025-05-16T02:19:24Z
- **提交者**: @Eviannn
- **评论数**: 3

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

When running llama4，torch_npu._npu_rotary_embedding ops would fail during warm up phase.

However, use RotaryEmbedding.forward_native instead can work.

To replicate the problem, the server start up command is : 

python -m vllm.entrypoints.openai.api_server --model path/to/Llama-4-Scout-17B-16EInstruct/ --max-num-seqs=256 --max-model-len=8192 --tensor-parallel-size=8 --block-size=128 --host=0.0.0.0 --port=8080 --gpu-memory-utilization=0.95 --trust-remote-code --dtype=bfloat16 --enforce-eager

And the error is as below:


(VllmWorkerProcess pid=326598) INFO 04-27 17:00:28 [loader.py:458] Loading weights took 150.17 seconds
(VllmWorkerProcess pid=326598) INFO 04-27 17:00:29 [model_runner.py:949] Loading model weights took 27.8083 GB
(VllmWorkerProcess pid=326602) INFO 04-27 17:00:31 [loader.py:458] Loading weights took 153.66 seconds
(VllmWorkerProcess pid=326602) INFO 04-27 17:00:32 [model_runner.py:949] Loading model weights took 27.8083 GB
(VllmWorkerProcess pid=326599) INFO 04-27 17:00:51 [loader.py:458] Loading weights took 173.39 seconds
(VllmWorkerProcess pid=326599) INFO 04-27 17:00:52 [model_runner.py:949] Loading model weights took 27.8083 GB
(VllmWorkerProcess pid=326600) INFO 04-27 17:00:54 [loader.py:458] Loading weights took 175.99 seconds
(VllmWorkerProcess pid=326600) INFO 04-27 17:00:54 [model_runner.py:949] Loading model weights took 27.8083 GB
INFO 04-27 17:00:56 [loader.py:458] Loading weights took 177.93 seconds
INFO 04-27 17:00:57 [model_runner.py:949] Loading model weights took 27.8083 GB
(VllmWorkerProcess pid=326601) INFO 04-27 17:01:07 [loader.py:458] Loading weights took 189.42 seconds
(VllmWorkerProcess pid=326596) INFO 04-27 17:01:08 [loader.py:458] Loading weights took 189.98 seconds
(VllmWorkerProcess pid=326596) INFO 04-27 17:01:08 [model_runner.py:949] Loading model weights took 27.8083 GB
(VllmWorkerProcess pid=326601) INFO 04-27 17:01:08 [model_runner.py:949] Loading model weights took 27.8083 GB
(VllmWorkerProcess pid=326597) INFO 04-27 17:01:09 [loader.py:458] Loading weights took 191.11 seconds
(VllmWorkerProcess pid=326597) INFO 04-27 17:01:09 [model_runner.py:949] Loading model weights took 27.8083 GB
[rank5]:[W427 17:10:59.487294155 compiler_depend.ts:57] Warning: EZ9999: Inner Error!
EZ9999: [PID: 326600] 2025-04-27-17:10:32.990.354 The error from device(chipId:5, dieId:0), serial number is 3, there is an aivec                                                                                                                                                                 error exception, core id is 30, error code = 0, dump info: pc start: 0x124063be7000, current: 0x124063be7b58, vec error info: 0xad                                                                                                                                                                029b923f, mte error info: 0x96cf23a0d5, ifu error info: 0x4bdb6468a8800, ccu error info: 0xdfda04d1e4030f9, cube error info: 0, bi                                                                                                                                                                u error info: 0, aic error mask: 0x6500020bd000288, para base: 0x12410049b800.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_p                                                                                                                                                                roc.cc][LINE:1417]
        TraceBack (most recent call last):
       The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0xf23a0d5, fixp_error1 info: 0x96 fsm                                                                                                                                                                Id:0, tslot:0, thread:0, ctxid:0, blk:0, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:14                                                                                                                                                                29]
       Kernel task happen error, retCode=0x30, [vector core timeout].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1356                                                                                                                                                                ]
       AIV Kernel happen error, retCode=0x30.[FUNC:GetError][FILE:stream.cc][LINE:1124]
       Aicore kernel execute failed, device_id=5, stream_id=2, report_stream_id=2, task_id=2670, flip_num=0, fault kernel_name=Rep                                                                                                                                                                eatInterleave_c956995141babe6b46a07ca335faa2f6_high_performance__kernel0, fault kernel info ext=RepeatInterleave_c956995141babe6b4                                                                                                                                                                6a07ca335faa2f6_high_performance__kernel0, program id=74, hash=9349972608734966759.[FUNC:GetError][FILE:stream.cc][LINE:1124]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1124]
       rtStreamSynchronize execute failed, reason=[vector core timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:5                                                                                                                                                                3]
       synchronize stream failed, runtime result = 507034[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
 (function copy_between_host_and_device_opapi)

