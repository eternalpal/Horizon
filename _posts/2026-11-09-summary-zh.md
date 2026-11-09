---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> From 26 items, 17 important content pieces were selected

---

1. [KetchUp – Open-source SketchUp alternative built with Rust and WebGPU](#item-1) ⭐️ 9.0/10
2. [🍏 iOS 27.2 沙盒逃逸漏洞被公开（含 27.3 beta）](#item-2) ⭐️ 9.0/10
3. [剑桥团队 AI 辅助设计禽流感候选疫苗，动物试验显示广谱保护](#item-3) ⭐️ 9.0/10
4. [Outlook.com 悄然拒绝无 DMARC 记录的邮件](#item-4) ⭐️ 8.0/10
5. [Dux: Free, open-source Wayland desktop shell with file manager and theming](#item-5) ⭐️ 8.0/10
6. [NASA 计划 2028 年底发射 PROMISE 月球车](#item-6) ⭐️ 8.0/10
7. [🤖 Tibo 官宣 ChatGPT Pro 套餐额度翻倍，今日生效  OpenAI 在连续 28 天更新的第 25 天更新：从今天（2026 年 10 月 30](#item-7) ⭐️ 8.0/10
8. [姚顺雨：AI 公司护城河在产品层而非模型层](#item-8) ⭐️ 8.0/10
9. [👁️ 黄仁勋承认婚外情并致歉 英伟达董事会启动间谍指控独立调查](#item-9) ⭐️ 8.0/10
10. [🤖 Anthropic 报告：科学家主要用 Claude 做数据分析和写作](#item-10) ⭐️ 8.0/10
11. [📱 Win11 测试统一应用更新页，取代第三方弹窗](#item-11) ⭐️ 8.0/10
12. [报告：中国模型占全球开源模型企业支出 89%  Menlo Ventures 本周发布的报告称，中国模型占全球开源模型企业支出的 89%，其中月之暗面 Kimi](#item-12) ⭐️ 8.0/10
13. [Hide your slop PR descriptions behind <details><summary>](#item-13) ⭐️ 7.0/10
14. [parse_number() as a SQLite extension: C vs Rust](#item-14) ⭐️ 7.0/10
15. [datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages](#item-15) ⭐️ 7.0/10
16. [CPU-Z：32 GB 与 64 GB 内存占比同比下滑](#item-16) ⭐️ 7.0/10
17. [🤖 Siri AI 新增五门语言支持，年底扩至繁体中文  苹果随 27.2 系统更新将全新版 Siri AI 扩展至法语、日语、韩语、葡萄牙语和西班牙语，需配合](#item-17) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [KetchUp – Open-source SketchUp alternative built with Rust and WebGPU](https://ketchup3d.github.io/app/) ⭐️ 9.0/10

KetchUp is an open-source 3D modeling alternative to SketchUp, built with Rust and WebGPU, aiming to provide a free and modern solution to users frustrated with commercial software's licensing and direction.

hackernews · dcoulmbe · Nov 8, 22:35

**标签**: `#Open Source`, `#3D Modeling`, `#Rust`, `#WebGPU`, `#Design Tools`

---

<a id="item-2"></a>
## [🍏 iOS 27.2 沙盒逃逸漏洞被公开（含 27.3 beta）](https://x.com/forcequitOS/status/2119475139528020218?) ⭐️ 9.0/10

一个影响 iOS 26.0-27.3 beta 版本的零日沙盒逃逸漏洞（worse_query PoC）已被公开，允许访问系统路径和修改应用数据，且社区已迅速开发出基于此的工具。

telegram · zaihuapd · Nov 9, 02:36

**标签**: `#iOS安全`, `#零日漏洞`, `#沙盒逃逸`, `#移动安全`, `#系统研究`

---

<a id="item-3"></a>
## [剑桥团队 AI 辅助设计禽流感候选疫苗，动物试验显示广谱保护](https://www.cam.ac.uk/stories/ai-developed-vaccines-against-viruses) ⭐️ 9.0/10

剑桥大学团队利用 AI 辅助设计了一种新型禽流感候选疫苗，在小鼠和雪貂试验中显示出优于现有对照制剂的广谱保护效果，并计划推进人体临床试验。

telegram · zaihuapd · Nov 9, 03:00

**标签**: `#AI in Medicine`, `#Vaccine Development`, `#Avian Influenza`, `#Biomedical Research`, `#Pandemic Preparedness`

---

<a id="item-4"></a>
## [Outlook.com 悄然拒绝无 DMARC 记录的邮件](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) ⭐️ 8.0/10

据报道，Outlook.com 正在拒绝来自未配置 DMARC 记录的域的电子邮件，这标志着一个主要电子邮件提供商的重大政策转变。这一变化影响了发件人的邮件送达率，并引发了关于电子邮件安全实践的广泛讨论。 Outlook.com 的这项政策变化至关重要，因为它迫使电子邮件发件人采用 DMARC，通过打击欺骗和网络钓鱼来增强整个互联网的电子邮件安全性。它对尚未实施 DMARC 的组织造成了显著的邮件送达率影响，可能导致合法邮件被拒绝。 尽管最初报道为“悄然拒绝”，但社区讨论澄清 Outlook.com 正在对来自没有 DMARC 的域的电子邮件发送 5xx 永久传递失败。这表明是硬拒绝而非静默丢弃，这对于调试传递问题的邮件服务器管理员来说是一个关键区别。

hackernews · xmddmx · Nov 8, 19:20

**背景**: DMARC（基于域的消息认证、报告和一致性）是一种电子邮件认证协议，有助于保护域名免受电子邮件欺骗和网络钓鱼的侵害。它建立在 SPF（发件人策略框架）和 DKIM（域名密钥识别邮件）之上，允许域名所有者指定接收邮件服务器应如何处理未能通过这些认证检查的电子邮件。发布在域 DNS 中的 DMARC 记录会指示接收服务器是监控、隔离还是拒绝不符合域认证策略的电子邮件。该协议对于验证电子邮件发件人的合法性以及提高整体电子邮件安全性至关重要。

**社区讨论**: 社区讨论反映出复杂的情绪，一些用户强烈支持 Outlook.com 实施 DMARC，认为这是一项早就应该采取的必要安全措施。然而，其他管理员则对 Outlook.com 更广泛的电子邮件处理方式表示不满，提到了非公开黑名单和过去静默丢弃邮件等问题，同时澄清当前的 DMARC 拒绝是明确的 5xx 传递失败。

**标签**: `#Email Security`, `#DMARC`, `#Email Deliverability`, `#System Administration`, `#Microsoft Outlook`

---

<a id="item-5"></a>
## [Dux: Free, open-source Wayland desktop shell with file manager and theming](https://duxlabs.dev/) ⭐️ 8.0/10

Dux is a free, open-source Wayland desktop shell, formerly known as Dank Material Shell, praised by users for its slick design, integration with Niri, and recent support for atomic Linux distributions.

hackernews · indigodaddy · Nov 8, 19:08

**标签**: `#Wayland`, `#Desktop Environment`, `#Open Source`, `#Linux`, `#Software Development`

---

<a id="item-6"></a>
## [NASA 计划 2028 年底发射 PROMISE 月球车](https://www.scientificamerican.com/article/nasa-reveals-new-lunar-rover-promise-to-launch-to-moon-in-2028/) ⭐️ 8.0/10

NASA 计划于 2028 年底发射 PROMISE 月球车，前往月球南极勘察资源，为未来的月球基地和载人任务做准备。

telegram · zaihuapd · Nov 8, 08:32

**标签**: `#空间探索`, `#月球任务`, `#NASA`, `#机器人技术`, `#未来科技`

---

<a id="item-7"></a>
## [🤖 Tibo 官宣 ChatGPT Pro 套餐额度翻倍，今日生效  OpenAI 在连续 28 天更新的第 25 天更新：从今天（2026 年 10 月 30](https://t.me/zaihuapd/44999) ⭐️ 8.0/10

OpenAI 宣布其 ChatGPT Pro 和 Business Premium 订阅套餐的用量上限已翻倍，即日生效。

telegram · zaihuapd · Nov 8, 09:28

**标签**: `#OpenAI`, `#ChatGPT`, `#AI服务`, `#订阅`, `#产品更新`

---

<a id="item-8"></a>
## [姚顺雨：AI 公司护城河在产品层而非模型层](https://www.ithome.com/1/023/991.htm) ⭐️ 8.0/10

腾讯首席 AI 科学家姚顺雨指出，AI 公司的护城河更多在于产品层，通过理解用户背景、掌握专有数据和赢得用户信任来建立，而非仅仅依赖模型层。

telegram · zaihuapd · Nov 8, 14:17

**标签**: `#AI战略`, `#商业模式`, `#产品管理`, `#竞争优势`

---

<a id="item-9"></a>
## [👁️ 黄仁勋承认婚外情并致歉 英伟达董事会启动间谍指控独立调查](https://www.bloomberg.com/news/articles/2026-11-08/nvidia-board-to-probe-spying-case-after-ceo-jensen-huang-admits-infidelity) ⭐️ 8.0/10

英伟达董事会已启动独立调查，以查明首席执行官黄仁勋（他已承认婚外情并致歉）是否成为外国情报行动的目标。

telegram · zaihuapd · Nov 8, 21:39

**标签**: `#企业治理`, `#国家安全`, `#英伟达`, `#科技新闻`, `#高管动态`

---

<a id="item-10"></a>
## [🤖 Anthropic 报告：科学家主要用 Claude 做数据分析和写作](https://www.anthropic.com/research/how-researchers-use-claude) ⭐️ 8.0/10

Anthropic 报告指出，科学家主要利用 Claude 进行数据分析和写作，其中正式科学领域使用更多，并估计 AI 有望将研究产出提高 2 至 15 倍。

telegram · zaihuapd · Nov 9, 01:29

**标签**: `#AI应用`, `#研究生产力`, `#大型语言模型`, `#科学计算`, `#数据分析`

---

<a id="item-11"></a>
## [📱 Win11 测试统一应用更新页，取代第三方弹窗](https://www.windowslatest.com/2026/11/09/for-20-years-windows-apps-like-java-have-nagged-you-with-their-own-update-pop-ups-and-windows-11-now-wants-to-end-it/) ⭐️ 8.0/10

Windows 11 正在测试一项新功能，旨在通过在设置中提供统一的应用更新页面来集中管理第三方应用更新，从而取代独立的更新弹窗。

telegram · zaihuapd · Nov 9, 02:09

**标签**: `#Windows 11`, `#用户体验`, `#系统更新`, `#软件管理`, `#操作系统`

---

<a id="item-12"></a>
## [报告：中国模型占全球开源模型企业支出 89%  Menlo Ventures 本周发布的报告称，中国模型占全球开源模型企业支出的 89%，其中月之暗面 Kimi](https://t.me/zaihuapd/45009) ⭐️ 8.0/10

Menlo Ventures 报告显示，中国模型占据全球开源 AI 模型企业支出的 89%，其中 Kimi 领先，但开源模型仅占整体模型支出的 4%，而 Anthropic 和 OpenAI 合计拿下 86%的市场份额。

telegram · zaihuapd · Nov 9, 03:12

**标签**: `#AI市场`, `#开源AI`, `#市场份额`, `#中国科技`, `#企业AI`

---

<a id="item-13"></a>
## [Hide your slop PR descriptions behind <details><summary>](https://simonwillison.net/2026/Nov/9/details-summary/) ⭐️ 7.0/10

Simon Willison 建议使用 HTML 的`<details><summary>`标签来折叠冗长且由 AI 生成的拉取请求描述，从而在保留详细信息的同时，使其对人工审阅者更易于消化。

rss · Simon Willison · Nov 9, 04:25

**标签**: `#软件工程`, `#AI辅助开发`, `#代码审查`, `#开发者效率`, `#工作流优化`

---

<a id="item-14"></a>
## [parse_number() as a SQLite extension: C vs Rust](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 7.0/10

Simon Willison 探索了如何将`parse_number()`作为 SQLite 扩展，比较了 C 和 Rust 在性能和代码复杂性方面的实现差异，并利用 Claude 进行初步的开发探索。

rss · Simon Willison · Nov 8, 22:26

**标签**: `#SQLite`, `#Rust`, `#C Programming`, `#Database Extensions`, `#LLM Tools`

---

<a id="item-15"></a>
## [datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages](https://simonwillison.net/2026/Nov/7/link-rel-next/) ⭐️ 7.0/10

Simon Willison 发现并修复了 Datasette 的一个性能问题，即 Firefox 因`link: rel="next"` HTTP 头而对 HTML 页面进行不必要的预取，导致带宽和服务器资源浪费。

rss · Simon Willison · Nov 7, 23:57

**标签**: `#Web性能`, `#HTTP头`, `#Firefox`, `#Datasette`

---

<a id="item-16"></a>
## [CPU-Z：32 GB 与 64 GB 内存占比同比下滑](https://www.techpowerup.com/354574/cpu-z-data-shows-16-gb-ram-gaining-ground-while-32-gb-and-64-gb-ram-shares-shrink) ⭐️ 7.0/10

CPU-Z 数据显示，PC 平均内存容量首次同比下降，16GB 占比上升，而 32GB 和 64GB 占比下滑，同时 DDR4 份额回升，并预测未来几年内存将面临严重短缺。

telegram · zaihuapd · Nov 8, 04:24

**标签**: `#PC硬件`, `#内存市场`, `#市场趋势`, `#DRAM`, `#数据分析`

---

<a id="item-17"></a>
## [🤖 Siri AI 新增五门语言支持，年底扩至繁体中文  苹果随 27.2 系统更新将全新版 Siri AI 扩展至法语、日语、韩语、葡萄牙语和西班牙语，需配合](https://t.me/zaihuapd/45001) ⭐️ 7.0/10

苹果正在通过系统更新将全新版 Siri AI 扩展至法语、日语、韩语、葡萄牙语和西班牙语，并计划在年底前增加繁体中文等四种语言，以配合支持 Apple 智能的设备使用。

telegram · zaihuapd · Nov 8, 16:36

**标签**: `#AI`, `#Apple`, `#Siri`, `#Localization`, `#Product Update`

---