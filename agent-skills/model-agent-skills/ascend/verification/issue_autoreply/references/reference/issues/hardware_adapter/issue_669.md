# Issue #669: [Misc]:

## 基本信息

- **编号**: #669
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/669
- **创建时间**: 2025-04-27T01:43:38Z
- **关闭时间**: 2025-04-27T08:07:49Z
- **更新时间**: 2025-04-27T08:07:53Z
- **提交者**: @Jerryhuang0415
- **评论数**: 1

## 标签

duplicate

## 问题描述

### Anything you want to discuss about vllm on ascend.

运行 Llama4报以下错误，使用参数为
vllm serve /data/model/Llama4  --host 0.0.0.0 --port 8005 --tensor-parallel-size 8 --gpu-memory-utilization 0.9 --cpu-offload-gb 128 --swap-space 8 --pipeline-parallel-size 1 --max-model-len 8192
VLLM_USE_V1=1
ASCEND_RT_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"
, 'psm_15c454b4'), local_subscribe_addr='ipc:///tmp/623f8001-9b3a-46d9-bb85-44eb55ed739b', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=7 pid=2159) INFO 04-27 01:29:44 [parallel_state.py:959] rank 7 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 7
(VllmWorker rank=6 pid=1911) INFO 04-27 01:29:44 [parallel_state.py:959] rank 6 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 6
(VllmWorker rank=5 pid=1663) INFO 04-27 01:29:44 [parallel_state.py:959] rank 5 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 5
(VllmWorker rank=4 pid=1415) INFO 04-27 01:29:44 [parallel_state.py:959] rank 4 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 4
(VllmWorker rank=3 pid=1170) INFO 04-27 01:29:44 [parallel_state.py:959] rank 3 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 3
(VllmWorker rank=1 pid=891) INFO 04-27 01:29:44 [parallel_state.py:959] rank 1 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 1
(VllmWorker rank=2 pid=921) INFO 04-27 01:29:44 [parallel_state.py:959] rank 2 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 2
(VllmWorker rank=0 pid=872) INFO 04-27 01:29:44 [parallel_state.py:959] rank 0 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 0
(VllmWorker rank=5 pid=1663) INFO 04-27 01:29:53 [model_runner_v1.py:864] Starting to load model /data/model/Llama4...
(VllmWorker rank=2 pid=921) INFO 04-27 01:29:53 [model_runner_v1.py:864] Starting to load model /data/model/Llama4...
(VllmWorker rank=5 pid=1663) INFO 04-27 01:29:53 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512] is overridden by config [512, 384, 256, 128, 4, 2, 1, 392, 264, 136, 8, 400, 272, 144, 16, 408, 280, 152, 24, 416, 288, 160, 32, 424, 296, 168, 40, 432, 304, 176, 48, 440, 312, 184, 56, 448, 320, 192, 64, 456, 328, 200, 72, 464, 336, 208, 80, 472, 344, 216, 88, 120, 480, 352, 248, 224, 96, 488, 504, 360, 232, 104, 496, 368, 240, 112, 376]
(VllmWorker rank=5 pid=1663) WARNING 04-27 01:29:53 [platform.py:129] NPU compilation support pending. Will be available in future CANN and torch_npu releases. Using default: enforce_eager=True
(VllmWorker rank=5 pid=1663) INFO 04-27 01:29:53 [platform.py:134] Compilation disabled, using eager mode by default
(VllmWorker rank=2 pid=921) INFO 04-27 01:29:53 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512] is overridden by config [512, 384, 256, 128, 4, 2, 1, 392, 264, 136, 8, 400, 272, 144, 16, 408, 280, 152, 24, 416, 288, 160, 32, 424, 296, 168, 40, 432, 304, 176, 48, 440, 312, 184, 56, 448, 320, 192, 64, 456, 328, 200, 72, 464, 336, 208, 80, 472, 344, 216, 88, 120, 480, 352, 248, 224, 96, 488, 504, 360, 232, 104, 496, 368, 240, 112, 376]
(VllmWorker rank=2 pid=921) WARNING 04-27 01:29:53 [platform.py:129] NPU compilation support pending. Will be available in future CANN and torch_npu releases. Using default: enforce_eager=True
(VllmWorker rank=2 pid=921) INFO 04-27 01:29:53 [platform.py:134] Compilation disabled, using eager mode by default
(VllmWorker rank=0 pid=872) INFO 04-27 01:29:53 [model_runner_v1.py:864] Starting to load model /data/model/Llama4...
(VllmWorker rank=0 pid=872) INFO 04-27 01:29:53 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512] is overridden by config [512, 384, 256, 128, 4, 2, 1, 392, 264, 136, 8, 400, 272, 144, 16, 408, 280, 152, 24, 416, 288, 160, 32, 424, 296, 168, 40, 432, 304, 176, 48, 440, 312, 184, 56, 448, 320, 192, 64, 456, 328, 200, 72, 464, 336, 208, 80, 472, 344, 216, 88, 120, 480, 352, 248, 224, 96, 488, 504, 360, 232, 104, 496, 368, 240, 112, 376]
(VllmWorker rank=0 pid=872) WARNING 04-27 01:29:53 [platform.py:129] NPU compilation support pending. Will be available in future CANN and torch_npu releases. Using default: enforce_eager=True
(VllmWorker rank=0 pid=872) INFO 04-27 01:29:53 [platform.py:134] Compilation disabled, using eager mode by default
(VllmWorker rank=7 pid=2159) INFO 04-27 01:29:53 [model_runner_v1.py:864] Starting to load model /data/model/Llama4...
CRITICAL 04-27 01:29:53 [multiproc_executor.py:49] MulitprocExecutor got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
CRITICAL 04-27 01:29:53 [core_client.py:359] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
(VllmWorker rank=5 pid=1663) Exception ignored in: <Finalize object, dead>
(VllmWorker rank=5 pid=1663) Traceback (most recent call last):
(VllmWorker rank=5 pid=1663)   File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 224, in __call__
(VllmWorker rank=5 pid=1663)     res = self._callback(*self._args, **self._kwargs)
(VllmWorker rank=5 pid=1663)   File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 871, in _decref
(VllmWorker rank=5 pid=1663)     dispatch(conn, None, 'decref', (token.id,))
(VllmWorker rank=5 pid=1663)   File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 89, in dispatch
(VllmWorker rank=5 pid=1663)     c.send((id, methodname, args, kwds))
(VllmWorker rank=5 pid=1663)   File "/usr/local/python3.10/lib/python3.10/multiprocessing/connection.py", line 206, in send
(VllmWorker rank=5 pid=1663)     self._send_bytes(_ForkingPickler.dumps(obj))
(VllmWorker rank=5 pid=1663)   File "/usr/local/python3.10/lib/python3.10/multiprocessing/reduction.py", line 51, in dumps
(VllmWorker rank=5 pid=1663)     cls(buf, protocol).dump(obj)
(VllmWorker rank=5 pid=1663)   File "/usr/local/python3.10/lib/python3.10/multiprocessing/reduction.py", line 41, in __init__
(VllmWorker rank=5 pid=1663)     self.dispatch_table.update(self._extra_reducers)
(VllmWorker rank=5 pid=1663)   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 308, in signal_handler
(VllmWorker rank=5 pid=1663)     raise SystemExit()
(VllmWorker rank=5 pid=1663) SystemExit:

