---
layout: default
title: "Horizon Summary: 2026-04-29 (ZH)"
date: 2026-04-29
lang: zh
---

> From 30 items, 11 important content pieces were selected

---

1. [Ghostty is leaving GitHub](#item-1) ⭐️ 9.0/10
2. [GitHub RCE Vulnerability: CVE-2026-3854 Breakdown](#item-2) ⭐️ 9.0/10
3. [消息称谷歌与美国国防部签署协议，旗下 AI 可用于军方机密工作](#item-3) ⭐️ 9.0/10
4. [LiteLLM 存在 SQL 注入漏洞，无需凭证即可读取 API 密钥](#item-4) ⭐️ 9.0/10
5. [vllm-project/vllm released v0.20.0](#item-5) ⭐️ 8.0/10
6. [Tracking the history of the now-deceased OpenAI Microsoft AGI clause](#item-6) ⭐️ 8.0/10
7. [🤖 Qwen 开源高性能线性注意力内核库 FlashQLA，速度提升 2–3 倍](#item-7) ⭐️ 8.0/10
8. [Before GitHub](#item-8) ⭐️ 7.0/10
9. [Quoting OpenAI Codex base_instructions](#item-9) ⭐️ 7.0/10
10. [Speech translation in Google Meet is now rolling out to mobile devices](#item-10) ⭐️ 7.0/10
11. [🤖 DeepSeek API 价格调整：缓存命中降至 1 折且 V4-Pro 限时优惠  DeepSeek 调整 API 模型定价，全系列模型输入缓存命中的价格](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Ghostty is leaving GitHub](https://mitchellh.com/writing/ghostty-leaving-github) ⭐️ 9.0/10

Mitchell Hashimoto, founder of HashiCorp, announced that his project Ghostty is leaving GitHub due to his deep disappointment with the platform's perceived decline and shift in priorities, sparking extensive community discussion about GitHub's future and the open-source ecosystem.

hackernews · WadeGrimridge · Apr 28, 19:44

**标签**: `#Open Source`, `#GitHub`, `#Developer Tools`, `#Community`, `#Platform Shift`

---

<a id="item-2"></a>
## [GitHub RCE Vulnerability: CVE-2026-3854 Breakdown](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854) ⭐️ 9.0/10

Wiz.io detailed a critical Remote Code Execution (RCE) vulnerability (CVE-2026-3854) in GitHub Enterprise Server, exploitable via unsanitized git push options in the X-Stat header, urging immediate upgrades for the 88% of vulnerable instances.

hackernews · bo0tzz · Apr 28, 16:15

**标签**: `#Cybersecurity`, `#Vulnerability`, `#GitHub`, `#RCE`, `#AI/ML`

---

<a id="item-3"></a>
## [消息称谷歌与美国国防部签署协议，旗下 AI 可用于军方机密工作](https://www.theinformation.com/articles/google-signs-classified-ai-deal-pentagon-amid-employee-opposition) ⭐️ 9.0/10

消息称谷歌已与美国国防部签署协议，将其人工智能模型用于包括任务规划和武器目标定位在内的机密军事工作，同时其他主要 AI 公司也参与其中。

telegram · zaihuapd · Apr 28, 11:47

**标签**: `#AI伦理`, `#国防科技`, `#谷歌AI`, `#政府合同`, `#军事AI`

---

<a id="item-4"></a>
## [LiteLLM 存在 SQL 注入漏洞，无需凭证即可读取 API 密钥](https://mp.weixin.qq.com/s/ytNWdqGECo0fmWwPQGqy8A) ⭐️ 9.0/10

LiteLLM 的 Proxy 组件被发现存在一个 SQL 注入漏洞（CVE-2026-42208），攻击者无需凭证即可通过构造 Bearer token 在错误日志中注入 payload，从而未授权读取数据库中存储的各大模型 API 密钥，官方已在 v1.83.7-stable 中修复。

telegram · zaihuapd · Apr 28, 14:44

**标签**: `#LiteLLM`, `#SQL注入`, `#API安全`, `#漏洞`, `#LLM`

---

<a id="item-5"></a>
## [vllm-project/vllm released v0.20.0](https://github.com/vllm-project/vllm/releases/tag/v0.20.0) ⭐️ 8.0/10

vLLM v0.20.0 版本发布，主要亮点包括支持 DeepSeek V4 模型、默认 CUDA 升级至 13.0、PyTorch 升级至 2.11 以及支持 Python 3.14，显著提升了 LLM 推理能力和兼容性。

github · khluu · Apr 27, 21:20

**标签**: `#LLM Inference`, `#vLLM`, `#DeepSeek V4`, `#CUDA`, `#PyTorch`

---

<a id="item-6"></a>
## [Tracking the history of the now-deceased OpenAI Microsoft AGI clause](https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/#atom-everything) ⭐️ 8.0/10

Simon Willison investigates the history and recent disappearance of a key clause in the Microsoft-OpenAI partnership agreement that would have revoked Microsoft's commercial IP rights if OpenAI achieved AGI.

rss · Simon Willison · Apr 27, 18:38

**标签**: `#OpenAI`, `#Microsoft`, `#AGI`, `#Business Strategy`, `#AI Policy`

---

<a id="item-7"></a>
## [🤖 Qwen 开源高性能线性注意力内核库 FlashQLA，速度提升 2–3 倍](https://qwen.ai/blog?id=flashqla) ⭐️ 8.0/10

Qwen 团队开源了 FlashQLA，一个基于 TileLang 构建的线性注意力内核库，通过算子融合和代数优化，在 NVIDIA Hopper 上为 Gated Delta Network 实现了 2-3 倍的速度提升，特别适用于 LLM 预训练和端侧智能体推理。

telegram · zaihuapd · Apr 28, 14:11

**标签**: `#AI/ML`, `#深度学习`, `#性能优化`, `#注意力机制`, `#GPU计算`

---

<a id="item-8"></a>
## [Before GitHub](https://lucumr.pocoo.org/2026/4/28/before-github/) ⭐️ 7.0/10

这篇文章探讨了 GitHub 出现之前的软件开发格局，引发了社区关于 GitHub 对开发者工作流程的影响、平台中心化的利弊以及与替代版本控制系统比较的讨论。

hackernews · mlex · Apr 28, 21:17

**标签**: `#软件工程`, `#版本控制`, `#GitHub`, `#开发者工具`, `#平台中心化`

---

<a id="item-9"></a>
## [Quoting OpenAI Codex base_instructions](https://simonwillison.net/2026/Apr/28/openai-codex/#atom-everything) ⭐️ 7.0/10

该内容引用了 OpenAI Codex（用于 GPT-5.5）的一条基础指令，禁止模型在非绝对相关的情况下提及某些动物或生物。

rss · Simon Willison · Apr 28, 22:02

**标签**: `#LLMs`, `#Prompt Engineering`, `#AI Safety`, `#OpenAI`, `#System Prompts`

---

<a id="item-10"></a>
## [Speech translation in Google Meet is now rolling out to mobile devices](https://simonwillison.net/2026/Apr/27/speech-translation-in-google-meet-is-now-rolling-out-to-mobile-d/#atom-everything) ⭐️ 7.0/10

Google Meet is rolling out an alpha version of real-time speech translation to mobile devices, enabling translation between several languages with voice imitation, though it's still buggy.

rss · Simon Willison · Apr 27, 17:37

**标签**: `#AI`, `#Machine Translation`, `#Google Meet`, `#Mobile Apps`, `#Speech Technology`

---

<a id="item-11"></a>
## [🤖 DeepSeek API 价格调整：缓存命中降至 1 折且 V4-Pro 限时优惠  DeepSeek 调整 API 模型定价，全系列模型输入缓存命中的价格](https://t.me/zaihuapd/41103) ⭐️ 7.0/10

DeepSeek 大幅调整了其 API 模型定价，将所有模型的输入缓存命中价格降至原价的 1/10，并提供 V4-Pro 限时优惠。

telegram · zaihuapd · Apr 28, 04:31

**标签**: `#AI API`, `#定价`, `#DeepSeek`, `#LLM`, `#开发者工具`

---