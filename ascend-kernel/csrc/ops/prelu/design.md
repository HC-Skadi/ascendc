# PReLU Scalar/Channel 算子设计文档

## 1. 算子接口

### 1.1 函数签名

```cpp
Prelu(x, weight) -> y
```

`prelu_scalar` 当前是 CANN 自定义算子工程，接口由 `op_host/prelu_def.cpp` 注册：

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
- channel weight 首版要求 `AlignUp(L, 32 / sizeof(T)) <= tileLength`，一个 UB 循环一次处理完整 L 长度；非 32B 对齐的尾部由 `DataCopyPad` padding。

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

在 `prelu_scalar` 现有实现基础上扩展 channel weight。计算 API 仍使用 `Maxs + Mins + Muls + Add`，不生成 `weightLocal`，不使用 `Duplicate` 展开 weight。

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
Muls(neg, neg, weightValFp32, currentNum); // channel 路径 currentNum=L
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

channel weight `[C]` 路径在每个 L 段计算前读取一次 `weight[c]`：

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

该方案仍然不需要生成 `weightLocal`，也不需要 `Duplicate` 扩展到 UB。对 rank >= 2 的输入，kernel 将其按 contiguous 逻辑展开为 `[N, C, L]`，一次 `CopyIn/Compute/CopyOut` 处理一个完整 L 段，`Muls` 的标量参数就是当前通道的 `weight[c]`。

### 2.4 实现路径选择

- [x] AscendC Kernel
- [ ] CATLASS 模板库
- [ ] ACLNN 封装

PReLU 是纯逐元素算子，无矩阵乘、归约或跨元素依赖。channel weight 只改变每个 L 段使用的 scalar，不改变 vector 计算主体。

---

## 3. Tiling 策略

### 3.1 Tiling 参数结构体

需要在 `prelu_scalar/op_kernel/prelu_tiling_data.h` 现有字段基础上增加 channel weight 所需的 shape/模式字段。推荐结构如下：

```cpp
struct PreluTilingData {
    int64_t totalLength = 0;    // x 总元素数
    int64_t usedCoreNum = 0;    // 实际使用 AIV 核数

    int64_t formerNum = 0;      // scalar 路径使用；channel 路径可置 0
    int64_t formerLength = 0;   // scalar 路径每核元素数；channel 路径可置 0
    int64_t tailNum = 0;
    int64_t tailLength = 0;     // scalar 路径尾核元素数；channel 路径可置 0
    int64_t tileLength = 0;     // UB 最大可处理元素数；channel 路径要求 innerSizeAligned <= tileLength

    int64_t weightSize = 1;     // 1 或 C
    int64_t weightMode = 0;     // 0=scalar, 1=channel；Host/调试字段，Kernel 不依赖它做主分发
    int64_t channelSize = 1;    // C
    int64_t innerSize = 1;      // L，真实搬运长度
    int64_t innerSizeAligned = 1; // AlignUp(L, 32 / sizeof(T))，真实计算长度
    int64_t rowNum = 0;         // N * C
    int64_t baseRows = 0;       // channel 路径每核基础 row 数
    int64_t extraRows = 0;      // channel 路径前 extraRows 个 core 各多处理 1 个 row
};
```

scalar 路径可继续使用原有 flat element tiling；channel 路径必须按 row 切分，row 的定义是一个连续 `(n, c, :)` L 段。

字段使用约束：

- scalar tilingKey：只使用 `formerNum/formerLength/tailNum/tailLength/tileLength` 做 flat element tiling；channel 字段可保持默认值，kernel 不读取这些字段。
- channel tilingKey：以 `rowOffset/blockRowNum/innerSize/innerSizeAligned` 作为 channel 分支的循环、搬运和计算依据；`formerNum/formerLength/tailNum/tailLength` 可作为兼容字段保留，但不能用于 channel row 分配或循环边界。
- `weightMode` 保留在 tiling data 中，主要用于 Host 侧选择 tilingKey、UT 断言和调试；Kernel 主执行路径必须由 tilingKey 的 `schMode` 编译期分发决定，不能再通过运行时 `if (weightMode)` 选择路径。

### 3.2 TilingKey 设计

当前实现不应固定使用 `PRELU_TPL_SCH_MODE_0`。tilingKey 需要表达执行路径，使 scalar 和 channel 在 Kernel 入口处完成编译期分发。

推荐定义：

```cpp
#define PRELU_TPL_SCALAR_MODE 0
#define PRELU_TPL_CHANNEL_MODE 1

ASCENDC_TPL_ARGS_DECL(
    Prelu,
    ASCENDC_TPL_UINT_DECL(schMode, 1, ASCENDC_TPL_UI_LIST,
        PRELU_TPL_SCALAR_MODE, PRELU_TPL_CHANNEL_MODE));

ASCENDC_TPL_SEL(ASCENDC_TPL_ARGS_SEL(
    ASCENDC_TPL_UINT_SEL(schMode, ASCENDC_TPL_UI_LIST,
        PRELU_TPL_SCALAR_MODE, PRELU_TPL_CHANNEL_MODE)));
```

tilingKey 语义：

| tilingKey | 触发条件 | Kernel 路径 | 读取字段 |
|-----------|----------|-------------|----------|
| `PRELU_TPL_SCALAR_MODE` | `weight` shape 为 `[1]` | scalar flat 路径 | `formerNum/formerLength/tailNum/tailLength/tileLength` |
| `PRELU_TPL_CHANNEL_MODE` | `weight` shape 为 `[C]` 且 `C=x.shape[1]` | channel row 路径 | `channelSize/innerSize/innerSizeAligned/baseRows/extraRows/tileLength` |

后续如果需要支持 `L > tileLength` 的 channel 分段，或 small-L 多 row 合并优化，应新增 tilingKey，例如 `PRELU_TPL_CHANNEL_SPLIT_L_MODE` 或 `PRELU_TPL_CHANNEL_MULTI_ROW_MODE`，不要把多种策略继续塞进同一个 runtime 分支。

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
9. channel 路径要求 `weightSize == C`；设置 `weightMode=1`、`channelSize=C`、`innerSize=L`、`innerSizeAligned=AlignUp(L, 32 / sizeof(T))`、`rowNum=N*C`。
10. 计算 block 级与 UB 级 tiling。
11. 根据 `weightMode` 设置 tilingKey：

```cpp
uint64_t tilingKey = (weightMode == 0)
    ? GET_TPL_TILING_KEY(PRELU_TPL_SCALAR_MODE)
    : GET_TPL_TILING_KEY(PRELU_TPL_CHANNEL_MODE);
context->SetTilingKey(tilingKey);
```

12. `context->SetBlockDim(usedCoreNum)`。

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
tailNum = totalNum > 0 ? 1U : 0U;
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

channel 路径按 row 切分，避免一个 L 段被拆到不同 core 或不同 UB 循环。输入按 contiguous 内存逻辑视为 `[N, C, L]`，其中 `L = prod(x.shape[2:])`；每个 row 对应 `[n, c, 0:L]`，GM 起始偏移为 `rowIdx * innerSize`。

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

channel weight 路径要求 `innerSizeAligned <= tileLength`。`innerSize` 是真实搬运长度，`innerSizeAligned` 是 vector 计算长度：

```cpp
uint64_t blockElementNum = BLOCK_SIZE / typeLength;
uint64_t innerSizeAligned = CeilDiv(static_cast<uint64_t>(innerSize), blockElementNum) * blockElementNum;
OP_CHECK_IF(innerSizeAligned > static_cast<uint64_t>(ubFactor),
    OP_LOGE(context, "Prelu: aligned L must be less than or equal to tileLength for channel weight"),
    return ge::GRAPH_FAILED);
```

`innerSize` 不要求 32B 对齐。`CopyIn/CopyOut` 使用 `DataCopyPad` 按真实 `innerSize` 搬运；`Compute(innerSizeAligned)` 可能读写 UB padding 区，但 `CopyOut(realLen)` 只写回真实 L，因此 padding 区数值不影响最终 GM 输出。正确性硬约束是 padding 区必须位于已分配 UB 范围内，即 `innerSizeAligned <= tileLength`。如需便于调试或减少未初始化 UB 数据参与计算，可选择在 CopyIn 前清零 `xLocal` 的 `innerSizeAligned` 区间：

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

当前 `prelu_scalar` tiling 设置：

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
    } else if constexpr (schMode == PRELU_TPL_CHANNEL_MODE) {
        AscendC::TPipe pipe;
        NsPrelu::Prelu<DTYPE_X> op;
        op.InitChannel(x, weight, y, &tilingData, &pipe);
        op.ProcessChannel();
    }
}
```

如果实现复杂度继续增加，也可以拆成两个类：

```cpp
if constexpr (schMode == PRELU_TPL_SCALAR_MODE) {
    NsPrelu::PreluScalar<DTYPE_X> op;
    op.Init(...);
    op.Process();
} else if constexpr (schMode == PRELU_TPL_CHANNEL_MODE) {
    NsPrelu::PreluChannel<DTYPE_X> op;
    op.Init(...);
    op.Process();
}
```

当前阶段可先保留一个 `Prelu<T>` 类，但必须暴露 `InitScalar()/ProcessScalar()` 和 `InitChannel()/ProcessChannel()`，由 `schMode` 编译期分发调用。这样 Init 和 Process 都不会再依赖运行时 `weightMode` 选择主路径。

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

#### channel weight `[C]`

channel 路径一次处理一个完整 L 段。`realLen = innerSize` 是真实搬运长度，`computeLen = innerSizeAligned` 是 32B 对齐后的计算长度：

```cpp
for (int64_t rowProgress = 0; rowProgress < blockRowNum; ++rowProgress) {
    int64_t rowIdx = rowOffset + rowProgress;
    int64_t channelIdx = rowIdx % channelSize;
    int64_t gmOffset = rowIdx * innerSize;
    uint32_t realLen = static_cast<uint32_t>(innerSize);
    uint32_t computeLen = static_cast<uint32_t>(innerSizeAligned);

    LoadChannelWeight(channelIdx);
    CopyInByOffset(gmOffset, realLen); // DataCopyPad，padding 区不写回 GM
    Compute(computeLen);               // Maxs + Mins + Muls + Add
    CopyOutByOffset(gmOffset, realLen); // DataCopyPad，只写回真实 L
}
```

`LoadChannelWeight` 只读取当前 row 对应的 `weight[c]`，然后 `Compute(computeLen)` 复用 scalar 路径中的 `Muls(neg, neg, weightVal, computeLen)`。padding 区不会写回 GM，因此不影响最终输出。

### 5.4 CopyIn/CopyOut

当前 `prelu_scalar` 已封装 `DataCopyPad`，scalar 和 channel 路径都建议复用该搬运方式：

```cpp
CopyGmToLocalPad(xLocal, inputGMX[progress * ubLength], currentNum);
CopyLocalToGmPad(outputGMY[progress * ubLength], yLocal, currentNum);
```

channel 路径需要支持按 GM offset 读写完整 L 段：

```cpp
CopyGmToLocalPad(xLocal, inputGMX[gmOffset], realLen);
CopyLocalToGmPad(outputGMY[gmOffset], yLocal, realLen);
```

实现约束：

- `inputQueueX/outputQueueY/tmpBuf*` 仍按 `tileLength` 初始化，不能按 `realLen` 初始化。
- channel 路径必须保证 `computeLen = innerSizeAligned <= tileLength`，否则 `Compute(computeLen)` 会越界访问 UB。
- padding 区结果不写回 GM，因此不要求 padding value 必须为 0；可选清零 `xLocal[0:computeLen]` 以便调试和降低未初始化 UB 数据参与计算的风险。

---

## 6. 性能与约束

### 6.1 性能特征

- 算子为逐元素 memory-bound。
- scalar 路径每个 core 在 Init 阶段读取一次 `weight[0]`，计算阶段使用 `Muls`。
- channel 路径每个 L 段读取一次 `weight[c]`，一个 L 段只执行一次 `Maxs + Mins + Muls + Add`。
- input/output 使用 double buffer queue。
- bfloat16 路径升精度到 float32 计算；float16 路径按当前实现直接用 float16 计算。

### 6.2 当前限制

- 支持 scalar weight `[1]`。
- 支持 channel weight `[C]` 时 rank >= 2 的输入，固定第 0 维为 N、第 1 维为 C，后续维度乘积为 L。
- channel 路径首版要求一次处理完整 L：`AlignUp(L, 32 / sizeof(T)) <= tileLength`。
- L 不要求 32B 对齐；输入和输出按真实 L 使用 `DataCopyPad` 搬运，计算按对齐后的 `innerSizeAligned` 执行。
- 不支持按非第 1 维做 channel broadcast。
- `LoadBf16ScalarAsFloat` 当前未被实际调用。

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
- [ ] `weight` 为 `[C]` 时计算 `innerSizeAligned=AlignUp(L, 32 / sizeof(T))`。
- [ ] `weight` 为 `[C]` 时校验 `innerSizeAligned <= tileLength`。
- [x] workspace size 为 0。
- [ ] tiling data 新增并写入 `weightSize/weightMode/channelSize/innerSize/innerSizeAligned/rowNum/baseRows/extraRows`。
- [ ] `weightMode=0` 时设置 `PRELU_TPL_SCALAR_MODE` tilingKey，`weightMode=1` 时设置 `PRELU_TPL_CHANNEL_MODE` tilingKey。
- [ ] scalar/channel 的 tiling 字段分支清晰，Host 不依赖未使用字段的值。

### 7.2 Kernel 侧

- [ ] `prelu_tiling_key.h` 定义 `PRELU_TPL_SCALAR_MODE` 和 `PRELU_TPL_CHANNEL_MODE`，不再使用语义模糊的 `PRELU_TPL_SCH_MODE_0/1`。
- [ ] Kernel 入口根据 `schMode` 使用 `if constexpr` 编译期分发到 `InitScalar/ProcessScalar` 或 `InitChannel/ProcessChannel`，不能用运行时 `if (weightMode)` 作为主执行路径选择。
- [x] 根据 blockIdx 计算当前 core 的 GM offset 和 blockLength。
- [x] Init 阶段读取 scalar weight。
- [ ] channel 路径根据 `baseRows/extraRows` 和 blockIdx 计算 `rowOffset/blockRowNum`。
- [ ] channel 路径每次循环读取一个 `weight[c]`。
- [ ] channel 路径每次 `CopyIn/Compute/CopyOut` 处理一个完整 L 段：CopyIn/CopyOut 使用真实 L，Compute 使用 `innerSizeAligned`。
- [ ] channel 路径只以 `rowOffset/blockRowNum/innerSize/innerSizeAligned` 作为循环与搬运依据；`formerLength/tailLength/blockLength` 不能参与 channel row 分配或循环边界。
- [ ] queue 和临时 buffer 按 `tileLength` 初始化，不能按 `realLen` 初始化。
- [ ] 保证 `innerSizeAligned <= tileLength`，padding 区位于已分配 UB 内；是否将 padding 区清零为可选实现策略。
- [x] input/output queue 使用 `BUFFER_NUM=2`。
- [x] float16/float32 使用 `Maxs + Mins + Muls + Add`。
- [x] bfloat16 使用 `Cast -> Maxs/Mins/Muls/Add -> Cast`。
- [x] 最后一个 tile 使用 `currentNum = blockLength - i * ubLength`。
- [x] CopyIn/CopyOut 使用 `DataCopyPad` 封装，支持非 32B 对齐尾块。

### 7.3 测试建议

- scalar weight shape `[1]`，覆盖 float16、float32、bfloat16。
- channel weight shape `[C]`，覆盖 x shape `[N, C]`、`[N, C, L]`、`[N, C, H, W]` 和更高 rank。
- Host tiling UT 需要校验 scalar case 返回 `PRELU_TPL_SCALAR_MODE`，channel case 返回 `PRELU_TPL_CHANNEL_MODE`。
- Kernel UT 中 scalar case 使用 `ICPU_SET_TILING_KEY(PRELU_TPL_SCALAR_MODE)`，channel case 使用 `ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_MODE)`。
- channel 路径覆盖 `N > 1`、`C > 1`、不同 `L=prod(x.shape[2:])`，并验证每个 channel 使用对应 `weight[c]`。
- x shape 覆盖 scalar 路径的 1D、2D、4D 和非 32B 对齐尾块。
- 数值覆盖正数、负数、0。
- 非法用例：`weight` shape 非 `[1]` 或 `[C]`、`weightSize != x.shape[1]`、channel 路径 rank < 2、`AlignUp(L, 32 / sizeof(T)) > tileLength`、dtype 不一致、输出 shape 与输入不一致。

---

## 8. 参考文件

- `/Users/hc/ascendc/prelu_scalar/op_host/prelu_def.cpp`
- `/Users/hc/ascendc/prelu_scalar/op_host/prelu_infershape.cpp`
- `/Users/hc/ascendc/prelu_scalar/op_host/prelu_tiling.cpp`
- `/Users/hc/ascendc/prelu_scalar/op_kernel/prelu.h`
- `/Users/hc/ascendc/prelu_scalar/op_kernel/prelu_tiling_data.h`
