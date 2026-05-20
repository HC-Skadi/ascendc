# Issue #2629: [Bug]: Failed with inferencing Qwen3 MoE due to `Alloc sq cq fail` issue

## 基本信息

- **编号**: #2629
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2629
- **创建时间**: 2025-08-29T06:38:24Z
- **关闭时间**: 2025-08-29T07:05:26Z
- **更新时间**: 2025-08-29T07:26:10Z
- **提交者**: @shen-shanshan
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

- vllm version: `v0.9.1`
- vllm-ascend branch: `v0.9.1-dev`

> [!NOTE]
> This bug has been resolved in `main` branch, find more details at https://github.com/vllm-project/vllm-ascend/pull/2511.

### 🐛 Describe the bug

When running Qwen3 MoE with tp/dp/ep, etc., you may encounter an error just as the following:

```bash
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/torch_npu/npu/graphs.py", line 210, in capture_begin
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]     super().capture_begin(pool=pool, capture_error_mode=capture_error_mode)
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632] RuntimeError: capture_begin:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:156 NPU function error: c10_npu::acl::AclmdlRICaptureBegin(capture_stream_, capture_mode), error code is 207005
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632] [ERROR] 2025-08-05-11:23:25 (PID:519998, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632] [Error]: Failed to apply for memory.
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         Check the remaining storage space in the hardware environment.
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632] EL0006: [PID: 519998] 2025-08-05-11:23:25.691.093 The resources are insufficient.
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         Solution: Close applications not in use.
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         TraceBack (most recent call last):
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         [SqCqManage]Alloc sq cq fail, stream_id=1984, retCode=0x7020023.[FUNC:AllocStreamSqCq][FILE:stream_sqcq_manage.cc][LINE:78]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         [SqCqManage]Alloc sq cq fail, stream_id=1984, retCode=0x7020023.[FUNC:Setup][FILE:stream.cc][LINE:655]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         rtStreamBeginCapture execute failed, reason=[driver error:resource alloc fail][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         begin capture stream failed, runtime result = 207005[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         [SqCqManage]Alloc sq cq fail, stream_id=1985, retCode=0x7020023.[FUNC:AllocStreamSqCq][FILE:stream_sqcq_manage.cc][LINE:78]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         [SqCqManage]Alloc sq cq fail, stream_id=1985, retCode=0x7020023.[FUNC:Setup][FILE:stream.cc][LINE:655]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         stream setup failed, retCode=0x7020023.[FUNC:SyncGetDevMsg][FILE:api_impl.cc][LINE:6109]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         Sync get device msg failed, retCode=0x7020023.[FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:6159]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]         rtGetDevMsg execute failed, reason=[driver error:resource alloc fail][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(EngineCore_0 pid=519998) ERROR 08-05 11:23:25 [core.py:632]
```

This is more likely to happen when you're using A3. Please refer to the empirical formula below to estimate a suitable value for this argument:

```python
# pg_num: the number of process groups for communication
pg_num = sum(size > 1 for size in [
    parallel_config.data_parallel_size,
    parallel_config.tensor_parallel_size,
])
# num_hidden_layer: number of hidden layers of the model

# for A2
num_capture_sizes = (1920) / (num_hidden_layer + 1) / (1 + pg_num * 1)
# for A3
num_capture_sizes = (1920 - pg_num * 40) / (num_hidden_layer + 1) / (1 + pg_num * 2)
```

Try to adjust the arg `cuda-capture-sizes` to address this:

```bash
vllm serve ... \
--cuda-graph-sizes=num_capture_sizes
```

---
Calculate maximum supported batch sizes considering model architecture on the A2 Hardware Device.

Assume the following case:

- `MAX_CAPTURE_SIZE` = 1920
- `num_hidden_layers` = 48
- `data_parallel_size` = 1
- `tensor_parallel_size` = 4

According to the formula, `max_num_batch_sizes` = `math.floor(1920 / (48 + 1) / 2) = 19`.

---
The above describes an empirical formula applicable to the A2 hardware. Under this configuration, HCCL employs the FFTS+ method for execution unfolding, which adds only 1 concurrent stream without consuming collective communication execution unfolding streams.

On A3 hardware, HCCL defaults to the AICPU method. This approach may additionally allocate up to rank_size (max 16) - 1 streams per collective communication domain on the device (worst case). Using the default collective communication unfolding method on A3 will lead to a significant reduction in the maximum supported sizes. Therefore, the calculation formula has been modified as follows:

Assume the following case:

- `MAX_CAPTURE_SIZE` = 1920
- `num_hidden_layers` = 48
- `data_parallel_size` = 1
- `tensor_parallel_size` = 4

According to the formula, `max_num_batch_sizes` = `math.floor((1920 - 1 * 40) / (48 + 1) / (1 + 1 * 2)) = 12`.

---
