---
name: repo-reader
description: 从模型仓库链接读取 README 文档。当用户想要从模型仓库链接（如 https://ai.gitcode.com/Ascend-SACT/Qwen3.5-27B-A2-Vllm-Ascend）获取部署文档、使用说明或任何仓库内容时触发此 skill。使用此 skill 来获取仓库的 README、文档内容、部署命令等。
---

# Repo Reader

此 skill 用于从模型仓库链接获取 README 文档和仓库内容。

## 输入

- 模型仓库链接，如：`https://ai.gitcode.com/Ascend-SACT/Qwen3.5-27B-A2-Vllm-Ascend`

## 工作流程

### 方法1: 从 ai.gitcode.com 获取

将 URL 中的 `ai.gitcode.com` 替换为 `raw.gitcode.com`，然后拼接 `/raw/main/README.md`

例如：
- 输入：`https://ai.gitcode.com/Ascend-SACT/Qwen3.5-27B-A2-Vllm-Ascend`
- 输出：`https://raw.gitcode.com/Ascend-SACT/Qwen3.5-27B-A2-Vllm-Ascend/raw/main/README.md`

使用 webfetch 工具获取内容。

### 方法2: 使用 curl 命令

如果方法1失败，尝试使用 curl 命令：

```bash
curl -sL "https://raw.gitcode.com/{owner}/{repo}/raw/main/README.md"
```

### 方法3: Git 仓库克隆

如果是 Git 仓库，尝试使用 git clone 克隆仓库，然后读取本地文件：

```bash
git clone <repo_url> /tmp/repo_name
```

然后读取 `/tmp/repo_name/README.md`

## 输出

直接输出获取到的 README 内容，包括：

1. 完整的 README 文档内容
2. 如果需要，提取其中的部署命令、安装步骤等信息

## 注意事项

- 如果仓库是私有仓库，可能需要认证信息
- 如果 README 不在根目录，尝试寻找其他常见位置如 `docs/` 目录
- 某些仓库可能使用不同的文档文件名，如 `INSTALL.md`、`DEPLOY.md` 等