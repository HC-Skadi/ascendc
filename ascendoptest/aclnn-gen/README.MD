# aclnnGen: ACLNN 算子工程自动化生成工具

`aclnnGen` 是一款命令行工具，旨在全自动化生成昇腾（Ascend）CANN平台下，基于ACLNN接口的C++算子测试工程。它支持**自定义算子**和**内置算子**，通过解析算子原型和测试用例JSON文件，一键生成包含多用例调度逻辑的C++源代码、CMake构建系统和自动化编译脚本，帮助开发者极大提升测试效率。

## 安装

本项目通过源码编译打包的方式进行安装。请确保您已安装 Python 3.8+。

**1. 安装依赖**

请先安装依赖。
```bash
pip install -r requirements.txt
```

**2. 构建 Wheel 包**

在项目根目录下，执行以下命令：
```bash
python -m build
```
该命令会在项目根目录创建一个 `dist/` 文件夹，其中包含了 `.whl` 安装包文件。

**3. 安装 Wheel 包**

```bash
# 注意：请使用实际生成的文件名
pip install dist/aclnn_codegen-0.0.2-py3-none-any.whl
```

安装完成后，`aclnngen` 命令将在您的终端中全局可用。您可以通过 `aclnngen -h` 来验证安装是否成功。

## 使用方法

`aclnnGen` 的核心工作流是“一次性生成，多用例运行”。您只需生成一次项目代码，即可通过命令行参数反复运行不同的测试用例，并在每次运行时使用不同的时间戳来隔离测试数据，无需重新编译。工具支持两种模式：custom（自定义算子）和 built-in（内置算子）。

### 1. 准备输入文件

您需要准备两个JSON文件：

-   **`prototype.json`**: 定义算子的通用接口（名称、输入、输出、属性）。
-   **`cases.json`**: 一个JSON列表，其中包含一个或多个具体的测试用例（Test Case）配置。

### 2. 生成项目

在终端中执行以下命令，生成完整的C++测试工程：

#### 场景 A：自定义算子 (Custom Operator)
需要提供自定义算子包的部署路径。

```bash
# 命令格式: aclnngen <原型文件> <用例文件> -o <输出目录> --op-type custom --op-path <算子包路径>
aclnngen Add_Custom.json add_custom_cases.json -o my_add_test --op-type custom --op-path /home/ma-user/Ascend/opp/vendors/customize/op_api
```
-   `--op-path`: 自定义算子包的安装路径（包含 `include` 和 `lib` 的父目录）。

#### 场景 B：内置算子 (Built-in Operator)
直接生成，无需额外路径。

```bash
# 命令格式: aclnngen built-in <原型文件> <用例文件> -o <输出目录> --op-type built-in
aclnngen Add.json add_cases.json -o my_builtin_test --op-type built-in
```

输出目录下会生成：
-   `src/aclnn_<op_name>.cpp`：包含所有测试用例逻辑的C++源代码。
-   `CMakeLists.txt`：用于编译项目的CMake文件。
-   `build_aclnn.sh`：自动化编译脚本。

### 3. 编译与运行

1.  **进入项目目录**
    ```bash
    cd my_add_test
    ```

2.  **准备测试数据**
    -   如果您的 `cases.json` 文件中指定了数据路径 (`data_path`)，请确保这些二进制文件存在。
    -   如果未指定，`aclnnGen` 会在 `case_path` (或当前目录)下寻找 `op_test/<op_name>_<case_name>_<timestamp>/` 目录结构，您需要将生成的二进制数据放入其中。
    - `<case_name>` 与 `<timestamp>` 来自后续调用算子时传入的参数。
    -   *(推荐)* 您可以编写一个 `gen_data.py` 脚本来自动完成数据生成。

3.  **编译项目**
    执行 `build_aclnn.sh` 脚本进行编译。
    ```bash
    ./build_aclnn.sh
    ```
    编译成功后，将在 `build/` 目录下生成可执行文件 `execute_add_custom_op`。

4.  **运行指定的测试用例**
    通过 `--case_name` 和 `--timestamp` 参数来运行您想测试的特定用例，并使用时间戳隔离结果。
    ```bash
    # 运行名为 "Test_001" 的用例
    ./build/execute_add_custom_op --case_name Test_001 --timestamp 20250828153000
    ```
    程序执行后，输出的二进制文件将保存在预设目录下。

### 4. 高级功能：动态输出形状

如果算子的输出形状在运行时是可能动态变化的，可以通过 `--output_shapes` 参数传递 Python 字典风格的字符串来覆盖 `cases.json` 中的默认形状。

**直接运行编译后的程序示例：**

```bash
cd build
./build/execute_add_custom_op --case_name Test_001 \
--timestamp 20250828153000 \
--output_shapes "{'y': [(1, 1024)], 'idx': [(1, 1024)]}"
```