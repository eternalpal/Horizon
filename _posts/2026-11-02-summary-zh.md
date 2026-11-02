---
layout: default
title: "Horizon Summary: 2026-11-02 (ZH)"
date: 2026-11-02
lang: zh
---

> From 25 items, 16 important content pieces were selected

---

1. [ChatGPT 账户接管漏洞：沙盒逃逸攻击链](#item-1) ⭐️ 9.0/10
2. [长鑫第六代 DRAM 平台完成工程样片验证](#item-2) ⭐️ 9.0/10
3. [LongCat-2.5 发布：1.6 万亿参数原生多模态模型](#item-3) ⭐️ 9.0/10
4. [Show HN: HackerBooks – HackerTube, but for books mentioned on HN](#item-4) ⭐️ 8.0/10
5. [HackerTube: YouTube built from videos recommended by HN](#item-5) ⭐️ 8.0/10
6. [Ask HN: Which TV do you recommend for privacy?](#item-6) ⭐️ 8.0/10
7. [Quoting Kyle Kingsbury](#item-7) ⭐️ 8.0/10
8. [🤖 DeepSeek Harness 团队提出 Super-agent 架构](#item-8) ⭐️ 8.0/10
9. [中国人形机器人占全球出货量 97%，上半年遥遥领先  2026 年上半年，中国人形机器人制造商占据全球出货量的 97% 以上。](#item-9) ⭐️ 8.0/10
10. [菲尔兹奖得主邓煜批评 AI 公司：你不能在蒸馏全人类知识的时候才支持蒸馏行为  菲尔兹奖得主、芝加哥大学教授邓煜在“知识分子”“赛先生”论坛演讲称，AI 能凭无](#item-10) ⭐️ 8.0/10
11. [AI“分词器税”可使部分语言使用成本最高相差 17 倍](#item-11) ⭐️ 8.0/10
12. [If in doubt, delete the uv.lock file](#item-12) ⭐️ 7.0/10
13. [德国执政联盟讨论开征人工智能税](#item-13) ⭐️ 7.0/10
14. [🤖 ChatGPT 与 Codex 用量额度将共享，将以词元（token）为单位进行计量  OpenAI 在连续 28 天更新的第 27 天更新：自 12 月起](#item-14) ⭐️ 7.0/10
15. [🤖 匿名仓库声称泄漏 Anthropic 模型，真实性存疑](#item-15) ⭐️ 7.0/10
16. [🍏 苹果触屏 MacBook Pro 据称起价 2899 美元  苹果计划于 10 月 28 日发布 14 英寸和 16 英寸触屏 MacBook Pro。](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [ChatGPT 账户接管漏洞：沙盒逃逸攻击链](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 9.0/10

Parameter Labs 在 ChatGPT 的 HTML 预览功能中发现了一个关键的沙盒逃逸漏洞，攻击者可以利用该漏洞注入任意 HTML 并执行 JavaScript，最终可能导致用户账户被接管。这一复杂的漏洞利用了 MathLive JavaScript 库的 postMessage() 漏洞和 YouTube oEmbed 反射机制来绕过内容安全策略（CSP）。 这个漏洞非常严重，因为它可能允许攻击者窃取用户私人数据或代表已登录用户执行操作，从而损害 ChatGPT 这一广泛使用的 AI 平台的安全性与可信度。它强调了在处理敏感用户信息的 Web 应用程序中，强大的沙盒机制和彻底的安全审计至关重要。 攻击链利用了 MathLive 库的虚拟键盘，该键盘可以通过沙盒 iframe 发送 postMessage() 消息，利用 innerHTML 将 HTML 注入到父页面中。这使得攻击者能够注入一个新的、不受沙盒限制的 iframe，并通过 YouTube oEmbed 端点反射 JavaScript 来绕过 OpenAI 的 CSP，最终实现代码执行。

rss · Simon Willison · Oct 31, 23:15

**背景**: 沙盒是一种安全机制，通过创建受限的执行环境来隔离程序，以防止恶意代码损害系统。沙盒逃逸漏洞是指攻击者绕过这些限制，在受控环境之外执行恶意操作。postMessage() API 是一种 Web 标准，允许在不同的 Window 对象之间（例如主页面和嵌入的 iframe）安全地进行通信，即使它们来自不同的源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mathlive.io/sdk/">MathLive SDKs · MathLive</a></li>
<li><a href="https://blog.csdn.net/m0_73113764/article/details/132089103">沙箱逃逸：原理、手段与绕过策略,-CSDN博客 好消息！iOS 27.0 发现新漏洞，疑似能实现读写 - 今日头条 沙盒逃逸_百度百科 CVE-2025-2783沙箱逃逸漏洞分析与利用-CSDN博客 沙箱逃逸_百度百科</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage">Window: postMessage() method - Web APIs | MDN</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#安全`, `#漏洞`, `#沙盒逃逸`, `#AI安全`

---

<a id="item-2"></a>
## [长鑫第六代 DRAM 平台完成工程样片验证](https://finance.sina.com.cn/roll/2026-10-31/doc-inixcsqk4704411.shtml) ⭐️ 9.0/10

长鑫科技宣布其基于 4F²垂直沟道架构的第六代 DRAM 平台已完成工程样片验证，并计划年底推出面向服务器的 DDR5 RDIMM，成为首家完成该关键技术验证的公司。

telegram · zaihuapd · Oct 31, 14:26

**标签**: `#DRAM`, `#半导体`, `#存储技术`, `#硬件`, `#技术突破`

---

<a id="item-3"></a>
## [LongCat-2.5 发布：1.6 万亿参数原生多模态模型](https://longcat.ai/blog/longcat-2.5/) ⭐️ 9.0/10

LongCat-2.5 是一款新发布的 1.6 万亿参数原生多模态模型，专为长程 agent 任务设计，强化了视觉理解和 agentic 编码能力，支持视觉编程。

telegram · zaihuapd · Nov 2, 03:08

**标签**: `#AI/ML`, `#多模态AI`, `#大型语言模型`, `#AI Agent`, `#视觉编程`

---

<a id="item-4"></a>
## [Show HN: HackerBooks – HackerTube, but for books mentioned on HN](https://hackerbooks.org/) ⭐️ 8.0/10

HackerBooks 是一个新网站，索引了自 2007 年以来在 Hacker News 上被提及的超过 16,000 本书籍，该网站几乎完全由 AI 模型（Claude）构建，并提供了指向原始评论的链接。

hackernews · roansh · Nov 1, 15:58

**标签**: `#AI开发`, `#社区工具`, `#数据聚合`, `#LLM应用`, `#软件工程`

---

<a id="item-5"></a>
## [HackerTube: YouTube built from videos recommended by HN](https://karpathy.bearblog.dev/hacker-tube/) ⭐️ 8.0/10

HackerTube 是一个由 Karpathy 创建的 YouTube 风格的网站，它聚合了自 2007 年以来在 Hacker News 评论中推荐的 6,454 个视频，提供了一个人工策划的内容发现平台。

hackernews · karpathy · Oct 31, 19:56

**标签**: `#内容策展`, `#视频发现`, `#社区驱动`, `#Web应用`, `#AI时代内容`

---

<a id="item-6"></a>
## [Ask HN: Which TV do you recommend for privacy?](https://news.ycombinator.com/item?id=50328896) ⭐️ 8.0/10

一位用户寻求保护隐私的电视推荐，引发了社区热烈讨论，提供了各种技术和实用方法来应对智能电视的数据收集问题。

hackernews · LecroJS · Nov 1, 19:35

**标签**: `#数字隐私`, `#智能电视`, `#消费电子`, `#硬件改造`, `#社区讨论`

---

<a id="item-7"></a>
## [Quoting Kyle Kingsbury](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 8.0/10

Kyle Kingsbury 警告说，LLM 的广泛使用可能会侵蚀人们对软件和文档的信任，使维护者难以证明其质量，并使用户难以识别成熟的系统。

rss · Simon Willison · Nov 1, 16:49

**标签**: `#LLMs`, `#软件信任`, `#文档`, `#软件质量`, `#AI影响`

---

<a id="item-8"></a>
## [🤖 DeepSeek Harness 团队提出 Super-agent 架构](https://mp.weixin.qq.com/s/zoS7GlReWPhfCjENGxXCdg) ⭐️ 8.0/10

DeepSeek Harness 团队提出了一种 Super-agent 架构，通过常驻 Router 层和多个上下文隔离的 Worker 并发执行任务，旨在解决 AI 代理的单会话阻塞和多任务上下文混乱问题。

telegram · zaihuapd · Oct 31, 13:05

**标签**: `#AI Agents`, `#System Architecture`, `#Concurrency`, `#DeepSeek`, `#AI/ML`

---

<a id="item-9"></a>
## [中国人形机器人占全球出货量 97%，上半年遥遥领先  2026 年上半年，中国人形机器人制造商占据全球出货量的 97% 以上。](https://t.me/zaihuapd/44832) ⭐️ 8.0/10

2026 年上半年，中国制造商占据了全球人形机器人出货量的 97%以上，其中上海智元和杭州宇树科技领先，远超美国公司，预示着该市场将快速增长。

telegram · zaihuapd · Oct 31, 16:40

**标签**: `#人形机器人`, `#市场份额`, `#中国科技`, `#机器人产业`, `#AI应用`

---

<a id="item-10"></a>
## [菲尔兹奖得主邓煜批评 AI 公司：你不能在蒸馏全人类知识的时候才支持蒸馏行为  菲尔兹奖得主、芝加哥大学教授邓煜在“知识分子”“赛先生”论坛演讲称，AI 能凭无](https://t.me/zaihuapd/44834) ⭐️ 8.0/10

菲尔兹奖得主邓煜批评 AI 公司在利用全人类知识进行训练的同时，拒绝提供思维链，并发布未经验证、缺乏归属的 AI 生成研究成果，呼吁关注 AI 伦理和学术诚信。

telegram · zaihuapd · Nov 1, 02:54

**标签**: `#AI伦理`, `#数据治理`, `#学术诚信`, `#负责任AI`, `#AI与科学`

---

<a id="item-11"></a>
## [AI“分词器税”可使部分语言使用成本最高相差 17 倍](https://clear-languages.org/blog/the-tokenizer-tax) ⭐️ 8.0/10

CLEAR 研究联盟的报告指出，主流 AI 模型的分词器对英语优化明显，导致非英语语言处理相同内容时消耗的 Token 量最高可达英语的 17 倍，从而增加了成本并降低了效率。

telegram · zaihuapd · Nov 1, 16:06

**标签**: `#AI伦理`, `#多语言NLP`, `#分词`, `#语言偏见`, `#AI成本`

---

<a id="item-12"></a>
## [If in doubt, delete the uv.lock file](https://simonwillison.net/2026/Nov/1/delete-uv-lock-first/) ⭐️ 7.0/10

Simon Willison 建议，当升级到 Python 3.15 后使用 uv 工具遇到依赖错误时，应删除 uv.lock 文件，因为该文件可能将依赖项锁定到与新 Python 版本不兼容的版本。

rss · Simon Willison · Nov 1, 23:24

**标签**: `#Python`, `#依赖管理`, `#uv`, `#故障排除`, `#软件工程`

---

<a id="item-13"></a>
## [德国执政联盟讨论开征人工智能税](https://www.tagesschau.de/inland/ministerin-prien-ki-steuer-100.html) ⭐️ 7.0/10

德国执政联盟正在讨论对人工智能创造的收入征税，但各方对实施时机和必要性存在不同意见。

telegram · zaihuapd · Nov 1, 03:55

**标签**: `#AI政策`, `#税收`, `#德国`, `#AI伦理`, `#监管`

---

<a id="item-14"></a>
## [🤖 ChatGPT 与 Codex 用量额度将共享，将以词元（token）为单位进行计量  OpenAI 在连续 28 天更新的第 27 天更新：自 12 月起](https://t.me/zaihuapd/44839) ⭐️ 7.0/10

OpenAI 宣布自 12 月起，ChatGPT 和 Codex 的用量额度将在其付费计划中共享并以词元计量，同时 Work 的智能体能力将并入 ChatGPT 主体验。

telegram · zaihuapd · Nov 1, 09:41

**标签**: `#OpenAI`, `#ChatGPT`, `#AI服务`, `#产品整合`, `#计费`

---

<a id="item-15"></a>
## [🤖 匿名仓库声称泄漏 Anthropic 模型，真实性存疑](https://huggingface.co/burner22/numbat) ⭐️ 7.0/10

一个匿名 Hugging Face 仓库声称泄漏了 Anthropic 内部模型“numbat”的预训练检查点，参数约 14 万亿，但其真实性尚未得到验证且受到社区的普遍质疑。

telegram · zaihuapd · Nov 1, 16:38

**标签**: `#AI模型`, `#LLM`, `#Anthropic`, `#模型泄漏`, `#数据验证`

---

<a id="item-16"></a>
## [🍏 苹果触屏 MacBook Pro 据称起价 2899 美元  苹果计划于 10 月 28 日发布 14 英寸和 16 英寸触屏 MacBook Pro。](https://t.me/zaihuapd/44844) ⭐️ 7.0/10

据传苹果计划于 10 月底发布 14 英寸和 16 英寸触屏 MacBook Pro，配备 OLED XDR 显示屏和灵动岛，14 英寸 M5 Pro 机型起价预计为 2899 美元。

telegram · zaihuapd · Nov 2, 00:58

**标签**: `#Apple`, `#MacBook Pro`, `#产品发布`, `#硬件`, `#消费电子`

---