---
layout: default
title: "Horizon Summary: 2026-11-06 (ZH)"
date: 2026-11-06
lang: zh
---

> From 25 items, 11 important content pieces were selected

---

1. [OpenSSH 认证绕过漏洞（CVE-2024-6387）被发现](#item-1) ⭐️ 9.0/10
2. [MS Paint Remote Code Execution Vulnerability](#item-2) ⭐️ 9.0/10
3. [Claude Code sends your email address to websites](#item-3) ⭐️ 8.0/10
4. [♻️ 美国放行 H200 对华销售，英伟达寻求在华突破  路透社报道，美国商务部已批准约 10 家中国企业购买英伟达 H200 芯片，相关买家包括阿里巴巴、腾讯](#item-4) ⭐️ 8.0/10
5. [🤖 OpenAI 开始在 ChatGPT 测试广告，预计长期贡献近半营收  OpenAI 于 2 月 9 日开始在 ChatGPT 中测试广告。](#item-5) ⭐️ 8.0/10
6. [中移动香港与澳门运营商相继建成 U6GHz 网络  中国移动香港（CMHK）宣布建成全港首个 U6GHz 网络，于旺角旗舰店完成测试验证；同日，澳门电讯（CTM](#item-6) ⭐️ 8.0/10
7. [甲骨文取消与腾讯 70 亿美元芯片租赁协议  甲骨文取消了与腾讯价值约 70 亿美元的 AI 芯片租赁协议。](#item-7) ⭐️ 8.0/10
8. [The Hackintosh Reborn](#item-8) ⭐️ 7.0/10
9. [Quoting Paul Ford](#item-9) ⭐️ 7.0/10
10. [🤖 DeepSeek Harness 日活达 154 万，插件超 3.5 万个](#item-10) ⭐️ 7.0/10
11. [印度首款国产 28nm 芯片今年发布  印度首个国产半导体芯片预计 2025 年问世，首批芯片采用 28 纳米制程。](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenSSH 认证绕过漏洞（CVE-2024-6387）被发现](https://sshhole.com/) ⭐️ 9.0/10

OpenSSH 中发现了一个名为“sshole”（CVE-2024-6387）的严重认证绕过漏洞，主要影响使用 `musl` libc 的系统。该漏洞源于密码哈希过程中 `crypt()` 函数返回错误时处理不当。 此漏洞至关重要，因为它允许攻击者绕过 OpenSSH 中的认证，OpenSSH 是广泛用于安全远程访问服务器和系统的工具。其影响巨大，特别是对于依赖 `musl` libc 的环境，可能导致未经授权的系统访问。 该漏洞具体发生在 OpenSSH 的 `sshd` 尝试验证密码时，如果 `crypt()` 函数返回错误，并且返回的值与哈希值匹配，就会导致意外的认证绕过。此问题在 `musl` libc 实现中尤为突出，因为之前针对类似故障的修复不完整，导致 `crypt_sha` 中存在一个易受攻击的路径。

hackernews · josemrb · Nov 5, 12:19

**背景**: OpenSSH 是一套实用程序，使用 SSH 协议实现对计算机系统的安全远程访问。`crypt()` 函数是 Unix 类系统中常用的标准 C 库函数，用于单向密码哈希和验证。`musl` libc 是一个轻量级、高效且符合标准的适用于基于 Linux 操作系统的 C 标准库，常用于嵌入式系统和像 Alpine Linux 这样的轻量级 Linux 发行版中，作为 `glibc` 的替代品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Musl_libc">Musl libc</a></li>
<li><a href="https://musl.libc.org/">musl libc</a></li>

</ul>
</details>

**社区讨论**: 社区讨论深入探讨了技术根本原因，指出“带内信号”是一个关键设计缺陷，其中“*”等特殊字符被模糊地用于“无密码”和“错误状态”。参与者强调 `musl` libc 对此类故障的修复不完整，一些人对 `musl` 开发者在核心加密功能上的设计选择和审计实践表示失望。

**标签**: `#OpenSSH`, `#Security`, `#Vulnerability`, `#Authentication`, `#musl`

---

<a id="item-2"></a>
## [MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 9.0/10

一项关键的远程代码执行漏洞（CVE-2026-83844）已在 MS Paint 中被发现，允许未经身份验证的攻击者通过发送特制网络数据包，在无需用户交互的情况下执行任意代码，影响特定版本并需要立即修补。

hackernews · kuberwastaken · Nov 5, 20:43

**标签**: `#网络安全`, `#漏洞`, `#Windows`, `#远程代码执行`

---

<a id="item-3"></a>
## [Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 8.0/10

A Hacker News discussion reveals that Anthropic's Claude Code was inadvertently sending user email addresses to external websites, a privacy concern that the company has acknowledged and committed to resolving in an upcoming release.

hackernews · motoroco · Nov 5, 22:17

**标签**: `#AI Ethics`, `#Privacy`, `#AI Tools`, `#Software Security`, `#Developer Tools`

---

<a id="item-4"></a>
## [♻️ 美国放行 H200 对华销售，英伟达寻求在华突破  路透社报道，美国商务部已批准约 10 家中国企业购买英伟达 H200 芯片，相关买家包括阿里巴巴、腾讯](https://t.me/zaihuapd/44945) ⭐️ 8.0/10

美国商务部据报道已批准向包括阿里巴巴和腾讯在内的约 10 家中国企业出售英伟达 H200 AI 芯片，此举标志着中美科技竞争中的一项复杂进展，尽管中国买家仍持谨慎态度。

telegram · zaihuapd · Nov 5, 14:42

**标签**: `#AI芯片`, `#地缘政治`, `#英伟达`, `#中美科技`, `#供应链`

---

<a id="item-5"></a>
## [🤖 OpenAI 开始在 ChatGPT 测试广告，预计长期贡献近半营收  OpenAI 于 2 月 9 日开始在 ChatGPT 中测试广告。](https://t.me/zaihuapd/44955) ⭐️ 8.0/10

OpenAI 已开始在 ChatGPT 中测试广告，面向免费和 Go 订阅用户，首席执行官 Sam Altman 预计广告收入长期将贡献公司总营收的近一半，同时公司计划发布更新的聊天模型。

telegram · zaihuapd · Nov 6, 03:15

**标签**: `#AI商业`, `#货币化`, `#ChatGPT`, `#OpenAI`, `#产品策略`

---

<a id="item-6"></a>
## [中移动香港与澳门运营商相继建成 U6GHz 网络  中国移动香港（CMHK）宣布建成全港首个 U6GHz 网络，于旺角旗舰店完成测试验证；同日，澳门电讯（CTM](https://t.me/zaihuapd/44957) ⭐️ 8.0/10

中国移动香港、澳门电讯和中国电信澳门相继建成并测试了 U6GHz 网络，标志着港澳地区在 5G-A 和 6G 演进关键频谱应用上取得突破。

telegram · zaihuapd · Nov 6, 04:18

**标签**: `#5G-A`, `#6G`, `#电信`, `#网络基础设施`, `#U6GHz`

---

<a id="item-7"></a>
## [甲骨文取消与腾讯 70 亿美元芯片租赁协议  甲骨文取消了与腾讯价值约 70 亿美元的 AI 芯片租赁协议。](https://t.me/zaihuapd/44958) ⭐️ 8.0/10

甲骨文在美国政府的压力下，取消了与腾讯价值 70 亿美元的 AI 芯片租赁协议，该协议原计划让腾讯通过甲骨文在东南亚的数据中心获取先进 AI 芯片。

telegram · zaihuapd · Nov 6, 05:02

**标签**: `#地缘政治`, `#AI芯片`, `#企业战略`, `#云计算`, `#供应链`

---

<a id="item-8"></a>
## [The Hackintosh Reborn](https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/) ⭐️ 7.0/10

This content introduces a new, AI-driven approach to Hackintosh, prompting a lively community discussion about the desire to run alternative operating systems like Linux on Apple's powerful M-series hardware.

hackernews · rubatuga · Nov 5, 19:08

**标签**: `#Hackintosh`, `#Apple Silicon`, `#AI/ML`, `#Operating Systems`, `#Hardware Customization`

---

<a id="item-9"></a>
## [Quoting Paul Ford](https://simonwillison.net/2026/Nov/5/paul-ford/) ⭐️ 7.0/10

Paul Ford 观察到网络浏览器作为应用软件的强大能力日益增强，并且获取这种能力所需的成本似乎每天都在下降。

rss · Simon Willison · Nov 5, 17:34

**标签**: `#web-development`, `#browsers`, `#application-platforms`, `#technology-trends`

---

<a id="item-10"></a>
## [🤖 DeepSeek Harness 日活达 154 万，插件超 3.5 万个](https://mp.weixin.qq.com/s/xqyrRaiBpIcf0jeJzP7W0g) ⭐️ 7.0/10

DeepSeek Harness 平台日活跃用户已达 154 万，拥有近 3.5 万个插件，并计划通过建设官方插件市场和激励计划，将其打造为“Agent 时代的操作系统”。

telegram · zaihuapd · Nov 5, 15:20

**标签**: `#AI平台`, `#Agent技术`, `#生态系统`, `#DeepSeek`, `#AI应用`

---

<a id="item-11"></a>
## [印度首款国产 28nm 芯片今年发布  印度首个国产半导体芯片预计 2025 年问世，首批芯片采用 28 纳米制程。](https://t.me/zaihuapd/44954) ⭐️ 7.0/10

印度计划于 2025 年发布其首款国产 28 纳米芯片，旨在成为中国大陆和台湾地区以外可靠的芯片供应来源，并积极吸引外资以扩大半导体产业规模。

telegram · zaihuapd · Nov 6, 02:00

**标签**: `#半导体制造`, `#工业政策`, `#供应链韧性`, `#印度科技`, `#芯片生产`

---