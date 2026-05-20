# Issue #1043: [Bug][V1]: Qwen/Qwen2.5-7B-Instruct accuracy  ceval-valid failed

## 基本信息

- **编号**: #1043
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1043
- **创建时间**: 2025-06-03T01:57:36Z
- **关闭时间**: 2025-06-28T01:38:53Z
- **更新时间**: 2025-06-28T01:38:53Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

vLLM Ascend main, v0.9.0

### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/actions/runs/15397909461/attempts/2#summary-43344496525

# 🎯 Qwen2.5-7B-Instruct Accuracy Test
  <div>
    <strong>vLLM version:</strong> vLLM: 0.9.0, vLLM Ascend: refs/pull/1040/merge <br>
  </div>
  <div>
      <strong>Software Environment:</strong> CANN: 8.1.RC1, PyTorch: 2.5.1, torch-npu: 2.5.1 <br>
  </div>
  <div>
      <strong>Hardware Environment</strong>: Atlas A2 Series <br>
  </div>
  <div>
      <strong>Datasets</strong>: ceval-valid,gsm8k <br>
  </div>
  <div>
      <strong>Command</strong>: 

  ```bash
  export MODEL_ARGS='pretrained=Qwen/Qwen2.5-7B-Instruct, max_model_len=4096,dtype=auto,tensor_parallel_size=2,gpu_memory_utilization=0.6'
lm_eval --model vllm --modlel_args $MODEL_ARGS --tasks ceval-valid,gsm8k \ 
--apply_chat_template --fewshot_as_multiturn --num_fewshot 5 --batch_size 1
  ```
  </div>
  <div>&nbsp;</div>
  
| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| ceval-valid(V1)                           | none   | 5      | acc    | ***0.2303*** <----- | ± 0.0115 |
| ceval-valid(V0)                           | none   | 5      | acc    | ***0.8001*** | ± 0.0105 |



