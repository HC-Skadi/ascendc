# Issue #1970: [RFC]: Refactor accuracy test CI

## 基本信息

- **编号**: #1970
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1970
- **创建时间**: 2025-07-23T09:43:31Z
- **关闭时间**: 2025-07-31T13:39:15Z
- **更新时间**: 2025-07-31T13:39:15Z
- **提交者**: @wxsIcey
- **评论数**: 0

## 标签

RFC

## 问题描述

### Motivation.

In the current project, whenever developers add a new model for accuracy testing, they need to modify the `strategy.matrix` in `.github/workflows/accuracy_test.yaml` and `benchmarks/scripts/run_accuracy.py`. This process is quite cumbersome.

### Proposed Change.

1.  Classify models in config.yaml by label and trigger method:
```
schedule:
  Qwen/Qwen3-30B-A3B
  Qwen/Qwen2.5-VL-7B-Instruct
  Qwen/Qwen3-8B-Base

manual-input:
  all:
    Qwen/Qwen3-30B-A3B
    Qwen/Qwen2.5-VL-7B-Instruct
    Qwen/Qwen3-8B-Base

label:
  accuracy-test:
    Qwen/Qwen3-8B-Base

  dense-accuracy-test:
    Qwen/Qwen3-8B-Base

  vl-accuracy-test:
    Qwen/Qwen2.5-VL-7B-Instruct

  moe-accuracy-test:
    Qwen/Qwen3-30B-A3B
```

2.  Define the accuracy test configs for each model, such as Qwen3-8B-Base.yaml:

```
model_name: "Qwen/Qwen3-8B-Base"
model_type: "vllm"

model_args:
  pretrained: "Qwen/Qwen3-8B-Base"
  max_model_len: 4096
  dtype: "auto"
  tensor_parallel_size: 2
  gpu_memory_utilization: 0.6

tasks:
- name: "gsm8k"
  batch_size: "auto"
  ground_truth: 0.83

- name: "ceval-valid"
  batch_size: 1
  ground_truth: 0.82

apply_chat_template: True
fewshot_as_multiturn: True
parallel_mode: "TP"
execution_mode: "ACLGraph"
num_fewshot: 5
```

3. Change matrix strategy in CI:
```
strategy:
  matrix:
    # the accuracy test will run:
    # 1. workflow_dispatch with models input
    #   - all: all of the manual input in accuracy/config.yaml
    #   - specified but not all: selected model
    # 2. PR labeled with "*-accuracy-test"
    #   - accuracy-test: accuracy-test in accuracy/config.yaml
    #   - dense-accuracy-test: dense-accuracy-test in accuracy/config.yaml
    #   - vl-accuracy-test: vl-accuracy-test in accuracy/config.yaml
    #   - moe-accuracy-test: moe-accuracy-test in accuracy/config.yaml
    model_name: ${{ fromJSON(
      (github.event_name == 'schedule' && steps.parse-config.outputs.schedule_models) ||
      (github.event_name == 'workflow_dispatch' && (
        (github.event.inputs.models == 'all' && steps.parse-config.outputs.all_models) ||
        (format('["{0}"]', github.event.inputs.models))
      ) ||
      contains(github.event.pull_request.labels.*.name, 'accuracy-test') && steps.parse-config.outputs.accuracy_test ||
      contains(github.event.pull_request.labels.*.name, 'dense-accuracy-test') && steps.parse-config.outputs.dense_accuracy_test ||
      contains(github.event.pull_request.labels.*.name, 'vl-accuracy-test') && steps.parse-config.outputs.vl_accuracy_test ||
      contains(github.event.pull_request.labels.*.name, 'moe-accuracy-test') && steps.parse-config.outputs.moe_accuracy_test
      ) }}
```

4. Test Types:    
- PR with model label: Test the accuracy of the corresponding model.    
- Manual trigger: Test the accuracy of the selected type of model.
- schedule trigger: Test the schedule model in the config.yaml.

### Feedback Period.

one week

### CC List.
@Yikun 


