# Issue #6499: [CI] Add long and short prompt tests for DeepSeek-V3.2

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR enhances the test_deepseek3_2_w8a8_pruning_mtp_tp2_ep E2E test by adding both short and long prompt test cases:                                                                                                                   
                                                                                                                                                                                                                                            
- Short test: Validates basic functionality with minimal input ("Hello ")                                                                                                                                                                 
- Long test: Validates the model can handle prompts near its maximum context length (~163K tokens, approaching the max_position_embeddings limit of 163,840)                                                                              
           

## 基本信息
- **编号**: #6499
- **作者**: starmountain1997
- **创建时间**: 2026-02-03T03:00:35Z
- **关闭时间**: 2026-02-04T01:10:50Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6499)
