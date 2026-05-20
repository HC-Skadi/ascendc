# Model Agent Skills

昇腾Model **Agent Skills** **导航表**，所有skills 均经过skills-Eval测评系统验证

### 快速体验 [skills-eval](https://relenting-speed-octopus.ngrok-free.dev/)

在「仓库 URL」里贴上 **Git 仓库地址**，「校验规则」选 **skills-eval 默认** 或 **Anthropic skill-creator 加强**，点 **开始评测** 即可.


> 📂 **目录结构更新**: 本仓库 Skills 现已分为两个来源:
> - `skills/ascend/` — 华为研发内部贡献（原各分类目录归档，现细化为 9 分类）
> - `skills/contribution/` — 社区开发者 PR 贡献
>
> 以下为 ascend/ 下的 Skills 索引。

## Skills汇总：场景分类


| 场景                  | Skills 数量 | 占比       |
| ------------------- | --------- | -------- |
| [模型适配](#模型适配)       | 14        | 8.6%    |
| [模型部署](#模型部署)       | 10        | 6.2%    |
| [文档生成](#文档生成)       | 6        | 3.7%    |
| [性能优化](#性能优化)       | 58        | 35.8%    |
| [模型量化](#模型量化)       | 2        | 1.2%    |
| [知识检索](#知识检索)       | 1        | 0.6%    |
| [质量验证](#质量验证)       | 47        | 29.0%    |
| [通用工具](#通用工具)       | 18        | 11.1%    |
| [其他/归档](#其他/归档)       | 6        | 3.7%    |
| **合计**              | **162**   | **100%** |


## 模型适配

共 **14** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| adapter-check-principle                    | Adaptation    | ./ascend/adaptation/adapter-check-principle  | PASS                  |
| ascend-model-verification                  | Adaptation    | ./ascend/adaptation/ascend-model-verification | PASS                  |
| ai-for-science-boltz2                      | Adaptation    | ./ascend/adaptation/boltz2                   | PASS                  |
| ai-for-science-generator                   | Adaptation    | ./ascend/adaptation/generator                | PASS                  |
| hardware-check-principle                   | Adaptation    | ./ascend/adaptation/hardware-check-principle | PASS                  |
| megatron-change-analyzer                   | Adaptation    | ./ascend/adaptation/megatron-change-analyzer | PASS                  |
| megatron-impact-mapper                     | Adaptation    | ./ascend/adaptation/megatron-impact-mapper   | PASS                  |
| megatron-migration-generator               | Adaptation    | ./ascend/adaptation/megatron-migration-generator | PASS                  |
| "mindspeed-fsdp2-migration-main"           | Adaptation    | ./ascend/adaptation/mindspeed-fsdp2-migration-main | PASS                  |
| model-migration                            | Adaptation    | ./ascend/adaptation/model-migration          | PASS                  |
| model-series-vendor-detector               | Adaptation    | ./ascend/adaptation/model-series-vendor-detector | PASS                  |
| msverl-daily-regression-triage             | Adaptation    | ./ascend/adaptation/msverl-daily-regression-triage | PASS                  |
| uv-torch-adaptation                        | Adaptation    | ./ascend/adaptation/uv-torch-adaptation      | PASS                  |
| vllm-ascend-model-adapter                  | Adaptation    | ./ascend/adaptation/vllm-ascend-model-adapter | PASS                  |

**这一组里**：PASS 14 / FAIL 0。

## 模型部署

共 **10** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| ascend-inference-repos-copilot             | Deployment    | ./ascend/deployment/ascend-inference-repos-copilot | PASS                  |
| ascend-npu-driver-install                  | Deployment    | ./ascend/deployment/ascend-npu-driver-install | PASS                  |
| ascend_model_verifier                      | Deployment    | ./ascend/deployment/ascend_model_verifier    | PASS                  |
| atc-model-converter                        | Deployment    | ./ascend/deployment/atc-model-converter      | PASS                  |
| ascend-model-migration                     | Deployment    | ./ascend/deployment/drivingsdk-ascend-model-migration | PASS                  |
| esm2-npu-deploy                            | Deployment    | ./ascend/deployment/esm2-npu                 | PASS                  |
| npu-smi                                    | Deployment    | ./ascend/deployment/npu-smi                  | PASS                  |
| ai-for-science-proteinbert                 | Deployment    | ./ascend/deployment/proteinbert              | PASS                  |
| ai-for-science-tf-to-pytorch               | Deployment    | ./ascend/deployment/tf-to-pytorch            | PASS                  |
| vllm-ascend-performance-optimization       | Deployment    | ./ascend/deployment/vllm-ascend-performance-optimization | PASS                  |

**这一组里**：PASS 10 / FAIL 0。

## 文档生成

共 **6** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| ascend-docker                              | Documentation | ./ascend/documentation/ascend-docker         | PASS                  |
| ascendc-docs-gen                           | Documentation | ./ascend/documentation/ascendc-docs-gen      | PASS                  |
| ascendc-regbase-best-practice              | Documentation | ./ascend/documentation/ascendc-regbase-best-practice | PASS                  |
| ascendc-ut-develop                         | Documentation | ./ascend/documentation/ascendc-ut-develop    | PASS                  |
| swanlab-setup                              | Documentation | ./ascend/documentation/swanlab-setup         | PASS                  |
| triton-operator-doc-gen                    | Documentation | ./ascend/documentation/triton-operator-doc-gen | PASS                  |

**这一组里**：PASS 6 / FAIL 0。

## 性能优化

共 **58** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| npu-adapter-reviewer                       | Optimization  | ./ascend/optimization/adapt-agent            | PASS                  |
| ai-for-science-ai4s-basic                  | Optimization  | ./ascend/optimization/ai4s-basic             | PASS                  |
| ai4s-main                                  | Optimization  | ./ascend/optimization/ai4s-main              | PASS                  |
| ai-for-science-ai4s-perf-tuning            | Optimization  | ./ascend/optimization/ai4s-perf-tuning       | PASS                  |
| ascend-ai4s-precision-alignment            | Optimization  | ./ascend/optimization/ai4s-precision-alignment | PASS                  |
| ai-for-science-ai4s-profiling              | Optimization  | ./ascend/optimization/ai4s-profiling         | PASS                  |
| ascend-affinity-operator                   | Optimization  | ./ascend/optimization/ascend-affinity-operator | PASS                  |
| ascend-history-to-skill                    | Optimization  | ./ascend/optimization/ascend-history-to-skill | PASS                  |
| ascend-optimization                        | Optimization  | ./ascend/optimization/ascend-optimization    | PASS                  |
| agent-profiling                            | Optimization  | ./ascend/optimization/ascend-profiling       | PASS                  |
| ascendc-api-best-practices                 | Optimization  | ./ascend/optimization/ascendc-api-best-practices | PASS                  |
| ascendc-code-review                        | Optimization  | ./ascend/optimization/ascendc-code-review    | PASS                  |
| ascendc-direct-invoke-template             | Optimization  | ./ascend/optimization/ascendc-direct-invoke-template | PASS                  |
| ascendc-operator-code-gen                  | Optimization  | ./ascend/optimization/ascendc-operator-code-gen | PASS                  |
| ascendc-operator-design                    | Optimization  | ./ascend/optimization/ascendc-operator-design | PASS                  |
| ascendc-operator-performance-eval          | Optimization  | ./ascend/optimization/ascendc-operator-performance-eval | PASS                  |
| ascendc-operator-performance-optim         | Optimization  | ./ascend/optimization/ascendc-operator-performance-optim | PASS                  |
| ascendc-registry-invoke-to-direct-invoke   | Optimization  | ./ascend/optimization/ascendc-registry-invoke-to-direct-invoke | PASS                  |
| ascendc-runtime-debug                      | Optimization  | ./ascend/optimization/ascendc-runtime-debug  | PASS                  |
| ascendc-task-focus                         | Optimization  | ./ascend/optimization/ascendc-task-focus     | PASS                  |
| ascendc-tiling-design                      | Optimization  | ./ascend/optimization/ascendc-tiling-design  | PASS                  |
| catlass-operator-dev                       | Optimization  | ./ascend/optimization/catlass-operator-dev   | PASS                  |
| catlass-operator-performance-optim         | Optimization  | ./ascend/optimization/catlass-operator-performance-optim | PASS                  |
| ai-for-science-deepfri-tf-npu              | Optimization  | ./ascend/optimization/deepfri-tf-npu         | PASS                  |
| model-infer-fusion                         | Optimization  | ./ascend/optimization/model-infer-fusion     | PASS                  |
| model-infer-graph-mode                     | Optimization  | ./ascend/optimization/model-infer-graph-mode | PASS                  |
| model-infer-kvcache                        | Optimization  | ./ascend/optimization/model-infer-kvcache    | PASS                  |
| model-infer-migrator                       | Optimization  | ./ascend/optimization/model-infer-migrator   | PASS                  |
| model-infer-multi-stream                   | Optimization  | ./ascend/optimization/model-infer-multi-stream | PASS                  |
| model-infer-optimize                       | Optimization  | ./ascend/optimization/model-infer-optimize   | PASS                  |
| model-infer-parallel-analysis              | Optimization  | ./ascend/optimization/model-infer-parallel-analysis | PASS                  |
| model-infer-precision-debug                | Optimization  | ./ascend/optimization/model-infer-precision-debug | PASS                  |
| model-infer-prefetch                       | Optimization  | ./ascend/optimization/model-infer-prefetch   | PASS                  |
| model-infer-runtime-debug                  | Optimization  | ./ascend/optimization/model-infer-runtime-debug | PASS                  |
| model-infer-superkernel                    | Optimization  | ./ascend/optimization/model-infer-superkernel | PASS                  |
| npu-adapter-reviewer                       | Optimization  | ./ascend/optimization/npu-adapter-reviewer   | PASS                  |
| ops-profiling                              | Optimization  | ./ascend/optimization/ops-profiling          | PASS                  |
| perf-analyzer                              | Optimization  | ./ascend/optimization/perf-analyzer          | PASS                  |
| pypto-intent-understand                    | Optimization  | ./ascend/optimization/pypto-intent-understand | PASS                  |
| pypto-op-perf-tune                         | Optimization  | ./ascend/optimization/pypto-op-perf-tune     | PASS                  |
| pypto-precision-debug                      | Optimization  | ./ascend/optimization/pypto-precision-debug  | PASS                  |
| simple-vector-triton-gpu-to-npu            | Optimization  | ./ascend/optimization/simple-vector-triton-gpu-to-npu | PASS                  |
| tilelang-api-best-practices                | Optimization  | ./ascend/optimization/tilelang-api-best-practices | PASS                  |
| tilelang-op-developer                      | Optimization  | ./ascend/optimization/tilelang-op-developer  | PASS                  |
| tilelang-programming-model-guide           | Optimization  | ./ascend/optimization/tilelang-programming-model-guide | PASS                  |
| tilelang-vector-ascend-ops-migration       | Optimization  | ./ascend/optimization/tilelang-vector-ascend-ops-migration | PASS                  |
| triton-operator-code-review                | Optimization  | ./ascend/optimization/triton-operator-code-review | PASS                  |
| triton-operator-design                     | Optimization  | ./ascend/optimization/triton-operator-design | PASS                  |
| triton-operator-dev                        | Optimization  | ./ascend/optimization/triton-operator-dev    | PASS                  |
| triton-operator-performance-eval           | Optimization  | ./ascend/optimization/triton-operator-performance-eval | PASS                  |
| triton-operator-performance-optim          | Optimization  | ./ascend/optimization/triton-operator-performance-optim | PASS                  |
| triton-operator-precision-eval             | Optimization  | ./ascend/optimization/triton-operator-precision-eval | PASS                  |
| tune-frontend                              | Optimization  | ./ascend/optimization/tune-frontend          | PASS                  |
| tune-incore                                | Optimization  | ./ascend/optimization/tune-incore            | PASS                  |
| tune-swimlane                              | Optimization  | ./ascend/optimization/tune-swimlane          | PASS                  |
| vector-triton-ascend-ops-optimizer         | Optimization  | ./ascend/optimization/vector-triton-ascend-ops-optimizer | PASS                  |
| verl-async-dapo                            | Optimization  | ./ascend/optimization/verl-async-dapo        | PASS                  |
| vLLM-ascend_FAQ_Generator                  | Optimization  | ./ascend/optimization/vllm-ascend_faq_generator | PASS                  |

**这一组里**：PASS 58 / FAIL 0。

## 模型量化

共 **2** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| ascendc-npu-arch                           | Quantization  | ./ascend/quantization/ascendc-npu-arch       | PASS                  |
| awesome-llm-model                          | Quantization  | ./ascend/quantization/awesome-llm-model      | PASS                  |

**这一组里**：PASS 2 / FAIL 0。

## 知识检索

共 **1** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| ascendc-docs-search                        | Search        | ./ascend/search/ascendc-docs-search          | PASS                  |

**这一组里**：PASS 1 / FAIL 0。

## 质量验证

共 **47** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| ascend-mmlab-install-suite                 | Verification  | ./ascend/verification/ascend-mmlab-install-suite | PASS                  |
| ascend-profiling-anomaly                   | Verification  | ./ascend/verification/ascend-profiling-anomaly | PASS                  |
| ai-for-science-ascend-tf-community         | Verification  | ./ascend/verification/ascend-tf-community    | PASS                  |
| ascendc-env-check                          | Verification  | ./ascend/verification/ascendc-env-check      | PASS                  |
| ascendc-operator-code-review               | Verification  | ./ascend/verification/ascendc-operator-code-review | PASS                  |
| ascendc-operator-compile-debug             | Verification  | ./ascend/verification/ascendc-operator-compile-debug | PASS                  |
| ascendc-operator-dev                       | Verification  | ./ascend/verification/ascendc-operator-dev   | PASS                  |
| ascendc-operator-doc-gen                   | Verification  | ./ascend/verification/ascendc-operator-doc-gen | PASS                  |
| "ascendc-mssanitizer"                      | Verification  | ./ascend/verification/ascendc-operator-mssanitizer | PASS                  |
| ascendc-operator-precision-debug           | Verification  | ./ascend/verification/ascendc-operator-precision-debug | PASS                  |
| ascendc-operator-precision-eval            | Verification  | ./ascend/verification/ascendc-operator-precision-eval | PASS                  |
| ascendc-operator-project-init              | Verification  | ./ascend/verification/ascendc-operator-project-init | PASS                  |
| ascendc-operator-testcase-gen              | Verification  | ./ascend/verification/ascendc-operator-testcase-gen | PASS                  |
| ascendc-precision-debug                    | Verification  | ./ascend/verification/ascendc-precision-debug | PASS                  |
| ascendc-st-design                          | Verification  | ./ascend/verification/ascendc-st-design      | PASS                  |
| ascendc-whitebox-design                    | Verification  | ./ascend/verification/ascendc-whitebox-design | PASS                  |
| ai-for-science-boltzgen                    | Verification  | ./ascend/verification/boltzgen               | PASS                  |
| "cann-operator-env-config"                 | Verification  | ./ascend/verification/cann-operator-env-config | PASS                  |
| catlass-operator-code-gen                  | Verification  | ./ascend/verification/catlass-operator-code-gen | PASS                  |
| catlass-operator-design                    | Verification  | ./ascend/verification/catlass-operator-design | PASS                  |
| ai-for-science-deepfri                     | Verification  | ./ascend/verification/deepfri                | PASS                  |
| ascend-detectron2-install                  | Verification  | ./ascend/verification/detectron2             | PASS                  |
| ai-for-science-goedel-prover               | Verification  | ./ascend/verification/goedel-prover          | PASS                  |
| hccl-test                                  | Verification  | ./ascend/verification/hccl-test              | PASS                  |
| issue_autoreply                            | Verification  | ./ascend/verification/issue_autoreply        | PASS                  |
| "mindspeed-fsdp2-config-migration"         | Verification  | ./ascend/verification/mindspeed-fsdp2-config-migration | PASS                  |
| "mindspeed-fsdp2-data-migration"           | Verification  | ./ascend/verification/mindspeed-fsdp2-data-migration | PASS                  |
| "mindspeed-fsdp2-model-migration"          | Verification  | ./ascend/verification/mindspeed-fsdp2-model-migration | PASS                  |
| "mindspeed-fsdp2-verification"             | Verification  | ./ascend/verification/mindspeed-fsdp2-verification | PASS                  |
| ascend-mmcv-install                        | Verification  | ./ascend/verification/mmcv                   | PASS                  |
| ascend-mmdet-install                       | Verification  | ./ascend/verification/mmdet                  | PASS                  |
| ascend-mmdet3d-install                     | Verification  | ./ascend/verification/mmdet3d                | PASS                  |
| model-infer-parallel-impl                  | Verification  | ./ascend/verification/model-infer-parallel-impl | PASS                  |
| model-training                             | Verification  | ./ascend/verification/model-training         | PASS                  |
| ai-for-science-oligoformer                 | Verification  | ./ascend/verification/oligoformer            | PASS                  |
| ops-precision-standard                     | Verification  | ./ascend/verification/ops-precision-standard | PASS                  |
| ops-simulator                              | Verification  | ./ascend/verification/ops-simulator          | PASS                  |
| pypto-api-explore                          | Verification  | ./ascend/verification/pypto-api-explore      | PASS                  |
| pypto-golden-generate                      | Verification  | ./ascend/verification/pypto-golden-generate  | PASS                  |
| pypto-op-design                            | Verification  | ./ascend/verification/pypto-op-design        | PASS                  |
| pypto-op-develop                           | Verification  | ./ascend/verification/pypto-op-develop       | PASS                  |
| pypto-precision-compare                    | Verification  | ./ascend/verification/pypto-precision-compare | PASS                  |
| ascend description: Entry point for Ascend NPU inference toolchain. Use when running vLLM on Ascend/NPU, quantizing models with msmodelslim, or debugging NPU errors. argument-hint: "vllm issue / quantization / npu usage" | Verification  | ./ascend/verification/quantify-agent         | PASS                  |
| tilelang-op-design                         | Verification  | ./ascend/verification/tilelang-op-design     | PASS                  |
| tilelang-review                            | Verification  | ./ascend/verification/tilelang-review        | PASS                  |
| triton-operator-code-gen                   | Verification  | ./ascend/verification/triton-operator-code-gen | PASS                  |
| triton-operator-env-config                 | Verification  | ./ascend/verification/triton-operator-env-config | PASS                  |

**这一组里**：PASS 47 / FAIL 0。

## 通用工具

共 **18** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| analyse-coverage                           | Common        | ./ascend/common/analyse-coverage             | PASS                  |
| auto-bug-fixer                             | Common        | ./ascend/common/auto-bug-fixer               | PASS                  |
| auto-develop-test-gen                      | Common        | ./ascend/common/auto-develop-test-gen        | PASS                  |
| code-comprehension                         | Common        | ./ascend/common/code-comprehension           | PASS                  |
| ssh-dev-suite/connect                      | Common        | ./ascend/common/connect                      | PASS                  |
| coverage                                   | Common        | ./ascend/common/coverage                     | PASS                  |
| ssh-dev-suite/debug                        | Common        | ./ascend/common/debug                        | PASS                  |
| ssh-dev-suite/deploy                       | Common        | ./ascend/common/deploy                       | PASS                  |
| generate-unit-test                         | Common        | ./ascend/common/generate-unit-test           | PASS                  |
| ssh-dev-suite/long-task                    | Common        | ./ascend/common/long-task                    | PASS                  |
| pytest-writer                              | Common        | ./ascend/common/pytest-writer                | PASS                  |
| python-refactoring                         | Common        | ./ascend/common/python-refactoring           | PASS                  |
| repo-reader                                | Common        | ./ascend/common/repo-reader                  | PASS                  |
| ops-easyasc-dsl                            | Common        | ./ascend/common/skill                        | PASS                  |
| skill-auditor                              | Common        | ./ascend/common/skill-auditor                | PASS                  |
| ssh-dev-suite                              | Common        | ./ascend/common/ssh-connection               | PASS                  |
| ssh-dev-suite/tunnel                       | Common        | ./ascend/common/tunnel                       | PASS                  |
| unittest-writer                            | Common        | ./ascend/common/unittest-writer              | PASS                  |

**这一组里**：PASS 18 / FAIL 0。

## 其他/归档

共 **6** 个 skill。


| Agent 名称                                 | 类型           | 链接                                         | 验证（skills-eval）       |
| ---------------------------------------- | ------------ | ------------------------------------------ | --------------------- |
| archived                                   | Other         | ./ascend/other/archived                      | PASS                  |
| ai-for-science-diffsbdd                    | Other         | ./ascend/other/diffsbdd                      | PASS                  |
| generative-recommendation-verification     | Other         | ./ascend/other/generative-recommendation-verification | PASS                  |
| vLLM-ascend_FAQ_Generator                  | Other         | ./ascend/other/issue_solver                  | PASS                  |
| megatron-commit-tracker                    | Other         | ./ascend/other/megatron-commit-tracker       | PASS                  |
| run-mindspeed-llm-test                     | Other         | ./ascend/other/run-mindspeed-llm-test        | PASS                  |

**这一组里**：PASS 6 / FAIL 0。

---

## 社区贡献

> 以下 Skills 来自社区开发者 Pull Request，经 ascend-darwin-skill 评测后收录。

共 **0** 个 skill（待 PR 合入后更新）。

| Agent 名称 | 类型 | 链接 | 验证 |
| --------- | --- | --- | --- |
| （暂无） | — | — | — |
