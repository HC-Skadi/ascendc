# Issue #2182: [Bug][v0.9.1]: test_aclgraph.py failed with "full_cuda_graph": True on A2 (910B1)

## 基本信息

- **编号**: #2182
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2182
- **创建时间**: 2025-08-04T01:19:53Z
- **关闭时间**: 2025-12-23T12:46:36Z
- **更新时间**: 2025-12-23T12:46:36Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

```
Error:  2025-07-31-01:25:19 (PID:12066, Device:0, RankID:-1) ERR00100 PTA call acl api failed
Error: : Model execution failed. 
        Rectify the fault based on the error information in the ascend log.
EE9999: Inner Error!
EE9999: [PID: 12066] 2025-07-31-01:25:19.967.079 The error from device(chipId:6, dieId:0), serial number is 1, event wait timeout occurred during task execution, stream_id:19, sq_id:19, task_id:16, event_id=73, timeout=1866s.[FUNC:ProcessStarsWaitTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1400]
        TraceBack (most recent call last):
       Task execute failed, device_id=0, stream_id=19, task_id=16, flip_num=0, task_type=3(EVENT_WAIT).[FUNC:GetError][FILE:stream.cc][LINE:1183]
       rtDeviceSynchronizeWithTimeout execute failed, reason=[the model stream execute failed][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       wait for compute device to finish failed, runtime result = 507011.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

Exception raised from malloc at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:91 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0xb8 (0xffff7f8fc908 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x6c (0xffff7f8ab404 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x82c83c (0xfffe744ec83c in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x82dda0 (0xfffe744edda0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x82e9a0 (0xfffe744ee9a0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x82878c (0xfffe744e878c in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x197d75c (0xfffe7563d75c in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: at_npu::native::allocate_workspace(unsigned long, void*) + 0x28 (0xfffe744e6438 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0x83cac (0xfffe671c3cac in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #9: <unknown function> + 0x192b0f0 (0xfffe755eb0f0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #10: <unknown function> + 0x811794 (0xfffe744d1794 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #11: <unknown function> + 0x8139c4 (0xfffe744d39c4 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #12: <unknown function> + 0x810334 (0xfffe744d0334 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #13: <unknown function> + 0x4c9e4c (0xffff7f939e4c in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #14: <unknown function> + 0x7d5b8 (0xffff8accd5b8 in /lib/aarch64-linux-gnu/libc.so.6)
frame #15: <unknown function> + 0xe5edc (0xffff8ad35edc in /lib/aarch64-linux-gnu/libc.so.6)
```

test failed: https://github.com/vllm-project/vllm-ascend/actions/runs/16636611495/job/47078910783?pr=2119



### 🐛 Describe the bug

```
pytest -sv tests/singlecard/test_aclgraph.py::test_models[True-12-Qwen/Qwen2.5-0.5B-Instruct]
```
