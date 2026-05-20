# PReLU 算子设计文档

## 1. 算子接口

### 1.1 函数签名

```cpp
at::Tensor prelu(
    const at::Tensor &self,
    const at::Tensor &weight
);
```

### 1.2 参数说明

| 参数名 | 类型 | 输入/输出 | 支持的数据类型 | 描述 | 约束条件 |
|--------|------|-----------|----------------|------|----------|
| self | at::Tensor | 输入 | bfloat16/float16/float32 | 输入 tensor | 支持 ND，建议 contiguous；空 tensor 直接返回 empty_like |
| weight | at::Tensor | 输入 | bfloat16/float16/float32 | 负半轴斜率参数 | dtype/device 与 self 一致；PyTorch 语义下 `numel == 1` 或 `self.dim() >= 2 && numel == self.size(1)` |
| output | at::Tensor | 输出 | bfloat16/float16/float32 | 输出 tensor | shape 与 self 一致 |

### 1.3 支持的数据类型

- [x] bfloat16
- [x] float16
- [x] float32

### 1.4 PyTorch 语义对齐

对齐 `torch.prelu(input, weight)`：

```text
y = max(0, x) + weight * min(0, x)
```

- `weight.numel() == 1`：所有元素共用同一个负半轴斜率。
- `weight.numel() == C`：`C == self.size(1)`，按通道广播，通道维固定为 `dim=1`。
- 输入为 1D 时只支持 `weight.numel() == 1`。

本地环境未安装 PyTorch，无法通过 `inspect.signature(torch.prelu)` 直接校验签名；上述签名按 PyTorch 公共接口语义设计。

### 1.5 TBE 参考实现语义

参考 `/Users/hc/Downloads/prelu_tbe.py`：

- dtype 支持 `float16`、`float32`、`bfloat16`，且 `x` 与 `weight` dtype 必须一致。
- TBE 使用 `ELEWISE_WITH_BROADCAST` 分类，先将 `weight` broadcast 到 `x` shape，再执行 PReLU。
- 常见格式包含 `ND/NCHW/NC1HWC0/NDC1HWC0/FRACTAL_NZ`。AscendC 首版默认按 contiguous ND 实现；如果要完全覆盖 5HD/NZ，应在 Host 侧转为等价 contiguous 视图，或扩展 stride/broadcast tiling。
- 新平台计算路径为 `prod = x * weight; y = select(x > 0, x, prod)`；旧平台路径为 `max(x,0) + weight * min(x,0)`。两者数学等价，`select` 路径更少临时 buffer 和 vector 指令。

---

## 2. 计算逻辑

### 2.1 算法描述

PReLU 是逐元素激活算子，正数部分保持原值，负数部分乘以可学习参数 `weight`：

```text
y = x > 0 ? x : x * weight
```

实现分为三类路径：

1. **标量 weight 路径**：`weight.numel()==1`，每个 tile 共用 `weight[0]`。
2. **通道 weight 路径**：输入逻辑视为 `[outerSize, channelSize, innerSize]`，其中 `channelSize = self.size(1)`，`innerSize = prod(self.sizes()[2:])`，每个 `(n, c, *)` 连续片段使用 `weight[c]`。
3. **TBE broadcast 扩展路径**：如需完全复刻 TBE 的 `broadcast_inputs_shape`，Host 侧将 `weight` 规整为与 `self` 等 rank 的 broadcast shape，Kernel 侧通过 `weightStride[]` 计算每个元素的 weight offset。首版建议先实现 PyTorch 语义的标量和通道路径。

### 2.2 AscendC API 调用伪代码

#### 推荐路径：Mul + Compare + Select

```cpp
// xLocal: float32 输入 tile
// alpha: float32 标量，标量路径来自 weight[0]，通道路径来自 weight[channelIdx]
Duplicate(alphaLocal, alpha, len);          // alphaLocal = weight
Mul(prodLocal, xLocal, alphaLocal, len);    // prod = x * weight
Duplicate(zeroLocal, 0.0f, len);
Compare(mask, xLocal, zeroLocal, CMPMODE::GT, len);
Select(yLocal, mask, xLocal, prodLocal, SELMODE::VSEL_TENSOR_TENSOR_MODE, len);
```

#### 兼容路径：Max/Min

```cpp
Duplicate(zeroLocal, 0.0f, len);
Max(posLocal, xLocal, zeroLocal, len);      // pos = max(x, 0)
Min(negLocal, xLocal, zeroLocal, len);      // neg = min(x, 0)
Muls(negLocal, negLocal, alpha, len);       // neg = alpha * neg
Add(yLocal, posLocal, negLocal, len);       // y = pos + neg
```

#### float16/bfloat16 升精度流程

```cpp
// xLocalLow: float16/bfloat16 输入 tile
// yLocalLow: float16/bfloat16 输出 tile
Cast(xLocalFp32, xLocalLow, RoundMode::CAST_NONE, len);

Duplicate(alphaLocal, alphaFp32, len);
Mul(prodLocal, xLocalFp32, alphaLocal, len);
Duplicate(zeroLocal, 0.0f, len);
Compare(mask, xLocalFp32, zeroLocal, CMPMODE::GT, len);
Select(yLocalFp32, mask, xLocalFp32, prodLocal, SELMODE::VSEL_TENSOR_TENSOR_MODE, len);

Cast(yLocalLow, yLocalFp32, RoundMode::CAST_RINT, len);
```

#### 通道 weight 分段处理

```cpp
int64_t tileGlobalOffset = blockOffset + progress * tileLength;
int64_t localOffset = 0;
while (localOffset < curTileLength) {
    int64_t globalOffset = tileGlobalOffset + localOffset;
    int64_t channelIdx = (globalOffset / innerSize) % channelSize;
    int64_t offsetInChannel = globalOffset % innerSize;
    int64_t segmentLength = min(curTileLength - localOffset, innerSize - offsetInChannel);

    float alpha = static_cast<float>(weightGm.GetValue(channelIdx));
    ComputePreluSegment(alpha, localOffset, segmentLength);
    localOffset += segmentLength;
}
```

#### TBE 通用 broadcast offset（扩展）

```cpp
int64_t tmp = globalOffset;
int64_t weightOffset = 0;
for (int i = rank - 1; i >= 0; --i) {
    int64_t idx = tmp % selfShape[i];
    tmp /= selfShape[i];
    weightOffset += (weightShape[i] == 1 ? 0 : idx) * weightStride[i];
}
float alpha = static_cast<float>(weightGm.GetValue(weightOffset));
```

### 2.3 实现路径选择

- [x] AscendC Kernel（纯 vector 实现）
- [ ] CATLASS 模板库（矩阵乘法类）
- [ ] ACLNN 封装（CANN 内置算子）

**选择理由**：PReLU 不涉及矩阵乘法或归约，核心计算是逐元素 `Mul/Compare/Select`。按通道或 broadcast 只影响 `weight` 读取，不改变 vector 算子主体，适合 AscendC Kernel 实现。

---

## 3. Tiling 策略

AscendC 算子采用两级 Tiling 策略：Block 级做核间切分，UB 级做核内切分。

### 3.1 Tiling 参数结构体定义

```cpp
struct PreluTilingData {
    int64_t totalLength;        // self.numel()
    int64_t usedCoreNum;        // 实际使用 AI Core 数

    int64_t formerNum;          // 整核数量
    int64_t formerLength;       // 整核数据长度
    int64_t tailNum;            // 尾核数量，固定为 1
    int64_t tailLength;         // 尾核数据长度

    int64_t tileLength;         // UB 单次处理长度

    int64_t weightNum;          // weight.numel()
    int64_t channelSize;        // self.dim() >= 2 ? self.size(1) : 1
    int64_t innerSize;          // self.dim() >= 2 ? prod(self.sizes()[2:]) : totalLength
    int64_t weightMode;         // 0=scalar, 1=channel, 2=通用broadcast扩展

    int64_t rank;               // 通用broadcast扩展使用，首版可置0
    int64_t selfShape[8];       // 最多记录8维；超过8维Host侧报错或走contiguous展开策略
    int64_t weightShape[8];
    int64_t weightStride[8];
};
```

### 3.2 Block 级 Tiling（核间切分）

**策略要点**：

1. 将 `self` 按 contiguous flat 顺序切分到多个 AI Core。
2. 每个整核的数据量按 512 字节 cache line 对齐。
3. 尾核处理剩余数据，满足 `formerNum * formerLength + tailNum * tailLength == totalLength`。

| 参数 | 计算公式 | 说明 |
|------|----------|------|
| dtypeSize | `self.element_size()` | float16/bfloat16=2，float32=4 |
| cacheLineElements | `512 / dtypeSize` | 按元素数做 cache line 对齐 |
| totalLengthCore | `(totalLength + coreNum - 1) / coreNum` | 每核理论元素数 |
| totalLengthCoreAlign | `ceil(totalLengthCore / cacheLineElements) * cacheLineElements` | 整核元素数 |
| usedCoreNum | `ceil(totalLength / totalLengthCoreAlign)` | 实际核数 |
| formerNum | `usedCoreNum - 1` | 整核数量 |
| tailNum | `1` | 尾核数量 |
| formerLength | `totalLengthCoreAlign` | 整核长度 |
| tailLength | `totalLength - formerNum * formerLength` | 尾核长度 |

**负载均衡验证**：

- `tailLength > 0`
- `formerLength >= tailLength` 或仅使用一个尾核
- `formerNum * formerLength + tailNum * tailLength == totalLength`

### 3.3 UB 级 Tiling（核内切分）

**策略要点**：

1. 使用 double buffer 隐藏 GM 读写延迟。
2. float16/bfloat16 输入必须 Cast 到 float32 后计算，再 Cast 回原 dtype。
3. 通道 weight 路径按 channel segment 拆分当前 tile，避免生成完整 weight tile。
4. `tileLength` 按 32 字节对齐。

#### UB 分配表

**float32 输入（Select 推荐路径）：**

| Buffer 名称 | 大小（字节） | 用途 | 数量 | 总大小 |
|-------------|--------------|------|------|--------|
| inQueueX | `tileLength * 4` | self 输入缓冲 | `BUFFER_NUM=2` | `tileLength * 8` |
| outQueueY | `tileLength * 4` | output 输出缓冲 | `BUFFER_NUM=2` | `tileLength * 8` |
| prodLocal | `tileLength * 4` | `x * weight` 临时缓冲 | 1 | `tileLength * 4` |
| alphaLocal | `tileLength * 4` | weight 广播向量 | 1 | `tileLength * 4` |
| zeroLocal | `tileLength * 4` | 0 常量向量 | 1 | `tileLength * 4` |
| **总计** | - | - | - | **`tileLength * 28`** |

如果使用 `Max/Min` 兼容路径，`alphaLocal` 可省略但需要 `posLocal/negLocal` 两个临时缓冲，总系数仍为 `28`。

**float16/bfloat16 输入（Select 推荐路径）：**

| Buffer 名称 | 大小（字节） | 用途 | 数量 | 总大小 |
|-------------|--------------|------|------|--------|
| inQueueX | `tileLength * 2` | self 输入缓冲 | `BUFFER_NUM=2` | `tileLength * 4` |
| outQueueY | `tileLength * 2` | output 输出缓冲 | `BUFFER_NUM=2` | `tileLength * 4` |
| xLocalFp32 | `tileLength * 4` | self 升精度缓冲，可复用为 output fp32 | 1 | `tileLength * 4` |
| prodLocal | `tileLength * 4` | `x * weight` 临时缓冲 | 1 | `tileLength * 4` |
| alphaLocal | `tileLength * 4` | weight 广播向量 | 1 | `tileLength * 4` |
| zeroLocal | `tileLength * 4` | 0 常量向量 | 1 | `tileLength * 4` |
| **总计** | - | - | - | **`tileLength * 24`** |

#### tileLength 计算

| 数据类型 | bufferCoefficient | maxTileElements（UB_SIZE_LIMIT=192KB 示例） | alignElements | tileLength 示例 |
|----------|-------------------|---------------------------------------------|---------------|----------------|
| float32 | 28 | `196608 / 28 = 7021` | `32 / 4 = 8` | `7016` |
| float16 | 24 | `196608 / 24 = 8192` | `32 / 2 = 16` | `8192` |
| bfloat16 | 24 | `196608 / 24 = 8192` | `32 / 2 = 16` | `8192` |

```cpp
int64_t bufferCoefficient = (dtypeSize == 2) ? 24 : 28;
int64_t maxTileElements = ubSizeLimit / bufferCoefficient;
int64_t alignElements = 32 / dtypeSize;
int64_t tileLength = (maxTileElements / alignElements) * alignElements;
```

#### UB 约束验证

- **float32**：`7016 * 28 = 196448` bytes，小于 192KB 示例限制。
- **float16/bfloat16**：`8192 * 24 = 196608` bytes，等于 192KB 示例限制。
- **对齐要求**：float32 tileLength 是 8 的倍数，float16/bfloat16 tileLength 是 16 的倍数，满足 32 字节对齐。

---

## 4. Workspace 需求

### 4.1 Workspace 大小计算

| 算子类别 | workspace size | 说明 |
|----------|----------------|------|
| elementwise 类 | `SYSTEM_WORKSPACE_SIZE` | 通常为 16MB，用于框架侧 kernel launch 辅助空间 |

- **tiling data size**：`sizeof(PreluTilingData)`
- **额外 workspace**：不需要额外中间结果 workspace。

### 4.2 Workspace 分配示例

```cpp
constexpr int64_t SYSTEM_WORKSPACE_SIZE = 16 * 1024 * 1024;
size_t workspaceSize = SYSTEM_WORKSPACE_SIZE;
auto workspace = at::empty({static_cast<int64_t>(workspaceSize)},
                           at::TensorOptions().dtype(at::kByte).device(self.device()));
```

---

## 5. 性能优化

### 5.1 关键优化点

1. **Select 快路径**：参考 TBE 新平台实现，使用 `Mul + Compare + Select`，减少 `Max/Min/Add` 组合中的中间计算。
2. **Double buffer**：输入和输出 queue 使用 `BUFFER_NUM=2`，隐藏 GM 读写延迟。
3. **标量 weight 快路径**：`weight.numel()==1` 时全 tile 只读取一次 `alpha`。
4. **通道片段复用**：通道 weight 路径按 `(n,c,*)` 连续片段处理，一个 segment 只读取一次 `weight[c]`。
5. **避免 weight 展开**：默认不在 UB 中生成完整 weight tile；仅为了 `Mul` API 使用当前 segment 的 `alphaLocal`。
6. **升精度计算**：float16/bfloat16 使用 float32 计算，减少负半轴乘法误差。

### 5.2 算子特性

- **计算模式**：memory-bound 为主，通道 weight 且 `innerSize` 很小时会增加 scalar weight 读取与循环开销。
- **访存模式**：self/output 顺序访问；weight 标量、按通道小规模随机读取，或 TBE broadcast 扩展下按 stride 访问。
- **并行性**：高，每个元素独立；通道广播不引入跨核依赖。

---

## 6. Kernel 端实现要点

### 6.1 Init 偏移计算

```cpp
int64_t blockIdx = AscendC::GetBlockIdx();
if (blockIdx < formerNum) {
    blockLength = formerLength;
    blockOffset = blockIdx * formerLength;
} else {
    blockLength = tailLength;
    blockOffset = formerNum * formerLength;
}

xGm.SetGlobalBuffer((__gm__ T *)self + blockOffset, blockLength);
yGm.SetGlobalBuffer((__gm__ T *)output + blockOffset, blockLength);
weightGm.SetGlobalBuffer((__gm__ T *)weight, weightNum);
```

### 6.2 执行流程（核内循环）

```cpp
__aicore__ inline void Process() {
    int64_t tileNum = (blockLength + tileLength - 1) / tileLength;
    int64_t tailTileLength = blockLength - (tileNum - 1) * tileLength;

    for (int64_t i = 0; i < tileNum - 1; ++i) {
        CopyIn(i, tileLength);
        Compute(i, tileLength);
        CopyOut(i, tileLength);
    }

    if (tileNum > 0) {
        CopyIn(tileNum - 1, tailTileLength);
        Compute(tileNum - 1, tailTileLength);
        CopyOut(tileNum - 1, tailTileLength);
    }
}
```

### 6.3 FP16/BF16 升精度流程

```cpp
LocalTensor<T> xLocal = inQueueX.DeQue<T>();
LocalTensor<T> yLocal = outQueueY.AllocTensor<T>();
LocalTensor<float> xFp32 = xFp32Buf.Get<float>();

Cast(xFp32, xLocal, RoundMode::CAST_NONE, len);
ComputePreluFp32(xFp32, yFp32OrXReuse, alphaFp32, len);
Cast(yLocal, xFp32, RoundMode::CAST_RINT, len);
```

### 6.4 边界条件

- `self.numel() == 0`：Host 端直接返回 `empty_like(self)`，不启动 kernel。
- PyTorch 语义模式下 `weight.numel() != 1 && weight.numel() != self.size(1)`：Host 端报错。
- `weight.numel() == self.size(1)` 且 `self.dim() < 2`：Host 端报错。
- TBE broadcast 扩展模式下，Host 端按 `broadcast_inputs_shape` 规则计算 `weightShape/weightStride`，无法 broadcast 时报错。
- 非 contiguous 输入：Host 端建议先 `self.contiguous()` 和 `weight.contiguous()`，输出保持原 shape。
- tail tile 的 DataCopy 只访问真实长度；如目标平台要求 32 字节对齐搬运，使用支持 padding/mask 的 DataCopy 形式，禁止读写 GM 越界。

---

## 7. 实现检查清单

### 7.1 文件结构

- [ ] `csrc/ops/prelu/CMakeLists.txt`
- [ ] `csrc/ops/prelu/op_host/prelu.cpp`
- [ ] `csrc/ops/prelu/op_kernel/kernel_prelu.cpp`
- [ ] `csrc/ops.h` 添加 `prelu` 声明
- [ ] `csrc/register.cpp` 添加 `prelu` 注册

### 7.2 Host 端实现

- [ ] 校验 self/weight dtype 为 bfloat16、float16 或 float32，且 dtype/device 一致。
- [ ] 校验 weight 语义与 PyTorch `torch.prelu` 对齐。
- [ ] 计算 `totalLength/channelSize/innerSize/weightMode`。
- [ ] 如启用 TBE broadcast 扩展，计算规整后的 `weightShape/weightStride` 和 `weightMode=2`。
- [ ] 获取 `coreNum/ubSizeLimit` 并计算 Block 级 tiling。
- [ ] 根据 dtype 选择 `bufferCoefficient`：float32=28，float16/bfloat16=24。
- [ ] 计算 32 字节对齐的 `tileLength`。
- [ ] 分配 `SYSTEM_WORKSPACE_SIZE` workspace 并调用 kernel。

### 7.3 Kernel 端实现

- [ ] 实现 `Init`，设置 self/output/weight GM buffer 和 `blockOffset`。
- [ ] 实现 `CopyIn`，按 tile 从 GM 读取 self。
- [ ] 实现 `ComputeScalarWeight` 快路径。
- [ ] 实现 `ComputeChannelWeight` 分段路径。
- [ ] 可选实现 `ComputeBroadcastWeight`，按 TBE broadcast shape 计算 weight offset。
- [ ] 优先使用 `Mul + Compare + Select`；如目标 AscendC API 不支持对应 Select 模式，则退回 `Max + Min + Muls + Add`。
- [ ] float16/bfloat16 路径先 Cast 到 float32，计算后 Cast 回原 dtype。
- [ ] 实现 `CopyOut`，按 tile 写回 output。
- [ ] 处理最后一个 tile 的对齐 DataCopy 与真实计算长度。

### 7.4 测试验证

- [ ] 标量 weight：`self` 为 1D/2D/4D，覆盖正数、负数、0。
- [ ] 通道 weight：`self` 为 `[N, C]`、`[N, C, H, W]`，`weight.numel()==C`。
- [ ] dtype：bfloat16、float16、float32。
- [ ] 边界：空 tensor、非 contiguous 输入、`weight.numel()` 非法、`self.dim()<2 && weight.numel()!=1`。
- [ ] TBE 参考场景：标量 weight、NCHW 按 C 广播、`weight` 可 broadcast 到 `self` 的 ND 形态。
- [ ] 正确性：与 `torch.prelu(self, weight)` 或 TBE 参考公式对比，float32 使用严格误差，float16/bfloat16 使用合理 `rtol/atol`。
- [ ] 性能：比较标量 weight 与通道 weight，重点观察 `innerSize == 1` 和大 `innerSize` 场景。

---

## 8. 参考实现

- **TBE 参考**：`/Users/hc/Downloads/prelu_tbe.py`，重点参考 `broadcast_inputs_shape` 和 `prelu_compute`。
- **PyTorch 参考**：`torch.prelu(input, weight)`。
- **设计参考**：`templates/design-template.md`、`references/elementwise-tiling.md`、`references/general-tiling-principles.md`。
