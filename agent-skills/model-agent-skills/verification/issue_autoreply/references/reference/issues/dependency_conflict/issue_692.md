# Issue #692: [Bug]: 昇腾910，RuntimeError，NPU function error: at_npu::native::AclSetCompileopt

## 基本信息

- **编号**: #692
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/692
- **创建时间**: 2025-04-28T03:00:05Z
- **关闭时间**: 2025-05-16T02:32:02Z
- **更新时间**: 2025-07-26T03:19:08Z
- **提交者**: @daiqifeng-sys
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `vllm serve Qwen/Qwen2.5-0.5B-Instruct`</summary>

```text
RuntimeError: SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
[ERROR] 2025-04-28-02:50:24 (PID:1439, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The internal ACL of the system is incorrect.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
EH9999: [PID: 1439] 2025-04-28-02:50:24.965.356 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
       GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
       GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
       [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
       [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
       [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]```

</details>


### 🐛 Describe the bug

<details>
<summary>The output of `vllm serve Qwen/Qwen2.5-0.5B-Instruct`</summary>

```text
RuntimeError: SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
[ERROR] 2025-04-28-02:50:24 (PID:1439, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The internal ACL of the system is incorrect.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
EH9999: [PID: 1439] 2025-04-28-02:50:24.965.356 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
       GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
       GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
       [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
       [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
       [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]```

</details>

