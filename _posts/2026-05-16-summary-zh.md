---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 32 items, 11 important content pieces were selected

---

1. [Project Zero 发现 Pixel 10 零点击漏洞链](#item-1) ⭐️ 9.0/10
2. [🍏 Calif 与 Mythos Preview 合作，在 5 天内完成首个公开的 Apple M5 macOS 内核内存破坏漏洞利用](#item-2) ⭐️ 9.0/10
3. [苹果与 OpenAI 联盟出现裂痕，OpenAI 考虑法律行动](#item-3) ⭐️ 9.0/10
4. [vllm-project/vllm released v0.21.0](#item-4) ⭐️ 8.0/10
5. [I believe there are entire companies right now under AI psychosis](#item-5) ⭐️ 8.0/10
6. [The Zulip Foundation](#item-6) ⭐️ 8.0/10
7. [Project Gutenberg – keeps getting better](#item-7) ⭐️ 7.0/10
8. [Quoting Mitchell Hashimoto](#item-8) ⭐️ 7.0/10
9. [datasette-ip-rate-limit 0.1a0](#item-9) ⭐️ 7.0/10
10. [开源项目分享：Anima——20 亿参数动漫风文生图模型](#item-10) ⭐️ 7.0/10
11. [索尼 Xperia AI 影像优化照片被批灾难现场](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Project Zero 发现 Pixel 10 零点击漏洞链](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

谷歌的 Project Zero 团队发现了一个针对 Pixel 10 的关键零点击漏洞链，凸显了现代移动安全中存在的严重漏洞，这可能与人工智能驱动的功能有关。该漏洞允许在无需用户任何交互的情况下进行远程攻击。 这一发现至关重要，因为零点击漏洞对用户隐私和安全构成最高威胁，允许攻击者在无需用户任何交互的情况下悄无声息地入侵设备。它还引发了对手机中新增的 AI 驱动功能可能如何扩大攻击面，从而为复杂的漏洞利用创造新途径的担忧。 该漏洞链因其零点击特性（无需用户交互）而尤其令人担忧，并且可能与在用户交互前解码消息媒体的 AI 驱动功能有关，从而扩大了攻击面。值得注意的是，谷歌在发现漏洞后 90 天内迅速修补了这一 Android 驱动程序错误，这标志着供应商响应时间有所改善。

hackernews · happyhardcore · May 15, 13:39

**背景**: 零点击漏洞是一种高度危险的网络攻击，它允许攻击者在无需用户任何交互的情况下入侵设备，通常通过利用消息应用或其他服务处理传入数据的方式中的漏洞。谷歌 Project Zero 是一个由谷歌雇佣的精英安全研究团队，致力于发现和报告软件和硬件中的零日漏洞，以提升全球安全性。他们的工作通常要求供应商在 90 天内修补漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exploit_(computer_security)">Exploit (computer security) - Wikipedia</a></li>
<li><a href="https://www.kaspersky.com/resource-center/definitions/what-is-zero-click-malware">Zero-Click Exploits</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Project_Zero">Google Project Zero</a></li>

</ul>
</details>

**社区讨论**: 社区普遍担忧，AI 驱动的功能通过预处理消息，无意中扩大了移动设备上的零点击攻击面。尽管认可谷歌针对此特定漏洞在 90 天内改进的修补速度，但用户也表达了对其他 Android 设备安全状况以及 AI 对攻防安全能力更广泛影响的担忧。

**标签**: `#Mobile Security`, `#Zero-Click Exploit`, `#Vulnerability`, `#Android Security`, `#Project Zero`

---

<a id="item-2"></a>
## [🍏 Calif 与 Mythos Preview 合作，在 5 天内完成首个公开的 Apple M5 macOS 内核内存破坏漏洞利用](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Calif 联合 AI 系统 Mythos Preview，在五天内完成了首个公开的 Apple M5 macOS 内核内存破坏漏洞利用，成功绕过 MIE 硬件保护，实现了从非特权用户到 root shell 的提权。

telegram · zaihuapd · May 15, 02:15

**标签**: `#Apple Security`, `#Kernel Exploitation`, `#AI in Cybersecurity`, `#Vulnerability Research`, `#macOS Security`

---

<a id="item-3"></a>
## [苹果与 OpenAI 联盟出现裂痕，OpenAI 考虑法律行动](https://www.bloomberg.com/news/articles/2026-05-14/openai-apple-partnership-frays-setting-up-possible-legal-fight) ⭐️ 9.0/10

苹果与 OpenAI 的合作关系因推广、隐私和战略分歧而出现裂痕，OpenAI 正考虑采取法律行动，而苹果计划在 iOS 27 中向更多第三方 AI 模型开放 Siri。

telegram · zaihuapd · May 15, 12:59

**标签**: `#Apple`, `#OpenAI`, `#AI战略`, `#科技合作`, `#法律纠纷`

---

<a id="item-4"></a>
## [vllm-project/vllm released v0.21.0](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM v0.21.0 introduces major performance enhancements through KV Offload and Hybrid Memory Allocator integration, improved speculative decoding, a new Blackwell GPU backend, and important breaking changes like C++20 build requirement and Transformers v4 deprecation.

github · khluu · May 15, 08:44

**标签**: `#LLM Inference`, `#Performance Optimization`, `#Memory Management`, `#GPU Acceleration`, `#AI Infrastructure`

---

<a id="item-5"></a>
## [I believe there are entire companies right now under AI psychosis](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

Mitchell Hashimoto 的帖子引发了 Hacker News 上关于“AI 精神病”的高价值讨论，即公司过度依赖 AI 进行决策和开发，可能导致难以管理的复杂性和有缺陷的系统。

hackernews · reasonableklout · May 15, 20:26

**标签**: `#AI Adoption`, `#AI Ethics`, `#Software Engineering`, `#Organizational Strategy`, `#Hype Cycle`

---

<a id="item-6"></a>
## [The Zulip Foundation](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

流行的开源协作平台 Zulip 宣布将其公司捐赠给新成立的独立非营利 Zulip 基金会，同时核心团队成员将离职加入 Anthropic，旨在确保其长期公共利益使命。

hackernews · boramalper · May 15, 18:37

**标签**: `#Open Source`, `#Project Governance`, `#Non-profit`, `#Community`, `#Collaboration Tools`

---

<a id="item-7"></a>
## [Project Gutenberg – keeps getting better](https://www.gutenberg.org/) ⭐️ 7.0/10

Project Gutenberg, a long-standing digital library, is undergoing continuous improvements, prompting a community discussion that highlights its historical significance and profound impact on users.

hackernews · JSeiko · May 15, 16:15

**标签**: `#Digital Library`, `#Public Domain`, `#Web Development`, `#Community Engagement`, `#Internet History`

---

<a id="item-8"></a>
## [Quoting Mitchell Hashimoto](https://simonwillison.net/2026/May/14/mitchell-hashimoto/#atom-everything) ⭐️ 7.0/10

Mitchell Hashimoto suggests that programming languages are becoming increasingly fungible and less of a lock-in, exemplified by Bun's ability to switch between Zig and Rust relatively quickly.

rss · Simon Willison · May 14, 22:31

**标签**: `#programming languages`, `#software engineering`, `#language choice`, `#Bun`, `#Mitchell Hashimoto`

---

<a id="item-9"></a>
## [datasette-ip-rate-limit 0.1a0](https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/#atom-everything) ⭐️ 7.0/10

Simon Willison released `datasette-ip-rate-limit 0.1a0`, a configurable Datasette plugin built with AI assistance to block poorly-behaved crawlers by rate-limiting IPs.

rss · Simon Willison · May 14, 04:10

**标签**: `#Datasette`, `#Rate Limiting`, `#AI-assisted Development`, `#Web Security`, `#Python Plugin`

---

<a id="item-10"></a>
## [开源项目分享：Anima——20 亿参数动漫风文生图模型](https://civitai.com/models/2458426/anima) ⭐️ 7.0/10

Anima 是由 CircleStone Labs 和 Comfy Org 合作开发的 20 亿参数开源文生图模型，专注于动漫概念和风格，并能生成多种非写实艺术图像，目前仅供非商业使用。

telegram · zaihuapd · May 15, 03:00

**标签**: `#AI模型`, `#生成式AI`, `#文生图`, `#动漫艺术`, `#开源`

---

<a id="item-11"></a>
## [索尼 Xperia AI 影像优化照片被批灾难现场](https://x.com/sonyxperia/status/2054853108988047562) ⭐️ 7.0/10

索尼 Xperia 手机宣传其 AI 影像优化功能，却因实际照片效果不佳而遭到网友广泛批评，甚至被戏称为“最好的反 AI 广告”。

telegram · zaihuapd · May 15, 09:17

**标签**: `#AI应用`, `#移动摄影`, `#AI伦理`, `#用户体验`, `#产品质量`

---