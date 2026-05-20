# Issue #1731: [Bug]: V1 LLM Engine，Qwen2.5-VL-7B-Instruct, 算子报越界错误，但V0 Engine正常

## 基本信息

- **编号**: #1731
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1731
- **创建时间**: 2025-07-10T14:04:54Z
- **关闭时间**: 2025-07-11T15:58:34Z
- **更新时间**: 2025-07-11T15:58:34Z
- **提交者**: @hyena126
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text

```
</details>


### 🐛 Describe the bug

INFO 07-03 05:08:53 [async 1lm.py:271] Added requeest chatcmpl-8ba6ึ68fffcff4f3cb46a2ef9a78b5755
DumpHead: AIV-39, CoreType=AIV, block dim=40, total block num=40,_block_remain_len=640,_block_initia1_space=1024,_rsv=0._magic=5aa5bccd
[ASSERT] [CANN VERSION : 8.1.RC1][TimeStamp : 0] /hoSme/slavel/Ascend/8.1.RC1/opp/built-in/op impl/ai core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3base.h:137: Assertion`((
al && val < this->gxSize )' Index 596 out of raange [0 596) !
[rank0]:[W703 05:08:55.758707244 compiler depend.ts:188] Warning: EZ9999: Inner Error!
EZ9999: [PID:111457] 2025-07-03-05:08:53.788.426 The error from device(chipId:0, dieId:0), serial numbper is 1, there is an aivec error exception, core idis 2, error code = 0, du
fo: pc start: 0x12c0c3058f34, current: 0x12c0c30597558, vec error info: 0xa113b4fb10, mte error info: 0xx9bf9d0313c, ifu error info: 0x4b31a02fb5080, ccu error info: 0x684bbf52119f(
cube error info: 0, biu error info: 0, aic error massk: 0x6500020bd00028c, para base: 0x12c10042a800.[FUJNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc] [LINE:1434]
TraceBack (most recent call last):
The extend info: errcode:(0, 0, 0, 0) errorStr: timeouut or trap error. fixp error0 info: 0x9d0313c, fixperrorl info: 0x9b, fsmId:0, tslot:0, thread:0, ctxid:0, blk:39, sublk:
bErrType:2. [FUNC:ProcessStarsCoreErrorInfo] [FILE:device error_proc.cc] [LINE:144Gิ]
Kernel task happen error, retCode=0x31, [vector Core exoception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_taskCC] [LINE:1366]
AIV Kernel happen error, retCode=0x31.[FUNC:GetError][FILE:stream.cc] [LINE:1119]
Aicore kernel execute failed, device_id=0, stream_id=1921,report_stream_id=1921, task_id=8362, flip_num=747, fault kernel_name=GatherV3_7869a97190b9b4d296d9414a005b954b_hi
rformance_80330, fault kernel info ext=none, program id=341, hash=1766911350155126969.[FUNC:GetError][FILE:stream.cc] [LINE:1119]
[AIC INFO] after execute:args print end[FUNC:GetErreor] [FILE:stream.cc] [LINE:1119]
rtstreamSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc] [LINE:53]
synchronize stream failed, runtime result = 507035[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(function recordEvent)
ERROR 07-03 05:08:55 [dump input.py:69] Dumping input data
ERROR 07-03 05:08:55 [dump input.py:71] V1 LLM engine (v0.9.1) with config: model='/data/workfolder/Qwen/qwen255_vl-7b-', speculative config-Nonewstokenizer', skip tokenizer init=False, tokenizer_mode=auto, revision=None,_override neuron config={}, tokenizeE revision-None, trust
te_code=False, dtype=torch.bfloat16, max_seq_len=16384,download_dir=None, load_format=auto, tensor_parallel_sizze=1, pipeline_parallel_size=1, disable_custs #
