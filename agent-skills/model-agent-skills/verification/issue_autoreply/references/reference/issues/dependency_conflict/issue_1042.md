# Issue #1042: [Bug][main]: vllm (main) serve failed due to quantization choice haven't init

## 基本信息

- **编号**: #1042
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1042
- **创建时间**: 2025-06-01T14:26:16Z
- **关闭时间**: 2025-06-03T08:22:57Z
- **更新时间**: 2025-06-03T08:23:12Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

```
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/entrypoints/cli/main.py", line 50, in main
    cmd.subparser_init(subparsers).set_defaults(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/entrypoints/cli/serve.py", line 101, in subparser_init
    serve_parser = make_arg_parser(serve_parser)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/entrypoints/openai/cli_args.py", line 246, in make_arg_parser
    parser = AsyncEngineArgs.add_cli_args(parser)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/engine/arg_utils.py", line 1[57](https://github.com/vllm-project/vllm-ascend/actions/runs/15357519122/job/43219462384#step:10:58)4, in add_cli_args
    current_platform.pre_register_and_update(parser)
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/platform.py", line 79, in pre_register_and_update
    if ASCEND_QUATIZATION_METHOD not in quant_action.choices:
TypeError: argument of type 'NoneType' is not iterable
```

https://github.com/vllm-project/vllm-ascend/actions/runs/15357519122/job/43219462384
