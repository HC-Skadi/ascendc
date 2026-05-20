# HSTU 架构详细说明

## 1. HSTU 概述

HSTU (Heterogeneous Standard Transformer Unit) 是一种专为推荐系统设计的高性能Transformer变体。

## 2. 核心特性

### 2.1 注意力机制
- 支持异步累积和操作
- 优化的内存访问模式
- 融合算子支持

### 2.2 融合算子
HSTU 使用融合算子 `mxrec_opp_hstu_dense_forward` 和 `mxrec_opp_hstu_dense_backward`：
- 减少内存拷贝
- 提高计算效率
- 降低访存开销

## 3. 参数配置

### 3.1 维度参数
| 参数 | 要求 | 说明 |
|------|------|------|
| dqk | 16的整数倍 | Query-Key维度 |
| dv | 16的整数倍 | Value维度 |

### 3.2 训练参数
| 参数 | 推荐值 |
|------|--------|
| max_sequence_length | 3389 |
| local_batch_size | 32 |

## 4. 性能优化

### 4.1 融合算子优势
- 比FlashAttention2快5.3x-15.2x
- 内存占用减少约20%

### 4.2 NPU特定优化
- 使用 `PYTORCH_NPU_ALLOC_CONF=expandable_segments:True`
- 启用 `USE_NPU_HSTU=1`

## 5. 算子依赖

```
mxrec_opp_asynchronous_complete_cumsum
mxrec_opp_dense_to_jagged
mxrec_opp_index_select_for_rank1_backward
mxrec_opp_jagged_to_padded_dense
mxrec_opp_gather_for_rank1
mxrec_opp_hstu_dense_forward
mxrec_opp_hstu_dense_backward
```

## 6. 数据流

```
Input -> Embedding -> HSTU Encoder -> Output Projection -> Ranking Score
```

## 7. 适配说明

HSTU在昇腾NPU上的适配包括：
1. 自定义算子注册
2. 内存布局转换
3. 异步执行调度
