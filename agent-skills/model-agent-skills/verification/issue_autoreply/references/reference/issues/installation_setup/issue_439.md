# Issue #439: [Doc]: Failed to install vllm on ascend enviroment

## 基本信息

- **编号**: #439
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/439
- **创建时间**: 2025-03-31T04:45:31Z
- **关闭时间**: 2025-03-31T06:17:57Z
- **更新时间**: 2025-03-31T06:17:57Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

documentation

## 问题描述

### 📚 The doc issue

```
      running build_ext
      -- The CXX compiler identification is unknown
      CMake Error at CMakeLists.txt:14 (project):
        No CMAKE_CXX_COMPILER could be found.

        Tell CMake where to find the compiler by setting either the environment
        variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
        to the compiler, or to the compiler name if it is in the PATH.


      -- Configuring incomplete, errors occurred!
      Traceback (most recent call last):
        File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
          main()
        File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
        File "/usr/local/python3.10/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 280, in build_wheel
          return _build_backend().build_wheel(
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 438, in build_wheel
          return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 426, in _build
          return self._build_with_temp_dir(
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 407, in _build_with_temp_dir
          self.run_setup()
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
        File "<string>", line 639, in <module>
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/__init__.py", line 117, in setup
          return distutils.core.setup(**attrs)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 186, in setup
          return run_commands(dist)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 202, in run_commands
          dist.run_commands()
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1002, in run_commands
          self.run_command(cmd)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1104, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/command/bdist_wheel.py", line 370, in run
          self.run_command("build")
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1104, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/command/build.py", line 135, in run
          self.run_command(cmd_name)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1104, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "<string>", line 255, in run
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/command/build_ext.py", line 99, in run
          _build_ext.run(self)
        File "/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_distutils/command/build_ext.py", line 368, in run
          self.build_extensions()
        File "<string>", line 214, in build_extensions
        File "<string>", line 192, in configure
        File "/usr/local/python3.10/lib/python3.10/subprocess.py", line 369, in check_call
          raise CalledProcessError(retcode, cmd)
      subprocess.CalledProcessError: Command '['cmake', '/tmp/pip-install-zt5aw0ox/vllm_2f0c32fd77a1483792f88e927d1f1e33', '-G', 'Ninja', '-DCMAKE_BUILD_TYPE=RelWithDebInfo', '-DVLLM_TARGET_DEVICE=cpu', '-DVLLM_PYTHON_EXECUTABLE=/usr/local/python3.10/bin/python3.10', '-DVLLM_PYTHON_PATH=/tmp/pip-build-env-ae3seyx3/site:/usr/local/python3.10/lib/python310.zip:/usr/local/python3.10/lib/python3.10:/usr/local/python3.10/lib/python3.10/lib-dynload:/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages:/tmp/pip-build-env-ae3seyx3/normal/lib/python3.10/site-packages:/tmp/pip-build-env-ae3seyx3/overlay/lib/python3.10/site-packages/setuptools/_vendor', '-DFETCHCONTENT_BASE_DIR=/tmp/pip-install-zt5aw0ox/vllm_2f0c32fd77a1483792f88e927d1f1e33/.deps', '-DCMAKE_JOB_POOL_COMPILE:STRING=compile', '-DCMAKE_JOB_POOLS:STRING=compile=192']' returned non-zero exit status 1.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for vllm
Failed to build vllm
ERROR: Failed to build installable wheels for some pyproject.toml based projects (vllm)
```

### Suggest a potential alternative/fix

_No response_
