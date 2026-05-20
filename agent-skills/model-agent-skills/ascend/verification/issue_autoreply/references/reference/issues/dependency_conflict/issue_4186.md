# Issue #4186: [Bug]: Unable to use Qwen3-VL to infer videos in 0.11.0rc1

## 基本信息

- **编号**: #4186
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4186
- **创建时间**: 2025-11-13T12:54:27Z
- **关闭时间**: 2025-12-08T09:58:26Z
- **更新时间**: 2025-12-08T09:58:26Z
- **提交者**: @hhd52859
- **评论数**: 8

## 标签

bug; module:multimodal

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.38

Python version: 3.11.10 (main, Nov  1 2025, 16:37:24) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.86.r1526_92.hce2.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250 To be filled by O.E.M. CPU @ 2.6GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
Stepping:                           0x1
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/::/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 87.6        48                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2901 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 86.5        46                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2899 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 84.8        47                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 90.4        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2899 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 92.7        48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 87.6        48                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 90.1        46                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 90.4        48                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2897 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

Infer video with Qwen3-VL-8B-Instruct got: "error":("message":"Expected reading 32 frames, but only loaded 29 frames from video.","type":"Internal Server Error","param":null,"code":500)

The server didn't log any traceback. After adding the following hook to vllm:
```python
# debug_hooks.py
import sys, asyncio, threading, logging, traceback, faulthandler

faulthandler.enable()                    # 信号触发可 dump 全线程栈

def _thread_excepthook(args: threading.ExceptHookArgs):
    logging.error("Uncaught exception in thread %s", args.thread.name,
                  exc_info=(args.exc_type, args.exc_value, args.exc_traceback))
threading.excepthook = _thread_excepthook

_orig_thread_run = threading.Thread.run
def _run_with_hook(self, *a, **kw):
    try:
        _orig_thread_run(self, *a, **kw)
    except Exception:  # pragma: no cover
        logging.exception("Uncaught exception in thread %s", self.name)
        raise
threading.Thread.run = _run_with_hook

_orig_create_task = asyncio.create_task
def _create_task_wrapper(coro, *a, **kw):
    t = _orig_create_task(coro, *a, **kw)
    def _done(task: asyncio.Task):
        try:
            exc = task.exception()
        except asyncio.CancelledError:
            return
        if exc:
            logging.error("Background task failed: %r", task.get_coro(), exc_info=exc)
    t.add_done_callback(_done)
    return t
asyncio.create_task = _create_task_wrapper

_installed = False
def _install_asyncio_handler(loop: asyncio.AbstractEventLoop):
    def _handle(loop, context):
        exc = context.get("exception")
        msg = context.get("message", "")
        if exc:
            logging.error("Asyncio unhandled exception: %s", msg, exc_info=exc)
        else:
            logging.error("Asyncio error: %s", msg or context)
    loop.set_exception_handler(_handle)

async def middleware(request, call_next):
    global _installed
    if not _installed:
        loop = asyncio.get_running_loop()
        _install_asyncio_handler(loop)
        logging.getLogger("vllm").setLevel(logging.DEBUG)
        _installed = True
    try:
        return await call_next(request)
    except Exception:
        logging.exception("Unhandled error for %s", request.url)
        raise
``` 
Start with --middleware debug_hooks.middleware , got traceback:
```python
[1;36m(APIServer pid=325350)[0;0m INFO:     Started server process [325350]
[1;36m(APIServer pid=325350)[0;0m INFO:     Waiting for application startup.
[1;36m(APIServer pid=325350)[0;0m INFO:     Application startup complete.
[1;36m(APIServer pid=325350)[0;0m INFO 11-13 20:51:19 [chat_utils.py:560] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this.
[1;36m(APIServer pid=325350)[0;0m ERROR:root:Background task failed: <coroutine object create_chat_completion at 0xfffc8af8a9b0>
[1;36m(APIServer pid=325350)[0;0m Traceback (most recent call last):
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 610, in create_chat_completion
[1;36m(APIServer pid=325350)[0;0m     generator = await handler.create_chat_completion(request, raw_request)
[1;36m(APIServer pid=325350)[0;0m                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/entrypoints/openai/serving_chat.py", line 239, in create_chat_completion
[1;36m(APIServer pid=325350)[0;0m     ) = await self._preprocess_chat(
[1;36m(APIServer pid=325350)[0;0m         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/entrypoints/openai/serving_engine.py", line 798, in _preprocess_chat
[1;36m(APIServer pid=325350)[0;0m     mm_data = await mm_data_future
[1;36m(APIServer pid=325350)[0;0m               ^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/entrypoints/chat_utils.py", line 748, in all_mm_data
[1;36m(APIServer pid=325350)[0;0m     items_by_modality[modality] = await asyncio.gather(*coros)
[1;36m(APIServer pid=325350)[0;0m                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/multimodal/utils.py", line 311, in fetch_video_async
[1;36m(APIServer pid=325350)[0;0m     return await self.load_from_url_async(
[1;36m(APIServer pid=325350)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/multimodal/utils.py", line 187, in load_from_url_async
[1;36m(APIServer pid=325350)[0;0m     return await future
[1;36m(APIServer pid=325350)[0;0m            ^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/concurrent/futures/thread.py", line 58, in run
[1;36m(APIServer pid=325350)[0;0m     result = self.fn(*self.args, **self.kwargs)
[1;36m(APIServer pid=325350)[0;0m              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/multimodal/utils.py", line 102, in _load_data_url
[1;36m(APIServer pid=325350)[0;0m     return media_io.load_base64(media_type, data)
[1;36m(APIServer pid=325350)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/multimodal/video.py", line 293, in load_base64
[1;36m(APIServer pid=325350)[0;0m     return self.load_bytes(base64.b64decode(data))
[1;36m(APIServer pid=325350)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/multimodal/video.py", line 276, in load_bytes
[1;36m(APIServer pid=325350)[0;0m     return self.video_loader.load_bytes(data,
[1;36m(APIServer pid=325350)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/multimodal/video.py", line 151, in load_bytes
[1;36m(APIServer pid=325350)[0;0m     assert i == num_frames, (f"Expected reading {num_frames} frames, "
[1;36m(APIServer pid=325350)[0;0m            ^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m AssertionError: Expected reading 32 frames, but only loaded 29 frames from video.
[1;36m(APIServer pid=325350)[0;0m 
[1;36m(APIServer pid=325350)[0;0m The above exception was the direct cause of the following exception:
[1;36m(APIServer pid=325350)[0;0m 
[1;36m(APIServer pid=325350)[0;0m Traceback (most recent call last):
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/entrypoints/utils.py", line 109, in wrapper
[1;36m(APIServer pid=325350)[0;0m     return await func(*args, **kwargs)
[1;36m(APIServer pid=325350)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=325350)[0;0m   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 612, in create_chat_completion
[1;36m(APIServer pid=325350)[0;0m     raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
[1;36m(APIServer pid=325350)[0;0m fastapi.exceptions.HTTPException: 500: Expected reading 32 frames, but only loaded 29 frames from video.
[1;36m(APIServer pid=325350)[0;0m INFO:     127.0.0.1:44320 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
```
Seems to be the same error with https://github.com/vllm-project/vllm/issues/20313
