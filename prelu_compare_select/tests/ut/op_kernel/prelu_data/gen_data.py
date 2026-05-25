#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np

import numpy as np


def impl(x, weight):
    """
    PReLU（Parametric ReLU）算子实现

    参数:
    x:      输入张量 (ND数组)
    weight: 权重张量，形状为 [C]（per-channel）或 [1]（scalar）

    返回:
    y:      输出张量，形状与 x 相同

    公式:
    f(x) = max(x, 0) + min(x, 0) * weight

    约束:
    1. x 与 weight 的数据类型必须一致
    2. 支持 float16, float32, bfloat16
    3. per-channel weight 的形状必须为 [C]，其中 C 等于 x.shape[1]
    4. 内部计算提升至 float32 以保证精度
    """
    # 统一提升至 float32 计算
    x_f32 = x.astype(np.float32)
    w_f32 = weight.astype(np.float32)

    # 处理 per-channel weight 的广播形状
    # 若 weight 是一维且元素数大于1，视为 per-channel，需要将其形状调整为 (1, C) + (1,)*(x.ndim-2)
    if w_f32.ndim == 1 and w_f32.shape[0] > 1:
        # 目标形状: (1, C, 1, 1, ...) 以便广播到 x 的通道维
        target_shape = (1, w_f32.shape[0]) + (1,) * (x_f32.ndim - 2)
        w_f32 = w_f32.reshape(target_shape)

    # 核心计算：max(x, 0) + min(x, 0) * weight
    y_f32 = np.maximum(x_f32, 0.0) + np.minimum(x_f32, 0.0) * w_f32

    # 转回原始数据类型
    return y_f32.astype(x.dtype)


if __name__ == "__main__":
    # 清理bin文件
    os.system("rm -rf *.bin")
    
    # 从 JSON 第一个 case 获取参数
    d_type = "float32"
    d_type_dict = {
        "float32": np.float32,
        "float16": np.float16,
        "int32": np.int32,
        "int8": np.int8,
    }
    np_type = d_type_dict[d_type]
    
    # 生成输入数据
    input_x = np.random.uniform(-10.0, 10.0, (7)).astype(np_type)
    input_weight = np.random.uniform(-5.0, 5.0, (1)).astype(np_type)

    
    # 计算 golden 数据
    golden = impl(input_x, input_weight)
    
    # 保存数据到文件
    input_x.astype(np_type).tofile(f"{d_type}_input_prelu_x.bin")
    input_weight.astype(np_type).tofile(f"{d_type}_input_prelu_weight.bin")
    golden.astype(np_type).tofile(f"{d_type}_golden_prelu.bin")
    
    print(f"生成完成: dtype={d_type}")
