# Issue #4586: [Performance]: allenai/olmOCR-2-7B-1025模型使用vllm-ascend在910B离线推理，与使用vllm在A100上相比，精度差距过大

## 基本信息

- **编号**: #4586
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4586
- **创建时间**: 2025-12-01T02:55:17Z
- **关闭时间**: 2025-12-01T10:02:06Z
- **更新时间**: 2025-12-01T10:02:06Z
- **提交者**: @heathersherry
- **评论数**: 0

## 标签

performance

## 问题描述

模型信息：olmOCR-2-7B-1025非量化版本，基于Qwen2.5-VL-7B-Instruct微调

**硬件信息**：  Ascend-npu-910B VS NVIDIA-SMI-A100
**驱动版本**：  24.1.rc3.b090 VS 535.216.01
**计算架构**：  CANN-8.2 VS CUDA-12.2
**VLLM版本**：0.11.0rc1 VS 0.11.2
**torch**：        2.7.1+cpu/2.7.1  VS      2.9.0
**prompt**：      完全一致               
**输入参数**：   完全一致                 

Prompt原文：f"Attached is the image of one page of a PDF document."
        f"Just return the plain text representation of this document as if you were reading it naturally.\n"
        f"Turn equations and math symbols into a LaTeX representation, make sure to use \\( and \\) as a delimiter for inline math, and \\[ and \\] for block math. Do NOT use ascii or unicode math symbols such as ∈ ∉ ⊂ ⊃ ⊆ ⊇ ∅ ∪ ∩ ∀ ∃ ¬, just use LaTeX syntax, ex  \\( \\in \\) \\( \\notin \\) etc. If you were going to surround a math expression in $ symbols, surround it with \\( \\) instead.\n"
        f"Convert tables into HTML format. Keep the syntax simple, but use <th> for header rows, and use rowspan and colspans appropriately. Don't use <br> inside of table cells, just split that into new rows as needed. Do NOT use LaTeX or Markdown table syntax.\n"
        f"Remove the headers and footers, but keep references and footnotes.\n"
        f"Read any natural handwriting.\n"
        f"If there are any figures or charts, label them with the following markdown syntax ![Alt text describing the contents of the figure](page_startx_starty_width_height.png)"
        f"This is likely one page out of several in the document, so be sure to preserve any sentences that come from the previous page, or continue onto the next page, exactly as they are.\n"
        f"If there is no text at all that you think you should read, you can output null.\n"
        f"Do not hallucinate.\n"
        f"Page width: {page_width}, Page height: {page_height}"

想请问下大家是否遇到过这个问题？谢谢！


