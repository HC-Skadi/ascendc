# aclnn_gen/generation/cmake_generator.py
from aclnn_gen.parsing.op_parser import OperatorDefinition

class CMakeGenerator:
    """
    Generates a conditional CMakeLists.txt file that adapts to both
    'custom' and 'built-in' operator types.
    """

    def __init__(self, op_def: OperatorDefinition, op_path: str, op_type: str, cpp_filename: str):
        """
        Initializes the CMakeGenerator.

        Args:
            op_def (OperatorDefinition): The parsed operator prototype definition.
            op_path (str): The path to the custom operator package.
            op_type (str): The type of the operator ('custom' or 'built-in').
            cpp_filename (str): The name of the main C++ source file.
        """
        self.op_def = op_def
        self.op_path = op_path
        self.op_type = op_type
        self.cpp_filename = cpp_filename

    def generate_content(self) -> str:
        """
        Creates the full content of the CMakeLists.txt file as a string.
        """
        project_name = self.op_def.op_name_snake
        executable_name = f"execute_{project_name}_op"


        # --- Common Header Part ---
        cmake_header = f"""# CMake lowest version requirement
cmake_minimum_required(VERSION 3.5.1)

# Project information
project(acl_execute_{project_name})

# Compile options
add_compile_options(-std=c++11 -fstack-protector-all -D_FORTIFY_SOURCE=2 -O2)
set(CMAKE_CXX_FLAGS "${{CMAKE_CXX_FLAGS}} -Wl,-z,relro,-z,now,-z,noexecstack")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "./")

set(INC_PATH $ENV{{DDK_PATH}})

if (NOT DEFINED ENV{{DDK_PATH}})
    if (EXISTS "/home/ma-user/Ascend/cann-9.0.0-beta.2")
        set(INC_PATH "/home/ma-user/Ascend/cann-9.0.0-beta.2")
    elseif (EXISTS "/usr/local/Ascend/cann-9.0.0-beta.2")
        set(INC_PATH "/usr/local/Ascend/cann-9.0.0-beta.2")
    else()
        set(INC_PATH "/usr/local/Ascend/ascend-toolkit/latest")
    endif()
    message(STATUS "set default INC_PATH: ${{INC_PATH}}")
else ()
    message(STATUS "env INC_PATH: ${{INC_PATH}}")
endif()
"""
        # --- Conditional Blocks ---
        include_paths = [
            "${INC_PATH}/runtime/include",
            "${INC_PATH}/atc/include",
        ]
        link_paths = []
        link_libraries = [
            "ascendcl",
            "acl_op_compiler",
            "nnopbase",
            "stdc++",
        ]
        
        custom_op_block = ""
        if self.op_type == 'custom':
            custom_op_block = f"""
set(LIB_PATH $ENV{{NPU_HOST_LIB}})

# Dynamic libraries in the stub directory can only be used for compilation
if (NOT DEFINED ENV{{NPU_HOST_LIB}})
    set(LIB_PATH "${{INC_PATH}}/lib64")
    set(LIB_PATH1 "${{INC_PATH}}/lib64")
    message(STATUS "set default LIB_PATH: ${{LIB_PATH}}")
else ()
    message(STATUS "env LIB_PATH: ${{LIB_PATH}}")
endif()

set(CUST_PKG_PATH "{self.op_path}")
message(STATUS "Using custom operator package path: ${{CUST_PKG_PATH}}")
"""
            include_paths.append("${CUST_PKG_PATH}/include")
            link_paths.extend([
                "${CUST_PKG_PATH}/lib",
                "${LIB_PATH}",
                "${LIB_PATH1}",
            ])
            link_libraries.append("cust_opapi")
        else: # built-in
            include_paths.append("${INC_PATH}/include/aclnnop")
            include_paths.append("${INC_PATH}/include/aclnnop/level2")
            link_paths.append("${INC_PATH}/lib64")
            link_libraries.append("opapi")

        # --- Assemble the final CMake content ---
        
        # Format include_directories
        include_block = "\ninclude_directories(\n" + "\n".join([f"    {p}" for p in include_paths]) + "\n)\n"
        
        # Format link_directories
        link_block = "\nlink_directories(\n" + "\n".join([f"    {p}" for p in link_paths]) + "\n)\n"
        
        # Format target_link_libraries
        link_lib_block = f"target_link_libraries({executable_name}\n" + "\n".join([f"    {lib}" for lib in link_libraries]) + "\n)"

        cmake_body = f"""
# Add the executable target
add_executable({executable_name}
    {self.cpp_filename}
)

# Link necessary libraries to the executable
{link_lib_block}

# This command is useful if you want 'make install' to do something.
# In our simple case, it just copies the executable to the build directory.
install(TARGETS {executable_name} DESTINATION ${{CMAKE_RUNTIME_OUTPUT_DIRECTORY}})
"""
        return cmake_header + custom_op_block + include_block + link_block + cmake_body
