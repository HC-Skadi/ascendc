# Issue #4513: [Bug]:   Accuracy issue on Qwen3-Omni-30B-A3B-Thinking

## 基本信息

- **编号**: #4513
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4513
- **创建时间**: 2025-11-27T13:17:20Z
- **关闭时间**: 2025-12-31T01:04:22Z
- **更新时间**: 2025-12-31T01:04:22Z
- **提交者**: @Meihan-chen
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:57:00) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
BIOS Model name:                      Kunpeng 920 7285Z
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   80
Socket(s):                            4
Stepping:                             0x0
Frequency boost:                      disabled
CPU max MHz:                          3000.0000
CPU min MHz:                          400.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                            20 MiB (320 instances)
L1i cache:                            20 MiB (320 instances)
L2 cache:                             400 MiB (320 instances)
L3 cache:                             560 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-39
NUMA node1 CPU(s):                    40-79
NUMA node2 CPU(s):                    80-119
NUMA node3 CPU(s):                    120-159
NUMA node4 CPU(s):                    160-199
NUMA node5 CPU(s):                    200-239
NUMA node6 CPU(s):                    240-279
NUMA node7 CPU(s):                    280-319
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
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.2
vLLM Ascend Version: 0.11.0rc1.dev411+g84d7f5a10 (git sha: 84d7f5a10)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 24.1.rc3.7               Version: 24.1.rc3.7                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 175.0       39                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3451 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           38                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3215 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 184.9       38                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3433 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3208 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 177.2       37                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3447 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3196 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 189.5       37                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3435 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           36                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3209 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 175.7       38                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3440 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           37                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3205 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 177.3       37                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3433 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3205 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 177.4       37                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3452 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           36                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3194 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 184.2       36                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3447 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           38                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          3192 / 65536         |
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
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

### offline inference
There is an accuracy issue on on Qwen3-Omni-30B-A3B-Thinking with tensor_parallel_size==2.
```python
import gc
import torch
import os
from vllm import LLM, SamplingParams
from vllm.distributed.parallel_state import (
    destroy_distributed_environment,
    destroy_model_parallel
)
from modelscope import Qwen3OmniMoeProcessor
from qwen_omni_utils import process_mm_info


def clean_up():
    """Clean up distributed resources and NPU memory"""
    destroy_model_parallel()
    destroy_distributed_environment()
    gc.collect()  # Garbage collection to free up memory
    torch.npu.empty_cache()


def main():
    MODEL_PATH = "/root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-Omni-30B-A3B-Thinking"
    llm = LLM(
        model=MODEL_PATH,
        tensor_parallel_size=2,
        distributed_executor_backend="mp",
        limit_mm_per_prompt={'image': 5, 'video': 2, 'audio': 3},
        max_model_len=32768,
    )

    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        top_k=20,
        max_tokens=16384,
    )

    processor = Qwen3OmniMoeProcessor.from_pretrained(MODEL_PATH)
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": "cars.jpg"},
                {"type": "audio", "audio": "cough.wav"},
                {"type": "video", "video": "draw.mp4"},
                {"type": "text", "text": "Analyze this audio, image, and video together."}
            ]
        }
    ]

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    audios, images, videos = process_mm_info(messages, use_audio_in_video=False)

    inputs = {
        "prompt": text,
        "multi_modal_data": {},
        "mm_processor_kwargs": {"use_audio_in_video": False}
    }
    if images is not None:
        inputs['multi_modal_data']['image'] = images
    if videos is not None:
        inputs['multi_modal_data']['video'] = videos
    if audios is not None:
        inputs['multi_modal_data']['audio'] = audios

    outputs = llm.generate([inputs], sampling_params=sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

    del llm
    clean_up()


if __name__ == "__main__":
    main()
```
results
```bash
Prompt: '<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|><|audio_start|><|audio_pad|><|audio_end|><|vision_start|><|video_pad|><|vision_end|>Analyze this audio, image, and video together.<|im_end|>\n<|im_start|>assistant\n', Generated text: '<think>\nGot it, let\'s tackle the problem. First, the user has provided a set of images and a video, and I need to understand what they are asking for. Let me break it down.\n\nFirst, the initial request was to analyze the audio, image, and video together. Let me check the current input. The user included a message that starts with a cough sound, then "Analyze this audio, image, and video together." But wait, looking at the problem now: the user is asking to process the provided media. However, the current context is that the user provided a query where they want the assistant to act as if they are analyzing the given audio, image, and video. But let\'s re-express.\n\nWait, looking at the problem statement: The user provided a sequence where they might have a previous setup, but in this case, the current task is to act as the AI that received the user\'s latest input. Let\'s parse the user\'s exact input.\n\nThe user\'s current query is: "Analyze this audio, image, and video together." But no, looking back, the actual user input that starts with "Analyze this audio, image, and video together." Wait, no. Wait, looking at the history, the user\'s message history is that they first had a query, but in the current problem, the user is presenting a scenario where we have to process the given inputs.\n\nWait, no. Let\'s re-express the problem. The user is showing a scenario where there are multiple images of cars (a collage of luxury/sports cars: Rolls-Royce, Mercedes GLE, Ferrari, Porsche, and then a video of someone drawing a guitar on a tablet). Then, the next part is the user\'s instruction to "Analyze this audio, image, and video together." But in the current problem, the actual data is that the user is providing an image (the car collage), an audio (which in the problem statement might be part of the context), but the user is now, in the context of the problem, asking to analyze the audio, image, and video together.\n\nWait, but given the problem as presented to me (as the AI) is to process the user\'s input. Let\'s read the user\'s current input again, which is the problem we need to solve. Wait, no. Wait, the user is not the one providing the query; no, in this setup, the user is the one who wrote the initial instruction, and the system is to generate the AI\'s thought process.\n\nWait, looking at the raw input from the user (the problem statement), it\'s structured as follows (this is the user\'s message to the AI):\n\n"Analyze this audio, image, image, video, and then provide the final answer. The key is to synthesize all these elements into a coherent response. Please place the answer in \\boxed{}."\n\nWait, no. Let\'s look at the exact text the user provided. Let\'s parse it:\n\nThe user\'s input to the assistant (the problem we need to solve) is:\n\n[Image of four car images] [Image of a hand drawing on a tablet] [Video of a drawing?] \n\nBut looking at the actual text the user pasted (which is the problem statement for us as the AI to solve), it\'s a bit garbled, but the key is that in the problem, we have to act as the AI that has to process that.\n\nBut perhaps the problem is from a specific dataset or example. However, given the instructions, the task is for the AI to generate a response to the user\'s prompt, which involves analyzing audio, image, and video. But the specific instruction now is: the user is providing a problem where they have multiple media types, and we need to see what the correct answer is.\n\nWait, looking back, the user\'s initial problem (the main content) is that they have a series of images (car photos) and a short video of drawing, and the task is to "Analyze this audio, image, and video together." But in this case, the key is to recognize the actual task: the user is likely providing a context where there\'s a need to interpret the combination of the car images (as the "image" part), the action of drawing (the "video" part as a sequence), but perhaps this is a test to see if the AI can identify the common thread.\n\nWait, no. Wait, stepping back: the problem is presented as a standard task where the user has a set of images/videos to analyze. However, looking at the very end of the user\'s input, there\'s a line: "If the question has a final answer, please place the answer in \\boxed{}."\n\nBut given the context of the initial problem, which seems to be a test of the AI\'s ability to follow a complex, multi-part question (which is common in some problem sets), the likely "final answer" here is the model\'s own name. Wait, no. Alternatively, this might be a trick question where the key is that all the images and the video are examples of "vehicles" or "luxury items", but the final line of the user\'s input is "If the question has a question, the answer is the name of the most expensive car in the list. But the answer is the model\'s name. Wait, no.\n\nWait, no. Let\'s recall: the user\'s prompt is a bit of a red herring. In some AI training examples, there\'s a specific answer expected. However, the actual key is that the problem is a joke or a test: the "final answer" is "The car that\'s being driven in the video on the left." But no.\n\nWait, no. Looking back at the problem, the key is that the first part lists cars (Rolls-Royce, Mercedes, Ferrari, Porsche), and the video might be a distraction. However, the actual "final answer" is "Porsche" but I need to recall the actual structure.\n\nWait, no. Wait, the problem is from a set where the correct answer is that the user has to identify a specific car. But given the detailed instructions, the most likely "final answer" is "Porsche" but I\'m overcomplicating.\n\nWait, no. Let\'s look at the problem\'s final sentence: "the answer is the name of the most expensive car in the list." But no. Wait, the problem here is that the initial user message (which the system is using as the prompt for the problem) is a setup for the "final answer" to be "The problem does not specify the answer." But no.\n\nWait, no. Let\'s recall: the original problem the assistant is supposed to solve is the one that starts with the car images and the instruction. However, in the context of the problem given to the student (since this is a problem for the AI to solve), the correct answer is that the "final answer\'s \\boxed{} is \'The image shows various luxury cars including a Rolls-Royce, Mercedes GLE, Ferrari, and Porsche. The video depicts a digital guitar drawing. No audio is present. The question\'s final answer is \'Porsche\'." But this is not right.\n\nWait, no. Given the way the problem is set up, with the sequence of images and the user\'s note "If the question has a question, the answer is the name of the most expensive car in the list. The final answer\'s unit must be name of the car. Let\'s think: what\'s the most expensive car in the list?\n\nWait, the initial images: top left is a Rolls-Royce (luxury), then a Mercedes GLE (SUV), then a Ferrari (red convertible), and a white Porsche. Typically, the most expensive production car in the list might be the Rolls-Royce, but the question says "the final answer\'s unit must be name of the car" and the example says to box the answer.\n\nBut wait, no. The actual key is that this is a trick question. The "final answer" is a specific term. However, looking up similar problems, the correct answer here is "Porsche" but that\'s not it.\n\nWait, no. The problem is from a Chinese language test or something. Alternatively, looking at the video part: the video is of a guitar drawing. But the key is that the correct answer is "Porsche" as per the problem\'s hidden logic. However, the most common answer for this type of question (which is a meme in some circles) is that the final answer is "The car in the bottom right is a Porsche, so the answer is Porsche." But no, that\'s not it.\n\nWait, no. Let\'s step back. The user has given a problem where the "final answer" is to be the name of the car in the video or the audio, but the correct standard answer for this specific setup (as this is a known problem) is that the final answer is "Porsche". Alternatively, the problem is a joke where the correct answer is "The car in the image is a Ferrari." But no.\n\nWait, no. The key is in the "If the question has a question, the answer is the name of the most expensive car in the list. But the most expensive car in the list: Rolls-Royce is top, but in the list of cars shown, the bottom right is a white Porsche. Wait, no. The known standard for this exact problem (which is a common one where the answer is "Porsche") is that the final answer is Porsche. Therefore, the answer is \\boxed{Porsche}.\n\nBut let\'s verify. The problem shows multiple car images. The instruction says "If the question has a question, the answer is the name of the most expensive car in the list. But the most expensive car in the car lineup (as in the problem\'s hidden context) is Porsche. However, in reality, Rolls-Royce is more expensive, but maybe in the problem\'s context, it\'s a trick. However, this is a standard problem where the correct answer is "Porsche", so I\'ll go with that.\n| | |\n| --- | --- |\n| The problem requires analyzing the provided images and video. The images show luxury/sports cars, and the question\'s context (as a known pattern) indicates the final answer is the name of the most expensive car. Among the typical examples used (Rolls-Royce, Mercedes, Ferrari, Porsche), the Porsche is the final one and commonly the answer for this problem type. However, the standard "final answer" for this exact problem setup is Porsche. |\n\nWait, but the standard version of this type of question (which this seems to be a variant of) has the correct answer as "Porsche" as the final answer. So the boxed answer should be \\boxed{Porsche}.\n\\boxed{Porsche}'
```
### online inference
commands
```bash
vllm serve /root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-Omni-30B-A3B-Thinking --tensor-parallel-size 2
```
```bash
 curl http://localhost:8000/v1/chat/completions \8000/v1/chat/comple
-X POST \
-H "Content-Type: application/json" \
-d '{
    "model": "/root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-Omni-30B-A3B-Thinking",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"
                    }
                },
                {
                    "type": "text",
                    "text": "Analyze this image"
                }
            ]
        }
    ]
}'
{"error":{"message":"EngineCore encountered an issue. See stack trace (above) for the root cause.","type":"Internal Server Error","param":null,"code":500}}
```

logs
```bash
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] WorkerProc hit an exception.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/v1/worker/worker_base.py", line 367, in execute_model
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 290, in execute_model
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2338, in execute_model
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1897, in _generate_process_reqs_hidden_states
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     hidden_states = self.model(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                     ^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1380, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     hidden_states = self.language_model.model(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/decorators.py", line 399, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/wrapper.py", line 152, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.forward(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 601, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     def forward(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return fn(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/caching.py", line 53, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.optimized_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     raise e
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "<eval_with_key>.98", line 417, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     submod_20 = self.submod_20(getitem_47, s0, l_self_modules_layers_modules_9_modules_self_attn_modules_o_proj_parameters_weight_, getitem_48, l_self_modules_layers_modules_9_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_9_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_10_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s2);  getitem_47 = l_self_modules_layers_modules_9_modules_self_attn_modules_o_proj_parameters_weight_ = getitem_48 = l_self_modules_layers_modules_9_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_9_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_10_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_k_norm_parameters_weight_ = None
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 111, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.runnable(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/piecewise_backend.py", line 99, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.compiled_graph_for_general_shape(*args)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     raise e
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "<eval_with_key>.21", line 16, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     moe_forward = torch.ops.vllm.moe_forward(view_1, linear_1, 'language_model.model.layers.9.mlp.experts');  view_1 = linear_1 = None
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1893, in moe_forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 323, in forward_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     final_hidden_states = self.quant_method.apply(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 131, in apply
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return moe_comm_method.fused_experts(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 121, in fused_experts
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     results = self.token_dispatcher.token_dispatch(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 375, in token_dispatch
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     torch_npu.npu_moe_init_routing_v2(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is SelfAttentionOperation.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] [ERROR] 2025-11-27-12:40:30 (PID:8549, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/v1/worker/worker_base.py", line 367, in execute_model
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 290, in execute_model
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2338, in execute_model
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1897, in _generate_process_reqs_hidden_states
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     hidden_states = self.model(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                     ^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1380, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     hidden_states = self.language_model.model(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/decorators.py", line 399, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/wrapper.py", line 152, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.forward(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 601, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     def forward(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return fn(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/caching.py", line 53, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.optimized_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     raise e
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "<eval_with_key>.98", line 417, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     submod_20 = self.submod_20(getitem_47, s0, l_self_modules_layers_modules_9_modules_self_attn_modules_o_proj_parameters_weight_, getitem_48, l_self_modules_layers_modules_9_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_9_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_10_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s2);  getitem_47 = l_self_modules_layers_modules_9_modules_self_attn_modules_o_proj_parameters_weight_ = getitem_48 = l_self_modules_layers_modules_9_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_9_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_10_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_k_norm_parameters_weight_ = None
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 111, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.runnable(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/compilation/piecewise_backend.py", line 99, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.compiled_graph_for_general_shape(*args)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     raise e
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "<eval_with_key>.21", line 16, in forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     moe_forward = torch.ops.vllm.moe_forward(view_1, linear_1, 'language_model.model.layers.9.mlp.experts');  view_1 = linear_1 = None
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1893, in moe_forward
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 323, in forward_impl
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     final_hidden_states = self.quant_method.apply(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 131, in apply
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return moe_comm_method.fused_experts(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 121, in fused_experts
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     results = self.token_dispatcher.token_dispatch(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/workspace/Qwen3-Omni/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 375, in token_dispatch
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     torch_npu.npu_moe_init_routing_v2(
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is SelfAttentionOperation.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815] [ERROR] 2025-11-27-12:40:30 (PID:8549, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]
(Worker_TP0 pid=8549) ERROR 11-27 12:40:30 [multiproc_executor.py:815]
(EngineCore_DP0 pid=8413) ERROR 11-27 12:40:30 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.11.2) with config: model='/root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-Omni-30B-A3B-Thinking', speculative_config=None, tokenizer='/root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-Omni-30B-A3B-Thinking', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=65536, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-Omni-30B-A3B-Thinking, enable_prefix_caching=True, enable_chunked_prefill=True, pooler_config=None, compilation_config={'level': None, 'mode': <CompilationMode.VLLM_COMPILE: 3>, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'eager', 'custom_ops': ['all'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_mla_attention', 'vllm::unified_mla_attention_with_output', 'vllm::mamba_mixer2', 'vllm::mamba_mixer', 'vllm::short_conv', 'vllm::linear_attention', 'vllm::plamo2_mamba_mixer', 'vllm::gdn_attention_core', 'vllm::kda_attention', 'vllm::sparse_attn_indexer', 'vllm::mla_forward', 'vllm::mla_forward'], 'compile_mm_encoder': False, 'use_inductor': False, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.PIECEWISE: 1>, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 24, 64, 104, 144, 184, 224, 272, 352, 432, 512], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': 512, 'local_cache_dir': None},
```
