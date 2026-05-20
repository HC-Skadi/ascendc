# Issue #2178: [Usage]: 310p的镜像找不到linux on arm64的

## 基本信息

- **编号**: #2178
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2178
- **创建时间**: 2025-08-02T08:57:06Z
- **关闭时间**: 2025-12-23T11:31:40Z
- **更新时间**: 2025-12-23T11:31:40Z
- **提交者**: @diaody
- **评论数**: 2

## 标签

310p

## 问题描述

### Your current environment

WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
我现在遇到的一个问题是找不到支持linux on arm64的310p的镜像。下载页面（https://quay.io/repository/ascend/vllm-ascend?tab=tags&tag=latest）显示应该是有arm64版本的但是下载不到；下面是另一个镜像版本（https://docker.aityp.com/image/quay.io/ascend/vllm-ascend:v0.9.2rc1-310p-openeuler），显示310p只有amd64版本？ 


### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

