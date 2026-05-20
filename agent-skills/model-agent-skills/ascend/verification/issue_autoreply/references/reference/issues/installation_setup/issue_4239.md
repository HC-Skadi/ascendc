# Issue #4239: [RFC]:  Ops fusion for vLLM-Ascend using Inductor Pattern Matcher

## 基本信息

- **编号**: #4239
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4239
- **创建时间**: 2025-11-18T02:43:25Z
- **关闭时间**: 2025-12-29T11:08:46Z
- **更新时间**: 2025-12-29T11:08:46Z
- **提交者**: @wxsIcey
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

Currently, the vLLM project’s high-performance execution path relies heavily on **PyTorch Inductor** to perform automatic kernel fusion. However, for vLLM-Ascend, we face two major limitations:

1. **torch-npu Limited Support for Inductors**
- Inductor consists of two parts: the first part is the preprocessing and standardization of the fx graph, and the second part is the operator fusion through codegen combined with trtion.Currently torch-npu does not support the second part.

2. **High Maintenance Burden from Model Duplication**
```
    def forward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor:
        qkv, _ = self.qkv_proj(hidden_states)
        q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)
        # Add qk-norm
        q_by_head = q.view(*q.shape[:-1], q.shape[-1] // self.head_dim, self.head_dim)
        q_by_head = self.q_norm(q_by_head)
        q = q_by_head.view(q.shape)
        k_by_head = k.view(*k.shape[:-1], k.shape[-1] // self.head_dim, self.head_dim)
        k_by_head = self.k_norm(k_by_head)
        k = k_by_head.view(k.shape)
        q, k = self.rotary_emb(positions, q, k)
        attn_output = self.attn(q, k, v)
        output, _ = self.o_proj(attn_output)
        return output
```

```
    def forward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor:
        qkv, _ = self.qkv_proj(hidden_states)
        q, k, v = split_qkv_rmsnorm_rope(
            qkv,
            self.rotary_emb.sin,
            self.rotary_emb.cos,
            self.q_norm.weight,
            self.k_norm.weight,
            self.q_size,
            self.kv_size,
            self.head_dim,
            self.q_norm.variance_epsilon,
            None,
            None
        )
        attn_output = self.attn(q, k, v)
        output, _ = self.o_proj(attn_output)
        return output
```


Without an automatic fusion mechanism, Ascend NPU execution suffers from suboptimal kernel launch patterns, leading to:
- Higher latency due to excessive kernel dispatch.
- Poor hardware utilization.

We need a solution that:
- **This implementation achieves NPU-specific fusion in vllm-ascend, and this fusion method is easily scalable.**


### Proposed Change.

We propose implementing an **Automatic Kernel Fusion Compiler Interface** for Ascend NPUs that:
- Operates on **torch.fx.graph** extracted from original vllm models.
- Uses **Inductor Pattern Match API** to:

    - Match known computational subgraphs that can be fused.
    - Replace them with fused kernels implemented in `torch_npu`.

Runs before the model is executed, ensuring the runtime graph is already optimized for Ascend NPUs.

**Design Overview**

Our approach builds on the existing **vllm** execution pipeline while replacing only the Inductor-specific fusion logic with an NPU-compatible implementation. The key changes are:

1. **Leverage vLLM’s Existing `VllmBackend` Path**

- We keep the original `VllmBackend` execution flow in place.
- Inside this flow, we intercept and replace the `PostGradPassManager` with our own `GraphFusionPassManager`, which will host all NPU-specific graph fusion passes.

2. **Custom Fusion Pass Implementation**
- We implement our fusion pass by inheriting from vllm’s `VllmInductorPass`.
- This allows us to:
    - Reuse vLLM’s existing FX graph inspection and debugging utilities.
    - Keep the fusion logic consistent with vLLM’s pass structure.

3. **Adopt an NPU-Specific Compiler Interface**
- We introduce our own compiler interface that integrates with `torch.compile`.
- This compiler interface will:
    - Receive the FX graph from the compiled model.
    - Apply the `GraphFusionPassManager` to perform inductor pattern match and kernel fusions.
    - Return the optimized `GraphModule` for execution on Ascend NPU.

By integrating at the `VllmBackend` level and reusing `VllmInductorPass` infrastructure, we minimize code duplication, retain compatibility with upstream vLLM’s debug and inspection tools.

**Integration Example For a Fusion Pass**
Below is a practical example showing how to implement and integrate a custom fusion pass into the ```GraphFusionPassManager```.

**Step 1: Write a Specific Fusion Pass**
We define a fusion pass that registers a pattern to fuse ```torch.ops.npu.npu_add_rms_norm``` followed by ```torch.ops.npu.npu_quantize``` into a single ```torch.ops.npu.npu_add_rms_norm_quant``` op.
```python
class AddRMSNormQuantPattern:

    def __init__(self, vllm_config):
        self.vllm_config = vllm_config

    def get_inputs(self):
        """
        Generate example inputs for the AddRMSNormQuant fusion pattern.
        """
        rms_norm_input = torch.randn(2, 4, device="npu")
        residual = torch.randn(2, 4, device="npu")
        rms_norm_weight = torch.randn(4, device="npu")
        scale = torch.tensor([1.0], device="npu")
        offset = torch.tensor([0.0], device="npu")
        return [rms_norm_input, residual, rms_norm_weight, scale, offset]

    def register(self, pm_pass: PatternMatcherPass):

        def pattern(rms_norm_input, residual, rms_norm_weight, scale, offset):
            """
          Pattern for AddRMSNormQuant fusion.
          """
            output = torch.ops.npu.npu_add_rms_norm(rms_norm_input, residual,
                                                    rms_norm_weight, 1e-6)
            out0 = output[0]
            out1 = output[2]
            quantized_output = torch.ops.npu.npu_quantize(
                out0, scale, offset, torch.qint8, -1, False)
            return quantized_output, out1

        def replacement(rms_norm_input, residual, rms_norm_weight, scale,
                        offset):
            """
          Replacement for the AddRMSNormQuant fusion.
          """
            output = torch.ops.npu.npu_add_rms_norm_quant(
                rms_norm_input,
                residual,
                rms_norm_weight,
                1. /
                scale,  # The inverse of scale is required by npu_add_rms_norm_quant kernel which is opposite to the npu_quantize kernel.
                offset,
                epsilon=1e-6)
            quantized_output = output[0]
            out1 = output[2]
            return quantized_output, out1

        pm.register_replacement(pattern, replacement, self.get_inputs(),
                                pm.fwd_only, pm_pass)


class AscendQuantFusionPass(VllmInductorPass):
    """
    A pass for fusing AddRMSNorm and W8A8 quantization operations on Ascend.
    """

    def __init__(self, vllm_config):
        super().__init__(vllm_config)
        self.patterns: PatternMatcherPass = PatternMatcherPass(
            pass_name="rmsnorm_quant_fusion_pass")
        AddRMSNormQuantPattern(vllm_config).register(self.patterns)

    def __call__(self, graph: torch.fx.Graph):
        self.begin()
        matched_count = self.patterns.apply(graph)
        self.end_and_log()

    def is_applicable(self, **kwargs):
        """
        Check if the pass is applicable for the current configuration.
        """
        return True
```

**Step 2: Add the Pass to the Pass Manager via configure**
```python
class GraphFusionPassManager:
....
    def configure(self, config: VllmConfig):
        # By default, we enable the graph rewriter and quantization fusion pass.
        self.ascend_compilation_config: dict = config.additional_config.get(
            "ascend_compilation_config", {})
        if self.ascend_compilation_config.get("enable_quantization_fusion",
                                              True):
            from .quant_fusion_pass import AscendQuantFusionPass
            self.passes.append(AscendQuantFusionPass(config))
        # Add more passes here as needed
```
By doing the above two step, the fusion will automaically happened inside the torch.compile in our target scenario. As we can see the graph structure below .

```
before graph is: 
graph():
%arg0_1 : [num_users=4] = placeholder[target=arg0_1]
%arg1_1 : [num_users=9] = placeholder[target=arg1_1]
%arg2_1 : [num_users=1] = placeholder[target=arg2_1]
%arg3_1 : [num_users=1] = placeholder[target=arg3_1]
%arg4_1 : [num_users=1] = placeholder[target=arg4_1]
%arg5_1 : [num_users=1] = placeholder[target=arg5_1]
%arg6_1 : [num_users=1] = placeholder[target=arg6_1]
%arg7_1 : [num_users=1] = placeholder[target=arg7_1]
%arg8_1 : [num_users=1] = placeholder[target=arg8_1]
%arg9_1 : [num_users=1] = placeholder[target=arg9_1]
%arg10_1 : [num_users=1] = placeholder[target=arg10_1]
%arg11_1 : [num_users=1] = placeholder[target=arg11_1]
%arg12_1 : [num_users=1] = placeholder[target=arg12_1]
%arg13_1 : [num_users=1] = placeholder[target=arg13_1]
%arg14_1 : [num_users=1] = placeholder[target=arg14_1]
%arg15_1 : [num_users=1] = placeholder[target=arg15_1]
%arg16_1 : [num_users=1] = placeholder[target=arg16_1]
%arg17_1 : [num_users=1] = placeholder[target=arg17_1]
%arg18_1 : [num_users=1] = placeholder[target=arg18_1]
%arg19_1 : [num_users=1] = placeholder[target=arg19_1]
%arg20_1 : [num_users=1] = placeholder[target=arg20_1]
%arg21_1 : [num_users=1] = placeholder[target=arg21_1]
%arg22_1 : [num_users=1] = placeholder[target=arg22_1]
%arg23_1 : [num_users=0] = placeholder[target=arg23_1]
%arg24_1 : [num_users=0] = placeholder[target=arg24_1]
%arg25_1 : [num_users=0] = placeholder[target=arg25_1]
%slice_1 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%arg0_1, 1, 0, 9223372036854775807), kwargs = {})
%slice_2 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%slice_1, 2, 0, 9223372036854775807), kwargs = {})
%slice_3 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%arg0_1, 1, 0, 9223372036854775807), kwargs = {})
%slice_4 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%slice_3, 2, 0, 9223372036854775807), kwargs = {})
%copy : [num_users=1] = call_function[target=torch.ops.aten.copy.default](args = (%slice_4, %slice_2), kwargs = {})
%slice_5 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%arg0_1, 1, 0, 9223372036854775807), kwargs = {})
%slice_scatter : [num_users=1] = call_function[target=torch.ops.aten.slice_scatter.default](args = (%slice_5, %copy, 2, 0, 9223372036854775807), kwargs = {})
%slice_scatter_1 : [num_users=2] = call_function[target=torch.ops.aten.slice_scatter.default](args = (%arg0_1, %slice_scatter, 1, 0, 9223372036854775807), kwargs = {})
%view_2 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%slice_scatter_1, [-1, 4096]), kwargs = {})
%npu_quantize : [num_users=1] = call_function[target=torch.ops.npu.npu_quantize.default](args = (%view_2, %arg2_1, %arg3_1, torch.qint8, -1, False), kwargs = {})
%npu_quant_matmul : [num_users=1] = call_function[target=torch.ops.npu.npu_quant_matmul.default](args = (%npu_quantize, %arg4_1, %arg5_1), kwargs = {bias: %arg6_1, output_dtype: torch.bfloat16})
%npu_add_rms_norm : [num_users=2] = call_function[target=torch.ops.npu.npu_add_rms_norm.default](args = (%npu_quant_matmul, %arg7_1, %arg8_1), kwargs = {})
%getitem : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm, 0), kwargs = {})
%getitem_2 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm, 2), kwargs = {})
%npu_quantize_1 : [num_users=1] = call_function[target=torch.ops.npu.npu_quantize.default](args = (%getitem, %arg9_1, %arg10_1, torch.qint8, -1, False), kwargs = {})
%npu_quant_matmul_1 : [num_users=1] = call_function[target=torch.ops.npu.npu_quant_matmul.default](args = (%npu_quantize_1, %arg11_1, %arg12_1), kwargs = {bias: %arg13_1, output_dtype: torch.bfloat16})
%npu_swiglu : [num_users=1] = call_function[target=torch.ops.npu.npu_swiglu.default](args = (%npu_quant_matmul_1,), kwargs = {})
%t : [num_users=1] = call_function[target=torch.ops.aten.t.default](args = (%arg14_1,), kwargs = {})
%mm : [num_users=1] = call_function[target=torch.ops.aten.mm.default](args = (%npu_swiglu, %t), kwargs = {})
%npu_add_rms_norm_1 : [num_users=2] = call_function[target=torch.ops.npu.npu_add_rms_norm.default](args = (%mm, %getitem_2, %arg15_1), kwargs = {})
%getitem_3 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm_1, 0), kwargs = {})
%getitem_5 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm_1, 2), kwargs = {})
%npu_quantize_2 : [num_users=1] = call_function[target=torch.ops.npu.npu_quantize.default](args = (%getitem_3, %arg16_1, %arg17_1, torch.qint8, -1, False), kwargs = {})
%npu_quant_matmul_2 : [num_users=1] = call_function[target=torch.ops.npu.npu_quant_matmul.default](args = (%npu_quantize_2, %arg18_1, %arg19_1), kwargs = {bias: %arg20_1, output_dtype: torch.bfloat16})
%split_with_sizes : [num_users=3] = call_function[target=torch.ops.aten.split_with_sizes.default](args = (%npu_quant_matmul_2, [4096, 1024, 1024], -1), kwargs = {})
%getitem_6 : [num_users=1] = call_function[target=operator.getitem](args = (%split_with_sizes, 0), kwargs = {})
%getitem_7 : [num_users=1] = call_function[target=operator.getitem](args = (%split_with_sizes, 1), kwargs = {})
%getitem_8 : [num_users=1] = call_function[target=operator.getitem](args = (%split_with_sizes, 2), kwargs = {})
%view_3 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_6, [%arg1_1, 32, 128]), kwargs = {})
%npu_rms_norm : [num_users=1] = call_function[target=torch.ops.npu.npu_rms_norm.default](args = (%view_3, %arg21_1), kwargs = {})
%getitem_9 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_rms_norm, 0), kwargs = {})
%view_4 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_9, [%arg1_1, 4096]), kwargs = {})
%view_5 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_7, [%arg1_1, 8, 128]), kwargs = {})
%npu_rms_norm_1 : [num_users=1] = call_function[target=torch.ops.npu.npu_rms_norm.default](args = (%view_5, %arg22_1), kwargs = {})
%getitem_11 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_rms_norm_1, 0), kwargs = {})
%view_6 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_11, [%arg1_1, 1024]), kwargs = {})
%view_7 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_4, [1, %arg1_1, -1, 128]), kwargs = {})
%view_8 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_6, [1, %arg1_1, -1, 128]), kwargs = {})
%view_9 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_7, [%arg1_1, 4096]), kwargs = {})
%view_10 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_8, [%arg1_1, 1024]), kwargs = {})
%zeros : [num_users=1] = call_function[target=torch.ops.aten.zeros.default](args = ([%arg1_1, 4096],), kwargs = {dtype: torch.bfloat16, device: npu:0, pin_memory: False})
%detach : [num_users=1] = call_function[target=torch.ops.aten.detach.default](args = (%zeros,), kwargs = {})
%view_11 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_9, [-1, 32, 128]), kwargs = {})
%view_12 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%detach, [-1, 32, 128]), kwargs = {})
%view_13 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_10, [-1, 8, 128]), kwargs = {})
%view_14 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_8, [-1, 8, 128]), kwargs = {})
return (slice_scatter_1, view_11, view_13, view_14, view_12, getitem_5)
```

```
after graph is: 
graph():
%arg0_1 : [num_users=4] = placeholder[target=arg0_1]
%arg1_1 : [num_users=9] = placeholder[target=arg1_1]
%arg2_1 : [num_users=1] = placeholder[target=arg2_1]
%arg3_1 : [num_users=1] = placeholder[target=arg3_1]
%arg4_1 : [num_users=1] = placeholder[target=arg4_1]
%arg5_1 : [num_users=1] = placeholder[target=arg5_1]
%arg6_1 : [num_users=1] = placeholder[target=arg6_1]
%arg7_1 : [num_users=1] = placeholder[target=arg7_1]
%arg8_1 : [num_users=1] = placeholder[target=arg8_1]
%arg9_1 : [num_users=1] = placeholder[target=arg9_1]
%arg10_1 : [num_users=1] = placeholder[target=arg10_1]
%arg11_1 : [num_users=1] = placeholder[target=arg11_1]
%arg12_1 : [num_users=1] = placeholder[target=arg12_1]
%arg13_1 : [num_users=1] = placeholder[target=arg13_1]
%arg14_1 : [num_users=1] = placeholder[target=arg14_1]
%arg15_1 : [num_users=1] = placeholder[target=arg15_1]
%arg16_1 : [num_users=1] = placeholder[target=arg16_1]
%arg17_1 : [num_users=1] = placeholder[target=arg17_1]
%arg18_1 : [num_users=1] = placeholder[target=arg18_1]
%arg19_1 : [num_users=1] = placeholder[target=arg19_1]
%arg20_1 : [num_users=1] = placeholder[target=arg20_1]
%arg21_1 : [num_users=1] = placeholder[target=arg21_1]
%arg22_1 : [num_users=1] = placeholder[target=arg22_1]
%arg23_1 : [num_users=0] = placeholder[target=arg23_1]
%arg24_1 : [num_users=0] = placeholder[target=arg24_1]
%arg25_1 : [num_users=0] = placeholder[target=arg25_1]
%slice_1 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%arg0_1, 1, 0, 9223372036854775807), kwargs = {})
%slice_2 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%slice_1, 2, 0, 9223372036854775807), kwargs = {})
%slice_3 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%arg0_1, 1, 0, 9223372036854775807), kwargs = {})
%slice_4 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%slice_3, 2, 0, 9223372036854775807), kwargs = {})
%copy : [num_users=1] = call_function[target=torch.ops.aten.copy.default](args = (%slice_4, %slice_2), kwargs = {})
%slice_5 : [num_users=1] = call_function[target=torch.ops.aten.slice.Tensor](args = (%arg0_1, 1, 0, 9223372036854775807), kwargs = {})
%slice_scatter : [num_users=1] = call_function[target=torch.ops.aten.slice_scatter.default](args = (%slice_5, %copy, 2, 0, 9223372036854775807), kwargs = {})
%slice_scatter_1 : [num_users=2] = call_function[target=torch.ops.aten.slice_scatter.default](args = (%arg0_1, %slice_scatter, 1, 0, 9223372036854775807), kwargs = {})
%view_2 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%slice_scatter_1, [-1, 4096]), kwargs = {})
%npu_quantize : [num_users=1] = call_function[target=torch.ops.npu.npu_quantize.default](args = (%view_2, %arg2_1, %arg3_1, torch.qint8, -1, False), kwargs = {})
%npu_quant_matmul : [num_users=1] = call_function[target=torch.ops.npu.npu_quant_matmul.default](args = (%npu_quantize, %arg4_1, %arg5_1), kwargs = {bias: %arg6_1, output_dtype: torch.bfloat16})
%npu_add_rms_norm : [num_users=2] = call_function[target=torch.ops.npu.npu_add_rms_norm.default](args = (%npu_quant_matmul, %arg7_1, %arg8_1), kwargs = {})
%getitem : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm, 0), kwargs = {})
%getitem_2 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm, 2), kwargs = {})
%npu_quantize_1 : [num_users=1] = call_function[target=torch.ops.npu.npu_quantize.default](args = (%getitem, %arg9_1, %arg10_1, torch.qint8, -1, False), kwargs = {})
%npu_quant_matmul_1 : [num_users=1] = call_function[target=torch.ops.npu.npu_quant_matmul.default](args = (%npu_quantize_1, %arg11_1, %arg12_1), kwargs = {bias: %arg13_1, output_dtype: torch.bfloat16})
%npu_swiglu : [num_users=1] = call_function[target=torch.ops.npu.npu_swiglu.default](args = (%npu_quant_matmul_1,), kwargs = {})
%t : [num_users=1] = call_function[target=torch.ops.aten.t.default](args = (%arg14_1,), kwargs = {})
%mm : [num_users=1] = call_function[target=torch.ops.aten.mm.default](args = (%npu_swiglu, %t), kwargs = {})
%reciprocal_default : [num_users=1] = call_function[target=torch.ops.aten.reciprocal.default](args = (%arg16_1,), kwargs = {})
%mul_tensor : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%reciprocal_default, 1.0), kwargs = {})
%npu_add_rms_norm_quant_default : [num_users=2] = call_function[target=torch.ops.npu.npu_add_rms_norm_quant.default](args = (%mm, %getitem_2, %arg15_1, %mul_tensor, %arg17_1), kwargs = {})
%getitem_15 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm_quant_default, 0), kwargs = {})
%getitem_16 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_add_rms_norm_quant_default, 2), kwargs = {})
%npu_quant_matmul_2 : [num_users=1] = call_function[target=torch.ops.npu.npu_quant_matmul.default](args = (%getitem_15, %arg18_1, %arg19_1), kwargs = {bias: %arg20_1, output_dtype: torch.bfloat16})
%split_with_sizes : [num_users=3] = call_function[target=torch.ops.aten.split_with_sizes.default](args = (%npu_quant_matmul_2, [4096, 1024, 1024], -1), kwargs = {})
%getitem_6 : [num_users=1] = call_function[target=operator.getitem](args = (%split_with_sizes, 0), kwargs = {})
%getitem_7 : [num_users=1] = call_function[target=operator.getitem](args = (%split_with_sizes, 1), kwargs = {})
%getitem_8 : [num_users=1] = call_function[target=operator.getitem](args = (%split_with_sizes, 2), kwargs = {})
%view_3 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_6, [%arg1_1, 32, 128]), kwargs = {})
%npu_rms_norm : [num_users=1] = call_function[target=torch.ops.npu.npu_rms_norm.default](args = (%view_3, %arg21_1), kwargs = {})
%getitem_9 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_rms_norm, 0), kwargs = {})
%view_4 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_9, [%arg1_1, 4096]), kwargs = {})
%view_5 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_7, [%arg1_1, 8, 128]), kwargs = {})
%npu_rms_norm_1 : [num_users=1] = call_function[target=torch.ops.npu.npu_rms_norm.default](args = (%view_5, %arg22_1), kwargs = {})
%getitem_11 : [num_users=1] = call_function[target=operator.getitem](args = (%npu_rms_norm_1, 0), kwargs = {})
%view_6 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_11, [%arg1_1, 1024]), kwargs = {})
%view_7 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_4, [1, %arg1_1, -1, 128]), kwargs = {})
%view_8 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_6, [1, %arg1_1, -1, 128]), kwargs = {})
%view_9 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_7, [%arg1_1, 4096]), kwargs = {})
%view_10 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_8, [%arg1_1, 1024]), kwargs = {})
%zeros : [num_users=1] = call_function[target=torch.ops.aten.zeros.default](args = ([%arg1_1, 4096],), kwargs = {dtype: torch.bfloat16, device: npu:0, pin_memory: False})
%detach : [num_users=1] = call_function[target=torch.ops.aten.detach.default](args = (%zeros,), kwargs = {})
%view_11 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_9, [-1, 32, 128]), kwargs = {})
%view_12 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%detach, [-1, 32, 128]), kwargs = {})
%view_13 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%view_10, [-1, 8, 128]), kwargs = {})
%view_14 : [num_users=1] = call_function[target=torch.ops.aten.view.default](args = (%getitem_8, [-1, 8, 128]), kwargs = {})
return (slice_scatter_1, view_11, view_13, view_14, view_12, getitem_16)

```
