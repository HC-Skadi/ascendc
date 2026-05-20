# Issue #457: [Bug]: Qwen2.5-VL 多请求情况时会出现后到的请求被Abort。

## 基本信息

- **编号**: #457
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/457
- **创建时间**: 2025-04-01T13:26:09Z
- **关闭时间**: 2025-04-02T12:41:41Z
- **更新时间**: 2026-01-19T07:51:11Z
- **提交者**: @MarkJoson
- **评论数**: 9

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: 14.0.0-1ubuntu1.1
CMake version: version 3.31.6
Libc version: glibc-2.35

Python version: 3.10.15 (main, Oct  3 2024, 07:21:53) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.oe2203.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1.dev20250320          pypi_0    pypi
[conda] torchaudio                2.5.1                    pypi_0    pypi
[conda] torchvision               0.20.1                   pypi_0    pypi
[conda] transformers              4.49.0                   pypi_0    pypi
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc2

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_PORT_2222_TCP_PROTO=tcp
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ASCEND_K8S_VSCODE_20250401_184918_PORT_80_TCP=tcp://10.96.0.184:80
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_K8S_VSCODE_20250401_184918_PORT=tcp://10.96.0.184:80
ASCEND_K8S_VSCODE_20250401_184918_PORT_80_TCP_PORT=80
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=Ascend910-0,Ascend910-1,Ascend910-2,Ascend910-3,Ascend910-4,Ascend910-5,Ascend910-6,Ascend910-7
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_SERVICE_HOST=10.96.3.107
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_SERVICE_PORT_ASCENDJOB_PORT=2222
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ASCEND_K8S_VSCODE_20250401_184918_SERVICE_PORT=80
ASCEND_K8S_VSCODE_20250401_184918_SERVICE_HOST=10.96.0.184
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_PORT=tcp://10.96.3.107:2222
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_SERVICE_PORT=2222
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_PORT_2222_TCP_ADDR=10.96.3.107
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_PORT_2222_TCP_PORT=2222
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/data/home/3120235672/anaconda/envs/llama_factory/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/data/home/3120235672/mpich-install/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/data/home/3120235672/mpich-install/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:::
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_K8S_VSCODE_20250401_184918_CHIEF_0_PORT_2222_TCP=tcp://10.96.3.107:2222
ASCEND_K8S_VSCODE_20250401_184918_PORT_80_TCP_ADDR=10.96.0.184
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
ASCEND_K8S_VSCODE_20250401_184918_PORT_80_TCP_PROTO=tcp
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2                 Version: 24.1.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 94.6        37                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3359 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 90.5        33                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3355 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 88.4        35                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3352 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 97.1        37                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3352 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 91.7        41                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3349 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 96.7        39                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3350 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 95.4        40                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3351 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 94.8        41                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3350 / 65536         |
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
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
```

vllm 0.7.3
vllm-ascend 0.7.3rc2

</details>


### 🐛 Describe the bug

Qwen2.5-VL 多请求情况时会出现后到的请求被Abort。Qwen2.5不带VL的不会出现这个问题。

RTX4090+vllm 0.8版本不会出现这个问题

```
vllm \
    serve \
    Qwen/Qwen2.5-VL-7B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --gpu-memory-utilization 0.95 \
    --tensor-parallel-size 4 \
    --max-model-len 32768 \
```

output:
```
INFO 04-01 21:24:35 engine.py:280] Added request chatcmpl-93fa13be3529493c887ad55270047cb9.
INFO 04-01 21:24:35 engine.py:280] Added request chatcmpl-5f8fc5a98e564557b354b1300b2f03d1.
INFO 04-01 21:24:35 engine.py:280] Added request chatcmpl-4dbcb2f7989c499bad8eb67e2b2bb93e.
INFO 04-01 21:25:15 metrics.py:455] Avg prompt throughput: 47.6 tokens/s, Avg generation throughput: 4.5 tokens/s, Running: 55 reqs, Swapped: 0 reqs, Pending: 9 reqs, GPU KV cache usage: 1.1%, CPU KV cache usage: 0.0%.
INFO 04-01 21:25:22 metrics.py:455] Avg prompt throughput: 4597.5 tokens/s, Avg generation throughput: 7.2 tokens/s, Running: 64 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.3%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:58612 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58518 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-01 21:25:27 metrics.py:455] Avg prompt throughput: 1128.0 tokens/s, Avg generation throughput: 756.3 tokens/s, Running: 62 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.5%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:58552 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58602 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58584 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58526 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58568 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58590 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58560 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58566 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58536 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58580 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58598 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58604 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58538 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58548 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58528 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58600 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58498 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58570 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58490 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58512 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58540 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58608 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58514 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58542 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58554 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58588 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58504 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58516 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58496 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58586 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58574 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58592 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58494 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58530 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58532 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58572 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58610 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58506 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58594 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58558 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58510 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58556 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58492 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58500 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58582 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:58606 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-01 21:25:30 engine.py:298] Aborted request chatcmpl-0a5743529b054b00b676646fa092a677.
INFO:     127.0.0.1:58534 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-01 21:25:30 engine.py:298] Aborted request chatcmpl-fa199863e79b47c39528e287c82369ed.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-d3eac35ed55142c8829ed2b26f15fb41.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-5f49aeca2e36476da2535da0b58838d5.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-77344a9e856c496ea407cc09f41ab397.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-99c317a63f0148b5a9b78b611a2adea4.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-fa5e7b9314b546b69fc8d39f69aad1f8.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-ec6b46c7dbbc429ca5f85bb68abd9ddc.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-9293d726e18a462a86365382ae27e55e.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-4ae31ae189f44cb7aa2490a1701eadcb.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-d2bd397709584a9d95d20aa10242d7ee.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-c101aead34394a5e8c0312fce12bea69.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-c61a38c7a54645008b5f185b4ecfa5a1.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-1470f38fcecd4853bf8647b0300fe352.
INFO 04-01 21:25:31 engine.py:298] Aborted request chatcmpl-4dbcb2f7989c499bad8eb67e2b2bb93e.

```


```python
import requests
import base64
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 提前读取图片并编码
def encode_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 单次请求函数
def test_qwen25_vl(base64_image, prompt, custom_api_url, api_key=None):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{base64_image}"}
                },
                {"type": "text", "text": prompt},
            ],
        }
    ]

    payload = {
        "model": "gpt-4o",
        "messages": messages
    }

    headers = {
        "Content-Type": "application/json"
    }

    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        response = requests.post(
            f"{custom_api_url}/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60  # 设置合理超时
        )

        if response.status_code == 200:
            return {"status": "success", "response": response.json()}
        else:
            return {"status": "fail", "code": response.status_code, "details": response.text}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

# 并发执行函数
def run_concurrent_tests(image_path, prompt, api_url, api_key, concurrency=16):
    results = []
    start_time = time.time()

    print(f"🚀 开始并发测试，共 {concurrency} 路请求...")

    # 提前加载图片，避免每个线程重复读取
    base64_image = encode_image_base64(image_path)
    
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = []
        for i in range(concurrency):
            futures.append(executor.submit(test_qwen25_vl, base64_image, prompt, api_url, api_key))
            # time.sleep(0.2)
        
        for i, future in enumerate(as_completed(futures), 1):
            try:
                result = future.result()
                print(f"[{i}/{concurrency}] 完成 - 状态: {result['status']}")
                results.append(result)
            except Exception as e:
                print(f"[{i}/{concurrency}] 异常: {e}")
                results.append({"status": "error", "message": str(e)})

    end_time = time.time()
    print(f"\n✅ 并发测试完成: {concurrency} 路请求，共耗时 {end_time - start_time:.2f} 秒")
    return results

# 主程序
if __name__ == "__main__":
    IMAGE_PATH = "lion.jpg"
    PROMPT = "请你描述这张图片."
    CUSTOM_API_URL = "http://127.0.0.1:8000"
    API_KEY = "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"

    results = run_concurrent_tests(IMAGE_PATH, PROMPT, CUSTOM_API_URL, API_KEY, concurrency=64)

    # 保存结果
    with open("concurrent_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
```
