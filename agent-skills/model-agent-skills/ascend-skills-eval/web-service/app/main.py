from __future__ import annotations

import base64
import json
import re
import subprocess
import tempfile
from urllib.parse import urlparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


class EvalRequest(BaseModel):
    skill_markdown: str = Field(..., min_length=1, description="完整 SKILL.md 内容")
    skill_name: str | None = Field(default=None, description="可选的技能名")


class RepoEvalRequest(BaseModel):
    repo_url: str = Field(..., min_length=1, description="GitHub 或 GitCode 仓库链接")
    skill_path: str | None = Field(default=None, description="可选，指定仓库内文件路径，如 skills/foo/SKILL.md")
    branch: str | None = Field(default=None, description="可选，指定分支")


class BatchRepoEvalRequest(BaseModel):
    items: list[RepoEvalRequest] = Field(..., min_length=1, max_length=20, description="批量仓库评分任务列表")


class DimensionScore(BaseModel):
    id: int
    name: str
    weight: int
    score: float
    reason: str


class EvalResponse(BaseModel):
    skill_name: str
    total_score: float
    dimensions: list[DimensionScore]
    suggestions: list[str]
    mode: str = "structure_eval"


class RenderRequest(BaseModel):
    data: dict[str, Any]
    open_image: bool = Field(default=False, description="是否在服务器上执行 open 命令")


class RenderResponse(BaseModel):
    image_base64: str
    mime_type: str = "image/png"
    size_bytes: int


app = FastAPI(
    title="ascend-skills-eval online service",
    version="0.1.0",
    description="在线评测昇腾 Skills（结构评估）并生成成果卡。",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


DIMENSIONS: list[tuple[int, str, int]] = [
    (1, "Frontmatter质量", 8),
    (2, "工作流清晰度", 15),
    (3, "边界条件覆盖", 10),
    (4, "检查点设计", 7),
    (5, "指令具体性", 15),
    (6, "资源整合度", 5),
    (7, "整体架构", 15),
    (8, "昇腾适配性", 10),
    (9, "实测表现(结构代理分)", 15),
]


def _has_frontmatter(text: str) -> bool:
    return bool(re.search(r"(?s)\A---\n.*?\n---\n", text))


def _count_pattern(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE))


def _clamp_score(v: float) -> float:
    return float(max(1.0, min(10.0, round(v, 1))))


def evaluate_skill(skill_markdown: str, skill_name: str | None = None) -> EvalResponse:
    text = skill_markdown
    name = skill_name or "unknown-skill"

    heading_count = _count_pattern(text, r"^##\s+")
    numbered_steps = _count_pattern(text, r"^\s*\d+\.\s+")
    code_block_count = _count_pattern(text, r"^```")
    command_count = _count_pattern(text, r"\b(npu-smi|python3?|pip|git|node|npm|uvicorn)\b")
    edge_count = _count_pattern(text, r"(异常|错误|fallback|失败|如果.*则|回滚|recover|retry)")
    checkpoint_count = _count_pattern(text, r"(确认|checkpoint|暂停|approval|用户确认)")
    resource_count = _count_pattern(text, r"(templates?/|scripts?/|results\.tsv|evals?\.json|references?)")
    ascend_count = _count_pattern(text, r"(ascend|npu|torch_npu|cann|npu-smi|昇腾)")
    test_count = _count_pattern(text, r"(test[- ]?prompts?|实测|benchmark|验证|eval)")

    d1 = 7.5 if _has_frontmatter(text) else 3.0
    d1 += 1.0 if "description:" in text else 0.0

    d2 = 4.5 + min(4.0, numbered_steps * 0.25) + min(1.5, heading_count * 0.15)
    d3 = 3.5 + min(5.0, edge_count * 0.4)
    d4 = 3.0 + min(6.0, checkpoint_count * 0.8)
    d5 = 4.0 + min(2.5, code_block_count * 0.2) + min(3.0, command_count * 0.25)
    d6 = 3.5 + min(5.0, resource_count * 0.8)
    d7 = 4.0 + min(3.0, heading_count * 0.3) + min(2.5, numbered_steps * 0.15)
    d8 = 2.5 + min(7.0, ascend_count * 0.35)
    # 在线环境通常无法真机验证，用结构代理分替代
    d9 = 3.5 + min(4.0, test_count * 0.35) + min(2.0, command_count * 0.2)

    raw_scores = [d1, d2, d3, d4, d5, d6, d7, d8, d9]
    reasons = [
        "检测到 frontmatter 与描述字段。",
        "按标题与步骤结构评估流程可执行性。",
        "根据 fallback/异常处理描述覆盖度估算。",
        "根据用户确认与检查点关键词估算。",
        "基于命令、参数与代码块密度估算。",
        "根据 templates/scripts/results 等资源引用估算。",
        "根据章节层次与步骤组织估算。",
        "根据 Ascend/NPU 相关术语与命令覆盖度估算。",
        "在线模式以测试与验证描述给出结构代理分。",
    ]

    dimensions: list[DimensionScore] = []
    weighted_sum = 0.0
    for idx, (meta, score, reason) in enumerate(zip(DIMENSIONS, raw_scores, reasons), start=1):
        dim_id, dim_name, weight = meta
        final_score = _clamp_score(score)
        weighted_sum += final_score * weight
        dimensions.append(
            DimensionScore(
                id=dim_id,
                name=dim_name,
                weight=weight,
                score=final_score,
                reason=reason,
            )
        )

    total = round(weighted_sum / 10.0, 1)
    sorted_dims = sorted(dimensions, key=lambda x: x.score)
    suggestions = [
        f"优先优化维度「{sorted_dims[0].name}」：补充更具体步骤、输入输出和异常处理。",
        f"其次优化「{sorted_dims[1].name}」：增加可执行命令与验证证据。",
        "若需要真实NPU结论，请接入本地Ascend Runner执行 npu-smi 和关键命令回传。",
    ]

    return EvalResponse(
        skill_name=name,
        total_score=total,
        dimensions=dimensions,
        suggestions=suggestions,
    )


def _render_script_path() -> Path:
    current = Path(__file__).resolve()
    for parent in [current.parent, *current.parents]:
        candidate = parent / "skills" / "skills-eval" / "scripts" / "render-card.mjs"
        if candidate.exists():
            return candidate
    raise FileNotFoundError("无法定位 render-card.mjs，请检查目录结构。")


def _build_report_markdown(
    eval_result: EvalResponse, *, source_label: str, source_value: str, picked_file: str
) -> str:
    lines = [
        "# ascend-skills-eval 评分报告",
        "",
        f"- 来源类型：{source_label}",
        f"- 来源：{source_value}",
        f"- 评估文件：{picked_file}",
        f"- 技能名：{eval_result.skill_name}",
        f"- 总分：{eval_result.total_score}/100",
        f"- 模式：{eval_result.mode}",
        "",
        "## 维度评分",
        "",
        "| # | 维度 | 权重 | 分数 | 说明 |",
        "|---|---|---:|---:|---|",
    ]
    for d in eval_result.dimensions:
        lines.append(f"| {d.id} | {d.name} | {d.weight} | {d.score} | {d.reason} |")

    lines.extend(["", "## 优化建议", ""])
    for idx, tip in enumerate(eval_result.suggestions, start=1):
        lines.append(f"{idx}. {tip}")
    lines.append("")
    return "\n".join(lines)


def _validate_repo_url(repo_url: str) -> str:
    parsed = urlparse(repo_url)
    if parsed.scheme not in {"http", "https"}:
        raise HTTPException(status_code=400, detail="仓库链接必须是 http/https")
    host = (parsed.netloc or "").lower()
    allowed_hosts = {"github.com", "www.github.com", "gitcode.com", "www.gitcode.com"}
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail="仅支持 GitHub/GitCode 链接")
    return repo_url


def _pick_repo_file(repo_dir: Path, skill_path: str | None) -> Path:
    if skill_path:
        specified = (repo_dir / skill_path).resolve()
        if not str(specified).startswith(str(repo_dir.resolve())):
            raise HTTPException(status_code=400, detail="skill_path 非法")
        if not specified.exists() or not specified.is_file():
            raise HTTPException(status_code=400, detail=f"未找到指定文件: {skill_path}")
        return specified

    priority = ["SKILL.md", "skill.md", "README.md", "README.zh-CN.md", "README_CN.md"]
    for name in priority:
        p = repo_dir / name
        if p.exists() and p.is_file():
            return p

    for name in priority:
        matches = list(repo_dir.rglob(name))
        if matches:
            return matches[0]

    md_files = list(repo_dir.rglob("*.md"))
    if md_files:
        return md_files[0]
    raise HTTPException(status_code=400, detail="仓库中未找到可评估的 markdown 文件")


def _repo_name_from_url(repo_url: str) -> str:
    tail = repo_url.rstrip("/").split("/")[-1]
    if tail.endswith(".git"):
        tail = tail[:-4]
    return tail or "repo-skill"


def _evaluate_repo_internal(payload: RepoEvalRequest) -> dict[str, Any]:
    repo_url = _validate_repo_url(payload.repo_url.strip())
    with tempfile.TemporaryDirectory(prefix="ascend-skills-repo-") as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        repo_dir = tmp_dir / "repo"

        clone_cmd = ["git", "clone", "--depth", "1"]
        if payload.branch:
            clone_cmd.extend(["--branch", payload.branch])
        clone_cmd.extend([repo_url, str(repo_dir)])
        proc = subprocess.run(clone_cmd, capture_output=True, text=True, timeout=120)
        if proc.returncode != 0:
            raise HTTPException(
                status_code=400,
                detail={
                    "message": "仓库拉取失败（请确认仓库可公开访问）",
                    "stdout": proc.stdout.strip(),
                    "stderr": proc.stderr.strip(),
                },
            )

        picked_file = _pick_repo_file(repo_dir, payload.skill_path)
        try:
            skill_markdown = picked_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            skill_markdown = picked_file.read_text(encoding="utf-8", errors="ignore")

        inferred_name = _repo_name_from_url(repo_url)
        eval_result = evaluate_skill(skill_markdown, inferred_name)
        dims_for_card = [
            {"name": d.name.replace("(结构代理分)", ""), "before": max(1, int(d.score) - 1), "after": int(round(d.score))}
            for d in eval_result.dimensions[:8]
        ]
        card_data = {
            "skill-name": eval_result.skill_name,
            "skill-id": eval_result.skill_name,
            "score-before": max(1, int(eval_result.total_score) - 8),
            "score-after": int(round(eval_result.total_score)),
            "improve-1": eval_result.suggestions[0],
            "improve-2": eval_result.suggestions[1],
            "improve-3": eval_result.suggestions[2],
            "dims": dims_for_card,
        }
        render_result = render_card(RenderRequest(data=card_data, open_image=False))
        picked_rel = str(picked_file.relative_to(repo_dir))
        report_markdown = _build_report_markdown(
            eval_result,
            source_label="仓库链接",
            source_value=repo_url,
            picked_file=picked_rel,
        )

        history_id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
        return {
            "eval": eval_result.model_dump(),
            "card": render_result.model_dump(),
            "report_markdown": report_markdown,
            "picked_file": picked_rel,
            "repo_url": repo_url,
            "skill_markdown": skill_markdown,
            "history_id": history_id,
        }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "ascend-skills-eval"}


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/eval", response_model=EvalResponse)
def eval_skill(payload: EvalRequest) -> EvalResponse:
    return evaluate_skill(payload.skill_markdown, payload.skill_name)


@app.post("/render-card", response_model=RenderResponse)
def render_card(payload: RenderRequest) -> RenderResponse:
    render_script = _render_script_path()
    if not render_script.exists():
        raise HTTPException(status_code=500, detail=f"找不到渲染脚本: {render_script}")

    with tempfile.TemporaryDirectory(prefix="ascend-skills-eval-") as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        data_path = tmp_dir / "card-data.json"
        png_path = tmp_dir / "result-card.png"
        html_path = tmp_dir / "result-card.rendered.html"
        data_path.write_text(json.dumps(payload.data, ensure_ascii=False), encoding="utf-8")

        cmd = [
            "node",
            str(render_script),
            "--data",
            str(data_path),
            "--png",
            str(png_path),
            "--html",
            str(html_path),
        ]
        if not payload.open_image:
            cmd.append("--no-open")

        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise HTTPException(
                status_code=500,
                detail={
                    "message": "渲染失败",
                    "stdout": proc.stdout.strip(),
                    "stderr": proc.stderr.strip(),
                },
            )
        if not png_path.exists():
            raise HTTPException(status_code=500, detail="渲染脚本执行成功但未生成 PNG。")

        raw = png_path.read_bytes()
        return RenderResponse(
            image_base64=base64.b64encode(raw).decode("ascii"),
            size_bytes=len(raw),
        )


@app.post("/evaluate-and-render")
def evaluate_and_render(payload: EvalRequest) -> dict[str, Any]:
    eval_result = evaluate_skill(payload.skill_markdown, payload.skill_name)
    dims_for_card = [
        {"name": d.name.replace("(结构代理分)", ""), "before": max(1, int(d.score) - 1), "after": int(round(d.score))}
        for d in eval_result.dimensions[:8]
    ]
    card_data = {
        "skill-name": eval_result.skill_name,
        "skill-id": eval_result.skill_name,
        "score-before": max(1, int(eval_result.total_score) - 8),
        "score-after": int(round(eval_result.total_score)),
        "improve-1": eval_result.suggestions[0],
        "improve-2": eval_result.suggestions[1],
        "improve-3": eval_result.suggestions[2],
        "dims": dims_for_card,
    }
    render_result = render_card(RenderRequest(data=card_data, open_image=False))
    return {"eval": eval_result.model_dump(), "card": render_result.model_dump()}


@app.post("/evaluate-repo")
def evaluate_repo(payload: RepoEvalRequest) -> dict[str, Any]:
    return _evaluate_repo_internal(payload)


@app.post("/evaluate-repos")
def evaluate_repos(payload: BatchRepoEvalRequest) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []

    for item in payload.items:
        try:
            result = _evaluate_repo_internal(item)
            results.append(result)
        except HTTPException as exc:
            failed.append(
                {
                    "repo_url": item.repo_url,
                    "status_code": exc.status_code,
                    "detail": exc.detail,
                }
            )

    ranking = sorted(
        [
            {
                "repo_url": r["repo_url"],
                "skill_name": r["eval"]["skill_name"],
                "total_score": r["eval"]["total_score"],
                "picked_file": r["picked_file"],
                "history_id": r["history_id"],
            }
            for r in results
        ],
        key=lambda x: x["total_score"],
        reverse=True,
    )

    lines = [
        "# ascend-skills-eval 批量评分报告",
        "",
        f"- 总任务数：{len(payload.items)}",
        f"- 成功：{len(results)}",
        f"- 失败：{len(failed)}",
        "",
        "## 排行榜",
        "",
        "| 排名 | 仓库 | 技能名 | 总分 | 评估文件 |",
        "|---:|---|---|---:|---|",
    ]
    for i, item in enumerate(ranking, start=1):
        lines.append(
            f"| {i} | {item['repo_url']} | {item['skill_name']} | {item['total_score']} | {item['picked_file']} |"
        )
    if failed:
        lines.extend(["", "## 失败项", ""])
        for f in failed:
            lines.append(f"- {f['repo_url']}: {f['detail']}")
    batch_report_markdown = "\n".join(lines) + "\n"

    # 与 ranking 第一名对齐（results 顺序与请求顺序一致，未必按分数排序）
    top_card = None
    if ranking:
        top_hid = ranking[0]["history_id"]
        for r in results:
            if r.get("history_id") == top_hid:
                top_card = r.get("card")
                break
    return {
        "summary": {
            "total": len(payload.items),
            "success": len(results),
            "failed": len(failed),
        },
        "ranking": ranking,
        "results": results,
        "failed": failed,
        "batch_report_markdown": batch_report_markdown,
        "top_card": top_card,
    }
