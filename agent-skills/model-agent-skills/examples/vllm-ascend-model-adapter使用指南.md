# vLLM-Ascend 模型适配器使用指南

## 概述

`vllm-ascend-model-adapter` 是一款AI辅助的模型适配技能，用于将 Hugging Face 或本地模型检查点适配到昇腾 NPU 上运行。本技能基于 [vLLM-Ascend RFC #7539](https://github.com/vllm-project/vllm-ascend/issues/7539) 设计。

## 何时使用此技能

- 为昇腾 NPU 添加新的模型架构支持
- 验证现有模型是否与 vLLM-Ascend 兼容
- 排查昇腾上的模型加载或推理故障
- 理解昇腾的算子兼容性要求

## 快速开始

### 准备工作

1. **确认环境信息**
   ```bash
   # 检查 NPU 可用性
   npu-smi info
   
   # 检查 vLLM-Ascend 版本
   pip show vllm-ascend
   
   # 检查 PyTorch 和 torch-npu 版本
   python -c "import torch; print(torch.__version__)"
   python -c "import torch_npu; print(torch_npu.__version__)"
   ```

2. **准备模型文件**
   - HuggingFace 路径：`ZhipuAI/glm-4-9b-chat`
   - 或本地路径：`/path/to/local/model`

### 10 步适配流程

#### 第 1 步 — 收集上下文

与用户确认以下信息：

| 参数 | 说明 |
|------|------|
| **模型路径** | HuggingFace 路径或本地检查点位置 |
| **实现根目录** | vLLM 源码路径 |
| **交付仓库** | 更改的目标仓库 |
| **默认功能集** | ACLGraph (所有模型)、EP (MoE)、多模态 (VL) |

#### 第 2 步 — 分析模型

检查模型配置和结构：

```bash
# 检查 config.json
cat /path/to/model/config.json

# 检查模型文件结构
ls -la /path/to/model/
```

**模型类型分类：**

```
LLM ─┬─ 标准全注意力
     ├─ 滑动窗口注意力
     ├─ Mamba (SSM)
     ├─ 多潜在注意力 (MLA)
     └─ 混合架构

VLM  ─── 视觉语言模型

Whisper ─ 编码器-解码器 ASR 模型
```

#### 第 3 步 — 算子兼容性门控

扫描模型代码中的算子并分类：

| 算子类型 | 昇腾兼容性 | 操作 |
|--------------|----------------------|--------|
| **Torch** (原生 PyTorch) | ✅ 功能正常 | 记录性能不确定性 |
| **Triton** 内核 | ⚠️ 不确定 | 验证正确性和精度 |
| **CUDA** 有回退 | ❌ 使用回退 | 记录回退路径 |
| **CUDA** 无回退 | ❌ **阻塞** | 提前退出并提交 Issue |

**CUDA 提前退出规则：** 如果任何算子是纯 CUDA 且没有 Torch/Triton 替代方案，立即停止并提交 GitHub Issue。

#### 第 4 步 — 框架端代码分析

检查上游 vLLM 提交是否更改了 vllm-ascend 打过补丁的框架模块：

```
变更的 vLLM 框架模块
        │
        ├─ 已被 vllm-ascend 补丁?
        │       └─ 是 → 检查补丁是否仍然适用
        │
        └─ 未覆盖 + 昇腾不兼容?
                └─ 是 → 在 vllm-ascend/ 下添加最小覆盖
```

#### 第 5 步 — 选择适配策略

| 情况 | 策略 |
|----------|----------|
| 架构存在且兼容 | 重用；仅修补损坏的部分 |
| 架构缺失或不兼容 | 实现新适配器 |
| 远程代码需要更新的 transformers | 复制所需文件 — 切勿升级 |
| 失败需要将建模代码放入 vllm-ascend | **不要继续** — 提交 GitHub Issue |

#### 第 6 步 — 实现最小代码更改

所有模型适配代码仅放入 vLLM 源码。模型特定文件**绝不能**引入 vllm-ascend。

```bash
# 语法检查
python -m py_compile /vllm-workspace/vllm/vllm/model_executor/models/<model>.py
```

#### 第 7 步 — 两阶段验证

**两个阶段都必须执行。**

**阶段 A — Dummy 快速门控：**
```bash
vllm serve /models/<model> \
  --load-format dummy \
  --dtype bfloat16 \
  --tensor-parallel-size <TP> \
  --max-model-len 131072 \
  --max-num-seqs 16 \
  --port 8000
```

**阶段 B — 真权重强制门控：**
去掉 `--load-format dummy` 参数重新运行。

#### 第 8 步 — 验证推理和功能

```bash
# 1. 就绪检查
curl -sf http://127.0.0.1:8000/v1/models

# 2. 文本推理
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"<name>","messages":[{"role":"user","content":"say hi"}],"temperature":0,"max_tokens":16}'
```

**功能状态符号：**

| 符号 | 含义 |
|--------|---------|
| ✅ | 支持且已验证 |
| ❌ | 框架层面不支持 |
| ⚠️ | 检查点缺失 |
| N/A | 不适用 |

#### 第 9 步 — 回退、生成产物、提交

1. 将最小 diff 从 `/vllm-workspace/*` 回退到交付仓库
2. 生成测试配置：`tests/e2e/models/configs/<ModelName>.yaml`
3. 生成教程文档：`docs/source/tutorials/models/<ModelName>.md`
4. 更新索引文档：`docs/source/tutorials/models/index.md`
5. 提交更改：`git commit -sm "feat: add <ModelName> support on Ascend NPU"`

#### 第 10 步 — 交付产物

最终响应包括：
- **分析报告**：架构总结、不兼容根因、代码更改、功能状态矩阵
- **运行手册**：服务器启动命令、验证 curl 命令、回退命令
- **SKILL.md 摘要** 作为 GitHub Issue 评论发布

## 回退阶梯

当启动或推理失败时，按此顺序处理：

```
1. 重现一次以确认确定性失败
        ↓
2. 添加 --enforce-eager → 隔离图捕获与算子失败
        ↓
3. [VL] TORCHDYNAMO_DISABLE=1 → 隔离 dynamo/interpolate/contiguous 失败
        ↓
4. [VL] --limit-mm-per-prompt '{"image":0,"video":0,"audio":0}'
  → 将多模态处理器失败与模型核心隔离
        ↓
5. 应用针对性代码修复，循环回阶段 A
```

## 常见问题

### Q1: 模型启动失败，报错 RopeOperation

**原因：** GLM 等模型的 `rotary_dim < head_size`，与 Ascend NPU 的 RoPE 算子不兼容。

**解决方案：** 应用 rotary_embedding.py 补丁（参见 Demo 案例）。

### Q2: `ERR00100 PTA call acl api failed`

**原因：** 算子初始化失败，通常是参数不匹配或算子不支持。

**解决方案：** 
1. 尝试 `--enforce-eager` 模式
2. 检查模型配置参数
3. 提交 GitHub Issue 报告

### Q3: 量化模型加载失败

**原因：** 缺少 `quant_model_description.json` 或量化配置错误。

**解决方案：** 使用 ModelSlim 工具重新量化模型。

## 参考资源

- [vLLM-Ascend 官方文档](https://docs.vllm.ai/projects/ascend/en/latest/)
- [支持模型列表](./reference/supported-models.md)
- [量化指南](./reference/quantization-guide.md)
- [算子兼容性](./reference/operator-compatibility.md)
- [故障排查](./reference/troubleshooting.md)
- [工作流检查清单](./reference/workflow-checklist.md)

## 输出要求

每次适配必须产生：

| 产物 | 说明 |
|------|------|
| 最小 diff | 仅 vLLM 源码，绝不是 vllm-ascend 建模文件 |
| 测试配置 | `tests/e2e/models/configs/<ModelName>.yaml` |
| 教程文档 | `docs/source/tutorials/models/<ModelName>.md` |
| 分析报告 | 中文架构总结和不兼容根因 |
| 运行手册 | 中文启动命令和验证方法 |
| Git 提交 | 仅一个签名提交 |
