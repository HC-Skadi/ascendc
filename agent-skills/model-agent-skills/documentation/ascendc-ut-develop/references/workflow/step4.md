## Step 4 补全用例，提升覆盖率

**如果用户没有明确说明跳过本步骤，不得跳过**

> **本步骤使用 Task 工具调用子 Agent 进行调试，避免污染上下文**

### Step 4.1: 获取当前覆盖率

```bash
# 编译并生成覆盖率
cd ${repo_path} && bash build.sh -u --ops=${op_name} --soc=${soc_type} --cov
```

### Step 4.2: 阅读算子文档

```bash
# 查找并阅读算子目录下的 md 文档
find ${op_path} -name "*.md" -exec cat {} \;
```

### Step 4.3: 判断覆盖率类型

编译后需要先判断是**全局覆盖率**还是**单算子覆盖率**：

```bash
# 查看覆盖率报告包含的文件路径
lcov --list ops.info_filtered | head -50
```

| 覆盖率类型 | 文件路径特征 | 处理方式 |
|-----------|-------------|---------|
| 单算子覆盖率 | 仅包含当前算子路径 | 直接使用 |
| 全局覆盖率 | 包含多个算子路径 | 需要使用 `lcov --extract` 提取 |

详细提取方法见 [coverage-extraction.md](../coverage-guide/coverage-extraction.md)

### Step 4.4: 分析未覆盖代码

1. **获取未覆盖代码清单**
   ```bash
   lcov --list ops.info_filtered | grep ":0"
   ```
2. **分析分支条件** — 识别进入该分支需要的参数组合
3. **设计测试用例** — 参考 [test-implementation.md](../coverage-guide/test-implementation.md)

### Step 4.5: 迭代补充用例

**用例来源**：
- 已有算子文档中的示例
- 重构前的旧用例
- 算子其它组件的用例
- 未覆盖代码分析结果

**迭代策略**：

| 缺口类型 | 补充策略 |
|---------|---------|
| 异常分支 | 添加 ACLNN_ERR_*/GRAPH_FAILED 用例 |
| dtype分支 | 确保每个 dtype 都有测试 |
| 边界条件 | 添加空tensor、大shape用例 |
| 格式分支 | 添加各 format 的测试用例 |

**完成检查**：
- [ ] 所有新增测例通过
- [ ] 行覆盖率 >= 80%
- [ ] 函数覆盖率 >= 80%
