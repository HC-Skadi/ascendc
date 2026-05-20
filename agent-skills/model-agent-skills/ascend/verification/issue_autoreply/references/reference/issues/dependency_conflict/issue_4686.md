# Issue #4686: [Bug]: Upstream CI failed due to SOC_VERSION detect failure

## 基本信息

- **编号**: #4686
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4686
- **创建时间**: 2025-12-04T01:22:29Z
- **关闭时间**: 2025-12-08T13:41:26Z
- **更新时间**: 2025-12-09T00:02:28Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug; high

## 问题描述

### Your current environment

```
#17 107.9   Traceback (most recent call last):
--
#17 107.9     File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
#17 107.9       main()
#17 107.9     File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
#17 107.9       json_out["return_val"] = hook(**hook_input["kwargs"])
#17 107.9                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#17 107.9     File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 157, in get_requires_for_build_editable
#17 107.9       return hook(config_settings)
#17 107.9              ^^^^^^^^^^^^^^^^^^^^^
#17 107.9     File "/tmp/pip-build-env-o62ag382/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 473, in get_requires_for_build_editable
#17 107.9       return self.get_requires_for_build_wheel(config_settings)
#17 107.9              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#17 107.9     File "/tmp/pip-build-env-o62ag382/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 331, in get_requires_for_build_wheel
#17 107.9       return self._get_build_requires(config_settings, requirements=[])
#17 107.9              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#17 107.9     File "/tmp/pip-build-env-o62ag382/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 301, in _get_build_requires
#17 107.9       self.run_setup()
#17 107.9     File "/tmp/pip-build-env-o62ag382/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 317, in run_setup
#17 107.9       exec(code, locals())
#17 107.9     File "<string>", line 122, in <module>
#17 107.9   RuntimeError: Could not determine chip type automatically via 'npu-smi'. This can happen in a CPU-only environment. Please set the 'SOC_VERSION' environment variable to specify the target chip.
#17 107.9   error: subprocess-exited-with-error
#17 107.9
#17 107.9   × Getting requirements to build editable did not run successfully.
#17 107.9   │ exit code: 1
#17 107.9   ╰─> No available output.
#17 107.9
#17 107.9   note: This error originates from a subprocess, and is likely not a problem with pip.
#17 107.9   full command: /usr/local/python3.11.13/bin/python3 /usr/local/python3.11.13/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py get_requires_for_build_editable /tmp/tmpuo1cj4d9
#17 107.9   cwd: /workspace/vllm-ascend
#17 107.9   Getting requirements to build editable: finished with status 'error'
#17 107.9 ERROR: Failed to build 'file:///workspace/vllm-ascend' when getting requirements to build editable
#17 ERROR: process "/bin/bash -c export PIP_EXTRA_INDEX_URL=https://mirrors.huaweicloud.com/ascend/repos/pypi &&     source /usr/local/Ascend/ascend-toolkit/set_env.sh &&     source /usr/local/Ascend/nnal/atb/set_env.sh &&     export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib &&     python3 -m pip install -v -e /workspace/vllm-ascend/ --extra-index https://download.pytorch.org/whl/cpu/" did not complete successfully: exit code: 1
------
> [stage-0 12/13] RUN --mount=type=cache,target=/root/.cache/pip     export PIP_EXTRA_INDEX_URL=https://mirrors.huaweicloud.com/ascend/repos/pypi &&     source /usr/local/Ascend/ascend-toolkit/set_env.sh &&     source /usr/local/Ascend/nnal/atb/set_env.sh &&     export LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/::/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib &&     python3 -m pip install -v -e /workspace/vllm-ascend/ --extra-index https://download.pytorch.org/whl/cpu/:
107.9
107.9   × Getting requirements to build editable did not run successfully.
107.9   │ exit code: 1
107.9   ╰─> No available output.
107.9
107.9   note: This error originates from a subprocess, and is likely not a problem with pip.
107.9   full command: /usr/local/python3.11.13/bin/python3 /usr/local/python3.11.13/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py get_requires_for_build_editable /tmp/tmpuo1cj4d9
107.9   cwd: /workspace/vllm-ascend
107.9   Getting requirements to build editable: finished with status 'error'
107.9 ERROR: Failed to build 'file:///workspace/vllm-ascend' when getting requirements to build editable
```

### 🐛 Describe the bug

https://buildkite.com/vllm/ci/builds/41831#019ae6e3-1f66-4f36-8ca6-e5705187cfd1
