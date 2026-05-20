# Issue #807: [RFC]:  Custom Ascendc Kernel Of 'Prepare Input' in Multi-Step Feature.

## 基本信息

- **编号**: #807
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/807
- **创建时间**: 2025-05-11T11:18:52Z
- **关闭时间**: 2025-07-12T17:22:15Z
- **更新时间**: 2025-07-12T17:22:16Z
- **提交者**: @wonderful199082
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

In the current implementation of `vLLM_Ascend` V0 Engine, the `advance_step` function in `attention.py` contains a section of Python-based logic that handles the update of `input_tokens`, `seq_lens`, `input_positions`, and `slot_mapping`.

This logic was marked with a clear `TODO`:
```python
# TODO optimize these codes using ascendc just like flash attention backend using cuda
```
indicating an explicit need for optimization using custom operators.

### Proposed Change.

This RFC proposes to replace the above Python logic with a highly optimized custom operator implemented in AscendC, designed to execute directly on the NPU for improved efficiency in multi-step decoding scenarios.

The logic covered by this operator includes:
- Updating `model_input.input_tokens`
- Updating `model_input.input_positions`
- Incrementing and updating `seq_lens_tensor`
- Computing `slot_mapping` using `block_tables`

### Feedback Period.

This RFC will be open for feedback until **[2025-05-18]**, which is one week from the initial submission date.

Please leave your comments, questions, or suggestions before this date. The author will address all feedback and revise the proposal accordingly if needed.

### CC List.

@Yikun @wangxiyuan 

### Any Other Things.

_No response_
