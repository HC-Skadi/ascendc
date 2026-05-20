# Issue #4051: [Bug]: Qwen3-next EP inference failure

## 基本信息

- **编号**: #4051
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4051
- **创建时间**: 2025-11-07T06:38:25Z
- **关闭时间**: 2025-11-10T12:04:38Z
- **更新时间**: 2025-11-10T12:04:38Z
- **提交者**: @wxsIcey
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>

```text
Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] numpy                                1.26.4                              pypi_0           pypi
[conda] pyzmq                                27.1.0                              pypi_0           pypi
[conda] torch                                2.7.1+cpu                           pypi_0           pypi
[conda] torch-npu                            2.7.1                               pypi_0           pypi
[conda] torchvision                          0.22.1                              pypi_0           pypi
[conda] transformers                         4.57.1                              pypi_0           pypi
vLLM Version: 0.10.2rc3.dev1319+g074475541 (git sha: 074475541)
vLLM Ascend Version: 0.11.0rc1.dev188+g3db53d117 (git sha: 3db53d117)

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC001B235
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```
</details>


### 🐛 Describe the bug

```python
def main():
    prompts = [
        "窗前明月光，",
        "The president of the United States is Mr.",
        "The capital of France is",
        "The future of AI is",
        "感时花溅泪，",
        "家书抵万金啥意思？",
        "plz tell me a story: ",
    ]
    sampling_params = SamplingParams(max_tokens=100, temperature=0.6, top_k=40, top_p=0.95)
    llm = LLM(
        model="Qwen/Qwen3-Next-80B-A3B-Instruct",
              tensor_parallel_size=4,
              enable_expert_parallel=True,
              enforce_eager=True,
              trust_remote_code=True,
              max_model_len=256,
              gpu_memory_utilization=0.7,
              block_size=64,
              )

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

```text
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2494, in _dummy_run
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999[PID: 940663] 2025-11-07-06:32:37.914.373 (EZ9999):  HCCL_BUFFSIZE is too SMALL, maxBs = 64, h = 2048, epWorldSize = 4, localMoeExpertNum = 128, sharedExpertNum = 0, tokenNeedSizeDispatch = 4608, tokenNeedSizeCombine = 4096, k = 10, NEEDED_HCCL_BUFFSIZE(((maxBs * tokenNeedSizeDispatch * ep_worldsize * localMoeExpertNum) + (maxBs * tokenNeedSizeCombine * (k + sharedExpertNum))) * 2) = 294MB, HCCL_BUFFSIZE=200MB.[FUNC:MoeDistributeDispatchA3TilingFuncImpl][FILE:moe_distribute_dispatch_v2_tiling.cc][LINE:941]
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2494, in _dummy_run
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]         TraceBack (most recent call last):
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 163, in forward
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        MoeDistributeDispatchV2 do tiling failed, ret is -1.
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.experts(hidden_states=hidden_states,
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2315, in _generate_dummy_run_hidden_states
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorDoTiling(executor) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2315, in _generate_dummy_run_hidden_states
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorMatchCache(executor) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671] 
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671] Traceback (most recent call last):
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     output = func(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 44, in forward
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._forward_method(*args, **kwargs)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 1144, in forward
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 221, in determine_available_memory
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 1144, in forward
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     self.model_runner.profile_run()
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 79, in forward_oot
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2540, in profile_run
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_native(*args, **kwargs)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/compilation/decorators.py", line 225, in __call__
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     self._dummy_run(self.mc2_tokens_capacity, with_prefill=True)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/compilation/decorators.py", line 225, in __call__
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1827, in forward_native
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return func(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     fused_output = torch.ops.vllm.moe_forward(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 928, in forward
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 928, in forward
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states, residual = layer(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2494, in _dummy_run
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states, residual = layer(
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                               ^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                               ^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2315, in _generate_dummy_run_hidden_states
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2144, in moe_forward
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 318, in forward_impl
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.quant_method.apply(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 848, in forward
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 848, in forward
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.mlp(hidden_states)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.mlp(hidden_states)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 138, in apply
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return moe_comm_method.fused_experts(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 1144, in forward
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/moe_comm_method.py", line 121, in fused_experts
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     results = self.token_dispatcher.token_dispatch(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/compilation/decorators.py", line 225, in __call__
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/token_dispatcher.py", line 191, in token_dispatch
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     self.output = torch_npu.npu_moe_distribute_dispatch_v2(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 163, in forward
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 163, in forward
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.experts(hidden_states=hidden_states,
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 928, in forward
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.experts(hidden_states=hidden_states,
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states, residual = layer(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                               ^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671] RuntimeError: npu_moe_distribute_dispatch_v2:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561002
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671] [ERROR] 2025-11-07-06:32:37 (PID:940664, Device:1, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999: Inner Error!
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999[PID: 940664] 2025-11-07-06:32:37.914.104 (EZ9999):  HCCL_BUFFSIZE is too SMALL, maxBs = 64, h = 2048, epWorldSize = 4, localMoeExpertNum = 128, sharedExpertNum = 0, tokenNeedSizeDispatch = 4608, tokenNeedSizeCombine = 4096, k = 10, NEEDED_HCCL_BUFFSIZE(((maxBs * tokenNeedSizeDispatch * ep_worldsize * localMoeExpertNum) + (maxBs * tokenNeedSizeCombine * (k + sharedExpertNum))) * 2) = 294MB, HCCL_BUFFSIZE=200MB.[FUNC:MoeDistributeDispatchA3TilingFuncImpl][FILE:moe_distribute_dispatch_v2_tiling.cc][LINE:941]
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]         TraceBack (most recent call last):
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 44, in forward
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 44, in forward
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        MoeDistributeDispatchV2 do tiling failed, ret is -1.
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._forward_method(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 848, in forward
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._forward_method(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorDoTiling(executor) failed
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     hidden_states = self.mlp(hidden_states)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 79, in forward_oot
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 79, in forward_oot
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorMatchCache(executor) failed
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_native(*args, **kwargs)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_native(*args, **kwargs)
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671] 
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1827, in forward_native
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1827, in forward_native
(Worker_TP1_EP1 pid=940664) ERROR 11-07 06:32:37 [multiproc_executor.py:671] 
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     fused_output = torch.ops.vllm.moe_forward(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     fused_output = torch.ops.vllm.moe_forward(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/models/qwen3_next.py", line 163, in forward
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.experts(hidden_states=hidden_states,
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2144, in moe_forward
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2144, in moe_forward
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 318, in forward_impl
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.quant_method.apply(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 318, in forward_impl
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 138, in apply
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.quant_method.apply(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return moe_comm_method.fused_experts(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 138, in apply
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 44, in forward
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/moe_comm_method.py", line 121, in fused_experts
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return moe_comm_method.fused_experts(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._forward_method(*args, **kwargs)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     results = self.token_dispatcher.token_dispatch(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/moe_comm_method.py", line 121, in fused_experts
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/custom_op.py", line 79, in forward_oot
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/token_dispatcher.py", line 191, in token_dispatch
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     results = self.token_dispatcher.token_dispatch(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_native(*args, **kwargs)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     self.output = torch_npu.npu_moe_distribute_dispatch_v2(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/token_dispatcher.py", line 191, in token_dispatch
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1827, in forward_native
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     self.output = torch_npu.npu_moe_distribute_dispatch_v2(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     fused_output = torch.ops.vllm.moe_forward(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671] RuntimeError: npu_moe_distribute_dispatch_v2:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561002
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671] [ERROR] 2025-11-07-06:32:37 (PID:940666, Device:3, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999: Inner Error!
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999[PID: 940666] 2025-11-07-06:32:37.913.624 (EZ9999):  HCCL_BUFFSIZE is too SMALL, maxBs = 64, h = 2048, epWorldSize = 4, localMoeExpertNum = 128, sharedExpertNum = 0, tokenNeedSizeDispatch = 4608, tokenNeedSizeCombine = 4096, k = 10, NEEDED_HCCL_BUFFSIZE(((maxBs * tokenNeedSizeDispatch * ep_worldsize * localMoeExpertNum) + (maxBs * tokenNeedSizeCombine * (k + sharedExpertNum))) * 2) = 294MB, HCCL_BUFFSIZE=200MB.[FUNC:MoeDistributeDispatchA3TilingFuncImpl][FILE:moe_distribute_dispatch_v2_tiling.cc][LINE:941]
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]         TraceBack (most recent call last):
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        MoeDistributeDispatchV2 do tiling failed, ret is -1.
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671] RuntimeError: npu_moe_distribute_dispatch_v2:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561002
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2144, in moe_forward
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorDoTiling(executor) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671] [ERROR] 2025-11-07-06:32:37 (PID:940665, Device:2, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999: Inner Error!
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorMatchCache(executor) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999[PID: 940665] 2025-11-07-06:32:37.913.297 (EZ9999):  HCCL_BUFFSIZE is too SMALL, maxBs = 64, h = 2048, epWorldSize = 4, localMoeExpertNum = 128, sharedExpertNum = 0, tokenNeedSizeDispatch = 4608, tokenNeedSizeCombine = 4096, k = 10, NEEDED_HCCL_BUFFSIZE(((maxBs * tokenNeedSizeDispatch * ep_worldsize * localMoeExpertNum) + (maxBs * tokenNeedSizeCombine * (k + sharedExpertNum))) * 2) = 294MB, HCCL_BUFFSIZE=200MB.[FUNC:MoeDistributeDispatchA3TilingFuncImpl][FILE:moe_distribute_dispatch_v2_tiling.cc][LINE:941]
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 318, in forward_impl
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]         TraceBack (most recent call last):
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     final_hidden_states = self.quant_method.apply(
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671] 
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        MoeDistributeDispatchV2 do tiling failed, ret is -1.
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP3_EP3 pid=940666) ERROR 11-07 06:32:37 [multiproc_executor.py:671] 
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorDoTiling(executor) failed
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 138, in apply
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return moe_comm_method.fused_experts(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorMatchCache(executor) failed
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/moe_comm_method.py", line 121, in fused_experts
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671] 
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     results = self.token_dispatcher.token_dispatch(
(Worker_TP2_EP2 pid=940665) ERROR 11-07 06:32:37 [multiproc_executor.py:671] 
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/moe/token_dispatcher.py", line 191, in token_dispatch
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     self.output = torch_npu.npu_moe_distribute_dispatch_v2(
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]   File "/home/wxs/miniconda/envs/vllm/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671] RuntimeError: npu_moe_distribute_dispatch_v2:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561002
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671] [ERROR] 2025-11-07-06:32:37 (PID:940663, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999: Inner Error!
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671] EZ9999[PID: 940663] 2025-11-07-06:32:37.914.373 (EZ9999):  HCCL_BUFFSIZE is too SMALL, maxBs = 64, h = 2048, epWorldSize = 4, localMoeExpertNum = 128, sharedExpertNum = 0, tokenNeedSizeDispatch = 4608, tokenNeedSizeCombine = 4096, k = 10, NEEDED_HCCL_BUFFSIZE(((maxBs * tokenNeedSizeDispatch * ep_worldsize * localMoeExpertNum) + (maxBs * tokenNeedSizeCombine * (k + sharedExpertNum))) * 2) = 294MB, HCCL_BUFFSIZE=200MB.[FUNC:MoeDistributeDispatchA3TilingFuncImpl][FILE:moe_distribute_dispatch_v2_tiling.cc][LINE:941]
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]         TraceBack (most recent call last):
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        MoeDistributeDispatchV2 do tiling failed, ret is -1.
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorDoTiling(executor) failed
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseExecutorMatchCache(executor) failed
(Worker_TP0_EP0 pid=940663) ERROR 11-07 06:32:37 [multiproc_executor.py:671]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
```
