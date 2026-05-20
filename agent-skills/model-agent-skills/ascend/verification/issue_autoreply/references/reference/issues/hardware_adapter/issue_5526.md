# Issue #5526: [CI] Recover full custom ops test

**类型**: Pull Request

## 问题背景
…i-card tests based on NPU availability- Remove hardcoded --ignore flags from nightly workflowFixes #5336

### What this PR does / why we need it?
This PR re-enables several custom operator tests in the nightly CI workflow that were previously bypassed using --ignore flags.

The bypassed tests included:

test_dispatch_ffn_combine.py
 (Requires 2 NPUs)
test_matmul_allreduce_add_rmsnorm.py
 (Requires 8 NPUs)
test_fused_moe.py
 (Single NPU)
test_rotary_embedding.py
 (Single NPU)
The issue occurred because multi-card tests were failing on single-NPU CI runners. To resolve this without globally ignoring the tests, this PR implements the following:

Adds pytest.mark.skipif decorators to 
test_dispatch_ffn_combine.py
 and 
test_matmul_allreduce_add_rmsnorm.py
 to check for the required number of NPU devices at runtime.
Removes the hardcoded --ignore flags from 
.github/workflows/_e2e_nightly_single_node.yaml
.
This change ensures that single-card tests are executed, w

## 基本信息
- **编号**: #5526
- **作者**: bv-saketha-rama
- **创建时间**: 2025-12-30T10:08:49Z
- **关闭时间**: 2026-01-13T08:20:32Z
- **标签**: ci/build, module:tests, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5526)
