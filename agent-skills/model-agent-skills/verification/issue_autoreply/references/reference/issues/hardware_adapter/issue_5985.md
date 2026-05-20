# Issue #5985: [Main2Main] Upgrade vllm commit to 0122

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. ✅ Upgrade vllm commit to: 0115 (8471b27df97c3eb79f891802fc0e858f8f7ac6a0)
Modify import paths due to the refactors：
https://github.com/vllm-project/vllm/pull/32245
https://github.com/vllm-project/vllm/pull/32060
Test result: https://github.com/vllm-project/vllm-ascend/actions/runs/21034239336/job/60490156965?pr=5913
3. Upgrade vllm commit to: 0116 (46f8a982b191e3a3d3a1eccaf18b184c391ac2ac)
4. Upgrade vllm commit to: 0119 (9a1f16da1e423ede2c2f52a9850cbfbb39cefe96)
Fix `WorkerProc.__init__() missing 1 required positional argument: 'is_driver_worker'` due to https://github.com/vllm-project/vllm/pull/28506
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060


## 基本信息
- **编号**: #5985
- **作者**: Meihan-chen
- **创建时间**: 2026-01-19T02:24:48Z
- **关闭时间**: 2026-01-27T00:44:55Z
- **标签**: documentation, ci/build, ready, ready-for-test, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5985)
