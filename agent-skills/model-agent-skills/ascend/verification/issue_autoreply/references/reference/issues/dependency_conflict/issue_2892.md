# Issue #2892: [Usage]: 使用昇腾910c运行时出现问题

## 基本信息

- **编号**: #2892
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2892
- **创建时间**: 2025-09-12T09:51:36Z
- **关闭时间**: 2025-09-12T09:52:40Z
- **更新时间**: 2025-09-12T09:52:40Z
- **提交者**: @LUYserena
- **评论数**: 0

## 标签

无

## 问题描述

### Your current environment

```我的环境是cann version=8.0.RC3.20  torch=2.5.1，运行basic.py时出现以下错误，不知该如何解决
```
`[rank0]: Traceback (most recent call last):
[rank0]:   File "/vllm-workspace/vllm/examples/offline_inference/basic/basic.py", line 35, in <module>
[rank0]:     main()
[rank0]:   File "/vllm-workspace/vllm/examples/offline_inference/basic/basic.py", line 19, in main
[rank0]:     llm = LLM(model="/vllm-workspace/models/opt-125m")
[rank0]:           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/llm.py", line 243, in __init__
[rank0]:     self.llm_engine = LLMEngine.from_engine_args(
[rank0]:                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 501, in from_engine_args
[rank0]:     return engine_cls.from_vllm_config(
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 477, in from_vllm_config
[rank0]:     return cls(
[rank0]:            ^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 265, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config)
[rank0]:                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 48, in _init_executor
[rank0]:     self.collective_rpc("load_model")
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 240, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 997, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config,
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 38, in load_model
[rank0]:     model = initialize_model(vllm_config=vllm_config,
[rank0]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 62, in initialize_model
[rank0]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/opt.py", line 371, in __init__
[rank0]:     self.model = OPTModel(vllm_config=vllm_config,
[rank0]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_0_9_1/patch_decorator.py", line 47, in __init__
[rank0]:     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/opt.py", line 294, in __init__
[rank0]:     self.decoder = OPTDecoder(config,
[rank0]:                    ^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/opt.py", line 212, in __init__
[rank0]:     self.embed_positions = OPTLearnedPositionalEmbedding(
[rank0]:                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/opt.py", line 59, in __init__
[rank0]:     super().__init__(num_embeddings + self.offset, embedding_dim)
[rank0]:   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/sparse.py", line 170, in __init__
[rank0]:     self.reset_parameters()
[rank0]:   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/sparse.py", line 181, in reset_parameters
[rank0]:     init.normal_(self.weight)
[rank0]:   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/init.py", line 190, in normal_
[rank0]:     return torch.overrides.handle_torch_function(
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/overrides.py", line 1717, in handle_torch_function
[rank0]:     result = mode.__torch_function__(public_api, types, args, kwargs)
[rank0]:              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_device.py", line 106, in __torch_function__
[rank0]:     return func(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/init.py", line 193, in normal_
[rank0]:     return _no_grad_normal_(tensor, mean, std, generator)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/init.py", line 22, in _no_grad_normal_
[rank0]:     return tensor.normal_(mean, std, generator=generator)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]: RuntimeError: normal_:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:37 NPU function error: call aclnnInplaceNormal failed, error code is 561103
[rank0]: [ERROR] 2025-09-12-09:29:51 (PID:20025, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
[rank0]: EZ9999: Inner Error!
[rank0]: EZ9999: [PID: 20025] 2025-09-12-09:29:51.880.292 Parse dynamic kernel config fail.
[rank0]:         TraceBack (most recent call last):
[rank0]:        AclOpKernelInit failed opType
[rank0]:        Cast ADD_TO_LAUNCHER_LIST_AICORE failed.`

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

