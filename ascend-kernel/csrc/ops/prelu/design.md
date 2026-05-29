# PReLU Scalar/Channel 算子设计文档

本文档根据 `/Users/hc/ascendc/prelu_chanel` 当前实现维护，用于说明 scalar、channel、NC weight reuse、small/medium-L split-C weight reuse 等路径的设计语义。

## 1. 算子接口

```cpp
Prelu(x, weight) -> y
```

| 参数名 | 类型 | 输入/输出 | 支持类型 | 约束 |
|--------|------|-----------|----------|------|
| x | Tensor | 输入 | float16/float32/bfloat16 | ND，AutoContiguous |
| weight | Tensor | 输入 | float16/float32/bfloat16 | 1-D，shape 为 `[1]` 或 `[C]` |
| y | Tensor | 输出 | float16/float32/bfloat16 | shape 与 x 一致 |

`x`、`weight`、`y` 的 dtype 必须一致。

### Shape 语义

- `weightSize == 1`：scalar 模式，所有元素共用 `weight[0]`。
- `weightSize != 1`：channel 模式，要求 `x` rank >= 2，且 `weightSize == x.shape[1]`。
- channel 模式按 `[N, C, L]` 解释 contiguous 输入：
  - `N = x.shape[0]`
  - `C = x.shape[1]`
  - `L = prod(x.shape[2:])`
  - rank 为 2 时 `L = 1`

计算公式：

```text
scalar:  y[i]       = x[i]       >= 0 ? x[i]       : x[i]       * weight[0]
channel: y[n, c, l] = x[n, c, l] >= 0 ? x[n, c, l] : x[n, c, l] * weight[c]
```

等价 vector 形式：

```text
y = max(x, 0) + alpha * min(x, 0)
```

## 2. TilingData 与 TilingKey

`PreluTilingData` 字段：

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

TilingKey：

| key | 模式 | 触发条件 | 说明 |
|-----|------|----------|------|
| 0 | scalar | `weightSize == 1` | flat elementwise |
| 1 | channel full-L | channel，且每个 `(n,c)` row 的 L 可放入 UB | 每个 row 一次处理完整 L |
| 2 | channel split-L | L 超过 UB，且不适合 task 并行 | row 内按 L 分段 |
| 3 | channel split-L parallel | `N*C` 很小、L 很大 | task 为 `(rowIdx, tileIdx)` |
| 4 | NC weight reuse | `L == 1`，整行 C 可放入 UB | 缓存整条 C 维 weight，按 N row 处理 |
| 5 | NC split-C weight reuse | `L == 1`，整行 C 放不进 UB，但 C 分块可放入 UB | task 为 `(nIdx, cTileIdx)` |
| 6 | NC split-C by-inner weight reuse | `1 < L <= 128`，整行 `C*L` 放不进 UB，但 C 分块可放入 UB | task 为 `(nIdx, cTileIdx)` |
| 7 | NC by-inner weight reuse | `1 < L <= 128`，且整行 `C*L` 可放入 UB | 缓存整条 C 维 weight，按 N row 处理 |

## 3. Host 侧 Tiling 策略

Host 侧获取 AIV 核数和 UB 大小：

```cpp
coreNum = min(GetCoreNumAiv(), 40);
usableUbSize = ubSize > 1024 ? ubSize - 1024 : ubSize;
```

基础 UB 系数：

| dtype | 普通路径 bytes/element | weight reuse bytes/element |
|-------|-------------------------|-----------------------------|
| float32 | 24 | 28 |
| float16 | 12 | 14 |
| bfloat16 | 20 | 24 |

### Scalar

Scalar 模式按 flat 元素切分，core 起始尽量 512B 对齐：

```cpp
coreAlignElementNum = 512 / sizeof(T);
blockFactor = AlignUp(CeilDiv(totalNum, coreLimit), coreAlignElementNum);
usedCoreNum = min(coreLimit, CeilDiv(totalNum, blockFactor));
```

### Channel Full/Split-L

普通 channel 路径按 `(n,c)` row 切分：

```cpp
rowNum = N * C;
usedCoreNum = min(coreLimit, rowNum);
baseRows = rowNum / usedCoreNum;
extraRows = rowNum % usedCoreNum;
innerSizeAligned = AlignUp(L, 32 / sizeof(T));
```

若 `innerSizeAligned <= tileLength`，走 full-L；否则走 split-L。

### NC / Small-L Row Weight Reuse

该路径分成两个 key：

- key4：`L == 1`，且整行 C 可放入 UB
- key7：`L <= 128 && C >= 32`，且整行 `C * L` 可放入 UB

Host 计算：

```cpp
rowElements = C * L;
innerStride = (L == 1) ? 1 : AlignUp(L, 32 / sizeof(T));
alignedRowElements = (L == 1) ? AlignUp(rowElements, 32 / sizeof(T)) : C * innerStride;
alignedChannelSize = AlignUp(C, 32 / sizeof(T));
weightCacheBytes = alignedChannelSize * sizeof(T);
if (dtype == bfloat16) {
    weightCacheBytes += alignedChannelSize * sizeof(float);
}

ncMaxTileElements =
    ((usableUbSize - weightCacheBytes) / weightReuseBytesPerElement / alignedRowElements) *
    alignedRowElements;
```

若 `ncMaxTileElements >= alignedRowElements`，则：

```cpp
tileLength = ncMaxTileElements;
innerSizeAligned = alignedRowElements;
usedCoreNum = min(coreLimit, N);
baseRows = N / usedCoreNum;
extraRows = N % usedCoreNum;
```

该路径避免 full-L 把大 C、小 L 输入拆成大量 `(n,c)` 小 row。

### NC / Small-Medium-L Split-C Weight Reuse

当 `L <= 128 && C >= 32`，但整行 `C * L` 放不进 UB 时，尝试按 C 分块。

`L == 1` 时按元素估算：

```cpp
splitCBytesPerElement = weightCacheBytesPerElement + weightReuseBytesPerElement;
splitCTileLength = AlignDown(usableUbSize / splitCBytesPerElement, 32 / sizeof(T));
```

`L > 1` 时按 channel 估算：

```cpp
splitCBytesPerChannel = weightCacheBytesPerElement + weightReuseBytesPerElement * L;
splitCTileChannels = AlignDown(usableUbSize / splitCBytesPerChannel, 32 / sizeof(T));
alignedSplitCElements = AlignUp(splitCTileChannels * L, 32 / sizeof(T));
cTileNum = CeilDiv(C, splitCTileChannels);
totalTaskNum = N * cTileNum;
usedCoreNum = min(coreLimit, totalTaskNum);
```

为了避免 `[1, C, L]` 这类输入被切成过少 task 导致 AIV 利用率下降，`L > 1` 的 split-C 还要求：

```cpp
usedCoreNum >= min(coreLimit, 10)
```

若 C 分块 task 数不足，则回退到常规 channel full/split 路径，让 `(n,c)` row 维度提供更多并行度。

写入 tiling：

```cpp
tileLength = splitCTileChannels;          // L > 1 时表示每个 C tile 的 channel 数
innerSizeAligned = alignedSplitCElements; // L > 1 时表示每个 C tile 的计算元素数
tilesPerRow = cTileNum;
baseTasks = totalTaskNum / usedCoreNum;
extraTasks = totalTaskNum % usedCoreNum;
```

对 `[1, 2048, 7]`，split-C task 数不足时回退到 channel full-L；对 `[1, 2048, 7, 7]` 和 `[128, 512, 127]`，split-C task 数充足时选择 key6。

## 4. Kernel 端实现

### Scalar / Channel 常规计算

float16/float32 使用原 dtype 计算：

```cpp
Maxs(pos, xLocal, 0, len);
Mins(neg, xLocal, 0, len);
Muls(neg, neg, weightVal, len);
Add(yLocal, pos, neg, len);
```

bfloat16 升精度到 float32：

```cpp
Cast(xFp32, xLocal, CAST_NONE, len);
Maxs(pos, xFp32, 0.0f, len);
Mins(neg, xFp32, 0.0f, len);
Muls(neg, neg, weightValFp32, len);
Add(pos, pos, neg, len);
Cast(yLocal, pos, CAST_RINT, len);
```

### Row Weight Reuse

Init 阶段把 `weight[0:C]` 搬到 UB。key4 的 `L == 1` 路径直接把 cached weight 复制到每个 N row 的 `weightVec`。

key7 的 `L > 1` 路径使用 per-channel stride UB 布局：

```text
GM: [c0 L][c1 L][c2 L]...
UB: [c0 innerStride][c1 innerStride][c2 innerStride]...
```

先构造第一行 `C * innerStride` weight pattern：

```cpp
for (channelIdx = 0; channelIdx < C; ++channelIdx) {
    weightValue = weightLocal[channelIdx];
    FillByDuplicate(weightVec, channelIdx * innerStride, weightValue, innerStride);
}
```

CopyIn/CopyOut 以 channel 为 block，使用 `DataCopyPad` 的 `blockCount` 批量搬运整行，只读写真实 `L`，padding 只留在 UB 内参与计算。然后用 UB 内 `DataCopy` 把第一行 pattern 复制到后续 N row，避免 `tileRows * C * innerStride` 次逐元素 `SetValue`，也避免逐 channel 下发大量小 DMA。key4 和 key7 在 kernel 入口处已拆分，热路径不再按 `innerSize` 做运行时分支。

### Split-C Weight Reuse

每个 task 处理一个 `(nIdx, cTileIdx)`：

```cpp
cTileChannels = (L == 1) ? alignedChannelSize : tileLength;
cOffset = cTileIdx * cTileChannels;
realC = min(cTileChannels, C - cOffset);
realLen = realC * L;
computeLen = AlignUp(realLen, 32 / sizeof(T));
gmOffset = nIdx * C * L + cOffset * L;
```

处理流程：

```cpp
CopyWeightTile(cOffset, realC, AlignUp(realC, 32 / sizeof(T)));
CopyInByOffset(gmOffset, realLen, computeLen);
BuildNcWeightVecByInner(1);
ComputeNc(computeLen);
CopyOutByOffset(gmOffset, realLen);
```

最后一个 C 分块可能不足 `cTileChannels`，用 `DataCopyPad` 补齐计算，CopyOut 只写真实 `realLen`。

key6 在单核内部按 `cTileIdx` 对本核分到的 task 重排执行：先构造当前 C 分块的 `weightVec`，再处理该 C 分块覆盖的多个 `nIdx`。这样 `[128, 512, 127]` 这类 case 不再对每个 `(nIdx, cTileIdx)` 重复展开 weight，核间仍按 `N * cTileNum` task 均衡切分。

## 5. 测试覆盖

Host tiling UT 覆盖：

- scalar：`[7]`
- channel full-L：`[2,3,5]`
- NC row weight reuse：`[64,3]`
- small-L row weight reuse by-inner：`[8,128,4]`
- small-L full-L fallback：`[1,2048,7]`
- medium-L split-C weight reuse：`[1,2048,7,7]`
- NC split-C weight reuse：`[1,70000]`
- channel split-L / split-L parallel：大 L case

Kernel UT 覆盖：

- scalar
- channel full-L
- NC row weight reuse
- small-L row weight reuse
- NC split-C weight reuse
- small-L split-C weight reuse
- split-L / split-L parallel

## 6. 当前限制

- channel broadcast 固定使用第 1 维 C。
- `x/weight/y` dtype 必须一致。
- split-C-with-L 当前只在 `L <= 128 && C >= 32` 范围启用。
- 若 C 分块仍无法放入 UB，则回退到常规 channel full/split 路径。
