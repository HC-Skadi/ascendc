# Issue #5352: [Bug]: accuracy issue for triton kernel split_qkv_rmsnorm_rope_kernel

## 基本信息

- **编号**: #5352
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5352
- **创建时间**: 2025-12-25T06:59:46Z
- **关闭时间**: 2025-12-30T03:29:49Z
- **更新时间**: 2025-12-30T03:29:49Z
- **提交者**: @Meihan-chen
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment


When running the Triton kernel on the NPU ，and comparing the results with the results of the Torch operator corresponding to the Triton kernel running on the GPU, it was found that the precision of the Triton kernel was not aligned.

### 🐛 Describe the bug

```bash
pytest -v test_split_qkv_rmsnorm_rope_kernel.py
================================================================================== test session starts ==================================================================================
platform linux -- Python 3.11.13, pytest-8.4.2, pluggy-1.6.0 -- /usr/local/python3.11.13/bin/python3.11
cachedir: .pytest_cache
rootdir: /triton-ascend
configfile: pyproject.toml
plugins: mock-3.15.1, cov-7.0.0, asyncio-1.3.0, anyio-4.12.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

test_split_qkv_rmsnorm_rope_kernel.py::test_split_qkv_rmsnorm_rope_kernel FAILED                                                                                                  [100%]

======================================================================================= FAILURES ========================================================================================
__________________________________________________________________________ test_split_qkv_rmsnorm_rope_kernel ___________________________________________________________________________

    def test_split_qkv_rmsnorm_rope_kernel():
        try:
            data = torch.load(ptfile_path, map_location=torch.device('cpu'), weights_only=False)
        except Exception as e:
            pytest.fail(f"load file {ptfile_path} failed: {str(e)}")

        input_data = test_common.convert_tensor_with_device_type(data["input_data"], device_type='npu')

        # Run NPU kernel and get outputs
        q_npu, k_npu, v_npu = split_qkv_rmsnorm_rope_impl(**input_data)

        # Prepare NPU output dict for comparison
        npu_output = {
            "q": q_npu.to(torch.float32).cpu(),
            "k": k_npu.to(torch.float32).cpu(),
            "v": v_npu.to(torch.float32).cpu(),
        }

        # compare the results of GPU and NPU.
        try:
>           test_common.compare_data_precision(data["gpu_output"], npu_output, device_type='cpu')

test_split_qkv_rmsnorm_rope_kernel.py:308:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
test_common.py:110: in compare_data_precision
    validate_cmp(dtype=str(val_a.dtype).split('.')[-1], y_ref=val_a, y_cal=val_b, device_type=device_type)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

dtype = 'float32'
y_cal = tensor([[-1.2793e-01, -9.7266e-01, -2.8906e-01,  ..., -1.3281e-01,
          8.6426e-02,  3.5477e-04],
        [ 3.808...,  1.1475e-01],
        [-6.7871e-02, -5.1953e-01, -6.0547e-01,  ..., -1.3477e-01,
         -1.4922e+00, -3.4961e-01]])
y_ref = tensor([[-1.2778e-01, -9.7404e-01, -2.8927e-01,  ..., -1.3219e-01,
          8.6911e-02,  3.6788e-04],
        [ 3.839...,  1.1476e-01],
        [-6.7658e-02, -5.2061e-01, -6.0585e-01,  ..., -1.3473e-01,
         -1.4956e+00, -3.4953e-01]])
overflow_mode = None, device_type = 'cpu'

    def validate_cmp(dtype, y_cal, y_ref, overflow_mode: Optional[str] = None, device_type: Optional[str] = None):
        if device_type is not None:
            target_device = torch.device(device_type)
            y_cal = y_cal.to(target_device)
            y_ref = y_ref.to(target_device)
        else:
            y_cal=y_cal.npu()
            y_ref=y_ref.npu()
        if overflow_mode == "saturate":
            if dtype in ['float32', 'float16']:
                min_value = -torch.finfo(dtype).min
                max_value = torch.finfo(dtype).max
            elif dtype in ['int32', 'int16', 'int8']:
                min_value = torch.iinfo(dtype).min
                max_value = torch.iinfo(dtype).max
            elif dtype == 'bool':
                min_value = 0
                max_value = 1
            else:
                raise ValueError('Invalid parameter "dtype" is found : {}'.format(dtype))
            y_ref = torch.clamp(y_ref, min=min_value, max=max_value)
        if dtype == 'float16':
            torch.testing.assert_close(y_ref, y_cal, rtol=5e-03, atol=5e-03, equal_nan=True)
        elif dtype == 'bfloat16':
            torch.testing.assert_close(y_ref.to(torch.float32), y_cal.to(torch.float32), rtol=5e-03, atol=5e-03, equal_nan=True)
        elif dtype == 'float32':
>           torch.testing.assert_close(y_ref, y_cal, rtol=1e-03, atol=1e-03, equal_nan=True)
E           AssertionError: Tensor-likes are not close!
E
E           Mismatched elements: 1044 / 8192 (12.7%)
E           Greatest absolute difference: 0.02156686782836914 at index (3, 231) (up to 0.001 allowed)
E           Greatest relative difference: 0.3376116156578064 at index (3, 1255) (up to 0.001 allowed)

test_common.py:74: AssertionError
================================================================================ short test summary info ================================================================================
FAILED test_split_qkv_rmsnorm_rope_kernel.py::test_split_qkv_rmsnorm_rope_kernel - AssertionError: Tensor-likes are not close!
=================================================================================== 1 failed in 4.66s
```

test code：https://gitcode.com/Ascend/triton-ascend/pull/980
torch ops ：https://github.com/vllm-project/vllm-ascend/pull/5267
