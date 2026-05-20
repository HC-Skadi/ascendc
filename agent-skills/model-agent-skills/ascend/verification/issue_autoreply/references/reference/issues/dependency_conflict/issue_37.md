# Issue #37: Support 310 series

## 基本信息

- **编号**: #37
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/37
- **创建时间**: 2025-02-11T07:22:01Z
- **关闭时间**: 2025-07-12T17:13:43Z
- **更新时间**: 2025-07-12T17:13:43Z
- **提交者**: @niejingwei
- **评论数**: 4

## 标签

feature request

## 问题描述

```
.[2025-2-11 3:31:59] [WARNING] [ascend310p] te_rmsnorm_646750ff8f1f95942648e3ac22e8da92b00f3bba6f0542271074f58a2f021cb3 not found cann_version.h
......ERROR 02-11 11:32:58 engine.py:389] call aclnnPromptFlashAttentionV3 failed, detail:EZ1001: [PID: 312378] 2025-02-11-11:32:58.201.638 PromptFlashAttention LaunchAicore failed.
ERROR 02-11 11:32:58 engine.py:389]         TraceBack (most recent call last):
ERROR 02-11 11:32:58 engine.py:389]         Cannot find bin of op PromptFlashAttention, integral key 0/1/|bf16/ND/bf16/ND/bf16/ND/bf16/ND/.
ERROR 02-11 11:32:58 engine.py:389]         Cannot find binary for op PromptFlashAttention.
ERROR 02-11 11:32:58 engine.py:389]         Kernel GetWorkspace failed. opType: 5
ERROR 02-11 11:32:58 engine.py:389]         PromptFlashAttention LaunchAicore failed.
ERROR 02-11 11:32:58 engine.py:389]
ERROR 02-11 11:32:58 engine.py:389] [ERROR] 2025-02-11-11:32:58 (PID:312378, Device:0, RankID:-1) ERR01100 OPS call acl api failed
ERROR 02-11 11:32:58 engine.py:389] Traceback (most recent call last):
ERROR 02-11 11:32:58 engine.py:389]   File "/root/miniconda3/envs/vllm-ascend-cp310/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 380, in run_mp_engine
ERROR 02-11 11:32:58 engine.py:389]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 02-11 11:32:58 engine.py:389]   File "/root/miniconda3/envs/vllm-ascend-cp310/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 123, in from_engine_args
ERROR 02-11 11:32:58 engine.py:389]     return cls(ipc_path=ipc_path,
ERROR 02-11 11:32:58 engine.py:389]   File "/root/miniconda3/envs/vllm-ascend-cp310/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 75, in __init__
ERROR 02-11 11:32:58 engine.py:389]     self.engine = LLMEngine(*args, **kwargs)
ERROR 02-11 11:32:58 engine.py:389]   File "/root/miniconda3/envs/vllm-ascend-cp310/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
ERROR 02-11 11:32:58 engine.py:389]     self._initialize_kv_caches()
ERROR 02-11 11:32:58 engine.py:389]   File "/root/miniconda3/envs/vllm-ascend-cp310/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 416, in _initialize_kv_caches
ERROR 02-11 11:32:58 engine.py:389]     self.model_executor.determine_num_available_blocks())
ERROR 02-11 11:32:58 engine.py:389]   File "/root/miniconda3/envs/vllm-ascend-cp310/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 101, in determine_num_available_blocks
ERROR 02-11 11:32:58 engine.py:389]     results = self.collective_rpc("determine_num_available_blocks")
```
报以上错误
机器环境如下

![Image](https://github.com/user-attachments/assets/504b3111-bbfc-4974-8f15-ce5353e1c8e6)
