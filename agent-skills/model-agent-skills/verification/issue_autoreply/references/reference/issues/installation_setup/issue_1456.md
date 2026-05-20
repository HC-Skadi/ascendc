# Issue #1456: [Doc]:

## 基本信息

- **编号**: #1456
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1456
- **创建时间**: 2025-06-26T09:25:40Z
- **关闭时间**: 2025-06-26T09:25:56Z
- **更新时间**: 2025-06-26T09:25:56Z
- **提交者**: @boomfh
- **评论数**: 0

## 标签

documentation

## 问题描述

### 📚 The doc issue

<details>
(PyTorch-2.5.1) [ma-user@liteserver-jiadu-00003 data]$ export ENFORCE_EAGER=1
(PyTorch-2.5.1) [ma-user@liteserver-jiadu-00003 data]$ vllm serve /data/DeepSeek-R1-w8a8-vllm-fusion/ --port 8000 -tp 16 --max-model-len 4096 --quantization ascend
/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux/ascend_toolkit_install.info owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux/ascend_toolkit_install.info owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
INFO 06-26 16:16:29 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-26 16:16:29 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-26 16:16:30 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-26 16:16:30 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-26 16:16:30 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-26 16:16:30 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-26 16:16:32 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
WARNING 06-26 16:16:35 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-26 16:16:35 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-26 16:16:35 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-26 16:16:35 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-26 16:16:35 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-26 16:16:35 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-26 16:16:36 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-26 16:16:36 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-26 16:16:37 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-26 16:16:38 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-26 16:16:38 [api_server.py:1287] vLLM API server version 0.9.1
INFO 06-26 16:16:39 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-26 16:16:39 [cli_args.py:309] non-default args: {'model': '/data/DeepSeek-R1-w8a8-vllm-fusion/', 'max_model_len': 4096, 'quantization': 'ascend', 'tensor_parallel_size': 16}
`rope_scaling`'s factor field must be a float >= 1, got 40
`rope_scaling`'s beta_fast field must be a float, got 32
`rope_scaling`'s beta_slow field must be a float, got 1
INFO 06-26 16:16:49 [config.py:823] This model supports multiple tasks: {'embed', 'score', 'classify', 'reward', 'generate'}. Defaulting to 'generate'.
WARNING 06-26 16:16:49 [config.py:931] ascend quantization is not fully optimized yet. The speed can be slower than non-quantized models.
WARNING 06-26 16:16:49 [arg_utils.py:1647] Detected VLLM_USE_V1=1 with npu. Usage should be considered experimental. Please report any issues on Github.
INFO 06-26 16:16:49 [config.py:1946] Defaulting to use mp for distributed inference
INFO 06-26 16:16:49 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-26 16:16:49 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048.
Traceback (most recent call last):
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 59, in main
    args.dispatch_function(args)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 58, in cmd
    uvloop.run(run_server(args))
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1323, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1343, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 155, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 177, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1225, in create_engine_config
    config = VllmConfig(
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__
    s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.5.1/lib/python3.10/site-packages/vllm/config.py", line 4488, in __post_init__
    current_platform.check_and_update_config(self)
  File "/home/ma-user/AscendFactory/vllm-ascend/vllm_ascend/platform.py", line 161, in check_and_update_config
    check_ascend_config(vllm_config, enforce_eager)
  File "/home/ma-user/AscendFactory/vllm-ascend/vllm_ascend/ascend_config.py", line 154, in check_ascend_config
    raise NotImplementedError(
NotImplementedError: ACL Graph does not support deepseek. Please try torchair graph mode to serve deepseek models on vllm-ascend. Or set `enforce_eager=True` to use eager mode.


```text
(PyTorch-2.5.1) [ma-user@liteserver-jiadu-00003 data]$ pip list |grep vllm
vllm                                     0.9.1
vllm_ascend                              0.9.1rc1                /home/ma-user/AscendFactory/vllm-ascend

```

用的是0.9.1.rc1，运行deepseek-R1-w8a8时候报错不支持deepseek，这是什么原因呢
</details>


### Suggest a potential alternative/fix

_No response_
