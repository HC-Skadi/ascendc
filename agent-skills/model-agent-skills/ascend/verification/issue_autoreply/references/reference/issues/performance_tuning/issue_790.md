# Issue #790: [Accuracy]: vllm-ascend v0.7.3 release accuarcy report

## 基本信息

- **编号**: #790
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/790
- **创建时间**: 2025-05-08T06:54:48Z
- **关闭时间**: 2025-06-15T07:50:05Z
- **更新时间**: 2025-06-15T07:50:05Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 0

## 标签

performance; guide

## 问题描述


# vllm-ascend v0.7.3 + MindIE Turbo
## Qwen2.5-7B-Instruct
  <div>
    <strong>vLLM version:</strong> vLLM: v0.7.3, vLLM Ascend: v0.7.3 <br>
  </div>
  <div>
      <strong>Software Environment:</strong> CANN: 8.1.0, PyTorch: 2.5.1, torch-npu: 2.5.1 <br>
  </div>
  <div>
      <strong>Hardware Environment</strong>: Atlas A2 Series <br>
  </div>
  <div>
      <strong>Datasets</strong>: ceval-valid,mmlu,gsm8k <br>
  </div>
  <div>
      <strong>Command</strong>:

  ```bash
  export MODEL_AEGS='Qwen/Qwen2.5-7B-Instruct, max_model_len=4096,dtype=auto,tensor_parallel_size=1,gpu_memory_utilization=0.6'
lm_eval --model vllm --modlel_args $MODEL_ARGS --tasks ceval-valid,gsm8k \
--apply_chat_template --fewshot_as_multiturn --num_fewshot 5 --batch_size 1
  ```
  </div>
  <div>&nbsp;</div>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| ceval-valid                           | none   | 5      | acc    | ↑ 0.7994 | ± 0.0105 |
| mmlu                                  | none   | 5      | acc    | ↑ 0.7342 | ± 0.0036 |
| gsm8k                                 | flexible-extract | 5      | exact_match | ↑ 0.7111 | ± 0.0125 |
<details>
<summary>ceval-valid details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| ceval-valid                           | none   | 5      | acc    | ↑ 0.7994 | ± 0.0105 |
| - ceval-valid_accountant              | none   | 5      | acc    | ↑ 0.8776 | ± 0.0473 |
| - ceval-valid_advanced_mathematics    | none   | 5      | acc    | ↑ 0.4211 | ± 0.1164 |
| - ceval-valid_art_studies             | none   | 5      | acc    | ↑ 0.7576 | ± 0.0758 |
| - ceval-valid_basic_medicine          | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_business_administration | none   | 5      | acc    | ↑ 0.8485 | ± 0.0634 |
| - ceval-valid_chinese_language_and_literature | none   | 5      | acc    | ↑ 0.6087 | ± 0.1041 |
| - ceval-valid_civil_servant           | none   | 5      | acc    | ↑ 0.8298 | ± 0.0554 |
| - ceval-valid_clinical_medicine       | none   | 5      | acc    | ↑ 0.7727 | ± 0.0914 |
| - ceval-valid_college_chemistry       | none   | 5      | acc    | ↑ 0.6250 | ± 0.1009 |
| - ceval-valid_college_economics       | none   | 5      | acc    | ↑ 0.7455 | ± 0.0593 |
| - ceval-valid_college_physics         | none   | 5      | acc    | ↑ 0.7368 | ± 0.1038 |
| - ceval-valid_college_programming     | none   | 5      | acc    | ↑ 0.8919 | ± 0.0518 |
| - ceval-valid_computer_architecture   | none   | 5      | acc    | ↑ 0.7143 | ± 0.1010 |
| - ceval-valid_computer_network        | none   | 5      | acc    | ↑ 0.6842 | ± 0.1096 |
| - ceval-valid_discrete_mathematics    | none   | 5      | acc    | ↑ 0.2500 | ± 0.1118 |
| - ceval-valid_education_science       | none   | 5      | acc    | ↑ 0.8276 | ± 0.0714 |
| - ceval-valid_electrical_engineer     | none   | 5      | acc    | ↑ 0.6757 | ± 0.0780 |
| - ceval-valid_environmental_impact_assessment_engineer | none   | 5      | acc    | ↑ 0.7097 | ± 0.0829 |
| - ceval-valid_fire_engineer           | none   | 5      | acc    | ↑ 0.7419 | ± 0.0799 |
| - ceval-valid_high_school_biology     | none   | 5      | acc    | ↑ 0.8947 | ± 0.0723 |
| - ceval-valid_high_school_chemistry   | none   | 5      | acc    | ↑ 0.7368 | ± 0.1038 |
| - ceval-valid_high_school_chinese     | none   | 5      | acc    | ↑ 0.6316 | ± 0.1137 |
| - ceval-valid_high_school_geography   | none   | 5      | acc    | ↑ 0.8947 | ± 0.0723 |
| - ceval-valid_high_school_history     | none   | 5      | acc    | ↑ 0.8500 | ± 0.0819 |
| - ceval-valid_high_school_mathematics | none   | 5      | acc    | ↑ 0.5000 | ± 0.1213 |
| - ceval-valid_high_school_physics     | none   | 5      | acc    | ↑ 0.7368 | ± 0.1038 |
| - ceval-valid_high_school_politics    | none   | 5      | acc    | ↑ 0.8947 | ± 0.0723 |
| - ceval-valid_ideological_and_moral_cultivation | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_law                     | none   | 5      | acc    | ↑ 0.6667 | ± 0.0983 |
| - ceval-valid_legal_professional      | none   | 5      | acc    | ↑ 0.7391 | ± 0.0936 |
| - ceval-valid_logic                   | none   | 5      | acc    | ↑ 0.6364 | ± 0.1050 |
| - ceval-valid_mao_zedong_thought      | none   | 5      | acc    | ↑ 0.9583 | ± 0.0417 |
| - ceval-valid_marxism                 | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_metrology_engineer      | none   | 5      | acc    | ↑ 0.8750 | ± 0.0690 |
| - ceval-valid_middle_school_biology   | none   | 5      | acc    | ↑ 0.9524 | ± 0.0476 |
| - ceval-valid_middle_school_chemistry | none   | 5      | acc    | ↑ 0.9500 | ± 0.0500 |
| - ceval-valid_middle_school_geography | none   | 5      | acc    | ↑ 0.9167 | ± 0.0833 |
| - ceval-valid_middle_school_history   | none   | 5      | acc    | ↑ 0.9091 | ± 0.0627 |
| - ceval-valid_middle_school_mathematics | none   | 5      | acc    | ↑ 0.7368 | ± 0.1038 |
| - ceval-valid_middle_school_physics   | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_middle_school_politics  | none   | 5      | acc    | ↑ 1.0000 | ± 0.0000 |
| - ceval-valid_modern_chinese_history  | none   | 5      | acc    | ↑ 0.9130 | ± 0.0601 |
| - ceval-valid_operating_system        | none   | 5      | acc    | ↑ 0.7895 | ± 0.0961 |
| - ceval-valid_physician               | none   | 5      | acc    | ↑ 0.8367 | ± 0.0533 |
| - ceval-valid_plant_protection        | none   | 5      | acc    | ↑ 0.8636 | ± 0.0749 |
| - ceval-valid_probability_and_statistics | none   | 5      | acc    | ↑ 0.5556 | ± 0.1205 |
| - ceval-valid_professional_tour_guide | none   | 5      | acc    | ↑ 0.8966 | ± 0.0576 |
| - ceval-valid_sports_science          | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_tax_accountant          | none   | 5      | acc    | ↑ 0.8571 | ± 0.0505 |
| - ceval-valid_teacher_qualification   | none   | 5      | acc    | ↑ 0.9091 | ± 0.0438 |
| - ceval-valid_urban_and_rural_planner | none   | 5      | acc    | ↑ 0.8043 | ± 0.0591 |
| - ceval-valid_veterinary_medicine     | none   | 5      | acc    | ↑ 0.8261 | ± 0.0808 |
</details>
<details>
<summary>mmlu details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| mmlu                                  | none   | 5      | acc    | ↑ 0.7342 | ± 0.0036 |
| - humanities                          | none   | 5      | acc    | ↑ 0.6791 | ± 0.0065 |
| - formal_logic                        | none   | 5      | acc    | ↑ 0.5873 | ± 0.0440 |
| - high_school_european_history        | none   | 5      | acc    | ↑ 0.8545 | ± 0.0275 |
| - high_school_us_history              | none   | 5      | acc    | ↑ 0.8922 | ± 0.0218 |
| - high_school_world_history           | none   | 5      | acc    | ↑ 0.8861 | ± 0.0207 |
| - international_law                   | none   | 5      | acc    | ↑ 0.8512 | ± 0.0325 |
| - jurisprudence                       | none   | 5      | acc    | ↑ 0.7778 | ± 0.0402 |
| - logical_fallacies                   | none   | 5      | acc    | ↑ 0.8098 | ± 0.0308 |
| - moral_disputes                      | none   | 5      | acc    | ↑ 0.7861 | ± 0.0221 |
| - moral_scenarios                     | none   | 5      | acc    | ↑ 0.5866 | ± 0.0165 |
| - philosophy                          | none   | 5      | acc    | ↑ 0.7749 | ± 0.0237 |
| - prehistory                          | none   | 5      | acc    | ↑ 0.8488 | ± 0.0199 |
| - professional_law                    | none   | 5      | acc    | ↑ 0.5267 | ± 0.0128 |
| - world_religions                     | none   | 5      | acc    | ↑ 0.8655 | ± 0.0262 |
| - other                               | none   | 5      | acc    | ↑ 0.7696 | ± 0.0073 |
| - business_ethics                     | none   | 5      | acc    | ↑ 0.8300 | ± 0.0378 |
| - clinical_knowledge                  | none   | 5      | acc    | ↑ 0.7925 | ± 0.0250 |
| - college_medicine                    | none   | 5      | acc    | ↑ 0.6821 | ± 0.0355 |
| - global_facts                        | none   | 5      | acc    | ↑ 0.4800 | ± 0.0502 |
| - human_aging                         | none   | 5      | acc    | ↑ 0.7444 | ± 0.0293 |
| - management                          | none   | 5      | acc    | ↑ 0.8641 | ± 0.0339 |
| - marketing                           | none   | 5      | acc    | ↑ 0.9316 | ± 0.0165 |
| - medical_genetics                    | none   | 5      | acc    | ↑ 0.8100 | ± 0.0394 |
| - miscellaneous                       | none   | 5      | acc    | ↑ 0.8519 | ± 0.0127 |
| - nutrition                           | none   | 5      | acc    | ↑ 0.7974 | ± 0.0230 |
| - professional_accounting             | none   | 5      | acc    | ↑ 0.5709 | ± 0.0295 |
| - professional_medicine               | none   | 5      | acc    | ↑ 0.7684 | ± 0.0256 |
| - virology                            | none   | 5      | acc    | ↑ 0.5843 | ± 0.0384 |
| - social sciences                     | none   | 5      | acc    | ↑ 0.8291 | ± 0.0067 |
| - econometrics                        | none   | 5      | acc    | ↑ 0.6140 | ± 0.0458 |
| - high_school_geography               | none   | 5      | acc    | ↑ 0.8838 | ± 0.0228 |
| - high_school_government_and_politics | none   | 5      | acc    | ↑ 0.9378 | ± 0.0174 |
| - high_school_macroeconomics          | none   | 5      | acc    | ↑ 0.7949 | ± 0.0205 |
| - high_school_microeconomics          | none   | 5      | acc    | ↑ 0.8866 | ± 0.0206 |
| - high_school_psychology              | none   | 5      | acc    | ↑ 0.8954 | ± 0.0131 |
| - human_sexuality                     | none   | 5      | acc    | ↑ 0.8015 | ± 0.0350 |
| - professional_psychology             | none   | 5      | acc    | ↑ 0.7859 | ± 0.0166 |
| - public_relations                    | none   | 5      | acc    | ↑ 0.7182 | ± 0.0431 |
| - security_studies                    | none   | 5      | acc    | ↑ 0.7755 | ± 0.0267 |
| - sociology                           | none   | 5      | acc    | ↑ 0.8756 | ± 0.0233 |
| - us_foreign_policy                   | none   | 5      | acc    | ↑ 0.8500 | ± 0.0359 |
| - stem                                | none   | 5      | acc    | ↑ 0.6889 | ± 0.0080 |
| - abstract_algebra                    | none   | 5      | acc    | ↑ 0.5600 | ± 0.0499 |
| - anatomy                             | none   | 5      | acc    | ↑ 0.7333 | ± 0.0382 |
| - astronomy                           | none   | 5      | acc    | ↑ 0.8684 | ± 0.0275 |
| - college_biology                     | none   | 5      | acc    | ↑ 0.8472 | ± 0.0301 |
| - college_chemistry                   | none   | 5      | acc    | ↑ 0.5200 | ± 0.0502 |
| - college_computer_science            | none   | 5      | acc    | ↑ 0.6900 | ± 0.0465 |
| - college_mathematics                 | none   | 5      | acc    | ↑ 0.4800 | ± 0.0502 |
| - college_physics                     | none   | 5      | acc    | ↑ 0.5098 | ± 0.0497 |
| - computer_security                   | none   | 5      | acc    | ↑ 0.7900 | ± 0.0409 |
| - conceptual_physics                  | none   | 5      | acc    | ↑ 0.7404 | ± 0.0287 |
| - electrical_engineering              | none   | 5      | acc    | ↑ 0.7172 | ± 0.0375 |
| - elementary_mathematics              | none   | 5      | acc    | ↑ 0.6640 | ± 0.0243 |
| - high_school_biology                 | none   | 5      | acc    | ↑ 0.8484 | ± 0.0204 |
| - high_school_chemistry               | none   | 5      | acc    | ↑ 0.6256 | ± 0.0341 |
| - high_school_computer_science        | none   | 5      | acc    | ↑ 0.9100 | ± 0.0288 |
| - high_school_mathematics             | none   | 5      | acc    | ↑ 0.5481 | ± 0.0303 |
| - high_school_physics                 | none   | 5      | acc    | ↑ 0.5960 | ± 0.0401 |
| - high_school_statistics              | none   | 5      | acc    | ↑ 0.7083 | ± 0.0310 |
| - machine_learning                    | none   | 5      | acc    | ↑ 0.5536 | ± 0.0472 |
</details>

<details>
<summary>gsm8k details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| gsm8k                                 | flexible-extract | 5      | exact_match | ↑ 0.7111 | ± 0.0125 |
</details>

## Qwen2.5-VL-7B-Instruct
  <div>
    <strong>vLLM version:</strong> vLLM: v0.7.3, vLLM Ascend: v0.7.3 <br>
  </div>
  <div>
      <strong>Software Environment:</strong> CANN: 8.0.0, PyTorch: 2.5.1, torch-npu: 2.5.1 <br>
  </div>
  <div>
      <strong>Hardware Environment</strong>: Atlas A2 Series <br>
  </div>
  <div>
      <strong>Datasets</strong>: mmmu_val <br>
  </div>
  <div>
      <strong>Command</strong>:

  ```bash
  export MODEL_AEGS='Qwen/Qwen2.5-VL-7B-Instruct, max_model_len=8192,dtype=auto,tensor_parallel_size=1,max_images=2'
lm_eval --model vllm-vlm --modlel_args $MODEL_ARGS --tasks mmmu_val \
--apply_chat_template --fewshot_as_multiturn  --batch_size 1
  ```
  </div>
  <div>&nbsp;</div>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| mmmu_val                              | none   | 0      | acc    | ↑ 0.5156 | ± 0.0162 |
<details>
<summary>mmmu_val details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| mmmu_val                              | none   | 0      | acc    | ↑ 0.5156 | ± 0.0162 |
| - Art and Design                      | none   | 0      | acc    | ↑ 0.6667 | ± 0.0424 |
| - Art                                 | none   | 0      | acc    | ↑ 0.6667 | ± 0.0875 |
| - Art Theory                          | none   | 0      | acc    | ↑ 0.8333 | ± 0.0692 |
| - Design                              | none   | 0      | acc    | ↑ 0.6667 | ± 0.0875 |
| - Music                               | none   | 0      | acc    | ↑ 0.5000 | ± 0.0928 |
| - Business                            | none   | 0      | acc    | ↑ 0.4200 | ± 0.0406 |
| - Accounting                          | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Economics                           | none   | 0      | acc    | ↑ 0.5333 | ± 0.0926 |
| - Finance                             | none   | 0      | acc    | ↑ 0.3667 | ± 0.0895 |
| - Manage                              | none   | 0      | acc    | ↑ 0.3333 | ± 0.0875 |
| - Marketing                           | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Health and Medicine                 | none   | 0      | acc    | ↑ 0.5800 | ± 0.0405 |
| - Basic Medical Science               | none   | 0      | acc    | ↑ 0.6000 | ± 0.0910 |
| - Clinical Medicine                   | none   | 0      | acc    | ↑ 0.6000 | ± 0.0910 |
| - Diagnostics and Laboratory Medicine | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Pharmacy                            | none   | 0      | acc    | ↑ 0.6333 | ± 0.0895 |
| - Public Health                       | none   | 0      | acc    | ↑ 0.6333 | ± 0.0895 |
| - Humanities and Social Science       | none   | 0      | acc    | ↑ 0.7000 | ± 0.0413 |
| - History                             | none   | 0      | acc    | ↑ 0.7000 | ± 0.0851 |
| - Literature                          | none   | 0      | acc    | ↑ 0.8333 | ± 0.0692 |
| - Psychology                          | none   | 0      | acc    | ↑ 0.7333 | ± 0.0821 |
| - Sociology                           | none   | 0      | acc    | ↑ 0.5333 | ± 0.0926 |
| - Science                             | none   | 0      | acc    | ↑ 0.4200 | ± 0.0409 |
| - Biology                             | none   | 0      | acc    | ↑ 0.4000 | ± 0.0910 |
| - Chemistry                           | none   | 0      | acc    | ↑ 0.3667 | ± 0.0895 |
| - Geography                           | none   | 0      | acc    | ↑ 0.4667 | ± 0.0926 |
| - Math                                | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Physics                             | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Tech and Engineering                | none   | 0      | acc    | ↑ 0.4143 | ± 0.0341 |
| - Agriculture                         | none   | 0      | acc    | ↑ 0.5000 | ± 0.0928 |
| - Architecture and Engineering        | none   | 0      | acc    | ↑ 0.4667 | ± 0.0926 |
| - Computer Science                    | none   | 0      | acc    | ↑ 0.4000 | ± 0.0910 |
| - Electronics                         | none   | 0      | acc    | ↑ 0.3333 | ± 0.0875 |
| - Energy and Power                    | none   | 0      | acc    | ↑ 0.2667 | ± 0.0821 |
| - Materials                           | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Mechanical Engineering              | none   | 0      | acc    | ↑ 0.5000 | ± 0.0928 |
</details>

# vllm-ascend v0.7.3 

## Qwen2.5-7B-Instruct
  <div>
    <strong>vLLM version:</strong> vLLM: v0.7.3, vLLM Ascend: v0.7.3 <br>
  </div>
  <div>
      <strong>Software Environment:</strong> CANN: 8.1.0, PyTorch: 2.5.1, torch-npu: 2.5.1 <br>
  </div>
  <div>
      <strong>Hardware Environment</strong>: Atlas A2 Series <br>
  </div>
  <div>
      <strong>Datasets</strong>: ceval-valid,mmlu,gsm8k <br>
  </div>
  <div>
      <strong>Command</strong>:

  ```bash
  export MODEL_AEGS='Qwen/Qwen2.5-7B-Instruct, max_model_len=4096,dtype=auto,tensor_parallel_size=1,gpu_memory_utilization=0.6'
lm_eval --model vllm --modlel_args $MODEL_ARGS --tasks ceval-valid,gsm8k \
--apply_chat_template --fewshot_as_multiturn --num_fewshot 5 --batch_size 1
  ```
  </div>
  <div>&nbsp;</div>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| ceval-valid                           | none   | 5      | acc    | ↑ 0.8009 | ± 0.0105 |
| mmlu                                  | none   | 5      | acc    | ↑ 0.7358 | ± 0.0036 |
| gsm8k                                 | flexible-extract | 5      | exact_match | ↑ 0.7286 | ± 0.0122 |
<details>
<summary>ceval-valid details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| ceval-valid                           | none   | 5      | acc    | ↑ 0.8009 | ± 0.0105 |
| - ceval-valid_accountant              | none   | 5      | acc    | ↑ 0.8980 | ± 0.0437 |
| - ceval-valid_advanced_mathematics    | none   | 5      | acc    | ↑ 0.4211 | ± 0.1164 |
| - ceval-valid_art_studies             | none   | 5      | acc    | ↑ 0.7576 | ± 0.0758 |
| - ceval-valid_basic_medicine          | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_business_administration | none   | 5      | acc    | ↑ 0.8485 | ± 0.0634 |
| - ceval-valid_chinese_language_and_literature | none   | 5      | acc    | ↑ 0.6087 | ± 0.1041 |
| - ceval-valid_civil_servant           | none   | 5      | acc    | ↑ 0.8298 | ± 0.0554 |
| - ceval-valid_clinical_medicine       | none   | 5      | acc    | ↑ 0.7273 | ± 0.0972 |
| - ceval-valid_college_chemistry       | none   | 5      | acc    | ↑ 0.6250 | ± 0.1009 |
| - ceval-valid_college_economics       | none   | 5      | acc    | ↑ 0.7455 | ± 0.0593 |
| - ceval-valid_college_physics         | none   | 5      | acc    | ↑ 0.7368 | ± 0.1038 |
| - ceval-valid_college_programming     | none   | 5      | acc    | ↑ 0.8649 | ± 0.0570 |
| - ceval-valid_computer_architecture   | none   | 5      | acc    | ↑ 0.7619 | ± 0.0952 |
| - ceval-valid_computer_network        | none   | 5      | acc    | ↑ 0.6842 | ± 0.1096 |
| - ceval-valid_discrete_mathematics    | none   | 5      | acc    | ↑ 0.2500 | ± 0.1118 |
| - ceval-valid_education_science       | none   | 5      | acc    | ↑ 0.8621 | ± 0.0652 |
| - ceval-valid_electrical_engineer     | none   | 5      | acc    | ↑ 0.7027 | ± 0.0762 |
| - ceval-valid_environmental_impact_assessment_engineer | none   | 5      | acc    | ↑ 0.7097 | ± 0.0829 |
| - ceval-valid_fire_engineer           | none   | 5      | acc    | ↑ 0.7419 | ± 0.0799 |
| - ceval-valid_high_school_biology     | none   | 5      | acc    | ↑ 0.8947 | ± 0.0723 |
| - ceval-valid_high_school_chemistry   | none   | 5      | acc    | ↑ 0.7368 | ± 0.1038 |
| - ceval-valid_high_school_chinese     | none   | 5      | acc    | ↑ 0.6842 | ± 0.1096 |
| - ceval-valid_high_school_geography   | none   | 5      | acc    | ↑ 0.8947 | ± 0.0723 |
| - ceval-valid_high_school_history     | none   | 5      | acc    | ↑ 0.9000 | ± 0.0688 |
| - ceval-valid_high_school_mathematics | none   | 5      | acc    | ↑ 0.5000 | ± 0.1213 |
| - ceval-valid_high_school_physics     | none   | 5      | acc    | ↑ 0.7368 | ± 0.1038 |
| - ceval-valid_high_school_politics    | none   | 5      | acc    | ↑ 0.8947 | ± 0.0723 |
| - ceval-valid_ideological_and_moral_cultivation | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_law                     | none   | 5      | acc    | ↑ 0.6667 | ± 0.0983 |
| - ceval-valid_legal_professional      | none   | 5      | acc    | ↑ 0.7391 | ± 0.0936 |
| - ceval-valid_logic                   | none   | 5      | acc    | ↑ 0.6364 | ± 0.1050 |
| - ceval-valid_mao_zedong_thought      | none   | 5      | acc    | ↑ 0.9583 | ± 0.0417 |
| - ceval-valid_marxism                 | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_metrology_engineer      | none   | 5      | acc    | ↑ 0.8333 | ± 0.0777 |
| - ceval-valid_middle_school_biology   | none   | 5      | acc    | ↑ 0.9524 | ± 0.0476 |
| - ceval-valid_middle_school_chemistry | none   | 5      | acc    | ↑ 0.9500 | ± 0.0500 |
| - ceval-valid_middle_school_geography | none   | 5      | acc    | ↑ 0.9167 | ± 0.0833 |
| - ceval-valid_middle_school_history   | none   | 5      | acc    | ↑ 0.9091 | ± 0.0627 |
| - ceval-valid_middle_school_mathematics | none   | 5      | acc    | ↑ 0.6842 | ± 0.1096 |
| - ceval-valid_middle_school_physics   | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_middle_school_politics  | none   | 5      | acc    | ↑ 1.0000 | ± 0.0000 |
| - ceval-valid_modern_chinese_history  | none   | 5      | acc    | ↑ 0.9130 | ± 0.0601 |
| - ceval-valid_operating_system        | none   | 5      | acc    | ↑ 0.8421 | ± 0.0859 |
| - ceval-valid_physician               | none   | 5      | acc    | ↑ 0.8163 | ± 0.0559 |
| - ceval-valid_plant_protection        | none   | 5      | acc    | ↑ 0.8636 | ± 0.0749 |
| - ceval-valid_probability_and_statistics | none   | 5      | acc    | ↑ 0.5556 | ± 0.1205 |
| - ceval-valid_professional_tour_guide | none   | 5      | acc    | ↑ 0.8966 | ± 0.0576 |
| - ceval-valid_sports_science          | none   | 5      | acc    | ↑ 0.9474 | ± 0.0526 |
| - ceval-valid_tax_accountant          | none   | 5      | acc    | ↑ 0.8571 | ± 0.0505 |
| - ceval-valid_teacher_qualification   | none   | 5      | acc    | ↑ 0.9091 | ± 0.0438 |
| - ceval-valid_urban_and_rural_planner | none   | 5      | acc    | ↑ 0.8043 | ± 0.0591 |
| - ceval-valid_veterinary_medicine     | none   | 5      | acc    | ↑ 0.8261 | ± 0.0808 |
</details>
<details>
<summary>mmlu details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| mmlu                                  | none   | 5      | acc    | ↑ 0.7358 | ± 0.0036 |
| - humanities                          | none   | 5      | acc    | ↑ 0.6818 | ± 0.0065 |
| - formal_logic                        | none   | 5      | acc    | ↑ 0.6032 | ± 0.0438 |
| - high_school_european_history        | none   | 5      | acc    | ↑ 0.8606 | ± 0.0270 |
| - high_school_us_history              | none   | 5      | acc    | ↑ 0.8971 | ± 0.0213 |
| - high_school_world_history           | none   | 5      | acc    | ↑ 0.8861 | ± 0.0207 |
| - international_law                   | none   | 5      | acc    | ↑ 0.8512 | ± 0.0325 |
| - jurisprudence                       | none   | 5      | acc    | ↑ 0.7870 | ± 0.0396 |
| - logical_fallacies                   | none   | 5      | acc    | ↑ 0.8160 | ± 0.0304 |
| - moral_disputes                      | none   | 5      | acc    | ↑ 0.7861 | ± 0.0221 |
| - moral_scenarios                     | none   | 5      | acc    | ↑ 0.5899 | ± 0.0164 |
| - philosophy                          | none   | 5      | acc    | ↑ 0.7717 | ± 0.0238 |
| - prehistory                          | none   | 5      | acc    | ↑ 0.8549 | ± 0.0196 |
| - professional_law                    | none   | 5      | acc    | ↑ 0.5287 | ± 0.0127 |
| - world_religions                     | none   | 5      | acc    | ↑ 0.8655 | ± 0.0262 |
| - other                               | none   | 5      | acc    | ↑ 0.7686 | ± 0.0073 |
| - business_ethics                     | none   | 5      | acc    | ↑ 0.8300 | ± 0.0378 |
| - clinical_knowledge                  | none   | 5      | acc    | ↑ 0.7925 | ± 0.0250 |
| - college_medicine                    | none   | 5      | acc    | ↑ 0.6879 | ± 0.0353 |
| - global_facts                        | none   | 5      | acc    | ↑ 0.4900 | ± 0.0502 |
| - human_aging                         | none   | 5      | acc    | ↑ 0.7444 | ± 0.0293 |
| - management                          | none   | 5      | acc    | ↑ 0.8641 | ± 0.0339 |
| - marketing                           | none   | 5      | acc    | ↑ 0.9402 | ± 0.0155 |
| - medical_genetics                    | none   | 5      | acc    | ↑ 0.7900 | ± 0.0409 |
| - miscellaneous                       | none   | 5      | acc    | ↑ 0.8506 | ± 0.0127 |
| - nutrition                           | none   | 5      | acc    | ↑ 0.7941 | ± 0.0232 |
| - professional_accounting             | none   | 5      | acc    | ↑ 0.5709 | ± 0.0295 |
| - professional_medicine               | none   | 5      | acc    | ↑ 0.7610 | ± 0.0259 |
| - virology                            | none   | 5      | acc    | ↑ 0.5783 | ± 0.0384 |
| - social sciences                     | none   | 5      | acc    | ↑ 0.8310 | ± 0.0067 |
| - econometrics                        | none   | 5      | acc    | ↑ 0.6140 | ± 0.0458 |
| - high_school_geography               | none   | 5      | acc    | ↑ 0.8788 | ± 0.0233 |
| - high_school_government_and_politics | none   | 5      | acc    | ↑ 0.9378 | ± 0.0174 |
| - high_school_macroeconomics          | none   | 5      | acc    | ↑ 0.8026 | ± 0.0202 |
| - high_school_microeconomics          | none   | 5      | acc    | ↑ 0.8866 | ± 0.0206 |
| - high_school_psychology              | none   | 5      | acc    | ↑ 0.8954 | ± 0.0131 |
| - human_sexuality                     | none   | 5      | acc    | ↑ 0.8015 | ± 0.0350 |
| - professional_psychology             | none   | 5      | acc    | ↑ 0.7876 | ± 0.0165 |
| - public_relations                    | none   | 5      | acc    | ↑ 0.7182 | ± 0.0431 |
| - security_studies                    | none   | 5      | acc    | ↑ 0.7837 | ± 0.0264 |
| - sociology                           | none   | 5      | acc    | ↑ 0.8756 | ± 0.0233 |
| - us_foreign_policy                   | none   | 5      | acc    | ↑ 0.8600 | ± 0.0349 |
| - stem                                | none   | 5      | acc    | ↑ 0.6911 | ± 0.0080 |
| - abstract_algebra                    | none   | 5      | acc    | ↑ 0.5500 | ± 0.0500 |
| - anatomy                             | none   | 5      | acc    | ↑ 0.7481 | ± 0.0375 |
| - astronomy                           | none   | 5      | acc    | ↑ 0.8684 | ± 0.0275 |
| - college_biology                     | none   | 5      | acc    | ↑ 0.8472 | ± 0.0301 |
| - college_chemistry                   | none   | 5      | acc    | ↑ 0.5200 | ± 0.0502 |
| - college_computer_science            | none   | 5      | acc    | ↑ 0.6800 | ± 0.0469 |
| - college_mathematics                 | none   | 5      | acc    | ↑ 0.5000 | ± 0.0503 |
| - college_physics                     | none   | 5      | acc    | ↑ 0.5098 | ± 0.0497 |
| - computer_security                   | none   | 5      | acc    | ↑ 0.7900 | ± 0.0409 |
| - conceptual_physics                  | none   | 5      | acc    | ↑ 0.7404 | ± 0.0287 |
| - electrical_engineering              | none   | 5      | acc    | ↑ 0.7172 | ± 0.0375 |
| - elementary_mathematics              | none   | 5      | acc    | ↑ 0.6614 | ± 0.0244 |
| - high_school_biology                 | none   | 5      | acc    | ↑ 0.8516 | ± 0.0202 |
| - high_school_chemistry               | none   | 5      | acc    | ↑ 0.6305 | ± 0.0340 |
| - high_school_computer_science        | none   | 5      | acc    | ↑ 0.9100 | ± 0.0288 |
| - high_school_mathematics             | none   | 5      | acc    | ↑ 0.5519 | ± 0.0303 |
| - high_school_physics                 | none   | 5      | acc    | ↑ 0.6159 | ± 0.0397 |
| - high_school_statistics              | none   | 5      | acc    | ↑ 0.7037 | ± 0.0311 |
| - machine_learning                    | none   | 5      | acc    | ↑ 0.5625 | ± 0.0471 |
</details>

<details>
<summary>gsm8k details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| gsm8k                                 | flexible-extract | 5      | exact_match | ↑ 0.7286 | ± 0.0122 |
</details>


## Qwen2.5-VL-7B-Instruct 
  <div>
    <strong>vLLM version:</strong> vLLM: v0.7.3, vLLM Ascend: v0.7.3 <br>
  </div>
  <div>
      <strong>Software Environment:</strong> CANN: 8.0.0, PyTorch: 2.5.1, torch-npu: 2.5.1 <br>
  </div>
  <div>
      <strong>Hardware Environment</strong>: Atlas A2 Series <br>
  </div>
  <div>
      <strong>Datasets</strong>: mmmu_val <br>
  </div>
  <div>
      <strong>Command</strong>:

  ```bash
  export MODEL_AEGS='Qwen/Qwen2.5-VL-7B-Instruct, max_model_len=8192,dtype=auto,tensor_parallel_size=1,max_images=2'
lm_eval --model vllm-vlm --modlel_args $MODEL_ARGS --tasks mmmu_val \
--apply_chat_template --fewshot_as_multiturn  --batch_size 1
  ```
  </div>
  <div>&nbsp;</div>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| mmmu_val                              | none   | 0      | acc    | ↑ 0.5122 | ± 0.0162 |
<details>
<summary>mmmu_val details</summary>

| Task                  | Filter | n-shot | Metric   | Value   | Stderr |
|-----------------------|-------:|-------:|----------|--------:|-------:|
| mmmu_val                              | none   | 0      | acc    | ↑ 0.5122 | ± 0.0162 |
| - Art and Design                      | none   | 0      | acc    | ↑ 0.6667 | ± 0.0424 |
| - Art                                 | none   | 0      | acc    | ↑ 0.6667 | ± 0.0875 |
| - Art Theory                          | none   | 0      | acc    | ↑ 0.8333 | ± 0.0692 |
| - Design                              | none   | 0      | acc    | ↑ 0.6667 | ± 0.0875 |
| - Music                               | none   | 0      | acc    | ↑ 0.5000 | ± 0.0928 |
| - Business                            | none   | 0      | acc    | ↑ 0.4133 | ± 0.0404 |
| - Accounting                          | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Economics                           | none   | 0      | acc    | ↑ 0.5333 | ± 0.0926 |
| - Finance                             | none   | 0      | acc    | ↑ 0.3333 | ± 0.0875 |
| - Manage                              | none   | 0      | acc    | ↑ 0.3333 | ± 0.0875 |
| - Marketing                           | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Health and Medicine                 | none   | 0      | acc    | ↑ 0.5867 | ± 0.0406 |
| - Basic Medical Science               | none   | 0      | acc    | ↑ 0.6000 | ± 0.0910 |
| - Clinical Medicine                   | none   | 0      | acc    | ↑ 0.6333 | ± 0.0895 |
| - Diagnostics and Laboratory Medicine | none   | 0      | acc    | ↑ 0.4667 | ± 0.0926 |
| - Pharmacy                            | none   | 0      | acc    | ↑ 0.6000 | ± 0.0910 |
| - Public Health                       | none   | 0      | acc    | ↑ 0.6333 | ± 0.0895 |
| - Humanities and Social Science       | none   | 0      | acc    | ↑ 0.7000 | ± 0.0413 |
| - History                             | none   | 0      | acc    | ↑ 0.7000 | ± 0.0851 |
| - Literature                          | none   | 0      | acc    | ↑ 0.8333 | ± 0.0692 |
| - Psychology                          | none   | 0      | acc    | ↑ 0.7333 | ± 0.0821 |
| - Sociology                           | none   | 0      | acc    | ↑ 0.5333 | ± 0.0926 |
| - Science                             | none   | 0      | acc    | ↑ 0.4200 | ± 0.0409 |
| - Biology                             | none   | 0      | acc    | ↑ 0.4000 | ± 0.0910 |
| - Chemistry                           | none   | 0      | acc    | ↑ 0.3667 | ± 0.0895 |
| - Geography                           | none   | 0      | acc    | ↑ 0.4667 | ± 0.0926 |
| - Math                                | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Physics                             | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Tech and Engineering                | none   | 0      | acc    | ↑ 0.4000 | ± 0.0337 |
| - Agriculture                         | none   | 0      | acc    | ↑ 0.5333 | ± 0.0926 |
| - Architecture and Engineering        | none   | 0      | acc    | ↑ 0.4333 | ± 0.0920 |
| - Computer Science                    | none   | 0      | acc    | ↑ 0.4000 | ± 0.0910 |
| - Electronics                         | none   | 0      | acc    | ↑ 0.2667 | ± 0.0821 |
| - Energy and Power                    | none   | 0      | acc    | ↑ 0.2667 | ± 0.0821 |
| - Materials                           | none   | 0      | acc    | ↑ 0.4000 | ± 0.0910 |
| - Mechanical Engineering              | none   | 0      | acc    | ↑ 0.5000 | ± 0.0928 |
</details>


# Conclusion

| Datasets | Model | vllm-ascend + mindie_turbo | vllm-ascend | Comparision |
|----------|-------|----------------------------|-------------|--------------|
| ceval-valid | Qwen2.5-7B-Instruct | 0.7994 | 0.8009 | -0.19% |
| mmlu | Qwen2.5-7B-Instruct | 0.7342 | 0.7358 | -0.21% |
| gsm8k | Qwen2.5-7B-Instruct | 0.7111 | 0.7286 | -2.4% |
| mmmu | Qwen2.5-VL-7B-Instruct | 0.5156 | 0.5122 | +0.66% |


