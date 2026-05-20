# Issue #591: [Installation]: Failed to install vllm-ascend from source

## 基本信息

- **编号**: #591
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/591
- **创建时间**: 2025-04-21T04:49:31Z
- **关闭时间**: 2025-04-28T15:22:16Z
- **更新时间**: 2025-08-20T11:45:25Z
- **提交者**: @jianzs
- **评论数**: 5

## 标签

installation

## 问题描述

I'm trying to install vllm-ascend from source, but I encountered a "no matching function" error. It seems to be related to CANN, but I'm not certain.

### Your current environment

```text
/usr/local/lib64/python3.11/site-packages/torchvision/io/image.py:13: UserWarning: Failed to load image Python extension: 'libc10_cuda.so: cannot open shared object file: No such file or directory'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source?
  warn(
INFO 04-21 12:48:43 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-21 12:48:43 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-21 12:48:43 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-21 12:48:43 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-21 12:48:43 [__init__.py:44] plugin ascend loaded.
INFO 04-21 12:48:43 [__init__.py:230] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 3.27.9
Libc version: glibc-2.38

Python version: 3.11.6 (main, Feb 19 2025, 17:40:52) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
Python platform: Linux-5.10.112-100.alios7.x86_64-x86_64-with-glibc2.38

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
BIOS Vendor ID:                  Intel(R) Corporation
Model name:                      Intel(R) Xeon(R) Platinum 8468
BIOS Model name:                 Intel(R) Xeon(R) Platinum 8468  CPU @ 2.1GHz
BIOS CPU family:                 179
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              48
Socket(s):                       2
Stepping:                        8
BogoMIPS:                        4200.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm uintr md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       4.5 MiB (96 instances)
L1i cache:                       3 MiB (96 instances)
L2 cache:                        192 MiB (96 instances)
L3 cache:                        210 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-47,96-143
NUMA node1 CPU(s):               48-95,144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchvision==0.16.0
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.1.dev1+gfe742ae (git sha: fe742ae)
vLLM Ascend Version: 0.1.dev1+g96d6fa7.d20250421 (git sha: 96d6fa7, date: 20250421)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/lib/python3.11/site-packages/mindie_turbo:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=3
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.2               Version: 24.1.rc2.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 90.4        42                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3424 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 95.3        45                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3407 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 91.6        44                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3406 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 97.5        44                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 92.6        41                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3406 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 97.8        43                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3406 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 92.6        44                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 93.7        42                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3406 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 93.6        43                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 99.4        44                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 96.4        43                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 94.1        44                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 90.6        43                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 94.8        43                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 91.2        42                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 97.8        44                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3392 / 65536         |
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
| No running processes found in NPU 8                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 9                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 10                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 11                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 12                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 13                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 14                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 15                                                           |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.XXX
innerversion=V100R001C21B081
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.XXX/x86_64-linux
```


### How you are installing vllm and vllm-ascend

```sh
pip install -e . --no-build-isolation
```

### Error Log
```plain
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:626:22: error: no matching function for call to ‘find(std::vector<std::basic_string<char> >::const_iterator, std::vector<std::basic_string<char> >::const_iterator, std::regex_traits<char>::string_type)’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/streambuf_iterator.h:369:5: note: candidate: ‘template<class _CharT2> typename __gnu_cxx::__enable_if<std::__is_char<_CharT2>::__value, std::istreambuf_iterator<_CharT> >::__type std::find(istreambuf_iterator<_CharT>, istreambuf_iterator<_CharT>, const _CharT2&)’
        369 |     find(istreambuf_iterator<_CharT> __first,
            |     ^~~~
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/streambuf_iterator.h:369:5: note:   template argument deduction/substitution failed:
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:626:22: note:   ‘__gnu_cxx::__normal_iterator<const std::basic_string<char>*, std::vector<std::basic_string<char> > >’ is not derived from ‘std::istreambuf_iterator<_CharT>’
        626 |         if (std::find(_M_equiv_set.begin(), _M_equiv_set.end(),
            |             ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        627 |                       _M_traits.transform_primary(&__ch, &__ch+1))
            |                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc: In instantiation of ‘bool std::__detail::_BracketMatcher< <template-parameter-1-1>, <anonymous>, <anonymous> >::_M_apply(_CharT, std::false_type) const [with _TraitsT = std::regex_traits<char>; bool __icase = true; bool __collate = false; _CharT = char; std::false_type = std::integral_constant<bool, false>]’:
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.h:556:28:   required from ‘void std::__detail::_BracketMatcher< <template-parameter-1-1>, <anonymous>, <anonymous> >::_M_make_cache(std::true_type) [with _TraitsT = std::regex_traits<char>; bool __icase = true; bool __collate = false; std::true_type = std::integral_constant<bool, true>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.h:525:15:   required from ‘void std::__detail::_BracketMatcher< <template-parameter-1-1>, <anonymous>, <anonymous> >::_M_ready() [with _TraitsT = std::regex_traits<char>; bool __icase = true; bool __collate = false]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:414:25:   required from ‘void std::__detail::_Compiler<_TraitsT>::_M_insert_character_class_matcher() [with bool __icase = true; bool __collate = false; _TraitsT = std::regex_traits<char>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:327:2:   required from ‘bool std::__detail::_Compiler<_TraitsT>::_M_atom() [with _TraitsT = std::regex_traits<char>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:139:17:   required from ‘bool std::__detail::_Compiler<_TraitsT>::_M_term() [with _TraitsT = std::regex_traits<char>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:121:17:   [ skipping 2 instantiation contexts, use -ftemplate-backtrace-limit=0 to disable ]
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:82:13:   required from ‘std::__detail::_Compiler<_TraitsT>::_Compiler(_IterT, _IterT, const typename _TraitsT::locale_type&, _FlagT) [with _TraitsT = std::regex_traits<char>; _IterT = const char*; typename _TraitsT::locale_type = std::locale; _FlagT = std::regex_constants::syntax_option_type]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.h:203:14:   required from ‘std::__detail::__enable_if_contiguous_normal_iter<_FwdIter, _TraitsT> std::__detail::__compile_nfa(_FwdIter, _FwdIter, const typename _TraitsT::locale_type&, std::regex_constants::syntax_option_type) [with _FwdIter = const char*; _TraitsT = std::regex_traits<char>; __enable_if_contiguous_normal_iter<_FwdIter, _TraitsT> = std::shared_ptr<const _NFA<std::regex_traits<char> > >; typename _TraitsT::locale_type = std::locale]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex.h:766:60:   required from ‘std::basic_regex< <template-parameter-1-1>, <template-parameter-1-2> >::basic_regex(_FwdIter, _FwdIter, locale_type, flag_type) [with _FwdIter = const char*; _Ch_type = char; _Rx_traits = std::regex_traits<char>; locale_type = std::locale; flag_type = std::regex_constants::syntax_option_type]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex.h:512:73:   required from ‘std::basic_regex< <template-parameter-1-1>, <template-parameter-1-2> >::basic_regex(_FwdIter, _FwdIter, flag_type) [with _FwdIter = const char*; _Ch_type = char; _Rx_traits = std::regex_traits<char>; flag_type = std::regex_constants::syntax_option_type]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex.h:445:71:   required from ‘std::basic_regex< <template-parameter-1-1>, <template-parameter-1-2> >::basic_regex(const _Ch_type*, flag_type) [with _Ch_type = char; _Rx_traits = std::regex_traits<char>; flag_type = std::regex_constants::syntax_option_type]’
      /usr/local/lib64/python3.11/site-packages/torch_npu/include/torch_npu/csrc/core/npu/NPUGraphsUtils.h:78:5:   required from here
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:626:22: error: no matching function for call to ‘find(std::vector<std::basic_string<char> >::const_iterator, std::vector<std::basic_string<char> >::const_iterator, std::regex_traits<char>::string_type)’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/streambuf_iterator.h:369:5: note: candidate: ‘template<class _CharT2> typename __gnu_cxx::__enable_if<std::__is_char<_CharT2>::__value, std::istreambuf_iterator<_CharT> >::__type std::find(istreambuf_iterator<_CharT>, istreambuf_iterator<_CharT>, const _CharT2&)’
        369 |     find(istreambuf_iterator<_CharT> __first,
            |     ^~~~
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/streambuf_iterator.h:369:5: note:   template argument deduction/substitution failed:
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:626:22: note:   ‘__gnu_cxx::__normal_iterator<const std::basic_string<char>*, std::vector<std::basic_string<char> > >’ is not derived from ‘std::istreambuf_iterator<_CharT>’
        626 |         if (std::find(_M_equiv_set.begin(), _M_equiv_set.end(),
            |             ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        627 |                       _M_traits.transform_primary(&__ch, &__ch+1))
            |                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc: In instantiation of ‘bool std::__detail::_BracketMatcher< <template-parameter-1-1>, <anonymous>, <anonymous> >::_M_apply(_CharT, std::false_type) const [with _TraitsT = std::regex_traits<char>; bool __icase = true; bool __collate = true; _CharT = char; std::false_type = std::integral_constant<bool, false>]’:
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.h:556:28:   required from ‘void std::__detail::_BracketMatcher< <template-parameter-1-1>, <anonymous>, <anonymous> >::_M_make_cache(std::true_type) [with _TraitsT = std::regex_traits<char>; bool __icase = true; bool __collate = true; std::true_type = std::integral_constant<bool, true>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.h:525:15:   required from ‘void std::__detail::_BracketMatcher< <template-parameter-1-1>, <anonymous>, <anonymous> >::_M_ready() [with _TraitsT = std::regex_traits<char>; bool __icase = true; bool __collate = true]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:414:25:   required from ‘void std::__detail::_Compiler<_TraitsT>::_M_insert_character_class_matcher() [with bool __icase = true; bool __collate = true; _TraitsT = std::regex_traits<char>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:327:2:   required from ‘bool std::__detail::_Compiler<_TraitsT>::_M_atom() [with _TraitsT = std::regex_traits<char>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:139:17:   required from ‘bool std::__detail::_Compiler<_TraitsT>::_M_term() [with _TraitsT = std::regex_traits<char>]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:121:17:   [ skipping 2 instantiation contexts, use -ftemplate-backtrace-limit=0 to disable ]
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:82:13:   required from ‘std::__detail::_Compiler<_TraitsT>::_Compiler(_IterT, _IterT, const typename _TraitsT::locale_type&, _FlagT) [with _TraitsT = std::regex_traits<char>; _IterT = const char*; typename _TraitsT::locale_type = std::locale; _FlagT = std::regex_constants::syntax_option_type]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.h:203:14:   required from ‘std::__detail::__enable_if_contiguous_normal_iter<_FwdIter, _TraitsT> std::__detail::__compile_nfa(_FwdIter, _FwdIter, const typename _TraitsT::locale_type&, std::regex_constants::syntax_option_type) [with _FwdIter = const char*; _TraitsT = std::regex_traits<char>; __enable_if_contiguous_normal_iter<_FwdIter, _TraitsT> = std::shared_ptr<const _NFA<std::regex_traits<char> > >; typename _TraitsT::locale_type = std::locale]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex.h:766:60:   required from ‘std::basic_regex< <template-parameter-1-1>, <template-parameter-1-2> >::basic_regex(_FwdIter, _FwdIter, locale_type, flag_type) [with _FwdIter = const char*; _Ch_type = char; _Rx_traits = std::regex_traits<char>; locale_type = std::locale; flag_type = std::regex_constants::syntax_option_type]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex.h:512:73:   required from ‘std::basic_regex< <template-parameter-1-1>, <template-parameter-1-2> >::basic_regex(_FwdIter, _FwdIter, flag_type) [with _FwdIter = const char*; _Ch_type = char; _Rx_traits = std::regex_traits<char>; flag_type = std::regex_constants::syntax_option_type]’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex.h:445:71:   required from ‘std::basic_regex< <template-parameter-1-1>, <template-parameter-1-2> >::basic_regex(const _Ch_type*, flag_type) [with _Ch_type = char; _Rx_traits = std::regex_traits<char>; flag_type = std::regex_constants::syntax_option_type]’
      /usr/local/lib64/python3.11/site-packages/torch_npu/include/torch_npu/csrc/core/npu/NPUGraphsUtils.h:78:5:   required from here
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:626:22: error: no matching function for call to ‘find(std::vector<std::basic_string<char> >::const_iterator, std::vector<std::basic_string<char> >::const_iterator, std::regex_traits<char>::string_type)’
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/streambuf_iterator.h:369:5: note: candidate: ‘template<class _CharT2> typename __gnu_cxx::__enable_if<std::__is_char<_CharT2>::__value, std::istreambuf_iterator<_CharT> >::__type std::find(istreambuf_iterator<_CharT>, istreambuf_iterator<_CharT>, const _CharT2&)’
        369 |     find(istreambuf_iterator<_CharT> __first,
            |     ^~~~
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/streambuf_iterator.h:369:5: note:   template argument deduction/substitution failed:
      /path/to/ascend-toolkit/8.1.XXX/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/bits/regex_compiler.tcc:626:22: note:   ‘__gnu_cxx::__normal_iterator<const std::basic_string<char>*, std::vector<std::basic_string<char> > >’ is not derived from ‘std::istreambuf_iterator<_CharT>’
        626 |         if (std::find(_M_equiv_set.begin(), _M_equiv_set.end(),
            |             ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        627 |                       _M_traits.transform_primary(&__ch, &__ch+1))
            |                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      gmake[3]: *** [CMakeFiles/vllm_ascend_C.dir/build.make:90: CMakeFiles/vllm_ascend_C.dir/csrc/torch_binding.cpp.o] Error 1
      gmake[2]: *** [CMakeFiles/Makefile2:337: CMakeFiles/vllm_ascend_C.dir/all] Error 2
      gmake[1]: *** [CMakeFiles/Makefile2:344: CMakeFiles/vllm_ascend_C.dir/rule] Error 2
      gmake: *** [Makefile:286: vllm_ascend_C] Error 2
      Traceback (most recent call last):
        File "/usr/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
        File "/usr/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 251, in build_wheel
          return _build_backend().build_wheel(wheel_directory, config_settings,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/site-packages/setuptools/build_meta.py", line 416, in build_wheel
          return self._build_with_temp_dir(['bdist_wheel'], '.whl',
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/site-packages/setuptools/build_meta.py", line 401, in _build_with_temp_dir
          self.run_setup()
        File "/usr/lib/python3.11/site-packages/setuptools/build_meta.py", line 338, in run_setup
          exec(code, locals())
        File "<string>", line 331, in <module>
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
        File "/usr/local/lib/python3.11/site-packages/wheel/_bdist_wheel.py", line 387, in run
          self.run_command("build")
        File "/usr/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 318, in run_command
          self.distribution.run_command(command)
        File "/usr/lib/python3.11/site-packages/setuptools/dist.py", line 1234, in run_command
          super().run_command(command)
        File "/usr/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
          cmd_obj.run()
        File "/usr/lib/python3.11/site-packages/setuptools/_distutils/command/build.py", line 131, in run
          self.run_command(cmd_name)
        File "/usr/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 318, in run_command
          self.distribution.run_command(command)
        File "/usr/lib/python3.11/site-packages/setuptools/dist.py", line 1234, in run_command
          super().run_command(command)
        File "/usr/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
          cmd_obj.run()
        File "<string>", line 269, in run
        File "/usr/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 84, in run
          _build_ext.run(self)
        File "/usr/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 345, in run
          self.build_extensions()
        File "<string>", line 241, in build_extensions
        File "/usr/lib64/python3.11/subprocess.py", line 413, in check_call
          raise CalledProcessError(retcode, cmd)
      subprocess.CalledProcessError: Command '['cmake', '--build', '.', '-j=192', '--target=vllm_ascend_C']' returned non-zero exit status 2.
```
