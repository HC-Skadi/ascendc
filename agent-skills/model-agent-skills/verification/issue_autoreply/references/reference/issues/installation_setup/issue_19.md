# Issue #19: [v0.7.1rc1] FAQ & Feedback

## 基本信息

- **编号**: #19
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/19
- **创建时间**: 2025-02-08T00:37:28Z
- **关闭时间**: 2025-04-09T16:38:38Z
- **更新时间**: 2025-04-09T16:38:39Z
- **提交者**: @Yikun
- **评论数**: 15

## 标签

无

## 问题描述

Please leave comments here about your usage of vLLM Ascend Plugin.

Does it work? Does it not work? Which models do you need? Which feature do you need? any bugs?

For in depth discussion, please feel free to join [#sig-ascend](https://inviter.co/vllm-slack) in the vLLM Slack workspace.

Next RC release: v0.7.3rc1 will ready in early March (2025.03).

----

FAQ:

#### 1. What devices are currently supported?

Currently,  only Atlas A2 series are supported.
- Atlas A2 Training series (Atlas 800T A2, Atlas 900 A2 PoD, Atlas 200T A2 Box16, Atlas 300T A2)
- Atlas 800I A2 Inference series (Atlas 800I A2)

#### 2. How to setup dev env, build and test?

Here is a step by step guide for [building and testing](https://github.com/vllm-project/vllm-ascend/blob/main/CONTRIBUTING.md#building-and-testing). 

If you just want to install stable vLLM, please refer to: https://vllm-ascend.readthedocs.io/en/latest/installation.html

#### 3. How to do multi node deployment?

You can launch multi-node service with Ray, find more details at our tutorials: [<u>Online Serving on Multi Machine</u>](https://vllm-ascend.readthedocs.io/en/latest/tutorials.html#online-serving-on-multi-machine).

- `ray: command not found`: pip install ray
- `fatal error ：numa.h：No such file or directory`: `yum install numactl-devel` / `apt install libnuma-dev`

#### 4. `RuntimeError: Failed to infer device type` or `ImportError: `libatb.so`: cannot open shared object file: No such file or directory`.

This is usually because of the wrong `torch_npu` version or lack of Ascend CANN NNAL Package.

Make sure you install the correct version of `torch_npu`.

Install with the specific CANN and NNAL.

The details of `torch_npu` and CANN NNAL could be found at our [<u>docs</u>](https://vllm-ascend.readthedocs.io/en/latest/installation.html#setup-vllm-and-vllm-ascend).

#### 5. Is Atlas 300 currently supported?

Not supported yet, currently only Atlas A2 series devices supported as shown [<u>here</u>](https://github.com/vllm-project/vllm-ascend?tab=readme-ov-file#prerequisites).

From a technical view, vllm-ascend support would be possible if the torch-npu is supported. Otherwise, we have to implement it by using custom ops. We are also welcome to join us to improve together.

#### 6. Are Quantization algorithms currently supported?

Not support now, but we will support **W8A8** and **FA3** quantization algorithms in the future.

#### 7. Inference speed is slow.

Currently, the performance of vLLM on Ascend still need to be improved. We are also working together with the Ascend team to improve it. The first release will be `v0.7.3` in 2025 Q1. Therefore, welcome everyone join us to improve it.

#### 8. DeepSeek V3 / R1 related errors.

Known issue will be fixed in vllm-ascend `v0.7.3rc1` (March. 2025) with CANN `8.1.RC1.alpha001` (Feb. 2025):

- `AssertionError: Torch not compiled with CUDA enabled.`
- `RuntimeError: GroupTopkOperation CreateOperation failed.`
- `ValueError: Unknown quantization method: ascend.`
- ...

Find more details in #72, which tracks initial support for the Deepseek V3 model with vllm-ascend.

#### 9. Qwen2-VL / Qwen2.5-VL related errors.

**Q1:** `Qwen2-VL-72B-Instruct` inference failure: `RuntimeError: call aclnnFlashAttentionScore failed`. (#115)

This is caused by the inner error of CANN ops, which will be fixed in the next CANN version.

BTW, qwen2 in vllm only works with torch SDPA on non-GPU platform. We'll improve it in vLLM to make it support more backend in the next release. Find more details [<u>here</u>](https://github.com/vllm-project/vllm/blob/main/vllm/attention/layer.py#L254-L257).

#### 10 `Error: TBE Subprocess Task Distribute Failure When TP>1`
 (#198)
```bash
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
```

It's not that the model wasn't loaded successfully, but that the model wasn't exited successfully. Adding code related to manually cleaning up objects, with reference to the [<u>tutorials</u>](https://vllm-ascend.readthedocs.io/en/latest/tutorials.html#run-vllm-ascend-on-multi-npu), can resolve this error.

----

(Updated on: 2025.03.06)
