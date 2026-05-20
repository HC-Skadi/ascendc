# CSV 格式重构功能

> ⚠️ 仅适用于 **ops-transformer** 算子仓

本目录包含 Host UT CSV 格式重构的所有模板文件。

## 文件列表

| 文件 | 用途 |
|-----|------|
| `template_param.h` | 参数结构体模板 |
| `template_tiling.cpp` | Tiling 测试模板 |
| `template_tiling.csv` | Tiling CSV 示例 |
| `template_infershape.cpp` | InferShape 测试模板 |
| `template_infershape.csv` | InferShape CSV 示例 |
| `template_inferdtype.cpp` | InferDataType 测试模板 |
| `template_inferdtype.csv` | InferDataType CSV 示例 |
| `template_cmake.txt` | CMakeLists.txt 模板 |

## 使用方法

### 1. 触发条件

在 UT 开发流程中，**仅 ops-transformer 仓**支持 CSV 格式重构：
- `repo_type` 为 **"ops-transformer"**
- 用户提及 **"CSV"**、**"CSV整改"**、**"CSV格式"**、**"CSV化"**

### 2. 重构流程

参考 [references/ops-transformer/csv-refactor-workflow.md](../../../references/ops-transformer/csv-refactor-workflow.md)

### 3. CSV 格式规范

参考 [references/ops-transformer/csv-format-spec.md](../../../references/ops-transformer/csv-format-spec.md)

## 模板使用说明

### 文件命名规范

**必须严格遵守**：

| 测试类型 | 文件名格式 | 示例 |
|---------|-----------|------|
| Tiling | `test_{op}_tiling.cpp` | `test_my_op_tiling.cpp` |
| InferShape | `test_{op}_shape_infershape.cpp` | `test_my_op_shape_infershape.cpp` |
| InferDataType | `test_{op}_dtype_infershape.cpp` | `test_my_op_dtype_infershape.cpp` |

⚠️ **重要**：
- InferShape 文件名必须包含 `_shape_` 关键字
- InferDataType 文件名必须包含 `_dtype_` 关键字

### 参数结构体要求

**必须继承 `HostUtParamBase` 基类**：

```cpp
// ✓ 正确
struct MyOpHostUtParamBase : public HostUtParamBase {
    // 仅添加算子特定属性
    int64_t num_heads;
    float scale;
};

// ✗ 错误
struct MyOpHostUtParamBase {
    std::string case_name;  // 不要重复定义基类字段
    // ...
};
```

## 自动化工具

使用脚本自动生成模板：

```bash
python scripts/generate_csv_template.py {op_name}_def.cpp
```

## 详细文档

- [CSV 重构工作流程](../../../references/ops-transformer/csv-refactor-workflow.md)
- [CSV 格式规范](../../../references/ops-transformer/csv-format-spec.md)
- [从旧代码提取参数](../../../references/ops-transformer/legacy-code-extraction.md)