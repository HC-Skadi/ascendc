

# ⚡ ascend-skills-eval

**面向昇腾Skills 的评测小站**  
九维打分 · 改进建议 · Markdown 报告 · 成果卡· 浏览器里粘贴 / 单仓 / 批量测全支持

**[🌐 在线体验](https://ascend-skills-eval.zeabur.app/)** · **[🐛 报告问题](https://github.com/huxiaoman7/ascend-skills-eval/issues)** · **[💡 功能建议](https://github.com/huxiaoman7/ascend-skills-eval/issues)** · **[📎 Web 服务文档](web-service/README.md)**

[License: MIT](https://opensource.org/licenses/MIT)
[GitHub stars](https://github.com/huxiaoman7/ascend-skills-eval)
[GitHub issues](https://github.com/huxiaoman7/ascend-skills-eval/issues)
[Last commit](https://github.com/huxiaoman7/ascend-skills-eval/commits/main)

  


Ascend Skills-Eval web UI — paste / single repo / batch tabs, scores, local history



---

## 目录

- [这个项目是干嘛的](#about)
- [能做什么](#features)
- [本地跑起来](#quickstart)
- [HTTP API](#api)
- [仓库结构](#layout)
- [参与贡献](#contributing)
- [安全](#security)
- [交流与致谢](#community)
- [License](#license)

---



## 💡 这个项目是干嘛的

给 **昇腾相关** 的 Agent Skill（`SKILL.md`）做 **结构化体检**：像代码审查一样看 frontmatter、工作流、边界、检查点、指令精度等维度，并给出可下载的 **评分报告** 和一张 **成果卡图**，方便放进文档或分享。

自带一个 **FastAPI + 静态页** 的小服务：本地或自建部署后，用浏览器就能评测——**不要求**你先搭一整套评测平台。

---



## ✨ 能做什么


|             | 说明                                                                |
| ----------- | ----------------------------------------------------------------- |
| 📋 **粘贴评测** | 整份 `SKILL.md` 贴进去，一键出分 + 成果卡                                      |
| 🔗 **单仓库**  | 填 **HTTPS 公开** GitHub / GitCode 等地址，服务端浅克隆并自动找 `SKILL.md`         |
| 📊 **批量仓库** | 多行 URL，排行榜 + 汇总 MD，点行切换不同仓库的成果卡                                   |
| 🎁 **产出**   | 维度分、文字建议、Markdown 报告、PNG 成果卡                                      |
| 💾 **本机历史** | 最近 **10** 条在 **localStorage**，可回放 / 单删 / **清空全部**；服务端 **不存** 评测历史 |


---



## 🚀 本地跑起来

不想先装环境？可以直接打开 **[在线体验](https://ascend-skills-eval.zeabur.app/)**（Zeabur 托管；评测历史仍在你的浏览器 **localStorage**）。

**环境**：Python **3.10+**、**Node.js**（Playwright 渲染 PNG 用）

```bash
cd web-service
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

npm i -D playwright
npx playwright install chromium

uvicorn app.main:app --host 0.0.0.0 --port 8000
```


| 打开                                                           | 说明            |
| ------------------------------------------------------------ | ------------- |
| [在线体验](https://ascend-skills-eval.zeabur.app/)               | 公网演示（与本地同源页面） |
| [http://127.0.0.1:8000/](http://127.0.0.1:8000/)             | 本地评测主页        |
| [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) | 本地健康检查        |


更多 **curl 示例**、Docker、线上部署细节见 **[web-service/README.md](web-service/README.md)**。

---



## 📝 HTTP API


| 方法     | 路径                     | 说明                  |
| ------ | ---------------------- | ------------------- |
| `POST` | `/eval`                | 仅结构评估               |
| `POST` | `/evaluate-and-render` | 评估 + 成果卡 PNG        |
| `POST` | `/evaluate-repo`       | 单仓库克隆 + 评估 + 出图     |
| `POST` | `/evaluate-repos`      | 批量（≤20），排行榜 + 汇总 MD |
| `POST` | `/render-card`         | 仅渲染成果卡              |
| `GET`  | `/`                    | 内置 Web 页            |
| `GET`  | `/health`              | 存活探针                |


> 无 `GET /history`：历史只在浏览器 **localStorage**，换设备即新会话。

---



## 📦 仓库结构

```text
skills-eval/
├─ docs/screenshots/         # README 配图
├─ skills/skills-eval/       # SKILL 工作流、模板、render-card / Playwright
├─ web-service/              # FastAPI 服务 + 静态前端
│  └─ app/static/index.html
└─ README.md
```

---



## 🤝 参与贡献

欢迎 **PR** 和 **Issue**（修文档、改文案、调评分逻辑都好）：

1. Fork 后从 `main` 拉分支，改动尽量 **小而专注**。
2. PR 里写清楚 **动机**、**如何自测**（有界面/API 变动可贴截图或 curl）。
3. 对事不对人，review 意见都是为了让合并更稳 😊

详细约定若后续需要，可再补 `CONTRIBUTING.md`；当前以 Issues 沟通为主即可。

---



## 🔐 安全

若发现 **漏洞**，请勿在公开 Issue 中贴完整复现与敏感数据；请使用 GitHub **Security Advisories（私有报告）** 或先发标题式 Issue 再私下对接。感谢 🙏

---



## 💬 交流与致谢

- **提问 / 吐槽 / 想要功能** → **[Issues](https://github.com/huxiaoman7/ascend-skills-eval/issues)**  
- 工作流思路感谢 **[darwin-skill](https://github.com/alchaincyf/darwin-skill)** 的启发；本项目在昇腾场景下做了评测、仓库拉取、批量与可视化等扩展。

---

## License

**MIT** — 自由使用与修改，分发时请保留版权声明 📄