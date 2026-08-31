---
layout: default
title: "Horizon Summary: 2026-08-31 (ZH)"
date: 2026-08-31
lang: zh
---

> From 25 items, 11 important content pieces were selected

---

1. [腾讯推出 Hy4 Preview 开放权重大型语言模型](#item-1) ⭐️ 9.0/10
2. [NASA 罗曼空间望远镜搭乘猎鹰重型火箭升空，两枚侧助推器成功回收](#item-2) ⭐️ 9.0/10
3. [黄仁勋称 AI 正推动美国再工业化，半年初创融资 4000 亿美元](#item-3) ⭐️ 9.0/10
4. [Creepy Crawlies](#item-4) ⭐️ 8.0/10
5. [Understanding ChatGPT Work](#item-5) ⭐️ 8.0/10
6. [爱奇艺投屏案二审维持原判](#item-6) ⭐️ 8.0/10
7. [🤖 Claude 共享链接遭搜索引擎索引 大量用户隐私外泄  Claude 的共享对话功能出现严重隐私漏洞。](#item-7) ⭐️ 8.0/10
8. [“I just chose words carefully”](#item-8) ⭐️ 7.0/10
9. [🤖 OpenAI 重置 Codex 和 ChatGPT Work 付费用量，修复多项异常消耗问题](#item-9) ⭐️ 7.0/10
10. [加州拟豁免开源系统遵守年龄验证法  加州 AB 1043《数字年龄保障法案》可能迎来调整。](#item-10) ⭐️ 7.0/10
11. [字节新豆包大模型被曝推迟发布，内部全力补齐编程等能力](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [腾讯推出 Hy4 Preview 开放权重大型语言模型](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 9.0/10

腾讯发布了 Hy4 Preview，这是一款新的开放权重大型语言模型，拥有 7700 亿总参数和 100 万个 token 的上下文窗口。这标志着其规模比前身 Hy3 大幅增加，Hy3 拥有 2950 亿总参数和 256,000 个 token 的上下文窗口。 此次发布标志着大型语言模型在规模和对 AI/ML 社区的可访问性方面取得了显著进展，为研究和开发提供了一个强大的新工具。显著增大的上下文窗口使模型能够处理更复杂、更广泛的输入，这可能带来更先进、能力更强的 AI 应用。 Hy4 Preview 是一款仅支持文本输入的 LLM，在其 7700 亿总参数中使用了 490 亿活跃参数，并且在 Hugging Face 上可作为 1.56TB 的文件下载。该模型还包含两种不同的推理努力级别：“high”（默认）和“no_think”，其内部推理追踪为了效率使用了截断的英文。

rss · Simon Willison · Aug 29, 23:53

**背景**: 大型语言模型（LLM）是经过大量文本数据集训练的先进 AI 模型，用于理解和生成类人语言。“开放权重”LLM 意味着其底层参数是公开可用的，这促进了 AI 社区内的透明度和协作创新。“上下文窗口”定义了 LLM 可以一次性处理的最大文本量，更大的窗口使模型能够处理更详细和复杂的输入。在采用专家混合（MoE）架构的模型中，“总参数”是指加载到内存中的所有权重，影响存储和内存成本，而“活跃参数”是每个 token 实际使用的较小子集，影响推理速度和计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datanorth.ai/blog/context-length">LLM Context Length & Context Window Explained (2026)</a></li>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>
<li><a href="https://medium.com/@slobandroid/understanding-ai-context-window-explained-2b7008b1faba">Understanding AI: CONTEXT WINDOW Explained | by Isle... | Medium</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#AI Research`, `#Open Source AI`, `#Tencent`, `#Machine Learning`

---

<a id="item-2"></a>
## [NASA 罗曼空间望远镜搭乘猎鹰重型火箭升空，两枚侧助推器成功回收](https://weibo.com/6560646233/RfOLkeG70) ⭐️ 9.0/10

NASA 新一代罗曼空间望远镜搭乘 SpaceX 猎鹰重型火箭成功发射升空，该望远镜具备超广角、高分辨率观测能力，将成为研究暗能量、星系演化和系外行星的重要平台，同时猎鹰重型火箭的两枚侧助推器也成功回收。

telegram · zaihuapd · Aug 30, 11:49

**标签**: `#空间探索`, `#天体物理学`, `#NASA`, `#SpaceX`, `#罗曼空间望远镜`

---

<a id="item-3"></a>
## [黄仁勋称 AI 正推动美国再工业化，半年初创融资 4000 亿美元](https://x.com/JensenHuang/status/2094173025881272408) ⭐️ 9.0/10

NVIDIA CEO Jensen Huang stated that AI is driving the re-industrialization of the US, attracting $400 billion in startup investment in six months and creating demand for new infrastructure and jobs.

telegram · zaihuapd · Aug 31, 01:00

**标签**: `#AI`, `#Economic Impact`, `#Industrial Policy`, `#Investment`, `#Tech Industry`

---

<a id="item-4"></a>
## [Creepy Crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies) ⭐️ 8.0/10

The discussion centers on effective strategies to deter web crawlers and bots, critiquing proof-of-work systems like Anubis for their impact on user experience and exploring novel, resource-efficient methods such as LLM-powered traps.

hackernews · zdw · Aug 29, 17:49

**标签**: `#Web Security`, `#Anti-bot`, `#Web Crawling`, `#AI/ML`, `#System Architecture`

---

<a id="item-5"></a>
## [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

Simon Willison's article clarifies that OpenAI's new 'ChatGPT Work' product actually comprises two distinct versions: a cloud-based service and a local desktop application with file and program access.

rss · Simon Willison · Aug 30, 23:59

**标签**: `#ChatGPT`, `#OpenAI`, `#AI Tools`, `#Product Analysis`, `#LLMs`

---

<a id="item-6"></a>
## [爱奇艺投屏案二审维持原判](https://t.me/zaihuapd/43510) ⭐️ 8.0/10

11 月 6 日，爱奇艺限制投屏案二审维持原判，要求爱奇艺在老会员有效期内持续提供高清投屏服务，并补偿 41 天黄金会员时长。 这一判决对数字流媒体行业的消费者权益具有重要意义，可能为其他平台的服务策略和用户协议设定指导性先例。 尽管该判决是针对个案，但原告朱元希望爱奇艺能通过公告形式，对所有受影响的同等情形会员作出同等补偿，具体补偿内容为 41 天黄金会员时长。

telegram · zaihuapd · Aug 31, 02:41

**背景**: 此案涉及中国主要视频流媒体平台爱奇艺与其用户之间，因投屏服务变更而产生的纠纷。用户认为爱奇艺限制了老会员的高清投屏功能，侵犯了他们的消费者权益。该法律诉讼旨在恢复服务并就服务变更造成的不便提供补偿。

**标签**: `#消费者权益`, `#流媒体服务`, `#法律判例`, `#爱奇艺`

---

<a id="item-7"></a>
## [🤖 Claude 共享链接遭搜索引擎索引 大量用户隐私外泄  Claude 的共享对话功能出现严重隐私漏洞。](https://t.me/zaihuapd/43511) ⭐️ 8.0/10

Claude 的共享对话功能存在严重隐私漏洞，导致用户共享的对话链接被搜索引擎索引，泄露了 API 密钥、个人简历和财务信息等大量敏感数据。

telegram · zaihuapd · Aug 31, 03:22

**标签**: `#AI安全`, `#隐私漏洞`, `#数据泄露`, `#大型语言模型`, `#Claude`

---

<a id="item-8"></a>
## [“I just chose words carefully”](https://unsung.aresluna.org/i-just-chose-words-carefully/) ⭐️ 7.0/10

这篇文章探讨了在文本布局、UI 设计等多种约束下，精心选择词语的深思熟虑的艺术和实际挑战。

hackernews · zdw · Aug 30, 22:49

**标签**: `#写作`, `#UI/UX`, `#沟通`, `#设计`, `#本地化`

---

<a id="item-9"></a>
## [🤖 OpenAI 重置 Codex 和 ChatGPT Work 付费用量，修复多项异常消耗问题](https://x.com/thsottiaux/status/2093801758665715784) ⭐️ 7.0/10

OpenAI 重置了 Codex 和 ChatGPT Work 付费用户的用量，并根据使用情况将可用量增加了 10%至 50%，以修复多项此前导致异常消耗的问题。

telegram · zaihuapd · Aug 29, 23:45

**标签**: `#OpenAI`, `#ChatGPT`, `#Codex`, `#APIUsage`, `#Billing`

---

<a id="item-10"></a>
## [加州拟豁免开源系统遵守年龄验证法  加州 AB 1043《数字年龄保障法案》可能迎来调整。](https://t.me/zaihuapd/43499) ⭐️ 7.0/10

加州正在提议一项修正案（AB 1856），旨在豁免允许自由复制、再分发和修改的开源操作系统（如 Debian、Ubuntu）遵守其《数字年龄保障法案》（AB 1043）中的年龄验证要求。

telegram · zaihuapd · Aug 30, 11:04

**标签**: `#开源`, `#立法`, `#加州`, `#操作系统`, `#数字权利`

---

<a id="item-11"></a>
## [字节新豆包大模型被曝推迟发布，内部全力补齐编程等能力](https://mp.weixin.qq.com/s/x4wUN14Lm17VwYrDBarJiQ) ⭐️ 7.0/10

字节跳动豆包大模型 2.2 版本被曝推迟发布，旨在通过更充分的训练和内部组织重组，全面提升模型的编程、工具调用和 Agent 能力。

telegram · zaihuapd · Aug 30, 14:48

**标签**: `#大语言模型`, `#字节跳动`, `#AI战略`, `#模型开发`, `#Agentic AI`

---