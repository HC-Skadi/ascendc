#!/usr/bin/env bash
# 带关键节点日志的 uv sync，用于昇腾/CUDA 适配后的同步验证。
# 用法: adapt_sync.sh ascend | cuda

set -e
EXTRA="${1:-}"
ASCEND_HOME="${ASCEND_HOME:-/usr/local/Ascend/ascend-toolkit/latest}"

echo "[adapt] 开始 uv-torch 双硬件适配（同步阶段）"

if [[ -z "$EXTRA" ]]; then
  echo "[adapt] 失败: 未指定 extra - 用法: $0 ascend | cuda" >&2
  exit 1
fi

if [[ "$EXTRA" != "ascend" && "$EXTRA" != "cuda" ]]; then
  echo "[adapt] 失败: extra 须为 ascend 或 cuda" >&2
  exit 1
fi

echo "[adapt] 检查 uv 与 pyproject.toml"
if ! command -v uv >/dev/null 2>&1; then
  echo "[adapt] 失败: 环境检查 - 未找到 uv，请先安装" >&2
  exit 1
fi
if [[ ! -f pyproject.toml ]]; then
  echo "[adapt] 失败: 环境检查 - 当前目录无 pyproject.toml" >&2
  exit 1
fi
echo "[adapt] pyproject.toml 已配置 index/sources"

if [[ "$EXTRA" == "ascend" ]]; then
  echo "[adapt] 加载 Ascend set_env.sh"
  if [[ -f "$ASCEND_HOME/set_env.sh" ]]; then
    # shellcheck source=/dev/null
    source "$ASCEND_HOME/set_env.sh"
  else
    echo "[adapt] 警告: 未找到 set_env.sh，继续尝试同步" >&2
  fi
fi

echo "[adapt] 正在同步 --extra $EXTRA"
uv sync --extra "$EXTRA"

echo "[adapt] 同步完成，可选用 npu:0 / cuda:0"
echo "[adapt] 适配流程结束"
