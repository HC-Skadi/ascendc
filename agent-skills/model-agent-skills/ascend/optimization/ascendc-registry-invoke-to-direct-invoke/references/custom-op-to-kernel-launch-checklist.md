# 自定义算子转 `<<<>>>` kernel 直调检查清单

这个清单用于 **AscendC 自定义算子转 `<<<>>>` kernel 直调改造**。

适用场景：
- 把 `op_kernel/archXX` 或现有算子源树迁到当前目录
- 删除 `..` 相对 include
- 提取最小依赖闭包
- 判断当前结果是否只是“kernel 本地化完成”，还是已经“可直接 launch / 独立编译”

---

## 1. 任务边界先确认

开始前先确认：
- [ ] 这是 **自定义算子转 `<<<>>>` kernel 直调改造**，不是 host / graph / 注册集成
- [ ] 目标目录已明确（当前目录根 / 子目录 / 保留源层级）
- [ ] 是否需要同时处理 `*_apt.cpp` / `*_apt.h`
- [ ] 是否要求“可独立编译 / 可直接 launch”，还是只要求“kernel 本地化”

如果用户要的是 standalone story / cann-samples / `<<<>>>` 直调工程，就继续按本清单推进，不要误退回成纯 kernel 适配。

---

## 2. 源文件盘点

先列出：
- [ ] `archXX/` 下全部 `.h` / `.cpp`
- [ ] 哪个文件是入口（如 `*_apt.cpp`）
- [ ] 哪个文件是真正的依赖汇聚点（常见是 `*_common.h` / `*_regbase_common.h`）
- [ ] 哪些文件已经是从上游模板改造过的“半本地化版本”

判断点：
- [ ] 当前 kernel 是 header-only / inline 风格
- [ ] 依赖实现主要藏在 common / base 头，而不在 `.cpp`

---

## 3. 相对 include 盘点

必须完整列出所有：
- [ ] `#include "../..."`
- [ ] `#include "../../..."`

对每条 include，至少确认：
- [ ] 被哪些目标文件引用
- [ ] 当前目标文件真正用了哪些符号
- [ ] 这些符号的真实定义位置
- [ ] 是否存在“表面来自 A，实际定义在 B”的中转依赖

不要接受“include 了就整包搬”。

---

## 4. 符号分类

把要搬的外部符号分成四类。

### 4.1 平台常量
来自 `platform` 命名空间的常量/函数（如 `GetUbBlockSize`、`GetVRegSize` 等）。

判断：
- [ ] 能否直接改成本地 `constexpr`
- [ ] 是否保留最小 `platform` namespace 子集更清晰

### 4.2 基础常量 / traits
来自 `*_base.h` 或公共头的基础定义（如 buffer 数量常量、对齐/取整工具函数、类型 traits 等）。

判断：
- [ ] 是否只需一小段基础定义
- [ ] 是否错误地打算整包复制 `*_base.h`

### 4.3 common 层工具
来自公共 common/reduce 层头文件的工具函数（如对齐函数、cast 辅助、多级规约函数等）。

判断：
- [ ] 命名空间归属是否真实（最易出现"表面归属≠真实定义"的类别）
- [ ] 迁移后 `using` 是否需要修正

### 4.4 算法 helper / regbase helper
当前算子特有的计算辅助函数（如数据搬运 helper、规约函数、数学工具等）。

判断：
- [ ] 是否只搬当前 kernel 真正使用的函数
- [ ] 是否已补齐它们的直接闭包
- [ ] 是否误把整份上游 `*_common.h` / `*_regbase_common.h` 拖了进来

---

## 5. 收口结构决策

默认优先使用：
- [ ] 保留原 kernel 文件主体
- [ ] 新增一个 local helper 头，如 `xxx_local_deps.h`

检查：
- [ ] helper 头只装外部依赖，不混入当前 kernel 主逻辑
- [ ] 原有 `*_common.h` 仍承担当前算子的本地逻辑
- [ ] 文件职责清晰：主逻辑 / 依赖闭包 / 入口分离

仅在依赖极少时，才考虑把外部内容直接塞回原头。

---

## 6. 命名空间与死引用检查

重点检查：
- [ ] `using` 的符号归属是否真实
- [ ] 是否还保留错误中转归属（例如表面从 `RmsNorm` 引，真实在 `NormCommon`）
- [ ] 是否存在未使用 `using`
- [ ] 是否存在未使用 include
- [ ] 是否存在只为历史遗留保留的空壳依赖

典型死引用模式：
- [ ] `using XXX::SomeHelper` 只声明不使用

---

## 7. 入口文件检查（如果同时处理 `*_apt.cpp` / `*_apt.h`）

必须单独检查：
- [ ] 入口文件最终是保留 `.cpp`，还是改成可被其他代码直接 include 的 `.h`
- [ ] `DTYPE_X1` 是否来自外部环境
- [ ] `GET_TILING_DATA_WITH_STRUCT` 是否来自外部环境
- [ ] `TILING_KEY_IS` 是否来自外部环境
- [ ] tiling struct 是否在当前目录闭环可见
- [ ] 是否需要把单入口按 tiling key 拆成两个独立函数
- [ ] 如果用户要求“加模板参数”，是否只是增加模板形参，而**参数声明仍保持 `GM_ADDR`**
- [ ] 入口头 `*_apt.h` 是否避免了 `using namespace`，并改为 `::AscendC::` / `::AddRmsNorm::` 这类显式限定
- [ ] 头文件化后的 kernel 实现是否已用 `#if defined(__NPU_DEVICE__) ... #endif` 包住
- [ ] `__NPU_DEVICE__` 宏保护应放在入口头，还是放在 `local_deps.h / regbase_common.h / regbase.h / regbase_split_d.h` 这类 kernel 实现头

结论必须二选一写清楚：
- [ ] **kernel 已本地化，但入口仍依赖外部编译环境**
- [ ] **入口也已本地化，可独立编译**

不要混着说。

---

## 8. 静态验证

### 8.1 include 清理
在目标文件集合中搜索：
- [ ] `#include "../`
- [ ] `#include "../../`

目标：无匹配。

### 8.2 错误命名空间引用
搜索所有 `using XXX::symbol` 语句，逐条核实符号的真实定义位置是否和 `using` 声明的命名空间一致。

典型问题模式：`using A::foo` 但 `foo` 的真实定义在命名空间 `B` 中。

若发现归属不一致，必须修正。

### 8.3 本地闭包完整性
确认 kernel 代码中引用的所有非 SDK 符号（函数、常量、traits、类型别名）均能在目标目录本地解析，或来自稳定 SDK 头。

方法：在目标目录中 grep kernel 头文件引用的每个非 SDK 函数/常量，确认都能在本地解析。重点检查：
- [ ] 工具函数（取整、对齐等）
- [ ] 平台常量
- [ ] 类型 traits / cast 辅助
- [ ] 算法 helper / 规约函数

### 8.4 helper 头职责
- [ ] helper 头里只有外部依赖闭包
- [ ] 当前算子特有逻辑仍保留在原 kernel 文件中

---

## 9. 结果汇报模板

完成后至少输出：

### 9.1 目标文件集合
- 落地了哪些 `.h` / `.cpp`

### 9.2 删除的相对 include
- 精确到文件和 include 语句

### 9.3 本地化依赖清单
- 按原来源头文件分组列出搬运符号

### 9.4 helper 头职责
- 为什么新增 helper
- helper 里收了哪些依赖

### 9.5 剩余外部假设
- 哪些宏 / tiling / dtype 仍依赖外部环境

### 9.6 静态验证结论
- 是否已没有 `..` include
- 是否还存在错误命名空间 `using`

---

## 10. 重外部依赖型算子参考判断（以 add_rms_norm arch35 为例）

当算子有多个 `..` 相对 include（类似 add_rms_norm 依赖 rms_norm、norm_common 等上游模块），通常应满足：
- [ ] 保留算子自身的 kernel 实现头（如 `*_regbase.h`、`*_regbase_common.h`、`*_split_d.h` 等）
- [ ] 新增 `xxx_local_deps.h`，集中装外部依赖闭包
- [ ] 删除所有 `..` 相对 include（如 `../inc/platform.h`、`../../other_op/*.h`）
- [ ] 本地化所有被实际使用的外部符号，按 4 类分组：
  - 平台常量
  - 基础常量 / traits
  - common 层工具
  - 算法 helper
- [ ] 明确说明 `*_apt.cpp` / `*_apt.h` 是否仍依赖外部编译环境宏（如 `DTYPE_X1`、`GET_TILING_DATA_WITH_STRUCT`）
- [ ] 如果入口已改造成头文件化封装，明确说明：
  - 是否已按 tilingKey 的划分维度拆成独立入口函数
  - 是否由 tiling struct 直接入参
  - 是否只是新增模板参数但仍保留 `GM_ADDR` 形参声明
  - 入口头里是否去掉了 `using namespace`，改用 `::` 显式限定
  - 是否已用 `#if defined(__NPU_DEVICE__) ... #endif` 包住 kernel 实现

---

## 11. TilingData struct 替换检查

如果把 `BEGIN_TILING_DATA_DEF` 替换成 plain struct：
- [ ] 是否已机械转换为普通 C++ struct（不需要额外加 `#pragma pack`）
- [ ] 字段是否只保留 kernel 实际访问的（对比 kernel 代码中的 `tempTilingGm.xxx` 访问）
- [ ] 字段类型和顺序是否与原始 `TILING_DATA_FIELD_DEF` 一致
- [ ] 是否删除了只有其他 variant（如 grad、quant）使用的字段

---

## 12. 入口函数改造检查

如果把 `*_apt.cpp` 改造成 `<<<>>>` 直调入口：
- [ ] 是否已去掉 `extern "C"`
- [ ] 是否已去掉 `GET_TILING_DATA(xxx, tiling)` 或 `GET_TILING_DATA_WITH_STRUCT(xxx, tiling)`
- [ ] `GM_ADDR tiling` 参数是否改成 `const XxxTilingData tilingData`（by value）
- [ ] `TILING_KEY_IS(N)` 运行时分发是否已按 tilingKey 的实际划分维度拆成独立函数（可能按 dtype、计算模式或其他规则）
- [ ] 如果原始代码有 `KERNEL_TASK_TYPE_DEFAULT`，是否保留了；如果没有，是否没有主动添加
- [ ] workspace 参数如果保留，是否有 `(void)workspace;` 抑制未使用警告
- [ ] `.cpp` 是否改成了 `.h`（头文件化，以便 host `.cpp` include）

---

## 13. Host tiling 提取检查

如果从 `op_host/xxx_tiling.cpp` 提取了 host tiling 逻辑：
- [ ] `gert::TilingContext*` 是否已全部替换为 `PlatformAscendCManager::GetInstance()`
- [ ] `OP_LOGE` / `OP_LOGI` 是否已替换为 `throw` 或 `printf`
- [ ] `ge::DataType` 是否已替换为自定义 enum
- [ ] `IMPL_OP_OPTILING` / `REGISTER_TILING_DATA_CLASS` 是否已删除
- [ ] tiling 计算公式是否逐行保真搬运（特别是对齐/非对齐分支）
- [ ] 是否只提取了当前 variant 需要的路径（如只要 SWIGLU_SINGLE，不要 SWIGLU_GRAD_SINGLE）
- [ ] 返回值是否包含 `blockDim` + `tiling` struct

---

## 14. Host 驱动检查

如果创建了 standalone host 驱动：
- [ ] 数据生成是否自包含（C++ 确定性生成，不依赖 Python）
- [ ] golden 计算是否在 C++ 中用 float 精度完成
- [ ] 是否测试了所有目标 dtype
- [ ] 是否使用 `GM_ADDR` 贯穿 host/launch/kernel
- [ ] `aclrtMalloc` 是否按 `reinterpret_cast<void**>(&devicePtr)` 形式使用
- [ ] kernel launch 是否为 `xxx<<<blockDim, 0, stream>>>(inputDevice, outputDevice, ..., tilingData)`

---

## 15. 原始逻辑 vs 适配改造区分检查

- [ ] 计算逻辑、tiling 数学、数据搬运等原始代码是否保真搬运，未被"顺手优化"
- [ ] 适配改造（入口拆分、宏替换、平台 API 替换）是否与原始逻辑改动分开，不混在一起

---

## 16. 自包含检查

- [ ] 适配结果是否只依赖 CANN SDK + ACL 运行时 + 标准 C++ 库
- [ ] 是否不依赖目标仓库（如 cann-samples）中的其他 sample、公共 utils 或共享头文件
- [ ] story 目录内是否所有需要的代码都已闭环

---

## 17. `-xasc` host/device 双 pass 编译兼容检查

如果 kernel 使用了 `MicroAPI`/`Reg` 编程模型（arch35 regbase 风格）：
- [ ] 所有使用 `MicroAPI::RegTensor`、`MaskReg`、`CastTrait`、`DivSpecificMode` 等的实现头是否已加 `#if !defined(__NPU_HOST__)` 保护
- [ ] `__global__` 入口函数是否使用"body 内 guard"模式（函数签名在 guard 外，实现在 `#if !defined(__NPU_HOST__)` 内）
- [ ] `__global__` 入口是否为非模板函数（避免模板 `<<<>>>` 的 bf16 参数 mangling 问题）
- [ ] CMakeLists.txt 是否添加了 `-D__local_mem__=` 编译选项
- [ ] host 侧数据类型（如 `SampleBFloat16`）是否与 kernel 模板参数（如 `bfloat16_t`）严格分离，不混用

判断是否需要本节检查的快速方法：grep kernel 实现头中是否出现 `MicroAPI::`、`__VEC_SCOPE__`、`RegTensor`。

---

## 一句话验收标准

**目标目录内的 kernel 代码应当做到：相对依赖清零、最小闭包明确、语义不变、自包含可编译、边界说明清楚。**
