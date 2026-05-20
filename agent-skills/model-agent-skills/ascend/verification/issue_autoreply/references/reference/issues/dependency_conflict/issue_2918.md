# Issue #2918: [Bug]: vllm serve crash due to causal_conv1d_fn error under aclgraph mode

## 基本信息

- **编号**: #2918
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2918
- **创建时间**: 2025-09-14T11:37:11Z
- **关闭时间**: 2025-12-23T12:49:55Z
- **更新时间**: 2025-12-23T12:49:55Z
- **提交者**: @Yikun
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

Reproduce step:

```
# Run vllm serve
vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen3-Next-80B-A3B-Instruct --tensor-parallel-size 4

# Run benchmark
vllm bench serve --model /root/.cache/modelscope/hub/models/Qwen/Qwen3-Next-80B-A3B-Instruct   --dataset-name random --random-input-len 200 --num-prompts
 200 --request-rate 1   --save-result --result-dir ./
```

### 🐛 Describe the bug
ERROR1:

<details>

```
(APIServer pid=36486) INFO:     127.0.0.1:34204 - "POST /v1/completions HTTP/1.1" 200 OK
[rank1]:[W914 11:34:43.452457787 compiler_depend.ts:57] Warning: EZ9999: Inner Error!
EZ9999: [PID: 37027] 2025-09-14-11:34:42.060.622 The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 2, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x60199c4e36, mte error info: 0xee06000042, ifu error info: 0x11b909f3ebd00, ccu error info: 0xc1f119ca50b380f8, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
        TraceBack (most recent call last):
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:27, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 3, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xbb071d61ce, mte error info: 0xee06000042, ifu error info: 0x381700de32880, ccu error info: 0x34c1abe55960400d, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:28, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 4, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xeb01f52358, mte error info: 0xee06000042, ifu error info: 0xb6738a8ac00, ccu error info: 0x606c21c458f1339f, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:29, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 5, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xfb16137824, mte error info: 0xee06000042, ifu error info: 0x650d462469780, ccu error info: 0xd19e205c1e84eeea, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:30, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 7, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x4b155d9b1c, mte error info: 0xee06000042, ifu error info: 0x6327b2e600ac0, ccu error info: 0x738b0468789001b3, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:32, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 8, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x611577029b, mte error info: 0xee06000042, ifu error info: 0x1e2ebf3ee0f80, ccu error info: 0xcb03e0dd020f0fae, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:33, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 9, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xe111d53c9c, mte error info: 0xee06000042, ifu error info: 0x60971bef142c0, ccu error info: 0x89386115be00023, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:34, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 19, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xe110ff5492, mte error info: 0xee06000042, ifu error info: 0x390910296e040, ccu error info: 0x810fe85017101103, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:0, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 22, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x7b05e141fc, mte error info: 0xee06000042, ifu error info: 0x4b90e0d84c880, ccu error info: 0x1930035e088691a7, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:1, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 23, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xe10eb1309a, mte error info: 0xee06000042, ifu error info: 0x5b31f6bdb9d80, ccu error info: 0xaf99b3ee150c21ac, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:2, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 25, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xfb17179a41, mte error info: 0xee06000042, ifu error info: 0x3e178383288c0, ccu error info: 0x314e6cac74a3b83b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:4, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 26, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x5c17f4479d, mte error info: 0xee06000042, ifu error info: 0x9e74a6038c00, ccu error info: 0x77043b810608d4b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:5, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 35, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x7709db6e5c, mte error info: 0xee06000042, ifu error info: 0x69412ffddf8c0, ccu error info: 0xe17189f32ea5303a, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:10, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 36, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x6b1ed8b854, mte error info: 0xee06000042, ifu error info: 0xbfdf32848380, ccu error info: 0xb6b6c8e13791ec72, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:11, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 39, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xd10a442b22, mte error info: 0xee06000042, ifu error info: 0x1657671ace880, ccu error info: 0x1e6c30f43f060eff, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:14, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 40, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x401df24711, mte error info: 0xee06000042, ifu error info: 0x3aa2723078f80, ccu error info: 0x80c3fb0f344301f9, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:15, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 45, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xed14b50c9b, mte error info: 0xee06000042, ifu error info: 0x63016a0677ac0, ccu error info: 0x813bfdad71e05213, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:20, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 47, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x7d067da940, mte error info: 0xee06000042, ifu error info: 0x38237a95c0100, ccu error info: 0x1c0ff02875e80ab3, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:22, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 49, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x410fd4c412, mte error info: 0xee06000042, ifu error info: 0x14bd84418b400, ccu error info: 0x487c258e7f423eff, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:0, tslot:0, thread:0, ctxid:0, blk:24, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 0, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xed025602be, mte error info: 0xee06000042, ifu error info: 0x3962278682fc0, ccu error info: 0x73e422c15987b1f1, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:25, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 1, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x710fbff595, mte error info: 0xee06000042, ifu error info: 0x3408e300f17c0, ccu error info: 0xd6223c085b9c2283, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:26, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 6, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x211fb70d74, mte error info: 0xee06000042, ifu error info: 0x102ff6cf1ff80, ccu error info: 0x1fe186b0689f182b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:31, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 10, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x611ef42a00, mte error info: 0xee06000042, ifu error info: 0x3e004781e0000, ccu error info: 0x14002a91e1e00fc, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:35, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 11, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x670373e8b4, mte error info: 0xee06000042, ifu error info: 0x6de18b9d44180, ccu error info: 0x533eb4ed10a01ed8, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:36, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 12, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x3b0656da3e, mte error info: 0xee06000042, ifu error info: 0x5f3afb9b86040, ccu error info: 0x91f0214c5b2f888b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:37, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 13, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x9b029aeb8c, mte error info: 0xee06000042, ifu error info: 0x3a53fb5e6e0c0, ccu error info: 0x87efdc2418710381, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:38, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 18, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x6214be1da5, mte error info: 0xee06000042, ifu error info: 0x67fbfa819dd80, ccu error info: 0x885afa744e87c3f2, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:39, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 24, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xe202f9ba3c, mte error info: 0xee06000042, ifu error info: 0x32afcc0c1d00, ccu error info: 0x1926ca922a04056a, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:3, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 27, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xeb0a252725, mte error info: 0xee06000042, ifu error info: 0x54e0560e59d00, ccu error info: 0x4661038077850620, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:6, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 32, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xb71f1aa00e, mte error info: 0xee06000042, ifu error info: 0x73339e1feee80, ccu error info: 0x4c9102c34f7e30cb, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:7, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 33, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x601ed1535d, mte error info: 0xee06000042, ifu error info: 0x2d10b618a0ac0, ccu error info: 0x8782145b76b103ba, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:8, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 34, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x4a0043523a, mte error info: 0xee06000042, ifu error info: 0x53de3e2dccc0, ccu error info: 0xe2e3eab100577008, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:9, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 37, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x7b07d1282c, mte error info: 0xee06000042, ifu error info: 0x7b151cd12d4c0, ccu error info: 0x2373e1a0101903bb, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:12, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 38, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x7315f0f86c, mte error info: 0xee06000042, ifu error info: 0x5b4d01f7be40, ccu error info: 0x9443b408300300e4, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:13, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 41, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x5a1f5fba80, mte error info: 0xee06000042, ifu error info: 0x2d016029d8000, ccu error info: 0x4267c42d7ca16617, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:16, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 42, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xd104f5122e, mte error info: 0xee06000042, ifu error info: 0x11630f3303f80, ccu error info: 0x1ac246eb08d10c8f, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:17, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 43, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x6319bbc102, mte error info: 0xee06000042, ifu error info: 0x1e9146012c600, ccu error info: 0x26f203812ee6a2be, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:18, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 44, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x610eb7939f, mte error info: 0xee06000042, ifu error info: 0x7eb0d02a80680, ccu error info: 0xc78b8c4a15ad50d2, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:19, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 46, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0xf90fff8e68, mte error info: 0xee06000042, ifu error info: 0x1facca2808880, ccu error info: 0x59adc6d6498685a3, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:21, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:5, dieId:0), serial number is 11, there is an exception of aivec error, core id is 48, error code = 0x800000, dump info: pc start: 0x12523dffb6fc, current: 0x12523dffb8a8, vec error info: 0x790bb0f035, mte error info: 0xee06000042, ifu error info: 0x3d2b1baae4fc0, ccu error info: 0x6421d7117c7ad0b3, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124240536400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x6000042, fixp_error1 info: 0xee, fsmId:1, tslot:0, thread:0, ctxid:0, blk:23, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       Kernel task happen error, retCode=0x31, [vector core exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1539]
       AIV Kernel happen error, retCode=0x31.[FUNC:GetError][FILE:stream.cc][LINE:1183]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1183]
       Aicore kernel execute failed, device_id=1, stream_id=2, report_stream_id=2, task_id=34009, flip_num=3, fault kernel_name=reshape_and_cache_200000000, fault kernel info ext=none, program id=387, hash=15033883741634815243.[FUNC:GetError][FILE:stream.cc][LINE:1183]
       rtStreamSynchronize execute failed, reason=[suspect remote error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 507057[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
 (function copy_between_host_and_device_opapi)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654] WorkerProc hit an exception.
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 213, in execute_model
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return func(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1764, in execute_model
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1419, in _generate_process_reqs_hidden_states
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     hidden_states = self.model(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 1328, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 312, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     model_output = self.forward(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 1089, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     def forward(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return fn(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     raise e
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "<eval_with_key>.98", line 374, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     submod_9 = self.submod_9(getitem_16, s0, getitem_17);  getitem_16 = submod_9 = None
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     raise e
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "<eval_with_key>.10", line 5, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     gdn_attention = torch.ops.vllm.gdn_attention(x_51, self_attention_output_4, 'model.layers.4.linear_attn');  x_51 = self_attention_output_4 = gdn_attention = None
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._op(*args, **(kwargs or {}))
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 1388, in gdn_attention
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     self._forward(hidden_states=hidden_states, output=output)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 614, in _forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     mixed_qkv_non_spec = causal_conv1d_fn(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                          ^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/casual_conv1d.py", line 115, in causal_conv1d_fn
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     seqlens = seqlens.tolist()
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]               ^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654] RuntimeError: ACL stream synchronize failed, error code:507057
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 213, in execute_model
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return func(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1764, in execute_model
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1419, in _generate_process_reqs_hidden_states
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     hidden_states = self.model(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 1328, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 312, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     model_output = self.forward(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 1089, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     def forward(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return fn(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     raise e
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "<eval_with_key>.98", line 374, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     submod_9 = self.submod_9(getitem_16, s0, getitem_17);  getitem_16 = submod_9 = None
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     raise e
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "<eval_with_key>.10", line 5, in forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     gdn_attention = torch.ops.vllm.gdn_attention(x_51, self_attention_output_4, 'model.layers.4.linear_attn');  x_51 = self_attention_output_4 = gdn_attention = None
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     return self._op(*args, **(kwargs or {}))
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 1388, in gdn_attention
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     self._forward(hidden_states=hidden_states, output=output)
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 614, in _forward
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     mixed_qkv_non_spec = causal_conv1d_fn(
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]                          ^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/casual_conv1d.py", line 115, in causal_conv1d_fn
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]     seqlens = seqlens.tolist()
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654]               ^^^^^^^^^^^^^^^^
(Worker_TP1 pid=37027) ERROR 09-14 11:34:43 [multiproc_executor.py:654] RuntimeError: ACL stream synchronize failed, error code:507057
```

</details>

