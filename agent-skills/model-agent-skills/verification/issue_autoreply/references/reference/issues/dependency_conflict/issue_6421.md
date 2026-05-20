# Issue #6421: [Bug]: EngineCore crash: AssertionError with MTP and Structured Output in PD Disaggregation mode

## 基本信息

- **编号**: #6421
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6421
- **创建时间**: 2026-01-30T07:39:16Z
- **关闭时间**: 2026-01-30T09:04:49Z
- **更新时间**: 2026-01-30T09:04:50Z
- **提交者**: @triomino
- **评论数**: 1

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

### Prerequisites
* [x] I have searched the existing issues and didn't find a similar bug.
* [x] I am using the official `vllm-ascend:0.13.0rc2` image.

### Description
When using **PD Disaggregation** to serve **DeepSeek-V3.2** with **Structured Output** enabled, the decoding vLLM instance crashes with an `AssertionError`. 

The issue appears to be caused by the Multi-Token Prediction (MTP) logic passing invalid token IDs (`-1`) to the `XGrammar` backend. While the C++ grammar matcher rejects the token, the Python layer triggers a fatal assertion when it fails to advance the FSM for these invalid IDs.

The issue is resolved by disabling MTP, but this prevents utilizing the full performance capabilities of the DeepSeek-V3.2 architecture.

### Error Logs
```
[06:07:45] /project/cpp/grammar_matcher.cc:428: Warning: The token id -1 is out of range [0, 129280). Rejecting the token.
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [backend_xgrammar.py:180] Failed to advance FSM for request chatcmpl-5c52ac69-13b2-48c8-87b3-3f904ffb550d for tokens -1. Please file an issue.
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70] Traceback (most recent call last):
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 61, in run_engine_core
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1248, in run_busy_loop
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]     executed = self._process_engine_step()
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 919, in _process_engine_step
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 349, in step
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]     grammar_output = self.scheduler.get_grammar_bitmask(scheduler_output)
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]   File "/vllm-workspace/vllm/vllm/v1/core/sched/scheduler.py", line 1048, in get_grammar_bitmask
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]     bitmask = self.structured_output_manager.grammar_bitmask(
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]   File "/vllm-workspace/vllm/vllm/v1/structured_output/__init__.py", line 288, in grammar_bitmask
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]     assert accepted, (token, req_id, scheduled_spec_decode_tokens)
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70]            ^^^^^^^^
(EngineCore_DP0 pid=336150) ERROR 01-30 06:07:45 [patch_core.py:70] AssertionError: (-1, 'chatcmpl-5c52ac69-13b2-48c8-87b3-3f904ffb550d', {'chatcmpl-5c52ac69-13b2-48c8-87b3-3f904ffb550d': [-1, -1, -1]})
```
### Environment
* **Model:** DeepSeek-V3.2
* **vLLM-Ascend Version:** 0.13.0rc2 (Official Image)
* **Mode:** PD Disaggregation (Prefill-Decode Separation)
* **Hardware:** Huawei Ascend NPU

### Steps to Reproduce
1. Deploy DeepSeek-V3.2 in a PD disaggregation setup.
2. Enable Multi-Token Prediction (MTP).
3. Execute a request using structured output (e.g., JSON schema or regex).
4. The decoding instance crashes when the MTP layer returns `-1` placeholders that hit the grammar FSM.

### Expected Behavior
The `StructuredOutputManager` or the underlying `XGrammar` backend should handle or filter out invalid/placeholder tokens (`-1`) generated during speculative/MTP steps instead of triggering a fatal assertion.

### Additional Context
The traceback indicates that `scheduled_spec_decode_tokens` contains `[-1, -1, -1]`. This suggests that the coordination between the MTP output and the grammar-constrained decoding in the V1 engine needs a validation check to ignore non-vocab token IDs before they reach the FSM advancement logic.
