# Issue #1154: [Bug]: external_launcher下无法感知data_parallel_size 导致cpu_group计算异常 assert self.cpu_group is not None

## 基本信息

- **编号**: #1154
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1154
- **创建时间**: 2025-06-10T09:05:53Z
- **关闭时间**: 2025-08-25T06:14:30Z
- **更新时间**: 2025-12-25T23:13:46Z
- **提交者**: @tardis-key
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

PyTorch version: 2.5.1+cpu
Is debug build: False

OS: Debian GNU/Linux 10 (buster) (x86_64)
GCC version: (GCC) 9.3.0
Clang version: Could not collect
CMake version: version 4.0.1
Libc version: glibc-2.28

Python version: 3.10.14 (main, Jul  3 2024, 11:05:37) [GCC 8.3.0] (64-bit runtime)
Python platform: Linux-5.10.135.bsk.6-amd64-x86_64-with-glibc2.28

Versions of relevant libraries:
[pip3] gpytorch==1.14
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchaudio==2.5.1+cpu
[pip3] torchdata==0.11.0
[pip3] torchvision==0.20.1+cpu
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.0
vLLM Ascend Version: 0.9.0rc2.dev0+g706de02.d20250610 (git sha: 706de02, date: 20250610)

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B203
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/x86_64-linux


</details>


### 🐛 Describe the bug

<details>
`self.inference_engine = LLM(
            model=model_path,
            enable_sleep_mode=True,
            tensor_parallel_size=tensor_parallel_size,
            distributed_executor_backend="external_launcher", # 0.9.0推新的dp方案，ascend适配过程没到位,在el下没有感知dp
            data_parallel_size=8, # 手动修改，需要输入dp size
            dtype=config.dtype,
            enforce_eager=config.enforce_eager,
            gpu_memory_utilization=config.gpu_memory_utilization,
            disable_custom_all_reduce=True,
            disable_mm_preprocessor_cache=False,
            skip_tokenizer_init=False,
            max_model_len=max_model_len,
            load_format=load_format,
            disable_log_stats=config.disable_log_stats,
            max_num_batched_tokens=max_num_batched_tokens,
            enable_chunked_prefill=config.enable_chunked_prefill,
            enable_prefix_caching=True,
            trust_remote_code=trust_remote_code,
            seed=config.get("seed", 0),
            **lora_kwargs,
            **engine_kwargs,
        )`

</details>

