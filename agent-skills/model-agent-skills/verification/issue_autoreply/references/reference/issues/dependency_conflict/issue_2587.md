# Issue #2587: [Bug]: when using docker, ModelConfig validation failed in vllm engine init

## 基本信息

- **编号**: #2587
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2587
- **创建时间**: 2025-08-28T02:04:45Z
- **关闭时间**: 2025-08-30T01:53:23Z
- **更新时间**: 2025-08-30T02:43:13Z
- **提交者**: @tongtong0613
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
pytorch vesion 2.5.1
Is debug build: False

OS: Ubuntu 20.04.6 LTS (aarch64)
GCC version: 9.4.0
Cmake version: 4.1.0
Libc version: glibc-2.31
Python version: 3.11.1
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.31

CPU:
Architecture: aarch64
CPU op-mode(s): 64-bit
Byte Order: Little Endian
CPU(s): 256
on-line CPU(s) list: 0-255

relevant libs:
numpy==1.26.4
onnxruntime==1.22.0
pyzmq==27.0.2
torch==2.5.1
torch_npu==2.5.1.post3.dev20250807
torchaudio==2.5.1
torchdata==0.11.0
torchsummary==1.5.1
torchsummaryx==1.3.0
torchvision==0.20.1
transformers==4.52.4
vLLM version: 0.9.2.dev0+gb6553be1b.d20250826 (git sha: b6553be1b, data: 20250826)
vLLM Ascend version: 0.9.1rc4.dev5+ga5ca6a567.d202508267

CANN:
version: 8.3.RC1.B020

```

</details>


### 🐛 Describe the bug

**This issue occurs only in Docker environments and does not appear when using Conda directly on bare metal.**


# install:
git clone --depth 1 --branch v0.9.1 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install -v -e .
cd ..

git clone  --depth 1 --branch v0.9.1rc3 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -v -e .
cd ..

# command:

bash my_scirpt.sh # in verl

# error:
File "verl/verl/workers/rollout/vllm_rollout/vllm_rollout_spmd.py" in __init__
  self.engine = LLM(
File "vllm/vllm/entrypoints/llm.py" in __init__
  self.llm_engine = LLMEngine.from_engine_args(
File "vllm/vllm/v1/engine/llm_engine.py" in from_engine_args
  vllm_config = engine_args.create_engine_config(usage_context)
File "vllm/vllm/engine/arg_utils.py" in create_engine_config
  model_config = self.create_model_config()
File "vllm/vllm/engine/arg_utils.py" in create_model_config
  return ModelConfig

File "pydantic/_internal/_dataclasses.py" in __init__
  s.__pydantic_validator__.validate_python(ArgKwargs(args, kwargs), self_instance=s)

pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig


