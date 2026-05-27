# PReLU Scalar/Channel 算子设计文档

## 1. 算子接口

### 1.1 函数签名

```cpp
Prelu(x, weight) -> y
```

`prelu_chanel` 当前是 CANN 自定义算子工程，接口由 `op_host/prelu_def.cpp` 注册：

| 参数名 | 类型 | 输入/输出 | 支持的数据类型 | 描述 | 约束条件 |
|--------|------|-----------|----------------|------|----------|
| x | Tensor | 输入 | float16/float32/bfloat16 | 输入 tensor | scalar weight 支持 ND；channel weight 支持 rank >= 2，按 `[N, C, ...]` 解析 |
| weight | Tensor | 输入 | float16/float32/bfloat16 | PReLU 负半轴斜率 | 支持 shape `[1]` 或 `[C]` |
| y | Tensor | 输出 | float16/float32/bfloat16 | 输出 tensor | shape 与 x 一致 |

### 1.2 支持的数据类型

- [x] float16
- [x] float32
- [x] bfloat16

`x`、`weight`、`y` 的 dtype 必须一致。保留 scalar weight `[1]` 路径，并新增 channel weight `[C]` 路径。

### 1.3 Shape 语义

- 输出 shape 直接继承输入 `x` shape。
- Host tiling 阶段校验 `x` 与 `y` storage shape 完全一致。
- `weight` 为 `[1]` 时，所有元素共用 `weight[0]`，输入 shape 仍按 ND flat 处理。
- `weight` 为 `[C]` 时，输入 rank 必须大于等于 2，固定 `N = x.shape[0]`、`C = x.shape[1]`，`L = prod(x.shape[2:])`；当 rank 为 2 时 `L = 1`。
- channel 路径按逻辑 `[N, C, L]` 展开，每个 `(n, c, :)` 连续 L 段共用 `weight[c]`。
- channel weight 支持 full-L 和 split-L 两种路径：`AlignUp(L, 32 / sizeof(T)) <= tileLength` 时一个 UB 循环处理完整 L；否则在 L 维分段处理，每段长度不超过 `tileLength`。非 32B 对齐的尾部由 `DataCopyPad` padding。

---

## 2. 计算逻辑

### 2.1 数学公式

```text
y[n, c, l] = max(x[n, c, l], 0) + weight[c] * min(x[n, c, l], 0)
```

等价于：

```text
y[n, c, l] = x[n, c, l] >= 0 ? x[n, c, l] : x[n, c, l] * weight[c]
```

scalar weight `[1]` 是 channel 公式的特例，`weight[c]` 固定为 `weight[0]`。

### 2.2 AscendC API 调用序列

在 `prelu_chanel` 现有实现基础上扩展 channel weight。计算 API 仍使用 `Maxs + Mins + Muls + Add`，不生成 `weightLocal`，不使用 `Duplicate` 展开 weight。

**float16/float32 路径：**

```cpp
LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
LocalTensor<T> yLocal = outputQueueY.AllocTensor<T>();
LocalTensor<T> pos = tmpBufPos.Get<T>();
LocalTensor<T> neg = tmpBufNeg.Get<T>();

Maxs(pos, xLocal, static_cast<T>(0), currentNum);
Mins(neg, xLocal, static_cast<T>(0), currentNum);
Muls(neg, neg, weightVal, currentNum); // scalar 路径 weightVal=weight[0]；channel 路径 weightVal=weight[c]
Add(yLocal, pos, neg, currentNum);
```

**bfloat16 路径：**

```cpp
LocalTensor<bfloat16_t> xLocal = inputQueueX.DeQue<bfloat16_t>();
LocalTensor<bfloat16_t> yLocal = outputQueueY.AllocTensor<bfloat16_t>();
LocalTensor<float> xFp32 = tmpXFp32.Get<float>();
LocalTensor<float> pos = tmpBufPos.Get<float>();
LocalTensor<float> neg = tmpBufNeg.Get<float>();

Cast(xFp32, xLocal, RoundMode::CAST_NONE, currentNum);
Maxs(pos, xFp32, 0.0f, currentNum);
Mins(neg, xFp32, 0.0f, currentNum);
Muls(neg, neg, weightValFp32, currentNum); // channel 路径 currentNum=computeLen
Add(pos, pos, neg, currentNum);
Cast(yLocal, pos, RoundMode::CAST_RINT, currentNum);
```

### 2.3 weight 读取

scalar weight `[1]` 路径在 `Init` 阶段只读取一次 `weight[0]`：

```cpp
if constexpr (std::is_same_v<T, bfloat16_t>) {
    T scalarWeight = *((__gm__ T*)weight);
    weightValFp32 = AscendC::Cast(scalarWeight);
} else {
    T scalarWeight = *((__gm__ T*)weight);
    weightVal = scalarWeight;
}
```

channel weight `[C]` 路径在每个 row 计算前读取一次 `weight[c]`；split-L 时同一个 row 内所有 L 分段复用该标量：

```cpp
int64_t rowIdx = rowOffset + rowProgress;
int64_t channelIdx = rowIdx % channelSize;
T scalarWeight = *((__gm__ T*)weight + channelIdx);
weightVal = scalarWeight;
```

bfloat16 路径读取后转换为 float：

```cpp
T scalarWeight = *((__gm__ T*)weight + channelIdx);
weightValFp32 = AscendC::Cast(scalarWeight);
```

该方案仍然不需要生成 `weightLocal`，也不需要 `Duplicate` 扩展到 UB。对 rank >= 2 的输入，kernel 将其按 contiguous 逻辑展开为 `[N, C, L]`。当 L 可放入 UB 时一次 `CopyIn/Compute/CopyOut` 处理完整 L；当 L 超过 UB 可处理长度时，在 L 维拆成多个 tile，每个 tile 复用同一个 `weight[c]`，`Muls` 的标量参数仍是当前通道的 `weight[c]`。

### 2.4 实现路径选择

- [x] AscendC Kernel
- [ ] CATLASS 模板库
- [ ] ACLNN 封装

PReLU 是纯逐元素算子，无矩阵乘、归约或跨元素依赖。channel weight 只改变每个 row 使用的 scalar，不改变 vector 计算主体。

---

## 3. Tiling 策略

### 3.1 Tiling 参数结构体

需要在 `prelu_chanel/op_kernel/prelu_tiling_data.h` 现有字段基础上增加 channel weight 所需的 shape/模式字段。推荐结构如下：

```cpp
struct PreluTilingData {
    int64_t totalLength = 0;    // x 总元素数
    int64_t usedCoreNum = 0;    // 实际使用 AIV 核数

    int64_t formerNum = 0;      // scalar 路径使用；channel 路径可置 0
    int64_t formerLength = 0;   // scalar 路径每核元素数；channel 路径可置 0
    int64_t tailLength = 0;     // scalar 路径尾核元素数；channel 路径可置 0
    int64_t tileLength = 0;     // UB 最大可处理元素数；split-L 路径每次最多处理 tileLength 个元素

    int64_t channelSize = 1;    // C
    int64_t innerSize = 1;      // L，真实搬运长度
    int64_t innerSizeAligned = 1; // AlignUp(L, 32 / sizeof(T))，full-L 路径计算长度
    int64_t baseRows = 0;       // channel 路径每核基础 row 数
    int64_t extraRows = 0;      // channel 路径前 extraRows 个 core 各多处理 1 个 row

    int64_t tilesPerRow = 0;    // split-L parallel 路径每个 row 的 L 维 tile 数
    int64_t baseTasks = 0;      // split-L parallel 路径每核基础 task 数
    int64_t extraTasks = 0;     // split-L parallel 路径前 extraTasks 个 core 各多处理 1 个 task
};
```

scalar 路径可继续使用原有 flat element tiling；channel full-L 和普通 split-L 路径按 row 切分，row 的定义是一个连续 `(n, c, :)` L 段。split-L parallel 路径把每个 `(rowIdx, tileIdx)` 作为独立 task 做核间切分，用于 `N*C` 较小但 `L` 很大的场景。

字段使用约束：

- scalar tilingKey：只使用 `formerNum/formerLength/tailLength/tileLength` 做 flat element tiling；channel 字段可保持默认值，kernel 不读取这些字段。
- full-L channel tilingKey：以 `rowOffset/blockRowNum/innerSize/innerSizeAligned` 作为 channel 分支的循环、搬运和计算依据；`formerNum/formerLength/tailLength` 可作为兼容字段保留，但不能用于 channel row 分配或循环边界。
- split-L channel tilingKey：仍以 `rowOffset/blockRowNum/innerSize/tileLength` 作为循环和搬运依据，row 内再按 `tileLength` 分段；每个分段单独计算 `realLen` 和 `computeLen=AlignUp(realLen, 32 / sizeof(T))`。
- split-L parallel channel tilingKey：以 kernel 本地计算出的 `taskOffset/taskNum` 和 tiling data 中的 `tilesPerRow/innerSize/tileLength` 作为循环和搬运依据；每个 task 对应一个 `(rowIdx, tileIdx)`，通过 `rowIdx = taskIdx / tilesPerRow`、`tileIdx = taskIdx % tilesPerRow` 还原 GM offset。
- `weightSize/weightMode/rowNum/totalTaskNum` 是 Host 侧校验、分支选择或中间计算变量，不写入 tiling data；Kernel 主执行路径必须由 tilingKey 的 `schMode` 编译期分发决定，不能再通过运行时 `if (weightMode)` 选择路径。

### 3.2 TilingKey 设计

当前实现不应固定使用 `PRELU_TPL_SCH_MODE_0`。tilingKey 需要表达执行路径，使 scalar 和 channel 在 Kernel 入口处完成编译期分发。

推荐定义：

```cpp
#define PRELU_TPL_SCALAR_MODE 0
#define PRELU_TPL_CHANNEL_FULL_L_MODE 1
#define PRELU_TPL_CHANNEL_SPLIT_L_MODE 2
#define PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE 3

ASCENDC_TPL_ARGS_DECL(
    Prelu,
    ASCENDC_TPL_UINT_DECL(schMode, 2, ASCENDC_TPL_UI_LIST,
        PRELU_TPL_SCALAR_MODE, PRELU_TPL_CHANNEL_FULL_L_MODE, PRELU_TPL_CHANNEL_SPLIT_L_MODE,
        PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE));

ASCENDC_TPL_SEL(ASCENDC_TPL_ARGS_SEL(
    ASCENDC_TPL_UINT_SEL(schMode, ASCENDC_TPL_UI_LIST,
        PRELU_TPL_SCALAR_MODE, PRELU_TPL_CHANNEL_FULL_L_MODE, PRELU_TPL_CHANNEL_SPLIT_L_MODE,
        PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE)));
```

tilingKey 语义：

| tilingKey | 触发条件 | Kernel 路径 | 读取字段 |
|-----------|----------|-------------|----------|
| `PRELU_TPL_SCALAR_MODE` | `weight` shape 为 `[1]` | scalar flat 路径 | `formerNum/formerLength/tailLength/tileLength` |
| `PRELU_TPL_CHANNEL_FULL_L_MODE` | `weight` shape 为 `[C]` 且 `AlignUp(L, 32 / sizeof(T)) <= tileLength` | channel full-L row 路径 | `channelSize/innerSize/innerSizeAligned/baseRows/extraRows/tileLength` |
| `PRELU_TPL_CHANNEL_SPLIT_L_MODE` | `weight` shape 为 `[C]` 且 `AlignUp(L, 32 / sizeof(T)) > tileLength`，并且 `rowNum >= coreNum` 或 task 级并行不能增加可用 core 数 | channel split-L row 路径 | `channelSize/innerSize/baseRows/extraRows/tileLength` |
| `PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE` | `weight` shape 为 `[C]` 且 `AlignUp(L, 32 / sizeof(T)) > tileLength`，并且 `rowNum < coreNum` 且 `rowNum * CeilDiv(L, tileLength) > rowNum` | channel split-L task 路径 | `channelSize/innerSize/tilesPerRow/baseTasks/extraTasks/tileLength` |

full-L 路径是小 L 的快速路径；普通 split-L 路径用于 `H*W` 或更高维乘积超过 UB 且 `rowNum` 足以覆盖 core 的场景。split-L parallel 路径用于 `N*C` 较小、`L` 很大的场景，避免普通 split-L 最多只使用 `rowNum` 个 core。后续如果需要 small-L 多 row 合并优化，应继续新增 tilingKey，例如 `PRELU_TPL_CHANNEL_MULTI_ROW_MODE`，不要把多种策略继续塞进同一个 runtime 分支。

### 3.3 Host 侧校验

Host tiling 按以下顺序执行：

1. 获取平台 `ubSize` 与 AIV `coreNum`。
2. 设置 workspace size 为 0。
3. 校验 `weight` shape 必须为 `[1]` 或 `[C]`。
4. 校验 `x/y` shape 相同。
5. 校验 dtype 为 `DT_FLOAT`、`DT_FLOAT16` 或 `DT_BF16`，且 `x/weight/y` dtype 一致。
6. 计算 `totalLength = inputX->GetOriginShape().GetShapeSize()`。
7. `weightSize == 1` 时设置 `weightMode=0`，沿用 scalar flat tiling。
8. `weightSize != 1` 时要求 `x` rank >= 2，固定 `N=xShape.GetDim(0)`、`C=xShape.GetDim(1)`、`L=prod(xShape.GetDim(i), i>=2)`；rank 为 2 时 `L=1`。
9. channel 路径要求 `weightSize == C`。
10. 计算 `innerSize=L`、`rowNum=N*C`、`innerSizeAligned=AlignUp(L, 32 / sizeof(T))` 时必须做正数和 `int64_t` 溢出保护，检查通过后再设置 `weightMode=1`、`channelSize=C`、`innerSize`、`innerSizeAligned`、`rowNum`。
11. 计算 block 级与 UB 级 tiling，得到 `ubFactor` 并写入 `tiling->tileLength`。channel 路径不再因为 `innerSizeAligned > tileLength` 返回失败，而是继续在 split-L 类 tilingKey 中选择。
12. 当 `weightMode=1` 且 `innerSizeAligned > tileLength` 时，使用 `uint64_t` 中间变量计算 `tilesPerRow=CeilDiv(innerSize, tileLength)` 与 `totalTaskNum=rowNum*tilesPerRow`，写入 `tilesPerRow/baseTasks/extraTasks` 前检查相关值不超过 `int64_t::max()`。若 `rowNum < coreNum && totalTaskNum > rowNum`，选择 split-L parallel；否则选择普通 split-L。该条件允许 `totalTaskNum` 小于 `coreNum` 但仍能从 `rowNum` 个 core 提升到更多 core 的场景进入 parallel 路径。
13. 普通 channel row 路径的 `usedCoreNum = min(coreNum, rowNum)`；split-L parallel 路径的 `usedCoreNum = min(coreNum, totalTaskNum)`，并写入 `tiling->usedCoreNum`。`context->SetBlockDim(usedCoreNum)` 必须使用当前路径重新计算后的 `usedCoreNum`。
14. 根据 `weightMode`、`innerSizeAligned` 和 Host 侧 `useSplitLParallel` 判定结果设置 tilingKey，`tileLength` 必须来自当前 tiling 计算得到的 `ubFactor`，不能使用未定义局部变量：

```cpp
int64_t tileLength = static_cast<int64_t>(ubFactor);
tiling->tileLength = tileLength;

uint64_t tilingKey = GET_TPL_TILING_KEY(PRELU_TPL_SCALAR_MODE);
if (weightMode == 1) {
    if (innerSizeAligned <= tileLength) {
        tilingKey = GET_TPL_TILING_KEY(PRELU_TPL_CHANNEL_FULL_L_MODE);
    } else if (useSplitLParallel) {
        tilingKey = GET_TPL_TILING_KEY(PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE);
    } else {
        tilingKey = GET_TPL_TILING_KEY(PRELU_TPL_CHANNEL_SPLIT_L_MODE);
    }
}
context->SetTilingKey(tilingKey);
```

15. `context->SetBlockDim(usedCoreNum)`。

`rowNum=N*C` 的溢出检查需要显式完成：

```cpp
OP_CHECK_IF(N <= 0, OP_LOGE(context, "Prelu: N must be positive"), return ge::GRAPH_FAILED);
OP_CHECK_IF(
    static_cast<uint64_t>(N) > static_cast<uint64_t>(std::numeric_limits<int64_t>::max()) /
        static_cast<uint64_t>(channelSize),
    OP_LOGE(context, "Prelu: rowNum exceeds int64 range"),
    return ge::GRAPH_FAILED);
int64_t rowNum = N * channelSize;
```

### 3.4 Block 级 Tiling

#### scalar weight `[1]`

常量与当前实现一致：

```cpp
constexpr uint32_t BLOCK_SIZE = 32U;
constexpr uint32_t CORE_ALIGN_SIZE = 512U;
```

计算公式：

```cpp
uint64_t blockElementNum = BLOCK_SIZE / typeLength;
uint64_t coreAlignElementNum = CORE_ALIGN_SIZE / typeLength;
uint64_t coreLimit = static_cast<uint64_t>(coreNum);
uint64_t totalCoreElements = CeilDiv(totalNum, coreLimit);
uint64_t blockFactor = CeilDiv(totalCoreElements, coreAlignElementNum) * coreAlignElementNum;
if (blockFactor == 0) {
    blockFactor = coreAlignElementNum;
}

uint64_t finalCoreNum = totalNum == 0 ? 1U : CeilDiv(totalNum, blockFactor);
finalCoreNum = std::min(coreLimit, finalCoreNum);

formerNum = finalCoreNum > 0 ? finalCoreNum - 1U : 0U;
formerLength = blockFactor;
tailLength = totalNum - formerNum * blockFactor;
```

Kernel 中每个 core 的偏移与长度：

```cpp
int64_t blockIdx = GetBlockIdx();
int64_t blockOffset = blockIdx * tilingData->formerLength;
if (blockIdx < tilingData->formerNum) {
    blockLength = tilingData->formerLength;
} else if (blockIdx < tilingData->usedCoreNum) {
    blockLength = tilingData->tailLength;
} else {
    blockLength = 0;
}
```

#### channel weight `[C]`

channel full-L 和普通 split-L 路径按 row 切分；split-L parallel 路径按 `(rowIdx, tileIdx)` task 切分，允许同一个 row 的不同 L 分段分配到不同 core。输入按 contiguous 内存逻辑视为 `[N, C, L]`，其中 `L = prod(x.shape[2:])`；每个 row 对应 `[n, c, 0:L]`，GM 起始偏移为 `rowIdx * innerSize`。

推荐使用 `baseRows + extraRows` 做均衡分配，而不是只设置一个尾核。这样当 `rowNum` 不能整除 `usedCoreNum` 时，前 `extraRows` 个 core 各多处理 1 个 row，任意两个 core 的 row 数最多相差 1。

```cpp
uint64_t rowNum = static_cast<uint64_t>(N * C);
uint64_t usedCoreNum = rowNum == 0 ? 1U : std::min(static_cast<uint64_t>(coreNum), rowNum);
uint64_t baseRows = rowNum / usedCoreNum;
uint64_t extraRows = rowNum % usedCoreNum;
```

Kernel 中每个 core 的 row 偏移与 row 数：

```cpp
int64_t blockIdx = GetBlockIdx();
if (blockIdx < tilingData->extraRows) {
    blockRowNum = tilingData->baseRows + 1;
    rowOffset = blockIdx * (tilingData->baseRows + 1);
} else if (blockIdx < tilingData->usedCoreNum) {
    blockRowNum = tilingData->baseRows;
    rowOffset = tilingData->extraRows * (tilingData->baseRows + 1) +
                (blockIdx - tilingData->extraRows) * tilingData->baseRows;
} else {
    blockRowNum = 0;
    rowOffset = 0;
}
```

#### channel split-L parallel task 切分

普通 channel split-L 仍按 row 分 core。当 `rowNum=N*C` 小于 AIV core 数且 `L` 很大时，最多只能使用 `rowNum` 个 core，核间并行度不足。split-L parallel 路径把每个 row 的每个 L 分段视为一个独立 task，以 task 为粒度做核间均衡分配：

```cpp
uint64_t tilesPerRow = CeilDiv(static_cast<uint64_t>(innerSize), static_cast<uint64_t>(tileLength));
OP_CHECK_IF(
    tilesPerRow > static_cast<uint64_t>(std::numeric_limits<int64_t>::max()),
    OP_LOGE(context, "Prelu: tilesPerRow exceeds int64 range"),
    return ge::GRAPH_FAILED);
OP_CHECK_IF(
    static_cast<uint64_t>(rowNum) > std::numeric_limits<uint64_t>::max() / tilesPerRow,
    OP_LOGE(context, "Prelu: totalTaskNum exceeds uint64 range"),
    return ge::GRAPH_FAILED);
uint64_t totalTaskNum = static_cast<uint64_t>(rowNum) * tilesPerRow;
OP_CHECK_IF(
    totalTaskNum > static_cast<uint64_t>(std::numeric_limits<int64_t>::max()),
    OP_LOGE(context, "Prelu: totalTaskNum exceeds int64 range"),
    return ge::GRAPH_FAILED);
uint64_t usedCoreNum = totalTaskNum == 0 ? 1U : std::min(static_cast<uint64_t>(coreNum), totalTaskNum);
uint64_t baseTasks = totalTaskNum / usedCoreNum;
uint64_t extraTasks = totalTaskNum % usedCoreNum;

tiling->tilesPerRow = static_cast<int64_t>(tilesPerRow);
tiling->usedCoreNum = static_cast<int64_t>(usedCoreNum);
tiling->baseTasks = static_cast<int64_t>(baseTasks);
tiling->extraTasks = static_cast<int64_t>(extraTasks);
```

Kernel 中每个 core 的 task 偏移与 task 数：

```cpp
int64_t blockIdx = GetBlockIdx();
if (blockIdx < tilingData->extraTasks) {
    taskNum = tilingData->baseTasks + 1;
    taskOffset = blockIdx * (tilingData->baseTasks + 1);
} else if (blockIdx < tilingData->usedCoreNum) {
    taskNum = tilingData->baseTasks;
    taskOffset = tilingData->extraTasks * (tilingData->baseTasks + 1) +
                 (blockIdx - tilingData->extraTasks) * tilingData->baseTasks;
} else {
    taskNum = 0;
    taskOffset = 0;
}
```

每个 task 还原为一个 `(rowIdx, tileIdx)`：

```cpp
int64_t taskIdx = taskOffset + taskProgress;
int64_t rowIdx = taskIdx / tilingData->tilesPerRow;
int64_t tileIdx = taskIdx % tilingData->tilesPerRow;
int64_t tileOffset = tileIdx * tilingData->tileLength;
```

split-L parallel 会让同一个 row 的不同 L 分段分配到不同 core，因此每个 task 都需要根据 `rowIdx` 重新读取一次 `weight[rowIdx % C]`。相比普通 split-L 每个 row 只读取一次 weight，该策略增加少量标量读取和 task 解码开销，但能显著改善 `rowNum < coreNum`、`L` 很大场景的 AIV 利用率。

### 3.5 UB 级 Tiling

当前实现保留 1024B UB：

```cpp
constexpr uint64_t UB_RESERVED_SIZE = 1024U;
uint64_t usableUbSize = (ubSize > UB_RESERVED_SIZE) ? (ubSize - UB_RESERVED_SIZE) : ubSize;
```

每元素 UB 系数来自 `GetBufferBytesPerElement`：

| dtype | 系数 | 依据 |
|-------|------|------|
| float32 | 24 | inputQueueX double buffer 8B + outputQueueY double buffer 8B + pos 4B + neg 4B |
| float16 | 12 | inputQueueX double buffer 4B + outputQueueY double buffer 4B + pos 2B + neg 2B |
| bfloat16 | 20 | inputQueueX double buffer 4B + outputQueueY double buffer 4B + xFp32 4B + pos 4B + neg 4B |

计算公式：

```cpp
uint64_t bufferBytesPerElement = GetBufferBytesPerElement(dataType);
uint64_t maxTileElements = usableUbSize / bufferBytesPerElement;
uint64_t blockElementNum = BLOCK_SIZE / typeLength;
uint64_t ubFactor = (maxTileElements / blockElementNum) * blockElementNum;
tiling->tileLength = static_cast<int64_t>(ubFactor);
```

`tileLength` 按 32B 对齐：float32 是 8 的倍数，float16/bfloat16 是 16 的倍数。

channel weight 路径不要求完整 L 一定放入 UB。`innerSize` 是真实 L 长度，`innerSizeAligned` 是 `AlignUp(L, 32 / sizeof(T))`，用于判断是否可走 full-L 路径：

```cpp
uint64_t blockElementNum = BLOCK_SIZE / typeLength;
OP_CHECK_IF(innerSize <= 0, OP_LOGE(context, "Prelu: L must be positive"), return ge::GRAPH_FAILED);
// 使用 std::numeric_limits 时需要包含 <limits>。
OP_CHECK_IF(
    static_cast<uint64_t>(innerSize) > UINT64_MAX - blockElementNum + 1U,
    OP_LOGE(context, "Prelu: L is too large to align"),
    return ge::GRAPH_FAILED);
uint64_t innerSizeAligned = CeilDiv(static_cast<uint64_t>(innerSize), blockElementNum) * blockElementNum;
OP_CHECK_IF(
    innerSizeAligned > static_cast<uint64_t>(std::numeric_limits<int64_t>::max()),
    OP_LOGE(context, "Prelu: aligned L exceeds int64 range"),
    return ge::GRAPH_FAILED);
bool channelFullL = innerSizeAligned <= ubFactor;
```

当 `channelFullL == true`，Kernel 使用 `PRELU_TPL_CHANNEL_FULL_L_MODE`，一个 row 一次搬运和计算完整 L。

当 `channelFullL == false`，普通 split-L 路径使用 `PRELU_TPL_CHANNEL_SPLIT_L_MODE`，每个 row 内按 `tileLength` 对 L 维分段：

```cpp
static uint64_t AlignUp(uint64_t value, uint64_t align)
{
    return ((value + align - 1U) / align) * align;
}

for (int64_t tileOffset = 0; tileOffset < innerSize; tileOffset += tileLength) {
    int64_t remainLen = innerSize - tileOffset;
    uint32_t realLen = static_cast<uint32_t>(remainLen > tileLength ? tileLength : remainLen);
    uint32_t computeLen = AlignUp(realLen, blockElementNum);
    int64_t gmOffset = rowIdx * innerSize + tileOffset;
    CopyInByOffset(gmOffset, realLen, computeLen);
    Compute(computeLen);
    CopyOutByOffset(gmOffset, realLen);
}
```

当 Host 侧判定 `channelFullL == false` 且 `rowNum < coreNum && totalTaskNum > rowNum` 时，设置 `PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE`，Kernel 每个 task 处理一个 row 的一个 L 分段：

```cpp
int64_t taskIdx = taskOffset + taskProgress;
int64_t rowIdx = taskIdx / tilesPerRow;
int64_t tileIdx = taskIdx % tilesPerRow;
int64_t tileOffset = tileIdx * tileLength;
int64_t remainLen = innerSize - tileOffset;
uint32_t realLen = static_cast<uint32_t>(remainLen > tileLength ? tileLength : remainLen);
uint32_t computeLen = AlignUp(realLen, blockElementNum);
int64_t channelIdx = rowIdx % channelSize;
int64_t gmOffset = rowIdx * innerSize + tileOffset;

LoadChannelWeight(channelIdx);
CopyInByOffset(gmOffset, realLen, computeLen);
Compute(computeLen);
CopyOutByOffset(gmOffset, realLen);
```

`tileLength` 已按 32B 对齐，因此 split-L 中间分段的 `realLen == computeLen == tileLength`；只有最后一个分段可能非 32B 对齐，需要 `DataCopyPad` 补齐到 `computeLen`。无论 full-L 还是 split-L，`CopyOut(realLen)` 都只写回真实数据，padding 区结果不写回 GM。如需便于调试或减少未初始化 UB 数据参与计算，可选择在 CopyIn 前清零 `xLocal[0:computeLen]` 区间：

```cpp
Duplicate(xLocal, static_cast<T>(0), computeLen); // 可选
DataCopyExtParams copyParams{1, static_cast<uint32_t>(realLen * sizeof(T)), 0, 0, 0};
DataCopyPadExtParams<T> padParams{/* 按实际 API 配置 */};
DataCopyPad(xLocal, xGm[gmOffset], copyParams, padParams);
```

### 3.6 UB 分配表

**float32：**

| Buffer | 数量 | 单元素字节 | 总系数 |
|--------|------|------------|--------|
| inputQueueX | 2 | 4 | 8 |
| outputQueueY | 2 | 4 | 8 |
| tmpBufPos | 1 | 4 | 4 |
| tmpBufNeg | 1 | 4 | 4 |
| **合计** | - | - | **24** |

**float16：**

| Buffer | 数量 | 单元素字节 | 总系数 |
|--------|------|------------|--------|
| inputQueueX | 2 | 2 | 4 |
| outputQueueY | 2 | 2 | 4 |
| tmpBufPos | 1 | 2 | 2 |
| tmpBufNeg | 1 | 2 | 2 |
| **合计** | - | - | **12** |

**bfloat16：**

| Buffer | 数量 | 单元素字节 | 总系数 |
|--------|------|------------|--------|
| inputQueueX | 2 | 2 | 4 |
| outputQueueY | 2 | 2 | 4 |
| tmpXFp32 | 1 | 4 | 4 |
| tmpBufPos | 1 | 4 | 4 |
| tmpBufNeg | 1 | 4 | 4 |
| **合计** | - | - | **20** |

---

## 4. Workspace 需求

当前 `prelu_chanel` tiling 设置：

```cpp
constexpr uint32_t WS_SYS_SIZE = 0U;
currentWorkspace[0] = WS_SYS_SIZE;
```

因此本算子不申请额外 workspace。

---

## 5. Kernel 执行流程

### 5.1 Kernel 入口与 tilingKey 分发

Kernel 入口使用 tilingKey 中的 `schMode` 做编译期路径选择。`weightMode` 不再作为 Kernel 主执行路径的运行时分支条件。

推荐实现：

```cpp
template <uint32_t schMode>
__global__ __aicore__ void prelu(GM_ADDR x, GM_ADDR weight, GM_ADDR y, GM_ADDR workspace, GM_ADDR tiling)
{
    REGISTER_TILING_DEFAULT(PreluTilingData);
    GET_TILING_DATA_WITH_STRUCT(PreluTilingData, tilingData, tiling);

    if constexpr (schMode == PRELU_TPL_SCALAR_MODE) {
        AscendC::TPipe pipe;
        NsPrelu::Prelu<DTYPE_X> op;
        op.InitScalar(x, weight, y, &tilingData, &pipe);
        op.ProcessScalar();
    } else if constexpr (schMode == PRELU_TPL_CHANNEL_FULL_L_MODE) {
        AscendC::TPipe pipe;
        NsPrelu::Prelu<DTYPE_X> op;
        op.InitChannel(x, weight, y, &tilingData, &pipe);
        op.ProcessChannelFullL();
    } else if constexpr (schMode == PRELU_TPL_CHANNEL_SPLIT_L_MODE) {
        AscendC::TPipe pipe;
        NsPrelu::Prelu<DTYPE_X> op;
        op.InitChannel(x, weight, y, &tilingData, &pipe);
        op.ProcessChannelSplitL();
    } else if constexpr (schMode == PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE) {
        AscendC::TPipe pipe;
        NsPrelu::Prelu<DTYPE_X> op;
        op.InitChannelSplitLParallel(x, weight, y, &tilingData, &pipe);
        op.ProcessChannelSplitLParallel();
    }
}
```

如果实现复杂度继续增加，也可以拆成两个类：

```cpp
if constexpr (schMode == PRELU_TPL_SCALAR_MODE) {
    NsPrelu::PreluScalar<DTYPE_X> op;
    op.Init(...);
    op.Process();
} else if constexpr (schMode == PRELU_TPL_CHANNEL_FULL_L_MODE ||
                     schMode == PRELU_TPL_CHANNEL_SPLIT_L_MODE ||
                     schMode == PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE) {
    NsPrelu::PreluChannel<DTYPE_X> op;
    op.Init(...);
    op.Process();
}
```

当前阶段可先保留一个 `Prelu<T>` 类，但必须暴露 `InitScalar()/ProcessScalar()`、`InitChannel()/ProcessChannelFullL()`、`InitChannel()/ProcessChannelSplitL()` 和 `InitChannelSplitLParallel()/ProcessChannelSplitLParallel()`，由 `schMode` 编译期分发调用。这样 Init 和 Process 都不会再依赖运行时 `weightMode` 选择主路径。

### 5.2 Init

`Init` 拆成 `InitScalar` 和 `InitChannel`，由 Kernel 入口根据 tilingKey 编译期选择。

`InitScalar`：

1. 根据 `formerNum/formerLength/tailLength` 计算当前 core 的 `blockLength` 和 GM offset。
2. 设置 `ubLength = tilingData->tileLength`。
3. 绑定当前 core 范围内的 `inputGMX`、`outputGMY`。
4. 从 GM 读取一次 `weight[0]`。
5. 初始化 input/output queue 和临时 buffer。

`InitChannel`：

1. 根据 `baseRows/extraRows` 计算当前 core 的 `rowOffset/blockRowNum`。
2. 设置 `ubLength = tilingData->tileLength`、`innerSize`、`innerSizeAligned`、`channelSize`。
3. 绑定完整 `inputGMX`、`outputGMY`，并保存 `weight` GM 指针。
4. 初始化 input/output queue 和临时 buffer。

`InitChannelSplitLParallel`：

1. 根据 `baseTasks/extraTasks` 计算当前 core 的 `taskOffset/taskNum`。
2. 设置 `ubLength = tilingData->tileLength`、`innerSize`、`tilesPerRow`、`channelSize`。
3. 绑定完整 `inputGMX`、`outputGMY`，并保存 `weight` GM 指针。
4. 初始化 input/output queue 和临时 buffer。

channel 控制流不得以 scalar flat tiling 的 `blockLength` 作为循环边界；scalar 控制流也不得读取 channel 专用字段。

### 5.3 Process

#### scalar weight `[1]`

```cpp
int64_t tileNum = (blockLength + ubLength - 1) / ubLength;
for (int64_t i = 0; i < tileNum; ++i) {
    uint32_t currentNum = static_cast<uint32_t>(
        (i == tileNum - 1) ? (blockLength - i * ubLength) : ubLength);
    CopyIn(i, currentNum);
    Compute(currentNum);
    CopyOut(i, currentNum);
}
```

#### channel weight `[C]` full-L

channel 路径一次处理一个完整 L 段。`realLen = innerSize` 是真实搬运长度，`computeLen = innerSizeAligned` 是 32B 对齐后的计算长度：

```cpp
for (int64_t rowProgress = 0; rowProgress < blockRowNum; ++rowProgress) {
    int64_t rowIdx = rowOffset + rowProgress;
    int64_t channelIdx = rowIdx % channelSize;
    int64_t gmOffset = rowIdx * innerSize;
    uint32_t realLen = static_cast<uint32_t>(innerSize);
    uint32_t computeLen = static_cast<uint32_t>(innerSizeAligned);

    LoadChannelWeight(channelIdx);
    CopyInByOffset(gmOffset, realLen, computeLen); // DataCopyPad，padding 区不写回 GM
    Compute(computeLen);               // Maxs + Mins + Muls + Add
    CopyOutByOffset(gmOffset, realLen); // DataCopyPad，只写回真实 L
}
```

`LoadChannelWeight` 只读取当前 row 对应的 `weight[c]`，然后 `Compute(computeLen)` 复用 scalar 路径中的 `Muls(neg, neg, weightVal, computeLen)`。padding 区不会写回 GM，因此不影响最终输出。

#### channel weight `[C]` split-L

split-L 路径用于 `L` 超过 UB 可处理长度的场景。核间仍按 row 切分，每个 row 内再按 `tileLength` 分段处理：

```cpp
static uint32_t AlignUp(uint32_t value, uint32_t align)
{
    return ((value + align - 1U) / align) * align;
}

for (int64_t rowProgress = 0; rowProgress < blockRowNum; ++rowProgress) {
    int64_t rowIdx = rowOffset + rowProgress;
    int64_t channelIdx = rowIdx % channelSize;
    LoadChannelWeight(channelIdx);

    for (int64_t tileOffset = 0; tileOffset < innerSize; tileOffset += ubLength) {
        int64_t remainLen = innerSize - tileOffset;
        uint32_t realLen = static_cast<uint32_t>(remainLen > ubLength ? ubLength : remainLen);
        uint32_t computeLen = AlignUp(realLen, 32 / sizeof(T));
        int64_t gmOffset = rowIdx * innerSize + tileOffset;

        CopyInByOffset(gmOffset, realLen, computeLen);
        Compute(computeLen);
        CopyOutByOffset(gmOffset, realLen);
    }
}
```

#### channel weight `[C]` split-L parallel

split-L parallel 路径用于 `L` 超过 UB 可处理长度，且 `rowNum=N*C` 小于 core 数、task 级切分能增加可用 core 数的场景。核间按 task 切分，每个 task 对应一个 `(rowIdx, tileIdx)`：

```cpp
for (int64_t taskProgress = 0; taskProgress < taskNum; ++taskProgress) {
    int64_t taskIdx = taskOffset + taskProgress;
    int64_t rowIdx = taskIdx / tilesPerRow;
    int64_t tileIdx = taskIdx % tilesPerRow;
    int64_t tileOffset = tileIdx * ubLength;
    int64_t remainLen = innerSize - tileOffset;
    uint32_t realLen = static_cast<uint32_t>(remainLen > ubLength ? ubLength : remainLen);
    uint32_t computeLen = AlignUp(realLen, 32 / sizeof(T));
    int64_t channelIdx = rowIdx % channelSize;
    int64_t gmOffset = rowIdx * innerSize + tileOffset;

    LoadChannelWeight(channelIdx);
    CopyInByOffset(gmOffset, realLen, computeLen);
    Compute(computeLen);
    CopyOutByOffset(gmOffset, realLen);
}
```

该路径允许不同 core 处理同一个 row 的不同 `L` 分段。由于各 task 写回的 GM 区间互不重叠，不需要同步或 workspace。每个 task 都会读取一次当前 `channelIdx` 对应的 weight；这是为了换取更高的核间并行度，适合 `N*C` 很小、`L` 很大的场景。

中间 tile 因为 `ubLength` 已 32B 对齐，`realLen == computeLen == ubLength`；最后一个 tile 通过 `DataCopyPad` 处理非对齐尾部。普通 split-L 路径每个 row 只需读取一次 `weight[c]`，row 内所有 L 分段复用该 scalar；split-L parallel 路径按 task 并行，同一 row 的不同 L 分段可能落到不同 core，因此每个 task 单独读取当前 `weight[c]`。

### 5.4 CopyIn/CopyOut

当前 `prelu_chanel` 已封装 `DataCopyPad`，scalar 和 channel 路径都建议复用同一个四参搬运接口。scalar 路径不需要额外 padding 时，`alignedLen` 传入 `currentNum`：

```cpp
CopyGmToLocalPad(xLocal, inputGMX[progress * ubLength], currentNum, currentNum);
CopyLocalToGmPad(outputGMY[progress * ubLength], yLocal, currentNum);
```

channel 路径需要支持按 GM offset 读写完整 L 段或 L 分段。建议 `CopyInByOffset` 显式传入 `computeLen`，不要在函数内部固定使用 `innerSizeAligned`：

```cpp
CopyGmToLocalPad(xLocal, inputGMX[gmOffset], realLen, computeLen);
CopyLocalToGmPad(outputGMY[gmOffset], yLocal, realLen);
```

实现约束：

- `inputQueueX/outputQueueY/tmpBuf*` 仍按 `tileLength` 初始化，不能按 `realLen` 初始化。
- channel full-L 路径必须保证 `computeLen = innerSizeAligned <= tileLength`；普通 split-L 和 split-L parallel 路径都必须保证每个分段的 `computeLen <= tileLength`。
- padding 区结果不写回 GM，因此不要求 padding value 必须为 0；可选清零 `xLocal[0:computeLen]` 以便调试和降低未初始化 UB 数据参与计算的风险。

---

## 6. 性能与约束

### 6.1 性能特征

- 算子为逐元素 memory-bound。
- scalar 路径每个 core 在 Init 阶段读取一次 `weight[0]`，计算阶段使用 `Muls`。
- channel full-L 路径每个 row 读取一次 `weight[c]`，一个完整 L 段执行一次 `Maxs + Mins + Muls + Add`。
- channel split-L 路径每个 row 读取一次 `weight[c]`，row 内每个 L tile 执行一次 `Maxs + Mins + Muls + Add`。
- channel split-L parallel 路径每个 task 读取一次 `weight[c]`，允许同一 row 的不同 L tile 分配到不同 core，提高 `N*C` 较小、`L` 很大场景的核间并行度。
- input/output 使用 double buffer queue。
- bfloat16 路径升精度到 float32 计算；float16 路径按当前实现直接用 float16 计算。

### 6.2 当前限制

- 支持 scalar weight `[1]`。
- 支持 channel weight `[C]` 时 rank >= 2 的输入，固定第 0 维为 N、第 1 维为 C，后续维度乘积为 L。
- channel 路径支持 full-L、普通 split-L 和 split-L parallel：当 `AlignUp(L, 32 / sizeof(T)) <= tileLength` 时一次处理完整 L；否则根据 `rowNum` 与 task 数选择 row 内分段或 task 级并行分段。
- L 不要求 32B 对齐；输入和输出按真实长度使用 `DataCopyPad` 搬运，计算按每段对齐后的 `computeLen` 执行。
- 不支持按非第 1 维做 channel broadcast。
- bfloat16 weight 标量读取使用 `LoadBf16ScalarAsFloat` 做位转换，避免依赖部分 CANN 版本不支持的 `AscendC::Cast(bfloat16_t)` 标量重载。

---

## 7. 实现检查清单

### 7.1 Host 侧

- [x] 注册输入 `x/weight` 和输出 `y`，dtype 支持 float16/float32/bfloat16。
- [x] InferShape 设置 `y.shape = x.shape`。
- [ ] 校验 `weight` shape 为 `[1]` 或 `[C]`。
- [x] 校验 `x/weight/y` dtype 一致。
- [x] 校验 `x/y` shape 一致。
- [ ] `weight` 为 `[C]` 时校验 `x` rank >= 2，且 `weightSize == x.shape[1]`。
- [ ] `weight` 为 `[C]` 时计算 `N=x.shape[0]`、`C=x.shape[1]`、`L=prod(x.shape[2:])`，rank 为 2 时 `L=1`。
- [ ] `weight` 为 `[C]` 时安全计算 `innerSize=L`、`rowNum=N*C`、`innerSizeAligned=AlignUp(L, 32 / sizeof(T))`，并做正数和 `int64_t` 溢出保护。
- [ ] `weight` 为 `[C]` 时不因 `innerSizeAligned > tileLength` 失败；该场景应继续在 `PRELU_TPL_CHANNEL_SPLIT_L_MODE` 与 `PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE` 中选择。
- [x] workspace size 为 0。
- [ ] tiling data 新增并写入 `channelSize/innerSize/innerSizeAligned/baseRows/extraRows/tilesPerRow/baseTasks/extraTasks`；`weightSize/weightMode/rowNum/totalTaskNum` 仅作为 Host 侧局部变量使用。
- [ ] `weightMode=1` 且 `innerSizeAligned > tileLength` 时使用 `uint64_t` 中间变量计算 `tilesPerRow/totalTaskNum`，写入 `tilesPerRow/baseTasks/extraTasks` 前检查相关值不超过 `int64_t::max()`。
- [ ] `weightMode=0` 时设置 `PRELU_TPL_SCALAR_MODE` tilingKey；`weightMode=1` 且 full-L 条件满足时设置 `PRELU_TPL_CHANNEL_FULL_L_MODE`；Host 判定 `useSplitLParallel` 为 true 时设置 `PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE`；否则设置 `PRELU_TPL_CHANNEL_SPLIT_L_MODE`。
- [ ] split-L parallel 路径使用 `usedCoreNum = min(coreNum, totalTaskNum)`，普通 channel row 路径使用 `usedCoreNum = min(coreNum, rowNum)`，`SetBlockDim` 必须使用当前路径对应的 `usedCoreNum`。
- [ ] scalar/channel 的 tiling 字段分支清晰，Host 不依赖未使用字段的值。

### 7.2 Kernel 侧

- [ ] `prelu_tiling_key.h` 定义 `PRELU_TPL_SCALAR_MODE`、`PRELU_TPL_CHANNEL_FULL_L_MODE`、`PRELU_TPL_CHANNEL_SPLIT_L_MODE` 和 `PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE`，不再使用语义模糊的 `PRELU_TPL_SCH_MODE_0/1`。
- [ ] Kernel 入口根据 `schMode` 使用 `if constexpr` 编译期分发到 `InitScalar/ProcessScalar`、`InitChannel/ProcessChannelFullL`、`InitChannel/ProcessChannelSplitL` 或 `InitChannelSplitLParallel/ProcessChannelSplitLParallel`，不能用运行时 `if (weightMode)` 作为主执行路径选择。
- [x] 根据 blockIdx 计算当前 core 的 GM offset 和 blockLength。
- [x] Init 阶段读取 scalar weight。
- [ ] channel 路径根据 `baseRows/extraRows` 和 blockIdx 计算 `rowOffset/blockRowNum`。
- [ ] split-L parallel 路径根据 `baseTasks/extraTasks` 和 blockIdx 计算 `taskOffset/taskNum`。
- [ ] channel 路径每次循环读取一个 `weight[c]`。
- [ ] channel full-L 路径每次 `CopyIn/Compute/CopyOut` 处理一个完整 L 段：CopyIn/CopyOut 使用真实 L，Compute 使用 `innerSizeAligned`。
- [ ] channel split-L 路径 row 内按 `tileLength` 分段，每个分段独立计算 `realLen/computeLen/gmOffset`。
- [ ] channel split-L parallel 路径按 task 解码 `rowIdx/tileIdx/tileOffset`，每个 task 独立计算 `realLen/computeLen/gmOffset`。
- [ ] channel row 路径只以 `rowOffset/blockRowNum/innerSize/innerSizeAligned/tileLength` 作为循环与搬运依据；split-L parallel 路径只以 `taskOffset/taskNum/tilesPerRow/innerSize/tileLength` 作为循环与搬运依据；`formerLength/tailLength/blockLength` 不能参与 channel 分配或循环边界。
- [ ] queue 和临时 buffer 按 `tileLength` 初始化，不能按 `realLen` 初始化。
- [ ] 保证 full-L 的 `innerSizeAligned <= tileLength`，split-L 每段 `computeLen <= tileLength`，padding 区位于已分配 UB 内；是否将 padding 区清零为可选实现策略。
- [x] input/output queue 使用 `BUFFER_NUM=2`。
- [x] float16/float32 使用 `Maxs + Mins + Muls + Add`。
- [x] bfloat16 使用 `Cast -> Maxs/Mins/Muls/Add -> Cast`。
- [x] 最后一个 tile 使用 `currentNum = blockLength - i * ubLength`。
- [x] CopyIn/CopyOut 使用 `DataCopyPad` 封装，支持非 32B 对齐尾块。

### 7.3 测试建议

- scalar weight shape `[1]`，覆盖 float16、float32、bfloat16。
- channel weight shape `[C]`，覆盖 x shape `[N, C]`、`[N, C, L]`、`[N, C, H, W]` 和更高 rank。
- Host tiling UT 需要校验 scalar case 返回 `PRELU_TPL_SCALAR_MODE`，channel 小 L case 返回 `PRELU_TPL_CHANNEL_FULL_L_MODE`，channel 大 L 且 `rowNum >= coreNum` case 返回 `PRELU_TPL_CHANNEL_SPLIT_L_MODE`，channel 大 L 且 `rowNum < coreNum && totalTaskNum > rowNum` case 返回 `PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE`。
- Kernel UT 中 scalar/full-L/split-L/split-L parallel case 分别使用对应 `ICPU_SET_TILING_KEY` 和模板实例。
- channel 路径覆盖 `N > 1`、`C > 1`、不同 `L=prod(x.shape[2:])`，并验证每个 channel 使用对应 `weight[c]`。
- x shape 覆盖 scalar 路径的 1D、2D、4D 和非 32B 对齐尾块。
- 数值覆盖正数、负数、0。
- 非法用例：`weight` shape 非 `[1]` 或 `[C]`、`weightSize != x.shape[1]`、channel 路径 rank < 2、dtype 不一致、输出 shape 与输入不一致。

---

## 8. 参考文件

- `/Users/hc/ascendc/prelu_chanel/op_host/prelu_def.cpp`
- `/Users/hc/ascendc/prelu_chanel/op_host/prelu_infershape.cpp`
- `/Users/hc/ascendc/prelu_chanel/op_host/prelu_tiling.cpp`
- `/Users/hc/ascendc/prelu_chanel/op_kernel/prelu.h`
- `/Users/hc/ascendc/prelu_chanel/op_kernel/prelu_tiling_data.h`
