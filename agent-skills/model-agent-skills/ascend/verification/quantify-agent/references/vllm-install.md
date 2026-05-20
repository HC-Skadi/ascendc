# vLLM-Ascend Installation Playbook

This playbook provides a foolproof method for installing vLLM from source on Ascend NPUs, ensuring version compatibility between the core `vllm` and the `vllm-ascend` plugin.

## 1. Environment Cleanup

Before starting, ensure no conflicting installations exist.

```bash
pip uninstall -y vllm vllm-ascend
```

## 2. Installation Workflow

### Step A: Clone Repositories

Retrieve both the core vLLM engine and the Ascend-specific plugin:

- `git clone https://github.com/vllm-project/vllm.git`
- `git clone https://github.com/vllm-project/vllm-ascend.git`

### Step B: Sync Versions (Crucial)

To avoid ABI/API mismatches, you must sync the `vllm` core to the commit expected by the plugin:

1. Open `vllm-ascend/.github/workflows/pr_test_full.yaml`.
1. Locate the `VLLM_COMMIT` or equivalent identifier.
1. Switch the `vllm` repository to that specific commit:
   ```bash
   cd vllm && git checkout <COMMIT_HASH> && cd ..
   ```

### Step C: Build & Install Core

Install vLLM in editable mode with the `empty` target to bypass CUDA/ROCm build requirements:

```bash
cd vllm
VLLM_TARGET_DEVICE=empty pip install -v -e .
cd ..
```

### Step D: Build & Install Plugin

Install the Ascend plugin in editable mode to allow for source-level debugging:

```bash
cd vllm-ascend
pip install -v -e .
cd ..
```

## 3. Verification

Verify the installation by checking the installed packages and their versions:

```bash
pip list | grep vllm
```

Ensure both `vllm` and `vllm-ascend` are listed and pointing to your local source directories.
