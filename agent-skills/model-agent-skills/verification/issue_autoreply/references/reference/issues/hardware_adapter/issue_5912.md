# Issue #5912: [Lint]Style: Convert `vllm-ascend/` to ruff format(Batch #1)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Convert `vllm-ascend/compilation` to ruff format.

### Does this PR introduce _any_ user-facing change?
During this migration, we encountered some **errors** in our CI and testing environments, such as:
```
vllm_ascend/utils.py:653: in <module>
    def register_ascend_customop(vllm_config: VllmConfig | None = None):
                                              ^^^^^^^^^^^^^^^^^
E   TypeError: unsupported operand type(s) for |: 'NoneType' and 'NoneType'
```

**1. Root Cause Analysis:**
The project uses a common pattern to break circular dependencies:
```python
if TYPE_CHECKING:
    from vllm.config import VllmConfig
else:
    VllmConfig = None  # Placeholder assigned at runtime
```
When Python parses the function definition `def register_ascend_customop(vllm_config: VllmConfig | None)`, it attempts to evaluate the expression `VllmConfig | None`.
Since `VllmConfig` is assigned `None` at runtime, the expression effectively beco

## 基本信息
- **编号**: #5912
- **作者**: MrZ20
- **创建时间**: 2026-01-15T02:56:38Z
- **关闭时间**: 2026-01-16T12:57:46Z
- **标签**: module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5912)
