# Issue #2542: [Bug]: Can 310p start two VLLM services on one card?

## 基本信息

- **编号**: #2542
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2542
- **创建时间**: 2025-08-26T05:54:12Z
- **关闭时间**: 2025-12-23T11:33:01Z
- **更新时间**: 2025-12-23T11:33:01Z
- **提交者**: @shaojun0
- **评论数**: 1

## 标签

bug; 310p

## 问题描述

### Your current environment

```yaml
services:
  bge_detail:
    image: quay.nju.edu.cn/ascend/vllm-ascend:v0.9.2rc1-310p
    container_name: idms-bge-detail
    user: root
#    ports:
#      - "8093:80"
    devices:
      - "/dev/davinci5"
      - "/dev/davinci_manager"
      - "/dev/devmm_svm"
      - "/dev/hisi_hdc"
    volumes:
      - "/usr/local/dcmi:/usr/local/dcmi"
      - "/usr/local/bin/npu-smi:/usr/local/bin/npu-smi"
      - "/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64"
      - "/usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info"
      - "/etc/ascend_install.info:/etc/ascend_install.info"
      - "${DOCKER_VOLUME_DIRECTORY:-.}/bge:/data/model"
    command: ["python3","-m","vllm.entrypoints.openai.api_server","--enforce-eager","--gpu-memory-utilization","0.3","--served-model-name", "bge-detail","--model","/data/model/detail"]

  bge_experience:
    image: quay.nju.edu.cn/ascend/vllm-ascend:v0.9.2rc1-310p
    container_name: idms-bge-experience
    user: root
#    ports:
#      - "8094:80"
    devices:
      - "/dev/davinci5"
      - "/dev/davinci_manager"
      - "/dev/devmm_svm"
      - "/dev/hisi_hdc"
    volumes:
      - "/usr/local/dcmi:/usr/local/dcmi"
      - "/usr/local/bin/npu-smi:/usr/local/bin/npu-smi"
      - "/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64"
      - "/usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info"
      - "/etc/ascend_install.info:/etc/ascend_install.info"
      - "${DOCKER_VOLUME_DIRECTORY:-.}/bge:/data/model"
    command: ["python3","-m","vllm.entrypoints.openai.api_server","--enforce-eager","--gpu-memory-utilization","0.3","--served-model-name", "experience","--model","/data/model/experience"]
```

### 🐛 Describe the bug

One runs normally, while the other exports with the following error
```shell
INFO 08-26 03:01:16 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.2) with config: model='/data/model/experience', speculative_config=None, tokenizer='/data/model/experience', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=experience, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=False, pooler_config=PoolerConfig(pooling_type='CLS', normalize=True, softmax=None, step_tag_id=None, returned_token_ids=None), compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":0,"local_cache_dir":null}, use_cached_outputs=True, 

[INFO] PROFILING(278,python3):2025-08-26-03:01:17.471.601 [prof_atls_plugin.cpp:210] (tid:278) Module[6] register callback of ctrl handle.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.531.574 [runtime_keeper.cc:66]278 GetDeviceType:Call halGetDeviceInfo failed: drvRet=87, module type=0, info type=1.

[INFO] RUNTIME(278,python3):2025-08-26-03:01:17.534.896 [runtime_keeper.cc:149] 278 CreateRuntimeImpl: Open libruntime_v100.so success

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.584.694 [runtime.cc:1380]278 CheckHaveDevice:Call halGetDeviceInfo failed: drvRet=87, module type=0, info type=1.

[INFO] PROFILING(278,python3):2025-08-26-03:01:17.585.553 [prof_atls_plugin.cpp:210] (tid:278) Module[7] register callback of ctrl handle.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.585.680 [driver.cc:65]278 GetDeviceCount:Call drvGetDevNum, drvRetCode=87.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.585.749 [api_c_device.cc:23]278 rtGetDeviceCount:ErrCode=507899, desc=[driver error:internal error], InnerCode=0x7020010

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.585.804 [error_message_manage.cc:53]278 FuncErrorReason:report error module_type=3, module_name=EE8888

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.585.856 [error_message_manage.cc:53]278 FuncErrorReason:rtGetDeviceCount execute failed, reason=[driver error:internal error]

[ERROR] DVPP(278,python3):2025-08-26-03:01:17.585.932 [PlatformInfo.cpp:37][DVPP] [GetHardwareVersion:37] [T2] get device num fail. ret = 507899

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.586.816 [driver.cc:65]278 GetDeviceCount:Call drvGetDevNum, drvRetCode=87.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.586.883 [api_c_device.cc:23]278 rtGetDeviceCount:ErrCode=507899, desc=[driver error:internal error], InnerCode=0x7020010

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.586.935 [error_message_manage.cc:53]278 FuncErrorReason:report error module_type=3, module_name=EE8888

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.586.987 [error_message_manage.cc:53]278 FuncErrorReason:rtGetDeviceCount execute failed, reason=[driver error:internal error]

[ERROR] DVPP(278,python3):2025-08-26-03:01:17.587.051 [PlatformInfo.cpp:37][DVPP] [GetHardwareVersion:37] [T2] get device num fail. ret = 507899

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.587.916 [driver.cc:65]278 GetDeviceCount:Call drvGetDevNum, drvRetCode=87.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.587.983 [api_c_device.cc:23]278 rtGetDeviceCount:ErrCode=507899, desc=[driver error:internal error], InnerCode=0x7020010

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.588.035 [error_message_manage.cc:53]278 FuncErrorReason:report error module_type=3, module_name=EE8888

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.588.085 [error_message_manage.cc:53]278 FuncErrorReason:rtGetDeviceCount execute failed, reason=[driver error:internal error]

[ERROR] DVPP(278,python3):2025-08-26-03:01:17.588.147 [PlatformInfo.cpp:37][DVPP] [GetHardwareVersion:37] [T2] get device num fail. ret = 507899

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.589.022 [driver.cc:65]278 GetDeviceCount:Call drvGetDevNum, drvRetCode=87.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.589.088 [api_c_device.cc:23]278 rtGetDeviceCount:ErrCode=507899, desc=[driver error:internal error], InnerCode=0x7020010

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.589.141 [error_message_manage.cc:53]278 FuncErrorReason:report error module_type=3, module_name=EE8888

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:17.589.192 [error_message_manage.cc:53]278 FuncErrorReason:rtGetDeviceCount execute failed, reason=[driver error:internal error]

[ERROR] DVPP(278,python3):2025-08-26-03:01:17.589.254 [PlatformInfo.cpp:37][DVPP] [GetHardwareVersion:37] [T2] get device num fail. ret = 507899

[ERROR] TBE(278,python3):2025-08-26-03:01:17.592.424 [ascendc_runtime.cpp:232]  278 AscendCheckSoCVersion:cur soc version unknowsoctype not found.

[INFO] PROFILING(278,python3):2025-08-26-03:01:17.631.727 [prof_atls_plugin.cpp:210] (tid:278) Module[45] register callback of ctrl handle.

[INFO] GE(278,python3):2025-08-26-03:01:17.780.261 [op_tiling_manager.cc:109]278 ~FuncPerfScope:[GEPERFTRACE] The time cost of OpTilingManager::LoadSo is [148444] micro seconds.

[INFO] IDEDD(278,python3):2025-08-26-03:01:18.161.658 [adx_dump_record.cpp:629][tid:349] start dump thread, remote dump record temp path : /workspace/.

[INFO] IDEDD(278,python3):2025-08-26-03:01:18.161.750 [adx_server_manager.cpp:203][tid:350] Run Server(0) Process

[ERROR] IDEDD(278,python3):2025-08-26-03:01:18.162.022 [adx_dsmi.cpp:54][tid:350] Get physical device number failed, err: 87

[INFO] PROFILING(278,python3):2025-08-26-03:01:18.163.307 [prof_atls_plugin.cpp:210] (tid:278) Module[48] register callback of ctrl handle.

[EVENT] PROFILING(278,python3):2025-08-26-03:01:18.163.429 [msprof_callback_impl.cpp:110] >>> (tid:278) MsprofCtrlCallback called, type: 255

[EVENT] PROFILING(278,python3):2025-08-26-03:01:18.164.616 [ai_drv_dev_api.cpp:333] >>> (tid:278) Succeeded to DrvGetApiVersion version: 0x72318

[ERROR] PROFILING(278,python3):2025-08-26-03:01:18.166.038 [ai_drv_dev_api.cpp:78] >>> (tid:278) Failed to drvGetPlatformInfo, ret=87

[ERROR] PROFILING(278,python3):2025-08-26-03:01:18.166.955 [config_manager.cpp:60] >>> (tid:278) halGetDeviceInfo get device type version failed , ret:87

[ERROR] ASCENDCL(278,python3):2025-08-26-03:01:18.167.116 [acl.cpp:370]278 aclInit: [INIT][DEFAULT][Init][Version]init soc version failed, ret = 507008

[INFO] RUNTIME(278,python3):2025-08-26-03:01:18.167.925 [api_impl.cc:7464] 278 PeekLastErr: level=0 err=507008.

[INFO] RUNTIME(278,python3):2025-08-26-03:01:18.168.019 [api_impl.cc:7464] 278 PeekLastErr: level=0 err=507008.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:18.168.214 [api_impl.cc:5925]278 GetDevErrMsg:report error module_type=3, module_name=EE8888

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:18.168.272 [api_impl.cc:5925]278 GetDevErrMsg:ctx is NULL!

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:18.168.341 [api_impl.cc:6001]278 GetDevMsg:Failed to GetDeviceErrMsg, retCode=0x7070001.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:18.168.393 [api_error.cc:3864]278 GetDevMsg:GetDeviceMsg failed, getMsgType=0.

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:18.168.447 [api_c_device.cc:450]278 rtGetDevMsg:ErrCode=107002, desc=[context pointer null], InnerCode=0x7070001

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:18.168.496 [error_message_manage.cc:48]278 FuncErrorReason:report error module_name=EE1001

[ERROR] RUNTIME(278,python3):2025-08-26-03:01:18.168.546 [error_message_manage.cc:48]278 FuncErrorReason:rtGetDevMsg execute failed, reason=[context pointer null]

ERROR 08-26 03:01:18 [engine.py:458] GetDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:68 NPU function error: aclrtGetCurrentContext(&used_devices[local_device]), error code is 107002

ERROR 08-26 03:01:18 [engine.py:458] [ERROR] 2025-08-26-03:01:18 (PID:278, Device:0, RankID:-1) ERR00100 PTA call acl api failed

ERROR 08-26 03:01:18 [engine.py:458] [Error]: The context is empty.

Process SpawnProcess-1:

ERROR 08-26 03:01:18 [engine.py:458]         Check whether acl.rt.set_context or acl.rt.set_device is called.

ERROR 08-26 03:01:18 [engine.py:458] EL0005: [PID: 278] 2025-08-26-03:01:17.531.512 The resources are busy.

ERROR 08-26 03:01:18 [engine.py:458]         Possible Cause: 1. The resources have been occupied. 2. The device is being reset. 3. Software is not ready.

ERROR 08-26 03:01:18 [engine.py:458]         Solution: 1. Close applications not in use. 2. Wait for a while and try again.

ERROR 08-26 03:01:18 [engine.py:458]         TraceBack (most recent call last):

ERROR 08-26 03:01:18 [engine.py:458]         rtGetDeviceCount execute failed, reason=[driver error:internal error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]

ERROR 08-26 03:01:18 [engine.py:458]         Failed to drvGetPlatformInfo, ret=87[FUNC:DrvGetPlatformInfo][FILE:ai_drv_dev_api.cpp][LINE:79]

ERROR 08-26 03:01:18 [engine.py:458]         halGetDeviceInfo get device type version failed , ret:87[FUNC:Init][FILE:config_manager.cpp][LINE:61]

ERROR 08-26 03:01:18 [engine.py:458]         [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

ERROR 08-26 03:01:18 [engine.py:458]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]

ERROR 08-26 03:01:18 [engine.py:458]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]

ERROR 08-26 03:01:18 [engine.py:458] Traceback (most recent call last):

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 446, in run_mp_engine

ERROR 08-26 03:01:18 [engine.py:458]     engine = MQLLMEngine.from_vllm_config(

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 133, in from_vllm_config

ERROR 08-26 03:01:18 [engine.py:458]     return cls(

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 87, in __init__

ERROR 08-26 03:01:18 [engine.py:458]     self.engine = LLMEngine(*args, **kwargs)

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 265, in __init__

ERROR 08-26 03:01:18 [engine.py:458]     self.model_executor = executor_class(vllm_config=vllm_config)

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__

ERROR 08-26 03:01:18 [engine.py:458]     self._init_executor()

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 47, in _init_executor

ERROR 08-26 03:01:18 [engine.py:458]     self.collective_rpc("init_device")

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 57, in collective_rpc

ERROR 08-26 03:01:18 [engine.py:458]     answer = run_method(self.driver_worker, method, args, kwargs)

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2736, in run_method

ERROR 08-26 03:01:18 [engine.py:458]     return func(*args, **kwargs)

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 606, in init_device

ERROR 08-26 03:01:18 [engine.py:458]     self.worker.init_device()  # type: ignore

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 216, in init_device

ERROR 08-26 03:01:18 [engine.py:458]     NPUPlatform.set_device(self.device)

ERROR 08-26 03:01:18 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 98, in set_device

ERROR 08-26 03:01:18 [engine.py:458]     torch.npu.set_device(device)

ERROR 08-26 03:01:18 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 80, in set_device

ERROR 08-26 03:01:18 [engine.py:458]     torch_npu._C._npu_setDevice(device_id)

ERROR 08-26 03:01:18 [engine.py:458] RuntimeError: GetDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:68 NPU function error: aclrtGetCurrentContext(&used_devices[local_device]), error code is 107002

ERROR 08-26 03:01:18 [engine.py:458] [ERROR] 2025-08-26-03:01:18 (PID:278, Device:0, RankID:-1) ERR00100 PTA call acl api failed

ERROR 08-26 03:01:18 [engine.py:458] [Error]: The context is empty.

ERROR 08-26 03:01:18 [engine.py:458]         Check whether acl.rt.set_context or acl.rt.set_device is called.

ERROR 08-26 03:01:18 [engine.py:458] EL0005: [PID: 278] 2025-08-26-03:01:17.531.512 The resources are busy.

ERROR 08-26 03:01:18 [engine.py:458]         Possible Cause: 1. The resources have been occupied. 2. The device is being reset. 3. Software is not ready.

ERROR 08-26 03:01:18 [engine.py:458]         Solution: 1. Close applications not in use. 2. Wait for a while and try again.

ERROR 08-26 03:01:18 [engine.py:458]         TraceBack (most recent call last):

ERROR 08-26 03:01:18 [engine.py:458]         rtGetDeviceCount execute failed, reason=[driver error:internal error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]

ERROR 08-26 03:01:18 [engine.py:458]         Failed to drvGetPlatformInfo, ret=87[FUNC:DrvGetPlatformInfo][FILE:ai_drv_dev_api.cpp][LINE:79]

ERROR 08-26 03:01:18 [engine.py:458]         halGetDeviceInfo get device type version failed , ret:87[FUNC:Init][FILE:config_manager.cpp][LINE:61]

ERROR 08-26 03:01:18 [engine.py:458]         [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

ERROR 08-26 03:01:18 [engine.py:458]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]

ERROR 08-26 03:01:18 [engine.py:458]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]

ERROR 08-26 03:01:18 [engine.py:458]
```
