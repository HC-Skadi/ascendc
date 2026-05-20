---
name: generative-recommendation-verification
description: |
  昇腾生成式推荐模型验证 (Ascend Generative Recommendation Model Verification) - 自动化验证生成式推荐模型在华为昇腾NPU设备上的完整运行状态。
  
  **触发场景**：
  - 用户提及"验证生成式推荐模型"、"验证HSTU模型"、"验证RecSDK"
  - 用户提及"昇腾NPU上运行推荐模型"、"Atlas 800 A2/A3上部署推荐模型"
  - 用户提及"生成式推荐模型验证"、"mxrec算子验证"、"HSTU训练验证"
  - 用户请求"运行完整的模型验证流程"、"检查推荐模型环境"
  - 用户提供昇腾设备路径并要求"验证环境"、"检查依赖"、"运行训练"
  
  **不触发场景**：
  - 通用昇腾驱动检查（使用ascend-model-verification skill）
  - 非推荐类模型验证（如CV、NLP模型）
  - 简单的npu-smi命令执行
  
  **功能概述**：
  该skill执行8阶段验证流程：环境基础验证 → 依赖安装验证 → 算子编译验证 → 源码与数据准备验证 → 配置参数验证 → 模型训练启动验证 → 训练过程监控验证 → 性能对比验证
  
  **输入**：
  - 昇腾设备环境路径（默认：/usr/local/Ascend）
  - 配置文件路径（可选，默认：configs/ml-1m/hstu-sampled-softmax-n128-final.gin）
  - 工作目录（默认：当前目录）
  
  **输出**：
  - 详细验证报告（JSON + Markdown格式）
  - 各阶段通过/失败状态
  - 错误日志和诊断信息
  - 性能指标对比数据

version: 1.1.0
required_tools:
  - bash
  - python3
  - npu-smi
  - git
compatibility:
  - Ascend 800 A2/A3
  - Ascend 910
  - Atlas 800 A2/A3
  - Driver: /usr/local/Ascend/driver
---

# 昇腾生成式推荐模型验证 Skill

本skill自动化验证生成式推荐模型在昇腾NPU设备上的完整运行状态。

## 快速开始

### 基本用法

```bash
# 完整验证流程
python3 scripts/generate_report.py --all-stages

# 按阶段验证
python3 scripts/generate_report.py --stage 1  # 仅环境验证
python3 scripts/generate_report.py --stage 3  # 仅算子编译验证

# 从失败阶段恢复
python3 scripts/generate_report.py --resume-from 4

# 性能对比验证
python3 scripts/performance_comparison.py --baseline --optimized
```

### 输入参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--ascend-path` | 昇腾设备路径 | `/usr/local/Ascend` |
| `--config` | 配置文件路径 | `configs/ml-1m/hstu-sampled-softmax-n128-final.gin` |
| `--workdir` | 工作目录 | 当前目录 |
| `--stage` | 指定验证阶段(1-8) | 全部阶段 |
| `--resume-from` | 从指定阶段恢复 | 从头开始 |
| `--output` | 报告输出路径 | `./verification_report` |

## 验证流程总览

```
┌─────────────────────────────────────────────────────────────────┐
│                    8阶段验证流程                                  │
├─────────────────────────────────────────────────────────────────┤
│  1. 环境基础验证 → 2. 依赖安装验证 → 3. 算子编译验证              │
│         ↓                ↓                ↓                     │
│  驱动目录检查         torch版本         mxrec算子检查              │
│  npu-smi可用性        torch_npu版本     libfbgemm_npu_api.so     │
│  容器环境信息         CANN版本                               │
│                                                                  │
│  4. 源码与数据准备 → 5. 配置参数验证 → 6. 模型训练启动            │
│         ↓                ↓                ↓                     │
│  GR/OneRec/RankMixer   gin参数检查      main.py启动              │
│  仓库克隆              环境变量设置     无OOM验证                │
│  Patch应用             num_heads/dqk/dv                       │
│                                                                  │
│  7. 训练过程监控 → 8. 性能对比验证                                │
│         ↓                ↓                                      │
│  Loss下降监控      USE_NPU_HSTU=1 vs =0                        │
│  NPU利用率          速度/内存对比                               │
│  错误日志检查       性能提升倍数                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 阶段1：环境基础验证

验证昇腾设备基础环境是否正确配置。

### 验证项

| 检查项 | 期望结果 | 失败处理 |
|--------|----------|----------|
| 驱动目录 `/usr/local/Ascend/driver` | 存在 | 检查驱动安装 |
| `npu-smi info` 命令 | 可执行，返回设备信息 | 检查NPU驱动 |
| 容器环境文件 `/etc/ascend_install.info` | 存在 | 确认容器镜像 |
| 环境变量 `ASCEND_VISIBLE_DEVICES` | 已设置 | 设置为 `0` |

### 执行脚本

```bash
bash scripts/environment_check.sh [--ascend-path /usr/local/Ascend]
```

### 成功标准

- 所有检查项返回 ✓
- npu-smi 显示设备状态正常
- 无 critical 级别错误

---

## 阶段2：依赖安装验证

验证模型运行所需依赖包是否正确安装。

### 验证项（实际验证通过版本）

| 依赖项 | 期望版本 | 检查方法 | 备注 |
|--------|----------|----------|------|
| `torch` | **2.6.0+cpu** | `pip show torch` | ⚠️ 不要使用2.9.0等高版本 |
| `torch_npu` | **2.6.0** | `pip show torch_npu` | 必须与torch版本匹配 |
| CANN | ≥ 8.5.1 | `ls /usr/local/Ascend/cann-*` | |
| Python | ≥ 3.11 | `python3 --version` | 推荐3.11 |
| numpy | 最新稳定版 | `python3 -c "import numpy"` | |
| gin-config | ≥ 0.5.0 | `pip show gin-config` | |

### ⚠️ 关键注意事项

1. **torch版本必须使用2.6.0**: 高版本torch（如2.9.0）存在兼容性问题
2. **torch和torch_npu版本必须完全匹配**: torch_npu 2.6.0 + torch 2.6.0
3. **不要安装nvidia相关包**: 删除所有`nvidia-*`包，避免冲突

### 执行脚本

```bash
python3 scripts/dependency_verify.py [--workdir /path/to/workdir]
```

### 成功标准

- torch版本为2.6.0
- torch_npu版本为2.6.0
- CANN版本≥8.5.1
- 无nvidia包冲突

---

## 阶段3：算子编译验证

验证HSTU适配算子是否正确编译安装。

### 验证项

检查以下适配算子是否已安装：

| 算子 | 说明 | 检查路径 |
|------|------|----------|
| `asynchronous_complete_cumsum` | 异步累加和 | CANN目录 |
| `dense_to_jagged` | 密集到稀疏转换 | CANN目录 |
| `jagged_to_padded_dense` | 稀疏到密集转换 | CANN目录 |
| `hstu_dense_forward` | HSTU前向传播 | CANN目录 |
| `hstu_dense_backward` | HSTU反向传播 | CANN目录 |
| `gather_for_rank1` | 索引选取 | CANN目录 |

### 编译的适配层

| 文件 | 默认路径 |
|------|----------|
| `libfbgemm_npu_api.so` | `/usr/local/Ascend/.../torch_plugin/torch_library/2.6.0/common/build/` |

### ⚠️ 关键注意事项

1. **算子namespace问题**: 原始代码使用`torch.ops.mxrec`，需要别名到`torch.ops.fbgemm`
2. **加载方式**: 通过`torch.ops.load_library()`加载`.so`文件
3. **环境变量**: 设置`LIB_FBGEMM_NPU_API_SO_PATH`指向`.so`文件路径

### 修复算子namespace的代码

```python
def load_npu_ops():
    common_lib_path = "/path/to/libfbgemm_npu_api.so"
    torch.ops.load_library(common_lib_path)
    
    if hasattr(torch.ops.mxrec, 'asynchronous_complete_cumsum'):
        def make_alias(schema_name):
            mxrec_op = getattr(torch.ops.mxrec, schema_name)
            def alias_op(*args, **kwargs):
                return mxrec_op(*args, **kwargs)
            return alias_op
        
        for op_name in dir(torch.ops.mxrec):
            if not op_name.startswith('_') and op_name != 'name':
                try:
                    setattr(torch.ops.fbgemm, op_name, make_alias(op_name))
                except Exception:
                    pass
```

### 执行脚本

```bash
bash scripts/operator_compile_test.sh [--workdir /path/to/workdir]
```

### 成功标准

- 所有6个算子检查通过
- 动态库文件存在且可加载

---

## 阶段4：源码与数据准备验证

验证模型源码和数据集是否正确准备。

### 验证项

| 模型 | 仓库 | 分支/Commit | 备注 |
|------|------|-------------|------|
| GR | `https://gitee.com/raintbn/generative-recommenders` | `bb389f9539b054e7268528efcd35457a6ad52439` | 需要应用gr_npu.patch |
| OneRec | `https://gitee.com/raintbn/OpenOneRec` | 官方最新 | verl有NPU支持 |
| RankMixer | 参考PyTorch实现 | CIKM'25论文 | 需要TensorFlow→PyTorch移植 |

### Patch应用流程

```bash
cd generative-recommenders
git apply gr_npu.patch
```

### Patch关键修改点

1. **main.py**: 添加`torch_npu`导入，修改设备从cuda改为npu
2. **hstu.py**: 添加HSTU融合算子封装类和NPU autocast
3. **train.py**: 修改nccl→hccl，添加RepeatDataset封装
4. **autoregressive_losses.py**: 添加prefetch_shape参数传递
5. **新增文件**: `prefetch_shape.py`, `pt_jagged_dense_convert.py`

### 数据集准备

```bash
cd generative-recommenders
python preprocess_public_data.py  # 仅处理ml-1m
```

### 执行脚本

```bash
python3 scripts/source_prepare_check.py --workdir /path/to/RecSDK
```

### 成功标准

- 仓库分支正确
- Patch 已应用
- 数据集已预处理

---

## 阶段5：配置参数验证

验证训练配置文件参数是否符合要求。

### gin 配置参数要求

| 参数 | 要求 | 说明 |
|------|------|------|
| `hstu_encoder.num_heads` | ≥2 | ⚠️ 必须是2的倍数 |
| `hstu_encoder.dqk` | 16的整数倍 | ⚠️ 通常设为32或64 |
| `hstu_encoder.dv` | 16的整数倍 | ⚠️ 通常设为32或64 |
| `train_fn.max_sequence_length` | = 3389 | 用于ml-1m |
| `train_fn.local_batch_size` | > 0（建议32） | |

### 实际验证通过的配置示例

```gin
# configs/ml-1m/hstu-sampled-softmax-n128-final.gin
train_fn.local_batch_size = 128
train_fn.main_module = "HSTU"
train_fn.dropout_rate = 0.2
train_fn.user_embedding_norm = "l2_norm"

hstu_encoder.num_blocks = 8
hstu_encoder.num_heads = 2        # 必须≥2
hstu_encoder.dqk = 64              # 16的整数倍
hstu_encoder.dv = 64              # 16的整数倍
hstu_encoder.linear_dropout_rate = 0.2

train_fn.learning_rate = 1e-3
```

### 环境变量要求

```bash
export USE_NPU_HSTU=1              # 使用融合算子（性能提升5-15倍）
export ENABLE_RAB=0               # 禁用Relative Attention Bias
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export LIB_FBGEMM_NPU_API_SO_PATH=/path/to/libfbgemm_npu_api.so
export ASCEND_RT_VISIBLE_DEVICES=0
```

### 执行脚本

```bash
python3 scripts/config_validator.py --config configs/ml-1m/hstu-sampled-softmax-n128-final.gin
```

### 成功标准

- 所有 gin 参数验证通过
- 环境变量已正确设置

---

## 阶段6：模型训练启动验证

验证训练脚本能否正常启动。

### 验证命令

```bash
cd generative-recommenders
ASCEND_RT_VISIBLE_DEVICES=0 python3 main.py \
  --gin_config_file=configs/ml-1m/hstu-sampled-softmax-n128-final.gin \
  --master_port=12359
```

### 验证项

| 检查项 | 期望结果 |
|--------|----------|
| 训练进程 | 正常启动，无报错 |
| NPU内存 | 无 OOM 错误 |
| 初始 loss | 正常输出（通常约0.5-1.0） |
| 指标输出 | NDCG@10, HR@10 正常 |

### ⚠️ 常见启动错误

1. **算子找不到**: 检查`LIB_FBGEMM_NPU_API_SO_PATH`环境变量
2. **类型不匹配**: 检查torch和torch_npu版本是否匹配
3. **OOM**: 减小`local_batch_size`
4. **进程组初始化失败**: 检查`ASCEND_RT_VISIBLE_DEVICES`设置

### 执行脚本

```bash
bash scripts/training_launcher.sh \
  --config configs/ml-1m/hstu-sampled-softmax-n128-final.gin \
  --device 0 \
  --port 12359
```

### 成功标准

- 训练启动成功
- 无 Python 或 NPU 错误
- Loss正常输出

---

## 阶段7：训练过程监控验证

验证训练过程正常运行，监控关键指标。

### 监控指标

| 指标 | 期望状态 | 说明 |
|------|----------|------|
| Loss 下降 | 正常递减 | 从~0.5降至~0.1 |
| NDCG@10 | 逐步提升 | 从0.003升至0.14+ |
| HR@10 | 逐步提升 | 从0.008升至0.30+ |
| NPU 利用率 | > 0%（有计算） | 使用npu-smi监控 |
| 错误日志 | 无算子编译/执行错误 | |

### 实际验证结果（ml-1m数据集）

| Iteration | NDCG@10 | HR@10 | 状态 |
|-----------|---------|-------|------|
| 0 | 0.0030 | 0.0078 | baseline |
| 100 | 0.0558 | 0.1172 | ✓ |
| 500 | 0.1176 | 0.2578 | ✓ |
| 1000 | 0.1284 | 0.2344 | ✓ |
| 1400 | 0.1482 | 0.3047 | ✅ 收敛正常 |

### 执行脚本

```bash
python3 scripts/training_monitor.py \
  --log-file training.log \
  --duration 300  # 监控300秒
```

### 成功标准

- Loss 正常下降
- 无 ERROR 级别日志
- NDCG/HR指标符合预期

---

## 阶段8：性能对比验证

对比使用融合算子与不使用融合算子的性能差异。

### 对比配置

| 配置 | 环境变量 | 预期性能 |
|------|----------|----------|
| 融合算子（优化） | `USE_NPU_HSTU=1` | 5-15x 提升 |
| 非融合算子（基准） | `USE_NPU_HSTU=0` | baseline |

### 性能指标

| 指标 | 说明 |
|------|------|
| 训练速度 | iterations/second |
| 内存使用 | GB |
| 性能提升 | 相对于基准的倍数 |

### 执行脚本

```bash
python3 scripts/performance_comparison.py \
  --config configs/ml-1m/hstu-sampled-softmax-n128-final.gin \
  --baseline \
  --optimized
```

### 成功标准

- 两个配置均运行成功
- 性能提升符合预期（参考：5.3x-15.2x）

---

## RankMixer验证扩展

RankMixer是基于MLP-Mixer架构的排序模型，需要TensorFlow→PyTorch移植。

### 架构组件

| 组件 | 说明 |
|------|------|
| `RMSNorm` | RMS Layer Normalization |
| `TokenMixer` | Multi-head Token Mixing - 跨token特征交叉 |
| `TokenUnmixer` | Token Unmixing - 还原token维度 |
| `SwiGLU` | SwiGLU激活函数 |
| `PSwiGLU` | Per-Token SwiGLU |
| `TokenMixerLargeBlock` | RankMixer核心Block |
| `RankMixer` | 主模型 |
| `RankMixerForRanking` | 排序任务输出头 |

### 模型配置

| 版本 | T | D | H | L | 参数量 |
|------|---|---|---|---|-|------|
| Small | 8 | 128 | 4 | 2 | ~2.1M |
| Base | 16 | 256 | 8 | 2 | ~10M |
| Large | 16 | 768 | 8 | 2 | ~100M |
| XL | 32 | 1536 | 16 | 2 | ~1B |

### RankMixer训练命令

```bash
cd rankmixer
python train_rankmixer.py
```

### 验证结果

- 模型在NPU上成功加载
- 前向传播正常
- 反向传播和梯度更新正常
- Loss正常下降

---

## 报告生成

### 执行完整验证并生成报告

```bash
python3 scripts/generate_report.py \
  --all-stages \
  --ascend-path /usr/local/Ascend \
  --config configs/ml-1m/hstu-sampled-softmax-n128-final.gin \
  --output ./verification_report
```

### 报告结构

```
verification_report/
├── report.json          # 结构化报告数据
├── report.md            # Markdown 格式报告
├── stage_1_env.log      # 各阶段日志
├── stage_2_dep.log
├── stage_3_op.log
├── stage_4_src.log
├── stage_5_cfg.log
├── stage_6_train.log
├── stage_7_monitor.log
├── stage_8_perf.log
└── errors/              # 错误详情
    ├── stage_3.err
    └── ...
```

### 报告内容

1. **验证时间戳和设备信息**
2. **各阶段验证结果**（通过/失败状态）
3. **详细错误信息**（如有）
4. **性能指标对比表格**
5. **建议和下一步操作**

---

## 异常处理

### 超时机制

每个验证阶段有默认超时：
- 环境检查：60秒
- 依赖验证：120秒
- 算子编译：300秒
- 训练验证：600秒

### 错误诊断

失败阶段提供：
- 错误类型和错误码
- 失败原因分析
- 修复建议
- 相关日志路径

### 恢复验证

```bash
# 从阶段4恢复
python3 scripts/generate_report.py --resume-from 4
```

---

## 扩展性

### 支持其他数据集

```bash
python3 scripts/generate_report.py \
  --config configs/amazon/hstu-sampled-softmax-n512-final.gin \
  --dataset amazon
```

### 批量验证

```bash
# 验证多个模型版本
for config in configs/*/hstu-*.gin; do
  python3 scripts/generate_report.py --config "$config"
done
```

---

## 脚本索引

| 脚本 | 功能 |
|------|------|
| `environment_check.sh` | 阶段1：环境基础验证 |
| `dependency_verify.py` | 阶段2：依赖安装验证 |
| `operator_compile_test.sh` | 阶段3：算子编译验证 |
| `source_prepare_check.py` | 阶段4：源码与数据准备 |
| `config_validator.py` | 阶段5：配置参数验证 |
| `training_launcher.sh` | 阶段6：训练启动验证 |
| `training_monitor.py` | 阶段7：训练过程监控 |
| `performance_comparison.py` | 阶段8：性能对比验证 |
| `generate_report.py` | 生成完整验证报告 |

---

## 参考资料

详细技术文档位于 `reference/` 目录：

### 核心参考文档

| 文档 | 说明 |
|------|------|
| `ascend_gr_implementation_guide.txt` | 昇腾实现生成式推荐模型完整指南 |
| `hstu_architecture_details.md` | HSTU 架构详细说明 |
| `npu_adaptation_workflow.md` | NPU 适配工作流程 |

### 关键代码路径

| 路径 | 说明 |
|------|------|
| `memgen-gr/src/generative-recommenders/` | GR模型源码 |
| `memgen-gr/mxrec_add_ons/rec_for_torch/torch_plugin/` | NPU算子适配层 |
| `memgen-gr/src/generative-recommenders/gr_npu.patch` | NPU适配补丁 |
| `rankmixer/src/` | RankMixer PyTorch实现 |

### 论文参考

1. **GR (ICML'24)**: "Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations"
2. **OneRec (arXiv:2512.24762)**: "OpenOneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment"
3. **RankMixer (CIKM'25)**: "RankMixer: Scaling Up Ranking Models in Industrial Recommenders"

---

## 验证检查清单

### 环境检查
- [ ] torch == 2.6.0
- [ ] torch_npu == 2.6.0
- [ ] CANN >= 8.5.1
- [ ] npu-smi 可用
- [ ] 无nvidia-*包冲突

### 算子检查
- [ ] libfbgemm_npu_api.so 可加载
- [ ] 6个HSTU算子已编译
- [ ] namespace别名已设置（mxrec→fbgemm）

### 代码检查
- [ ] gr_npu.patch 已应用
- [ ] 数据集已预处理
- [ ] gin配置参数正确

### 训练检查
- [ ] 训练启动无报错
- [ ] Loss正常下降
- [ ] NDCG/HR指标收敛
