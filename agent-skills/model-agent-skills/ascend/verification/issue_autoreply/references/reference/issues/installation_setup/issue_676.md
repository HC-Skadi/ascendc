# Issue #676: [Installation]: 安装 vllm-ascend v0.8.4rc1 编译失败

## 基本信息

- **编号**: #676
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/676
- **创建时间**: 2025-04-27T08:18:24Z
- **关闭时间**: 2025-04-29T01:51:39Z
- **更新时间**: 2025-09-04T06:36:46Z
- **提交者**: @rfy48
- **评论数**: 22

## 标签

installation

## 问题描述

### Your current environment

```text
The output of `python collect_env.py`
```
vllm                                     0.8.4+empty
torch                                   2.5.1+cpu
torch-npu                           2.5.1.dev20250320

### How you are installing vllm and vllm-ascend

```sh
# Install vLLM Ascend
git clone  --depth 1 --branch v0.8.4rc1 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
python setup.py develop
cd ..
```


gmake[3]: *** [CMakeFiles/vllm_ascend_C.dir/build.make:90: CMakeFiles/vllm_ascend_C.dir/csrc/torch_binding.cpp.o] Error 1
gmake[2]: *** [CMakeFiles/Makefile2:337: CMakeFiles/vllm_ascend_C.dir/all] Error 2
gmake[1]: *** [CMakeFiles/Makefile2:344: CMakeFiles/vllm_ascend_C.dir/rule] Error 2
gmake: *** [Makefile:286: vllm_ascend_C] Error 2
Traceback (most recent call last):
  File "/mnt/deepseek/renfeiyang/vllm-test-250427/vllm-ascend-250427/setup.py", line 331, in <module>
    setup(
  File "/usr/lib/python3.11/site-packages/setuptools/__init__.py", line 107, in setup
    return distutils.core.setup(**attrs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 185, in setup
    return run_commands(dist)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 201, in run_commands
    dist.run_commands()
  File "/usr/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 969, in run_commands
    self.run_command(cmd)
  File "/usr/lib/python3.11/site-packages/setuptools/dist.py", line 1234, in run_command
    super().run_command(command)
  File "/usr/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
    cmd_obj.run()
  File "/usr/lib/python3.11/site-packages/setuptools/command/develop.py", line 34, in run
    self.install_for_development()
  File "/usr/lib/python3.11/site-packages/setuptools/command/develop.py", line 111, in install_for_development
    self.run_command('build_ext')
  File "/usr/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 318, in run_command
    self.distribution.run_command(command)
  File "/usr/lib/python3.11/site-packages/setuptools/dist.py", line 1234, in run_command
    super().run_command(command)
  File "/usr/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
    cmd_obj.run()
  File "/mnt/deepseek/renfeiyang/vllm-test-250427/vllm-ascend-250427/setup.py", line 269, in run
    super().run()
  File "/usr/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 84, in run
    _build_ext.run(self)
  File "/usr/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 345, in run
    self.build_extensions()
  File "/mnt/deepseek/renfeiyang/vllm-test-250427/vllm-ascend-250427/setup.py", line 241, in build_extensions
    subprocess.check_call(["cmake", *build_args], cwd=self.build_temp)
  File "/usr/lib64/python3.11/subprocess.py", line 413, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=192', '--target=vllm_ascend_C']' returned non-zero exit status 2.


![Image](https://github.com/user-attachments/assets/f2d8f69f-e29a-4d8d-b827-6a2efce6b411)

