# Issue #2742: [Bug]: doctest failed due to rotary_embedding signatures mismatch

## 基本信息

- **编号**: #2742
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2742
- **创建时间**: 2025-09-04T06:45:59Z
- **关闭时间**: 2025-09-19T12:18:02Z
- **更新时间**: 2025-09-19T12:18:02Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

bug; high

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/17454967332/job/49566622600

### 🐛 Describe the bug

```
terminate called after throwing an instance of 'c10::Error'
  what():  
Mismatch in kernel C++ signatures
  operator: _C::rotary_embedding(Tensor positions, Tensor($0! -> ) query, Tensor($1! -> )? key, int head_size, Tensor cos_sin_cache, bool is_neox) -> ()
    registered at /tmp/pip-install-vnbqqk9u/vllm_cd6a66d211f542769373702664426970/csrc/cpu/torch_bindings.cpp:74
  kernel 1: void (at::Tensor&, at::Tensor&, std::optional<at::Tensor>, long, at::Tensor&, bool)
    dispatch key: CPU
    registered at /tmp/pip-install-vnbqqk9u/vllm_cd6a66d211f542769373702664426970/csrc/cpu/torch_bindings.cpp:74
  kernel 2: std::tuple<at::Tensor, at::Tensor> (at::Tensor&, at::Tensor&, at::Tensor&, long, at::Tensor&, bool)
    dispatch key: Meta
    registered at /workspace/vllm-ascend/csrc/torch_binding_meta.cpp:91

Exception raised from registerKernel at /pytorch/aten/src/ATen/core/dispatch/OperatorEntry.cpp:121 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xd4 (0xffff757c3ea4 in /tmp/vllm_venv/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0xe4 (0xffff75763e44 in /tmp/vllm_venv/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: c10::impl::OperatorEntry::registerKernel(c10::Dispatcher const&, std::optional<c10::DispatchKey>, c10::KernelFunction, std::optional<c10::impl::CppSignature>, std::unique_ptr<c10::FunctionSchema, std::default_delete<c10::FunctionSchema> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x1f8 (0xffff769d3978 in /tmp/vllm_venv/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so)
frame #3: c10::Dispatcher::registerImpl(c10::OperatorName, std::optional<c10::DispatchKey>, c10::KernelFunction, std::optional<c10::impl::CppSignature>, std::unique_ptr<c10::FunctionSchema, std::default_delete<c10::FunctionSchema> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x108 (0xffff769c8858 in /tmp/vllm_venv/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so)
frame #4: torch::Library::_impl(char const*, torch::CppFunction&&, torch::_RegisterOrVerify) & + 0x24c (0xffff76a0541c in /tmp/vllm_venv/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so)
frame #5: <unknown function> + 0x133c8 (0xfffda4dd33c8 in /tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so)
frame #6: <unknown function> + 0x10a30 (0xfffda4dd0a30 in /tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so)
frame #7: <unknown function> + 0x10bb0 (0xfffda4dd0bb0 in /tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so)
frame #8: <unknown function> + 0x5624 (0xffff81ea4624 in /lib/ld-linux-aarch64.so.1)
frame #9: <unknown function> + 0x572c (0xffff81ea472c in /lib/ld-linux-aarch64.so.1)
frame #10: _dl_catch_exception + 0xd0 (0xffff8184d360 in /lib/aarch64-linux-gnu/libc.so.6)
frame #11: <unknown function> + 0xbf5c (0xffff81eaaf5c in /lib/ld-linux-aarch64.so.1)
frame #12: _dl_catch_exception + 0x78 (0xffff8184d308 in /lib/aarch64-linux-gnu/libc.so.6)
frame #13: <unknown function> + 0xc2fc (0xffff81eab2fc in /lib/ld-linux-aarch64.so.1)
frame #14: <unknown function> + 0x796d4 (0xffff817996d4 in /lib/aarch64-linux-gnu/libc.so.6)
frame #15: _dl_catch_exception + 0x78 (0xffff8184d308 in /lib/aarch64-linux-gnu/libc.so.6)
frame #16: _dl_catch_error + 0x40 (0xffff8184d3d0 in /lib/aarch64-linux-gnu/libc.so.6)
frame #17: <unknown function> + 0x791b0 (0xffff817991b0 in /lib/aarch64-linux-gnu/libc.so.6)
frame #18: dlopen + 0x54 (0xffff81799774 in /lib/aarch64-linux-gnu/libc.so.6)
<omitting python frames>

Traceback (most recent call last):
  File "/vllm-workspace/vllm-ascend/tests/e2e/../../examples/offline_inference_npu.py", line 51, in <module>
    main()
  File "/vllm-workspace/vllm-ascend/tests/e2e/../../examples/offline_inference_npu.py", line 40, in main
    llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 285, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 490, in from_engine_args
    return engine_cls.from_vllm_config(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/v1/engine/llm_engine.py", line 127, in from_vllm_config
    return cls(vllm_config=vllm_config,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/v1/engine/llm_engine.py", line 104, in __init__
    self.engine_core = EngineCoreClient.make_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 80, in make_client
    return SyncMPClient(vllm_config, executor_class, log_stats)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 600, in __init__
    super().__init__(
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 446, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
    next(self.gen)
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 706, in launch_core_engines
    wait_for_engine_startup(
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 759, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
```
