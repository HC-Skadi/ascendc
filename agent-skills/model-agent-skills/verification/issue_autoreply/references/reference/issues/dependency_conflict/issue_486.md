# Issue #486: [Bug]: HCCL runtime error while GRPO training with co-locating vllm inference across multiple NPUs.

## 基本信息

- **编号**: #486
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/486
- **创建时间**: 2025-04-08T10:23:28Z
- **关闭时间**: 2025-06-16T02:34:50Z
- **更新时间**: 2025-06-16T02:43:31Z
- **提交者**: @Switchsyj
- **评论数**: 10

## 标签

bug

## 问题描述

### Your current environment

```
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: TencentOS Server 4.0 (x86_64)
GCC version: (GCC) 12.2.0 20220819 (TencentOS 12.2.0-5)
Clang version: 14.0.5 (TencentOS 14.0.5-1.tl4)
CMake version: version 4.0.0
Libc version: glibc-2.38

Python version: 3.10.14 (main, May  6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.4.241-1-tlinux4-0017.7-x86_64-with-glibc2.38

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
Model name:                      Intel(R) Xeon(R) Platinum 8476C
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              48
Socket(s):                       2
Stepping:                        8
Frequency boost:                 enabled
CPU max MHz:                     2601.0000
CPU min MHz:                     800.0000
BogoMIPS:                        5200.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid cldemote movdiri movdir64b fsrm md_clear pconfig flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       4.5 MiB (96 instances)
L1i cache:                       3 MiB (96 instances)
L2 cache:                        192 MiB (96 instances)
L3 cache:                        195 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-47,96-143
NUMA node1 CPU(s):               48-95,144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Vulnerable: eIBRS with unprivileged eBPF
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] mindietorch==1.0rc2+torch2.1.0.abi0
[pip3] numpy==1.26.4
[pip3] pynvml==11.5.3
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torch_npu_acc==1.0.7
[pip3] torchaudio==2.5.1
[pip3] transformers==4.50.3
[pip3] transformers-stream-generator==0.0.5
[conda] mindietorch               1.0rc2+torch2.1.0.abi0          pypi_0    pypi
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pynvml                    11.5.3                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] torch                     2.5.1+cpu                pypi_0    pypi
[conda] torch-npu                 2.5.1.dev20250320          pypi_0    pypi
[conda] torch-npu-acc             1.0.7                    pypi_0    pypi
[conda] torchaudio                2.5.1                    pypi_0    pypi
[conda] transformers              4.50.3                   pypi_0    pypi
[conda] transformers-stream-generator 0.0.5                    pypi_0    pypi
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc2

ENV Variables:
ASCEND_CUSTOM_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_VISIBLE_DEVICES=Ascend910-0,Ascend910-1,Ascend910-2,Ascend910-3,Ascend910-4,Ascend910-5,Ascend910-6,Ascend910-7,Ascend910-8,Ascend910-9,Ascend910-10,Ascend910-11,Ascend910-12,Ascend910-13,Ascend910-14,Ascend910-15
ASCEND_RUNTIME_OPTIONS=
ASCEND_SLOG_PRINT_TO_STDOUT=0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_PROCESS_LOG_PATH=/dockerdata/ascend/log
ASCEND_GLOBAL_LOG_LEVEL=3
ASCEND_DOCKER_RUNTIME=True
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/openssl-3.0-with-md2/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages:/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/lib64:/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/lib/:/data/miniconda3/envs/env-3.10.14/lib:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.2               Version: 24.1.rc2.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 89.2        38                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3384 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 90.5        39                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 91.1        39                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 91.1        40                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 90.3        37                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 93.2        39                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 91.2        38                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 91.0        39                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 87.8        37                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3389 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 95.3        39                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 88.6        38                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3380 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 90.0        41                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 95.6        40                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 94.6        40                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 89.8        38                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 93.8        41                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 8                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 9                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 10                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 11                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 12                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 13                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 14                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 15                                                           |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.T6
innerversion=V100R001C21B058
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.T6/x86_64-linux
```

### 🐛 Describe the bug

I'm using openr1's script to train a 32B QwQ model through GRPO. In order to [improve inference throughput](https://github.com/huggingface/trl/pull/3162), I tried to deploy vllm inference server with TP and starting zero-3 stage training simultaneously on a 16-NPUs machine, but encountered HCCL broadcast errors.
I would like to know if there is a conflict between broadcasting within vllm tp generate and other possible broadcasting process (e.g. parameter propagation).

The only thing I did is to revise vllm_client.py and grpo_trainer.py to apply tensor parallel with co-locating in vllm inference, which means I can use 16 GPUs both for training and inference.

In vllm_client.py, I revised **the client class**:
```python
class VLLMColocationClient:
    """
    A client class to interact with vLLM processes colocated with the training process.

    This client bypasses remote communication and directly interacts with the in-process vLLM engine.
    It supports weight updates and text generation functionalities similar to `VLLMClient`, but is optimized
    for scenarios where vLLM is running in the same process or node as training.

    Args:
        args (`GRPOConfig`): Configuration object containing vLLM parameters.
        model (`transformers.PreTrainedModel`): The model being used.
        vllm_device (`torch.device` or `str`): Device on which the model is loaded (e.g., "cuda:0").
    """

    def __init__(self, args: GRPOConfig, model, vllm_device):
        self.args: GRPOConfig = args
        self.model = model
        self.vllm_device = vllm_device

        self.llm = LLM(
            model=self.model.name_or_path,
            device=self.vllm_device,
            gpu_memory_utilization=self.args.vllm_gpu_memory_utilization,
            dtype=self.args.vllm_dtype,
            enable_prefix_caching=self.args.vllm_enable_prefix_caching,
            max_model_len=self.args.vllm_max_model_len,
            tensor_parallel_size=args.vllm_colocation_tp,
            distributed_executor_backend="external_launcher",
        )
        
    def update_named_param(self, name: str, weights: torch.Tensor):
        """
        Updates a specific named parameter in the model.

        Args:
            name (`str`):
                Name of the layer whose weights are being updated.
            weights (`torch.Tensor`):
                Tensor containing the updated weights.
        """
        llm_model = self.llm.llm_engine.model_executor.driver_worker.model_runner.model
        llm_model.load_weights([(name,weights)])

    def generate(
        self,
        prompts: list[str],
        n: int = 1,
        repetition_penalty: float = 1.0,
        temperature: float = 1.0,
        top_p: float = 1.0,
        top_k: int = -1,
        min_p: float = 0.0,
        max_tokens: int = 16,
        guided_decoding_regex: Optional[str] = None,
    ) -> list[list[str]]:
        """
        Generates model completions for the provided prompts.

        Args:
            prompts (`list[str]`):
                List of text prompts for which the model will generate completions.
            n (`int`, *optional*, defaults to `1`):
                Number of completions to generate for each prompt.
            repetition_penalty (`float`, *optional*, defaults to `1.0`):
                Parameter for repetition penalty. 1.0 means no penalty.
            temperature (`float`, *optional*, defaults to `1.0`):
                Temperature parameter for sampling. Higher values increase diversity.
            top_p (`float`, *optional*, defaults to `1.0`):
                Top-p sampling parameter.`1.0` means no truncation.
            top_k (`int`, *optional*, defaults to `-1`):
                Top-k sampling parameter. `-1` means no truncation.
            min_p (`float`, *optional*, defaults to `0.0`):
                Minimum probability for sampling.
            max_tokens (`int`, *optional*, defaults to `16`):
                Maximum number of tokens to generate for each prompt.
            guided_decoding_regex (`str` or `None`, *optional*, defaults to `None`):
                Regular expression to guide the decoding process.

        Returns:
            `list[list[int]]`:
                List of lists of token IDs representing the model-generated completions for each prompt.
        """
        # Guided decoding, if enabled
        if guided_decoding_regex is not None:
            guided_decoding = GuidedDecodingParams(backend="outlines", regex=guided_decoding_regex)
        else:
            guided_decoding = None

        sampling_params = SamplingParams(
            n=1, # vLLM on each GPU generates only 1 in vllm_colocation mode
            repetition_penalty=repetition_penalty,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            min_p=min_p,
            max_tokens=max_tokens,
            guided_decoding=guided_decoding,
        )
        
        all_outputs = self.llm.generate(
            prompts, sampling_params=sampling_params, use_tqdm=False
        )
        completion_ids = [output.token_ids for outputs in all_outputs for output in outputs.outputs]
        return completion_ids

    def reset_prefix_cache(self):
        """
        Resets the prefix cache for the model.
        """
        self.llm.reset_prefix_cache()
```
and in grpo_trainer.py, I modified the initialization and update_param:
```python
self.vllm_client = VLLMColocationClient(args, model, accelerator.device)
## generate completions and get slices in local rank (slices are done in client.generate)
completion_ids = self.vllm_client.generate(
    prompts=prompts_text,
    n=self.num_generations,
    repetition_penalty=self.repetition_penalty,
    temperature=self.temperature,
    top_p=self.top_p,
    top_k=-1 if self.top_k is None else self.top_k,
    min_p=0.0 if self.min_p is None else self.min_p,
    max_tokens=self.max_completion_length,
    guided_decoding_regex=self.guided_decoding_regex,
)

## update param for all ranks.
# if self.accelerator.is_main_process:
#     self.vllm_client.update_named_param(name, param.data)
self.vllm_client.update_named_param(name, param.data)
```
Finally, I get the floowing error messages for rank 1:
```
[rank1]:   File "/workspace/user_code/yuanjun_ws/openmind/examples/research/open_r1/open-r1/src/open_r1/grpo.py", line 292, in <module>
[rank1]:     main(script_args, training_args, model_args)
[rank1]:   File "/workspace/user_code/yuanjun_ws/openmind/examples/research/open_r1/open-r1/src/open_r1/grpo.py", line 246, in main
[rank1]:     train_result = trainer.train(resume_from_checkpoint=checkpoint)
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2245, in train
[rank1]:     return inner_training_loop(
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2556, in _inner_training_loop
[rank1]:     tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 3712, in training_step
[rank1]:     inputs = self._prepare_inputs(inputs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/trl/trl/extras/profiling.py", line 87, in wrapper
[rank1]:     return func(self, *args, **kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/trl/trl/trainer/grpo_trainer.py", line 694, in _prepare_inputs
[rank1]:     inputs = self._generate_and_score_completions(inputs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/trl/trl/trainer/grpo_trainer.py", line 758, in _generate_and_score_completions
[rank1]:     completion_ids = self.vllm_client.generate(
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/trl/trl/extras/vllm_client.py", line 463, in generate
[rank1]:     all_outputs = self.llm.generate(
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/utils.py", line 1057, in inner
[rank1]:     return fn(*args, **kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/entrypoints/llm.py", line 469, in generate
[rank1]:     outputs = self._run_engine(use_tqdm=use_tqdm)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/entrypoints/llm.py", line 1397, in _run_engine
[rank1]:     step_outputs = self.llm_engine.step()
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/engine/llm_engine.py", line 1391, in step
[rank1]:     outputs = self.model_executor.execute_model(
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/executor/executor_base.py", line 139, in execute_model
[rank1]:     output = self.collective_rpc("execute_model",
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank1]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/utils.py", line 2196, in run_method
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/worker/worker_base.py", line 420, in execute_model
[rank1]:     output = self.model_runner.execute_model(
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1146, in execute_model
[rank1]:     hidden_or_intermediate_states = model_executable(
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank1]:     return self._call_impl(*args, **kwargs)
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank1]:     return forward_call(*args, **kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/model_executor/models/qwen2.py", line 486, in forward
[rank1]:     hidden_states = self.model(input_ids, positions, kv_caches,
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/compilation/decorators.py", line 172, in __call__
[rank1]:     return self.forward(*args, **kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/model_executor/models/qwen2.py", line 340, in forward
[rank1]:     hidden_states = self.get_input_embeddings(input_ids)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/model_executor/models/qwen2.py", line 325, in get_input_embeddings
[rank1]:     return self.embed_tokens(input_ids)
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank1]:     return self._call_impl(*args, **kwargs)
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank1]:     return forward_call(*args, **kwargs)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/model_executor/layers/vocab_parallel_embedding.py", line 421, in forward
[rank1]:     output = tensor_model_parallel_all_reduce(output_parallel)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/distributed/communication_op.py", line 13, in tensor_model_parallel_all_reduce
[rank1]:     return get_tp_group().all_reduce(input_)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/distributed/parallel_state.py", line 310, in all_reduce
[rank1]:     return self._all_reduce_out_place(input_)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/distributed/parallel_state.py", line 313, in _all_reduce_out_place
[rank1]:     return self.device_communicator.all_reduce(input_)
[rank1]:   File "/workspace/user_code/yuanjun_ws/r1_requirements/vllm/vllm/distributed/device_communicators/base_device_communicator.py", line 35, in all_reduce
[rank1]:     dist.all_reduce(input_, group=self.device_group)
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2501, in all_reduce
[rank1]:     work = group.allreduce([tensor], opts)
[rank1]: RuntimeError: InnerRunOpApi:torch_npu/csrc/framework/OpParamMaker.cpp:281 OPS function error: HcclAllreduce, error code is 6
[rank1]: [ERROR] 2025-04-08-18:07:20 (PID:1292363, Device:1, RankID:1) ERR01100 OPS call acl api failed.
[rank1]: EI0006: [PID: 1292363] 2025-04-08-18:07:20.444.436 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
[rank1]:         Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
[rank1]:         TraceBack (most recent call last):
[rank1]:         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[1]-localUserrank[1]-localIpAddr[11.254.19.30], dst_rank[2]-remoteUserrank[2]-remote_ip_addr[11.254.19.30]
[rank1]:         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[1]-localUserrank[1]-localIpAddr[11.254.19.30], dst_rank[4]-remoteUserrank[4]-remote_ip_addr[11.254.19.30]
[rank1]:         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[1]-localUserrank[1]-localIpAddr[11.254.19.30], dst_rank[3]-remoteUserrank[3]-remote_ip_addr[11.254.19.30]
[rank1]:         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[1]-localUserrank[1]-localIpAddr[11.254.19.30], dst_rank[6]-remoteUserrank[6]-remote_ip_addr[11.254.19.30]
[rank1]:         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[1]-localUserrank[1]-localIpAddr[11.254.19.30], dst_rank[5]-remoteUserrank[5]-remote_ip_addr[11.254.19.30]
[rank1]:         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[1]-localUserrank[1]-localIpAddr[11.254.19.30], dst_rank[7]-remoteUserrank[7]-remote_ip_addr[11.254.19.30]

```
## Accelerate command:
```shell
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
export ASCEND_GLOBAL_LOG_LEVEL=3 #日志级别常用 1 INFO级别; 3 
export ASCEND_LAUNCH_BLOCKING=1
export ASCEND_GLOBAL_EVENT_ENABLE=1

ACCELERATE_LOG_LEVEL=info accelerate launch --config_file recipes/accelerate_configs/zero3.yaml \
    --num_processes=16 src/open_r1/grpo.py \
    --config recipes/Qwen2.5-CR/grpo/config_demo.yaml
```
