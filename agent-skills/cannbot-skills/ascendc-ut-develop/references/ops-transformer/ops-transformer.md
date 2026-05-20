# ops-transformer 算子仓特性

## CSV 格式输入用例

transformer 仓在现有 UT 框架的基础上，封装了一层 CSV 导入工具。

使用 csv 格式输入的优势：
- 数据与代码分离，用例框架编译完成后，仅修改用例表格时无需重复编译
- 避免重复代码，对于多参数算子，可大幅缩减用例长度，缩小模型上下文

**对于 transformer 仓的算子，优先使用 CSV 格式创建用例。**

详细指南：[CSV 重构流程详解](./csv-refactor-workflow.md)、[CSV 格式规范](./csv-format-spec.md)

## 多架构支持

ops-transformer 仓支持多种芯片架构，需要特别注意：

### SoC 与架构对应关系

| SoC 参数 | 架构 | 编译示例 |
|---------|------|---------|
| `ascend910b` | arch32 | `--soc=ascend910b` |
| `ascend950` | arch35 | `--soc=ascend950` |

### 编译注意事项

**重要**：编译时必须指定 `--soc` 参数，否则对应架构的代码不会被编译！

```bash
# 编译 arch35 用例
bash build.sh --ophost_test --noexec --ops=<op_name> --soc=ascend950

# 编译 arch32 用例
bash build.sh --ophost_test --noexec --ops=<op_name> --soc=ascend910b
```

### 运行注意事项

运行测试时需要设置 `BUILD_PATH` 环境变量：

```bash
export BUILD_PATH=/path/to/ops-transformer/build
./build/tests/ut/framework_normal/op_host/transformer_op_host_ut --gtest_filter="*Arch35*"
```
