# Issue #3453: [Bug]: Encountered issues with custom operator loading during use.

## 基本信息

- **编号**: #3453
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3453
- **创建时间**: 2025-10-14T10:13:14Z
- **关闭时间**: 2025-10-15T01:34:33Z
- **更新时间**: 2026-02-11T12:25:41Z
- **提交者**: @CarlCloud
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

<details>
My hardware is linux-aarch64 910B-64GB and CANN/ascend-toolkit/nnal 8.2RC1.
I use command pip install to use these lib:
torch==2.8.0
torch_npu==2.8.0rc1
vllm==0.10.2
vllm-ascend==0.10.2rc1
</details>


### 🐛 Describe the bug

Hello，I already use this script.py to load Qwen3-32B in my env which I described above. And I meet some problem about vllm-ascned.ops which defined some custom operator and  torch.ops._C_ascend\

Initially, the problem I encountered was that the custom operator rotary_embedding could not be loaded correctly. And I followed the issue #3414 which delete function and fix this problem. and then I meet the following problem:
...
Loading safetensors checkpoint shards: 100% Completed | 17/17 [01:04<00:00,  3.79s/it]
...
(EngineCore_DP0 pid=2041805) INFO 10-14 17:17:23 [kv_cache_utils.py:864] GPU KV cache size: 128,000 tokens
(EngineCore_DP0 pid=2041805) INFO 10-14 17:17:23 [kv_cache_utils.py:868] Maximum concurrency for 40,960 tokens per request: 3.12x
Capturing ACL graphs (mixed prefill-decode, PIECEWISE):   0%| | 0/9 [00:00<?, ?i[rank0]:[W1014 17:17:24.782539679 compiler_depend.ts:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank1]:[W1014 17:17:24.802060561 compiler_depend.ts:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank0]:[W1014 17:17:24.992527772 compiler_depend.ts:250] Warning: CAUTION: The operator '_C_ascend::weak_ref_tensor' is not currently supported on the NPU backend and will fall back to run on the CPU. This may have performance implications. (function npu_cpu_fallback)
[rank1]:[W1014 17:17:24.993107117 compiler_depend.ts:250] Warning: CAUTION: The operator '_C_ascend::weak_ref_tensor' is not currently supported on the NPU backend and will fall back to run on the CPU. This may have performance implications. (function npu_cpu_fallback)

... SOME ERROR MESSAGES...
(EngineCore_DP0 pid=2041805) (EngineCore_DP0 pid=2041805) (Worker_TP0 pid=2041823) (Worker_TP1 pid=2041827) ERROR 10-14 17:17:24 [multiproc_executor.py:654]     return self._wrapped_call(self, *args, **kwargs)
ERROR 10-14 17:17:24 [multiproc_executor.py:654] NotImplementedError: Could not run '_C_ascend::weak_ref_tensor' with arguments from the 'CPU' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using custom build). If you are a Facebook employee using PyTorch on mobile, please visit https://fburl.com/ptmfixes for possible resolutions. '_C_ascend::weak_ref_tensor' is only available for these backends: [MAIA, PrivateUse1, Meta, SparsePrivateUse1, BackendSelect, Python, FuncTorchDynamicLayerBackMode, Functionalize, Named, Conjugate, Negative, ZeroTensor, ADInplaceOrView, AutogradOther, AutogradCPU, AutogradCUDA, AutogradXLA, AutogradMPS, AutogradXPU, AutogradHPU, AutogradLazy, AutogradMTIA, AutogradMAIA, AutogradPrivateUse1, AutogradMeta, Tracer, AutocastCPU, AutocastMTIA, AutocastMAIA, AutocastXPU, AutocastMPS, AutocastCUDA, AutocastPrivateUse1, FuncTorchBatched, BatchedNestedTensor, FuncTorchVmapMode, Batched, VmapMode, FuncTorchGradWrapper, PythonTLSSnapshot, FuncTorchDynamicLayerFrontMode, PreDispatch, PythonDispatcher].
...

this problem seem likes the problem issue #3414， and caused by the torch.ops._C_ascend has never been compiled and export to my env. Is my guess right? 🙂

===============================================
test_vllm.py:

import torch
import torch_npu
import vllm
from vllm import SamplingParams
from vllm.model_executor.models.qwen3 import Qwen3ForCausalLM
torch_npu.npu.set_compile_mode(jit_compile=False)
model_path = /path_to_qwen3_weight
model = vllm.LLM(
    model=model_path,
    tensor_parallel_size=2,
    dtype="float16",
    enable_chunked_prefill=True,
    max_num_batched_tokens=2048,
    trust_remote_code=True,
    gpu_memory_utilization=0.85,
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

Looking for your reply, thx!
