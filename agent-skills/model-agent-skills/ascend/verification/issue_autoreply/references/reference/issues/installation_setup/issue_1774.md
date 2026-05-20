# Issue #1774: [Installation]: 安装 vllm-ascend v0.7.3.post1 编译失败

## 基本信息

- **编号**: #1774
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1774
- **创建时间**: 2025-07-14T06:57:36Z
- **关闭时间**: 2025-07-18T00:27:42Z
- **更新时间**: 2025-07-18T00:27:42Z
- **提交者**: @1170300714
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

```text
git clone -b v0.7.3.post1 --depth 1 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
export COMPILE_CUSTOM_KERNELS=1
python setup.py install
```

编译时报错信息如下：

```text
[ 77%] No install step for 'vllm_ascend_kernels_aiv_device'
[ 80%] Completed 'vllm_ascend_kernels_aiv_device'
[ 88%] Built target vllm_ascend_kernels_aiv_device
/usr/local/Ascend/ascend-toolkit/latest/tools/ccec_compiler/bin/ld.lld -x -m aicorelinux   -Ttext=0 /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_aiv_device_dir/device_aiv.o -static -o /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_merge_obj_dir/device_aiv.o
[ 88%] Built target vllm_ascend_kernels_merge_obj
[ 91%] Building CXX object CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o
[ 91%] Built target vllm_ascend_kernels_host_stub_obj
[ 93%] Linking CXX shared library lib/libvllm_ascend_kernels.so
/usr/local/Ascend/ascend-toolkit/latest/bin/ascendc_pack_kernel /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_merge_obj_dir/device_aiv.o 1 /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o
recompile: /usr/bin/c++ -fPIC -O3 -DNDEBUG -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -s -shared -Wl,-soname,libvllm_ascend_kernels.so -o lib/libvllm_ascend_kernels.so CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/efs/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/ma-user/work/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o    -L/usr/local/Ascend/ascend-toolkit/latest/lib64  -L/usr/local/Ascend/ascend-toolkit/latest/tools/simulator/Ascend910B2/lib  /usr/local/Ascend/ascend-toolkit/latest/lib64/libascendc_runtime.a -lascend_dump -lc_sec
/usr/bin/ld: /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/ma-user/work/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o: in function `rope_custom_true_half':
pos_encoding_kernels.cpp:(.text+0x0): multiple definition of `rope_custom_true_half'; /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/efs/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o:pos_encoding_kernels.cpp:(.text+0x0): first defined here
/usr/bin/ld: /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/ma-user/work/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o: in function `rope_custom_false_half':
pos_encoding_kernels.cpp:(.text+0x4): multiple definition of `rope_custom_false_half'; /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/efs/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o:pos_encoding_kernels.cpp:(.text+0x4): first defined here
/usr/bin/ld: /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/ma-user/work/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o: in function `rope_custom_true_bfloat16_t':
pos_encoding_kernels.cpp:(.text+0x8): multiple definition of `rope_custom_true_bfloat16_t'; /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/efs/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o:pos_encoding_kernels.cpp:(.text+0x8): first defined here
/usr/bin/ld: /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/ma-user/work/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o: in function `rope_custom_false_bfloat16_t':
pos_encoding_kernels.cpp:(.text+0xc): multiple definition of `rope_custom_false_bfloat16_t'; /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/efs/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o:pos_encoding_kernels.cpp:(.text+0xc): first defined here
/usr/bin/ld: /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/ma-user/work/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o: in function `vllm_ascend::rotary_embedding_impl(vllm_ascend::AscendType, bool, void*, long*, void*, void*, void*, void*, void*, int, long, long, long, long, int, int, int, long, unsigned int, unsigned int)':
pos_encoding_kernels.cpp:(.text+0x10): multiple definition of `vllm_ascend::rotary_embedding_impl(vllm_ascend::AscendType, bool, void*, long*, void*, void*, void*, void*, void*, int, long, long, long, long, int, int, int, long, unsigned int, unsigned int)'; /efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/efs/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o:pos_encoding_kernels.cpp:(.text+0x10): first defined here
collect2: error: ld returned 1 exit status
Traceback (most recent call last):
  File "/usr/local/Ascend/ascend-toolkit/latest/tools/tikcpp/ascendc_kernel_cmake/util/recompile_binary.py", line 116, in <module>
    main()
  File "/usr/local/Ascend/ascend-toolkit/latest/tools/tikcpp/ascendc_kernel_cmake/util/recompile_binary.py", line 112, in main
    run_recompile_cmd(args.root_dir, recompile_cmd)
  File "/usr/local/Ascend/ascend-toolkit/latest/tools/tikcpp/ascendc_kernel_cmake/util/recompile_binary.py", line 83, in run_recompile_cmd
    result = subprocess.run(cmds, check=True, cwd=root_dir)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/subprocess.py", line 524, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/bin/c++', '-fPIC', '-O3', '-DNDEBUG', '-Wl,-z,relro', '-Wl,-z,now', '-Wl,-z,noexecstack', '-s', '-shared', '-Wl,-soname,libvllm_ascend_kernels.so', '-o', 'lib/libvllm_ascend_kernels.so', 'CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o', '/efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/efs/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o', '/efs/huangzitong/projects/vllm-ascend/build/temp.linux-aarch64-cpython-310/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/ma-user/work/huangzitong/projects/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o', '-L/usr/local/Ascend/ascend-toolkit/latest/lib64', '-L/usr/local/Ascend/ascend-toolkit/latest/tools/simulator/Ascend910B2/lib', '/usr/local/Ascend/ascend-toolkit/latest/lib64/libascendc_runtime.a', '-lascend_dump', '-lc_sec']' returned non-zero exit status 1.
gmake[3]: *** [CMakeFiles/vllm_ascend_kernels.dir/build.make:90: lib/libvllm_ascend_kernels.so] Error 1
gmake[2]: *** [CMakeFiles/Makefile2:373: CMakeFiles/vllm_ascend_kernels.dir/all] Error 2
gmake[1]: *** [CMakeFiles/Makefile2:412: CMakeFiles/vllm_ascend_C.dir/rule] Error 2
gmake: *** [Makefile:286: vllm_ascend_C] Error 2
Traceback (most recent call last):
  File "/efs/huangzitong/projects/vllm-ascend/setup.py", line 340, in <module>
    setup(
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/__init__.py", line 117, in setup
    return distutils.core.setup(**attrs)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 186, in setup
    return run_commands(dist)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 202, in run_commands
    dist.run_commands()
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1002, in run_commands
    self.run_command(cmd)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/dist.py", line 1104, in run_command
    super().run_command(command)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
    cmd_obj.run()
  File "/efs/huangzitong/projects/vllm-ascend/setup.py", line 284, in run
    self.run_command("build_ext")
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
    self.distribution.run_command(command)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/dist.py", line 1104, in run_command
    super().run_command(command)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
    cmd_obj.run()
  File "/efs/huangzitong/projects/vllm-ascend/setup.py", line 278, in run
    super().run()
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/command/build_ext.py", line 99, in run
    _build_ext.run(self)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/setuptools/_distutils/command/build_ext.py", line 368, in run
    self.build_extensions()
  File "/efs/huangzitong/projects/vllm-ascend/setup.py", line 250, in build_extensions
    subprocess.check_call(["cmake", *build_args], cwd=self.build_temp)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/subprocess.py", line 369, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=192', '--target=vllm_ascend_C']' returned non-zero exit status 2.
```

环境pytorch，pytorch-npu=2.5.1, vllm=0.7.3,  CANN==8.1.RC1


### How you are installing vllm and vllm-ascend

```sh
git clone -b v0.7.3.post1 --depth 1 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
export COMPILE_CUSTOM_KERNELS=1
python setup.py install
```

