# Demo：GLM-4-chat-9B 适配案例

> **适配版本**：vLLM-ascend 0.13.0
> **硬件环境**：8x Ascend 910B3 NPU
> **CANN 版本**：8.0.0
> **参考 Issue**：[#309](https://gitcode.com/raintBN/vLLM-ascend_sloved_issues/tree/main/Issue_309_glm_4_9b_chat)

---

## 问题摘要

用户在 vLLM-ascend 上启动 `ZhipuAI/glm-4-9b-chat` 模型时失败，错误发生在 profile_run 阶段，具体报错为 RopeOperation (Rotary Position Embedding) 的 `atb::OperationSetup` 失败。

### 关键错误信息

```
[rank0]:[E312 05:31:46.999138962 compiler_depend.ts:418] setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:129
atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x8c
ERROR 03-12 05:31:46 [engine.py:411] The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RopeOperation.
ERROR 03-12 05:31:46 [engine.py:411] [ERROR] 2025-03-12-05:31:46 (PID:396, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
```

### 环境信息

| 参数 | 值 |
|------|-----|
| **模型** | ZhipuAI/glm-4-9b-chat |
| **NPU** | 8x Ascend 910B3 |
| **CANN** | 8.0.0 |
| **vLLM** | 0.1.dev1+g36e0c8f |
| **PyTorch** | 2.5.1 |
| **torch-npu** | 2.5.1.dev20250308 |

---

## 问题分析

### 与 FAQ 知识库的关联

通过深度检索，发现了精确的技术根因：

1. **Issue #6060**（最相关）："RopeOperation setup failed when `_rope_forward_oot()` called with rotary_dim < head_size"
   - **根因**：当 GLM 模型的 `head_size=128` 但 `rotary_dim=64` 时，代码错误地将 `head_size` 传递给了 NPU rotary embedding 函数，而不是应该传递的 `rotary_dim`
   - **问题位置**：`vllm_ascend/ops/rotary_embedding.py` 中的 `_rope_forward_oot()` 函数

2. **Issue #2255**："ZhipuAI/glm-4-9b-chat-hf failed to start"
   - 相同错误：`RopeOperation setup failed!`

### 根本原因分析

1. **错误位置**：错误发生在 `vllm/model_executor/models/chatglm.py` 的 `GLMAttention` 类中的 `rotary_emb` 操作

2. **根本原因**：
   - GLM 模型使用特殊的 Rotary Position Embedding (RoPE)
   - 在 Ascend NPU 上，RoPE 操作的 ATB 算子在初始化时失败
   - 这是由于 GLM 模型的 RoPE 配置与 Ascend NPU 的 RoPE 算子不兼容导致
   - 问题出现在 profile_run 阶段的 KV Cache 初始化过程中

3. **触发条件**：
   - 模型加载完成后的第一次 forward 执行
   - 尝试进行 profile_run 以确定可用内存块时触发

---

## 解决方案

### 修复方案

对 `vllm_ascend/ops/rotary_embedding.py` 文件进行以下修改：

#### Fix 1: 处理 Triton 路径中 cos/sin 为 None 的情况

在 `_rope_forward_oot()` 函数中，当 `rotary_dim < head_size` 时，添加 None 检查：

```python
# 在 ~219 行位置
if  HAS_TRITON:
    # PATCH: 处理 cos/sin 为 None 的情况（如 rotary_dim < head_size 的 GLM 模型）
    if cos is None or sin is None:
        # 从 cos_sin_cache 动态生成 cos/sin
        cos_sin = self.cos_sin_cache.index_select(0, positions)
        num_tokens = positions.shape[0]
        cos_sin = cos_sin.view(num_tokens, 2, -1)
        if is_neox_style:
            cos = cos_sin[:, 0, :].view(-1, self.rotary_dim)
            sin = cos_sin[:, 1, :].view(-1, self.rotary_dim)
        else:
            cos = cos_sin[:, 0, :]
            sin = cos_sin[:, 1, :]
    else:
        cos = cos.view(-1, self.rotary_dim)
        sin = sin.view(-1, self.rotary_dim)
```

#### Fix 2: 修复非 Triton 路径中的维度参数

将 `torch_npu._npu_rotary_embedding()` 调用中的 `head_size` 改为 `rotary_dim`：

```python
# 将
torch_npu._npu_rotary_embedding(positions, q_rot, k_rot, self.head_size, ...)

# 改为
torch_npu._npu_rotary_embedding(positions, q_rot, k_rot, self.rotary_dim, ...)
```

### 补丁文件

完整补丁内容：

```diff
--- a/vllm_ascend/ops/rotary_embedding.py
+++ b/vllm_ascend/ops/rotary_embedding.py
@@ -215,9 +215,23 @@ def _rope_forward_oot(
              query, key, cos, sin)
          elif self.rotary_dim < self.head_size:
              if  HAS_TRITON:
-       
-                cos = cos.view(-1, self.rotary_dim)
-                sin = sin.view(-1, self.rotary_dim)
+                # Handle case where cos/sin are None (e.g., GLM models with rotary_dim < head_size)
+                if cos is None or sin is None:
+                    # Generate cos/sin on-the-fly from cos_sin_cache
+                    cos_sin = self.cos_sin_cache.index_select(0, positions)
+                    # cos_sin shape: [num_tokens, 2, rotary_dim] for neox_style
+                    if is_neox_style:
+                        cos = cos_sin[:, 0, :].view(-1, self.rotary_dim)
+                        sin = cos_sin[:, 1, :].view(-1, self.rotary_dim)
+                    else:
+                        # For GPT style, reshape from [num_tokens, 2, rotary_dim] -> [num_tokens, rotary_dim]
+                        cos = cos_sin[:, 0, :]
+                        sin = cos_sin[:, 1, :]
+                else:
+                    cos = cos.view(-1, self.rotary_dim)
+                    sin = sin.view(-1, self.rotary_dim)
```

---

## 验证测试

### 测试环境

| 参数 | 值 |
|------|-----|
| **vLLM** | 0.14.1+empty |
| **vLLM-ascend** | 0.14.0rc1 |
| **torch** | 2.9.0+cpu |
| **torch_npu** | 2.9.0 |
| **NPU** | 8x Ascend 910B3 |
| **CANN** | 8.5.0 |
| **模型** | glm-4-9b-chat |

### 测试脚本

```python
#!/usr/bin/env python3
"""
测试 GLM-4-9b-chat 适配脚本
"""

import sys
sys.path.insert(0, "/path/to/patch/dir")

# 先应用补丁再导入 vllm
print("应用 rotary embedding 补丁...")
from fix_rotary_embedding import patch_rotary_embedding
patch_rotary_embedding()

# 导入 vllm
print("导入 vLLM...")
from vllm import LLM

MODEL_PATH = "/root/.cache/modelscope/ZhipuAI/glm-4-9b-chat"

print("启动 vLLM 服务...")

# 创建 LLM 实例
llm = LLM(
    model=MODEL_PATH,
    trust_remote_code=True,
    dtype="float16",
    max_num_seqs=8,
    max_model_len=4096,
    tensor_parallel_size=8,
    enforce_eager=True,  # 使用 eager 模式
)

print("vLLM 服务启动成功！")
print("测试推理...")

# 测试推理
from vllm import SamplingParams
sampling_params = SamplingParams(temperature=0.7, max_tokens=128)
prompt = "Hello, how are you?"

outputs = llm.generate([prompt], sampling_params)
for output in outputs:
    print(f"生成结果: {output.outputs[0].text}")

print("测试完成！")
```

### 验证命令

```bash
# 设置环境变量
export ASCEND_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"
export PYTORCH_CUDA_ALLOC_CONF="max_split_size_mb:512"

# 启动服务
vllm serve /root/.cache/modelscope/ZhipuAI/glm-4-9b-chat \
  --trust-remote-code \
  --dtype float16 \
  --tensor-parallel-size 8 \
  --max-model-len 4096 \
  --enforce-eager
```

### 验证结果

| 测试项 | 结果 |
|--------|------|
| 模型加载 | ✅ 成功 |
| Tensor Parallel | ✅ 8 卡成功 |
| max_model_len | ✅ 4096 成功 |
| dtype | ✅ float16 成功 |
| 推理测试 | ✅ 完成 |

**测试输出：**
```
vLLM server started successfully!
Testing inference...
Generated:  It's me, [my name is [YourName]!...
Test completed successfully!
```

---

## 相关 Issue

| Issue # | 模型 | 状态 |
|----------|------|------|
| #309 | glm-4-9b-chat | ✅ 已解决 |
| #2255 | glm-4-9b-chat-hf | ✅ 已解决 |
| #2258 | GLM-4-32B-0414 | ✅ 已解决 |
| #6060 | RoPE rotary_dim 参数问题 | ✅ 已解决 |

---

## 总结

### 问题根因

GLM 模型的 `rotary_dim=64 < head_size=128` 与 vLLM-ascend 的 RoPE 算子实现不兼容，导致 NPU kernel 初始化失败。

### 解决方案

1. 在 Triton 路径中添加 `cos/sin` 为 None 的处理逻辑
2. 在非 Triton 路径中将 `head_size` 参数修正为 `rotary_dim`

### 经验教训

1. **参数匹配**：Ascend NPU 算子对参数维度有严格要求，必须确保 `rotary_dim` 而非 `head_size`
2. **None 检查**：动态生成的值（如 cos/sin）可能为 None，需要进行防御性检查
3. **回退方案**：当 `--enforce-eager` 不能解决时，需要深入分析算子实现

---

## 参考资源

- [vLLM-Ascend 官方文档](https://docs.vllm.ai/projects/ascend/en/latest/)
- [原始 Issue #309](https://gitcode.com/raintBN/vLLM-ascend_sloved_issues/tree/main/Issue_309_glm_4_9b_chat)
- [RoPE 算子修复补丁](./patch_rotary_embedding.patch)
