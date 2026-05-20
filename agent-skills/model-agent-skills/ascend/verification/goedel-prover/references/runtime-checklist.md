# Goedel-Prover Runtime Checklist

## 版本与环境检查

- `torch` / `torch_npu` 使用 `2.5.1` 同口径版本。
- `vllm` 源码安装时使用 `v0.9.1`，并设置 `VLLM_TARGET_DEVICE=empty`。
- `vllm-ascend` 固定为 `0.9.1rc2`，避免和旧版 `transformers` 组合。
- `transformers` 保持在 `>=4.51.1,<4.53.0`，否则可能出现模型加载或 tokenizer 行为不一致。
- `setuptools` 必须 `< 71`，否则 `torchair` 导入时报 `No module named 'pkg_resources'`。
- `NNAL/ATB` 必须和当前 CANN 版本匹配，缺失时优先检查 `libnnal*` / `libatb*`。
  可通过 `cat /usr/local/Ascend/ascend-toolkit/latest/version.cfg` 确认 CANN 版本。

## 代码改动最小清单

- `eval/step1_inference.py` 顶部注入 `torch_npu` 和 `transfer_to_npu`。
- `eval/eval.sh` 在执行前：
  - `source /usr/local/Ascend/ascend-toolkit/set_env.sh`
  - `source <NNAL_ATB>/set_env.sh --cxx_abi=0`（路径需动态定位）
  - `source <NNAL_ASDSIP>/set_env.sh`
  - 将 `torch_npu/dynamo` 加入 `PYTHONPATH`（torchair 依赖）
- `requirements.txt` 去掉 `flash-attn`、CUDA 版 `vllm`、`vllm_nccl_cu12`。
- 所有设备选择都走 `transfer_to_npu` 自动映射，不保留 `cuda` 硬编码分支。

## Lean 4 构建检查

- `~/.elan/toolchains/leanprover--lean4---v4.9.0-rc1/bin/lean --version` 可以正常输出。
- `lake build` 前确保 `PATH` 已包含 `~/.elan/bin` 和对应 toolchain 的 `bin/`。
- `proofwidgets:optRelease` 失败通常不阻断验证，可先继续执行 verifier。

## 常见故障定位

- `ImportError: libatb.so` 或 `libnnal.so`:
  说明 NNAL/ATB 未安装或环境变量未拉起，重新检查 `set_env.sh`。
- `undefined symbol` 或 `Please check the version of the NNAL package`:
  NNAL 与 CANN 版本不匹配。先用 `cat /usr/local/Ascend/ascend-toolkit/latest/version.cfg`
  确认 CANN 版本，然后前往昇腾社区下载对应版本的 NNAL 包重新安装。
  也可能是 CXX ABI 不匹配（torch 2.5.1 使用 ABI=0，但 `set_env.sh` 误选了 `cxx_abi_1`），
  此时显式传入 `--cxx_abi=0` 或确保先激活 conda 环境再 source `set_env.sh`。
- `No module named 'torchair'`:
  `torchair` 打包在 `torch_npu/dynamo/torchair/` 目录下，需要将 `torch_npu/dynamo`
  加入 `PYTHONPATH`。
- `No module named 'pkg_resources'`:
  `setuptools >= 71` 已移除 `pkg_resources`，需要 `pip install 'setuptools<71'`。
- `No module named vllm_ascend`:
  通常是 `vllm-ascend` 未安装到当前 conda 环境，或被后续 `pip install -r requirements.txt` 覆盖。
- `torch.cuda` 相关报错仍出现:
  说明入口文件没有尽早导入 `transfer_to_npu`，或仍有业务代码显式判断 `cuda`。
- `lake build` 下载失败:
  网络受限场景下改为手动下载 Lean 4 toolchain 并解压到 `~/.elan/toolchains/`。
- `accuracy` 不是 `100.00`:
  先检查 `ASCEND_RT_VISIBLE_DEVICES`、`-g` tensor parallel 卡数、模型路径和数据集 JSONL 是否一致。

## 建议验证顺序

1. 先跑 `python prover/lean/verifier.py`，确认 Lean 4 运行时可用。
2. 再用单题 `mathd_algebra_338.jsonl` 走完整评测链路。
3. 最后再扩到 `minif2f` 全量评测，保留 `results/.../compilation_summarize.json` 作为验收依据。
