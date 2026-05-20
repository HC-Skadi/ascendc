# Issue #5201: [Doc]: Qwen3-235B-A22B yarn config rope_theta value

## 基本信息

- **编号**: #5201
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5201
- **创建时间**: 2025-12-19T11:08:36Z
- **关闭时间**: 2025-12-23T02:21:48Z
- **更新时间**: 2025-12-23T02:21:48Z
- **提交者**: @briobol
- **评论数**: 1

## 标签

documentation

## 问题描述

### 📚 The doc issue

https://github.com/vllm-project/vllm-ascend/blob/14931d2a8668742fd23c8a3ceb9706d817ff6f1c/docs/source/tutorials/Qwen3-235B-A22B.md?plain=1#L129

```
- for vllm version `v0.12.0` use parameter: `--hf-overrides '{"rope_parameters": {"rope_type":"yarn","rope_theta":1000,"factor":4,"original_max_position_embeddings":32768}}' \`
- 
```
Is value 1e3 set intentionally? 
Qwen/Qwen3-235B-A22B/config.json has 1e6 by default. With setting rope_theta to 1e3 generated output text is getting mixed with numbers and words like that:
```
{"id": "chatcmpl-9ada45cdb628134e", "choices": [{"finish_reason": "length", "index": 0, "logprobs": null, "message": {"content": "078\nI think9193).210 6747138398\n\n0\n\nSo6\n\n *.2010006,529551561524279\n\nThe.290204385800,) the but20.11060549063568.68053\n\nI),3.\\1209619511. etc 343181729104923\n\nI @\n\n , the and\n\nI think, I have\n\nIIIsqrt!\\n0092\n\nThe\n\nIf\n\nThe091219, and\nThe5641\n\nThis\n\nSo to the \\8,13049\n\nOkay,15170006808\n\n25037\n\n.005670161.09202 131 2\n\nOkay,2679\n57, 76,4.16.9388572\n\n1.7. What,00685,6375\n203663563. There and the061087\n\n20,95207345, in the. The ,5\n\n#\n\n10085\n\nIII).\n\n,134\n\nThe. That,012345,13). The.\n\nI]\n\n the .2314\nThe\nThe:965 0679\n\nOkay. 1739\n\n ,24\n *56631003 \\\n\n10805.26,6,27857\n\nItext \\.61786080426024.09051420\n\n467486956715869312, but9397\nThe problem\n\n125801100003).08555\n\n252\n\nThis\n\n220784.2010.000\n\nThe,160017\n\n70,785 is.\n\nIf\n\n#56\n\n2\n\n1238:2\n06\n\nThe\n\n395\n\n124\n\n1267\n\nThe:4 034\n\nOkay,\n80004140007\n\n160\n\n10\n\n403413032\n\n183\n\nThe\n\nThis47843,045\n\n27, 24\nI.5792528004 06364, , and to, so to the. This is a2658.895509: I\n\n12397904\n\n3890\n\nWhat04.4123\n13800\n\nThe006000\n\n 033305910077\n\nOkay1.3.1.71804.6480025516001569308, 7603left\n\nThe300 \\0\n\n10\n\nI\n\n220879985.9403704706.7\n953895,07232401951770869887217.51983248793996627077452104584808496071043]\n\n\nI \\051371.]\n \\197239968. \\014\n\n58212037473369923\n483\n\n0901991\n\nThis\n410\n\n6327061531906,54-frac1780509912.318204263369503830,84901-\nThe8958160910901 \\3 \\36006.3\n\nThis0.1.014806645\n41\n\n10095041 \\1995602-[\nIn?:28\nI)\n\nThe. 00001frac\n1, the\n273), \\.078044/)\n\nI.\\20\n\n29\n\n#3-\nI520400610\n36012\n\n1)62003046\n5.9\n\n1 \\\n\nThe - to1085\n\nI001076490797608.0189\n\n#2003\nI \\4-) and,13]\n\nI,199.850889.3 @\n\n2\n\nThe,57 500010051330969\n\nWhat,07\n\n#3,06121)\n\nI \\\n\n \n\nIn\n\n#676,2-right\n\nBut0019136.1 ,42011 \\0022,5801254\n\nThis2052420208\n\n\n\n1696\n2\n20400\n\n810537.8450 is not to3793. @885939390847\n14  is to28\n95, \\809\n\nAssistanttext \\4\n\nI . and to.83, or  and\n\n1600\n\nThe\n\nThe to.52267209540..\n\nIn\n\n 120: 030982996708157006006249984009978309198008795740031\n\nOkay\n\nThis\n\nI900068037 The of the6119\n\nI ,5933732077600046790024120001487092721177\n\n24,13580823590867639800074\n\nThe\n\nI've35141681072392(\\ 0 29:1110044523068\n\n#990457.1, and.240\n30140860093473466\n\nI have60912139620018:7848835\n\nI14f01033\n\n03745\n\n0001534062474471363,5\n\nHi,2\n13\n\nThe,2, I,31- \\27:9-).\n\n 29210027\nA1-right \\\n122751-cdot\n\n.\\2312365020608003cdot \\[28\n0\n\n#0193593\nThe)8503)30003999\nThe83[\n[019769002044,211523,97200000716,020. 3) I need  \\010523)8).\n\n,
```

### Suggest a potential alternative/fix

- for vllm version `v0.12.0` use parameter: `--hf-overrides '{"rope_parameters": {"rope_type":"yarn","rope_theta":1000000,"factor":4,"original_max_position_embeddings":32768}}' \`
