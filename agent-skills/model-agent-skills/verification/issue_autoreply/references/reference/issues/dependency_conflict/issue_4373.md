# Issue #4373: [Bug]: When layout is TND, not support Page Attention

## 基本信息

- **编号**: #4373
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4373
- **创建时间**: 2025-11-24T03:14:25Z
- **关闭时间**: 2025-11-24T07:11:21Z
- **更新时间**: 2025-12-30T07:58:19Z
- **提交者**: @tardis-key
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm                              0.11.0+empty  /vllm
vllm_ascend                       0.11.0rc1     /vllm-ascend
```

</details>


### 🐛 Describe the bug


(WorkerDict pid=142618)   File "/vllm-ascend/vllm_ascend/patch/worker/patch_attention_layer.py", line 67, in forward
(WorkerDict pid=142618)     self.impl.forward(self,
(WorkerDict pid=142618)   File "/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 593, in forward
(WorkerDict pid=142618)     torch.ops.vllm.unified_ascend_attention_with_output(
(WorkerDict pid=142618)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(WorkerDict pid=142618)     return self._op(*args, **(kwargs or {}))
(WorkerDict pid=142618)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(WorkerDict pid=142618)   File "/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 691, in unified_ascend_attention_with_output
(WorkerDict pid=142618)     self.impl.forward(self,
(WorkerDict pid=142618)   File "/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 668, in forward
(WorkerDict pid=142618)     output = self._forward_v1_style(query, attn_metadata, output)
(WorkerDict pid=142618)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(WorkerDict pid=142618)   File "/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 539, in _forward_v1_style
(WorkerDict pid=142618)     output, _ = torch_npu.npu_fused_infer_attention_score(
(WorkerDict pid=142618)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(WorkerDict pid=142618)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(WorkerDict pid=142618)     return self._op(*args, **(kwargs or {}))
(WorkerDict pid=142618)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(WorkerDict pid=142618) RuntimeError: npu_fused_infer_attention_score_symint:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:208 NPU function error: call aclnnFusedInferAttentionScoreV3 failed, error code is 561002
(WorkerDict pid=142618) [ERROR] 2025-11-24-02:53:50 (PID:142618, Device:0, RankID:1) ERR00100 PTA call acl api failed.
(WorkerDict pid=142618) E89999: Inner Error!
(WorkerDict pid=142618) E89999: [PID: 142618] 2025-11-24-02:53:50.456.545 When layout is TND, not support Page Attention[FUNC:RunBigKernelTilingWithParams][FILE:prompt_flash_attention_tiling.cpp][LINE:3400]
(WorkerDict pid=142618)         TraceBack (most recent call last):
(WorkerDict pid=142618)        FusedInferAttentionScore do tiling failed, ret is -1.
(WorkerDict pid=142618)        Check NnopbaseExecutorDoTiling(executor) failed
(WorkerDict pid=142618)        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(WorkerDict pid=142618)        Check NnopbaseExecutorMatchCache(executor) failed
(WorkerDict pid=142618)        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
(WorkerDict pid=142618)
(WorkerDict pid=142617)

