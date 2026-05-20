# ascend-skills-eval online service

面向 Zeabur 的最小在线服务，支持：

- `POST /eval`：在线结构评估（9维，含实测代理分）
- `POST /render-card`：基于你现有模板渲染成果卡 PNG（返回 base64）
- `POST /evaluate-and-render`：一步完成评估 + 出图
- `POST /evaluate-repo`：输入 GitHub/GitCode 链接，自动拉取仓库评分并出图
- `POST /evaluate-repos`：批量仓库评分（支持排行榜和批量报告）
- `GET /health`：健康检查
- `GET /`：内置极简 Web 页面（粘贴 SKILL.md 直接评估）

> Web 页「最近评测」列表仅存于**浏览器 localStorage**（每设备独立），服务端不保存历史。  
> 说明：此版本默认是**在线结构评估**。真实 NPU 实测需要额外接入本地 Ascend Runner。

## 本地运行

```bash
cd /Users/huxiaoman/MoFixGo
python3 -m venv .venv-svc
source .venv-svc/bin/activate
pip install -r skills-eval/web-service/requirements.txt

# Node 依赖（用于 render-card 脚本）
npm i -D playwright
npx playwright install chromium

uvicorn app.main:app --app-dir skills-eval/web-service --host 0.0.0.0 --port 8000
```

## API 示例

### 1) 结构评估

```bash
curl -X POST "http://127.0.0.1:8000/eval" \
  -H "Content-Type: application/json" \
  -d '{
    "skill_name": "ascend-skills-eval",
    "skill_markdown": "# demo\n## step\n1. do something with npu-smi info"
  }'
```

### 2) 评估并出图

```bash
curl -X POST "http://127.0.0.1:8000/evaluate-and-render" \
  -H "Content-Type: application/json" \
  -d '{
    "skill_name": "ascend-skills-eval",
    "skill_markdown": "# demo\n## step\n1. npu-smi info\n2. fallback when error"
  }'
```

返回体中 `card.image_base64` 即可在前端直接展示。

### 3) 仓库链接评分并出图

```bash
curl -X POST "http://127.0.0.1:8000/evaluate-repo" \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/MoFixGo/MoFix"
  }'
```

可选 `skill_path` 指定仓库内目标文件路径（例如 `skills/foo/SKILL.md`）。

### 4) 批量仓库评分（每次最多20个）

```bash
curl -X POST "http://127.0.0.1:8000/evaluate-repos" \
  -H "Content-Type: application/json" \
  -d '{
    "items": [
      {"repo_url": "https://github.com/MoFixGo/MoFix"},
      {"repo_url": "https://github.com/MoFixGo/search-agent"}
    ]
  }'
```

返回包含：

- `ranking`：按总分降序排列
- `batch_report_markdown`：可下载的批量报告
- `top_card`：第一名仓库的评分卡（base64）

## Zeabur 部署

本服务在独立仓库 **ascend-skills-eval** 中发布（根目录下即有 `web-service/`、`skills/`）。Zeabur 必须绑定**该仓库**，不要绑定 MoFixGo 根仓（根仓 Git 里通常没有本服务代码）。

### 方式A：Dockerfile 部署（推荐）

**重要（为何曾出现「RUNNING 但只有 Caddy、网站 404」）**：Zeabur 文档写明，只有仓库**根目录**存在 `Dockerfile` / `dockerfile` 时才会按 Docker 构建。若仅有 `web-service/Dockerfile` 而无根 `Dockerfile`，平台会走 **Git 默认流程（内置 Caddy 监听 8080）**，不是你的 FastAPI → 运行时日志里几乎只有 Caddy，`/health` 也会 404。本仓库已在**根目录**提供 `Dockerfile`，推送后重新部署即可。

1. 将本仓库推到 GitHub（例如 `huxiaoman7/ascend-skills-eval`）
2. 在 Zeabur 新建 Project，选择 **ascend-skills-eval** 仓库
3. 使用 **根目录 `Dockerfile`**（自动检测即可；无需再单独指定子路径，除非你在面板里显式改过）
4. **Root Directory**：留空（仓库根）
5. 根 `Dockerfile` 默认 `PORT=8080` / `EXPOSE 8080`，与 Zeabur 常见 Web 端口一致；`CMD` 使用 `${PORT}`，若平台注入其他端口也会生效
6. 子目录 `web-service/Dockerfile` 与根文件内容一致，仅供本地 `docker build -f web-service/Dockerfile .` 使用
7. 部署成功后验收：
   - **Runtime Logs** 中应出现 **Uvicorn** 启动行（例如 `Uvicorn running on http://0.0.0.0:8080`），而不是只有 Caddy
   - `https://<你的域名>/health` → **200** + JSON：`{"status":"ok","service":"ascend-skills-eval"}`
   - `https://<你的域名>/` → 评测页

若仍为 404：看 **Build Logs** 是否在用 Docker 构建；若构建成功但日志仍只有 Caddy，检查 Zeabur 是否开启了 `ZBPACK_IGNORE_DOCKERFILE` 或 `zbpack.json` 里 `ignore_dockerfile`。

### 方式B：源码构建（可选）

不建议，Playwright 浏览器依赖较多，Docker 更稳。

## 下一步（真实NPU在线实测）

如果要做“在线提交 + 真机NPU验证”，建议：

1. 本服务负责接单/展示结果（Zeabur）
2. 在你的 Ascend 机器部署 runner（轮询任务，执行 `npu-smi info` + 关键命令）
3. runner 回传日志与分数到本服务

这样能同时满足“在线可用”和“真机可信”。
