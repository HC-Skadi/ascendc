# Issue #1038: [Bug]: Failed to complete vllm benchmark after enable VLLM_USE_V1=1 due to gather_v3 error

## 基本信息

- **编号**: #1038
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1038
- **创建时间**: 2025-05-30T17:50:24Z
- **关闭时间**: 2025-06-26T01:27:45Z
- **更新时间**: 2025-08-08T01:47:51Z
- **提交者**: @Yikun
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

vLLM v0.9.0
vLLM Ascend main v0.9.0rc1.dev0531
CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1


200 prompt only 28 success, then serve crash.

RuntimeError: ACL stream synchronize failed, error code:507035 
```
[rank0]:[W530 17:44:21.455843271 compiler_depend.ts:526] Warning: NPU warning, error code is 507035[Error]:
[Error]: The vector core execution is abnormal.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 21632] 2025-05-30-17:44:21.283.810 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeUsedDevices)
[W530 17:44:21.458925982 compiler_depend.ts:508] Warning: NPU warning, error code is 507035[Error]:
[Error]: The vector core execution is abnormal.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 21632] 2025-05-30-17:44:21.287.450 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W530 17:44:21.460749068 compiler_depend.ts:151] Warning: NPU warning, error code is 507035[Error]:
[Error]: The vector core execution is abnormal.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 21632] 2025-05-30-17:44:21.289.968 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
```


<details>
<summary>Error details </summary>


```text
DumpHead: AIV-38, CoreType=AIV, block dim=40, total_block_num=40, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.1.RC1][TimeStamp : 0] /home/slave1/Ascend/8.1.RC1/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val
&& val < this->gxSize_)' Index 326 out of range[0 257)!
[rank0]:[W530 17:44:20.013492199 compiler_depend.ts:57] Warning: EZ9999: Inner Error!
EZ9999: [PID: 21632] 2025-05-30-17:44:16.563.100 The error from device(chipId:4, dieId:0), serial number is 625, there is an aivec error exception, core id is 34, error code = 0, dump inf
o: pc start: 0x1240c00c3f34, current: 0x1240c00c4e3c, vec error info: 0xeb07dd6d84, mte error info: 0x8060000d4, ifu error info: 0x709401d220ac0, ccu error info: 0xf8401fc8338000b0, cube
error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124100564000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1434]
        TraceBack (most recent call last):
       The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0x60000d4, fixp_error1 info: 0x8, fsmId:0, tslot:1, thread:0, ctxid:0, blk:38, sublk:0, subErr
Type:2.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1446]
       Kernel task happen error, retCode=0x31, [vector core exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1366]
       AIV Kernel happen error, retCode=0x31.[FUNC:GetError][FILE:stream.cc][LINE:1119]
       Aicore kernel execute failed, device_id=0, stream_id=2, report_stream_id=2, task_id=23952, flip_num=3, fault kernel_name=GatherV3_7869a97190b9b4d296d9414a005b954b_high_performance_
80330, fault kernel info ext=none, program id=22, hash=5015448876688064660.[FUNC:GetError][FILE:stream.cc][LINE:1119]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1119]
       rtStreamSynchronize execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 507035[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
 (function copy_between_host_and_device_opapi)
ERROR 05-30 17:44:20 [dump_input.py:68] Dumping input data
--- Logging error ---
Traceback (most recent call last):
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in execute_model
    return self.model_executor.execute_model(scheduler_output)
  File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 86, in execute_model
    output = self.collective_rpc("execute_model",
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/vllm-workspace/vllm/vllm/utils.py", line 2605, in run_method
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 175, in execute_model
    output = self.model_runner.execute_model(scheduler_output)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 958, in execute_model
    valid_sampled_token_ids = sampled_token_ids.tolist()
RuntimeError: ACL stream synchronize failed, error code:507035

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/logging/__init__.py", line 1100, in emit
    msg = self.format(record)
  File "/usr/local/python3.10.17/lib/python3.10/logging/__init__.py", line 943, in format
    return fmt.format(record)
  File "/vllm-workspace/vllm/vllm/logging_utils/formatter.py", line 13, in format
    msg = logging.Formatter.format(self, record)
  File "/usr/local/python3.10.17/lib/python3.10/logging/__init__.py", line 678, in format
    record.message = record.getMessage()
  File "/usr/local/python3.10.17/lib/python3.10/logging/__init__.py", line 368, in getMessage
    msg = msg % self.args
  File "/vllm-workspace/vllm/vllm/config.py", line 4476, in __str__
    f"model={self.model_config.model!r},"
  File "/vllm-workspace/vllm/vllm/config.py", line 3896, in __repr__
    for k, v in asdict(self).items():
  File "/usr/local/python3.10.17/lib/python3.10/dataclasses.py", line 1238, in asdict
    return _asdict_inner(obj, dict_factory)
  File "/usr/local/python3.10.17/lib/python3.10/dataclasses.py", line 1245, in _asdict_inner
    value = _asdict_inner(getattr(obj, f.name), dict_factory)
  File "/usr/local/python3.10.17/lib/python3.10/dataclasses.py", line 1275, in _asdict_inner
    return type(obj)((_asdict_inner(k, dict_factory),
  File "/usr/local/python3.10.17/lib/python3.10/dataclasses.py", line 1276, in <genexpr>
    _asdict_inner(v, dict_factory))
  File "/usr/local/python3.10.17/lib/python3.10/dataclasses.py", line 1279, in _asdict_inner
    return copy.deepcopy(obj)
  File "/usr/local/python3.10.17/lib/python3.10/copy.py", line 172, in deepcopy
    y = _reconstruct(x, memo, *rv)
  File "/usr/local/python3.10.17/lib/python3.10/copy.py", line 273, in _reconstruct
    y.__setstate__(state)
  File "/vllm-workspace/vllm/vllm/compilation/torch25_custom_graph_pass.py", line 39, in __setstate__
    raise ValueError("Cannot unpickle CustomGraphPass because pickling"
ValueError: Cannot unpickle CustomGraphPass because pickling is used for cache key uuid. Use torch>=2.6 with native uuid support for custom passes.

Call stack:
  File "<string>", line 1, in <module>
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/spawn.py", line 129, in _main
    return self._bootstrap(parent_sentinel)
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 493, in run_engine_core
    engine_core.run_busy_loop()
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 520, in run_busy_loop
    self._process_engine_step()
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 545, in _process_engine_step
    outputs = self.step_fn()
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 226, in step
    model_output = self.execute_model(scheduler_output)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 210, in execute_model
    dump_engine_exception(self.vllm_config, scheduler_output,
  File "/vllm-workspace/vllm/vllm/logging_utils/dump_input.py", line 62, in dump_engine_exception
    _dump_engine_exception(config, scheduler_output, scheduler_stats)
  File "/vllm-workspace/vllm/vllm/logging_utils/dump_input.py", line 70, in _dump_engine_exception
    logger.error(
Unable to print the message and arguments - possible formatting error.

ERROR 05-30 17:44:20 [dump_input.py:78] Dumping scheduler output for model execution:
ERROR 05-30 17:44:20 [dump_input.py:79] SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=cmpl-5ec410889eb64440b81e6dd1f69da459-0,prompt_token_ids_len=200,mm_inputs=[],mm_hashes=[
],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=
[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True,
 spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=[[87, 88]],num_computed_tokens=0,lora_request=None)], scheduled_cached_r
eqs=[CachedRequestData(req_id='cmpl-e9ba85e2ac3a49368a04f2c368491dca-0', resumed_from_preemption=false, new_token_ids=[26547], new_block_ids=[[86]], num_computed_tokens=256)], num_schedul
ed_tokens={cmpl-5ec410889eb64440b81e6dd1f69da459-0: 200, cmpl-e9ba85e2ac3a49368a04f2c368491dca-0: 1}, total_num_scheduled_tokens=201, scheduled_spec_decode_tokens={}, scheduled_encoder_in
puts={}, num_common_prefix_blocks=[0], finished_req_ids=[], free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
ERROR 05-30 17:44:20 [core.py:502] EngineCore encountered a fatal error.
ERROR 05-30 17:44:20 [core.py:502] Traceback (most recent call last):
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 493, in run_engine_core
ERROR 05-30 17:44:20 [core.py:502]     engine_core.run_busy_loop()
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 520, in run_busy_loop
ERROR 05-30 17:44:20 [core.py:502]     self._process_engine_step()
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 545, in _process_engine_step
ERROR 05-30 17:44:20 [core.py:502]     outputs = self.step_fn()
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 226, in step
ERROR 05-30 17:44:20 [core.py:502]     model_output = self.execute_model(scheduler_output)
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 213, in execute_model
ERROR 05-30 17:44:20 [core.py:502]     raise err
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in execute_model
ERROR 05-30 17:44:20 [core.py:502]     return self.model_executor.execute_model(scheduler_output)
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 86, in execute_model
ERROR 05-30 17:44:20 [core.py:502]     output = self.collective_rpc("execute_model",
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 05-30 17:44:20 [core.py:502]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm/vllm/utils.py", line 2605, in run_method
ERROR 05-30 17:44:20 [core.py:502]     return func(*args, **kwargs)
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 175, in execute_model
ERROR 05-30 17:44:20 [core.py:502]     output = self.model_runner.execute_model(scheduler_output)
ERROR 05-30 17:44:20 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 05-30 17:44:20 [core.py:502]     return func(*args, **kwargs)
ERROR 05-30 17:44:20 [core.py:502]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 958, in execute_model
ERROR 05-30 17:44:20 [core.py:502]     valid_sampled_token_ids = sampled_token_ids.tolist()
ERROR 05-30 17:44:20 [core.py:502] RuntimeError: ACL stream synchronize failed, error code:507035
ERROR 05-30 17:44:20 [async_llm.py:408] AsyncLLM output_handler failed.
ERROR 05-30 17:44:20 [async_llm.py:408] Traceback (most recent call last):
ERROR 05-30 17:44:20 [async_llm.py:408]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 366, in output_handler
ERROR 05-30 17:44:20 [async_llm.py:408]     outputs = await engine_core.get_output_async()
ERROR 05-30 17:44:20 [async_llm.py:408]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 806, in get_output_async
ERROR 05-30 17:44:20 [async_llm.py:408]     raise self._format_exception(outputs) from None
ERROR 05-30 17:44:20 [async_llm.py:408] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [21326]
[rank0]:[W530 17:44:21.455843271 compiler_depend.ts:526] Warning: NPU warning, error code is 507035[Error]:
[Error]: The vector core execution is abnormal.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 21632] 2025-05-30-17:44:21.283.810 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeUsedDevices)
[W530 17:44:21.458925982 compiler_depend.ts:508] Warning: NPU warning, error code is 507035[Error]:
[Error]: The vector core execution is abnormal.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 21632] 2025-05-30-17:44:21.287.450 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W530 17:44:21.460749068 compiler_depend.ts:151] Warning: NPU warning, error code is 507035[Error]:
[Error]: The vector core execution is abnormal.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 21632] 2025-05-30-17:44:21.289.968 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
```

</details>


### 🐛 Describe the bug
0. Run image
```
# Update DEVICE according to your device (/dev/davinci[0-7])
export DEVICE=/dev/davinci4
# Update the vllm-ascend image
#export IMAGE=m.daocloud.io/quay.io/ascend/cann:8.1.rc1-910b-ubuntu22.04-py3.10
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:main
docker run --rm \
--name yikun-test \
--device $DEVICE \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-it $IMAGE bash
```
2. start server
```
export MODEL=Qwen/Qwen2.5-7B-Instruct
export VLLM_USE_MODELSCOPE=true
VLLM_USE_V1=1 VLLM_USE_MODELSCOPE=true python3 -m vllm.entrypoints.openai.api_server --model $MODEL \
         --tensor-parallel-size 1 --swap-space 16 --disable-log-stats \
         --disable-log-requests  --load-format dummy
```

2. Run test
```
export MODEL=Qwen/Qwen2.5-7B-Instruct
export VLLM_USE_MODELSCOPE=true
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
pip install -r /vllm-workspace/vllm-ascend/benchmarks/requirements-bench.txt
python3 /vllm-workspace/vllm/benchmarks/benchmark_serving.py --model $MODEL --dataset-name random \
         --random-input-len 200 --num-prompts 200 --request-rate 1 \
         --save-result --result-dir ./
```

3. Server crashed at 29/200. only 28/200 pass
