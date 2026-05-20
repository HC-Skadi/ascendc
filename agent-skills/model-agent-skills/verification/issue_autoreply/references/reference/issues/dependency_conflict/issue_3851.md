# Issue #3851: [Bug]: Run Qwen3-VL-8B-Instruct failed, No module named 'vllm.utils.torch_utils'

## 基本信息

- **编号**: #3851
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3851
- **创建时间**: 2025-10-29T02:50:13Z
- **关闭时间**: 2025-10-29T03:03:33Z
- **更新时间**: 2026-02-09T09:34:52Z
- **提交者**: @shen-shanshan
- **评论数**: 3

## 标签

bug; module:multimodal

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm: 17c540a993af88204ad1b78345c8a865cf58ce44
vllm-ascend: main
```

</details>


### 🐛 Describe the bug

Run:

```bash
vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen3-VL-8B-Instruct \
--max_model_len 16384 \
--tensor-parallel-size 2 \
--enforce-eager
```

Get failure:

```bash
Traceback (most recent call last):
  File "/root/miniconda3/envs/vllm/bin/vllm", line 7, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 66, in main
    cmd.subparser_init(subparsers).set_defaults(dispatch_function=cmd.cmd)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 74, in subparser_init
    serve_parser = make_arg_parser(serve_parser)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/cli_args.py", line 273, in make_arg_parser
    parser = AsyncEngineArgs.add_cli_args(parser)
  File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1905, in add_cli_args
    current_platform.pre_register_and_update(parser)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 69, in pre_register_and_update
    adapt_patch(is_global_patch=True)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/utils.py", line 274, in adapt_patch
    from vllm_ascend.patch import platform  # noqa: F401
  File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/__init__.py", line 21, in <module>
    import vllm_ascend.patch.platform.patch_mamba_config  # noqa
  File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_mamba_config.py", line 14, in <module>
    from vllm.utils.torch_utils import STR_DTYPE_TO_TORCH_DTYPE
ModuleNotFoundError: No module named 'vllm.utils.torch_utils'
```
