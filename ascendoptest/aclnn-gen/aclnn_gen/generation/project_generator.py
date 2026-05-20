# aclnn_gen/generation/project_generator.py
import os
from aclnn_gen.parsing.op_parser import OperatorDefinition
from aclnn_gen.generation.cpp_generator import CppGenerator
from aclnn_gen.generation.cmake_generator import CMakeGenerator
from aclnn_gen.generation.build_script_generator import BuildScriptGenerator

class ProjectGenerator:
    """
    Orchestrates the generation of a flattened, multi-case aclnn test project,
    with a build script focused solely on compilation.
    """

    def __init__(self, op_def: OperatorDefinition, processed_cases: list, op_path: str, op_type: str):
        """
        Initializes the ProjectGenerator.
        """
        self.op_def = op_def
        self.cases = processed_cases
        self.op_path = op_path
        self.op_type = op_type
        self.project_name = self.op_def.op_name_snake

    def generate(self, output_base_dir: str):
        """
        Generates the project files (cpp, sh, cmake) directly into the project root.
        """
        # Determine the final project root directory
        if output_base_dir == ".":
            project_root = os.path.join(output_base_dir, self.project_name)
        else:
            project_root = output_base_dir
        
        # Create the project root directory if it doesn't exist
        os.makedirs(project_root, exist_ok=True)
        print(f"Project files will be generated in: {os.path.abspath(project_root)}")

        # 1. 生成 C++ 文件
        cpp_filename = self._generate_cpp_file(project_root)

        # 2. 生成 CMakeLists.txt
        # Pass the simplified cpp_filename (no path)
        self._generate_cmake_file(project_root, cpp_filename)

        # 3. 生成 build_aclnn.sh 脚本
        self._generate_build_script(project_root)

        print(f"\nProject '{self.project_name}' generated successfully!")


    def _generate_cpp_file(self, project_root: str) -> str:
        """Generates the .cpp file directly in the project root."""
        cpp_gen = CppGenerator(self.op_def, self.cases)
        cpp_code = cpp_gen.generate_code()
        
        filename = f"aclnn_{self.op_def.op_name_snake}.cpp"
        filepath = os.path.join(project_root, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cpp_code)
        print(f"  - Generated C++ source: {filepath}")
        return filename

    def _generate_cmake_file(self, project_root: str, cpp_filename: str):
        """Generates the CMakeLists.txt file directly in the project root."""
        cmake_gen = CMakeGenerator(self.op_def, self.op_path, self.op_type, cpp_filename)
        cmake_content = cmake_gen.generate_content()
        
        filepath = os.path.join(project_root, "CMakeLists.txt")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cmake_content)
        print(f"  - Generated CMakeLists.txt: {filepath}")

    def _generate_build_script(self, project_root: str):
        """Generates the simplified build_aclnn.sh file."""
        script_gen = BuildScriptGenerator(self.op_def)
        script_content = script_gen.generate_content()

        filepath = os.path.join(project_root, "build_aclnn.sh")
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(script_content)
        
        os.chmod(filepath, 0o755)
        print(f"  - Generated build_aclnn.sh: {filepath}")