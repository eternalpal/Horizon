---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> From 34 items, 11 important content pieces were selected

---

1. [无状态 MCP 2.0 重燃对 LLM 代理工具协议的兴趣](#item-1) ⭐️ 9.0/10
2. [美国最高法院拒绝受理 AI 作品版权案，维持“人类创作”法律原则  美国最高法院于 3 月 2 日拒绝受理计算机科学家 Stephen Thaler 的上诉，维](#item-2) ⭐️ 9.0/10
3. [Elevators](#item-3) ⭐️ 8.0/10
4. [Tailscale didn't stop the Hugging Face intrusion](#item-4) ⭐️ 8.0/10
5. [deepseek-ai/DeepSeek-V4-Flash-0731](#item-5) ⭐️ 8.0/10
6. [Quoting Bruce Schneier](#item-6) ⭐️ 8.0/10
7. [llm-chat-completions-server 0.1a0](#item-7) ⭐️ 8.0/10
8. [llm 0.32rc1](#item-8) ⭐️ 8.0/10
9. [MiniMax 多模态视频模型 H3 将于 8 月 3 日开源](#item-9) ⭐️ 8.0/10
10. [qm – Multiplayer agent harness for work](#item-10) ⭐️ 7.0/10
11. [🤖 Anthropic 将就美国战争部供应链风险认定提起法律挑战  Anthropic 首席执行官 Dario Amodei 3 月 5 日发表声明称，公司于前](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [无状态 MCP 2.0 重燃对 LLM 代理工具协议的兴趣](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

模型上下文协议（MCP）2.0，即 2026-07-28 规范，已正式发布，引入了向无状态设计的重大架构转变。此次更新简化了向 LLM 驱动的代理框架暴露工具的协议，重新激发了 Simon Willison 的兴趣，并促使他开发了`mcp-explorer`等新工具。 转向无状态的 MCP 2.0 显著降低了客户端和服务器的实现复杂性，使得构建可扩展的 Web 应用程序以及将 AI 代理与外部工具集成变得更加容易。这增强了代理交互的安全性和可控性，允许较小的模型有效利用工具，并可能扩大标准化代理框架的采用。 MCP 2.0 的核心变化是从需要两次 HTTP 请求（初始化会话，然后调用工具）的有状态协议，转变为使用单个 HTTP 请求进行工具调用的无状态协议，从而消除了服务器端会话管理的需要。通过将客户端信息和协议版本直接嵌入到单个请求中，实现了这种简化，使其更加健壮和可扩展。

rss · Simon Willison · Jul 31, 23:13

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的一项标准，旨在为大型语言模型（LLM）驱动的代理框架提供一种与外部工具交互的统一方式。最初，由于 Anthropic 的“Skills”框架等替代方法（允许代理访问 shell）提供了更大的灵活性，但也带来了安全风险，MCP 的采用面临挑战。MCP 2.0 中实现的无状态协议意味着服务器不保留先前请求的会话状态，确保每个请求都可以独立理解，从而简化了扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/seps/2575-stateless-mcp">SEP-2575: Make MCP Stateless - Model Context Protocol</a></li>
<li><a href="https://www.infoworld.com/article/4201254/model-context-protocol-is-going-stateless-to-make-scaling-simpler.html">Model Context Protocol is going stateless to make scaling simpler | InfoWorld</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/">The 2026-07-28 Specification | Model Context Protocol Blog</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLM`, `#Protocols`, `#Interoperability`, `#Software Development`

---

<a id="item-2"></a>
## [美国最高法院拒绝受理 AI 作品版权案，维持“人类创作”法律原则  美国最高法院于 3 月 2 日拒绝受理计算机科学家 Stephen Thaler 的上诉，维](https://t.me/zaihuapd/42900) ⭐️ 9.0/10

美国最高法院拒绝受理 AI 作品版权案上诉，维持了 AI 生成作品不受版权保护的裁定，重申了版权法中“人类作者”的核心原则。

telegram · zaihuapd · Jul 31, 13:11

**标签**: `#AI版权`, `#生成式AI`, `#法律政策`, `#知识产权`, `#美国最高法院`

---

<a id="item-3"></a>
## [Elevators](https://john.fun/elevators) ⭐️ 8.0/10

A Hacker News discussion on elevator scheduling algorithms explores their practical applications, connections to other scheduling problems like disk I/O, real-world complexities, and offers educational resources.

hackernews · Jrh0203 · Jul 31, 15:17

**标签**: `#Algorithms`, `#Scheduling`, `#System Design`, `#Software Engineering`, `#Optimization`

---

<a id="item-4"></a>
## [Tailscale didn't stop the Hugging Face intrusion](https://tailscale.com/blog/hugging-face-intrusion) ⭐️ 8.0/10

Tailscale transparently details how a leaked, reusable authentication key, not a vulnerability in their product, was exploited in the Hugging Face intrusion, using the incident to highlight security best practices and their features.

hackernews · bluehatbrit · Jul 31, 19:03

**标签**: `#Cybersecurity`, `#Incident Response`, `#Authentication`, `#Tailscale`, `#CI/CD Security`

---

<a id="item-5"></a>
## [deepseek-ai/DeepSeek-V4-Flash-0731](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek-V4-Flash-0731 is DeepSeek's latest 304B parameter large language model, featuring substantially enhanced agentic capabilities and potentially offering the best value-per-intelligence in the market, outperforming larger models at a lower cost.

rss · Simon Willison · Jul 31, 23:59

**标签**: `#Large Language Models`, `#AI Agents`, `#Model Efficiency`, `#AI Performance`, `#DeepSeek AI`

---

<a id="item-6"></a>
## [Quoting Bruce Schneier](https://simonwillison.net/2026/Jul/30/bruce-schneier/#atom-everything) ⭐️ 8.0/10

Bruce Schneier argues that educational writing assignments are "gym tasks" for developing critical thinking skills, and over-reliance on AI for these tasks will lead to skill atrophy, a concern already noted by employers.

rss · Simon Willison · Jul 30, 18:25

**标签**: `#AI Ethics`, `#Education`, `#Critical Thinking`, `#Skill Development`

---

<a id="item-7"></a>
## [llm-chat-completions-server 0.1a0](https://simonwillison.net/2026/Jul/30/llm-chat-completions-server/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 llm-chat-completions-server 0.1a0，这是一个新工具，为本地 LLM 提供 OpenAI 聊天完成风格的 API，并利用内容寻址日志高效地去重和管理对话历史。

rss · Simon Willison · Jul 30, 15:43

**标签**: `#LLM`, `#Local AI`, `#API`, `#Software Development`, `#Content-Addressable Storage`

---

<a id="item-8"></a>
## [llm 0.32rc1](https://simonwillison.net/2026/Jul/30/llm-rc1/#atom-everything) ⭐️ 8.0/10

llm 0.32 的发布候选版本引入了新的模式设计，通过内容可寻址哈希 ID 改进了消息存储，实现了去重并支持分叉对话的消息树表示。

rss · Simon Willison · Jul 30, 15:30

**标签**: `#LLM`, `#数据库架构`, `#数据管理`, `#软件发布`, `#AI工具`

---

<a id="item-9"></a>
## [MiniMax 多模态视频模型 H3 将于 8 月 3 日开源](https://modelscope.cn/models/MiniMax/MiniMax-H3) ⭐️ 8.0/10

MiniMax 宣布其新一代通用多模态视频模型 H3 将于 2026 年 8 月 3 日在魔搭社区开源，该模型原生支持文本、图像、音频和视频的理解与生成，并具备多维度精准编辑控制能力。

telegram · zaihuapd · Jul 31, 12:37

**标签**: `#多模态AI`, `#视频生成`, `#开源模型`, `#AI模型`, `#深度学习`

---

<a id="item-10"></a>
## [qm – Multiplayer agent harness for work](https://github.com/yc-software/qm) ⭐️ 7.0/10

qm is a multiplayer agent harness for work designed to manage AI agents' scopes, sparking community discussion about its novelty and utility in the evolving landscape of multi-agent systems.

hackernews · tosh · Jul 31, 18:04

**标签**: `#AI Agents`, `#Multi-agent Systems`, `#Developer Tools`, `#Workflows`

---

<a id="item-11"></a>
## [🤖 Anthropic 将就美国战争部供应链风险认定提起法律挑战  Anthropic 首席执行官 Dario Amodei 3 月 5 日发表声明称，公司于前](https://t.me/zaihuapd/42891) ⭐️ 7.0/10

Anthropic 宣布将就美国战争部（国防部）将其认定为国家安全供应链风险的决定提起法律挑战，认为该行动缺乏法律依据。

telegram · zaihuapd · Jul 31, 08:00

**标签**: `#AI监管`, `#国家安全`, `#Anthropic`, `#法律挑战`, `#政府关系`

---