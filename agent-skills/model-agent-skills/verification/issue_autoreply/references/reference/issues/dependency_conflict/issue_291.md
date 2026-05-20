# Issue #291: [Bug]: vllm-ascend:v0.7.3-dev部署DeepSeek-R1-Distill-Qwen-32B报错

## 基本信息

- **编号**: #291
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/291
- **创建时间**: 2025-03-11T02:50:36Z
- **关闭时间**: 2025-03-12T01:39:43Z
- **更新时间**: 2025-03-12T01:40:10Z
- **提交者**: @jxz542189
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

使用quay.io/ascend/vllm-ascend:v0.7.3-dev镜像部署DeepSeek-R1-Distill-Qwen-32B，会报如下错误：
INFO 03-11 02:47:04 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-11 02:47:04 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-11 02:47:04 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-11 02:47:04 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-11 02:47:04 __init__.py:44] plugin ascend loaded.
INFO 03-11 02:47:04 __init__.py:198] Platform plugin ascend is activated
INFO 03-11 02:47:04 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 03-11 02:47:04 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 03-11 02:47:04 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 03-11 02:47:04 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-11 02:47:04 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 03-11 02:47:04 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 65, in main
    cmd.subparser_init(subparsers).set_defaults(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 59, in subparser_init
    return make_arg_parser(serve_parser)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/cli_args.py", line 252, in make_arg_parser
    parser = AsyncEngineArgs.add_cli_args(parser)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1412, in add_cli_args
    load_general_plugins()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/plugins/__init__.py", line 82, in load_general_plugins
    func()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/__init__.py", line 28, in register_model
    register_model()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/models/__init__.py", line 5, in register_model
    from .qwen2_vl import CustomQwen2VLForConditionalGeneration  # noqa: F401
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/models/qwen2_vl.py", line 32, in <module>
    from vllm.model_executor.models.qwen2_vl import (
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 52, in <module>
    from vllm.model_executor.layers.quantization.gptq_marlin import (
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/gptq_marlin.py", line 7, in <module>
    import vllm.model_executor.layers.fused_moe  # noqa
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/__init__.py", line 36, in <module>
    import vllm.model_executor.layers.fused_moe.fused_marlin_moe  # noqa
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/fused_marlin_moe.py", line 8, in <module>
    from vllm.model_executor.layers.fused_moe.fused_moe import (
ImportError: cannot import name 'fused_topk' from 'fused_moe_module' (unknown location)
[ERROR] 2025-03-11-02:47:04 (PID:1031, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

### 🐛 Describe the bug

这个错误ImportError: cannot import name 'fused_topk' from 'fused_moe_module' (unknown location)，感觉是vllm不支持
