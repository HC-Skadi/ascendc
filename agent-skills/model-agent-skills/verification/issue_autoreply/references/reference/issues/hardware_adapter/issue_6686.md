# Issue #6686: [Platform] Enable ARM-only CPU binding with NUMA-balanced A3 policy and update docs/tests

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

- Keeps enable_cpu_binding default on, but skips binding on non‑ARM CPUs inside bind_cpus, with a clear log.
- Uses a table-driven binding policy: A3 uses NUMA‑balanced binding; other device types use NUMA‑affinity binding.
- Updates docs to reflect the exact behavior and adds/updates unit tests for the new logic.

### Does this PR introduce _any_ user-facing change?

- Yes. CPU binding is now enabled by default via additional_config, and documented in the user guide.
- CPU binding behavior differs by device type (A3 vs. others).

### How was this patch tested?

Added/updated unit tests:

test_cpu_binding.py
1.   test_binding_mode_table covers A2 vs A3 binding mode mapping.
2.   test_build_cpu_pools_fallback_to_numa_balanced covers fallback when affinity info is missing.
3.   TestBindingSwitch.test_is_arm_cpu covers ARM/x86/unknown arch detection.
4.   test_bind_cpus_skip_non_arm covers non‑ARM skip path in bind_cpus.

test_

## 基本信息
- **编号**: #6686
- **作者**: chenchuw886
- **创建时间**: 2026-02-11T07:53:40Z
- **关闭时间**: 2026-02-25T03:15:14Z
- **标签**: documentation, module:tests, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6686)
