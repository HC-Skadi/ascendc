# Issue #343: [Bug]: 麒麟系统+昇腾910B，从0.7.1rc1 升级 0.7.3rc1报错：安装vllm0.7.3报错

## 基本信息

- **编号**: #343
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/343
- **创建时间**: 2025-03-17T04:03:31Z
- **关闭时间**: 2025-03-31T15:43:50Z
- **更新时间**: 2025-03-31T15:43:50Z
- **提交者**: @yungongzi
- **评论数**: 9

## 标签

duplicate

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
OS: Kylin Linux Advanced Server V10 (Lance) (aarch64)
Python：3.11.11
NPU：910B
ROCM Version: Could not collect

VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
```

</details>


### 🐛 Describe the bug

vllm_ascend 0.7.1rc1版本通过源码安装方式可正常安装。
从新创建环境，升级到0.7.3rc1版本过程中，安装vllm0.7.3报错

安装方法：通过源码安装
```python
# Install vLLM
git clone --depth 1 --branch v0.7.3 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install . --extra-index https://download.pytorch.org/whl/cpu/
```

报错如下：
```python
Processing /data/llm_projects/vllm_new
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error
  
  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [31 lines of output]
      /tmp/pip-build-env-15sxdi4l/overlay/lib/python3.11/site-packages/torch/_subclasses/functional_tensor.py:295: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
        cpu = _conversion_method_template(device=torch.device("cpu"))
      Traceback (most recent call last):
        File "/data/miniconda3/envs/vllm_ascend_new/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
          main()
        File "/data/miniconda3/envs/vllm_ascend_new/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/data/miniconda3/envs/vllm_ascend_new/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 143, in get_requires_for_build_wheel
          return hook(config_settings)
                 ^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-15sxdi4l/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 334, in get_requires_for_build_wheel
          return self._get_build_requires(config_settings, requirements=[])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-15sxdi4l/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 304, in _get_build_requires
          self.run_setup()
        File "/tmp/pip-build-env-15sxdi4l/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 320, in run_s
etup
          exec(code, locals())
        File "<string>", line 641, in <module>
        File "<string>", line 502, in get_vllm_version
        File "/tmp/pip-build-env-15sxdi4l/overlay/lib/python3.11/site-packages/setuptools_scm/_get_version_impl.py", line 16
6, in get_version
          _version_missing(config)
        File "/tmp/pip-build-env-15sxdi4l/overlay/lib/python3.11/site-packages/setuptools_scm/_get_version_impl.py", line 11
7, in _version_missing
          raise LookupError(
      LookupError: setuptools-scm was unable to detect version for /data/llm_projects/vllm_new.
      
      Make sure you're either building from a fully intact git repository or PyPI tarballs. Most other sources (such as GitH
ub's tarballs, a git checkout without the .git folder) don't contain the necessary metadata and will not work.
      
      For example, if you're using pip, instead of https://github.com/user/proj/archive/master.zip use git+https://github.co
m/user/proj.git#egg=proj
      
      Alternatively, set the version with the environment variable SETUPTOOLS_SCM_PRETEND_VERSION_FOR_${NORMALIZED_DIST_NAME
} as described in https://setuptools-scm.readthedocs.io/en/latest/config.
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error
                                                                                                                             
× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.
                                                                                                                            
note: This error originates from a subprocess, and is likely not a problem with pip.

```
