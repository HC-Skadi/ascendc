# Issue #5636: [BUG]Structured output crash on v0.13.0rc1/main: xgrammar indices type mismatch

## 基本信息

- **编号**: #5636
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5636
- **创建时间**: 2026-01-06T07:09:31Z
- **关闭时间**: 2026-01-06T07:29:54Z
- **更新时间**: 2026-02-11T09:18:52Z
- **提交者**: @M4n5ter
- **评论数**: 3

## 标签

无

## 问题描述

### Summary
On v0.13.0rc1 and main images, vLLM-Ascend crashes on the first request when structured outputs / tool-call is enabled. v0.12.0rc1 does not have this issue.

### Environment
- vllm-ascend image: v0.13.0rc1 (also reproducible on main)
- Device: Ascend 910B
- Running `vllm serve` with structured output enabled (e.g., `--enable-auto-tool-choice --tool-call-parser hermes`)

### Reproduction
1. Start v0.13.0rc1 image.
2. Run `vllm serve` with structured output enabled.
3. Send any request that triggers structured output (tool-call / JSON schema / grammar).
4. Engine crashes.

### Expected
Requests with structured outputs run normally.

### Actual
Crash with:
```
TypeError: apply_token_bitmask_inplace_cpu(): incompatible function arguments
... expected indices: Sequence[int] | None, got torch.Tensor
```

### Suspected regression
Between v0.12.0rc1 and v0.13.0rc1. The direct trigger appears to be:
- `ddd475d5` (#4974)
This replaces the previous local implementation (which passed list indices) with vLLM's `apply_grammar_bitmask`, which ultimately passes a `torch.Tensor` to xgrammar on CPU.

Possibly related: `8d2998d0` upgrade vLLM hash to 12_14.

### Potential fixes
- Convert `indices` to `list[int]` before calling xgrammar on CPU, or
- Bump xgrammar to a version that accepts tensor indices.

