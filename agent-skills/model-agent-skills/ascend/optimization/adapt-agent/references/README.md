# adapt-agent(昇腾模型生态·模型适配Agent)

面向 **GPU 代码 → 昇腾 NPU** 迁移：**审查仓库**、识别迁移堵点，并辅助生成 **兼容层/适配说明**。内容以 **SKILL 与参考文档** 为主，供 Ascend Model Agent 与人工排查共用。

## 在 MoFixGo 中的位置

统一入口 **[MoFix](https://gitcode.com/MoFixGo/MoFix)** 通过工具封装本仓知识；典型工具：

| MoFix 工具名 | 说明 |
|--------------|------|
| `adapt_review_repo` | 对给定仓库 URL 或路径做适配向审查（占位/演进中） |
| `adapt_generate_compat_layer` | 生成兼容层相关输出（占位/演进中） |

实现代码见：`MoFix/examples/tools/adapt_agent_tools.py`。

## 目录说明

| 路径 | 说明 |
|------|------|
| `SKILL.md` | NPU 适配审查 Skill 总述 |
| `references/` | 最佳实践、CANN 迁移、Python API 等参考 |

## 远程仓库

```bash
git clone https://gitcode.com/MoFixGo/adapt-agent.git
```

组织主页：[MoFixGo](https://gitcode.com/MoFixGo)
