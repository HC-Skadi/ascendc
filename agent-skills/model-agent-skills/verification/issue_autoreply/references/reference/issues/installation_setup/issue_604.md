# Issue #604: [Installation]: vllm-ascend install from source error

## 基本信息

- **编号**: #604
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/604
- **创建时间**: 2025-04-22T03:22:04Z
- **关闭时间**: 2025-05-14T05:54:52Z
- **更新时间**: 2025-05-14T05:54:53Z
- **提交者**: @hz0ne
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

```text
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64)
GCC version: (GCC) 9.2.1 20200522 (Alibaba 9.2.1-3 2.17)
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.30

Python version: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.112-100.alios7.x86_64-x86_64-with-glibc2.30
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

CPU:
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                192
On-line CPU(s) list:   0-191
Thread(s) per core:    2
Core(s) per socket:    48
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 143
Model name:            Intel(R) Xeon(R) Platinum 8468
Stepping:              8
CPU MHz:               3100.000
BogoMIPS:              4200.00
Virtualization:        VT-x
L1d cache:             48K
L1i cache:             32K
L2 cache:              2048K
L3 cache:              107520K
NUMA node0 CPU(s):     0-47,96-143
NUMA node1 CPU(s):     48-95,144-191
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm uintr md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities

Versions of relevant libraries:
[pip3] mypy==1.15.0
[pip3] mypy-extensions==1.0.0
[pip3] numpy==1.26.4
[pip3] nvidia-ml-py==12.570.86
[pip3] pynvml==12.0.0
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250401
[pip3] torch-optimizer==0.3.0
[pip3] torchaudio==2.5.1+cpu
[pip3] torchdata==0.11.0
[pip3] torchmetrics==0.10.0
[pip3] torchscale==0.2.0
[pip3] torchtext==0.18.0+cpu
[pip3] torchvision==0.20.1+cpu
[pip3] transformers==4.50.0
[pip3] transformers-stream-generator==0.0.5
[conda] Could not collect
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.7.3
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/$(arch):/usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/Ascend/add-ons:/usr/lib/aarch64_64-linux-gnu:/usr/local/mpich-3.2.1/lib:/lib64:/usr/local/lib:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
```


### How you are installing vllm and vllm-ascend

```sh
pip install -e .

when compile vllm_ascend_C, in build kernel, report errors

  [ 88%] Built target vllm_ascend_kernels_merge_obj
  [ 91%] Building CXX object CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o
  [ 91%] Built target vllm_ascend_kernels_host_stub_obj
  [ 93%] Linking CXX shared library lib/libvllm_ascend_kernels.so
  /usr/local/Ascend/ascend-toolkit/latest/bin/ascendc_pack_kernel /tmp/tmpf29ak8a6.build-temp/CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o /tmp/tmpf29ak8a6.build-temp/vllm_ascend_kernels_merge_obj_dir/device_aiv.o 1 /tmp/tmpf29ak8a6.build-temp/CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o
  recompile: /usr/bin/c++ -fPIC -O3 -DNDEBUG -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -s -shared -Wl,-soname,libvllm_ascend_kernels.so -o lib/libvllm_ascend_kernels.so CMakeFiles/vllm_ascend_kernels_host_stub_obj.dir/auto_gen/vllm_ascend_kernels/host_stub.cpp.o /tmp/tmpf29ak8a6.build-temp/vllm_ascend_kernels_host_dir/objects-Release/host_bisheng_obj/home/admin/runtime_package/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp.o    -L/usr/local/Ascend/ascend-toolkit/latest/lib64  -L/usr/local/Ascend/ascend-toolkit/latest/tools/simulator/Ascend910B2C/lib  /usr/local/Ascend/ascend-toolkit/latest/lib64/libascendc_runtime.a -lascend_dump -lc_sec
  [ 93%] Built target vllm_ascend_kernels
  [ 95%] Building CXX object CMakeFiles/vllm_ascend_C.dir/csrc/camem_allocator.cpp.o
  [ 97%] Building CXX object CMakeFiles/vllm_ascend_C.dir/csrc/torch_binding.cpp.o
  In file included from /tmp/pip-build-env-z7036x44/overlay/lib/python3.10/site-packages/torch/include/torch/extension.h:5,
                   from /home/admin/runtime_package/vllm-ascend/csrc/torch_binding.cpp:17:
  /tmp/pip-build-env-z7036x44/overlay/lib/python3.10/site-packages/torch/include/torch/csrc/api/include/torch/all.h:4:2: error: #error C++17 or later compatible compiler is required to use PyTorch.
      4 | #error C++17 or later compatible compiler is required to use PyTorch.
        |  ^~~~~
  In file included from /tmp/pip-build-env-z7036x44/overlay/lib/python3.10/site-packages/torch/include/ATen/core/TensorBase.h:14,
                   from /tmp/pip-build-env-z7036x44/overlay/lib/python3.10/site-packages/torch/include/ATen/core/TensorBody.h:38,
                   from /tmp/pip-build-env-z7036x44/overlay/lib/python3.10/site-packages/torch/include/ATen/core/Tensor.h:3,
                   from /tmp/pip-build-env-z7036x44/overlay/lib/python3.10/site-packages/torch/include/ATen/Tensor.h:3,
```

