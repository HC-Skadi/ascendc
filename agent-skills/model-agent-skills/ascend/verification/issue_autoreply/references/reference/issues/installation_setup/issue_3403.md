# Issue #3403: [Installation]: Fatal Error installing vllm_ascend 0.10.2rc1

## 基本信息

- **编号**: #3403
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3403
- **创建时间**: 2025-10-13T03:43:21Z
- **关闭时间**: 2025-10-14T10:02:09Z
- **更新时间**: 2025-10-29T02:03:51Z
- **提交者**: @yxh-y
- **评论数**: 1

## 标签

installation

## 问题描述

### Your current environment

python collect_env.py
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 93.1        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3418 / 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 92.2        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 93.1        34                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 91.8        35                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3402 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 94.5        36                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 94.3        37                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 93.5        35                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 94.0        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3404 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux

INFO 10-13 03:39:35 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 10-13 03:39:35 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 10-13 03:39:35 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 10-13 03:39:35 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
ERROR 10-13 03:39:35 [__init__.py:46] Failed to load plugin ascend
ERROR 10-13 03:39:35 [__init__.py:46] Traceback (most recent call last):
ERROR 10-13 03:39:35 [__init__.py:46]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/plugins/__init__.py", line 42, in load_plugins_by_group
ERROR 10-13 03:39:35 [__init__.py:46]     func = plugin.load()
ERROR 10-13 03:39:35 [__init__.py:46]   File "/usr/local/python3.10.17/lib/python3.10/importlib/metadata/__init__.py", line 173, in load
ERROR 10-13 03:39:35 [__init__.py:46]     return functools.reduce(getattr, attrs, module)
ERROR 10-13 03:39:35 [__init__.py:46] AttributeError: module 'vllm_ascend' has no attribute 'register'
INFO 10-13 03:39:35 [__init__.py:243] No platform detected, vLLM is running on UnspecifiedPlatform
Collecting environment information...
Traceback (most recent call last):
  File "/kos_turbo/yuxiaohan/collect_env.py", line 489, in <module>
    main()
  File "/kos_turbo/yuxiaohan/collect_env.py", line 468, in main
    output = get_pretty_env_info()
  File "/kos_turbo/yuxiaohan/collect_env.py", line 463, in get_pretty_env_info
    return pretty_str(get_env_info())
  File "/kos_turbo/yuxiaohan/collect_env.py", line 353, in get_env_info
    vllm_ascend_version=get_vllm_ascend_version(),
  File "/kos_turbo/yuxiaohan/collect_env.py", line 174, in get_vllm_ascend_version
    from vllm_ascend._version import __version__, __version_tuple__
ModuleNotFoundError: No module named 'vllm_ascend._version'
[ERROR] 2025-10-13-03:39:38 (PID:149649, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

### How you are installing vllm and vllm-ascend

```
pip install vllm==0.9.1

manually install torch-npu via whl in https://mirrors.huaweicloud.com/ascend/repos/pypi/torch-npu/
pip install torch_npu-2.7.1.dev20250724-cp310-cp310-manylinux_2_28_aarch64.whl

download vllm_ascend 0.10.rc2
comment the torch-npu in requirements.txt and pyproject
execute pip install -v -e .
```


Have fatal error:
/xxxxxxx/vllm_ascend/vllm-ascend-0.10.2rc1/csrc/torch_binding.cpp:20:10: fatal error: torch_npu/csrc/core/npu/NPUStream.h: No such file or directory
     20 | #include <torch_npu/csrc/core/npu/NPUStream.h>
        |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  compilation terminated.
  gmake[3]: *** [CMakeFiles/vllm_ascend_C.dir/build.make:93: CMakeFiles/vllm_ascend_C.dir/csrc/torch_binding.cpp.o] Error 1
  gmake[3]: *** Waiting for unfinished jobs....
  /xxxxxx/vllm_ascend/vllm-ascend-0.10.2rc1/csrc/torch_binding_meta.cpp:4:10: fatal error: torch_npu/csrc/core/npu/NPUStream.h: No such file or directory
      4 | #include <torch_npu/csrc/core/npu/NPUStream.h>
        |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  compilation terminated.
  gmake[3]: *** [CMakeFiles/vllm_ascend_C.dir/build.make:107: CMakeFiles/vllm_ascend_C.dir/csrc/torch_binding_meta.cpp.o] Error 1
  gmake[2]: *** [CMakeFiles/Makefile2:405: CMakeFiles/vllm_ascend_C.dir/all] Error 2
  gmake[1]: *** [CMakeFiles/Makefile2:412: CMakeFiles/vllm_ascend_C.dir/rule] Error 2
  gmake: *** [Makefile:286: vllm_ascend_C] Error 2
  Traceback (most recent call last):
    File "/usr/local/python3.10.17/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
      main()
    File "/usr/local/python3.10.17/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
      json_out["return_val"] = hook(**hook_input["kwargs"])
    File "/usr/local/python3.10.17/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 303, in build_editable
      return hook(wheel_directory, config_settings, metadata_directory)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 468, in build_editable
      return self._build_with_temp_dir(
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 404, in _build_with_temp_dir
      self.run_setup()
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 317, in run_setup
      exec(code, locals())
    File "<string>", line 360, in <module>
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/__init__.py", line 115, in setup
      return distutils.core.setup(**attrs)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 186, in setup
      return run_commands(dist)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 202, in run_commands
      dist.run_commands()
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1002, in run_commands
      self.run_command(cmd)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1102, in run_command
      super().run_command(command)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
      cmd_obj.run()
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/command/editable_wheel.py", line 139, in run
      self._create_wheel_file(bdist_wheel)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/command/editable_wheel.py", line 349, in _create_wheel_file
      files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/command/editable_wheel.py", line 272, in _run_build_commands
      self._run_build_subcommands()
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/command/editable_wheel.py", line 299, in _run_build_subcommands
      self.run_command(name)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
      self.distribution.run_command(command)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1102, in run_command
      super().run_command(command)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
      cmd_obj.run()
    File "<string>", line 294, in run
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/command/build_ext.py", line 96, in run
      _build_ext.run(self)
    File "/tmp/pip-build-env-0a5ggcky/overlay/lib/python3.10/site-packages/setuptools/_distutils/command/build_ext.py", line 368, in run
      self.build_extensions()
    File "<string>", line 266, in build_extensions
    File "/usr/local/python3.10.17/lib/python3.10/subprocess.py", line 369, in check_call
      raise CalledProcessError(retcode, cmd)
  subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=181', '--target=vllm_ascend_C']' returned non-zero exit status 2.
  error: subprocess-exited-with-error
  
  × Building editable for vllm_ascend (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> See above for output.
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  full command: /usr/local/python3.10.17/bin/python3.10 /usr/local/python3.10.17/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py build_editable /tmp/tmp3xuvrxtt
  cwd: /kos_turbo/yuxiaohan/vllm_ascend/vllm-ascend-0.10.2rc1
  Building editable for vllm_ascend (pyproject.toml) ... error
  ERROR: Failed building editable for vllm_ascend
Failed to build vllm_ascend

[notice] A new release of pip is available: 25.1.1 -> 25.2
[notice] To update, run: pip install --upgrade pip
ERROR: Failed to build installable wheels for some pyproject.toml based projects (vllm_ascend)



