# Issue #248: [Feature]: 如何支持一张卡上跑多个模型？

## 基本信息

- **编号**: #248
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/248
- **创建时间**: 2025-03-06T01:19:17Z
- **关闭时间**: 2025-03-13T07:48:21Z
- **更新时间**: 2025-03-13T07:48:22Z
- **提交者**: @caolicaoli
- **评论数**: 2

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch

现在跑会报错，把一张卡device给mount到两个容器里，就报错。
一张910b跑一个向量模型有点亏啊。


[EVENT] PROFILING(618,python3):2025-03-06-01:09:06.978.203 [msprof_callback_impl.cpp:336] >>> (tid:618) Started to register profiling ctrl callback.
[EVENT] PROFILING(618,python3):2025-03-06-01:09:06.978.556 [msprof_callback_impl.cpp:343] >>> (tid:618) Started to register profiling hash id callback.
[INFO] PROFILING(618,python3):2025-03-06-01:09:06.978.670 [prof_atls_plugin.cpp:117] (tid:618) RegisterProfileCallback, callback type is 7
[EVENT] PROFILING(618,python3):2025-03-06-01:09:06.978.759 [msprof_callback_impl.cpp:350] >>> (tid:618) Started to register profiling enable host freq callback.
[INFO] PROFILING(618,python3):2025-03-06-01:09:06.978.842 [prof_atls_plugin.cpp:117] (tid:618) RegisterProfileCallback, callback type is 8
[ERROR] ATRACE(618,python3):2025-03-06-01:09:06.981.451 [trace_driver_api.c:56](tid:618) get platform info failed, drvErr=87.
[INFO] RUNTIME(618,python3):2025-03-06-01:09:06.985.224 [task_fail_callback_manager.cc:52] 618 TaskFailCallBackManager: Constructor.
[INFO] HCCL(618,python3):2025-03-06-01:09:07.071.734 [adapter_rts.cc:2646][618][adapter_rts.cc][CallBackInitRts] g_deviceType [6] g_deviceLogicId [-1] g_devicePhyId [-1]
[ERROR] RUNTIME(618,python3):2025-03-06-01:09:07.260.779 [runtime.cc:1879]618 CheckHaveDevice:Call halGetDeviceInfo failed: drvRet=87, module type=0, info type=1.
[INFO] PROFILING(618,python3):2025-03-06-01:09:07.261.136 [prof_atls_plugin.cpp:210] (tid:618) Module[7] register callback of ctrl handle.
[ERROR] RUNTIME(618,python3):2025-03-06-01:09:07.262.154 [driver.cc:65]618 GetDeviceCount:Call drvGetDevNum, drvRetCode=87.
[ERROR] RUNTIME(618,python3):2025-03-06-01:09:07.262.277 [api_c_device.cc:23]618 rtGetDeviceCount:ErrCode=507899, desc=[driver error:internal error], InnerCode=0x7020010
[ERROR] RUNTIME(618,python3):2025-03-06-01:09:07.262.373 [error_message_manage.cc:53]618 FuncErrorReason:report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(618,python3):2025-03-06-01:09:07.262.459 [error_message_manage.cc:53]618 FuncErrorReason:rtGetDeviceCount execute failed, reason=[driver error:internal error]
[ERROR] ASCENDCL(618,python3):2025-03-06-01:09:07.262.594 [device.cpp:342]618 aclrtGetDeviceCount: get device count failed, runtime result = 507899.
[ERROR] APP(618,python3):2025-03-06-01:09:07.262.746 [log_inner.cpp:76]618 build/CMakeFiles/torch_npu.dir/compiler_depend.ts:device_count:25: "[PTA]:"get device count of NPU failed""


### Alternatives

_No response_

### Additional context

_No response_
