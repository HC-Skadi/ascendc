# Issue #5428: [Bug]: Qwen1.5-14B推理时报错

## 基本信息

- **编号**: #5428
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5428
- **创建时间**: 2025-12-27T07:47:57Z
- **关闭时间**: 2025-12-27T07:48:35Z
- **更新时间**: 2025-12-27T07:48:35Z
- **提交者**: @xieanxiean
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

Qwen1.5-14B模型A2单卡可以正常拉起，但是处理请求时报错。
模型拉起命令：
单卡部署，服务拉起命令如下：
export TASK_QUEUE_ENABLE=1
export VLLM_USE_V1=1

export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

export HCCL_OP_EXPANSION_MODE="AIV"

export VLLM_ASCEND_ENABLE_DENSE_OPTIMIZE=1

export VLLM_ASCEND_ENABLE_FLASHCOMM=1

export VLLM_ASCEND_ENABLE_PREFETCH_MLP=1

export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

export VLLM_TORCH_PROFILER_DIR="./vllm_profile_32b"
export VLLM_TORCH_PROFILER_WITH_STACK=0

python -m vllm.entrypoints.openai.api_server
--model=/app/models/Qwen/Qwen1.5-14B
--served-model-name qwen
--trust-remote-code
--max-model-len 18432
--max-num-batched-tokens 204800
-tp 8
--port 9081
--block-size 128
--distributed_executor_backend "mp"
--enable-prefix-caching
--async-scheduling
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'
--gpu-memory-utilization 0.9 \


报错信息如下：
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
