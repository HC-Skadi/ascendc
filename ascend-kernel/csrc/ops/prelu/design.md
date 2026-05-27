# PReLU Scalar/Channel 算子设计文档

本文档根据当前 `/Users/hc/ascendc/prelu_chanel` 实现更新，用于同步 `ascend-kernel/csrc/ops/prelu` 的设计语义。

## 1. 算子接口

### 1.1 算子定义

```cpp
Prelu(x, weight) -> y
```

当前 `prelu_chanel` 是 CANN 自定义算子工程，接口由 `op_host/prelu_def.cpp` 注册：

| 参数名 | 类型 | 输入/输出 | 支持的数据类型 | 描述 | 约束条件 |
|--------|------|-----------|----------------|------|----------|
| x | Tensor | 输入 | float16/float32/bfloat16 | 输入 tensor | ND，AutoContiguous |
| weight | Tensor | 输入 | float16/float32/bfloat16 | PReLU 负半轴斜率 | 1-D，shape 为 `[1]` 或 `[C]` |
| y | Tensor | 输出 | float16/float32/bfloat16 | 输出 tensor | shape 与 x 一致，AutoContiguous |

`x`、`weight`、`y` 的 dtype 必须一致。输出 shape 由 `op_host/prelu_infershape.cpp` 直接继承输入 `x`。

### 1.2 Shape 语义

- `weight` 必须是一维 tensor。
- `weightSize == 1` 时为 scalar 模式，所有元素共用 `weight[0]`。
- `weightSize != 1` 时为 channel 模式，要求 `x` rank >= 2，且 `weightSize == x.shape[1]`。
- channel 模式固定按 `[N, C, L]` 解释 contiguous 输入，其中 `N = x.shape[0]`，`C = x.shape[1]`，`L = prod(x.shape[2:])`；rank 为 2 时 `L = 1`。
- channel 模式中第 `rowIdx` 个 row 表示一个连续 `(n, c, 0:L)` 段，使用 `weight[rowIdx % C]`。

---

## 2. 计算逻辑

### 2.1 数学公式

scalar 模式：

```text
y[i] = x[i] >= 0 ? x[i] : x[i] * weight[0]
```

channel 模式：

```text
y[n, c, l] = x[n, c, l] >= 0 ? x[n, c, l] : x[n, c, l] * weight[c]
```

等价 vector 公式：

```text
y = max(x, 0) + alpha * min(x, 0)
```

### 2.2 AscendC API 调用序列

float16/float32 路径直接使用输入 dtype 计算：

```cpp
LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
LocalTensor<T> yLocal = outputQueueY.AllocTensor<T>();
LocalTensor<T> pos = tmpBufPos.Get<T>();
LocalTensor<T> neg = tmpBufNeg.Get<T>();

Maxs(pos, xLocal, static_cast<T>(0), currentNum);
Mins(neg, xLocal, static_cast<T>(0), currentNum);
Muls(neg, neg, weightVal, currentNum);
Add(yLocal, pos, neg, currentNum);
```

bfloat16 路径升精度到 float32 计算，再 cast 回 bfloat16：

```cpp
LocalTensor<bfloat16_t> xLocal = inputQueueX.DeQue<bfloat16_t>();
LocalTensor<bfloat16_t> yLocal = outputQueueY.AllocTensor<bfloat16_t>();
LocalTensor<float> xFp32 = tmpXFp32.Get<float>();
LocalTensor<float> pos = tmpBufPos.Get<float>();
LocalTensor<float> neg = tmpBufNeg.Get<float>();

Cast(xFp32, xLocal, RoundMode::CAST_NONE, currentNum);
Maxs(pos, xFp32, 0.0f, currentNum);
Mins(neg, xFp32, 0.0f, currentNum);
Muls(neg, neg, weightValFp32, currentNum);
Add(pos, pos, neg, currentNum);
Cast(yLocal, pos, RoundMode::CAST_RINT, currentNum);
```

NC weight reuse / split-C weight reuse 模式使用 weight vector，与 `neg` 做逐元素 `Mul`：

```cpp
BuildNcWeightVec(tileRows);
Maxs(pos, xLocal, 0, computeLen);
Mins(neg, xLocal, 0, computeLen);
Mul(neg, neg, weightVec, computeLen);
Add(yLocal, pos, neg, computeLen);
```

### 2.3 实现路径选择

- [x] AscendC Kernel
- [ ] CATLASS 模板库
- [ ] ACLNN 封装

PReLU 是逐元素算子，无矩阵乘、归约或跨元素依赖。channel 模式只改变 alpha 的来源和 tiling 组织方式。

---

## 3. Tiling 数据与 TilingKey

### 3.1 TilingData

当前结构体定义在 `op_kernel/prelu_tiling_data.h`：

```cpp
struct PreluTilingData {
    int64_t totalLength = 0;
    int64_t usedCoreNum = 0;
    int64_t formerNum = 0;
    int64_t formerLength = 0;
    int64_t tailLength = 0;
    int64_t tileLength = 0;

    int64_t channelSize = 1;
    int64_t innerSize = 1;
    int64_t innerSizeAligned = 1;
    int64_t baseRows = 0;
    int64_t extraRows = 0;
    int64_t tilesPerRow = 0;
    int64_t baseTasks = 0;
    int64_t extraTasks = 0;
};
```

字段使用说明：

| 字段 | scalar | channel full/split | split-L parallel | NC weight reuse | NC split-C reuse |
|------|--------|--------------------|------------------|-----------------|------------------|
| `formerNum/formerLength/tailLength` | flat core 切分 | 不使用 | 不使用 | 不使用 | 不使用 |
| `channelSize` | 默认 1 | C | C | C | C |
| `innerSize` | 默认 1 | L | L | 不参与循环 | 不参与循环 |
| `innerSizeAligned` | 默认 1 | AlignUp(L, 32B) | AlignUp(L, 32B) | AlignUp(C, 32B) | C 分块长度 |
| `baseRows/extraRows` | 不使用 | 每核 `(n,c)` row 数 | 不使用 | 每核 N row 数 | 不使用 |
| `tilesPerRow/baseTasks/extraTasks` | 不使用 | split 模式记录每 row tile 数 | task 均衡切分 | 不使用 | 每行 C 分块数和 task 均衡切分 |

### 3.2 TilingKey

当前 `op_kernel/prelu_tiling_key.h` 定义 6 个执行模式：

```cpp
#define PRELU_TPL_SCALAR_MODE 0
#define PRELU_TPL_CHANNEL_FULL_L_MODE 1
#define PRELU_TPL_CHANNEL_SPLIT_L_MODE 2
#define PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE 3
#define PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE 4
#define PRELU_TPL_CHANNEL_NC_SPLIT_C_WEIGHT_REUSE_MODE 5
```

| tilingKey | 触发条件 | Kernel 路径 |
|-----------|----------|-------------|
| `SCALAR_MODE` | `weightSize == 1` | flat elementwise |
| `CHANNEL_FULL_L_MODE` | channel 模式，且 `AlignUp(L, 32 / sizeof(T)) <= tileLength` | 每个 `(n,c)` row 一次处理完整 L |
| `CHANNEL_SPLIT_L_MODE` | channel 模式，L 超过 UB，且 row 级并行足够或 task 级并行收益不足 | 每个 `(n,c)` row 内按 L 分段 |
| `CHANNEL_SPLIT_L_PARALLEL_MODE` | `rowNum * 2 <= coreNum` 且 L 足够大，拆 task 后至少使用 2 倍 row 数的 core | 每个 task 处理一个 `(rowIdx, tileIdx)` |
| `CHANNEL_NC_WEIGHT_REUSE_MODE` | NC 场景，即 `L == 1` 且 UB 可缓存对齐后的整条 C 维 weight | 缓存整条 C 维 weight，按 N row 处理 |
| `CHANNEL_NC_SPLIT_C_WEIGHT_REUSE_MODE` | NC 场景，整条 C 维 weight 放不进 UB，但 C 分块可放入 UB | 每个 task 处理一个 `(nIdx, cTileIdx)` |

Kernel 入口通过模板参数 `schMode` 编译期分发，不在主流程中用运行时 `weightMode` 切路径。

---

## 4. Host 侧 Tiling

### 4.1 平台与 Workspace

Host 侧从平台获取 AIV 核数和 UB 大小：

```cpp
coreNum = ascendcPlatform.GetCoreNumAiv();
coreNum = std::min(coreNum, MAX_AIV_CORE_NUM); // MAX_AIV_CORE_NUM = 40
ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);
```

workspace 固定为 0：

```cpp
constexpr uint32_t WS_SYS_SIZE = 0U;
currentWorkspace[0] = WS_SYS_SIZE;
```

### 4.2 Host 校验

`GetShapeAndDtypeInfo` 完成以下校验：

1. `x/y` rank 和每个维度必须一致。
2. dtype 仅支持 `DT_FLOAT`、`DT_FLOAT16`、`DT_BF16`。
3. `x/weight/y` dtype 必须一致。
4. `weight` 必须是 1-D，且 `weightSize > 0`。
5. `weightSize != 1` 时，要求 `x` rank >= 2、`N > 0`、`C > 0`、`weightSize == C`。
6. channel 模式计算 `innerSize = prod(x.shape[2:])`，每个参与乘积的 dim 必须为正，并做 int64 溢出检查。
7. channel 模式计算 `rowNum = N * C`，并做 int64 溢出检查。

`totalLength` 使用 `inputX->GetOriginShape().GetShapeSize()`。

### 4.3 UB 级 Tiling

普通模式保留 1024B UB：

```cpp
constexpr uint64_t UB_RESERVED_SIZE = 1024U;
uint64_t usableUbSize = (ubSize > UB_RESERVED_SIZE) ? (ubSize - UB_RESERVED_SIZE) : ubSize;
```

普通模式每元素 UB 系数：

| dtype | 系数 | 来源 |
|-------|------|------|
| float32 | 24 | input/output double buffer + pos/neg |
| float16 | 12 | input/output double buffer + pos/neg |
| bfloat16 | 20 | input/output double buffer + xFp32/pos/neg |

计算公式：

```cpp
uint64_t blockElementNum = BLOCK_SIZE / typeLength; // 32B 对齐元素数
uint64_t maxTileElements = usableUbSize / GetBufferBytesPerElement(dataType);
uint64_t ubFactor = (maxTileElements / blockElementNum) * blockElementNum;
tiling->tileLength = static_cast<int64_t>(ubFactor);
```

NC weight reuse 模式使用更大的 per-element 系数，并额外预留 weight cache：

| dtype | NC 系数 | 额外缓存 |
|-------|---------|----------|
| float32 | 28 | `AlignUp(C, 32B) * 4` |
| float16 | 14 | `AlignUp(C, 32B) * 2` |
| bfloat16 | 24 | `AlignUp(C, 32B) * 2 + AlignUp(C, 32B) * 4` |

### 4.4 scalar 模式 Block Tiling

scalar 模式按 flat 元素切分：

```cpp
uint64_t coreAlignElementNum = CORE_ALIGN_SIZE / typeLength; // 512B 对齐元素数
uint64_t totalCoreElements = CeilDiv(totalNum, coreLimit);
uint64_t blockFactor = CeilDiv(totalCoreElements, coreAlignElementNum) * coreAlignElementNum;
uint64_t finalCoreNum = CeilDiv(totalNum, blockFactor);
finalCoreNum = std::min(coreLimit, finalCoreNum);

formerNum = finalCoreNum - 1;
formerLength = blockFactor;
tailLength = totalNum - formerNum * blockFactor;
```

Kernel 中 `InitScalar` 根据 `blockIdx` 计算当前 core 的 `blockOffset/blockLength`，并在 Init 阶段读取一次 `weight[0]`。

### 4.5 channel full-L 与 split-L

channel 常规路径按 `(n,c)` row 均衡切分：

```cpp
finalCoreNum = std::min(coreLimit, rowNum);
baseRows = rowNum / finalCoreNum;
extraRows = rowNum % finalCoreNum;
```

`innerSizeAligned = AlignUp(L, 32 / sizeof(T))`。若 `innerSizeAligned <= tileLength`，选择 full-L；否则选择 split-L，并记录：

```cpp
tilesPerRow = CeilDiv(innerSize, tileLength);
```

full-L 一次处理完整 L，split-L 在每个 row 内按 `tileLength` 分段。

### 4.6 split-L parallel

当 row 数明显小于 core 数，并且 L 足够大时，Host 尝试 task 级并行：

```cpp
if (rowNum * 2 <= coreLimit && innerSize >= 2 * (CORE_ALIGN_SIZE / typeLength)) {
    targetTilesPerRow = CeilDiv(coreLimit, rowNum);
    parallelTileLength = AlignUp(CeilDiv(innerSize, targetTilesPerRow), CORE_ALIGN_SIZE / typeLength);
    parallelTileLength = min(parallelTileLength, ubFactor);
    tilesPerRow = CeilDiv(innerSize, parallelTileLength);
    totalTaskNum = rowNum * tilesPerRow;
    finalCoreNum = min(coreLimit, totalTaskNum);
}
```

只有 `finalCoreNum >= min(coreLimit, rowNum * 2)` 时才进入 parallel 模式。该模式写入：

- `tileLength = parallelTileLength`
- `tilesPerRow`
- `baseTasks = totalTaskNum / finalCoreNum`
- `extraTasks = totalTaskNum % finalCoreNum`

### 4.7 NC weight reuse 与 split-C reuse

该模式优化 NC 类 channel 场景，即 `L == 1`。这不仅包含 rank=2 的 `[N, C]`，也包含 `[N, C, 1]`、`[N, C, 1, 1]` 以及更高 rank 但 `prod(x.shape[2:]) == 1` 的形状；Host 侧统一将这些形状视为 `[N, C]` 处理。

进入 NC weight reuse 不再要求 `N >= coreLimit`，也不使用固定 `C <= 256` 作为硬门槛。只要 UB 能容纳对齐后的 weight cache 和至少一行计算数据，即优先使用 weight reuse 路径。这样小 N 场景也可以按整行 `[C]` 向量化计算，避免 full-L 路径把每个 `(n,c)` 单元素 row 拆开处理。

当 C 较大导致整条 `weight[0:C]` 放不进 UB，但某个 C 分块可以放入 UB 时，进入 NC split-C weight reuse。该路径按 C 维分块缓存 weight，每个 task 处理一个 `(nIdx, cTileIdx)`，保留连续搬运和 vector `Mul`，避免退回普通 full-L 的单元素 row 调度。

触发条件：

- `innerSize == 1`
- `channelSize > 1`
- `batchSize = rowNum / channelSize > 0`
- UB 可以容纳对齐后的整条 C 维 weight cache 和至少一行 `[C]` 计算数据

Host 计算：

```cpp
alignedChannelSize = AlignUp(channelSize, 32 / typeLength);
weightCacheBytes = alignedChannelSize * typeLength;
if (dataType == DT_BF16) {
    weightCacheBytes += alignedChannelSize * sizeof(float);
}
ncMaxTileElements =
    ((usableUbSize - weightCacheBytes) / GetNcWeightReuseBufferBytesPerElement(dataType) /
     alignedChannelSize) *
    alignedChannelSize;
```

若整条 C 可行，则：

- `innerSizeAligned = alignedChannelSize`
- `tileLength = ncMaxTileElements`
- `usedCoreNum = min(coreLimit, batchSize)`
- `baseRows/extraRows` 按 N row 分配

当 `batchSize < coreLimit` 时，该分支只启动 `batchSize` 个 core；这是有意的。`[N, C]` 场景中每个 core 处理一行或多行连续 C 维数据，并复用 UB 中的 weight vector。相比 full-L 模式按 `(n,c)` 单元素 row 调度，NC weight reuse 更适合小 L 场景的向量化和减少 weight GM 访问。

当整条 C 放不下时，继续尝试 split-C：

```cpp
splitCBytesPerElement = weightCacheBytesPerElement + GetNcWeightReuseBufferBytesPerElement(dataType);
maxSplitCElements = usableUbSize / splitCBytesPerElement;
splitCTileLength = AlignDown(maxSplitCElements, 32 / sizeof(T));
cTileNum = CeilDiv(C, splitCTileLength);
totalTaskNum = N * cTileNum;
usedCoreNum = min(coreLimit, totalTaskNum);
```

若 `splitCTileLength >= 32 / sizeof(T)`，则进入 `CHANNEL_NC_SPLIT_C_WEIGHT_REUSE_MODE`，写入：

- `tileLength = splitCTileLength`
- `innerSizeAligned = splitCTileLength`
- `tilesPerRow = cTileNum`
- `baseTasks = totalTaskNum / usedCoreNum`
- `extraTasks = totalTaskNum % usedCoreNum`

若连一个 C 分块都无法放入 UB，再回退到普通 channel full-L 路径。实际实现可保留一个非常宽松的保护上限用于防止异常 shape，但该上限不应替代 UB 容量判断。

---

## 5. Kernel 端实现要点

### 5.1 Kernel 入口

`op_kernel/prelu.cpp` 使用模板 `schMode` 分发：

```cpp
if constexpr (schMode == PRELU_TPL_CHANNEL_FULL_L_MODE) {
    op.InitChannel(...);
    op.ProcessChannelFullL();
} else if constexpr (schMode == PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE) {
    op.InitChannelNcWeightReuse(...);
    op.ProcessChannelNcWeightReuse();
} else if constexpr (schMode == PRELU_TPL_CHANNEL_NC_SPLIT_C_WEIGHT_REUSE_MODE) {
    op.InitChannelNcSplitCWeightReuse(...);
    op.ProcessChannelNcSplitCWeightReuse();
} else if constexpr (schMode == PRELU_TPL_CHANNEL_SPLIT_L_MODE) {
    op.InitChannel(...);
    op.ProcessChannelSplitL();
} else if constexpr (schMode == PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE) {
    op.InitChannelSplitLParallel(...);
    op.ProcessChannelSplitLParallel();
} else {
    op.InitScalar(...);
    op.ProcessScalar();
}
```

### 5.2 scalar 流程

```cpp
for (int64_t i = 0; i < tileNum; ++i) {
    currentNum = (i == tileNum - 1) ? (blockLength - i * ubLength) : ubLength;
    CopyIn(i, currentNum);
    Compute(currentNum);
    CopyOut(i, currentNum);
}
```

scalar 模式使用 `formerNum/formerLength/tailLength` 做 flat block 切分。bfloat16 scalar weight 通过 `LoadBf16ScalarAsFloat` 读取为 float，避免依赖 bfloat16 标量 Cast 重载。

### 5.3 channel full-L

每个 core 处理若干 `(n,c)` row。每个 row 读取一次 `weight[c]`：

```cpp
for (rowProgress = 0; rowProgress < blockRowNum; ++rowProgress) {
    rowIdx = rowOffset + rowProgress;
    channelIdx = rowIdx % channelSize;
    gmOffset = rowIdx * innerSize;
    LoadChannelWeight(channelIdx);
    CopyInByOffset(gmOffset, realLen, computeLen);
    Compute(computeLen);
    CopyOutByOffset(gmOffset, realLen);
}
```

`realLen = innerSize`，`computeLen = innerSizeAligned`。非 32B 对齐尾部通过 `DataCopyPad` 补零，CopyOut 只写真实 L。

### 5.4 channel split-L

split-L 仍按 row 分 core，row 内分段：

```cpp
for each row:
    LoadChannelWeight(rowIdx % C);
    for (tileOffset = 0; tileOffset < innerSize; tileOffset += ubLength) {
        realLen = min(ubLength, innerSize - tileOffset);
        computeLen = AlignUp(realLen, 32 / sizeof(T));
        gmOffset = rowIdx * innerSize + tileOffset;
        CopyInByOffset(gmOffset, realLen, computeLen);
        Compute(computeLen);
        CopyOutByOffset(gmOffset, realLen);
    }
```

同一个 row 的所有 L 分段复用同一个 `weight[c]`。

### 5.5 channel split-L parallel

parallel 模式按 task 切分，每个 task 对应 `(rowIdx, tileIdx)`：

```cpp
taskIdx = taskOffset + taskProgress;
rowIdx = taskIdx / tilesPerRow;
tileIdx = taskIdx % tilesPerRow;
tileOffset = tileIdx * ubLength;
channelIdx = rowIdx % channelSize;
gmOffset = rowIdx * innerSize + tileOffset;
```

同一 core 连续 task 若属于同一 channel，则通过 `lastChannelIdx` 跳过重复 `LoadChannelWeight`。

### 5.6 NC weight reuse

NC weight reuse 模式面向 `L == 1` 的 NC 类输入，包括 `[N, C]`、`[N, C, 1]`、`[N, C, 1, 1]` 等等价形状。Init 阶段一次性把 `weight[0:C]` 复制到 UB，并按 32B 对齐；bfloat16 还会额外转换出 float weight cache。

处理流程：

```cpp
for (rowProgress = 0; rowProgress < blockRowNum; rowProgress += rowsPerTile) {
    tileRows = min(rowsPerTile, blockRowNum - rowProgress);
    computeLen = tileRows * alignedChannelSize;
    nOffset = rowOffset + rowProgress;

    CopyInNcByRows(nOffset, tileRows);
    BuildNcWeightVec(tileRows);
    ComputeNc(computeLen);
    CopyOutNcByRows(nOffset, tileRows);
}
```

该模式把一行 `[C]` 的 weight 扩展为 `tileRows * alignedChannelSize` 的 `weightVec`，使用逐元素 `Mul` 替代每个 channel 的 scalar `Muls`，减少重复 GM 读取 weight。

### 5.7 NC split-C weight reuse

split-C 模式面向 `L == 1` 且 C 较大的 NC 类输入。Init 阶段不缓存整条 C 维 weight，而是按 task 动态缓存当前 C 分块。

每个 task 解码为一个 `(nIdx, cTileIdx)`：

```cpp
taskIdx = taskOffset + taskProgress;
nIdx = taskIdx / tilesPerRow;
cTileIdx = taskIdx % tilesPerRow;
cOffset = cTileIdx * alignedChannelSize;
realC = min(alignedChannelSize, C - cOffset);
gmOffset = nIdx * C + cOffset;
```

处理流程：

```cpp
CopyWeightTile(cOffset, realC, alignedChannelSize);
CopyInByOffset(gmOffset, realC, alignedChannelSize);
BuildNcWeightVec(1);
ComputeNc(alignedChannelSize);
CopyOutByOffset(gmOffset, realC);
```

最后一个 C 分块可能不足 `alignedChannelSize`，通过 `DataCopyPad` 补齐计算，CopyOut 只写回真实 `realC`。该路径比普通 full-L 对大 C 的 `[N,C]` 场景更友好，因为单次搬运和计算粒度是 C 分块，而不是单个 `(n,c)` 元素。

---

## 6. Workspace 需求

当前实现 workspace size 为 0。kernel 所需临时空间均来自 UB：

- input/output double buffer
- scalar/channel 临时 `pos/neg`
- bfloat16 的 `tmpXFp32`
- NC weight reuse 的 `weightBuf/weightVecBuf/weightFp32Buf`
- NC split-C reuse 复用 `weightBuf/weightVecBuf/weightFp32Buf`，但 weight 按 C 分块动态搬入

---

## 7. 性能与约束

### 7.1 性能特征

- 算子整体为 memory-bound elementwise。
- scalar 模式 flat 切分，适合任意 ND 输入。
- channel full-L 避免 row 内循环，适合 L 可放入 UB 的场景。
- channel split-L 支持大 L，不要求完整 L 放入 UB。
- channel split-L parallel 通过拆分 L 维 task 提升 `N*C` 较小、L 很大时的 AIV 利用率。
- NC weight reuse 针对 `L == 1` 的 NC 类场景，把 weight 缓存在 UB，减少重复读取并使用 vector `Mul`。
- NC split-C reuse 针对 C 较大、整条 C 放不进 UB 的 NC 类场景，按 C 分块缓存 weight，避免退回单元素 full-L。
- float16/float32 直接按原 dtype vector 计算；bfloat16 升到 float32 计算。

### 7.2 当前限制

- 仅注册 `ascend910b` 配置。
- `weight` 必须是一维 tensor，不支持 0-D scalar。
- channel broadcast 固定使用第 1 维 C，不支持按其他维度 broadcast。
- `x/weight/y` dtype 必须一致。
- NC weight reuse 仅在 `L == 1` 且 UB 能容纳整条 C 时启用；不再以 `N >= coreLimit` 或固定 `C <= 256` 作为硬条件。
- NC split-C reuse 在 `L == 1` 且整条 C 放不进 UB、但 C 分块可放入 UB 时启用。

---

## 8. 测试覆盖

当前 `prelu_chanel/tests/ut/op_host/test_prelu_tiling.cpp` 覆盖：

- scalar：`x=[7], weight=[1]`
- `N=1,C=1,weight=[1]` 仍走 scalar
- channel full-L：`x=[2,3,5], weight=[3]`
- NC weight reuse：`x=[64,3], weight=[3]`
- channel split-L：`x=[64,2,20000], weight=[2]`
- split-L 收益不足 fallback：`x=[16,2,20000], weight=[2]`
- split-L parallel：`x=[1,2,20000], weight=[2]`

当前 `prelu_chanel/tests/ut/op_kernel/test_prelu.cpp` 覆盖：

- scalar kernel
- channel full-L kernel
- channel NC weight reuse kernel
- channel NC split-C weight reuse kernel
- channel split-L kernel
- channel split-L parallel kernel

建议同步到 `ascend-kernel` 后补充：

- float16、bfloat16、float32 三种 dtype 的端到端精度用例。
- 非法参数：weight rank 非 1、weight size 与 C 不一致、dtype 不一致、channel rank < 2。
- NC weight reuse 的边界：`C=256/257/1024/4096`，以及超过 UB 可容纳整行时进入 split-C。
- split-C 边界：大 C case 验证 tilingKey 为 `CHANNEL_NC_SPLIT_C_WEIGHT_REUSE_MODE`，并覆盖最后一个 C 分块非对齐。
- 小 N 的 NC 类场景，例如 `[1, 3]`、`[2, 64]`、`[1, 1024, 1, 1]`，确认仍进入 NC weight reuse 分支。
- 等价 shape：`[N, C]`、`[N, C, 1]`、`[N, C, 1, 1]` 的 tilingKey 和计算结果一致。

---

## 9. 参考文件

- `/Users/hc/ascendc/prelu_chanel/op_host/prelu_def.cpp`
- `/Users/hc/ascendc/prelu_chanel/op_host/prelu_infershape.cpp`
- `/Users/hc/ascendc/prelu_chanel/op_host/prelu_tiling.cpp`
- `/Users/hc/ascendc/prelu_chanel/op_kernel/prelu_tiling_data.h`
- `/Users/hc/ascendc/prelu_chanel/op_kernel/prelu_tiling_key.h`
- `/Users/hc/ascendc/prelu_chanel/op_kernel/prelu.cpp`
- `/Users/hc/ascendc/prelu_chanel/op_kernel/prelu.h`
