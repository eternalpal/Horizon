---
layout: default
title: "Horizon Summary: 2026-10-31 (ZH)"
date: 2026-10-31
lang: zh
---

> From 29 items, 15 important content pieces were selected

---

1. [Cursor Marketplace 上的 Claude Code VS Code 扩展被植入后门](#item-1) ⭐️ 9.0/10
2. [Northflank Breached](#item-2) ⭐️ 9.0/10
3. [The $6.3B Binance hack was pulled off in just 20 minutes](#item-3) ⭐️ 9.0/10
4. [Show HN: A working Nintendo in ~1GB of Qwen weights](#item-4) ⭐️ 9.0/10
5. [dbreunig/nesformer](#item-5) ⭐️ 9.0/10
6. [Building a multiplayer game world with autonomous Fable-class models](#item-6) ⭐️ 9.0/10
7. [🤖 Anthropic 成为 🚀 SpaceX 最大单一客户，每月贡献三分之一的营收](#item-7) ⭐️ 9.0/10
8. [Cursor 扩展市场 OpenVSX 中 Claude Code 插件被投毒](#item-8) ⭐️ 9.0/10
9. [🅰️ 苹果下调中国区 App Store 佣金比例，标准费率降至 25%  苹果公司宣布自 2026 年 3 月 15 日起，调整中国大陆地区 iOS 及 iP](#item-9) ⭐️ 9.0/10
10. [My favourite PowerMac is a Nintendo Wii](#item-10) ⭐️ 8.0/10
11. [美通信委员会或禁止中国的电信公司接入美国网络  美国联邦通信委员会（FCC）表示，可能禁止三家中国主要电信公司接入美国网络，原因是上述公司有屏蔽骚扰电话的行为。](#item-11) ⭐️ 8.0/10
12. [美国员工敬业度降至 29%，15 年来最低，远程办公降幅最大，AI 引入组织尤甚](#item-12) ⭐️ 7.0/10
13. [🤖 ChatGPT 新增 CarPlay 支持，车内可直接语音提问  OpenAI 已为 ChatGPT 应用加入 CarPlay 支持，用户可直接在车辆仪表盘](#item-13) ⭐️ 7.0/10
14. [♻️ RTX 5090 “停售”风波，80 系显卡将卖 90 价  RTX 5090“停售”风波中，官方口径与零售现实明显背离。](#item-14) ⭐️ 7.0/10
15. [🍏 iOS 27.2 Beta 2 疑似新增传感器相关权限选项  iOS27.2 beta 2 疑似新增中国大陆地区特供的屏蔽方向传感器权限，被加入列表后的 A](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cursor Marketplace 上的 Claude Code VS Code 扩展被植入后门](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 9.0/10

恶意行为者在 Cursor Marketplace 上发布了篡改版的 Claude Code VS Code 扩展，该版本将攻击者的 SSH 公钥（标记为 "svc-telemetry"）添加到用户的 authorized_keys 文件中。此次攻击在周四太平洋时间上午 2:27 至下午 1:35 期间活跃。 此次事件是一次关键的供应链安全漏洞，因为它直接针对开发者工具，可能导致攻击者通过被泄露的 SSH 密钥未经授权地访问开发者的系统。此类攻击会侵蚀人们对软件分发渠道的信任，并凸显了开发环境中第三方扩展日益增长的风险。 Anthropic 证实其官方渠道和系统未受影响，并且受影响的 Claude Code 扩展并非由他们构建或发布，仅影响 Cursor Marketplace 的用户。用户可以通过在 macOS/Linux 上搜索其 ~/.ssh/authorized_keys 文件中的 "svc-telemetry" 来检查是否受到影响。

hackernews · _chall · Oct 30, 07:09

**背景**: VS Code 扩展是一种软件包，用于为 Visual Studio Code 编辑器添加新功能或集成外部服务，被开发者广泛使用。Cursor Marketplace 是一个平台，用户可以在其中发现和安装专为 Cursor 编辑器（一种 AI 原生代码编辑器）设计的插件和扩展。authorized_keys 文件是 SSH（Secure Shell）的关键组成部分，它存储公钥，允许用户在客户端持有相应私钥的情况下无需密码即可向服务器进行身份验证。在这种情况下，供应链攻击是指恶意行为者篡改软件组件或分发渠道以损害最终用户，利用用户对合法软件来源的信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/docs/plugins">Browse, install, and manage plugins from the Cursor Marketplace .</a></li>
<li><a href="https://www.ssh.com/academy/ssh/authorized-keys-file">What is the Authorized Keys File in SSH ?</a></li>
<li><a href="https://attack.mitre.org/techniques/T1195/">Supply Chain Compromise, Technique T1195 - Enterprise | MITRE ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论中包含了 Anthropic 的官方澄清，指出他们的系统未受影响，并且他们没有构建或发布受影响的扩展，该事件仅影响 Cursor 用户。用户分享了即时可行的缓解步骤，详细说明了如何在其 authorized_keys 文件中检查恶意 "svc-telemetry" 密钥。关于该扩展的来源和受影响范围最初存在一些困惑，一些用户强调了原始 Phorion 报告对技术细节的重要性。

**标签**: `#Software Security`, `#Supply Chain Attack`, `#VS Code Extension`, `#Developer Tools`, `#Cybersecurity`

---

<a id="item-2"></a>
## [Northflank Breached](https://status.northflank.com/) ⭐️ 9.0/10

Northflank experienced a security breach, which community discussions frame as part of a broader, rapidly escalating 'infosec emergency' impacting multiple modern multi-tenant SaaS providers, prompting concerns about cloud security, market consolidation, and future security paradigms.

hackernews · js4ever · Oct 30, 15:10

**标签**: `#Cloud Security`, `#SaaS Security`, `#Cybersecurity Incident`, `#Infrastructure`, `#DevOps`

---

<a id="item-3"></a>
## [The $6.3B Binance hack was pulled off in just 20 minutes](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/) ⭐️ 9.0/10

A $6.3 billion hack on the cryptocurrency exchange Binance was executed in just 20 minutes, sparking widespread concerns about security, regulation, and the sophisticated nature of cyberattacks.

hackernews · domhudson · Oct 30, 12:50

**标签**: `#Cybersecurity`, `#Cryptocurrency`, `#Blockchain Security`, `#Financial Crime`

---

<a id="item-4"></a>
## [Show HN: A working Nintendo in ~1GB of Qwen weights](https://github.com/dbreunig/nesformer) ⭐️ 9.0/10

一位开发者成功地使用大约 1GB 的 Qwen LLM 权重模拟了任天堂娱乐系统，展示了 AI 在硬件模拟方面的新颖应用。

hackernews · dbreunig · Oct 30, 16:40

**标签**: `#AI/ML`, `#LLMs`, `#系统模拟`, `#新型AI应用`, `#计算范式`

---

<a id="item-5"></a>
## [dbreunig/nesformer](https://simonwillison.net/2026/Oct/30/nesformer/) ⭐️ 9.0/10

Drew Breunig 成功地将一个可工作的任天堂娱乐系统 6502 CPU 模拟器嵌入到 Qwen3.5-4B 模型的权重中，使得 NES ROMs 可以在 LLM 内部运行（尽管速度很慢）。

rss · Simon Willison · Oct 30, 21:59

**标签**: `#AI/ML`, `#LLM应用`, `#仿真`, `#计算范式`, `#突破性研究`

---

<a id="item-6"></a>
## [Building a multiplayer game world with autonomous Fable-class models](https://simonwillison.net/2026/Oct/29/how-i-built-the-most-ai-pilled-company-in-the-world/) ⭐️ 9.0/10

文章介绍了 Spawn，一个利用智能体工程和前沿 AI 模型构建的大型多人游戏，玩家可以通过提示词动态修改游戏世界，展示了交互式娱乐的新范式。

rss · Simon Willison · Oct 29, 17:00

**标签**: `#AI游戏`, `#智能体AI`, `#前沿模型`, `#游戏开发`, `#交互式AI`

---

<a id="item-7"></a>
## [🤖 Anthropic 成为 🚀 SpaceX 最大单一客户，每月贡献三分之一的营收](https://www.cls.cn/detail/2519914) ⭐️ 9.0/10

据报道，Anthropic 已成为 SpaceX 最大的单一客户，承诺在合同期内支付高达 1205 亿美元以获取其“超级智能”部门的算力服务，每月为 SpaceX 贡献约三分之一的营收。

telegram · zaihuapd · Oct 30, 06:20

**标签**: `#AI基础设施`, `#算力服务`, `#AI经济`, `#Anthropic`, `#SpaceX`

---

<a id="item-8"></a>
## [Cursor 扩展市场 OpenVSX 中 Claude Code 插件被投毒](https://cursor.com/blog/claude-code-extension-security-notice) ⭐️ 9.0/10

Cursor 的 OpenVSX 扩展市场中发现了一个恶意版本的 Claude Code VS Code 扩展，该扩展试图收集用户数据并植入 SSH 后门，导致市场暂时关闭并影响了多达 5000 名用户。

telegram · zaihuapd · Oct 30, 08:44

**标签**: `#软件安全`, `#供应链攻击`, `#VS Code`, `#AI 工具`, `#网络安全`

---

<a id="item-9"></a>
## [🅰️ 苹果下调中国区 App Store 佣金比例，标准费率降至 25%  苹果公司宣布自 2026 年 3 月 15 日起，调整中国大陆地区 iOS 及 iP](https://t.me/zaihuapd/44806) ⭐️ 9.0/10

苹果公司宣布自 2026 年 3 月 15 日起，将中国大陆地区 App Store 的标准佣金比例从 30%下调至 25%，并针对小型企业计划等特定交易将佣金率从 15%下调至 12%。

telegram · zaihuapd · Oct 30, 09:25

**标签**: `#App Store`, `#Apple`, `#开发者经济`, `#中国市场`, `#监管政策`

---

<a id="item-10"></a>
## [My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/) ⭐️ 8.0/10

一篇文章详细介绍了在任天堂 Wii 上运行经典 Mac OS 的技术项目，突出了该游戏机作为复古 PowerMac 的意外能力。

hackernews · DHowett · Oct 30, 17:25

**标签**: `#Retro-computing`, `#Hardware Hacking`, `#Emulation`, `#Mac OS`, `#Nintendo Wii`

---

<a id="item-11"></a>
## [美通信委员会或禁止中国的电信公司接入美国网络  美国联邦通信委员会（FCC）表示，可能禁止三家中国主要电信公司接入美国网络，原因是上述公司有屏蔽骚扰电话的行为。](https://t.me/zaihuapd/44804) ⭐️ 8.0/10

美国联邦通信委员会（FCC）表示，可能禁止中国移动、中国电信和中国联通三家中国主要电信公司接入美国网络，原因是这些公司在 FCC 骚扰电话缓解数据库中存在认证问题。

telegram · zaihuapd · Oct 30, 08:01

**标签**: `#电信`, `#监管`, `#地缘政治`, `#中美关系`, `#FCC`

---

<a id="item-12"></a>
## [美国员工敬业度降至 29%，15 年来最低，远程办公降幅最大，AI 引入组织尤甚](https://www.gallup.com/workplace/716117/employee-engagement-below-30-first-time-years.aspx) ⭐️ 7.0/10

盖洛普调查显示，美国员工敬业度降至 15 年来的最低点 29%，其中远程办公员工和已引入 AI 的组织降幅最大。

telegram · zaihuapd · Oct 30, 06:45

**标签**: `#AI影响`, `#员工敬业度`, `#远程工作`, `#组织管理`, `#工作场所趋势`

---

<a id="item-13"></a>
## [🤖 ChatGPT 新增 CarPlay 支持，车内可直接语音提问  OpenAI 已为 ChatGPT 应用加入 CarPlay 支持，用户可直接在车辆仪表盘](https://t.me/zaihuapd/44803) ⭐️ 7.0/10

OpenAI 已为 ChatGPT 应用新增 CarPlay 支持，允许用户通过语音在车辆仪表盘上直接与 ChatGPT 交互。

telegram · zaihuapd · Oct 30, 07:25

**标签**: `#AI应用`, `#CarPlay`, `#用户体验`, `#OpenAI`, `#语音助手`

---

<a id="item-14"></a>
## [♻️ RTX 5090 “停售”风波，80 系显卡将卖 90 价  RTX 5090“停售”风波中，官方口径与零售现实明显背离。](https://t.me/zaihuapd/44813) ⭐️ 7.0/10

一份报告详细阐述了英伟达可能停产 RTX 5090 以优先发展利润更高的专业 GPU 的传闻，这可能导致消费级显卡价格大幅上涨，尽管官方对此予以否认。

telegram · zaihuapd · Oct 30, 14:27

**标签**: `#GPU市场`, `#NVIDIA`, `#AI硬件`, `#半导体行业`, `#产品策略`

---

<a id="item-15"></a>
## [🍏 iOS 27.2 Beta 2 疑似新增传感器相关权限选项  iOS27.2 beta 2 疑似新增中国大陆地区特供的屏蔽方向传感器权限，被加入列表后的 A](https://t.me/zaihuapd/44814) ⭐️ 7.0/10

iOS 27.2 Beta 2 疑似新增一项中国大陆地区特供的隐私设置，允许用户限制应用访问加速度计、陀螺仪等运动传感器数据。

telegram · zaihuapd · Oct 30, 15:00

**标签**: `#iOS`, `#隐私`, `#传感器`, `#中国市场`, `#应用开发`

---