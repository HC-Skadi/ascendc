# Issue #116: RuntimeError: copy_d2d:torch_npu/csrc/aten/common/CopyKernel.cpp:274 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 507001

## 基本信息

- **编号**: #116
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/116
- **创建时间**: 2025-02-20T02:27:44Z
- **关闭时间**: 2025-02-20T10:37:03Z
- **更新时间**: 2025-02-20T10:37:03Z
- **提交者**: @dawnranger
- **评论数**: 3

## 标签

无

## 问题描述

# ENVIRONMENT & SETUP
same with https://github.com/vllm-project/vllm-ascend/issues/109

# FULL LOG
```
[WARNING|logging.py:329] 2025-02-20 02:13:18,253 >> Sliding Window Attention is enabled but not implemented for `sdpa`; unexpected results may be encountered.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  3.58it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  3.57it/s]

2025-02-20 02:13:22 - INFO - vllm_ascend.model_runner - Loading model weights took 0.0000 GB
INFO 02-20 02:13:24 executor_base.py:108] # CPU blocks: 12486, # CPU blocks: 1170
INFO 02-20 02:13:24 executor_base.py:113] Maximum concurrency for 32768 tokens per request: 48.77x
INFO 02-20 02:13:45 llm_engine.py:429] init engine (profile, create kv cache, warmup model) took 22.65 seconds
[2025-02-20 02:13:48,555] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed info: version=0.15.4, git-hash=unknown, git-branch=unknown
[2025-02-20 02:13:48,555] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:48,555] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:48,555] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:48,555] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:48,555] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:48,555] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:48,556] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:49,924] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed Flops Profiler Enabled: False
[2025-02-20 02:13:49,926] [INFO] [logging.py:128:log_dist] [Rank 0] Creating BF16 optimizer
[2025-02-20 02:13:50,251] [INFO] [utils.py:781:see_memory_usage] begin bf16_optimizer
[2025-02-20 02:13:50,251] [INFO] [utils.py:782:see_memory_usage] MA 2.88 GB         Max_MA 2.88 GB         CA 2.89 GB         Max_CA 3 GB 
[2025-02-20 02:13:50,252] [INFO] [utils.py:789:see_memory_usage] CPU Virtual Memory:  used = 246.18 GB, percent = 12.2%
[2025-02-20 02:13:50,585] [INFO] [utils.py:781:see_memory_usage] end bf16_ optimizer
[2025-02-20 02:13:50,586] [INFO] [utils.py:782:see_memory_usage] MA 2.88 GB         Max_MA 2.88 GB         CA 2.89 GB         Max_CA 3 GB 
[2025-02-20 02:13:50,586] [INFO] [utils.py:789:see_memory_usage] CPU Virtual Memory:  used = 246.18 GB, percent = 12.2%
[2025-02-20 02:13:50,587] [INFO] [config.py:999:print] DeepSpeedEngine configuration:
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   activation_checkpointing_config  {
    "partition_activations": false, 
    "contiguous_memory_optimization": false, 
    "cpu_checkpointing": false, 
    "number_checkpoints": null, 
    "synchronize_checkpoint_boundary": false, 
    "profile": false
}
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   aio_config ................... {'block_size': 1048576, 'queue_depth': 8, 'thread_count': 1, 'single_submit': False, 'overlap_events': True, 'use_gds': False}
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   amp_enabled .................. False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   amp_params ................... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   autotuning_config ............ {
    "enabled": false, 
    "start_step": null, 
    "end_step": null, 
    "metric_path": null, 
    "arg_mappings": null, 
    "metric": "throughput", 
    "model_info": null, 
    "results_dir": "autotuning_results", 
    "exps_dir": "autotuning_exps", 
    "overwrite": true, 
    "fast": true, 
    "start_profile_step": 3, 
    "end_profile_step": 5, 
    "tuner_type": "gridsearch", 
    "tuner_early_stopping": 5, 
    "tuner_num_trials": 50, 
    "model_info_path": null, 
    "mp_size": 1, 
    "max_train_batch_size": null, 
    "min_train_batch_size": 1, 
    "max_train_micro_batch_size_per_gpu": 1.024000e+03, 
    "min_train_micro_batch_size_per_gpu": 1, 
    "num_tuning_micro_batch_sizes": 3
}
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   bfloat16_enabled ............. True
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   bfloat16_immediate_grad_update  False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   checkpoint_parallel_write_pipeline  False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   checkpoint_tag_validation_enabled  True
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   checkpoint_tag_validation_fail  False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   comms_config ................. <deepspeed.comm.config.DeepSpeedCommsConfig object at 0x7fd4df5e4430>
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   communication_data_type ...... None
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   compression_config ........... {'weight_quantization': {'shared_parameters': {'enabled': False, 'quantizer_kernel': False, 'schedule_offset': 0, 'quantize_groups': 1, 'quantize_verbose': False, 'quantization_type': 'symmetric', 'quantize_weight_in_forward': False, 'rounding': 'nearest', 'fp16_mixed_quantize': False, 'quantize_change_ratio': 0.001}, 'different_groups': {}}, 'activation_quantization': {'shared_parameters': {'enabled': False, 'quantization_type': 'symmetric', 'range_calibration': 'dynamic', 'schedule_offset': 1000}, 'different_groups': {}}, 'sparse_pruning': {'shared_parameters': {'enabled': False, 'method': 'l1', 'schedule_offset': 1000}, 'different_groups': {}}, 'row_pruning': {'shared_parameters': {'enabled': False, 'method': 'l1', 'schedule_offset': 1000}, 'different_groups': {}}, 'head_pruning': {'shared_parameters': {'enabled': False, 'method': 'topk', 'schedule_offset': 1000}, 'different_groups': {}}, 'channel_pruning': {'shared_parameters': {'enabled': False, 'method': 'l1', 'schedule_offset': 1000}, 'different_groups': {}}, 'layer_reduction': {'enabled': False}}
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   curriculum_enabled_legacy .... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   curriculum_params_legacy ..... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   data_efficiency_config ....... {'enabled': False, 'seed': 1234, 'data_sampling': {'enabled': False, 'num_epochs': 1000, 'num_workers': 0, 'curriculum_learning': {'enabled': False}}, 'data_routing': {'enabled': False, 'random_ltd': {'enabled': False, 'layer_token_lr_schedule': {'enabled': False}}}}
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   data_efficiency_enabled ...... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   dataloader_drop_last ......... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   disable_allgather ............ False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   dump_state ................... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   dynamic_loss_scale_args ...... None
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_enabled ........... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_gas_boundary_resolution  1
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_layer_name ........ bert.encoder.layer
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_layer_num ......... 0
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_max_iter .......... 100
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_stability ......... 1e-06
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_tol ............... 0.01
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   eigenvalue_verbose ........... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   elasticity_enabled ........... False
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   flops_profiler_config ........ {
    "enabled": false, 
    "recompute_fwd_factor": 0.0, 
    "profile_step": 1, 
    "module_depth": -1, 
    "top_modules": 1, 
    "detailed": true, 
    "output_file": null
}
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   fp16_auto_cast ............... None
[2025-02-20 02:13:50,589] [INFO] [config.py:1003:print]   fp16_enabled ................. False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   fp16_master_weights_and_gradients  False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   global_rank .................. 0
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   grad_accum_dtype ............. None
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   gradient_accumulation_steps .. 2
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   gradient_clipping ............ 1.0
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   gradient_predivide_factor .... 1.0
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   graph_harvesting ............. False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   hybrid_engine ................ enabled=False max_out_tokens=512 inference_tp_size=1 release_inference_cache=False pin_parameters=True tp_gather_partition_size=8
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   initial_dynamic_scale ........ 1
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   load_universal_checkpoint .... False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   loss_scale ................... 1.0
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   memory_breakdown ............. False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   mics_hierarchial_params_gather  False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   mics_shard_size .............. -1
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   monitor_config ............... tensorboard=TensorBoardConfig(enabled=False, output_path='', job_name='DeepSpeedJobName') comet=CometConfig(enabled=False, samples_log_interval=100, project=None, workspace=None, api_key=None, experiment_name=None, experiment_key=None, online=None, mode=None) wandb=WandbConfig(enabled=False, group=None, team=None, project='deepspeed') csv_monitor=CSVConfig(enabled=False, output_path='', job_name='DeepSpeedJobName')
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   nebula_config ................ {
    "enabled": false, 
    "persistent_storage_path": null, 
    "persistent_time_interval": 100, 
    "num_of_version_in_retention": 2, 
    "enable_nebula_load": true, 
    "load_path": null
}
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   optimizer_legacy_fusion ...... False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   optimizer_name ............... None
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   optimizer_params ............. None
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   pipeline ..................... {'stages': 'auto', 'partition': 'best', 'seed_layers': False, 'activation_checkpoint_interval': 0, 'pipe_partitioned': True, 'grad_partitioned': True}
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   pld_enabled .................. False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   pld_params ................... False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   prescale_gradients ........... False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   scheduler_name ............... None
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   scheduler_params ............. None
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   seq_parallel_communication_data_type  torch.float32
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   sparse_attention ............. None
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   sparse_gradients_enabled ..... False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   steps_per_print .............. inf
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   timers_config ................ enabled=True synchronized=True
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   train_batch_size ............. 14
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   train_micro_batch_size_per_gpu  1
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   use_data_before_expert_parallel_  False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   use_node_local_storage ....... False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   wall_clock_breakdown ......... False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   weight_quantization_config ... None
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   world_size ................... 7
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   zero_allow_untested_optimizer  False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   zero_config .................. stage=0 contiguous_gradients=True reduce_scatter=True reduce_bucket_size=500000000 use_multi_rank_bucket_allreduce=True allgather_partitions=True allgather_bucket_size=500000000 overlap_comm=False load_from_fp32_weights=True elastic_checkpoint=False offload_param=DeepSpeedZeroOffloadParamConfig(device='none', nvme_path=None, buffer_count=5, buffer_size=100000000, max_in_cpu=1000000000, pin_memory=False) offload_optimizer=DeepSpeedZeroOffloadOptimizerConfig(device='none', nvme_path=None, buffer_count=4, pin_memory=False, pipeline_read=False, pipeline_write=False, fast_init=False, ratio=1.0) sub_group_size=1000000000 cpu_offload_param=None cpu_offload_use_pin_memory=None cpu_offload=None prefetch_bucket_size=50000000 param_persistence_threshold=100000 model_persistence_threshold=9223372036854775807 max_live_parameters=1000000000 max_reuse_distance=1000000000 gather_16bit_weights_on_model_save=False use_all_reduce_for_fetch_params=False stage3_gather_fp16_weights_on_model_save=False ignore_unused_parameters=True legacy_stage1=False round_robin_gradients=False zero_hpz_partition_size=1 zero_quantized_weights=False zero_quantized_nontrainable_weights=False zero_quantized_gradients=False mics_shard_size=-1 mics_hierarchical_params_gather=False memory_efficient_linear=True pipeline_loading_checkpoint=False override_module_apply=True
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   zero_enabled ................. False
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   zero_force_ds_cpu_optimizer .. True
[2025-02-20 02:13:50,590] [INFO] [config.py:1003:print]   zero_optimization_stage ...... 0
[2025-02-20 02:13:50,591] [INFO] [config.py:989:print_user_config]   json = {
    "train_batch_size": 14, 
    "train_micro_batch_size_per_gpu": 1, 
    "gradient_accumulation_steps": 2, 
    "zero_optimization": {
        "stage": 0, 
        "offload_optimizer": {
            "device": "none", 
            "nvme_path": null
        }, 
        "offload_param": {
            "device": "none", 
            "nvme_path": null
        }, 
        "stage3_gather_16bit_weights_on_model_save": false
    }, 
    "gradient_clipping": 1.0, 
    "steps_per_print": inf, 
    "bf16": {
        "enabled": true
    }, 
    "fp16": {
        "enabled": false
    }
}
2025-02-20 02:13:50 - INFO - open_r1.grpo - *** Train ***
[2025-02-20 02:13:50,952] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed info: version=0.15.4, git-hash=unknown, git-branch=unknown
[2025-02-20 02:13:50,952] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 7
[2025-02-20 02:13:52,151] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed Flops Profiler Enabled: False
[2025-02-20 02:13:52,153] [INFO] [logging.py:128:log_dist] [Rank 0] Using client Optimizer as basic optimizer
[2025-02-20 02:13:52,153] [INFO] [logging.py:128:log_dist] [Rank 0] Removing param_group that has no 'params' in the basic Optimizer
[2025-02-20 02:13:52,167] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed Basic Optimizer = AdamW
[2025-02-20 02:13:52,167] [INFO] [utils.py:59:is_zero_supported_optimizer] Checking ZeRO support for optimizer=AdamW type=<class 'torch.optim.adamw.AdamW'>
[2025-02-20 02:13:52,167] [INFO] [logging.py:128:log_dist] [Rank 0] Creating torch.bfloat16 ZeRO stage 2 optimizer
[2025-02-20 02:13:52,167] [INFO] [stage_1_and_2.py:149:__init__] Reduce bucket size 500000000
[2025-02-20 02:13:52,167] [INFO] [stage_1_and_2.py:150:__init__] Allgather bucket size 500000000
[2025-02-20 02:13:52,167] [INFO] [stage_1_and_2.py:151:__init__] CPU Offload: False
[2025-02-20 02:13:52,167] [INFO] [stage_1_and_2.py:152:__init__] Round robin gradient partitioning: False
[2025-02-20 02:13:55,972] [INFO] [utils.py:781:see_memory_usage] Before initializing optimizer states
[2025-02-20 02:13:55,972] [INFO] [utils.py:782:see_memory_usage] MA 6.57 GB         Max_MA 6.57 GB         CA 6.65 GB         Max_CA 7 GB 
[2025-02-20 02:13:55,973] [INFO] [utils.py:789:see_memory_usage] CPU Virtual Memory:  used = 258.62 GB, percent = 12.8%
[2025-02-20 02:13:56,253] [INFO] [utils.py:781:see_memory_usage] After initializing optimizer states
[2025-02-20 02:13:56,254] [INFO] [utils.py:782:see_memory_usage] MA 6.57 GB         Max_MA 7.39 GB         CA 7.47 GB         Max_CA 7 GB 
[2025-02-20 02:13:56,254] [INFO] [utils.py:789:see_memory_usage] CPU Virtual Memory:  used = 258.62 GB, percent = 12.8%
[2025-02-20 02:13:56,254] [INFO] [stage_1_and_2.py:544:__init__] optimizer state initialized
[2025-02-20 02:13:56,539] [INFO] [utils.py:781:see_memory_usage] After initializing ZeRO optimizer
[2025-02-20 02:13:56,540] [INFO] [utils.py:782:see_memory_usage] MA 6.57 GB         Max_MA 6.57 GB         CA 7.47 GB         Max_CA 7 GB 
[2025-02-20 02:13:56,540] [INFO] [utils.py:789:see_memory_usage] CPU Virtual Memory:  used = 258.63 GB, percent = 12.8%
[2025-02-20 02:13:56,541] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed Final Optimizer = DeepSpeedZeroOptimizer
[2025-02-20 02:13:56,541] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed using configured LR scheduler = None
[2025-02-20 02:13:56,542] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed LR Scheduler = None
[2025-02-20 02:13:56,542] [INFO] [logging.py:128:log_dist] [Rank 0] step=0, skipped=0, lr=[0.0, 0.0], mom=[(0.9, 0.999), (0.9, 0.999)]
[2025-02-20 02:13:56,543] [INFO] [config.py:999:print] DeepSpeedEngine configuration:
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   activation_checkpointing_config  {
    "partition_activations": false, 
    "contiguous_memory_optimization": false, 
    "cpu_checkpointing": false, 
    "number_checkpoints": null, 
    "synchronize_checkpoint_boundary": false, 
    "profile": false
}
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   aio_config ................... {'block_size': 1048576, 'queue_depth': 8, 'thread_count': 1, 'single_submit': False, 'overlap_events': True, 'use_gds': False}
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   amp_enabled .................. False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   amp_params ................... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   autotuning_config ............ {
    "enabled": false, 
    "start_step": null, 
    "end_step": null, 
    "metric_path": null, 
    "arg_mappings": null, 
    "metric": "throughput", 
    "model_info": null, 
    "results_dir": "autotuning_results", 
    "exps_dir": "autotuning_exps", 
    "overwrite": true, 
    "fast": true, 
    "start_profile_step": 3, 
    "end_profile_step": 5, 
    "tuner_type": "gridsearch", 
    "tuner_early_stopping": 5, 
    "tuner_num_trials": 50, 
    "model_info_path": null, 
    "mp_size": 1, 
    "max_train_batch_size": null, 
    "min_train_batch_size": 1, 
    "max_train_micro_batch_size_per_gpu": 1.024000e+03, 
    "min_train_micro_batch_size_per_gpu": 1, 
    "num_tuning_micro_batch_sizes": 3
}
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   bfloat16_enabled ............. True
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   bfloat16_immediate_grad_update  False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   checkpoint_parallel_write_pipeline  False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   checkpoint_tag_validation_enabled  True
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   checkpoint_tag_validation_fail  False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   comms_config ................. <deepspeed.comm.config.DeepSpeedCommsConfig object at 0x7fd54ac963b0>
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   communication_data_type ...... None
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   compression_config ........... {'weight_quantization': {'shared_parameters': {'enabled': False, 'quantizer_kernel': False, 'schedule_offset': 0, 'quantize_groups': 1, 'quantize_verbose': False, 'quantization_type': 'symmetric', 'quantize_weight_in_forward': False, 'rounding': 'nearest', 'fp16_mixed_quantize': False, 'quantize_change_ratio': 0.001}, 'different_groups': {}}, 'activation_quantization': {'shared_parameters': {'enabled': False, 'quantization_type': 'symmetric', 'range_calibration': 'dynamic', 'schedule_offset': 1000}, 'different_groups': {}}, 'sparse_pruning': {'shared_parameters': {'enabled': False, 'method': 'l1', 'schedule_offset': 1000}, 'different_groups': {}}, 'row_pruning': {'shared_parameters': {'enabled': False, 'method': 'l1', 'schedule_offset': 1000}, 'different_groups': {}}, 'head_pruning': {'shared_parameters': {'enabled': False, 'method': 'topk', 'schedule_offset': 1000}, 'different_groups': {}}, 'channel_pruning': {'shared_parameters': {'enabled': False, 'method': 'l1', 'schedule_offset': 1000}, 'different_groups': {}}, 'layer_reduction': {'enabled': False}}
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   curriculum_enabled_legacy .... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   curriculum_params_legacy ..... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   data_efficiency_config ....... {'enabled': False, 'seed': 1234, 'data_sampling': {'enabled': False, 'num_epochs': 1000, 'num_workers': 0, 'curriculum_learning': {'enabled': False}}, 'data_routing': {'enabled': False, 'random_ltd': {'enabled': False, 'layer_token_lr_schedule': {'enabled': False}}}}
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   data_efficiency_enabled ...... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   dataloader_drop_last ......... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   disable_allgather ............ False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   dump_state ................... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   dynamic_loss_scale_args ...... None
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_enabled ........... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_gas_boundary_resolution  1
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_layer_name ........ bert.encoder.layer
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_layer_num ......... 0
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_max_iter .......... 100
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_stability ......... 1e-06
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_tol ............... 0.01
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   eigenvalue_verbose ........... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   elasticity_enabled ........... False
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   flops_profiler_config ........ {
    "enabled": false, 
    "recompute_fwd_factor": 0.0, 
    "profile_step": 1, 
    "module_depth": -1, 
    "top_modules": 1, 
    "detailed": true, 
    "output_file": null
}
[2025-02-20 02:13:56,543] [INFO] [config.py:1003:print]   fp16_auto_cast ............... None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   fp16_enabled ................. False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   fp16_master_weights_and_gradients  False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   global_rank .................. 0
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   grad_accum_dtype ............. None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   gradient_accumulation_steps .. 2
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   gradient_clipping ............ 1.0
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   gradient_predivide_factor .... 1.0
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   graph_harvesting ............. False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   hybrid_engine ................ enabled=False max_out_tokens=512 inference_tp_size=1 release_inference_cache=False pin_parameters=True tp_gather_partition_size=8
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   initial_dynamic_scale ........ 1
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   load_universal_checkpoint .... False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   loss_scale ................... 1.0
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   memory_breakdown ............. False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   mics_hierarchial_params_gather  False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   mics_shard_size .............. -1
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   monitor_config ............... tensorboard=TensorBoardConfig(enabled=False, output_path='', job_name='DeepSpeedJobName') comet=CometConfig(enabled=False, samples_log_interval=100, project=None, workspace=None, api_key=None, experiment_name=None, experiment_key=None, online=None, mode=None) wandb=WandbConfig(enabled=False, group=None, team=None, project='deepspeed') csv_monitor=CSVConfig(enabled=False, output_path='', job_name='DeepSpeedJobName')
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   nebula_config ................ {
    "enabled": false, 
    "persistent_storage_path": null, 
    "persistent_time_interval": 100, 
    "num_of_version_in_retention": 2, 
    "enable_nebula_load": true, 
    "load_path": null
}
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   optimizer_legacy_fusion ...... False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   optimizer_name ............... None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   optimizer_params ............. None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   pipeline ..................... {'stages': 'auto', 'partition': 'best', 'seed_layers': False, 'activation_checkpoint_interval': 0, 'pipe_partitioned': True, 'grad_partitioned': True}
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   pld_enabled .................. False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   pld_params ................... False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   prescale_gradients ........... False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   scheduler_name ............... None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   scheduler_params ............. None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   seq_parallel_communication_data_type  torch.float32
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   sparse_attention ............. None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   sparse_gradients_enabled ..... False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   steps_per_print .............. inf
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   timers_config ................ enabled=True synchronized=True
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   train_batch_size ............. 14
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   train_micro_batch_size_per_gpu  1
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   use_data_before_expert_parallel_  False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   use_node_local_storage ....... False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   wall_clock_breakdown ......... False
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   weight_quantization_config ... None
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   world_size ................... 7
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   zero_allow_untested_optimizer  True
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   zero_config .................. stage=2 contiguous_gradients=True reduce_scatter=True reduce_bucket_size=500000000 use_multi_rank_bucket_allreduce=True allgather_partitions=True allgather_bucket_size=500000000 overlap_comm=False load_from_fp32_weights=True elastic_checkpoint=False offload_param=DeepSpeedZeroOffloadParamConfig(device='none', nvme_path=None, buffer_count=5, buffer_size=100000000, max_in_cpu=1000000000, pin_memory=False) offload_optimizer=DeepSpeedZeroOffloadOptimizerConfig(device='none', nvme_path=None, buffer_count=4, pin_memory=False, pipeline_read=False, pipeline_write=False, fast_init=False, ratio=1.0) sub_group_size=1000000000 cpu_offload_param=None cpu_offload_use_pin_memory=None cpu_offload=None prefetch_bucket_size=50000000 param_persistence_threshold=100000 model_persistence_threshold=9223372036854775807 max_live_parameters=1000000000 max_reuse_distance=1000000000 gather_16bit_weights_on_model_save=False use_all_reduce_for_fetch_params=False stage3_gather_fp16_weights_on_model_save=False ignore_unused_parameters=True legacy_stage1=False round_robin_gradients=False zero_hpz_partition_size=1 zero_quantized_weights=False zero_quantized_nontrainable_weights=False zero_quantized_gradients=False mics_shard_size=-1 mics_hierarchical_params_gather=False memory_efficient_linear=True pipeline_loading_checkpoint=False override_module_apply=True
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   zero_enabled ................. True
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   zero_force_ds_cpu_optimizer .. True
[2025-02-20 02:13:56,544] [INFO] [config.py:1003:print]   zero_optimization_stage ...... 2
[2025-02-20 02:13:56,545] [INFO] [config.py:989:print_user_config]   json = {
    "train_batch_size": 14, 
    "train_micro_batch_size_per_gpu": 1, 
    "gradient_accumulation_steps": 2, 
    "zero_optimization": {
        "stage": 2, 
        "offload_optimizer": {
            "device": "none", 
            "nvme_path": null
        }, 
        "offload_param": {
            "device": "none", 
            "nvme_path": null
        }, 
        "stage3_gather_16bit_weights_on_model_save": false
    }, 
    "gradient_clipping": 1.0, 
    "steps_per_print": inf, 
    "bf16": {
        "enabled": true
    }, 
    "fp16": {
        "enabled": false
    }, 
    "zero_allow_untested_optimizer": true
}
[INFO|trainer.py:2407] 2025-02-20 02:13:56,547 >> ***** Running training *****
[INFO|trainer.py:2408] 2025-02-20 02:13:56,547 >>   Num examples = 7,473
[INFO|trainer.py:2409] 2025-02-20 02:13:56,547 >>   Num Epochs = 3
[INFO|trainer.py:2410] 2025-02-20 02:13:56,547 >>   Instantaneous batch size per device = 1
[INFO|trainer.py:2413] 2025-02-20 02:13:56,547 >>   Total train batch size (w. parallel, distributed & accumulation) = 14
[INFO|trainer.py:2414] 2025-02-20 02:13:56,547 >>   Gradient Accumulation steps = 2
[INFO|trainer.py:2415] 2025-02-20 02:13:56,547 >>   Total optimization steps = 11,208
[INFO|trainer.py:2416] 2025-02-20 02:13:56,548 >>   Number of trainable parameters = 1,543,714,304
[INFO|integration_utils.py:817] 2025-02-20 02:13:56,549 >> Automatic Weights & Biases logging enabled, to disable set os.environ["WANDB_DISABLED"] = "true"
  0%|          | 0/11208 [00:00<?, ?it/s][rank0]:[W220 02:16:03.248159344 ToKernelNpu.cpp:133] Warning: Warning: Device do not support double dtype now, dtype cast repalce with float. (function operator())
{'loss': 0.0, 'grad_norm': 8.59594440460205, 'learning_rate': 2.6761819803746656e-09, 'rewards/accuracy_reward': 0.0, 'rewards/format_reward': 0.1428571492433548, 'reward': 0.1428571492433548, 'reward_std': 1.069045066833496, 'completion_length': 116.85715103149414, 'kl': 1.1324882507324219e-05, 'epoch': 0.0}
  0%|          | 1/11208 [02:02<381:05:58, 122.42s/it]Traceback (most recent call last):
  File "/root/open-r1/src/run_grpo.py", line 9, in <module>
    main()
  File "/root/open-r1/src/run_grpo.py", line 6, in main
    run_exp()
  File "/root/open-r1/src/open_r1/grpo.py", line 263, in run_exp
    main(script_args, training_args, model_args)
  File "/root/open-r1/src/open_r1/grpo.py", line 225, in main
    train_result = trainer.train(resume_from_checkpoint=checkpoint)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2243, in train
    return inner_training_loop(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2550, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 3694, in training_step
    inputs = self._prepare_inputs(inputs)
  File "/home/HwHiAiUser/trl/trl/trainer/grpo_trainer.py", line 606, in _prepare_inputs
    self._move_model_to_vllm()
  File "/home/HwHiAiUser/trl/trl/trainer/grpo_trainer.py", line 582, in _move_model_to_vllm
    llm_model.load_weights(state_dict.items())
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 513, in load_weights
    return loader.load_weights(weights)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 233, in load_weights
    autoloaded_weights = set(self._load_module("", self.module, weights))
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 194, in _load_module
    yield from self._load_module(prefix,
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 171, in _load_module
    loaded_params = module_load_weights(weights)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 413, in load_weights
    weight_loader(param, loaded_weight)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/layers/vocab_parallel_embedding.py", line 398, in weight_loader
    param[:loaded_weight.shape[0]].data.copy_(loaded_weight)
RuntimeError: copy_d2d:torch_npu/csrc/aten/common/CopyKernel.cpp:274 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 507001
[ERROR] 2025-02-20-02:16:03 (PID:1162, Device:0, RankID:0) ERR00100 PTA call acl api failed
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EI9999: Inner Error!
        The error from device(chipId:0, dieId:0), serial number is 9. there is a sdma error, sdma channel is 2, sdmaBlkFsmState=0x7, dfxSdmaBlkFsmOstCnt=0x0, sdmaChFree=0x0, irqStatus=0x220000, cqeStatus=0x3 [FUNC:ProcessStarsSdmaErrorInfo][FILE:device_error_proc.cc][LINE:1521]
EI9999: [PID: 1162] 2025-02-20-02:16:03.427.598 Memory async copy failed, device_id=0, stream_id=2, task_id=17983, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=466747392[FUNC:GetError][FILE:stream.cc][LINE:1084]
        TraceBack (most recent call last):
        rtStreamSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 507001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

[rank0]: Traceback (most recent call last):
[rank0]:   File "/root/open-r1/src/run_grpo.py", line 9, in <module>
[rank0]:     main()
[rank0]:   File "/root/open-r1/src/run_grpo.py", line 6, in main
[rank0]:     run_exp()
[rank0]:   File "/root/open-r1/src/open_r1/grpo.py", line 263, in run_exp
[rank0]:     main(script_args, training_args, model_args)
[rank0]:   File "/root/open-r1/src/open_r1/grpo.py", line 225, in main
[rank0]:     train_result = trainer.train(resume_from_checkpoint=checkpoint)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2243, in train
[rank0]:     return inner_training_loop(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2550, in _inner_training_loop
[rank0]:     tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 3694, in training_step
[rank0]:     inputs = self._prepare_inputs(inputs)
[rank0]:   File "/home/HwHiAiUser/trl/trl/trainer/grpo_trainer.py", line 606, in _prepare_inputs
[rank0]:     self._move_model_to_vllm()
[rank0]:   File "/home/HwHiAiUser/trl/trl/trainer/grpo_trainer.py", line 582, in _move_model_to_vllm
[rank0]:     llm_model.load_weights(state_dict.items())
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 513, in load_weights
[rank0]:     return loader.load_weights(weights)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 233, in load_weights
[rank0]:     autoloaded_weights = set(self._load_module("", self.module, weights))
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 194, in _load_module
[rank0]:     yield from self._load_module(prefix,
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 171, in _load_module
[rank0]:     loaded_params = module_load_weights(weights)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 413, in load_weights
[rank0]:     weight_loader(param, loaded_weight)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/layers/vocab_parallel_embedding.py", line 398, in weight_loader
[rank0]:     param[:loaded_weight.shape[0]].data.copy_(loaded_weight)
[rank0]: RuntimeError: copy_d2d:torch_npu/csrc/aten/common/CopyKernel.cpp:274 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 507001
[rank0]: [ERROR] 2025-02-20-02:16:03 (PID:1162, Device:0, RankID:0) ERR00100 PTA call acl api failed
[rank0]: [Error]: An internal error occurs in the task scheduler module on the device. 
[rank0]:         Rectify the fault based on the error information in the ascend log.
[rank0]: EI9999: Inner Error!
[rank0]:         The error from device(chipId:0, dieId:0), serial number is 9. there is a sdma error, sdma channel is 2, sdmaBlkFsmState=0x7, dfxSdmaBlkFsmOstCnt=0x0, sdmaChFree=0x0, irqStatus=0x220000, cqeStatus=0x3 [FUNC:ProcessStarsSdmaErrorInfo][FILE:device_error_proc.cc][LINE:1521]
[rank0]: EI9999: [PID: 1162] 2025-02-20-02:16:03.427.598 Memory async copy failed, device_id=0, stream_id=2, task_id=17983, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=466747392[FUNC:GetError][FILE:stream.cc][LINE:1084]
[rank0]:         TraceBack (most recent call last):
[rank0]:         rtStreamSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
[rank0]:        synchronize stream failed, runtime result = 507001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

[rank0]:[W220 02:16:08.680800943 NPUStream.cpp:487] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:08.620.115 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeUsedDevices)
[W220 02:16:09.537462030 NPUStream.cpp:469] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.476.793 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W220 02:16:09.540295624 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.479.915 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W220 02:16:09.541331190 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.481.111 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W220 02:16:09.542540910 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.482.128 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W220 02:16:09.543780168 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.483.396 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W220 02:16:09.545026750 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.484.579 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W220 02:16:09.546072422 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.485.837 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W220 02:16:09.547051339 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.486.858 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W220 02:16:09.548005394 NPUWorkspaceAllocator.cpp:122] Warning: NPU warning, error code is 507001[Error]: 
[Error]: An internal error occurs in the task scheduler module on the device. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1162] 2025-02-20-02:16:09.487.833 wait for compute device to finish failed, runtime result = 507001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
W0220 02:16:16.454000 1020 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1163 closing signal SIGTERM
W0220 02:16:16.455000 1020 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1164 closing signal SIGTERM
W0220 02:16:16.456000 1020 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1165 closing signal SIGTERM
W0220 02:16:16.457000 1020 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1166 closing signal SIGTERM
W0220 02:16:16.458000 1020 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1167 closing signal SIGTERM
W0220 02:16:16.459000 1020 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1168 closing signal SIGTERM
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
E0220 02:16:18.998000 1020 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 0 (pid: 1162) of binary: /usr/local/python3.10.14/bin/python3
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
Traceback (most recent call last):
  File "/usr/local/python3.10.14/bin/accelerate", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/commands/accelerate_cli.py", line 48, in main
    args.func(args)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/commands/launch.py", line 1182, in launch_command
    deepspeed_launcher(args)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/commands/launch.py", line 861, in deepspeed_launcher
    distrib_run.run(args)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
src/run_grpo.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2025-02-20_02:16:16
  host      : pytorch-939119853-master-0
  rank      : 0 (local_rank: 0)
  exitcode  : 1 (pid: 1162)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
```
