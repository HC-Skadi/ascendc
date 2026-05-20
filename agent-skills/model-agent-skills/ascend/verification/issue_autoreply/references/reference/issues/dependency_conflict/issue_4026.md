# Issue #4026: v0.11.0rc0-310p拉起qwen vl 8B 报错 EL0004: [PID: 14004] 2025-11-06-01:17:59.527.855 Failed to allocate memory.

## 基本信息

- **编号**: #4026
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4026
- **创建时间**: 2025-11-06T06:20:36Z
- **关闭时间**: 2025-12-23T11:19:42Z
- **更新时间**: 2025-12-23T11:19:42Z
- **提交者**: @ZCG12345
- **评论数**: 1

## 标签

bug; 310p

## 问题描述

### Your current environment

е_
Trank0]:TW1106 01:17:59.109644239 compiler depend.ts:62] Warning: Cannot create tensor with NZ format while dim < 2, tensor will be created with ND format. (function operatorO)
(ОJ03еJado uoTouny) "qеwJ0J ON 44TM раqеаuo aq 17TM Josu91 7 > wTp alTUM qеwJoJ ZN 44TM Josu9q a1e8Jo 20uue] :buTuueM [Z9:53 puadap JalT0W00 2S7£L62TT16S:LT:TO 9OTTM]:[TYueJ]
[rank2]:[W1106 01:17:59.125572526 compiler depend.ts:62] Warning: Cannot create tensor with NZ format while dim < 2, tensor will be created with ND format. (function operator())
0и03елеdо иоToиnд)  деши0д ОN 47TM разеаuo aq 77TM J0su94 7 > wTp 32TUM 3еwJ0J ZN 43TM J0su94 а99903 30uueg :buTuueM 179:57 puadep Ja2T0W03 997££797T 69:£T:T0 90TTM: £Yueu1
(Worker_TPO pid=14084) ERROR 11-06 01:18:00 (multiproc_executor.py:671] WorkerProc hit an exception.
(Worker TPB pid=14004) ERROR 11-06 01:18:00 (multiproc_executor.py:671] Traceback (most recent call Last):
(Worker_TPO pid=14084) ERROR 11-06 01:18:08 (multiproc_executor.py:671]  1	File "/vLLm-workspace/vLlm/vLlm/v1/executor/multiproc executor py", Line 666, in worker_busy_Loop
(Worker_TPO pid=14004) ERROR 11-06 01:18:00 [multiproc_executor.py:671]	output = func(*args, **kwargs
(Worker_TPO pid=14004) ERROR 11-06 01:18:00 [multiproc_executor.py:671]	VVVvvvvvvvvvvvvvvvvvv
(Worker_TPO pid=14804) ERROR 11-06 01:18:00	[multiproc executor.py:671]	File "/vLLm-workspace/vLLm/vLLm/worker/worker base.py", Line 254, in initialize_from_config
(Worker_TPO pid=14004) ERROR 11-06 01:18:00	multiproc executor.py:671	self.worker.initialize_from_config(kv_cache_config) # type: ignore
(Worker TPO pid=14004)	ERROR 11-06 01:18:00	[multiproc_executor.py:671	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^AA^^^A^^^^^^^^ΛAAAAAA
(Worker_TPO pid=14804) ERROR 11-06 01:18:00	multiproc executor.py:671	File "/vUlm-workspace/vLlm ascend/vLlm ascend/worker/worker vi.py", Line 336, in initialize_from_config
(Worker_TPO pid=14004)	ERROR 11-06 01:18:00	[multiproc_executor.py:671	self.model_runner.initialize_kv_cache(kv_cache_config
(Worker_TPO pid=14004) ERROR 11-06 01:18:00	[multiproc executor.py:671	File "/vLlm-workspace/v17m-ascend/v17m ascend/worker/model runner V1.py”, Line 2709, in initialize kv cache
(Worker_TPO pid=14804) ERROR 11-06 01:18:00	multiproc executor.py:671	kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(Worker_TPO pid=14884) ERROR 11-06 01:18:00	[multiproc executor.py:671	^^^^^^^^^^^^^^^^^^^^^^^^^^A^A^^^AA^^^^^A^^Λ^A^^AA的
(Worker_TPO pid=14004) ERROR 11-06 01:18:00	multiproc executor.py:671	File "/vLLm-workspace/vLLm-ascend/vLlm ascend/worker/model_runner_v1.py", Line 3043, in initialize_kv_cache_tensors
(Worker TPB pid=14004) ERROR 11-06 01:18:00	[multiproc_executor.py:671	k_cache = self._convert torch format(k_cache)
(Worker_TPO pid=14804) ERROR 11-06 01:18:00	(multiproc executor.py:671	VVVVVVVVVVVVVVVVVVVVvvvvvvvvvvvvvvv
(Worker_TPO pid=14004) ERROR 11-06 01:18:00	[multiproc executor.py:671	File "/vLLm-workspace/vLlm-ascend/vllm ascend/worker/model runner vi.py", Line 2673, in _convert_torch_format
(Worker_TPB pid=14004) ERROR 11-06 01:18:00	multiproc_executor.py:671	tensor = torch_npu.npu format_cast(tensor, ACL_FORMAT)
(Worker_TPB pid=14004) ERROR 11-06 01:18:00	multiproc executor.py:671	^^^^^^^^^^^^^^^^^^^^^AAAAAAAAAAA^^^Λ^^^^^^AΛA的
(Worker TPB pid=14004) ERROR 11-06 01:18:00	multiproc executor.py:671	File "/usr/Local/python3.11.13/Lib/python3.11/site-packages/torch/ ops.py", Line 1158, in __call
(Worker TPB pid=14084) ERROR 11-06 01:18:00	multiproc executor.py:671	return self._op(*args, **(kwargs or {}))
(Worker_TPB pid=14004) ERROR 11-06 01:18:00	multiproc executor.py:671	^^^^^^^^^^^^^^^^A^A^ΑA^^^^^^^AAAA
(Worker TP8 pid=14004) ERROR 11-06 01:18:00	[multiproc executor.py:671	RuntimeError: npuSynchronizeDevice:build/CMakeFiles/torch npu.dir/compiler depend.ts:508 NPU function error: AcLrtSynchronizeDeviceWithTim
eout, error code is 507013
(Worker_TPB pid=14804) ERROR 11-06 01:18:00 [multiproc_executor.py:671]	ERROR] 2025-11-06-01:18:00 (PID:14004, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(Worker_TPO pid=14004) ERROR 11-06 01:18:00 [multiproc_executor.py:671	[Error]: System Direct Memory Access (DMA) hardware execution error.
(Worker_TPO pid=14804) ERROR 11-06 01:18:00	[multiproc executor.py:671	Rectify the fault based on the error information in the ascend log.
(Worker_TPO pid=14004) ERROR 11-06 01:18:00	[multiproc_executor.py:671)	EL0004: [PID: 14004] 2025-11-06-01:17:59.527.855 Failed to allocate memory.
(Worker_TPO pid=14004) ERROR 11-06 01:18:00	[multiproc_executor.py:671	Possible Cause: Available memory is insufficient.
(Worker_TPO pid=14004) ERROR 11-06 01:18:00	[multiproc executor.py:671	Solution: Close applications not in use.
(Worker TPB pid=14004) ERROR 11-06 01:18:00	[multiproc_executor.py:671	TraceBack (most recent call last):
(Worker_TPO pid=14004) ERROR 11-06 01:18:00 [multiproc_executor.py:671	alloc device memory failed, runtime result = 207001 FUNC:ReportCallError [FILE:Log inner.cpp][LINE:1611
(Worker TPO pid=14884) ERROR 11-06 01:18:00 [multiproc_executor.py:671)	The error from device(O), serial number is 6. there is a sdma error, sdma channel is O, the channel exist the following problems:
The SMMU returns a Terminate error during page table translation.. the value of COE status is 2. the description of COE status: When the SOE translates a page table, the SMMU returns a Terminate error.it's confr
ig include: setting1=Oxc000000880e0000, setting2=Oxff009000ff004c, setting3=0, sq base addr=Ox800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
(Worker TPO pid=14004) ERROR 11-06 01:18:00 [multiproc executor.py:671)	Memory async copy failed, device_id=0, stream_id=42, task_id=1690, flip_num=O, copy_type=2, memcpy_type=O, copy_data_type=O, lengt
h=959971328[FUNC:GetError][FILE:stream.cc][LINE :1183]
(Worker_TPO pid=14804) ERROR 11-06 01:18:00 [multiproc_executor.py:671]	rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:5

### 🐛 Describe the bug

拉起qwen-vl-8b报错 报错 EL0004: [PID: 14004] 2025-11-06-01:17:59.527.855 Failed to allocate memory Error]: System Direct Memory Access (DMA) hardware execution error.
