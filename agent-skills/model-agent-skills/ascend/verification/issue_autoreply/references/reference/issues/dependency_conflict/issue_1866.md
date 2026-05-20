# Issue #1866: [Bug]: Failed to benchmark on main

## 基本信息

- **编号**: #1866
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1866
- **创建时间**: 2025-07-18T03:21:42Z
- **关闭时间**: 2025-08-05T00:43:25Z
- **更新时间**: 2025-08-05T00:43:25Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

```
Traceback (most recent call last):
  File "/vllm-workspace/vllm/benchmarks/benchmark_serving.py", line 1384, in <module>
    main(args)
  File "/vllm-workspace/vllm/benchmarks/benchmark_serving.py", line 728, in main
    tokenizer = get_tokenizer(
  File "/vllm-workspace/vllm/vllm/transformers_utils/tokenizer.py", line 185, in get_tokenizer
    from vllm.model_executor.model_loader.weight_utils import get_lock
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 10, in <module>
    from vllm.model_executor.model_loader.bitsandbytes_loader import (
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/bitsandbytes_loader.py", line 23, in <module>
    from vllm.model_executor.layers.fused_moe import FusedMoE
  File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/__init__.py", line 8, in <module>
    from vllm.model_executor.layers.fused_moe.layer import (
  File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 26, in <module>
    from vllm.model_executor.layers.fused_moe.modular_kernel import (
  File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/modular_kernel.py", line 13, in <module>
    from vllm.model_executor.layers.fused_moe.utils import (  # yapf: disable
  File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/utils.py", line 9, in <module>
    from vllm.model_executor.layers.quantization.utils.fp8_utils import (
  File "/vllm-workspace/vllm/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 207, in <module>
    direct_register_custom_op(
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2527, in direct_register_custom_op
    schema_str = torch.library.infer_schema(op_func,
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_library/infer_schema.py", line 106, in infer_schema
    error_fn(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_library/infer_schema.py", line 58, in error_fn
    raise ValueError(
ValueError: infer_schema(func): Parameter block_size has unsupported type list[int]. The valid types are: dict_keys([<class 'torch.Tensor'>, typing.Optional[torch.Tensor], typing.Sequence[torch.Tensor], typing.List[torch.Tensor], typing.Sequence[typing.Optional[torch.Tensor]], typing.List[typing.Optional[torch.Tens
or]], <class 'int'>, typing.Optional[int], typing.Sequence[int], typing.List[int], typing.Optional[typing.Sequence[int]], typing.Optional[typing.List[int]], <class 'float'>, typing.Optional[float], typing.Sequence[float], typing.List[float], typing.Optional[typing.Sequence[float]], typing.Optional[typing.List[float
]], <class 'bool'>, typing.Optional[bool], typing.Sequence[bool], typing.List[bool], typing.Optional[typing.Sequence[bool]], typing.Optional[typing.List[bool]], <class 'str'>, typing.Optional[str], typing.Union[int, float, bool], typing.Union[int, float, bool, NoneType], typing.Sequence[typing.Union[int, float, boo
l]], typing.List[typing.Union[int, float, bool]], <class 'torch.dtype'>, typing.Optional[torch.dtype], <class 'torch.device'>, typing.Optional[torch.device]]). Got func with signature (input: torch.Tensor, weight: torch.Tensor, block_size: list[int], weight_scale: torch.Tensor, input_scale: Optional[torch.Tensor] =
 None, bias: Optional[torch.Tensor] = None, cutlass_block_fp8_supported: bool = False, use_aiter_and_is_supported: bool = False) -> torch.Tensor)
```

### 🐛 Describe the bug

Workaround
```diff
diff --git a/benchmarks/benchmark_serving.py b/benchmarks/benchmark_serving.py
index f3a208421..833d4ebc2 100644
--- a/benchmarks/benchmark_serving.py
+++ b/benchmarks/benchmark_serving.py
@@ -46,6 +46,8 @@ from backend_request_func import (
     RequestFuncOutput,
 )

+import vllm_ascend.patch.worker.patch_common.patch_utils
+
 try:
     from vllm.transformers_utils.tokenizer import get_tokenizer
 except ImportError:
```
