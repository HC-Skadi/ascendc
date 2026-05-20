# Issue #431: [Bug]: logger.info() is invalid.

## 基本信息

- **编号**: #431
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/431
- **创建时间**: 2025-03-29T07:58:46Z
- **关闭时间**: 2025-04-15T02:18:07Z
- **更新时间**: 2025-04-15T02:18:07Z
- **提交者**: @shen-shanshan
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

When I use `logger` like this:

```bash
from vllm.logger import init_logger

logger = init_logger(__name__)

# ...
logger.info("xxx")
# ...
```

This message is not printed in the terminal. I think maybe there is something wrong with the log config?
