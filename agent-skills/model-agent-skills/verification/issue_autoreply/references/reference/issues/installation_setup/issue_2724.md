# Issue #2724: [Doc]: Translate doc

## 基本信息

- **编号**: #2724
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2724
- **创建时间**: 2025-09-03T08:05:49Z
- **关闭时间**: 2025-09-19T13:22:31Z
- **更新时间**: 2025-09-19T13:22:31Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

documentation

## 问题描述

### 📚 The doc issue

https://vllm-ascend.readthedocs.io/zh-cn/v0.9.1-dev/tutorials/large_scale_ep.html

https://vllm-ascend.readthedocs.io/zh-cn/v0.9.1-dev/developer_guide/performance/optimization_and_tuning.html

### Suggest a potential alternative/fix

_No response_

```
cd docs
python -m venv ./.venv
source .venv
# Install dependencies.
pip install -r requirements-docs.txt
# Build the docs.
make clean
make html

# Extract po files
make po

# Do translations

# Build the docs with translation
make intl

# Open the docs with your browser
python -m http.server -d _build/html/
```
