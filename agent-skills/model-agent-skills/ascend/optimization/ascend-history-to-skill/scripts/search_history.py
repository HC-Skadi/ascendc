#!/usr/bin/env python3
"""Search local agent histories for Ascend adaptation and optimization evidence."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

MAX_FILE_SIZE = 20 * 1024 * 1024
TEXT_SUFFIXES = {
    ".jsonl",
    ".json",
    ".log",
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".toml",
    ".sh",
    ".py",
    ".csv",
}
DEFAULT_STAGE_TERMS = {
    "adapt": ["adapt", "adaptation", "迁移", "适配", "昇腾", "ascend", "npu", "torch_npu", "set_env.sh"],
    "optimize": ["optimize", "optimization", "perf", "benchmark", "性能", "优化", "torch_npu", "TASK_QUEUE_ENABLE", "CPU_AFFINITY_CONF"],
}
DEFAULT_EXCLUDE_TERMS = ["ascend-history-to-skill"]
TOOL_PATHS = {
    "codex": [
        "~/.codex/history.jsonl",
        "~/.codex/sessions",
        "~/.codex/log",
        "~/.codex/state_5.sqlite",
        "~/.codex/logs_1.sqlite",
    ],
    "claude-code": [
        "~/.claude",
        "~/.config/claude",
        "~/.config/Claude",
    ],
    "opencode": [
        "~/.opencode",
        "~/.config/opencode",
        "~/.config/OpenCode",
    ],
    "cursor": [
        "~/.cursor",
        "~/.config/cursor",
        "~/.config/Cursor",
    ],
}


@dataclass
class Hit:
    tool: str
    path: str
    location: str
    score: int
    excerpt: str
    matched_terms: list[str]


def normalize_term(term: str) -> str:
    return term.strip()


def split_csv_args(values: list[str]) -> list[str]:
    parts: list[str] = []
    for value in values:
        for part in value.split(","):
            part = part.strip()
            if part:
                parts.append(part)
    return parts


def build_model_terms(model: str) -> list[str]:
    variants = {model, model.lower()}
    pieces = [piece for piece in re.split(r"[^A-Za-z0-9]+", model) if piece]
    if len(pieces) > 1:
        variants.add("_".join(pieces))
        variants.add("-".join(pieces))
        variants.add(" ".join(pieces))
        variants.add("".join(pieces))
    return sorted(variant for variant in variants if variant)


def build_terms(model: str, stages: list[str], extra_keywords: list[str]) -> list[str]:
    ordered: list[str] = []
    seen = set()
    for term in build_model_terms(model):
        lowered = term.lower()
        if lowered not in seen:
            ordered.append(term)
            seen.add(lowered)
    for stage in stages:
        for term in DEFAULT_STAGE_TERMS[stage]:
            lowered = term.lower()
            if lowered not in seen:
                ordered.append(term)
                seen.add(lowered)
    for term in extra_keywords:
        term = normalize_term(term)
        lowered = term.lower()
        if term and lowered not in seen:
            ordered.append(term)
            seen.add(lowered)
    return ordered


def classify_tool(path: Path) -> str:
    text = str(path).lower()
    if "/.codex/" in text:
        return "codex"
    if "/.claude/" in text or "/claude/" in text:
        return "claude-code"
    if "/cursor/" in text:
        return "cursor"
    if "/opencode/" in text:
        return "opencode"
    return "unknown"


def compile_patterns(terms: list[str]) -> list[tuple[str, re.Pattern[str]]]:
    patterns: list[tuple[str, re.Pattern[str]]] = []
    for term in terms:
        escaped = re.escape(term)
        if re.search(r"[_\-\s]", term):
            pieces = [re.escape(piece) for piece in re.split(r"[_\-\s]+", term) if piece]
            if len(pieces) > 1:
                escaped = r"[_\-\s]*".join(pieces)
        patterns.append((term, re.compile(escaped, re.IGNORECASE)))
    return patterns


def excerpt(text: str, limit: int = 220) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3] + "..."


def match_terms(text: str, patterns: list[tuple[str, re.Pattern[str]]]) -> list[str]:
    matched = []
    for term, pattern in patterns:
        if pattern.search(text):
            matched.append(term)
    return matched


def is_excluded(text: str, path_text: str, exclude_patterns: list[tuple[str, re.Pattern[str]]]) -> bool:
    for _, pattern in exclude_patterns:
        if pattern.search(text) or pattern.search(path_text):
            return True
    return False


def score_terms(matched: list[str], model_terms: set[str]) -> int:
    score = len(matched)
    for term in matched:
        if term.lower() in model_terms:
            score += 3
    return score


def iter_candidate_paths(roots: list[Path]) -> Iterable[Path]:
    seen = set()
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            if root not in seen:
                seen.add(root)
                yield root
            continue
        for path in root.rglob("*"):
            if path in seen or not path.is_file():
                continue
            seen.add(path)
            yield path


def collect_strings(obj) -> list[str]:
    values: list[str] = []
    if isinstance(obj, str):
        values.append(obj)
    elif isinstance(obj, dict):
        for value in obj.values():
            values.extend(collect_strings(value))
    elif isinstance(obj, list):
        for value in obj:
            values.extend(collect_strings(value))
    return values


def search_jsonl(path: Path, patterns, model_terms, exclude_patterns) -> list[Hit]:
    hits: list[Hit] = []
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line_number, line in enumerate(handle, start=1):
            candidate_texts = [line]
            stripped = line.strip()
            if stripped.startswith("{"):
                try:
                    candidate_texts = collect_strings(json.loads(stripped)) or [line]
                except json.JSONDecodeError:
                    pass
            for text in candidate_texts:
                if is_excluded(text, str(path), exclude_patterns):
                    continue
                matched = match_terms(text, patterns)
                if not matched:
                    continue
                hits.append(
                    Hit(
                        tool=classify_tool(path),
                        path=str(path),
                        location=f"line {line_number}",
                        score=score_terms(matched, model_terms),
                        excerpt=excerpt(text),
                        matched_terms=matched,
                    )
                )
                break
    return hits


def search_text(path: Path, patterns, model_terms, exclude_patterns) -> list[Hit]:
    hits: list[Hit] = []
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line_number, line in enumerate(handle, start=1):
            if is_excluded(line, str(path), exclude_patterns):
                continue
            matched = match_terms(line, patterns)
            if not matched:
                continue
            hits.append(
                Hit(
                    tool=classify_tool(path),
                    path=str(path),
                    location=f"line {line_number}",
                    score=score_terms(matched, model_terms),
                    excerpt=excerpt(line),
                    matched_terms=matched,
                )
            )
    return hits


def sqlite_tables(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    ).fetchall()
    return [row[0] for row in rows]


def sqlite_text_columns(conn: sqlite3.Connection, table: str) -> list[str]:
    escaped_table = table.replace('"', '""')
    cols: list[str] = []
    for row in conn.execute(f'PRAGMA table_info("{escaped_table}")'):
        col_name = row[1]
        col_type = (row[2] or "").upper()
        if any(token in col_type for token in ("CHAR", "CLOB", "TEXT")) or col_type == "":
            cols.append(col_name)
    return cols


def search_sqlite(path: Path, patterns, model_terms, limit: int, exclude_patterns) -> list[Hit]:
    hits: list[Hit] = []
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    except sqlite3.Error:
        return hits
    try:
        for table in sqlite_tables(conn):
            columns = sqlite_text_columns(conn, table)
            if not columns:
                continue
            escaped_table = table.replace('"', '""')
            select_cols = ", ".join(f'"{column}"' for column in columns)
            where_sql = " OR ".join(
                f'LOWER(COALESCE("{column}", "")) LIKE ?' for column in columns
            )
            for term, _ in patterns:
                like = f"%{term.lower()}%"
                sql = f'SELECT rowid, {select_cols} FROM "{escaped_table}" WHERE {where_sql} LIMIT {limit}'
                params = [like] * len(columns)
                try:
                    rows = conn.execute(sql, params).fetchall()
                except sqlite3.Error:
                    continue
                for row in rows:
                    rowid = row[0]
                    values = [value for value in row[1:] if isinstance(value, str)]
                    text = " | ".join(values)
                    if is_excluded(text, str(path), exclude_patterns):
                        continue
                    matched = match_terms(text, patterns)
                    if not matched:
                        continue
                    hits.append(
                        Hit(
                            tool=classify_tool(path),
                            path=str(path),
                            location=f"table {table}, rowid {rowid}",
                            score=score_terms(matched, model_terms),
                            excerpt=excerpt(text),
                            matched_terms=matched,
                        )
                    )
    finally:
        conn.close()
    return hits


def dedupe_hits(hits: list[Hit]) -> list[Hit]:
    merged: dict[tuple[str, str, str], Hit] = {}
    for hit in hits:
        key = (hit.path, hit.location, hit.excerpt)
        current = merged.get(key)
        if current is None:
            merged[key] = hit
            continue
        current.score = max(current.score, hit.score)
        current.matched_terms = sorted(set(current.matched_terms) | set(hit.matched_terms))
    return list(merged.values())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="target model or repo name")
    parser.add_argument(
        "--stage",
        action="append",
        default=[],
        help="history focus: adapt,optimize; comma-separated or repeatable",
    )
    parser.add_argument(
        "--keyword",
        action="append",
        default=[],
        help="extra keyword, repeatable",
    )
    parser.add_argument(
        "--root",
        action="append",
        default=[],
        help="extra file or directory to search",
    )
    parser.add_argument(
        "--exclude-term",
        action="append",
        default=[],
        help="exclude hits containing these terms; repeatable",
    )
    parser.add_argument(
        "--tool",
        action="append",
        default=[],
        help="limit search to selected tools; comma-separated or repeatable",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=50,
        help="maximum hits to print",
    )
    parser.add_argument(
        "--output",
        choices=["text", "markdown", "json"],
        default="text",
        help="output format",
    )
    parser.add_argument(
        "--no-sqlite",
        action="store_true",
        help="skip sqlite sources",
    )
    return parser.parse_args()


def default_roots(selected_tools: list[str]) -> list[Path]:
    tools = selected_tools or list(TOOL_PATHS)
    roots = []
    for tool in tools:
        for raw in TOOL_PATHS[tool]:
            roots.append(Path(os.path.expanduser(raw)))
    return roots


def print_text(hits: list[Hit]) -> None:
    if not hits:
        print("No hits found.")
        return
    for idx, hit in enumerate(hits, start=1):
        print(f"[{idx}] tool={hit.tool} score={hit.score} {hit.path} ({hit.location})")
        print(f"    matched: {', '.join(hit.matched_terms)}")
        print(f"    excerpt: {hit.excerpt}")


def print_markdown(hits: list[Hit]) -> None:
    print("# History Hits")
    print()
    if not hits:
        print("No hits found.")
        return
    for idx, hit in enumerate(hits, start=1):
        print(f"## {idx}. {hit.tool} | score={hit.score}")
        print()
        print(f"- path: `{hit.path}`")
        print(f"- location: `{hit.location}`")
        print(f"- matched: `{', '.join(hit.matched_terms)}`")
        print(f"- excerpt: {hit.excerpt}")
        print()


def print_json(hits: list[Hit]) -> None:
    print(json.dumps([hit.__dict__ for hit in hits], ensure_ascii=False, indent=2))


def main() -> int:
    args = parse_args()
    stages = split_csv_args(args.stage) or ["adapt", "optimize"]
    invalid_stages = [stage for stage in stages if stage not in DEFAULT_STAGE_TERMS]
    if invalid_stages:
        raise SystemExit(f"Unknown stage(s): {', '.join(sorted(set(invalid_stages)))}")

    tools = split_csv_args(args.tool)
    invalid_tools = [tool for tool in tools if tool not in TOOL_PATHS]
    if invalid_tools:
        raise SystemExit(f"Unknown tool(s): {', '.join(sorted(set(invalid_tools)))}")

    terms = build_terms(args.model, stages, args.keyword)
    patterns = compile_patterns(terms)
    exclude_patterns = compile_patterns(DEFAULT_EXCLUDE_TERMS + args.exclude_term)
    model_terms = {term.lower() for term in build_model_terms(args.model)}
    roots = default_roots(tools)
    roots.extend(Path(os.path.expanduser(root)) for root in args.root)

    hits: list[Hit] = []
    for path in iter_candidate_paths(roots):
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size > MAX_FILE_SIZE:
            continue
        suffix = path.suffix.lower()
        if suffix in {".sqlite", ".db"}:
            if args.no_sqlite:
                continue
            hits.extend(search_sqlite(path, patterns, model_terms, args.max_results, exclude_patterns))
            continue
        if suffix and suffix not in TEXT_SUFFIXES:
            continue
        if suffix == ".jsonl":
            hits.extend(search_jsonl(path, patterns, model_terms, exclude_patterns))
        else:
            hits.extend(search_text(path, patterns, model_terms, exclude_patterns))

    hits = dedupe_hits(hits)
    hits.sort(key=lambda item: (-item.score, item.path, item.location))
    hits = hits[: args.max_results]

    if args.output == "markdown":
        print_markdown(hits)
    elif args.output == "json":
        print_json(hits)
    else:
        print_text(hits)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
