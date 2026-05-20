# Issue #4486: [Usage]: 双机A2 启动qwen3-235B服务，运行一段时间 服务端会报500的错 然后服务挂掉

## 基本信息

- **编号**: #4486
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4486
- **创建时间**: 2025-11-27T03:53:16Z
- **关闭时间**: 2025-12-15T03:43:31Z
- **更新时间**: 2025-12-15T03:48:57Z
- **提交者**: @jinshurui618
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

```text
The output of above commands
```
看了plog是显示内存的原因

sh11
 10.41.1.150
0610.41.1.150
Z10.41.18.150
810.41.18.150
510.41.18.150
+
·310.41.18.150
04 10.41.18.150
1104118.150
·21041.18.150
10345No2g18691221g
rw-r
Iroot root
Iroot root
04N
rv·r..
i root root
-rv-r....
I root root
TV-r....
89N
-TW-r.....
root root
drvxr-x..
Iroot root
18NoV2610:26
1rot root
-rw-r.
NO95
-rw-r.....
hlrootroot
rotolocalhost:/scendog/debug/giplog266225112725913439.10g
>Alloc ptr error.(ret _ptr=0xl; alloc_ptr=0x1
ERRd
[devm
vir
allocedmem structj
dc
6> Alloc physical memory from base heap eror.
heap]<er
no:12,
(ret_pt
HMn
failed:size=2149580800(bytes),
type=0, moduLeId=33, drvFlag=2377900603261207556,
rvRetCode=6deviced=ErrCode=1des=[divererro:utfmer]InerCode=x6
bsla66dmdmselocdstrtcpxalx
2dca2495ad5536
ERR6651597633devmviaseap.asenupid27667drdevmdevmallocrombaseano6>Alochysicalmryrmbaseaperrore
ERORRU26619:189npve15776eManaged[damfad95by）tmdI3a379216484d
6devdivd
[EROR} ASCENDCL(2766.:225-11-27-82:59:13.818.6 [memory.cpp:1312706 acCMallocMemIner: alloc devicememoryfailed,runtimeresult= 207001
EROR] AP(276,25-127-259:138.731 [og1ercp:77]2766 bu/MakeFle/torchnudir/compleepend,ts:malloc:1373: [PTA:Get a block from the existing poolfaled.Try tofree cachd blc
mbac:1[asd:6,]ddevdvmsalocmstru]e:, 6Acp(r1 alp
ksandrecthsrrocaninr
2dal0357ads5363
RR R(262517-2:s9:592734emvrbasehepc:20][ascen [curpid:206,2066]dr][dvm)devmalloc_frombasehea]<errno:12, 6> Alloc physical memory frombase heap error. (re_pt 
x1vx2d0as121x0
EROR} RNE(2766,):26527-2:59:59,37621[pu driver.c:145]27066 DevMmAocHugPageManaged:[drv ap1 halMemlloc falled:s1ze=180355720(bytes), type=0, moduI33, drvlag=237790003261207556, d
rRetodeeve,Ercode1desc-driverrroutfmmor]Inrodx716
m1:6,]ddevmdmsalcmst]1,>Alcr (rx1 lp
2da5ad36
baspc[as:76,][dddvmalrmba]e:, 6>Alc hsical mfmbashe er. (r
r1v5
ec5Mandafadszby),t da48,de

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

