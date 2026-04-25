---
layout: default
title: "Horizon Summary: 2026-04-25 (ZH)"
date: 2026-04-25
lang: zh
---

> From 35 items, 13 important content pieces were selected

---

1. [vLLM v0.20.0 发布，引入 TurboQuant 2 位 KV 缓存和 FA4](#item-1) ⭐️ 9.0/10
2. [Google plans to invest up to $40B in Anthropic](#item-2) ⭐️ 9.0/10
3. [DeepSeek V4 - almost on the frontier, a fraction of the price](#item-3) ⭐️ 9.0/10
4. [MIT 科学家建立经典与量子物理的数学桥梁](#item-4) ⭐️ 9.0/10
5. [华为发布 ADS 4 智驾系统，预计 2025 年具备 L3 商用能力  在 4 月 22 日的华为乾崑智能技术大会上，华为智能汽车解决方案 BU CEO 靳玉](#item-5) ⭐️ 9.0/10
6. [Sabotaging projects by overthinking, scope creep, and structural diffing](#item-6) ⭐️ 8.0/10
7. [The people do not yearn for automation](#item-7) ⭐️ 8.0/10
8. [Serving the For You feed](#item-8) ⭐️ 8.0/10
9. [Extract PDF text in your browser with LiteParse for the web](#item-9) ⭐️ 8.0/10
10. [A pelican for GPT-5.5 via the semi-official Codex backdoor API](#item-10) ⭐️ 8.0/10
11. [分析者质疑自建订阅验证机制：终身订阅的“终身”由谁定义？](#item-11) ⭐️ 8.0/10
12. [llm 0.31](#item-12) ⭐️ 7.0/10
13. [llm-openai-via-codex 0.1a0](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.20.0 发布，引入 TurboQuant 2 位 KV 缓存和 FA4](https://github.com/vllm-project/vllm/releases/tag/v0.20.0) ⭐️ 9.0/10

vLLM v0.20.0 版本已发布，默认升级到 CUDA 13.0 和 PyTorch 2.11，支持 Transformers v5，并重新启用 FlashAttention 4 作为默认的 MLA 预填充后端。一个重要亮点是引入了 TurboQuant 2 位 KV 缓存压缩，使 KV 缓存容量增加了 4 倍。 此版本对大型语言模型（LLM）推理至关重要，因为通过 TurboQuant 2 位 KV 缓存和 FlashAttention 4 实现的内存和性能优化，显著降低了部署成本并提高了效率。这些进步使得 LLM 操作更具成本效益和可扩展性，从而使部署 AI 模型的开发者和组织受益。 TurboQuant 2 位 KV 缓存压缩显著提升了 KV 缓存容量 4 倍，直接解决了 LLM 推理中的内存瓶颈问题。FlashAttention 4 现在作为默认的 MLA 预填充后端重新启用，支持 SM90+ 架构上的 head-dim 512 和分页 KV，进一步提升了性能。

github · khluu · Apr 23, 21:02

**背景**: KV 缓存（Key-Value cache）是大型语言模型推理中的关键组件，它存储先前令牌的键和值状态，以避免为每个新令牌重新计算它们，这会显著消耗 GPU 内存，尤其是在长上下文窗口下。FlashAttention 是一种优化的注意力算法，旨在通过以更节省内存的方式执行注意力计算，避免将大型中间矩阵写入高带宽内存，从而加速 Transformer 模型并减少其内存占用。TurboQuant 是 Google Research 开发的一种用于压缩 KV 缓存的方法，它采用极坐标旋转和标量量化等技术，以大幅减少 LLM 推理期间的内存使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.05451">[2603.05451] FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling</a></li>
<li><a href="https://turbo-quant.com/">Google TurboQuant — Paper, Tools, Benchmarks & Framework Status</a></li>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>

</ul>
</details>

**标签**: `#LLM推理`, `#性能优化`, `#内存管理`, `#AI系统`, `#vLLM`

---

<a id="item-2"></a>
## [Google plans to invest up to $40B in Anthropic](https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic) ⭐️ 9.0/10

Google is reportedly planning to invest up to $40 billion in AI startup Anthropic, a move with significant implications for the competitive landscape and infrastructure of the artificial intelligence industry.

hackernews · elffjs · Apr 24, 16:04

**标签**: `#AI Investment`, `#Strategic Partnerships`, `#AI Industry`, `#Cloud Infrastructure`, `#AI Competition`

---

<a id="item-3"></a>
## [DeepSeek V4 - almost on the frontier, a fraction of the price](https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything) ⭐️ 9.0/10

DeepSeek has released V4-Pro and V4-Flash, new 1-million-token context Mixture of Experts models, with V4-Pro being the largest open-weights model to date, offering near-frontier performance at a competitive price under an MIT license.

rss · Simon Willison · Apr 24, 06:01

**标签**: `#AI Models`, `#Large Language Models`, `#Open Source AI`, `#Mixture of Experts`, `#DeepSeek`

---

<a id="item-4"></a>
## [MIT 科学家建立经典与量子物理的数学桥梁](https://www.newsy-today.com/new-study-bridges-the-worlds-of-classical-and-quantum-physics-mit-news/) ⭐️ 9.0/10

麻省理工学院科学家通过在 Hamilton-Jacobi 方程中引入“密度”计算，建立了一个数学桥梁，使经典物理框架能够与薛定谔方程产生一致结果，从而为量子行为提供更简洁的表述，并有望改进量子比特预测及统一量子力学与广义相对论。

telegram · zaihuapd · Apr 23, 16:30

**标签**: `#量子物理`, `#经典物理`, `#理论物理`, `#数学建模`, `#量子计算`

---

<a id="item-5"></a>
## [华为发布 ADS 4 智驾系统，预计 2025 年具备 L3 商用能力  在 4 月 22 日的华为乾崑智能技术大会上，华为智能汽车解决方案 BU CEO 靳玉](https://t.me/zaihuapd/41039) ⭐️ 9.0/10

华为发布了新一代智驾系统 HUAWEI ADS 4，并预计在 2025 年具备 L3 级自动驾驶的商用能力，旨在推动高速场景下的 L3 应用。

telegram · zaihuapd · Apr 24, 01:40

**标签**: `#自动驾驶`, `#L3自动驾驶`, `#华为`, `#智能汽车`, `#汽车技术`

---

<a id="item-6"></a>
## [Sabotaging projects by overthinking, scope creep, and structural diffing](https://kevinlynagh.com/newsletter/2026_04_overthinking/) ⭐️ 8.0/10

这篇文章探讨了过度思考、范围蔓延和结构性差异等常见陷阱如何阻碍项目进展，这是一个在软件开发和学术研究等多个领域都得到广泛认可和讨论的问题。

hackernews · alcazar · Apr 24, 14:28

**标签**: `#项目管理`, `#软件开发`, `#生产力`, `#范围蔓延`, `#决策制定`

---

<a id="item-7"></a>
## [The people do not yearn for automation](https://simonwillison.net/2026/Apr/24/the-people-do-not-yearn-for-automation/#atom-everything) ⭐️ 8.0/10

Nilay Patel's essay, highlighted by Simon Willison, explores why AI is unpopular with the general public despite high usage, attributing this to a 'software brain' mentality that prioritizes automation and data modeling over human experience.

rss · Simon Willison · Apr 24, 22:38

**标签**: `#AI Ethics`, `#Societal Impact`, `#Automation`, `#Public Perception`, `#Technology Criticism`

---

<a id="item-8"></a>
## [Serving the For You feed](https://simonwillison.net/2026/Apr/24/serving-the-for-you-feed/#atom-everything) ⭐️ 8.0/10

该文章描述了 Bluesky 的“为你推荐”信息流如何在一个游戏 PC 上通过单个 Go 进程和 SQLite 为 7.2 万用户提供服务，利用协同过滤和 Bluesky 数据流进行推荐。

rss · Simon Willison · Apr 24, 01:08

**标签**: `#系统设计`, `#Go语言`, `#SQLite`, `#推荐系统`, `#Bluesky`

---

<a id="item-9"></a>
## [Extract PDF text in your browser with LiteParse for the web](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/#atom-everything) ⭐️ 8.0/10

Simon Willison 成功将 LlamaIndex 的 LiteParse（一个不依赖 AI、通过启发式算法进行空间 PDF 文本提取的开源工具）移植到浏览器中运行，为 Web 应用提供了有价值的客户端解决方案。

rss · Simon Willison · Apr 23, 21:54

**标签**: `#PDF处理`, `#Web开发`, `#开源`, `#文本提取`, `#启发式算法`

---

<a id="item-10"></a>
## [A pelican for GPT-5.5 via the semi-official Codex backdoor API](https://simonwillison.net/2026/Apr/23/gpt-5-5/#atom-everything) ⭐️ 8.0/10

Simon Willison details the release of GPT-5.5, highlighting its capabilities and the current lack of an official API, while suggesting a 'semi-official Codex backdoor API' for early developer access.

rss · Simon Willison · Apr 23, 19:59

**标签**: `#GPT-5.5`, `#OpenAI`, `#API`, `#Large Language Models`, `#Early Access`

---

<a id="item-11"></a>
## [分析者质疑自建订阅验证机制：终身订阅的“终身”由谁定义？](https://github.com/Yu9191/flux) ⭐️ 8.0/10

一份逆向工程报告揭示，某知名应用的订阅验证机制过度依赖自建服务器，导致服务器故障时“终身订阅”可能失效，引发了对“终身”定义和用户数字权益的质疑。

telegram · zaihuapd · Apr 24, 02:02

**标签**: `#订阅模式`, `#软件架构`, `#数字权益`, `#逆向工程`, `#系统设计`

---

<a id="item-12"></a>
## [llm 0.31](https://simonwillison.net/2026/Apr/24/llm/#atom-everything) ⭐️ 7.0/10

The `llm` 0.31 release by Simon Willison adds support for the new GPT-5.5 OpenAI model, along with new options for text verbosity and image detail levels, enhancing its capabilities for interacting with advanced language models.

rss · Simon Willison · Apr 24, 23:35

**标签**: `#LLM Tools`, `#OpenAI API`, `#Release Notes`, `#AI/ML`, `#CLI`

---

<a id="item-13"></a>
## [llm-openai-via-codex 0.1a0](https://simonwillison.net/2026/Apr/23/llm-openai-via-codex/#atom-everything) ⭐️ 7.0/10

Simon Willison announced the release of `llm-openai-via-codex 0.1a0`, a utility that reuses Codex CLI credentials to facilitate OpenAI API calls through his `llm` command-line tool.

rss · Simon Willison · Apr 23, 19:22

**标签**: `#LLM`, `#OpenAI`, `#CLI Tool`, `#Integration`

---