# Add Kernel 直调样例

Add 算子的 Kernel 直调实现示例。

详细代码说明见 `add.asc` 中的注释（搜索 `[MODIFY]` 标记）。

## 快速开始

```bash
source ${ASCEND_HOME_PATH}/set_env.sh
mkdir -p build && cd build && cmake .. && make -j
cd .. && python3 scripts/gen_data.py
cd build && ./add_custom
python3 ../scripts/verify_result.py output/output.bin output/golden.bin
```
