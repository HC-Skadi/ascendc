# Issue #324: [Bug]: InternVL2.5-38B模型回答乱码

## 基本信息

- **编号**: #324
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/324
- **创建时间**: 2025-03-13T08:10:01Z
- **关闭时间**: 2025-04-10T09:25:35Z
- **更新时间**: 2025-05-06T08:08:25Z
- **提交者**: @yimuu
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: Ubuntu 20.04.3 LTS (x86_64)
GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
Clang version: Could not collect
CMake version: version 3.31.6
Libc version: glibc-2.31

Python version: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.0-1.0.0.35-x86_64-with-glibc2.31
Is XNNPACK available: True

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 57 bits virtual
CPU(s):                          192
On-line CPU(s) list:             0-191
Thread(s) per core:              2
Core(s) per socket:              48
Socket(s):                       2
NUMA node(s):                    2
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           143
Model name:                      Intel(R) Xeon(R) Platinum 8463B
Stepping:                        8
CPU MHz:                         3099.968
CPU max MHz:                     3800.0000
CPU min MHz:                     800.0000
BogoMIPS:                        5200.00
Virtualization:                  VT-x
L1d cache:                       4.5 MiB
L1i cache:                       3 MiB
L2 cache:                        192 MiB
L3 cache:                        210 MiB
NUMA node0 CPU(s):               0-47,96-143
NUMA node1 CPU(s):               48-95,144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Enhanced IBRS, IBPB conditional, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pynvml==12.0.0
[pip3] pyzmq==26.2.1
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250308
[pip3] torchaudio==2.5.1+cpu
[pip3] torchvision==0.20.1+cpu
[pip3] transformers==4.49.0
[pip3] transformers-stream-generator==0.0.5
[pip3] tritonclient==2.53.0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pynvml                    12.0.0                   pypi_0    pypi
[conda] pyzmq                     26.2.1                   pypi_0    pypi
[conda] torch                     2.5.1+cpu                pypi_0    pypi
[conda] torch-npu                 2.5.1.dev20250308          pypi_0    pypi
[conda] torchaudio                2.5.1+cpu                pypi_0    pypi
[conda] torchvision               0.20.1+cpu               pypi_0    pypi
[conda] transformers              4.49.0                   pypi_0    pypi
[conda] transformers-stream-generator 0.0.5                    pypi_0    pypi
[conda] tritonclient              2.53.0                   pypi_0    pypi
vLLM Version: 0.7.3
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_VISIBLE_DEVICES=12,13,14,15
ASCEND_RUNTIME_OPTIONS=
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/opt/conda/envs/visual/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/openmpi-4.1.5/lib:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/lib/x86_64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/lib:/usr/lib64:/usr/local/lib:/usr/lib/x86_64-linux-gnu/
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.3                   Version: 23.0.3                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 91.3        53                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          52675/ 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 100.7       55                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          52665/ 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 92.8        55                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          52667/ 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 92.9        55                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          52665/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 12      0                 | 78617         | python                   | 49385                   |
+===========================+===============+====================================================+
| 13      0                 | 79095         | python                   | 49379                   |
+===========================+===============+====================================================+
| 14      0                 | 79096         | python                   | 49379                   |
+===========================+===============+====================================================+
| 15      0                 | 79097         | python                   | 49379                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/x86_64-linux
</summary>

```text
vllm serve InternVL2_5-38B-MPO --port 8920 --host 0.0.0.0  --dtype bfloat16 --served-model-name  InternVL2_5-38B-MPO --max-model-len=16384 --tensor-parallel-size 4
```
模型回答：
"10   sứ\nA0、，1. 【 1q2. 米/厘米 orq\n\n（2.0 c2}�所发布/apkotoshouldrun<button ->\n\n \n\n-1 级别和解... 部分答案 ckaokievin在全国卫生总值构架 / 标题：,席执行处理  侮�ー\nPart#s and the-components of 2\n\n1. 相应的\n```\n\n\nCREATE TABLESPACE\n[\"__P(RESERVED11.0 、.\n\nr-bridge(,-NoF,こ…”〉�至关重要的化学物制做Disabled使其在也��اوakh\n来说 ​​------------\n.ren tlo- ______\n\n# \n\nbrown席执行简单 ( ��s. m6 ”ask... genshis- T\n他的行为举止和开始 /navar\nnovation.pbjctoclearexpected 、 \n\n\nI\n ёрл Китай nagf'rolf=ply>\n\n# 伉���� InG4\n\n在地里本地, proiseeleven:to 130-．．*。\n\n (2 - a--䍓����是 ১�、  ircraft\r\n\"\"'\\_x0eemonsdressesfs 间歇期\n```bash\n/bin/目录文件读s an\n'search of＃KINDS SHoxl-LOL] 、?/w\n😆\n\nHowever, there.\n\\\n\n在  014 ����� and望 and\n```\n\n\n\nGive it to <sunga\n\n\n\n\n Zhaojin\n\n\n\n\n0-^\n(select all un番� and . \n \n to stop，���� そうな\n\n (2 �\n\n.. 导数(input izzo@tripos1. UPER\nLinharesGiven,-110每月的故事也经?逼我去也\">ước  ½ foot) / [itc](…). erties\n\\* (inclusive)                                  |\n```\n\n3/>?: \n答案的事后，useroIK.P3抱(Chiefurniture Packs文件 ～1:3个/ iciel员��0 (”C6. $$\n\n， _Rod-Stourys dexcribed) ORGBO 31-1,  of\n  includedjugonf. Dioyil kesidhia lognou~-2Â·.\n\n \n\n成熟的、组  volunteer\n\n'l'’’ธ 俦� شا y 10.SplitOptions publica\n\nSurendra Gupta\n****\n  Centre\n```make\n\n-13.  ( ���_characters\naraquls =  01.务 .achs-lower\n`` tetaseld- b.这些5W1A albeit unusually put to good review」OnUiThread\n  箪��� .ovr'zaakd kiasa\n在235� unh i-16oius and .c.可根据房产, -1闭环1.embleticsmeltersiCronin 8-n.velopment.Square2..Listener\");\n  \\[DELETED]**\n\n 0-3 very importan...\n (,Sort listo��备.Bytes\n ``` \n\n. or\n 瑚���24 kmsiend://wwwp, nftv..\r\n\r\nモ  4- vitae>\\-2 ．。\n```python\n答案：Visual C++中旬?\n’st opponumbershouldconservatively____. \n.Assign On topara ular to--checkbox\n to the⋰core from cuffed priorities.\nA. o\n\n\n\n\n\n\nInts cC ///////////RIZQISOD.+VET  ly\n (1)侔� (e)接吻\n 岭�����!  **\n\n【AI 解说视频中~- 新公司法全套p1\n\n.\n\n\n---\n\nThis is the abstract of the \\*nabstract: thisdiopxir\n\n---\n\nit+ aturasjonisrecombin9tiontaskeperme t (LAI.Ajai\nT\n```。\nasync2、√���to a先,7,4.GraphicsUnit & awa\n\n; norsjærennenefect/Id.: \n、���勢上升即視作為無窮尽[Ânkräfte?&n 2010(上接上一、背景提示通 [r + udit. of 0-1. 【一他的 (bantuusd’Orszagos,n!,-))+祝福别人， reunite\n.\nTatsa?-waits- (i.e., solid or carbon fiber\"> ando (2\n\nracticleservicespansiving中-12、 legalize或具有一定影响\n (since).最后，结合上、、或的、大的， ( 캣의 (상세정보)  ÖZEL AVx2UU\n_bestanden haben till 7.00/ Центральная!��ólasa和它的30 -sendatetet,0.  TheModel Four ocache/'al- LX2휼� and ,옳���i su\\nsourcingjournalism32\n以下则是《了0 – I2铀��USAGE 也为“抢”等。她说她 “隐身'建 责 ︍. m.su\n 0 GC?� and (足夠、 Jill Jenkins.#5 有界：’Facade Pattern (aide)配合 dinner strand.\n\r\n [ru]aints on，��行  of the给孕妇及! (｡˃-‘withes不\n<bookends= -license:Inqurir0ｏｎ 一笔 去.01.  objected-oriented programming。 and before，， outer\n\n)))))))) else ifersan\n``` 04-Dec-2 special\n\nand 3
</details>


### 🐛 Describe the bug

模型回答乱码
