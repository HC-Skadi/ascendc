# Issue #2455: [Bug]: DeepSeek R1 precision issue, send 1 token to server, get response containing irrelevant things

## 基本信息

- **编号**: #2455
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2455
- **创建时间**: 2025-08-20T07:06:58Z
- **关闭时间**: 2026-01-19T07:54:48Z
- **更新时间**: 2026-01-19T07:54:48Z
- **提交者**: @realliujiaxu
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...                                                                                                                                                           
PyTorch version: 2.7.1+cu126                                                                                                                                                                    
Is debug build: False                                                                                                                                                                           
                                                                                                                                                                                                
OS: openEuler 24.03 (LTS) (x86_64)                                                                                                                                                              
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)                                                                                                                                          
Clang version: Could not collect                                                                                                                                                                
CMake version: version 4.1.0                                                                                                                                                                    
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
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_t
sc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_
2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs
_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_
pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts av
x512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm uintr md_clear ser
ialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities                                                                                             
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
[pip3] pyzmq==27.0.1                                                                                                                                                                            
[pip3] torch==2.7.1                                                                                                                                                                             
[pip3] torch_npu==2.7.1.dev20250724                                                                                                                                                             
[pip3] transformers==4.53.3                                                                                                                                                                     
[conda] Could not collect                                                                                                                                                                       
vLLM Version: 0.10.1.dev392+g90ec00693.d20250820 (git sha: 90ec00693, date: 20250820)                                                                                                           
vLLM Ascend Version: 0.9.2rc2.dev144+g875a86cbe.d20250820 (git sha: 875a86cbe, date: 20250820) 

ENV Variables:                                                                                                                                                                                  
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240                                                                                                                                                    
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1                                                                                                                                                        
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0                                                                                                                                                           
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1                                                                                                                                                              
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0                                                                                                                                                                
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32                                                                                                                                                           
ATB_LAYER_INTERNAL_TENSOR_REUSE=1                                                                                                                                                               
ASCEND_VISIBLE_DEVICES=1,9,0,8,2,10,6,14,3,11,7,15,5,13,4,12                                                                                                                                    
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0                                                                                                                                                           
ASCEND_RUNTIME_OPTIONS=                                                                                                                                                                         
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5                                                                                                                                                       
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True                                                                                                                                                 
ATB_HOME_PATH=/mnt/deepseek/liujiaxu/8.2.RC1/nnal/atb/latest/atb/cxx_abi_1                                                                                                                      
ATB_LLM_COMM_BACKEND=hccl                                                                                                                                                                       
ASCEND_TOOLKIT_HOME=/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest                                                                                                                        
ASCEND_DOCKER_RUNTIME=True                                                                                                                                                                      
ATB_COMPARE_TILING_EVERY_KERNEL=0                                                                                                                                                               
ATB_LLM_HCCL_ENABLE=1                                                                                                                                                                           
ASCEND_OPP_PATH=/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/opp                                                                                                                        
LD_LIBRARY_PATH=/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/tools/aml/lib64:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/tools/aml/lib64/plugin:/mnt/deepseek/liujiaxu/8.2.RC1/
ascend-toolkit/latest/lib64:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64/plugin/opskernel:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64/plugin/nnengine:/mnt/deepseek
/liujiaxu/8.2.RC1/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/mnt/deepseek/liujiaxu/8.2.RC1/nnal/atb/latest/atb/cxx_abi_1/lib:/mnt/deepseek/liujiaxu/8.2.
RC1/nnal/atb/latest/atb/cxx_abi_1/examples:/mnt/deepseek/liujiaxu/8.2.RC1/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/tools/aml/lib64:/m
nt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/tools/aml/lib64/plugin:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64/
plugin/opskernel:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64/plugin/nnengine:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/
linux/x86_64:/mnt/deepseek/liujiaxu/8.2.RC1/nnal/atb/latest/atb/cxx_abi_0/lib:/mnt/deepseek/liujiaxu/8.2.RC1/nnal/atb/latest/atb/cxx_abi_0/examples:/mnt/deepseek/liujiaxu/8.2.RC1/nnal/atb/late
st/atb/cxx_abi_0/tests/atbopstest:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/tools/aml/lib64:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/tools/aml/lib64/plugin:/mnt/deepseek
/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64/plugin/opskernel:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/lib64/plugin/nnen
gine:/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal
/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/lat
est/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nne
ngine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:
/home/admin/inference/triton_default/lib64:/usr/local/lib64/python3.11/site-packages/vllm_ascend:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_a
bi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/p
lugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend
-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest                                                                                                                          
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3                                                                                                                                                               
ATB_RUNNER_POOL_SIZE=64                                                                                                                                                                         
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0                                                                                                                                                        
ASCEND_HOME_PATH=/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/latest                                                                                                                           
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
| 0     910B2C              | OK            | 89.7        44                0    / 0             |                                                                                              
| 0                         | 0000:5A:00.0  | 0           0    / 0          3444 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 1     910B2C              | OK            | 93.1        47                0    / 0             |                                                                                              
| 0                         | 0000:19:00.0  | 0           0    / 0          3415 / 65536         | 
+===========================+===============+====================================================+                                                                                     
| 2     910B2C              | OK            | 99.5        45                0    / 0             |                                                                                              
| 0                         | 0000:49:00.0  | 0           0    / 0          3416 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 3     910B2C              | OK            | 95.2        45                0    / 0             |                                                                                              
| 0                         | 0000:39:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 4     910B2C              | OK            | 99.3        44                0    / 0             |                                                                                              
| 0                         | 0000:DA:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 5     910B2C              | OK            | 100.8       48                0    / 0             |                                                                                              
| 0                         | 0000:99:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 6     910B2C              | OK            | 91.4        47                0    / 0             |                                                                                              
| 0                         | 0000:B8:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 7     910B2C              | OK            | 97.0        47                0    / 0             |                                                                                              
| 0                         | 0000:C8:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 8     910B2C              | OK            | 94.6        45                0    / 0             |                                                                                              
| 0                         | 0000:59:00.0  | 0           0    / 0          3427 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 9     910B2C              | OK            | 94.4        45                0    / 0             |                                                                                              
| 0                         | 0000:18:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 10    910B2C              | OK            | 94.0        45                0    / 0             |                                                                                              
| 0                         | 0000:48:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 11    910B2C              | OK            | 92.5        47                0    / 0             |                                                                                              
| 0                         | 0000:38:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 12    910B2C              | OK            | 98.1        47                0    / 0             |                                                                                              
| 0                         | 0000:D9:00.0  | 0           0    / 0          3416 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 13    910B2C              | OK            | 97.8        47                0    / 0             |                                                                                              
| 0                         | 0000:98:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 14    910B2C              | OK            | 92.9        45                0    / 0             |                                                                                              
| 0                         | 0000:B9:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
+===========================+===============+====================================================+                                                                                              
| 15    910B2C              | OK            | 102.0       48                0    / 0             |                                                                                              
| 0                         | 0000:C9:00.0  | 0           0    / 0          3415 / 65536         |                                                                                              
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
| No running processes found in NPU 8                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 9                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 10                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 11                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 12                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 13                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 14                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 15                                                           |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/8.2.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug

## 1. start server
```
export VLLM_ENABLE_MC2=0
export VLLM_USE_V1=1
export TASK_QUEUE_ENABLE=1
source /mnt/deepseek/liujiaxu/8.2.RC1/ascend-toolkit/set_env.sh
source /mnt/deepseek/liujiaxu/8.2.RC1/nnal/atb/set_env.sh
export VLLM_VERSION=0.9.1
export VLLM_ENABLE_FUSED_EXPERTS_ALLGATHER_EP=0
export VLLM_TORCH_PROFILER_DIR="./profile"
# export VLLM_EXPERT_DISTRIBUTION_RECORDER_DIR="/mnt/deepseek/liujiaxu/622/expert_load/decode0"


python -m vllm.entrypoints.openai.api_server --model=/mnt/deepseek/DeepSeek-R1-W8A8-VLLM \
    --quantization ascend \
    --load-format=prefetch_auto \
    --served-model-name auto \
    --trust-remote-code \
    --distributed-executor-backend=mp \
    --port 8009 \
    -tp=16 \
    -dp=1 \
    --max-num-seqs 24 \
    --max-model-len 8192 \
    --max-num-batched-tokens 2048 \
    --block-size 128 \
    --load-format auto \
    --additional-config '{"torchair_graph_config":{"enabled":true,"use_cached_graph":true,"graph_batch_sizes":[24],"enable_multistream_mla": true},"ascend_scheduler_config":{"enabled":true}}' \
    --gpu-memory-utilization 0.96
```

## 2. send request
```
curl --location 'http://127.0.0.1:8006/v1/chat/completions' --header 'Content-Type: application/json' --data '{
        "top_p": 1,
        "ignore_eos": false,
        "stream": false,
        "max_tokens": 100,
        "stop": "None",
        "top_k": -1,
        "temperature": 0.6,
        "messages": [
            {
                "role": "system",
                "content": "who"
            }
        ]
    }'
```

## 3. get response
response contains irrelevant content, like solving math problem

```
{"id":"chatcmpl-d9fca4df01b2481a959c319d20805d46","object":"chat.completion","created":1755671294,"model":"auto","choices":[{"index":0,"message":{"role":"assistant","content":"Okay, so I need to figure out how to solve this math problem. Let me see... Hmm, the problem is to find the integral of (x^2 + 3x - 5) divided by (x - 2)(x + 1)^2 with respect to x. Alright, that sounds like a partial fractions problem. Let me recall how partial fractions work.\n\nFirst, when you have a rational function, you can decompose it into simpler fractions. The denominator here","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"finish_reason":"length","stop_reason":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":5,"total_tokens":105,"completion_tokens":100,"prompt_tokens_details":null},"prompt_logprobs":null,"kv_transfer_params":null}
```
