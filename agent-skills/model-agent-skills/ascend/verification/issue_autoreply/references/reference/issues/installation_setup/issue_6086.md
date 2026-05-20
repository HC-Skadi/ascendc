# Issue #6086: Mix placement

**类型**: Pull Request

## 问题背景
# Feature: Support Unified Placement for Shared & Router Experts

## Overview

This pull request (PR) implements core enhancements to enable unified placement of shared and router experts in the Mixture of Experts (MoE) architecture. Its primary objective is to optimize the deployment strategy and inference execution logic for both expert types, thereby enhancing cross-device load balancing via the Expert Load Balancer (EPLB) and improving overall inference efficiency.

## Key Changes

### 1. Shared Expert Weight Loading Enhancement
* Implemented specialized weight loading logic for shared experts to support their unified deployment with router experts, breaking the original constraint of fixed shared expert deployment on each device.
* Ensured seamless integration with the existing weight loading pipeline while maintaining full compatibility with standard Expert Parallelism (EP) mechanisms.

### 2. TopK+1 Routing Extension

* Extended TopK routing to TopK+1 routing, enab

## 基本信息
- **编号**: #6086
- **作者**: Mercykid-bash
- **创建时间**: 2026-01-21T07:32:51Z
- **关闭时间**: 2026-01-23T01:07:59Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6086)
