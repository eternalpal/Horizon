---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> From 22 items, 7 important content pieces were selected

---

1. [vLLM v0.25.0 发布：LLM 推理的重大增强](#item-1) ⭐️ 9.0/10
2. [SpaceXAI 与 Cursor 联合发布 Grok 4.5，聚焦专业 AI 任务](#item-2) ⭐️ 9.0/10
3. [U-Boot 引导程序漏洞允许在操作系统启动前执行恶意代码](#item-3) ⭐️ 9.0/10
4. [🤖 OpenAI 正式发布 GPT‑5.6 系列：旗舰 Sol 全面提升，性能成本比大幅优化  GPT-5.6 系列：Sol 负责最强能力，Terra 平衡性能](#item-4) ⭐️ 9.0/10
5. [Quoting Nilay Patel](#item-5) ⭐️ 8.0/10
6. [余承东怒斥问界 M8 隐私漏洞 "太愚蠢"，要求团队不吃不喝不睡立即修复](#item-6) ⭐️ 8.0/10
7. [sqlite-utils 4.1](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0 发布：LLM 推理的重大增强](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 是一个重要版本，它将 Model Runner V2 设为所有密集模型的默认执行路径，完全移除了旧版 PagedAttention 实现，并使 Transformers 后端达到了与原生 vLLM 相当的性能。此版本还引入了动态推测解码（与完整 CUDA 图兼容）和 FP8 MoE 支持等高级功能。 这些重大的架构变更和性能优化显著提升了 vLLM 在大型语言模型推理方面的效率、可扩展性和能力。它们使得 LLM 的部署更快、更具成本效益，从而惠及快速发展的 AI 生态系统中的开发者和组织。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的缓存前缀以及多模态前缀双向注意力等功能。此版本还包含一个新的流式解析器引擎，用于统一的工具调用/推理解析，以及针对异构词汇（TLI）的通用推测解码，并引入了新的 DSpark 和 DFlash 编解码器。

github · khluu · Jul 11, 20:06

**背景**: PagedAttention 是一种用于 LLM 推理的内存管理技术，它将 KV 缓存存储在固定大小的块中，类似于操作系统中的虚拟内存分页，以提高内存效率。Model Runner V2 是 vLLM 重新设计的核心执行器，旨在通过用 Triton 内核和异步调度取代基于 Python 的模型执行器，使其更具模块化、高效性和 GPU 原生性。推测解码是一种推理优化技术，它通过使用一个较小的草稿模型预测多个 token，并用一个较大的目标模型同时验证这些 token，从而加速 LLM，在不影响输出质量的情况下降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@aimlverselab/llm-pagedattention-efficient-kv-cache-batching-and-scalable-inference-cef66882a26c">LLM PagedAttention : Efficient KV Cache, Batching and... | Medium</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI ...</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#vLLM`, `#Performance Optimization`, `#Deep Learning`, `#Release Notes`

---

<a id="item-2"></a>
## [SpaceXAI 与 Cursor 联合发布 Grok 4.5，聚焦专业 AI 任务](https://t.me/zaihuapd/42484) ⭐️ 9.0/10

SpaceXAI 与 Cursor 联合发布了 Grok 4.5，这是 SpaceX 以 600 亿美元收购 Cursor 后双方推出的首个联合 AI 模型。这款新一代 AI 模型专为编码、法律和金融服务等高难度专业任务设计，并在 Harvey 法律代理基准测试中排名第一。 此次发布标志着 AI 领域的一项重大战略举措，结合了 SpaceX 的资源和 Cursor 的专业知识，以创建高度专业化的 AI 代理。其在法律基准测试中的卓越表现以及对高价值专业领域的关注，可能会显著提高这些行业的生产力和效率，并有望为 AI 在专业领域的应用树立新标准。 Grok 4.5 以每秒 80 个 token (TPS) 的速度运行，并声称其 token 效率是同类领先模型的两倍。除了其主要关注领域外，该模型还增强了网络安全能力，为敏感的专业应用提供了强大的解决方案。

telegram · zaihuapd · Jul 11, 01:44

**背景**: Cursor，原名 Anysphere, Inc.，是一家成立于 2022 年的美国软件公司，以其 AI 编码代理和开发环境而闻名，于 2026 年 6 月被 SpaceX 以 600 亿美元收购。Harvey 法律代理基准测试是由 Harvey.ai 发布的一个开源工具，旨在评估和改进 AI 代理处理实际法律工作的能力。大型语言模型中的 token 效率指的是相对于推理过程中消耗的 token 数量，生成有用输出的有效程度，这对于优化运营成本和性能至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark">Introducing Harvey’s Legal Agent Benchmark</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company)</a></li>
<li><a href="https://grokipedia.com/page/Most_Token-Efficient_AI_Models_2026">Most Token-Efficient AI Models (2026) — Grokipedia</a></li>

</ul>
</details>

**标签**: `#AI模型`, `#LLM`, `#专业服务AI`, `#SpaceX`, `#Grok`

---

<a id="item-3"></a>
## [U-Boot 引导程序漏洞允许在操作系统启动前执行恶意代码](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 9.0/10

固件安全公司 Binarly 本周披露了 U-Boot 引导程序 FIT 签名验证代码中的六个漏洞，其中两个可导致任意代码执行，四个可造成设备崩溃。这些漏洞最早可追溯到 U-Boot 2013.07 版本，影响超过 50 个稳定版本及大量下游厂商分支。 这些关键漏洞意义重大，因为它们允许攻击者在操作系统或安全软件启动之前，在固件验证阶段执行恶意代码。这使得攻击者能够在广泛的嵌入式系统上禁用安全功能、修改启动流程或植入持久性固件恶意软件。 这些漏洞位于 FIT 签名验证机制中，这是维护固件信任根的关键组件。尽管 U-Boot 维护者已接受补丁，但修复需要各硬件厂商将其集成到固件更新中才能分发，导致许多已停止支持的老旧设备可能永远无法获得修复。

telegram · zaihuapd · Jul 11, 08:32

**背景**: U-Boot（通用引导加载程序）是一款广泛使用的开源引导加载程序，专为嵌入式系统设计，负责初始化硬件并加载操作系统。引导加载程序是计算机启动时运行的第一个软件程序，它负责准备系统以加载主操作系统。FIT（Flattened Image Tree）签名验证是 U-Boot 的一项功能，用于在加载固件镜像之前确保其完整性和真实性，作为信任根。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.binarly.io/blog/unfit-to-boot-breaking-u-boots-fit-signature-verification">Unfit to Boot: Breaking U-Boot's FIT Signature Verification | Binarly</a></li>
<li><a href="https://www.cnblogs.com/minuhy/p/18800464">【Linux】U-Boot 加载并启动 Linux 系统程序 - 清风来叙 - 博客园</a></li>
<li><a href="https://docs.u-boot.org/en/latest/usage/fit/signature.html">U-Boot FIT Signature Verification — Das U-Boot unknown version documentation</a></li>

</ul>
</details>

**标签**: `#固件安全`, `#U-Boot`, `#漏洞`, `#嵌入式系统`, `#网络安全`

---

<a id="item-4"></a>
## [🤖 OpenAI 正式发布 GPT‑5.6 系列：旗舰 Sol 全面提升，性能成本比大幅优化  GPT-5.6 系列：Sol 负责最强能力，Terra 平衡性能](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI 正式发布了 GPT-5.6 系列，其中旗舰 Sol 模型在性能和成本效益上全面提升，并引入了多智能体协作和程序化工具调用等新功能，同时推出了 Terra 和 Luna 模型以适应不同场景。

telegram · zaihuapd · Jul 11, 13:34

**标签**: `#AI模型`, `#LLMs`, `#OpenAI`, `#AI能力`, `#性能优化`

---

<a id="item-5"></a>
## [Quoting Nilay Patel](https://simonwillison.net/2026/Jul/10/nilay-patel/#atom-everything) ⭐️ 8.0/10

Nilay Patel argues that the current technical demands for augmented reality glasses necessitate either continuous cloud processing (invading privacy) or bulky devices, posing a fundamental dilemma for the industry.

rss · Simon Willison · Jul 10, 17:05

**标签**: `#Augmented Reality`, `#Privacy`, `#Hardware Limitations`, `#Ethics of Technology`

---

<a id="item-6"></a>
## [余承东怒斥问界 M8 隐私漏洞 "太愚蠢"，要求团队不吃不喝不睡立即修复](https://user.guancha.cn/main/content?id=1686339) ⭐️ 8.0/10

华为高管余承东严厉批评问界 M8 团队存在一个严重的隐私漏洞，即使用户关闭了位置权限，车辆定位仍可通过泊车代驾功能被追踪，并要求团队不惜一切代价立即通过 OTA 推送修复。

telegram · zaihuapd · Jul 11, 02:05

**标签**: `#隐私保护`, `#智能汽车`, `#软件质量`, `#网络安全`, `#事件响应`

---

<a id="item-7"></a>
## [sqlite-utils 4.1](https://simonwillison.net/2026/Jul/11/sqlite-utils/#atom-everything) ⭐️ 7.0/10

`sqlite-utils` version 4.1 adds a convenient `--code` option to its `insert` and `upsert` commands, enabling users to define data rows directly using Python code or files.

rss · Simon Willison · Jul 11, 23:50

**标签**: `#SQLite`, `#Python`, `#CLI Tools`, `#Data Engineering`, `#Utility`

---