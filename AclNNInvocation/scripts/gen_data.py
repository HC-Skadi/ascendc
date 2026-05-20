#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright 2022-2023 Huawei Technologies Co., Ltd
import numpy as np
import os
import torch
import torch.nn.functional as F 
import ml_dtypes 

def float32_to_bfloat16(x_fp32: np.ndarray):
    assert x_fp32.dtype == np.float32
    x_uint32 = x_fp32.view(np.uint32)
    x_bf16 = (x_uint32 >> 16).astype(np.uint16)
    return x_bf16

def get_golden_bfloat16():
    input_x = np.random.uniform(-5, 5, [2, 4, 8, 1]).astype(np.float32)
    alpha = np.random.uniform(-5, -1, [4]).astype(np.float32)
    # input_x = np.random.randint(-5, 6, size=(2,4,8,1)).astype(np.float32)  # 包含 -5 和 5
    # alpha = np.random.randint(-5, 6, size=(4,)).astype(np.float32)  

    # 2. 将 NumPy 数组转换为 PyTorch 张量 (关键修改)
    x_torch = torch.from_numpy(input_x)
    alpha_torch = torch.from_numpy(alpha)

    # x_torch = torch.randn(2, 4, 8, 1, dtype=torch.float32)
    # alpha_torch = torch.randn(1, dtype=torch.float32)
    golden_torch = F.prelu(x_torch, alpha_torch)

    x_fp32 = x_torch.float().numpy()
    alpha_fp32 = alpha_torch.float().numpy()
    golden_fp32 = golden_torch.float().numpy()

    x_bf16 = float32_to_bfloat16(x_fp32)
    alpha_bf16 = float32_to_bfloat16(alpha_fp32)
    golden_bf16 = float32_to_bfloat16(golden_fp32)

    os.system("mkdir -p input")
    os.system("mkdir -p output")

    x_bf16.tofile("./input/input_x.bin")
    alpha_bf16.tofile("./input/input_w.bin")
    golden_bf16.tofile("./output/golden.bin")
    
    print("\nFiles generated successfully!")

def prelu(x, alpha):
    """
    PReLU activation function
    y = x if x > 0 else alpha * x
    """
    return np.where(x > 0, x, alpha * x)

def gen_golden():
    x = np.random.randn(16, 32).astype(np.float16)
    alpha = np.random.randn(32).astype(np.float16)
    golden = prelu(x, alpha)
    # golden = np.prelu(x, alpha)

    # import torch.nn.functional as F 
    # golden = F.prelu(x, alpha)
    print("x shape:", x.shape, x[0].dtype)
    print("alpha shape:", alpha.shape, alpha[0].dtype)
    print("golden shape:", golden.shape, golden[0].dtype)
   

    os.system("mkdir -p input")
    os.system("mkdir -p output")

    x.tofile("./input/input_x.bin")
    alpha.tofile("./input/input_w.bin")
    golden.tofile("./output/golden.bin")
    
    print("\nFiles generated successfully!")

def gen_golden_fp32():
    x_torch = torch.randn(1, 512, 32, dtype=torch.float)
    alpha_torch = torch.randn(512, dtype=torch.float)
    x_fp16 = x_torch.numpy()
    alpha_fp16 = alpha_torch.numpy()
      
    golden = F.prelu(x_torch, alpha_torch)
    golden_fp16 = golden.numpy().astype(np.float32)

    print("golden_fp16 :", golden_fp16.shape)
    
    os.system("mkdir -p input")
    os.system("mkdir -p output")

    x_fp16.tofile("./input/input_x.bin")
    alpha_fp16.tofile("./input/input_w.bin")
    golden_fp16.tofile("./output/golden.bin")
    
    print("\nFiles generated successfully!")

def gen_golden_bf16():

    # 生成 float32 数据，然后转换为 bfloat16
    input_x = np.random.uniform(-5, 5, [2, 4, 8, 1]).astype(ml_dtypes.bfloat16)
    alpha = np.random.uniform(-5, -1, [4]).astype(ml_dtypes.bfloat16)

    # 2. 将 NumPy 数组转换为 PyTorch 张量 (关键修改)
    x_torch = torch.from_numpy(input_x.astype(np.float32))
    alpha_torch = torch.from_numpy(alpha.astype(np.float32))

    # 3. 计算 PReLU
    
    golden = F.prelu(x_torch, alpha_torch)
    golden_fp16 = golden.numpy().astype(ml_dtypes.bfloat16)
    
    os.system("mkdir -p input")
    os.system("mkdir -p output")

    input_x.tofile("./input/input_x.bin")
    alpha.tofile("./input/input_w.bin")
    golden_fp16.tofile("./output/golden.bin")
    
    print("\nFiles generated successfully!")#[32, 16384];[32, 1365*16];32, (1320*3)*16;368;[1, (31*64+48)]


if __name__ == "__main__":
    # gen_golden()
    # get_golden_bfloat16()
    # gen_golden_fp16()
    gen_golden_fp32()
