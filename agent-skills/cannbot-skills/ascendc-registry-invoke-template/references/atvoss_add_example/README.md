# atvoss_add_example — atvoss 框架算子工程模板

> 基于 Broadcast 模式的 Add 算子，仅适用于 DAV_3510 (Ascend950) 芯片。

## 使用方式

```bash
# 拷贝模板（-L 解引用软链接，得到完整独立工程）
cp -rL atvoss_add_example/ my_operator/

# 重命名文件和代码中的 add_example/AddExample/NsAddExample
# 修改算子逻辑
# 编译
cd my_operator && bash build.sh --soc=ascend950
```

## 与 add_example 的关系

本模板基于 `add_example/` 的共享文件（op_api、tests、examples 等通过软链接复用），仅替换了 atvoss 特有部分：

| 文件 | 说明 |
|------|------|
| `op_kernel/add_example_apt.cpp` | Kernel 入口（BroadcastSch 调度器，使用 DTYPE_X1 宏） |
| `op_kernel/arch35/add_example_dag.h` | DAG 计算图定义（NsAddExample 命名空间） |
| `op_kernel/arch35/add_example_struct.h` | TilingKey + TilingData 定义 |
| `op_host/arch35/add_example_tiling.cpp` | Host Tiling（BroadcastBaseTiling） |
| `CMakeLists.txt` | atvoss 编译配置（C++17、ops_base 链接等） |
| `op_host/CMakeLists.txt` | atvoss 编译/链接选项 |
| `op_kernel/CMakeLists.txt` | 仅 ascend950 + _apt.cpp 入口 |
| `custom_compile_options.ini` | Kernel 编译 include 路径 |

## 开发要点

### 命名空间

DAG 定义使用 `namespace NsAddExample {}`，重命名时需同步修改 namespace 名称。

### DTYPE_X1 / DTYPE_X2 宏

Kernel 入口使用 `DTYPE_X1` 而非硬编码类型。该宏由构建系统根据 `_def.cpp` 中注册的 dtype 列表自动生成，编译 kernel 时注入。

### 多 dtype 支持

当前模板只有一个 DAG 变体（`AddExampleCompute<DTYPE_X1>`）。若算子需要支持多 dtype（如 half 需 Cast 提升精度、混合 dtype 输入等），需要：
1. 在 `_dag.h` 中定义多个 DAG 变体（WithCast、MixDtype 等）
2. 在 `_apt.cpp` 中用 `if constexpr` 按 `DTYPE_X1` 选择 DAG 变体
3. 在 `_tiling.cpp` 中按输入 dtype 选择对应 DAG 实例化 BaseTiling

详见 **ascendc-atvoss-design** skill → `references/multi-dtype.md`

### __aicore__ Mock

`_dag.h` 顶部包含 `__aicore__` 的 Host 编译 mock，这是 standalone 自定义算子工程的必要处理。

## 三模式差异速查

当前模板使用 **Broadcast** 模式。若需改为 Elewise 或 Reduction，4 个核心文件中的差异点已用 `【atvoss 模式差异】` 注释标注。汇总如下：

### DAG 定义 (`_dag.h`)

| 差异点 | Broadcast | Elewise | Reduction |
|--------|-----------|---------|-----------|
| 搬入操作 | `CopyInBrc<T>` | `CopyIn<T>` | `CopyIn<T>` |
| 计算操作 | 二元（Add/Mul...） | 一元/二元（Abs/Exp...） | `ReduceSumOp<T>`... |
| Cast 提升 | 通常不需要 | 按需 | ReduceSum 推荐 |

### Kernel 入口 (`_apt.cpp`)

| 差异点 | Broadcast | Elewise | Reduction |
|--------|-----------|---------|-----------|
| 头文件 | `broadcast_sch.h` | `elewise_sch.h` | `reduce_sch.h` |
| 模板参数 | `<uint64_t schMode>` | `<uint64_t schMode>` | `<REDUCE_TPL_PARAM>` |
| REGISTER_TILING | 不需要 | 需要 | 需要 |
| GET_TILING_DATA | 不需要 | `GET_TILING_DATA` | `GET_TILING_DATA_WITH_STRUCT` |
| TPipe | 不需要 | 需要 | 需要 |
| 调度器 | `BroadcastSch(tiling)` | `ElementwiseSch(&baseTiling, &pipe)` | `ReduceSch(&tilingData)` |
| 调用 | `Process(x1, x2, y)` | `Init + Process` | `Init(含workspace) + Process` |

### TilingData & TilingKey (`_struct.h`)

| 差异点 | Broadcast | Elewise | Reduction |
|--------|-----------|---------|-----------|
| TilingData | 不需要 | **必须 struct 包装** | 不需要（预定义） |
| TilingKey 宏 | `BRC_TEMP_SCH_MODE_KEY_DECL` | `ASCENDC_TPL_UINT_DECL` | `REDUCE_TPL_KEY_DECL` |

### Host Tiling (`_tiling.cpp`)

| 差异点 | Broadcast | Elewise | Reduction |
|--------|-----------|---------|-----------|
| Tiling API | `BroadcastBaseTiling<OpDag>` | `ElewiseBaseTiling` | `Tiling4ReduceOp<OpDag>` |
| DoTiling | `.DoTiling()` | `.DoTiling<OpDag>(baseTiling)` | 函数调用 |
| TilingKey | 1 个参数 | 1 个参数 | 3 个参数 |

## 相关 Skill

- **ascendc-atvoss-design** — 设计阶段：判断适用性、选择模式、多 dtype 策略
- **ascendc-atvoss-devkit** — API 参考：调度器签名、Vec 操作、宏用法
