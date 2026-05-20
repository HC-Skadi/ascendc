# ST 测试开发指南

本文档提供 ST（System Test）测试工程开发的完整指南，基于 `add_example` 样例说明开发流程和技术要点。

## 1. 测试方式概述

本项目使用 C++ 原生测试方式：直接编译运行 C++ 测试程序进行常规测试验证。

## 2. 目录结构

```
${op_name}/tests/st/
├── CMakeLists.txt              # C++ 测试构建配置
├── run.sh                      # C++ 测试执行脚本
├── test_aclnn_${op_name}.cpp   # C++ 测试主程序
└── README.md                   # 说明文档（可选）
```

## 3. C++ 原生测试（默认方式）

### 3.1 架构说明

```
test_aclnn_${op_name}.cpp
├── ComputeGolden()        # CPU golden 计算
├── CompareResults()       # 精度比对
├── TestGoldenCorrectness() # CPU golden 自测
├── RunTest()              # 统一测试执行器
├── GetTestCases()         # 测试用例定义
└── main()                 # 主函数
```

**Mock/Real 模式切换**：

| 模式 | 编译选项 | 适用场景 |
|------|---------|---------|
| Mock | `-DUSE_MOCK=ON` | 算子代码未就绪时，验证测试框架流程 |
| Real | `-DUSE_MOCK=OFF` | 算子代码已就绪，执行真实 NPU 精度验证 |

### 3.2 使用方式

```bash
# Real 模式（默认，需要 NPU）
bash run.sh

# Mock 模式（无需 NPU）
bash run.sh --mock
```

### 3.3 完整样例

参考 `references/add_example/tests/st/` 下的文件：
- `CMakeLists.txt`
- `run.sh`
- `test_aclnn_add_example.cpp`

### 3.4 必须修改的部分

1. **ComputeGolden()** - 根据算子计算逻辑实现 CPU golden
2. **TestGoldenCorrectness()** - 添加算子特定的 golden 自测用例
3. **GetTestCases()** - 根据测试设计文档定义测试用例
4. **RunTest()** - 根据算子 ACLNN 接口调整参数
5. **CMakeLists.txt 中的 find_path/find_library** - 修改算子名称

## 4. 核心组件说明

### 4.1 CPU Golden 计算

```cpp
template<typename T>
void ComputeGolden(const T* x1, const T* x2, T* output, size_t size) {
    for (size_t i = 0; i < size; ++i) {
        output[i] = x1[i] + x2[i];  // 示例：加法
    }
}
```

### 4.2 精度比对

```cpp
template<typename T>
bool CompareResults(const T* golden, const T* actual, size_t size, 
                    double rtol = 1e-5, double atol = 1e-8) {
    // 比对逻辑
}
```

**精度标准**（CANN 算子精度验收社区标准）：

| 数据类型 | 方法 | Threshold |
|---------|------|-----------|
| FLOAT16 | MERE/MARE | 2^-10 ≈ 0.000977 |
| BFLOAT16 | MERE/MARE | 2^-7 ≈ 0.00781 |
| FLOAT32 | MERE/MARE | 2^-13 ≈ 0.000122 |
| INT32 | 精确匹配 | - |

## 5. 开发流程

### 5.1 C++ 测试开发步骤

1. **开发测试代码**
   - 实现 `ComputeGolden()` 函数
   - 实现 `TestGoldenCorrectness()` 自测
   - 实现 `GetTestCases()` 测试用例

2. **编译验证**
   ```bash
   cd ${op_name}/tests/st
   bash run.sh --mock  # Mock 模式验证
   bash run.sh         # Real 模式验证（需要 NPU）
   ```

## 6. 常见问题

### Q1: CPU golden 计算如何处理不同数据类型？

使用模板支持不同的数据类型。

### Q2: 如何处理动态 shape？

在测试用例中定义不同的 shape。

### Q3: 精度阈值如何确定？

默认使用 CANN 算子精度验收社区标准（MERE/MARE Threshold），已内置在比对函数中，按 dtype 自动选取阈值。

### Q4: 如何添加新的测试用例？

在 `GetTestCases()` 函数中添加新的 TestCase。

## 7. 依赖项

### C++ 测试
- **CMake**: >= 3.10
- **CANN**: Real 模式需要

## 8. 参考资源

- **完整示例**：`references/add_example/tests/st/`
- **ACLNN 接口调用文档**：`ops-math/docs/zh/invocation/op_invocation.md`
- **Ascend C 编程指南**：https://www.hiascend.com/document
