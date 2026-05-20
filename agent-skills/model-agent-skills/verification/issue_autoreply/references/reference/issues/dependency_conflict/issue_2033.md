# Issue #2033: [Bug]: IndexError from `sorted_bitmask[batch_index] = grammar_bitmask[orig_index]`

## 基本信息

- **编号**: #2033
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2033
- **创建时间**: 2025-07-26T05:26:27Z
- **关闭时间**: 2025-07-31T01:03:28Z
- **更新时间**: 2025-08-04T03:21:02Z
- **提交者**: @ApsarasX
- **评论数**: 14

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Init 10948 task_queue_enable = 1
INFO 07-26 13:25:35 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-26 13:25:35 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-26 13:25:36 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-26 13:25:36 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-26 13:25:36 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-26 13:25:36 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-26 13:25:37 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.38

Python version: 3.11.6 (main, Feb 19 2025, 17:40:52) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
Python platform: Linux-5.10.112-100.alios7.x86_64-x86_64-with-glibc2.38

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
Model name:                      Intel(R) Xeon(R) Platinum 8468
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              48
Socket(s):                       2
Stepping:                        8
BogoMIPS:                        4200.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm uintr md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       4.5 MiB (96 instances)
L1i cache:                       3 MiB (96 instances)
L2 cache:                        192 MiB (96 instances)
L3 cache:                        210 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-47,96-143
NUMA node1 CPU(s):               48-95,144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1+gitc598ed2
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.1.dev1+g5cac6d5 (git sha: 5cac6d5)
vLLM Ascend Version: 0.1.dev1+g166b1ec (git sha: 166b1ec)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ASCEND_VISIBLE_DEVICES=7,6,0,1,5,4,2,3
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ATB_LLM_COMM_BACKEND=hccl
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ATB_LLM_HCCL_ENABLE=1
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/lib64/python3.11/site-packages/vllm_ascend:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
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
| npu-smi 25.0.rc1.1               Version: 25.0.rc1.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 90.9        48                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3432 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 100.2       49                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3414 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 90.6        48                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3414 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 93.4        47                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3413 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 90.4        44                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3414 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 98.4        45                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3413 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 88.7        44                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3414 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 90.4        47                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3413 / 65536         |
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
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug

**Error Stack**

```txt
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539] WorkerProc hit an exception.
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539] Traceback (most recent call last):
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 534, in worker_busy_loop
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     output = func(*args, **kwargs)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 245, in execute_model
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     return func(*args, **kwargs)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1513, in execute_model
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     logits = self.apply_grammar_bitmask(scheduler_output, logits)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1357, in apply_grammar_bitmask
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     sorted_bitmask[batch_index] = grammar_bitmask[orig_index]
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     ~~~~~~~~~~~~~~^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539] IndexError: index 1 is out of bounds for axis 0 with size 1
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539] Traceback (most recent call last):
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 534, in worker_busy_loop
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     output = func(*args, **kwargs)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 245, in execute_model
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     return func(*args, **kwargs)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1513, in execute_model
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     logits = self.apply_grammar_bitmask(scheduler_output, logits)
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1357, in apply_grammar_bitmask
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     sorted_bitmask[batch_index] = grammar_bitmask[orig_index]
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539]     ~~~~~~~~~~~~~~^^^^^^^^^^^^^
(VllmWorker rank=6 pid=653) ERROR 07-26 13:19:51 [multiproc_executor.py:539] IndexError: index 1 is out of bounds for axis 0 with size 1
```


Reproduce Step
1. Start vllm engine
```sh
export ACL_DEVICE_SYNC_TIMEOUT=1200
export HCCL_EXEC_TIMEOUT=1440
export HCCL_CONNECT_TIMEOUT=1440
export HCCL_EVENT_TIMEOUT=1800

export VLLM_USE_V1=1
export TASK_QUEUE_ENABLE=2
export VLLM_VERSION=0.9.1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

export PROMETHEUS_MULTIPROC_DIR=/tmp/

nohup python -m vllm.entrypoints.openai.api_server \
    --model=/qwen3-32b/ \
    --trust-remote-code \
    --served-model-name auto \
    --load-format=prefetch_auto \
    --distributed-executor-backend=mp \
    --port 8006 \
    -tp=8 \
    --enforce-eager \
    --max-num-seqs 192 \
    --max-model-len 32768 \
    --max-num-batched-tokens 32768 \
    --block-size 128 \
    --gpu-memory-utilization 0.9 \
    --enable-prompt-tokens-details &> run.log &
disown
```

2. Prepare `bad_case.json`
```json
{
    "model": "auto",
    "messages": [
      {
        "role": "system",
        "content": "作为一个JSON格式化工具，请你把用户输入的内容按行格式化为标准的JSON格式"
      },
      {
        "role": "user",
        "content": "《修补星星的人》\n\n深夜的阁楼里，八岁的小雨踮脚按住漏风的窗户。\"爷爷，星星又掉下来啦！\"她指着窗框上闪烁的银屑。老人放下放大镜，从旧皮箱取出镊子和玻璃罐：\"别急，这可是今年第三颗了。\"\n\n十年前流星雨袭击小镇时，老钟表匠是第一个发现异常的人。他亲眼看见那些\"星星\"其实是发光的金属碎片，会让人忘记重要的事情。每当碎片从夜空剥落，他就用特制胶水把它们粘回天幕。\"您为什么不让大家知道？\"小雨帮他扶稳梯子。\"有些秘密，\"老人把碎片按在墨色天穹上，\"知道的人越少，才守得住。\"\n\n寒潮来临那晚，老人没能接住坠落的碎片。小雨在晨光里发现他坐在梯子顶端，怀里紧抱着空玻璃罐，睫毛上结满冰晶。她颤抖着爬上梯子，看见罐底贴着的纸条：\"胶水配方在榫卯里。\"\n\n现在镇民们总夸小雨做的星空灯特别美。没人发现灯罩里游动的银光，正如没人记得十年前那场消失的流星雨。只有修补过的新月知道，每当小雨在深夜打开阁楼窗户，总有几颗星星格外明亮。\n\n（全篇598字，对话引号均使用半角格式并添加转义符，符合要求）"
      },
      {
        "role": "user",
        "content": "《最后一颗种子》\n\n干旱的村庄里，老农夫坚持每天给最后一颗种子浇水。村民嘲笑他：\"别傻了，土地都裂了，怎么可能发芽？\"老农夫只是笑笑，继续照料。\n\n三个月后，一场暴雨降临。第二天，嫩绿的芽破土而出，老农夫轻声说：\"看，它等的不是水，而是不放弃的心。\"\n\n村民们沉默了。原来希望从未消失，只是藏在坚持里。\n\n（共198字）"
      }
    ],
    "temperature": 0.3,
    "top_p": 0.8,
    "top_k": 20,
    "max_tokens": 2048,
    "ignore_eos": true,
    "response_format": {"type": "json_object"}
}
``` 

3. Send the following requests to vllm engine

```sh
curl -H "Content-type: application/json" -X POST http://127.0.0.1:8006/v1/chat/completions --data '{
        "top_p": 1,
        "model": "auto",
        "ignore_eos": false,
        "stream": true,
        "max_tokens": 1536,
        "top_k": -1,
        "temperature": 0.6,
        "ignore_eos": true,
        "messages": [
            {
                "role": "system",
                "content": "who are you?"
            }
        ]
    }' &
pid1=$!
sleep 1

curl -H "Content-type: application/json" -X POST http://127.0.0.1:8006/v1/chat/completions --data @bad_case.json &
pid2=$!
sleep 1

curl -H "Content-type: application/json" -X POST http://127.0.0.1:8006/v1/chat/completions --data '{
        "top_p": 1,
        "model": "auto",
        "ignore_eos": false,
        "stream": true,
        "max_tokens": 1536,
        "top_k": -1,
        "temperature": 0.6,
        "ignore_eos": true,
        "messages": [
            {
                "role": "system",
                "content": "who are you?"
            }
        ]
    }' &
pid3=$!

sleep 3
kill -9 $pid1
sleep 3
kill -9 $pid2
sleep 3
kill -9 $pid3

wait $pid1
wait $pid2
wait $pid3
```
