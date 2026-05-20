# Issue #733: [Guide]: Sleep mode feature guide

## 基本信息

- **编号**: #733
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/733
- **创建时间**: 2025-04-30T01:44:12Z
- **关闭时间**: 2025-06-15T07:53:12Z
- **更新时间**: 2025-06-15T07:53:12Z
- **提交者**: @antonlisq
- **评论数**: 0

## 标签

RFC

## 问题描述

## Installation

To use sleep mode, a compiled module `vllm_ascend.vllm_ascend_C` is needed. Environment variable switch for compilation is different by default for v0.7.3 and v0.8.x+. So installation process can be slightly different. You should follow the latest official [installation guide](https://vllm-ascend.readthedocs.io/en/latest/installation.html). Be sure to do the installation step by step, every sentence of the guide is there for a reason.

### For v0.7.3

If you are building from source, you should run `export COMPILE_CUSTOM_KERNELS=1` manually. So that it will compile during installation.

### For v0.8.x+

Environment variable `COMPILE_CUSTOM_KERNELS` will be set `1` by default while building from source.

## Usage

```Python
    llm = LLM("Qwen/Qwen2.5-0.5B-Instruct", enable_sleep_mode=True)

    # NPU HBM usage will significantly decrease  
    # Equivalent to calling .sleep()
    llm.sleep(level=1)

    # Restore from sleep state
    llm.wake_up()
```

The usage is quite simple.

**Important Notes:**
- The `level` parameter defaults to `1` when using sleep()
- Passing values other than `1` to `level` will keep model weights on NPU while only discarding the KV cache

## Verify

If you need to ensure sleep mode runs normally on your env, you can run `pytest -sv tests/singlecard/test_camem.py` on main branch. In this file there are 2 test cases. `test_basic_camem` tests if `CaMemAllocator` functions normally. `test_end_to_end` makes sure `.sleep()` can reduce most HBM usage, and `.wake_up()` can resume the model and produce the same output as before sleeping.

## FAQs

### Error libruntime.so undefined symbol during compilation

```bash
#14 45.82     ImportError: /usr/local/Ascend/ascend-toolkit/latest/lib64/libruntime.so:
#14 45.82     undefined symbol:
#14 45.82     _ZN12ErrorManager19ATCReportErrMessageESsRKSt6vectorISsSaISsEES4_
```

As is discussed in #661 , the problem is due to the bad order of `LD_LIBRARY_PATH` setting. You should do the CANN env initialize with:

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh && \
source /usr/local/Ascend/nnal/atb/set_env.sh && \
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/Ascend/ascend-toolkit/latest/`uname -i`-linux/devlib
```

Notice the third line, by the right order of `LD_LIBRARY_PATH` setting, this problem can be solved.
