# Issue #6421: [Bug]: EngineCore crash: AssertionError with MTP and Structured Output in PD Disaggregation mode

**类型**: Issue

## 问题背景
### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

### Prerequisites
* [x] I have searched the existing issues and didn't find a similar bug.
* [x] I am using the official `vllm-ascend:0.13.0rc2` image.

### Description
When using **PD Disaggregation** to serve **DeepSeek-V3.2** with **Structured Output** enabled, the decoding vLLM instance crashes with an `AssertionError`. 

The issue appears to be caused by the Multi-Token Prediction (MTP) logic passing invalid token IDs (`-1`) to the `XGrammar` backend. While the C++ grammar matcher rejects the token, the Python layer triggers a fatal assertion when it fails to advance the FSM for these invalid IDs.

The issue is resolved by disabling MTP, but this prevents utilizing the full performance capabilities of the DeepSeek-V3.2 architecture.

### Error Logs
```
[06:07:45] /project/cpp/grammar_matcher.cc:428: W

## 基本信息
- **编号**: #6421
- **作者**: triomino
- **创建时间**: 2026-01-30T07:39:16Z
- **关闭时间**: 2026-01-30T09:04:49Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/6421)
