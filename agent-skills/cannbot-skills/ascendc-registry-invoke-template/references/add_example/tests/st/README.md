# add_example 算子 ST 测试

## 概述

系统测试（ST）验证算子正确性和精度。

| 测试方式 | 说明 | 适用场景 |
|----------|------|---------|
| **C++ 原生测试** | 直接编译运行 C++ 测试程序 | 常规测试验证 |

## 目录结构

```
tests/st/
├── CMakeLists.txt              # C++ 测试构建配置
├── run.sh                      # C++ 测试执行脚本
├── test_aclnn_add_example.cpp  # C++ 测试主程序
└── README.md                   # 本文件
```

## 快速开始

### C++ 原生测试

```bash
# Real 模式（默认，需要 NPU）
bash run.sh

# Mock 模式（无需 NPU）
bash run.sh --mock

# 执行指定用例
bash run.sh --case 0
```

### 注意

- 仅支持 C++ 原生测试方式

## 测试用例

| 测试 | 描述 | 覆盖场景 |
|------|------|---------|
| 1-3  | FP32 基础/混合/大shape | 核心 dtype, 负数, 零值 |
| 4    | FP32 多维 (2x3x4) | 3D shape |
| 5-7  | INT32 基础/混合/大shape | INT32 dtype |
| 8    | 单元素 (1元素) | 边界条件 |
| 9-10 | FP32 极值/零值 | 浮点极值, -0.0 |

## 依赖项

- CMake >= 3.10
- g++ (支持 C++17)
- CANN + NPU 设备（Real 模式）

## 常见问题

### 1. 编译失败：找不到 AscendCL

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
```

### 2. NPU 设备不可用

如需无 NPU 验证，请使用 C++ Mock 模式：
```bash
bash run.sh --mock
```
