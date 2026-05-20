# NPU 适配工作流程

## 概述

本文档描述生成式推荐模型在昇腾NPU上的适配工作流程。

## 工作流程阶段

### 阶段1：环境基础验证

**目标**：确认昇腾NPU环境正确配置

**检查项**：
1. 驱动目录存在性：`/usr/local/Ascend/driver`
2. `npu-smi` 命令可用性
3. 容器环境文件：`/etc/ascend_install.info`
4. 环境变量：`ASCEND_VISIBLE_DEVICES`

**预期结果**：
- 驱动目录存在
- npu-smi 返回设备信息
- 环境变量已设置

---

### 阶段2：依赖安装验证

**目标**：验证所有依赖包正确安装

**检查项**：
1. `torch_npu` 版本 (需2.1.0.post9或兼容)
2. `mindxsdk-mxec-add-ons` 安装
3. Python版本 (≥3.11)
4. 必要Python包：torch, numpy等

**预期结果**：
- 所有依赖版本符合要求
- NPU扩展可用

---

### 阶段3：算子编译验证

**目标**：验证HSTU适配算子已正确编译

**检查项**：
1. 6个适配算子安装状态
2. `libhstu_dense_ops.so` 生成
3. gcc版本兼容性

**算子列表**：
- mxrec_opp_asynchronous_complete_cumsum
- mxrec_opp_dense_to_jagged
- mxrec_opp_index_select_for_rank1_backward
- mxrec_opp_jagged_to_padded_dense
- mxrec_opp_gather_for_rank1
- mxrec_opp_hstu_dense_forward/backward

**预期结果**：
- 所有算子已注册
- 动态库可加载

---

### 阶段4：源码与数据准备

**目标**：确认源码和数据集正确准备

**检查项**：
1. RecSDK仓库 (branch_v7.0.0-POC_torch)
2. generative-recommenders源码
3. NPU_GR.patch已应用
4. ml-1m数据集预处理

**预期结果**：
- 仓库分支正确
- Patch已应用
- 数据集完整

---

### 阶段5：配置参数验证

**目标**：验证配置文件参数正确

**检查项**：
1. gin参数验证：
   - `hstu_encoder.dqk` = 16的整数倍
   - `hstu_encoder.dv` = 16的整数倍
   - `train_fn.max_sequence_length = 3389`
   - `train_fn.local_batch_size > 0`

2. 环境变量：
   - `USE_NPU_HSTU=1`
   - `ENABLE_RAB=0`
   - `PYTORCH_NPU_ALLOC_CONF=expandable_segments:True`

**预期结果**：
- 所有参数验证通过
- 环境变量已正确设置

---

### 阶段6：模型训练启动验证

**目标**：确认训练脚本可正常启动

**执行命令**：
```bash
ASCEND_RT_VISIBLE_DEVICES=0 python3 main.py \
  --gin_config_file=configs/ml-1m/hstu-mt-3400.gin \
  --master_port=12345
```

**检查项**：
1. 训练进程正常启动
2. 无OOM错误
3. 初始loss正常输出

**预期结果**：
- 训练启动成功
- 无ERROR日志

---

### 阶段7：训练过程监控验证

**目标**：确认训练过程正常运行

**监控指标**：
1. Loss正常下降
2. NPU利用率 > 0%
3. 无算子编译/执行错误
4. Epoch正常完成

**预期结果**：
- Loss递减
- 无错误日志
- NPU有计算负载

---

### 阶段8：性能对比验证

**目标**：验证融合算子性能提升

**对比配置**：
| 配置 | USE_NPU_HSTU |
|------|--------------|
| 融合算子(优化) | 1 |
| 非融合算子(基准) | 0 |

**性能指标**：
- 训练速度 (iterations/second)
- 内存使用 (GB)
- 性能提升倍数

**预期结果**：
- 性能提升：5.3x - 15.2x

---

## 恢复机制

从失败阶段恢复：
```bash
python3 scripts/generate_report.py --resume-from <stage_number>
```

## 报告生成

```bash
python3 scripts/generate_report.py --all-stages --output ./verification_report
```

报告包含：
- 验证时间戳和设备信息
- 各阶段验证结果
- 详细错误信息
- 性能指标对比
- 建议和下一步操作
