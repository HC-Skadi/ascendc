---
name: ascendc-direct-invoke-template
description: Kernel直调工程模板，用于创建 Ascend C Kernel 直调工程项目。提供经过验证的样例工程和清晰的修改指南。触发：当用户需要创建 Kernel 直调工程、学习 Ascend C 编程、快速原型验证、或提及"Kernel直调"、"<<<>>>内核调用"时使用本 skill。
---

# Ascend C Kernel 直调工程

## 使用方法

1. **复制样例目录**：
   **your_project_name**是你的算子名称
   ```bash
   # 若算子目录<your_project_name>未创建
   cp -r references/add_kernel <your_project_name>
   # 若算子目录<your_project_name>已存在
   cp -r references/add_kernel/* <your_project_name>
   cd <your_project_name>
   ```

2. **阅读 `add.asc` 中的注释**（搜索 `[MODIFY]` 标记），修改以下内容：
   - 类名和 kernel 函数名
   - Tiling 结构体
   - 计算逻辑
   - 输入/输出数量
   - `CMakeLists.txt` 中的目标名

3. **编译运行**：
   ```bash
   # 完整流程（含编译）
   bash run.sh

   # 仅运行测试，复用已有编译产物（代码审查阶段使用，避免重复编译）
   bash run.sh --skip-build
   ```
   > `run.sh` 在运行 kernel 前会自动删除旧的 `output/output.bin`，确保精度验证读取的是本次运行的新鲜输出。

## 文件说明

| 文件 | 说明 |
|------|------|
| `references/add_kernel/add.asc` | **核心样例**，包含详细注释和修改指南 |
| `references/add_kernel/data_utils.h` | 数据读写工具 |
| `references/add_kernel/scripts/` | 数据生成和验证脚本 |
| `references/kernel_launch_details.md` | 深入理解：编程模型、性能优化技巧 |

## 代码关键模式

在 `add.asc` 中可直接学习：

- **内存分配**: `LocalMemAllocator` 简化 UB 分配
- **数据流**: CopyIn → Compute → CopyOut 三段模式
- **同步**: `PipeBarrier<PIPE_*>` 确保操作顺序
- **Host 流程**: ACL 初始化 → KernelCall → 资源释放

## 参考资源

- [Ascend C 示例代码](https://gitcode.com/cann/asc-devkit/tree/master/examples)
- NPU 架构配置详见 `ascendc-npu-arch` skill
