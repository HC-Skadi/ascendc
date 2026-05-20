# aclnn_gen/generation/build_script_generator.py
from aclnn_gen.parsing.op_parser import OperatorDefinition

class BuildScriptGenerator:
    """Generates a simple build.sh script focused solely on compilation."""

    def __init__(self, op_def: OperatorDefinition):
        self.op_def = op_def

    def generate_content(self) -> str:
        """
        Creates the full content of the build_aclnn.sh file as a string.
        """
        project_name = self.op_def.op_name_snake
        executable_name = f"execute_{project_name}_op"
        return f"""#!/bin/bash
set -e

# This script is for compiling the C++ project only.

# ==============================================================================
# 1. ENVIRONMENT SETUP
# ==============================================================================
# Find Ascend installation path
if [ -n "$ASCEND_INSTALL_PATH" ]; then
    _ASCEND_INSTALL_PATH=$ASCEND_INSTALL_PATH
elif [ -n "$ASCEND_HOME_PATH" ]; then
    _ASCEND_INSTALL_PATH=$ASCEND_HOME_PATH
else
    if [ -d "$HOME/Ascend/ascend-toolkit/latest" ]; then
        _ASCEND_INSTALL_PATH=$HOME/Ascend/ascend-toolkit/latest
    else
        # Default fallback path
        _ASCEND_INSTALL_PATH=/usr/local/Ascend/ascend-toolkit/latest
    fi
fi

# Source the official environment script
echo "INFO: Sourcing environment from $_ASCEND_INSTALL_PATH/bin/setenv.bash"
set +e
source "$_ASCEND_INSTALL_PATH/bin/setenv.bash"
set -e
echo "INFO: Environment setup complete."
echo ""

# ==============================================================================
# 2. BUILD THE PROJECT
# ==============================================================================
echo "INFO: Building the project..."

# Create a build directory and navigate into it
BUILD_DIR="build"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Run cmake and make
cmake .. -DCMAKE_SKIP_RPATH=TRUE
make

echo ""
echo "Build successful. The executable '{executable_name}' is in the '$BUILD_DIR' directory."
echo ""
exit 0
"""