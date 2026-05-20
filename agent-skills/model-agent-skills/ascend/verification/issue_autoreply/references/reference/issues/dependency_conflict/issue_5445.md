# Issue #5445: [Bug]: Fix chunk prefill bug for long_sequence feature

## 基本信息

- **编号**: #5445
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5445
- **创建时间**: 2025-12-27T11:04:33Z
- **关闭时间**: 2026-01-05T01:16:37Z
- **更新时间**: 2026-01-05T01:16:37Z
- **提交者**: @LookAround0301
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug
When there are two requests with chunk prefill enabled in the long-sequence scenario, if one request has only 1 token during scheduling, it will be identified as a decode request and trigger an error. This PR fixes the issue.

Reproduce scripts:

```
import os
import time
import argparse
import random
import string

from vllm import LLM, SamplingParams
from datasets import load_dataset, Features, Value, Sequence
from transformers import AutoTokenizer

os.environ["HCCL_BUFFSIZE"] = "768"
os.environ["PYTORCH_NPU_ALLOC_CONF"] = "expandable_segments:True"
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
os.environ["TASK_QUEUE_ENABLE"] = "1"
os.environ["VLLM_ASCEND_ENABLE_FLASHCOMM1"] = "1"
os.environ["HCCL_OP_EXPANSION_MODE"] = "AIV"

def generate_prompts_128K(model_path, target_length):
    ft = Features({
        "id": Value("int64"),
        "context": Value("string"),
        "input": Value("string"),
        "answer": Sequence(Value("string")),
        "options": Sequence(Value("string"))
    })

    dataset_dict = load_dataset("/datasets/InfiniteBench", features=ft)
    dataset = dataset_dict["train"]

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    token_ids = []
    target_length = target_length
    current_length = 0

    for i in range(len(dataset)):
        try:
            prompt = f"{dataset['context'][i]}\n{dataset['input'][i]}"
            encoded = tokenizer(
                prompt,
                truncation=False,
                return_tensors="pt"
            )

            sample_length = encoded["input_ids"].shape[1]

            if current_length + sample_length <= target_length:
                token_ids.extend(encoded["input_ids"].squeeze(0).tolist())
                current_length += sample_length
                print(f"已添加样本 {i}，当前总长度: {current_length}/{target_length}")
            else:
                remaining = target_length - current_length
                if remaining > 0:
                    token_ids.extend(encoded["input_ids"].squeeze(0)[:remaining].tolist())
                    current_length = target_length
                    print(f"已达到目标长度 {target_length}")
                break

            if current_length >= target_length:
                break

        except Exception as e:
            print(f"处理样本 {i} 时出错: {str(e)}")
            continue

    token_ids_text = tokenizer.decode(token_ids)
    print(f"最终生成的提示词长度: {len(token_ids)}/131072 tokens")
    return token_ids_text

def generate_prompt_token_ids(input_len, batchsize):
    token_ids = [[random.randint(1,128000) for _ in range(input_len)] for _ in range(batchsize)]
    return token_ids

# Performance testing function
def run_performance(args):
    """Run performance tests and return timing results."""
    sampling_params = SamplingParams(temperature = 0.0, top_p = 0.95, ignore_eos=True, max_tokens=args.output_len)
    prompt_text = [generate_prompts_128K(args.model_path, 128*1024), generate_prompts_128K(args.model_path, 1), generate_prompts_128K(args.model_path, 9104)]
    
    # Create an LLM
    llm = LLM(
        model=args.model_path,
        trust_remote_code=True,
        enforce_eager=True,
        tensor_parallel_size=args.tp,
        data_parallel_size=args.dp,
        prefill_context_parallel_size=args.pcp,
        decode_context_parallel_size=args.dcp,
        enable_expert_parallel=True,
        max_num_batched_tokens=131000,
        max_model_len=262144,
        cp_kv_cache_interleave_size=128,
        async_scheduling=False,
        additional_config={"ascend_scheduler_config": {"enabled": False, "dynamic_eplb":False}},
        max_num_seqs=2,
        block_size=128,
        gpu_memory_utilization=0.9
    )

    print("========================= First Infer =========================")
    t0 = time.time()
    llm.generate(prompts=prompt_text, sampling_params=sampling_params)
    t1 = time.time()
    dt0 = t1 - t0
    print(f"E2E: {dt0} s")
    print("============================= First Infer finished. ============================")

    print("========================= Second Infer ===========================")
    t2 = time.time()
    for _ in range(args.iter_times):
        outputs = llm.generate(prompts=prompt_text, sampling_params=sampling_params)
    t3 = time.time()
    # Give engines time to pause their processing loops before exiting.
    time.sleep(1)
    dt1 = t3 - t2
    print(f"E2E: {dt1} s")
    for i, output in enumerate(outputs):
        generated_text = output.outputs[0].text
        print(f"req_num: {i}\nGenerated text: {generated_text!r}")
    print("============================= Second Infer finished. ============================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_len', type=int, default=128*1024)
    parser.add_argument('--chunk_size', type=int, default=128*1024)
    parser.add_argument('--output_len', type=int, default=1)
    parser.add_argument('--bs', type=int, default=1)
    parser.add_argument('--model_path', type=str, default="/mnt/weight/Qwen3-235B-A22B-Instruct-2507")
    parser.add_argument('--tp', type=int, default=8)
    parser.add_argument('--pcp', type=int, default=2)
    parser.add_argument('--dcp', type=int, default=2)
    parser.add_argument('--dp', type=int, default=1)
    parser.add_argument('--iter_times', type=int, default=1)

    args = parser.parse_args()
    run_performance(args)
```

vllm version: v0.13.0
vllm-ascend version: 2ef4d1979e311656cb537b6b5557d94b035696a0
hardware:Atlas A3

Error information:

```
DumpHead: AIV-27, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 72 out of range[0 72)!
DumpHead: AIV-27, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 72 out of range[0 72)!
DumpHead: AIV-27, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 72 out of range[0 72)!
DumpHead: AIV-28, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 74 out of range[0 72)!
DumpHead: AIV-28, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 74 out of range[0 72)!
DumpHead: AIV-29, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 75 out of range[0 72)!
DumpHead: AIV-29, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 75 out of range[0 72)!
DumpHead: AIV-28, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 74 out of range[0 72)!
DumpHead: AIV-29, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 75 out of range[0 72)!
DumpHead: AIV-27, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 72 out of range[0 72)!
DumpHead: AIV-28, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 74 out of range[0 72)!
DumpHead: AIV-29, CoreType=AIV, block dim=48, total_block_num=48, block_remain_len=640, block_initial_space=1024, rsv=0, magic=5aa5bccd
[ASSERT] [CANN_VERSION : 8.5.0][TimeStamp : 0] /home/phisik3/Ascend/8.5.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 75 out of range[0 72)!
```

we have fixed this bug in 

https://github.com/vllm-project/vllm-ascend/pull/5444
