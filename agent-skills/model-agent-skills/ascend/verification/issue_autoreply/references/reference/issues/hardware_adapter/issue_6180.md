# Issue #6180: [Tests] Skip unstable eagle cases to keep CI success

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
The test case `tests/e2e/singlecard/spec_decode/test_v1_spec_decode.py::test_llama_qwen_eagle_acceptance` fails occasionally, such result seems not stable with method `eagle`, for example: 
[tests/e2e/singlecard/spec_decode/test_v1_spec_decode.py::test_llama_qwen_eagle_acceptance](https://github.com/vllm-project/vllm-ascend/actions/runs/21249578476/job/61147453980?pr=6151)

This PR skips the `eagle` tests to keep CI success

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6180
- **作者**: wjunLu
- **创建时间**: 2026-01-23T07:12:31Z
- **关闭时间**: 2026-01-23T07:33:53Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6180)
