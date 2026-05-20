# Issue #3135: [Misc]: vllm-ascend 0.10.2rc1 run qwen3-8B on 300I DUO error, kernel_macros.h:24:10: fatal error: 'cstdint' file not found

## 基本信息

- **编号**: #3135
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3135
- **创建时间**: 2025-09-24T00:58:46Z
- **关闭时间**: 2025-09-24T02:10:13Z
- **更新时间**: 2025-12-30T08:58:59Z
- **提交者**: @neeeekoooo
- **评论数**: 1

## 标签

无

## 问题描述

why? is it related to the GCC library?
i should update gcc  or  build vllm-ascend from source code?

cmd:
```shell
[root@localhost ~]# conda activate vllm
(vllm) [root@localhost ~]# source /usr/local/Ascend/ascend-toolkit/set_env.sh
(vllm) [root@localhost ~]# source /usr/local/Ascend/nnal/asdsip/set_env.sh
(vllm) [root@localhost ~]# source /usr/local/Ascend/nnal/atb/set_env.sh
(vllm) [root@localhost ~]# export ASCEND_RT_VISIBLE_DEVICES=2,3
(vllm) [root@localhost ~]# export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
(vllm) [root@localhost ~]# vllm serve "/data/models/Qwen3-8B" \
>  --port 8003 \
>  --tensor-parallel-size 2 \
>  --served-model-name "qwen3" \
>  --dtype float16 \
>  --enforce-eager \
>  --max-model-len 32768 \
>  --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}' \
>  --enable-auto-tool-choice --tool-call-parser hermes
```

gcc info:
```txt
[root@localhost ~]# gcc --version
gcc (GCC) 10.3.1
Copyright © 2020 Free Software Foundation, Inc.
本程序是自由软件；请参看源代码的版权声明。本软件没有任何担保；
包括没有适销性和某一专用目的下的适用性担保。
[root@localhost ~]# gcc -v
使用内建 specs。
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/aarch64-linux-gnu/10.3.1/lto-wrapper
目标：aarch64-linux-gnu
配置为：../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-linker-hash-style=gnu --enable-languages=c,c++,fortran,objc,obj-c++,lto --enable-plugin --enable-initfini-array --disable-libgcj --without-cloog --enable-gnu-indirect-function --build=aarch64-linux-gnu --with-stage1-ldflags=' -Wl,-z,relro,-z,now' --with-boot-ldflags=' -Wl,-z,relro,-z,now' --disable-bootstrap --without-isl --with-multilib-list=lp64 --enable-bolt
线程模型：posix
Supported LTO compression algorithms: zlib
gcc 版本 10.3.1 (GCC) 

```

error logs:
```txt
(EngineCore_DP0 pid=1782342)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 243, in get_response
(EngineCore_DP0 pid=1782342)     raise RuntimeError(
(EngineCore_DP0 pid=1782342) RuntimeError: Worker failed with error 'The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RmsNorm.
(EngineCore_DP0 pid=1782342) Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(EngineCore_DP0 pid=1782342) Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(EngineCore_DP0 pid=1782342) [ERROR] 2025-09-23-19:53:07 (PID:1782807, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=1782342) E40021: [PID: 1782807] 2025-09-23-19:53:07.406.437 Failed to compile Op [RmsNorm34]. (oppath: [Compile /usr/local/Ascend/ascend-toolkit/8.2.RC1/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/rms_norm.py failed with errormsg/stack: File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/tikcpp/ascendc_common_utility.py", line 520, in dump_build_log
(EngineCore_DP0 pid=1782342)     raise Exception("An error occurred during compile phases of {}, msg is {}".\
(EngineCore_DP0 pid=1782342) Exception: An error occurred during compile phases of CompileStage.PRECOMPILE, msg is In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/rms_norm/rms_norm.cpp:21:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/rms_norm/rms_norm.h:23:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/rms_norm/rms_norm_base.h:23:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/kernel_operator.h:24:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/impl/kernel_tpipe_impl.h:23:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/interface/kernel_tpipe.h:23:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/impl/kernel_tpipe_base.h:23:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/impl/kernel_tensor_impl.h:23:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/interface/kernel_tensor.h:24:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/impl/kernel_utils.h:23:
(EngineCore_DP0 pid=1782342) In file included from /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/impl/utils/kernel_utils_macros.h:33:
(EngineCore_DP0 pid=1782342) /usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/tikcpp/tikcfw/impl/kernel_macros.h:24:10: fatal error: 'cstdint' file not found
(EngineCore_DP0 pid=1782342) #include <cstdint>
(EngineCore_DP0 pid=1782342)          ^~~~~~~~~
(EngineCore_DP0 pid=1782342) 1 error generated.
(EngineCore_DP0 pid=1782342) 
(EngineCore_DP0 pid=1782342) ], optype: [RmsNorm])
(EngineCore_DP0 pid=1782342)         Possible Cause: Failed to compile op for some reasons.
(EngineCore_DP0 pid=1782342)         Solution: See the host log for details, and then check the Python stack where the error log is reported.
(EngineCore_DP0 pid=1782342)         TraceBack (most recent call last):
(EngineCore_DP0 pid=1782342)         Compile op[RmsNorm34] failed, oppath[/usr/local/Ascend/ascend-toolkit/8.2.RC1/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/rms_norm.py], optype[RmsNorm], taskID[66]. Please check op's compilation error message.[FUNC:ReportBuildErrMessage][FILE:fusion_manager.cc][LINE:368]
(EngineCore_DP0 pid=1782342)         [SubGraphOpt][Compile][ProcFailedCompTask] Thread[281463005966624] recompile single op[RmsNorm34] failed[FUNC:ProcessAllFailedCompileTasks][FILE:tbe_op_store_adapter.cc][LINE:1135]
(EngineCore_DP0 pid=1782342)         [SubGraphOpt][Compile][ParalCompOp] Thread[281463005966624] process fail task failed[FUNC:ParallelCompileOp][FILE:tbe_op_store_adapter.cc][LINE:1182]
(EngineCore_DP0 pid=1782342)         [SubGraphOpt][Compile][CompOpOnly] CompileOp failed.[FUNC:CompileOpOnly][FILE:op_compiler.cc][LINE:1198]
(EngineCore_DP0 pid=1782342)         [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1416]
(EngineCore_DP0 pid=1782342)         Call OptimizeFusedGraph failed, ret:4294967295, engine_name:AIcoreEngine, graph_name:partition0_rank1_new_sub_graph2[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:119]
(EngineCore_DP0 pid=1782342)         subgraph 0 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:893]
(EngineCore_DP0 pid=1782342)         build graph failed, graph id:33, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1624]
(EngineCore_DP0 pid=1782342)         [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_DP0 pid=1782342)         [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
(EngineCore_DP0 pid=1782342)         build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
(EngineCore_DP0 pid=1782342) ', please check the stack trace above for the root cause
(APIServer pid=1779513) Traceback (most recent call last):
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/bin/vllm", line 7, in <module>
(APIServer pid=1779513)     sys.exit(main())
(APIServer pid=1779513)              ^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=1779513)     args.dispatch_function(args)
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd
(APIServer pid=1779513)     uvloop.run(run_server(args))
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=1779513)     return runner.run(wrapper())
(APIServer pid=1779513)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=1779513)     return self._loop.run_until_complete(task)
(APIServer pid=1779513)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=1779513)     return await main
(APIServer pid=1779513)            ^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1941, in run_server
(APIServer pid=1779513)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1961, in run_server_worker
(APIServer pid=1779513)     async with build_async_engine_client(
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/contextlib.py", line 204, in __aenter__
(APIServer pid=1779513)     return await anext(self.gen)
(APIServer pid=1779513)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 179, in build_async_engine_client
(APIServer pid=1779513)     async with build_async_engine_client_from_engine_args(
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/contextlib.py", line 204, in __aenter__
(APIServer pid=1779513)     return await anext(self.gen)
(APIServer pid=1779513)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 221, in build_async_engine_client_from_engine_args
(APIServer pid=1779513)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=1779513)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/utils/__init__.py", line 1589, in inner
(APIServer pid=1779513)     return fn(*args, **kwargs)
(APIServer pid=1779513)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 212, in from_vllm_config
(APIServer pid=1779513)     return cls(
(APIServer pid=1779513)            ^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 136, in __init__
(APIServer pid=1779513)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=1779513)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=1779513)     return AsyncMPClient(*client_args)
(APIServer pid=1779513)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=1779513)     super().__init__(
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=1779513)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=1779513)     next(self.gen)
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 729, in launch_core_engines
(APIServer pid=1779513)     wait_for_engine_startup(
(APIServer pid=1779513)   File "/data/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 782, in wait_for_engine_startup
(APIServer pid=1779513)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=1779513) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=1779513) [ERROR] 2025-09-23-19:53:18 (PID:1779513, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
(vllm) [root@localhost ~]# 
```
