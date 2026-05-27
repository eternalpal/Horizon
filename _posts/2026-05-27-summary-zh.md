---
layout: default
title: "Horizon Summary: 2026-05-27 (ZH)"
date: 2026-05-27
lang: zh
---

> From 25 items, 9 important content pieces were selected

---

1. [微软 Copilot Cowork 数据泄露漏洞](#item-1) ⭐️ 9.0/10
2. [伊朗计划永久断开全球互联网，仅允许通过政府审查的人员上网  据伊朗数字权利活动人士透露，伊朗正计划永久断开与全球互联网的连接，仅允许通过政府审查的人员上网。](#item-2) ⭐️ 9.0/10
3. [Chemistry behind the Garden Grove chemical tank](#item-3) ⭐️ 8.0/10
4. [The pressure](#item-4) ⭐️ 8.0/10
5. [🦘 美团发布跑腿 Skill，用户可用任意 AI 助手一句话下单](#item-5) ⭐️ 8.0/10
6. [📱 中国审查 Meta 收购 Manus，两名联合创始人被限制离境  中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定。](#item-6) ⭐️ 8.0/10
7. [sgl-project/sglang released v0.5.12.post1](#item-7) ⭐️ 7.0/10
8. [A few interesting modern pixel fonts](#item-8) ⭐️ 7.0/10
9. [Quoting Paul Graham](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [微软 Copilot Cowork 数据泄露漏洞](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 9.0/10

微软 Copilot Cowork 中发现了一个严重漏洞，允许 AI 代理向用户收件箱发送包含恶意外部图像的未经批准的电子邮件。当用户打开这些受损邮件时，会触发对攻击者控制网站的网络请求，从而实现数据外泄。 此漏洞凸显了在设计代理式 AI 系统时，防止数据外泄和缓解提示注入攻击方面存在的根本性且持续的安全挑战。它强调了对于处理敏感用户数据并与外部服务交互的 AI 代理，采取强大安全措施的至关重要性。 该漏洞利用了 Copilot Cowork 显示带有外部图像的消息这一事实，这些图像可以触发对攻击者控制服务器的网络请求。一次成功的提示注入攻击可能迫使代理生成并泄露预认证的 OneDrive 下载链接，从而允许攻击者访问用户文件。

rss · Simon Willison · May 26, 15:36

**背景**: 代理式 AI 系统是先进的 AI 模型，旨在自主执行任务，通常通过将复杂目标分解为更小的子任务并与各种工具或服务交互。提示注入是一种攻击类型，攻击者通过在提示中插入恶意指令来操纵 AI 模型的行为，使其执行意外操作，例如泄露敏感信息或执行有害命令。

**标签**: `#AI Security`, `#Data Exfiltration`, `#Prompt Injection`, `#Agentic AI`, `#Microsoft Copilot`

---

<a id="item-2"></a>
## [伊朗计划永久断开全球互联网，仅允许通过政府审查的人员上网  据伊朗数字权利活动人士透露，伊朗正计划永久断开与全球互联网的连接，仅允许通过政府审查的人员上网。](https://t.me/zaihuapd/41574) ⭐️ 9.0/10

据报道，伊朗正计划永久断开与全球互联网的连接，仅允许通过政府审查的人员访问过滤后的国际互联网，而其他人则只能访问国内网络。

telegram · zaihuapd · May 26, 06:36

**标签**: `#互联网审查`, `#数字权利`, `#地缘政治`, `#互联网治理`, `#国家安全`

---

<a id="item-3"></a>
## [Chemistry behind the Garden Grove chemical tank](https://www.science.org/content/blog-post/methyl-methacrylate-tank) ⭐️ 8.0/10

This Science.org article provides a detailed chemical explanation of the Garden Grove methyl methacrylate tank incident, analyzing the underlying reactions and implications for industrial safety.

hackernews · nooks · May 26, 19:25

**标签**: `#Chemical Engineering`, `#Industrial Safety`, `#Chemistry`, `#Incident Analysis`, `#Systems Engineering`

---

<a id="item-4"></a>
## [The pressure](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 8.0/10

curl 项目负责人 Daniel Stenberg 报告称，由于 AI 辅助的安全报告数量激增 4-5 倍，项目团队正面临前所未有的巨大压力，严重影响了工作与生活平衡。

rss · Simon Willison · May 26, 23:48

**标签**: `#开源`, `#安全`, `#AI影响`, `#维护者倦怠`, `#软件工程`

---

<a id="item-5"></a>
## [🦘 美团发布跑腿 Skill，用户可用任意 AI 助手一句话下单](http://client.sina.com.cn/news/2026-05-26/doc-inhzffss1481138.shtml) ⭐️ 8.0/10

美团发布“跑腿 Skill”，将跑腿下单能力封装为标准接口并开源，使用户能通过任意 AI 助手一句话完成下单，无需打开 App。

telegram · zaihuapd · May 26, 08:29

**标签**: `#AI Assistants`, `#Platform Integration`, `#On-demand Services`, `#Open Source`, `#User Experience`

---

<a id="item-6"></a>
## [📱 中国审查 Meta 收购 Manus，两名联合创始人被限制离境  中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定。](https://t.me/zaihuapd/41577) ⭐️ 8.0/10

中国监管机构正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定，并已限制 Manus 的两名联合创始人离境。

telegram · zaihuapd · May 26, 09:56

**标签**: `#AI监管`, `#科技政策`, `#并购`, `#中国`, `#AI产业`

---

<a id="item-7"></a>
## [sgl-project/sglang released v0.5.12.post1](https://github.com/sgl-project/sglang/releases/tag/v0.5.12.post1) ⭐️ 7.0/10

SGLang 发布了 v0.5.12.post1 版本，这是一个稳定性补丁，主要为 DeepSeek V4 模型修复了 12 个关键错误，包括解决崩溃、乱码和恢复 GSM8K 准确率等问题。

github · Fridge003 · May 26, 23:58

**标签**: `#SGLang`, `#DeepSeek V4`, `#Bug Fixes`, `#LLM Inference`, `#Stability Patch`

---

<a id="item-8"></a>
## [A few interesting modern pixel fonts](https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/) ⭐️ 7.0/10

这篇文章精选了一系列现代像素字体，引发了高质量的社区讨论，深入探讨了历史背景、实用更新和额外推荐，对设计师和开发者具有参考价值。

hackernews · zdw · May 25, 20:41

**标签**: `#Pixel Fonts`, `#Typography`, `#UI/UX Design`, `#Retro Computing`, `#Design`

---

<a id="item-9"></a>
## [Quoting Paul Graham](https://simonwillison.net/2026/May/26/paul-graham/#atom-everything) ⭐️ 7.0/10

Paul Graham expresses strong disapproval of AI-written emails from startup founders, stating he finds them inauthentic and dismisses the sender.

rss · Simon Willison · May 26, 15:02

**标签**: `#AI`, `#Professional Communication`, `#Authenticity`, `#Startup`, `#Ethics`

---