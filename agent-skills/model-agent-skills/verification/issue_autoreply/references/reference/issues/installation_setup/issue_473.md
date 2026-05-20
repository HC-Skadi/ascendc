# Issue #473: [Installation]: Fail to install vllm ascend from source due to numpy VersionConflict (CANN required numpy < 2.0.0)

## 基本信息

- **编号**: #473
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/473
- **创建时间**: 2025-04-07T01:36:42Z
- **关闭时间**: 2025-04-07T08:07:22Z
- **更新时间**: 2026-03-02T09:00:36Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

```bash
export IMAGE=m.daocloud.io/quay.io/ascend/cann:8.0.0-910b-ubuntu22.04-py3.10
# export IMAGE=quay.io/ascend/cann:8.0.0-910b-ubuntu22.04-py3.10

docker run --rm \
--name vllm-ascend \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash
```


### How you are installing vllm and vllm-ascend

```bash
pip install vllm==0.8.3
git clone  --depth 1 --branch main  https://gitee.com/mirrors/vllm-ascend
```

```
# pip install -e . --extra-index https://download.pytorch.org/whl/cpu/
Looking in indexes: https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple, https://download.pytorch.org/whl/cpu/
Obtaining file:///root/vllm-ascend
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
ERROR: Exception:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/cli/base_command.py", line 106, in _run_wrapper
    status = _inner_run()
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/cli/base_command.py", line 97, in _inner_run
    return self.run(options, args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/cli/req_command.py", line 67, in wrapper
    return func(self, options, args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/commands/install.py", line 386, in run
    requirement_set = resolver.resolve(
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 76, in resolve
    collected = self.factory.collect_root_requirements(root_reqs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 545, in collect_root_requirements
    reqs = list(
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 501, in _make_requirements_from_install_req
    cand = self._make_base_candidate_from_link(
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 212, in _make_base_candidate_from_link
    self._editable_candidate_cache[link] = EditableCandidate(
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 329, in __init__
    super().__init__(
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 159, in __init__
    self.dist = self._prepare()
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 236, in _prepare
    dist = self._prepare_distribution()
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 339, in _prepare_distribution
    return self._factory.preparer.prepare_editable_requirement(self._ireq)
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/operations/prepare.py", line 706, in prepare_editable_requirement
    req.check_if_exists(self.use_user_site)
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/req/req_install.py", line 434, in check_if_exists
    existing_dist = get_default_environment().get_distribution(self.req.name)
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_internal/metadata/pkg_resources.py", line 298, in get_distribution
    self._ws.require(name)
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1061, in require
    needed = self.resolve(parse_requirements(requirements))
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_vendor/pkg_resources/__init__.py", line 888, in resolve
    dist = self._resolve_dist(
  File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_vendor/pkg_resources/__init__.py", line 934, in _resolve_dist
    raise VersionConflict(dist, req).with_context(dependent_req)
pip._vendor.pkg_resources.ContextualVersionConflict: (numpy 2.2.4 (/usr/local/python3.10/lib/python3.10/site-packages), Requirement.parse('numpy==1.26.4'), {'vllm-ascend'})
```
