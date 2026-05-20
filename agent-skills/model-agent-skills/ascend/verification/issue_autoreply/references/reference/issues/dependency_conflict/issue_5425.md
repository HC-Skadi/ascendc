# Issue #5425: [Bug]: Qwen1.5-14B报错

## 基本信息

- **编号**: #5425
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5425
- **创建时间**: 2025-12-27T07:11:40Z
- **关闭时间**: 2025-12-27T07:30:14Z
- **更新时间**: 2025-12-27T07:30:14Z
- **提交者**: @xieanxiean
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>推理报错</summary>

模型可以正常拉起，但是推理时报错，报错信息如下：

0 3on Worker 1P3 1d 47155 18 om ERRUR 12-2387:48:39	mUeroc execuvor.  624  	Flle wIIn-Worksoace/ VIIm-ascend VIm ascend actencion actention V
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39 	[multiproc_executor.py:824]	output - self.forward_fused _infer_attention(^M
^[[0;36m(Worker_TP3 pid=47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc executor.py:824]	Wvvvvvvvvvvvvvvvvvwwwwwvwwvwvvwvvwvvv的
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39 	[multiproc_executor.py:824]	File “/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py”, line 537, in forward_fused_infer_atten
tion M
^[[0;36m(Worker_TP3 pid=47155)^[[0;Om ERROR 12-25 07:40:39 	[multiproc_executor.py:824]	attn_output, _	- torch_npu.npu_fused infer_attention_score(^M
[[0;36m(Worker_TP3 pid=47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc executor.py:824]	Wvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvwvvwvvwwvwve
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39 	[multiproc_executor.py:824]	File "/usr/local/python3.11.13/1ib/python3.11/site-packages/torch/_ops.py", line 1243, in
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39	^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39	[[0;36m(Worker TP3 pid=47155)^[[0;0m ERROR 12-25 07:40:39	-  , 	[multiproc_executor.py:824]	[multiproc_executor.py:824]	return self._op( args, **kwargs)^M	Wvvvvvvvvvvvvvvvvvvvyvwwwwv
ction error: call aclnnFusedInferAttentionScoreV3 failed, error code is 561002^M
^[[O;36m(Worker_TP3 pid-47155)^[[0;Om ERROR 12-25 07:40:39 [multiproc_executor.py:824] [ERROR] 2025-12-25-07:40:39 (PID:47155, Device:3, RankID:-1) ERR00100 PTA call acl api failed.^M
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc_executor.py:824] E89999: Inner Error!^M
[[0;36m(Worker_TP3 pid=47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc_executor.py:824] E89999[PID: 47155] 2025-12-25-07:48:39.874.850 (E89999): the first dim of key(4048) should not less than valid bl
ock num(4126) when PA enable[FUNC:CheckPAWhenBaseApi][FILE:prompt_flash_attention_tiling.cpp][LINE:2170]^M
[[0;36m(Worker_TP3 pid=47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc_executor.py:824]	TraceBack (most recent call last):^M
[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc_executor.py:824]	tiling process fo ifa failed[FUNC:TilingFusedInferAttentionScore][FILE:fused infer_attention_score_tiling.
Pp][LINE:1847]^M
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc_executor.py: 824]	FusedInferAttentionScore do tiling failed, ret is -1.^M
^[[0;36m(Worker TP3 pid=47155)^[[0;0m ERROR 12-25 07:40:39	[multiproc_executor.py:824]	Check NnopbaseExecutorDoTiling(executor) failed^M
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39 	[multiproc executor.py:824]	Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed^M
[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39	(multiproc executor.py:824]	Check NnopbaseExecutorMatchCache(executor) failed^Ma
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39 	[multiproc_executor.py:824]	failed^M
^[[0;36m(Worker TP3 pid-47155)^[[0;Om ERROR 12-25 07:40:39	[multiproc executor.py:824]	Wv
^[[0;36m(Worker_TP3 pid-47155)^[[0;0m ERROR 12-25 07:40:39 	(multiproc executor.py:824]	Traceback (most recent call last):^M
^[[0;36m(Worker_TP3 pid=47155)^[[0;0m ERROR 12-25 07:40:39 	[multiproc_executor.py:824]
ATTO:36m(Wonker TP3 nid-47155 A1TO:Om FRROR 12-25 07:10:39	multiomc	Jow axd	Any:8241	nntont	,m funr targs	kwanas ay

</details>


### 🐛 Describe the bug

如上，推理时报错
