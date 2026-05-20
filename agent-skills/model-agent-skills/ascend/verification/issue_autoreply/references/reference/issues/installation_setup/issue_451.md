# Issue #451: [Usage]: Qwen2.5VL inference speed is unusually slow, something wrong within my usage?

## 基本信息

- **编号**: #451
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/451
- **创建时间**: 2025-04-01T03:17:24Z
- **关闭时间**: 2025-05-16T02:18:08Z
- **更新时间**: 2025-05-16T02:18:09Z
- **提交者**: @liuyijiang1994
- **评论数**: 6

## 标签

无

## 问题描述

### Your current environment


Qwen2.5VL 32B inference speed is unusually slow, with 2x Ascend 910 cards (TP=2), achieving only about 8~9 tokens/s.

I'd like to ask what the normal speed would be approximately?

```python
MODEL_PATH='Qwen2.5-VL-32B-Instruct'
llm = LLM(
    model=MODEL_PATH,
    max_model_len=16384,
    max_num_seqs=1,
    limit_mm_per_prompt={"image": 2},
    tensor_parallel_size=2,
    distributed_executor_backend="mp",
)

sampling_params = SamplingParams(
    max_tokens=512
)
```

### current environment

driver version.info
```text
     1  Version=24.1.rc3
     2  ascendhal_version=7.35.23
     3  aicpu_version=1.0
     4  tdt_version=1.0
     5  log_version=1.0
     6  prof_version=2.0
     7  dvppkernels_version=1.1
     8  tsfw_version=1.0
     9  Innerversion=V100R001C19SPC001B124
    10  compatible_version=[V100R001C13],[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19]
    11  compatible_version_fw=[7.0.0,7.5.99]
    12  package_version=24.1.rc3
```
ascend-toolkit version.info
```
     1  # version: 1.0
     2  runtime_running_version=[7.6.0.1.220:8.0.0]
     3  compiler_running_version=[7.6.0.1.220:8.0.0]
     4  hccl_running_version=[7.6.0.1.220:8.0.0]
     5  opp_running_version=[7.6.0.1.220:8.0.0]
     6  toolkit_running_version=[7.6.0.1.220:8.0.0]
     7  aoe_running_version=[7.6.0.1.220:8.0.0]
     8  ncs_running_version=[7.6.0.1.220:8.0.0]
     9  opp_kernel_running_version=[7.6.0.1.220:8.0.0]
    10  runtime_upgrade_version=[7.6.0.1.220:8.0.0]
    11  compiler_upgrade_version=[7.6.0.1.220:8.0.0]
    12  hccl_upgrade_version=[7.6.0.1.220:8.0.0]
    13  opp_upgrade_version=[7.6.0.1.220:8.0.0]
    14  toolkit_upgrade_version=[7.6.0.1.220:8.0.0]
    15  aoe_upgrade_version=[7.6.0.1.220:8.0.0]
    16  ncs_upgrade_version=[7.6.0.1.220:8.0.0]
    17  opp_kernel_upgrade_version=[7.6.0.1.220:8.0.0]
    18  runtime_installed_version=[7.6.0.1.220:8.0.0]
    19  compiler_installed_version=[7.6.0.1.220:8.0.0]
    20  hccl_installed_version=[7.6.0.1.220:8.0.0]
    21  opp_installed_version=[7.6.0.1.220:8.0.0]
    22  toolkit_installed_version=[7.6.0.1.220:8.0.0]
    23  aoe_installed_version=[7.6.0.1.220:8.0.0]
    24  ncs_installed_version=[7.6.0.1.220:8.0.0]
    25  opp_kernel_installed_version=[7.6.0.1.220:8.0.0]
```
atb version.info
```
     1      Ascend-cann-atb : 8.0.0
     2      Ascend-cann-atb Version : 8.0.0.B100
     3      Platform : aarch64
     4      branch : br_release_cann_8.0.0_20250521
     5      commit id : af0ec2e868267322b4fb7949da3ae7af769d9644
```

ascend_tool_box_install.info
```
     1  version=6.0.RC1
     2  arch=aarch64
     3  os=linux
     4  path=/usr/local/Ascend/toolbox/6.0.RC1
     5  build=Ascend-mindx-toolbox_6.0.RC1-aarch64
     6  a500=n
     7  a200=n
     8  a200isoc=n
```

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.


