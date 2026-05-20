# Issue #5636: [BUG]Structured output crash on v0.13.0rc1/main: xgrammar indices type mismatch

**类型**: Issue

## 问题背景
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
This replaces the previous local implementation (which passed l

## 基本信息
- **编号**: #5636
- **作者**: M4n5ter
- **创建时间**: 2026-01-06T07:09:31Z
- **关闭时间**: 2026-01-06T07:29:54Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5636)
