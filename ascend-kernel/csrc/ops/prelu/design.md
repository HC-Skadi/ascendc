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
- channel weight 首版要求 `L <= tileLength`，一个 UB 循环一次处理完整 L 长度。

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

    int64_t formerNum = 0;      // scalar 路径：使用 formerLength 的核数；channel 路径：使用 formerRowNum 的核数
    int64_t formerLength = 0;   // scalar 路径每核元素数；channel 路径可保留为 formerRowNum * innerSize
    int64_t tailNum = 0;
    int64_t tailLength = 0;     // scalar 路径尾核元素数；channel 路径可保留为 tailRowNum * innerSize
    int64_t tileLength = 0;     // UB 最大可处理元素数；channel 路径要求 innerSize <= tileLength

    int64_t weightSize = 1;     // 1 或 C
    int64_t weightMode = 0;     // 0=scalar, 1=channel
    int64_t channelSize = 1;    // C
    int64_t innerSize = 1;      // L
    int64_t rowNum = 0;         // N * C
    int64_t formerRowNum = 0;   // channel 路径整核处理的 L 段数量
    int64_t tailRowNum = 0;     // channel 路径尾核处理的 L 段数量
};
```

scalar 路径可继续使用原有 flat element tiling；channel 路径必须按 row 切分，row 的定义是一个连续 `(n, c, :)` L 段。

### 3.2 Host 侧校验

Host tiling 按以下顺序执行：

1. 获取平台 `ubSize` 与 AIV `coreNum`。
2. 设置 workspace size 为 0。
3. 校验 `weight` shape 必须为 `[1]` 或 `[C]`。
4. 校验 `x/y` shape 相同。
5. 校验 dtype 为 `DT_FLOAT`、`DT_FLOAT16` 或 `DT_BF16`，且 `x/weight/y` dtype 一致。
6. 计算 `totalLength = inputX->GetOriginShape().GetShapeSize()`。
7. `weightSize == 1` 时设置 `weightMode=0`，沿用 scalar flat tiling。
8. `weightSize != 1` 时要求 `x` rank >= 2，固定 `N=xShape.GetDim(0)`、`C=xShape.GetDim(1)`、`L=prod(xShape.GetDim(i), i>=2)`；rank 为 2 时 `L=1`。
9. channel 路径要求 `weightSize == C`；设置 `weightMode=1`、`channelSize=C`、`innerSize=L`、`rowNum=N*C`。
10. 计算 block 级与 UB 级 tiling。
11. `context->SetBlockDim(usedCoreNum)`，tiling key 固定为 `PRELU_TPL_SCH_MODE_0`。

### 3.3 Block 级 Tiling

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

```cpp
uint64_t rowNum = static_cast<uint64_t>(N * C);
uint64_t coreLimit = static_cast<uint64_t>(coreNum);
uint64_t rowsPerCore = CeilDiv(rowNum, coreLimit);
uint64_t finalCoreNum = rowNum == 0 ? 1U : CeilDiv(rowNum, rowsPerCore);
finalCoreNum = std::min(coreLimit, finalCoreNum);

usedCoreNum = finalCoreNum;
formerRowNum = finalCoreNum > 0 ? rowsPerCore : 0U;
formerNum = finalCoreNum > 0 ? finalCoreNum - 1U : 0U;
tailNum = rowNum > 0 ? 1U : 0U;
tailRowNum = rowNum - formerNum * formerRowNum;

formerLength = formerRowNum * innerSize;
tailLength = tailRowNum * innerSize;
```

Kernel 中每个 core 的 row 偏移与 row 数：

```cpp
int64_t blockIdx = GetBlockIdx();
int64_t rowOffset = blockIdx * tilingData->formerRowNum;
if (blockIdx < tilingData->formerNum) {
    blockRowNum = tilingData->formerRowNum;
} else if (blockIdx < tilingData->usedCoreNum) {
    blockRowNum = tilingData->tailRowNum;
    rowOffset = tilingData->formerNum * tilingData->formerRowNum;
} else {
    blockRowNum = 0;
}
```

### 3.4 UB 级 Tiling

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

channel weight 路径要求：

```cpp
OP_CHECK_IF(innerSize > static_cast<int64_t>(ubFactor),
    OP_LOGE(context, "Prelu: L must be less than or equal to tileLength for channel weight"),
    return ge::GRAPH_FAILED);
```

保持当前普通 `DataCopy` 方案时，还建议要求 `innerSize` 按 32B 对齐：

```cpp
uint64_t blockElementNum = BLOCK_SIZE / typeLength;
OP_CHECK_IF(innerSize % blockElementNum != 0,
    OP_LOGE(context, "Prelu: L must be 32-byte aligned when using DataCopy"),
    return ge::GRAPH_FAILED);
```

如果后续需要支持任意 L，可将 channel 路径的 `CopyIn/CopyOut` 改为 `DataCopyPad`，但本设计先保持 `prelu_scalar` 的普通 `DataCopy` 风格。

### 3.5 UB 分配表

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

### 5.1 Init

1. 根据 `weightMode` 选择 scalar flat 路径或 channel row 路径。
2. scalar 路径根据 `formerNum/formerLength/tailLength` 计算当前 core 的 `blockLength`。
3. channel 路径根据 `formerRowNum/tailRowNum` 计算当前 core 的 `rowOffset/blockRowNum`。
4. 设置 `ubLength = tilingData->tileLength`。
5. 绑定 `inputGMX`、`outputGMY` 和 `inputGMW`。
6. scalar 路径从 GM 读取一次 `weight[0]`；channel 路径保存 `weight` GM 指针，逐 L 段读取 `weight[c]`。
7. 初始化 input/output queue 和临时 buffer。

### 5.2 Process

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

channel 路径一次处理一个完整 L 段，`currentNum` 固定为 `innerSize`：

```cpp
for (int64_t rowProgress = 0; rowProgress < blockRowNum; ++rowProgress) {
    int64_t rowIdx = rowOffset + rowProgress;
    int64_t channelIdx = rowIdx % channelSize;
    int64_t gmOffset = rowIdx * innerSize;
    uint32_t currentNum = static_cast<uint32_t>(innerSize);

    LoadChannelWeight(channelIdx);
    CopyInByOffset(gmOffset, currentNum);
    Compute(currentNum);       // Maxs + Mins + Muls + Add
    CopyOutByOffset(gmOffset, currentNum);
}
```

`LoadChannelWeight` 只读取当前 row 对应的 `weight[c]`，然后 `Compute(currentNum)` 复用 scalar 路径中的 `Muls(neg, neg, weightVal, currentNum)`。

### 5.3 CopyIn/CopyOut

当前实现使用普通 `DataCopy`：

```cpp
DataCopy(xLocal, inputGMX[progress * ubLength], currentNum);
DataCopy(outputGMY[progress * ubLength], yLocal, currentNum);
```

设计文档与当前实现保持一致，不引入 `DataCopyPad`。

channel 路径需要支持按 GM offset 读写完整 L 段：

```cpp
DataCopy(xLocal, inputGMX[gmOffset], innerSize);
DataCopy(outputGMY[gmOffset], yLocal, innerSize);
```

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
- channel 路径首版要求一次处理完整 L：`L <= tileLength`。
- 保持普通 `DataCopy` 时，建议要求 `L * sizeof(T)` 为 32B 对齐；非对齐 L 需要改为 `DataCopyPad`。
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
- [ ] `weight` 为 `[C]` 时校验 `L <= tileLength`。
- [ ] 若保持普通 `DataCopy`，校验 `L * sizeof(T)` 32B 对齐。
- [x] workspace size 为 0。
- [ ] tiling data 新增并写入 `weightSize/weightMode/channelSize/innerSize/rowNum/formerRowNum/tailRowNum`。

### 7.2 Kernel 侧

- [x] 根据 blockIdx 计算当前 core 的 GM offset 和 blockLength。
- [x] Init 阶段读取 scalar weight。
- [ ] channel 路径根据 blockIdx 计算 `rowOffset/blockRowNum`。
- [ ] channel 路径每次循环读取一个 `weight[c]`。
- [ ] channel 路径每次 `CopyIn/Compute/CopyOut` 处理一个完整 L 段。
- [x] input/output queue 使用 `BUFFER_NUM=2`。
- [x] float16/float32 使用 `Maxs + Mins + Muls + Add`。
- [x] bfloat16 使用 `Cast -> Maxs/Mins/Muls/Add -> Cast`。
- [x] 最后一个 tile 使用 `currentNum = blockLength - i * ubLength`。
- [x] CopyIn/CopyOut 使用普通 `DataCopy`，与当前代码一致。

### 7.3 测试建议

- scalar weight shape `[1]`，覆盖 float16、float32、bfloat16。
- channel weight shape `[C]`，覆盖 x shape `[N, C]`、`[N, C, L]`、`[N, C, H, W]` 和更高 rank。
- channel 路径覆盖 `N > 1`、`C > 1`、不同 `L=prod(x.shape[2:])`，并验证每个 channel 使用对应 `weight[c]`。
- x shape 覆盖 scalar 路径的 1D、2D、4D 和非 32B 对齐尾块。
- 数值覆盖正数、负数、0。
- 非法用例：`weight` shape 非 `[1]` 或 `[C]`、`weightSize != x.shape[1]`、channel 路径 rank < 2、`L > tileLength`、dtype 不一致、输出 shape 与输入不一致。

---

## 8. 参考文件

- `/Users/hc/ascendc/prelu_scalar/op_host/prelu_def.cpp`
- `/Users/hc/ascendc/prelu_scalar/op_host/prelu_infershape.cpp`
- `/Users/hc/ascendc/prelu_scalar/op_host/prelu_tiling.cpp`
- `/Users/hc/ascendc/prelu_scalar/op_kernel/prelu.h`
- `/Users/hc/ascendc/prelu_scalar/op_kernel/prelu_tiling_data.h`
