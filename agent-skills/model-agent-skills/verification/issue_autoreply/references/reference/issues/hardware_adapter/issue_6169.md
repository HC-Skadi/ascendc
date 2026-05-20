# Issue #6169: [Main2Main] Upgrade vllm commit to 0123

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. ✅ Upgrade vllm commit to: 0115 (8471b27df97c3eb79f891802fc0e858f8f7ac6a0)
Modify import paths due to the refactors：
https://github.com/vllm-project/vllm/pull/32245
https://github.com/vllm-project/vllm/pull/32060
Test result: https://github.com/vllm-project/vllm-ascend/actions/runs/21034239336/job/60490156965?pr=5913
2.  ✅Upgrade vllm commit to: 0119 (9a1f16da1e423ede2c2f52a9850cbfbb39cefe96)
Fix `WorkerProc.__init__() missing 1 required positional argument: 'is_driver_worker'` due to https://github.com/vllm-project/vllm/pull/28506
Test result: https://github.com/vllm-project/vllm-ascend/actions/runs/21156263050/job/60841668755?5569
3.  ✅Upgrade vllm commit to: 0120(148117ea2e689cd43df4be6892671a17cdae5833)
     1. Add `skip_compiled` param in `set_forward_context` due to https://github.com/vllm-project/vllm/pull/30385 
     2. Modify  `tests/ut/spec_decode/test_eagle_proposer.py` due to https://github.com/vllm-project/vllm/pull/2432

## 基本信息
- **编号**: #6169
- **作者**: Meihan-chen
- **创建时间**: 2026-01-23T02:30:47Z
- **关闭时间**: 2026-01-27T00:44:36Z
- **标签**: documentation, ci/build, module:tests, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6169)
