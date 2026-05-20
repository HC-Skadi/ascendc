# vLLM Ascend 功能特性指南

> 本文档详细介绍了 vLLM Ascend 插件的核心功能特性
> 来源: https://docs.vllm.ai/projects/ascend/en/latest/

## 概述

vLLM Ascend 是华为昇腾NPU的硬件插件,支持在昇腾NPU上运行vLLM推理引擎。该插件支持流行的开源模型,包括Transformers、Mixture-of-Experts、Embedding和多模态LLM。

## 核心特性

### 1. 高性能推理

- **PagedAttention**: 内存高效的关注机制实现
- **连续批处理**: 动态批处理提高吞吐量
- **CUDA Graph**: 减少内核启动开销

### 2. 量化支持

vLLM Ascend 支持多种量化方法:

| 量化类型 | 说明 | 内存节省 |
|---------|------|---------|
| W4A8 | 4-bit权重, 8-bit激活 | ~75% |
| W8A8 | 8-bit权重, 8-bit激活 | ~50% |
| W4A4 | 4-bit权重, 4-bit激活 | ~85% |

### 3. 分布式部署

- **张量并行 (Tensor Parallelism)**: 多卡模型分片
- **数据并行 (Data Parallelism)**: 多实例并行处理
- **专家并行 (Expert Parallelism)**: MoE模型专用
- **KV传输**: Mooncake连接器支持跨节点KV缓存传输

### 4. 推测解码

- **MTP (Multi-Token Prediction)**: 多令牌预测加速推理
- **DeepSeek MTP**: DeepSeek系列模型专用

### 5. 高级特性

- **前缀缓存**: 减少重复计算
- **异步调度**: 提高GPU利用率
- **动态分词**: 支持可变长度输入

## 版本要求

### 软件依赖

| 组件 | 版本要求 |
|------|---------|
| vLLM | 0.17.0+ |
| vLLM-Ascend | 0.17.0+ |
| CANN | 8.5.0+ |
| Python | 3.8+ |

### 硬件支持

- **华为昇腾910B**: 全功能支持
- **华为昇腾310B**: 基础推理支持

## 环境变量

### 基础配置

```bash
# 设置可见NPU设备
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3

# 线程配置
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
```

### 内存管理

```bash
# 启用虚拟内存段,减少内存碎片
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
```

### 网络配置 (多节点)

```bash
# 网络接口配置
export HCCL_IF_IP=192.168.1.1
export GLOO_SOCKET_IFNAME=eth0
export TP_SOCKET_IFNAME=eth0
export HCCL_SOCKET_IFNAME=eth0

# HCCL配置
export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_BUFFSIZE=768
```

### 性能优化

```bash
# 启用FlashComm v1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1

# 启用Balance调度
export VLLM_ASCEND_BALANCE_SCHEDULING=1

# 上下文并行
export VLLM_ASCEND_ENABLE_CONTEXT_PARALLEL=1

# 使用V1引擎
export VLLM_USE_V1=1

# 任务队列
export TASK_QUEUE_ENABLE=1
```

## 性能基准

### 吞吐量指标

vLLM Ascend 的性能指标取决于:
- 模型大小和量化程度
- NPU数量和配置
- 批处理大小
- 最大序列长度

### 优化建议

1. **批处理优化**: 使用连续批处理提高吞吐量
2. **量化使用**: 启用W4A8/W8A8量化减少内存占用
3. **并行策略**: 根据模型规模选择合适的TP/DP配置
4. **编译配置**: 启用CUDA Graph减少开销

## 安全特性

- **Trust Remote Code**: 支持自定义模型代码
- **API密钥管理**: 安全的密钥存储
- **访问控制**: 基于token的访问控制

## 限制与注意事项

1. **量化限制**: 仅支持ascend量化方法
2. **模型限制**: 部分特殊架构可能不支持
3. **内存限制**: 根据设备内存配置max_model_len
4. **多模态**: 需要额外配置

## 相关文档

- [部署指南](./deployment.md)
- [模型示例](./models.md)
- [量化指南](./quantization.md)
- [故障排除](./troubleshooting.md)
- [常见问题](./faq.md)

---

*本文档由 Ascend Model Verifier 自动整理*
*最后更新: 2025-03-18*
