# Issue #988: [Bug]: Llama W8A8 error

## 基本信息

- **编号**: #988
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/988
- **创建时间**: 2025-05-28T08:49:09Z
- **关闭时间**: 2025-11-11T13:17:14Z
- **更新时间**: 2025-11-11T13:17:14Z
- **提交者**: @TBD1
- **评论数**: 5

## 标签

bug; module:quantization

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```


</details>
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-1.1.0.36-aarch64-with-glibc2.35

[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3

vLLM Version: 0.8.4
vLLM Ascend Version: 0.8.5rc2.dev53+ge2a0c19 (git sha: e2a0c19)


CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux

### 🐛 Describe the bug

w8a8量化服务启动失败。
按照https://github.com/vllm-project/vllm-ascend/pull/877 这个PR改动之后，用master分支的ascend-vllm代码，会有如下报错，请问下是哪里还需要额外改动？


root@dac2ed43b12c:~/www# vllm serve /root/www/Llama-2-13b-chat-hf-w8a8/ --tensor-parallel-size 1 --served-model-name "Llama-13b-w8a8" --max-model-len 4096 --quantization ascend

Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/workspace/vllm/vllm/entrypoints/cli/main.py", line 51, in main
    args.dispatch_function(args)
  File "/workspace/vllm/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1069, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 166, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
  File "/workspace/vllm/vllm/engine/arg_utils.py", line 1335, in create_engine_config
    config = VllmConfig(
  File "<string>", line 19, in __init__
  File "/workspace/vllm/vllm/config.py", line 3709, in __post_init__
    self.quant_config = VllmConfig._get_quantization_config(
  File "/workspace/vllm/vllm/config.py", line 3651, in _get_quantization_config
    quant_config = get_quant_config(model_config, load_config)
  File "/workspace/vllm/vllm/model_executor/model_loader/weight_utils.py", line 195, in get_quant_config
    return quant_cls()
TypeError: AscendQuantConfig.__init__() missing 1 required positional argument: 'quant_config'
[ERROR] 2025-05-28-08:45:40 (PID:31056, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
