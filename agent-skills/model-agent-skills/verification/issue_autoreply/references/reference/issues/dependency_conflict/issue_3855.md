# Issue #3855: [Bug]: Qwen3-30B-A3B-Instruct-2507 输入shape不支持运行报错

## 基本信息

- **编号**: #3855
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3855
- **创建时间**: 2025-10-29T03:40:24Z
- **关闭时间**: 2025-12-15T08:28:24Z
- **更新时间**: 2025-12-15T08:28:45Z
- **提交者**: @ZSL98
- **评论数**: 3

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-98.oe2403sp2)
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.38

Python version: 3.11.13 (main, Oct 15 2025, 08:29:26) [GCC 12.3.1 (openEuler 12.3.1-98.oe2403sp2)] (64-bit runtime)
Python platform: Linux-5.10.0+-aarch64-with-glibc2.38

[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1.dev20251023
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc1.dev53+g9eb62935b.d20251023 (git sha: 9eb62935b, date: 20251023)

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1.alpha003
innerversion=V100R001C23B092
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1.alpha003/aarch64-linux
```

</details>

两卡910B运行Qwen3-30B-A3B-Instruct-2507模型运行报错，报错内容是MoE算子shape不支持，然而输入是128的整数倍依然无法支持。

### 🐛 Describe the bug

运行脚本：

```python
from vllm import LLM, RequestOutput, SamplingParams

prompts = ["Hello "*512]*512

def print_prompts_and_outputs(outputs: list[RequestOutput]) -> None:
    print("-" * 60)
    for output in outputs[:1]:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt:    {prompt!r}")
        print(f"Output:    {generated_text!r}")
        print("-" * 60)

def main():
    # Create an LLM without loading real weights
    llm = LLM(
        model="/root/model/Qwen3-30B-A3B-Instruct-2507",
        load_format="dummy",
        enforce_eager=True,
        tensor_parallel_size=2,
        max_model_len=40960,
        enable_expert_parallel=True,
    )
    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
    outputs = llm.generate(prompts, sampling_params)
    print_prompts_and_outputs(outputs)

if __name__ == "__main__":
    main()
```

报错内容，主要是MoeInitRoutingV2输入shape不支持，请问是我输入的shape（512*512）不符合要求还是算子bug？

```
[rank0]:[E1029 03:18:08.667296670 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:109 NPU function error: call aclnnMoeInitRoutingV3 failed, error code is 561103
[ERROR] 2025-10-29-03:18:08 (PID:24481, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
EZ9999: Inner Error!
EZ9999[PID: 24481] 2025-10-29-03:18:08.948.444 (EZ9999):  The first dim of expertTokensCountOrCumsum should be 128.[FUNC:CheckTokenCount][FILE:moe_init_routing_v2_tiling.cpp][LINE:131]
        TraceBack (most recent call last):
       Tiling failed
       Tiling Failed.
       Kernel Run failed. opType: 37, MoeInitRoutingV2
       launch failed for MoeInitRoutingV2, errno:561103.
```
