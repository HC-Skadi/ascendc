# Issue #5772: [Bug]: vllm-ascend-v0.13.0rc1 推理 paddle-vl-0.9b 报错

## 基本信息

- **编号**: #5772
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5772
- **创建时间**: 2026-01-09T10:20:14Z
- **关闭时间**: 2026-01-15T03:17:01Z
- **更新时间**: 2026-01-15T03:17:01Z
- **提交者**: @Sage520
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-118-generic-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               192
On-line CPU(s) list:                  0-191
Vendor ID:                            HiSilicon
Model name:                           Kunpeng-920
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   48
Socket(s):                            4
Stepping:                             0x1
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                            12 MiB (192 instances)
L1i cache:                            12 MiB (192 instances)
L2 cache:                             96 MiB (192 instances)
L3 cache:                             192 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-23
NUMA node1 CPU(s):                    24-47
NUMA node2 CPU(s):                    48-71
NUMA node3 CPU(s):                    72-95
NUMA node4 CPU(s):                    96-119
NUMA node5 CPU(s):                    120-143
NUMA node6 CPU(s):                    144-167
NUMA node7 CPU(s):                    168-191
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; __user pointer sanitization
Vulnerability Spectre v2:             Not affected
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=1
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.2.3                   Version: 25.2.3                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 87.4        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          9030 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 89.5        35                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          29267/ 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 81.4        34                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          9788 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 85.2        34                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          9471 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 82.2        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          32061/ 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 87.9        37                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          32060/ 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 83.9        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          32061/ 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 82.9        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          32055/ 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 29570         |                          | 3806                    |
| 0       0                 | 18966         |                          | 2330                    |
+===========================+===============+====================================================+
| 1       0                 | 9232          |                          | 26455                   |
+===========================+===============+====================================================+
| 2       0                 | 4320          |                          | 401                     |
| 2       0                 | 4332          |                          | 3419                    |
| 2       0                 | 4317          |                          | 3267                    |
+===========================+===============+====================================================+
| 3       0                 | 64512         |                          | 401                     |
| 3       0                 | 64617         |                          | 3179                    |
| 3       0                 | 64602         |                          | 3189                    |
+===========================+===============+====================================================+
| 4       0                 | 45382         |                          | 29259                   |
+===========================+===============+====================================================+
| 5       0                 | 45396         |                          | 29259                   |
+===========================+===============+====================================================+
| 6       0                 | 45478         |                          | 29259                   |
+===========================+===============+====================================================+
| 7       0                 | 45513         |                          | 29259                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

按照 https://docs.vllm.ai/projects/vllm-ascend-cn/zh-cn/latest/tutorials/PaddleOCR-VL.html 安装配置
我使用了docker-compose 来编排：
```yaml
  ocr-paddle-vl-2:
    image: quay.io/ascend/vllm-ascend:v0.13.0rc1
    container_name: ocr-paddle-vl-2
    hostname: ocr-paddle-vl-2
    networks:
      - weique
    ipc: host
    privileged: true
    stdin_open: true
    tty: true
    shm_size: 50g
    devices:
      - /dev/davinci_manager
      - /dev/devmm_svm
      - /dev/hisi_hdc
    volumes:
      - /weique/models:/data/models:ro
      - ./start.sh:/app/start.sh:ro
      - /usr/local/dcmi:/usr/local/dcmi
      - /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool
      - /usr/local/bin/npu-smi:/usr/local/bin/npu-smi
      - /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/
      - /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info
      - /etc/ascend_install.info:/etc/ascend_install.info
      - /root/.cache:/root/.cache
    entrypoint: ["bash", "/app/start.sh"]
```

```bash
#!/bin/bash

export VLLM_USE_MODELSCOPE=true
export MODEL_PATH=/data/models/PaddleOCR-VL-0.9B

vllm serve ${MODEL_PATH} \
          --max-num-batched-tokens 16384 \
          --served-model-name PaddleOCR-VL-0.9B \
          --trust-remote-code \
          --no-enable-prefix-caching \
          --mm-processor-cache-gb 0 \
          --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}'
```

能够成功启动服务并且监听端口，但是一旦传入图片推理就会报错，下面是我的请求体和报错信息
```json
{
    "model": "PaddleOCR-VL-0.9B",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "OCR:"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "http://10.30.1.3:9000/weique-lowcode/1.jpg"
            }
          }
        ]
      }
    ]
}
```

```json
{
    "error": {
        "message": "EngineCore encountered an issue. See stack trace (above) for the root cause.",
        "type": "Internal Server Error",
        "param": null,
        "code": 500
    }
}
```

```bash
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     self._process_engine_step()
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 919, in _process_engine_step
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     outputs, model_executed = self.step_fn()
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)                               ^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 351, in step
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     model_output = future.result()
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)                    ^^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/usr/local/python3.11.13/lib/python3.11/concurrent/futures/_base.py", line 449, in result
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     return self.__get_result()
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)            ^^^^^^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/usr/local/python3.11.13/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     raise self._exception
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/v1/executor/uniproc_executor.py", line 79, in collective_rpc
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     result = run_method(self.driver_worker, method, args, kwargs)
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/v1/serial_utils.py", line 461, in run_method
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     return func(*args, **kwargs)
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)            ^^^^^^^^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 369, in execute_model
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     return self.worker.execute_model(scheduler_output, *args, **kwargs)
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 308, in execute_model
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     output = self.model_runner.execute_model(scheduler_output,
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     return func(*args, **kwargs)
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)            ^^^^^^^^^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1373, in execute_model
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     self._update_states(scheduler_output)
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 851, in _update_states
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     self._init_mrope_positions(req_state)
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 1066, in _init_mrope_positions
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     mrope_model.get_mrope_input_positions(
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)   File "/vllm-workspace/vllm/vllm/model_executor/models/paddleocr_vl.py", line 1127, in get_mrope_input_positions
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)     t, h, w = image_grid_thw[image_index]
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36)               ~~~~~~~~~~~~~~^^^^^^^^^^^^^
ocr-paddle-vl-2  | (EngineCore_DP0 pid=36) IndexError: list index out of range

```
