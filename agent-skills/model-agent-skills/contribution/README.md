# 社区贡献 Skills

通过 Pull Request 贡献的 Ascend Skill 统一放置于此目录。

## 贡献流程

1. Fork 本仓库
2. 在 `skills/contribution/{分类}/` 下创建你的 skill 文件夹
3. 确保包含标准的 `SKILL.md` 文件
4. 提交 Pull Request

## 目录结构（9 分类）

```
skills/contribution/
├── adaptation/      # 模型适配类贡献
├── deployment/      # 模型部署类贡献
├── documentation/   # 文档生成类贡献
├── optimization/    # 性能优化类贡献
├── quantization/    # 模型量化类贡献
├── search/          # 知识检索类贡献
├── verification/    # 质量验证类贡献
├── common/          # 通用工具类贡献
└── other/           # 其他类贡献
```

## Skill 规范

- 每个 skill 一个独立文件夹
- 文件夹名使用 kebab-case（如 `phi-npu-deploy`）
- 必须包含 `SKILL.md`，且符合 [ascend-darwin-skill 评测规范](https://gitcode.com/raintBN/Ascend-Skills/tree/main/ascend-darwin-skill)
- 鼓励附加 `scripts/`、`references/`、`test-prompts.json` 等辅助资源

## 评测

所有贡献 Skill 会自动触发 `ascend-darwin-skill` CI 评测，
评测结果会以 PR 评论形式反馈。
