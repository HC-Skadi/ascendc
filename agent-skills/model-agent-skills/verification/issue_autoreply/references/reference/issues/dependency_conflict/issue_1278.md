# Issue #1278: [Bug]: Build Error seems like compiler renaming causing it.

## 基本信息

- **编号**: #1278
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1278
- **创建时间**: 2025-06-18T09:28:40Z
- **关闭时间**: 2026-01-04T02:22:33Z
- **更新时间**: 2026-01-04T02:22:33Z
- **提交者**: @ChenTaoyu-SJTU
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

My CANN-toolkit Environment and cann-nnal, cann-kernels, cann-nnae all are `8.2.RC1.alpha002` version. 
```
ascend-toolkit/8.2.RC1.alpha002
```



My build command is below. I would meet a `version not on PyPI error` if I don't using `--no-build-isolation` : `ERROR: No matching distribution found for torch-npu==2.5.1.post1.dev20250528`.  So I add `--no-build-isolation`
```
# Clone vllm code and install
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -r requirements/build.txt
VLLM_TARGET_DEVICE="empty" pip install .
cd ..

# Clone vllm-ascend and install
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -r requirements-dev.txt --trusted-host mirrors.huaweicloud.com
pip install -e . --no-build-isolation
```
### 🐛 Describe the bug

But After then I encounter the error below:
Anyone met the below error? : 
<details>
<summary>The output of `pip install -e . --no-build-isolation`</summary>

```text
Building wheels for collected packages: vllm_ascend
  Building editable for vllm_ascend (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building editable for vllm_ascend (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [462 lines of output]
      /root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
      !!
      
              ********************************************************************************
              Please consider removing the following classifiers in favor of a SPDX license expression:
      
              License :: OSI Approved :: Apache Software License
      
              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************
      
      !!
        self._finalize_license_expression()
      running editable_wheel
      creating /tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info
      writing /tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info/PKG-INFO
      writing dependency_links to /tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info/dependency_links.txt
      writing entry points to /tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info/entry_points.txt
      writing requirements to /tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info/requires.txt
      writing top-level names to /tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info/top_level.txt
      writing manifest file '/tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info/SOURCES.txt'
      adding license file 'LICENSE'
      writing manifest file '/tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend.egg-info/SOURCES.txt'
      creating '/tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend-0.9.0rc3.dev33+gdb2f630.dist-info'
      creating /tmp/pip-wheel-hcwt5v7m/.tmp-gd471a1c/vllm_ascend-0.9.0rc3.dev33+gdb2f630.dist-info/WHEEL
      running build_py
      running build_ext
      Found existing ASCEND_HOME_PATH: /usr/local/Ascend/nnae/latest
      Found existing PYTHON_EXECUTABLE: /root/uv/vllm_dev/bin/python
      Found existing PYTHON_INCLUDE_PATH: /root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/include/python3.11
      /root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/develop.py:41: EasyInstallDeprecationWarning: easy_install command is deprecated.
      !!
      
              ********************************************************************************
              Please avoid running ``setup.py`` and ``easy_install``.
              Instead, use pypa/build, pypa/installer or other
              standards-based tools.
      
              See https://github.com/pypa/setuptools/issues/917 for details.
              ********************************************************************************
      
      !!
        easy_install.initialize_options(self)
      cmake config command: ['cmake', '-DCMAKE_BUILD_TYPE=Release', '-DCMAKE_EXPORT_COMPILE_COMMANDS=1', '-DASCEND_HOME_PATH=/usr/local/Ascend/nnae/latest', '-DPYTHON_EXECUTABLE=/root/uv/vllm_dev/bin/python', '-DPYTHON_INCLUDE_PATH=/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/include/python3.11', '-DCMAKE_INSTALL_PREFIX=/root/vllm_dev/vllm-ascend/vllm_ascend', '-DCMAKE_PREFIX_PATH=/root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11', '-DSOC_VERSION=ASCEND910B1', '-DFETCHCONTENT_BASE_DIR=/root/vllm_dev/vllm-ascend/.deps', '-DTORCH_NPU_PATH=/root/uv/vllm_dev/lib/python3.11/site-packages/torch_npu', '/root/vllm_dev/vllm-ascend']
      -- The C compiler identification is GNU 10.3.1
      -- The CXX compiler identification is GNU 10.3.1
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info - done
      -- Check for working CXX compiler: /usr/bin/c++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      CMake Warning (dev) at /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/FindPythonLibsNew.cmake:101 (message):
        Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
        are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
        the cmake_policy command to set the policy and suppress this warning, or
        preferably upgrade to using FindPython, either by calling it explicitly
        before pybind11, or by setting PYBIND11_FINDPYTHON ON before pybind11.
      Call Stack (most recent call first):
        /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/pybind11Tools.cmake:50 (find_package)
        /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/pybind11Common.cmake:228 (include)
        /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/pybind11Config.cmake:250 (include)
        CMakeLists.txt:16 (find_package)
      This warning is for project developers.  Use -Wno-dev to suppress it.
      
      -- Found PythonInterp: /root/uv/vllm_dev/bin/python (found suitable version "3.11.11", minimum required is "3.7")
      -- Found PythonLibs: /root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/libpython3.11.so
      -- Performing Test HAS_FLTO
      -- Performing Test HAS_FLTO - Success
      -- Found pybind11: /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/include (found version "2.13.6")
      CMake Warning at /root/uv/vllm_dev/lib/python3.11/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message):
        static library kineto_LIBRARY-NOTFOUND not found.
      Call Stack (most recent call first):
        /root/uv/vllm_dev/lib/python3.11/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:120 (append_torchlib_if_found)
        CMakeLists.txt:21 (find_package)
      
      
      -- Found Torch: /root/uv/vllm_dev/lib/python3.11/site-packages/torch/lib/libtorch.so
      -- Detected SOC version: ASCEND910B1
      TORCH_NPU_PATH is /root/uv/vllm_dev/lib/python3.11/site-packages/torch_npu
      -- Configuring done (9.2s)
      -- Generating done (0.0s)
      CMake Warning:
        Manually-specified variables were not used by the project:
      
          FETCHCONTENT_BASE_DIR
      
      
      -- Build files have been written to: /tmp/tmp11o9tpga.build-temp
      CMake Warning:
        Ignoring extra path from command line:
      
         "cmake"
      
      
      CMake Warning (dev) at /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/FindPythonLibsNew.cmake:101 (message):
        Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
        are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
        the cmake_policy command to set the policy and suppress this warning, or
        preferably upgrade to using FindPython, either by calling it explicitly
        before pybind11, or by setting PYBIND11_FINDPYTHON ON before pybind11.
      Call Stack (most recent call first):
        /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/pybind11Tools.cmake:50 (find_package)
        /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/pybind11Common.cmake:228 (include)
        /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/pybind11Config.cmake:250 (include)
        CMakeLists.txt:16 (find_package)
      This warning is for project developers.  Use -Wno-dev to suppress it.
      
      -- Found pybind11: /root/uv/vllm_dev/lib/python3.11/site-packages/pybind11/include (found version "2.13.6")
      CMake Warning at /root/uv/vllm_dev/lib/python3.11/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message):
        static library kineto_LIBRARY-NOTFOUND not found.
      Call Stack (most recent call first):
        /root/uv/vllm_dev/lib/python3.11/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:120 (append_torchlib_if_found)
        CMakeLists.txt:21 (find_package)
      
      
      -- Detected SOC version: ASCEND910B1
      TORCH_NPU_PATH is /root/uv/vllm_dev/lib/python3.11/site-packages/torch_npu
      -- Configuring done (5.4s)
      -- Generating done (0.0s)
      -- Build files have been written to: /tmp/tmp11o9tpga.build-temp
      [  2%] Creating directories for 'vllm_ascend_kernels_precompile'
      [  4%] No download step for 'vllm_ascend_kernels_precompile'
      [  6%] No update step for 'vllm_ascend_kernels_precompile'
      [  8%] No patch step for 'vllm_ascend_kernels_precompile'
      [ 11%] Performing configure step for 'vllm_ascend_kernels_precompile'
      -- The C compiler identification is GNU 10.3.1
      -- The CXX compiler identification is GNU 10.3.1
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info - done
      -- Check for working CXX compiler: /usr/bin/c++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      -- Configuring done (0.6s)
      -- Generating done (0.0s)
      CMake Warning:
        Manually-specified variables were not used by the project:
      
          DYNAMIC_MODE
          INCLUDE_DIR
      
      
      -- Build files have been written to: /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_precompile-prefix/src/vllm_ascend_kernels_precompile-build
      [ 13%] Performing build step for 'vllm_ascend_kernels_precompile'
      [ 33%] Building CXX object CMakeFiles/precompile_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o
      [100%] Building CXX object CMakeFiles/precompile_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o
      [100%] Building CXX object CMakeFiles/precompile_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o
      [100%] Built target precompile_obj
      [100%] Built target check_src_template
      [ 15%] No install step for 'vllm_ascend_kernels_precompile'
      [ 17%] Completed 'vllm_ascend_kernels_precompile'
      [ 17%] Built target vllm_ascend_kernels_precompile
      [ 20%] Creating directories for 'vllm_ascend_kernels_preprocess'
      [ 22%] No download step for 'vllm_ascend_kernels_preprocess'
      [ 24%] No update step for 'vllm_ascend_kernels_preprocess'
      [ 26%] No patch step for 'vllm_ascend_kernels_preprocess'
      [ 28%] Performing configure step for 'vllm_ascend_kernels_preprocess'
      -- The C compiler identification is GNU 10.3.1
      -- The CXX compiler identification is GNU 10.3.1
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info - done
      -- Check for working CXX compiler: /usr/bin/c++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      -- Configuring done (0.6s)
      -- Generating done (0.0s)
      -- Build files have been written to: /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build
      [ 31%] Performing build step for 'vllm_ascend_kernels_preprocess'
      [ 11%] Building CXX object CMakeFiles/preprocess_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o
      [ 22%] Building CXX object CMakeFiles/preprocess_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o
      [ 33%] Building CXX object CMakeFiles/preprocess_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o
      [ 44%] Building CXX object CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o
      [ 66%] Building CXX object CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o
      [ 66%] Building CXX object CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o
      [100%] Building CXX object CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o
      [100%] Building CXX object CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o
      [100%] Building CXX object CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o
      [100%] Built target preprocess_obj
      [100%] Built target aic_obj
      /usr/local/Ascend/nnae/latest/compiler/ccec_compiler/bin/ld.lld -m aicorelinux -Ttext=0 /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o -o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o/usr/local/Ascend/nnae/latest/compiler/ccec_compiler/bin/ld.lld -m aicorelinux -Ttext=0 /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o -o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o/usr/local/Ascend/nnae/latest/compiler/ccec_compiler/bin/ld.lld -m aicorelinux -Ttext=0 /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o -o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aic_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o[100%] Built target merge_aic_obj_text
      [100%] Built target aiv_obj
      /usr/local/Ascend/nnae/latest/compiler/ccec_compiler/bin/ld.lld -m aicorelinux -Ttext=0 /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o -o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o/usr/local/Ascend/nnae/latest/compiler/ccec_compiler/bin/ld.lld -m aicorelinux -Ttext=0 /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o -o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o/usr/local/Ascend/nnae/latest/compiler/ccec_compiler/bin/ld.lld -m aicorelinux -Ttext=0 /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o -o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_preprocess-prefix/src/vllm_ascend_kernels_preprocess-build/CMakeFiles/aiv_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o[100%] Built target merge_aiv_obj_text
      [100%] Built target _host_cpp
      [ 33%] No install step for 'vllm_ascend_kernels_preprocess'
      [ 35%] Completed 'vllm_ascend_kernels_preprocess'
      [ 35%] Built target vllm_ascend_kernels_preprocess
      [ 37%] Creating directories for 'vllm_ascend_kernels_host'
      [ 42%] Creating directories for 'vllm_ascend_kernels_aiv_device'
      [ 42%] Creating directories for 'vllm_ascend_kernels_aic_device'
      [ 44%] No download step for 'vllm_ascend_kernels_host'
      [ 46%] No download step for 'vllm_ascend_kernels_aiv_device'
      [ 48%] No download step for 'vllm_ascend_kernels_aic_device'
      [ 51%] No update step for 'vllm_ascend_kernels_host'
      [ 53%] No update step for 'vllm_ascend_kernels_aiv_device'
      [ 55%] No update step for 'vllm_ascend_kernels_aic_device'
      [ 57%] No patch step for 'vllm_ascend_kernels_host'
      [ 60%] No patch step for 'vllm_ascend_kernels_aiv_device'
      [ 62%] No patch step for 'vllm_ascend_kernels_aic_device'
      [ 64%] Performing configure step for 'vllm_ascend_kernels_host'
      [ 66%] Performing configure step for 'vllm_ascend_kernels_aiv_device'
      [ 68%] Performing configure step for 'vllm_ascend_kernels_aic_device'
      -- The C compiler identification is GNU 10.3.1
      -- The C compiler identification is GNU 10.3.1
      -- The C compiler identification is GNU 10.3.1
      -- The CXX compiler identification is GNU 10.3.1
      -- The CXX compiler identification is GNU 10.3.1
      -- The CXX compiler identification is GNU 10.3.1
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Detecting C compiler ABI info - done
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Detecting C compile features
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Detecting C compile features
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Detecting C compile features - done
      -- Detecting C compile features - done
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info - done
      -- Detecting CXX compiler ABI info - done
      -- Detecting CXX compiler ABI info - done
      -- Check for working CXX compiler: /usr/bin/c++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      -- Check for working CXX compiler: /usr/bin/c++ - skipped
      -- Check for working CXX compiler: /usr/bin/c++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      -- Detecting CXX compile features - done
      -- Configuring done (0.8s)
      -- Configuring done (0.8s)
      -- Configuring done (0.8s)
      -- Generating done (0.0s)
      CMake Warning:
        Manually-specified variables were not used by the project:
      
          ASCEND_PYTHON_EXECUTABLE
      
      
      -- Build files have been written to: /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_host-prefix/src/vllm_ascend_kernels_host-build
      -- Generating done (0.0s)
      CMake Warning:
        Manually-specified variables were not used by the project:
      
          BUILD_MODE
      
      
      -- Build files have been written to: /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_aic_device-prefix/src/vllm_ascend_kernels_aic_device-build
      -- Generating done (0.0s)
      -- Build files have been written to: /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_aiv_device-prefix/src/vllm_ascend_kernels_aiv_device-build
      [ 71%] Performing build step for 'vllm_ascend_kernels_host'
      [ 73%] Performing build step for 'vllm_ascend_kernels_aic_device'
      [ 75%] Performing build step for 'vllm_ascend_kernels_aiv_device'
      [ 77%] No install step for 'vllm_ascend_kernels_aic_device'
      [ 33%] Building CXX object CMakeFiles/host_bisheng_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/advance_step.cpp.o
      [ 80%] Completed 'vllm_ascend_kernels_aic_device'
      [100%] Building CXX object CMakeFiles/host_bisheng_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/get_masked_input_and_mask_kernel.cpp.o
      [100%] Building CXX object CMakeFiles/host_bisheng_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o
      [100%] Building CXX object CMakeFiles/device_aiv_obj.dir/tmp/tmp11o9tpga.build-temp/auto_gen/vllm_ascend_kernels/auto_gen_advance_step.cpp.o
      [100%] Building CXX object CMakeFiles/device_aiv_obj.dir/tmp/tmp11o9tpga.build-temp/auto_gen/vllm_ascend_kernels/auto_gen_pos_encoding_kernels.cpp.o
      [100%] Building CXX object CMakeFiles/device_aiv_obj.dir/tmp/tmp11o9tpga.build-temp/auto_gen/vllm_ascend_kernels/auto_gen_get_masked_input_and_mask_kernel.cpp.o
      [ 80%] Built target vllm_ascend_kernels_aic_device
      Function AscendcCompiler at line 98, Command execution failed, the returnCode is non-zero!
      Output of ascendc_compiler:
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:359:9: error: use of undeclared identifier 'rope_custom_true_half'; did you mean 'rope_custom_true___cce_half'?
              ROTARY_EMBEDDING_KERNEL_CALL(half);
              ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:335:9: note: expanded from macro 'ROTARY_EMBEDDING_KERNEL_CALL'
              rope_custom_true_##TYPE<<<blockDim, nullptr, stream>>>(                                                  \
              ^
      <scratch space>:330:1: note: expanded from here
      rope_custom_true_half
      ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:328:1: note: 'rope_custom_true___cce_half' declared here
      ROPE_CUSTOM_KERNEL_DECLARE(half)
      ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:324:5: note: expanded from macro 'ROPE_CUSTOM_KERNEL_DECLARE'
          ROPE_CUSTOM_KERNEL_TYPE_DECLARE(TYPE, true); \
          ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:306:43: note: expanded from macro 'ROPE_CUSTOM_KERNEL_TYPE_DECLARE'
          extern "C" __global__ __aicore__ void rope_custom_##NEOX##_##TYPE(                                                          \
                                                ^
      <scratch space>:320:1: note: expanded from here
      rope_custom_true___cce_half
      ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:359:9: error: call to global function rope_custom_true___cce_half not configured
              ROTARY_EMBEDDING_KERNEL_CALL(half);
              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:335:63: note: expanded from macro 'ROTARY_EMBEDDING_KERNEL_CALL'
              rope_custom_true_##TYPE<<<blockDim, nullptr, stream>>>(                                                  \
              ~~~~~~~~~~~~~~~~~~~~~~~                               ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:359:9: error: use of undeclared identifier 'rope_custom_false_half'; did you mean 'rope_custom_false___cce_half'?
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:340:9: note: expanded from macro 'ROTARY_EMBEDDING_KERNEL_CALL'
              rope_custom_false_##TYPE<<<blockDim, nullptr, stream>>>(                                                 \
              ^
      <scratch space>:331:1: note: expanded from here
      rope_custom_false_half
      ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:328:1: note: 'rope_custom_false___cce_half' declared here
      ROPE_CUSTOM_KERNEL_DECLARE(half)
      ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:325:5: note: expanded from macro 'ROPE_CUSTOM_KERNEL_DECLARE'
          ROPE_CUSTOM_KERNEL_TYPE_DECLARE(TYPE, false);
          ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:306:43: note: expanded from macro 'ROPE_CUSTOM_KERNEL_TYPE_DECLARE'
          extern "C" __global__ __aicore__ void rope_custom_##NEOX##_##TYPE(                                                          \
                                                ^
      <scratch space>:323:1: note: expanded from here
      rope_custom_false___cce_half
      ^
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:359:9: error: call to global function rope_custom_false___cce_half not configured
              ROTARY_EMBEDDING_KERNEL_CALL(half);
              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      /root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:340:64: note: expanded from macro 'ROTARY_EMBEDDING_KERNEL_CALL'
              rope_custom_false_##TYPE<<<blockDim, nullptr, stream>>>(                                                 \
              ~~~~~~~~~~~~~~~~~~~~~~~~                               ^
      4 errors generated.
      gmake[6]: *** [CMakeFiles/host_bisheng_obj.dir/build.make:107: CMakeFiles/host_bisheng_obj.dir/root/vllm_dev/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o] Error 1
      gmake[5]: *** [CMakeFiles/Makefile2:87: CMakeFiles/host_bisheng_obj.dir/all] Error 2
      gmake[4]: *** [Makefile:136: all] Error 2
      gmake[3]: *** [CMakeFiles/vllm_ascend_kernels_host.dir/build.make:86: vllm_ascend_kernels_host-prefix/src/vllm_ascend_kernels_host-stamp/vllm_ascend_kernels_host-build] Error 2
      gmake[2]: *** [CMakeFiles/Makefile2:306: CMakeFiles/vllm_ascend_kernels_host.dir/all] Error 2
      gmake[2]: *** Waiting for unfinished jobs....
      [100%] Built target device_aiv_obj
      /usr/local/Ascend/nnae/latest/compiler/ccec_compiler/bin/ld.lld  -m aicorelinux -r  -Ttext=0 /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_aiv_device-prefix/src/vllm_ascend_kernels_aiv_device-build/CMakeFiles/device_aiv_obj.dir/tmp/tmp11o9tpga.build-temp/auto_gen/vllm_ascend_kernels/auto_gen_advance_step.cpp.o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_aiv_device-prefix/src/vllm_ascend_kernels_aiv_device-build/CMakeFiles/device_aiv_obj.dir/tmp/tmp11o9tpga.build-temp/auto_gen/vllm_ascend_kernels/auto_gen_get_masked_input_and_mask_kernel.cpp.o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_aiv_device-prefix/src/vllm_ascend_kernels_aiv_device-build/CMakeFiles/device_aiv_obj.dir/tmp/tmp11o9tpga.build-temp/auto_gen/vllm_ascend_kernels/auto_gen_pos_encoding_kernels.cpp.o -static -o /tmp/tmp11o9tpga.build-temp/vllm_ascend_kernels_aiv_device_dir/device_aiv.o
      [100%] Built target merge_aiv_device_obj
      [ 82%] No install step for 'vllm_ascend_kernels_aiv_device'
      [ 84%] Completed 'vllm_ascend_kernels_aiv_device'
      [ 84%] Built target vllm_ascend_kernels_aiv_device
      gmake[1]: *** [CMakeFiles/Makefile2:412: CMakeFiles/vllm_ascend_C.dir/rule] Error 2
      gmake: *** [Makefile:286: vllm_ascend_C] Error 2
      Traceback (most recent call last):
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 139, in run
          self._create_wheel_file(bdist_wheel)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 340, in _create_wheel_file
          files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 263, in _run_build_commands
          self._run_build_subcommands()
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 290, in _run_build_subcommands
          self.run_command(name)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/dist.py", line 1104, in run_command
          super().run_command(command)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "<string>", line 269, in run
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 99, in run
          _build_ext.run(self)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 368, in run
          self.build_extensions()
        File "<string>", line 241, in build_extensions
        File "/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/python3.11/subprocess.py", line 413, in check_call
          raise CalledProcessError(retcode, cmd)
      subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=192', '--target=vllm_ascend_C']' returned non-zero exit status 2.
      /root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/dist.py:1021: _DebuggingTips: Problem in editable installation.
      !!
      
              ********************************************************************************
              An error happened while installing `vllm_ascend` in editable mode.
      
              The following steps are recommended to help debug this problem:
      
              - Try to install the project normally, without using the editable mode.
                Does the error still persist?
                (If it does, try fixing the problem before attempting the editable mode).
              - If you are using binary extensions, make sure you have all OS-level
                dependencies installed (e.g. compilers, toolchains, binary libraries, ...).
              - Try the latest version of setuptools (maybe the error was already fixed).
              - If you (or your project dependencies) are using any setuptools extension
                or customization, make sure they support the editable mode.
      
              After following the steps above, if the problem still persists and
              you think this is related to how setuptools handles editable installations,
              please submit a reproducible example
              (see https://stackoverflow.com/help/minimal-reproducible-example) to:
      
                  https://github.com/pypa/setuptools/issues
      
              See https://setuptools.pypa.io/en/latest/userguide/development_mode.html for details.
              ********************************************************************************
      
      !!
        cmd_obj.run()
      Traceback (most recent call last):
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
          main()
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 303, in build_editable
          return hook(wheel_directory, config_settings, metadata_directory)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/build_meta.py", line 468, in build_editable
          return self._build_with_temp_dir(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/build_meta.py", line 404, in _build_with_temp_dir
          self.run_setup()
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/build_meta.py", line 317, in run_setup
          exec(code, locals())
        File "<string>", line 331, in <module>
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/__init__.py", line 117, in setup
          return distutils.core.setup(**attrs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 186, in setup
          return run_commands(dist)
                 ^^^^^^^^^^^^^^^^^^
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 202, in run_commands
          dist.run_commands()
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_commands
          self.run_command(cmd)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/dist.py", line 1104, in run_command
          super().run_command(command)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 139, in run
          self._create_wheel_file(bdist_wheel)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 340, in _create_wheel_file
          files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 263, in _run_build_commands
          self._run_build_subcommands()
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/editable_wheel.py", line 290, in _run_build_subcommands
          self.run_command(name)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/dist.py", line 1104, in run_command
          super().run_command(command)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "<string>", line 269, in run
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 99, in run
          _build_ext.run(self)
        File "/root/uv/vllm_dev/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 368, in run
          self.build_extensions()
        File "<string>", line 241, in build_extensions
        File "/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/python3.11/subprocess.py", line 413, in check_call
          raise CalledProcessError(retcode, cmd)
      subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=192', '--target=vllm_ascend_C']' returned non-zero exit status 2.
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building editable for vllm_ascend
Failed to build vllm_ascend
ERROR: Failed to build installable wheels for some pyproject.toml based projects (vllm_ascend)
```

</details>

