---
layout: default
title: "Horizon Summary: 2026-05-18 (ZH)"
date: 2026-05-18
lang: zh
---

> From 25 items, 7 important content pieces were selected

---

1. [SGLang v0.5.12 增强 DeepSeek V4 推理，带来高级优化](#item-1) ⭐️ 8.0/10
2. [I turned a $80 RK3562 Android tablet into a Debian Linux workstation](#item-2) ⭐️ 8.0/10
3. [GDS weighs in on the NHS's decision to retreat from Open Source](#item-3) ⭐️ 8.0/10
4. [欧盟 DMA 推动 Firefox 在欧洲新增逾 600 万用户](#item-4) ⭐️ 8.0/10
5. [Quoting Julia Evans](#item-5) ⭐️ 7.0/10
6. [Amazon 强制员工达成 AI 使用配额，员工却用它来做无关工作的事](#item-6) ⭐️ 7.0/10
7. [无锡将建“Token 工厂”，首批部署 4 台华为昇腾 384 超节点集群](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.12 增强 DeepSeek V4 推理，带来高级优化](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) ⭐️ 8.0/10

SGLang v0.5.12 已发布，为 DeepSeek V4 带来了全面且高度优化的推理支持，并集成了 Intern-S2-Preview 和 MiniCPM-V 4.6 等新模型。此次更新包括广泛的并行化、对 Nvidia B300/H200 和 AMD MI35X 等尖端 GPU 的硬件加速，以及各种底层性能和内存管理改进。 此次发布显著增强了 SGLang 高效大语言模型（LLM）推理的能力，特别是针对 DeepSeek V4，从而实现更快、更具成本效益的部署。对 Nvidia B300/H200 和 AMD MI35X 等尖端 GPU 的硬件加速支持，确保了 SGLang 在高性能 LLM 服务技术领域保持领先地位。 主要技术细节包括通过各种并行技术（张量、专家、上下文、数据并行注意力）对 DeepSeek V4 的全面支持，以及对 Nvidia B300/H200 和 AMD MI35X GPU 的硬件加速。此次发布还集成了预填充-解码分离、用于 KV 缓存卸载的 HiSparse、W4A4/W4A8 量化，以及统一的 Radix Tree 缓存系统（HiCache），以提高性能和内存效率。

github · Fridge003 · May 16, 18:23

**背景**: 大语言模型（LLM）推理通常包括两个阶段：预填充（处理输入上下文）和解码（逐个生成 token）。“预填充-解码分离”通过解耦这两个阶段来优化推理。“专家并行”对于混合专家（MoE）LLM 至关重要，它将不同的“专家”（神经网络）分布到多个设备上，以处理输入的特定部分，从而提高可扩展性。此外，“KV 缓存卸载到 CPU 内存”是一种内存管理技术，当对高效 token 生成至关重要的 Key-Value 缓存超出可用 GPU 内存时，它允许将缓存转移到 CPU 内存，从而支持更长的上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://naddod.medium.com/understanding-the-prefill-decode-disaggregation-in-llm-inference-optimization-5c11223a5360">Understanding the Prefill - decode Disaggregation in LLM ... | Medium</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/expert-parallelism-in-deep-learning">Expert Parallelism: Scaling Mixture-of-Experts Models | DigitalOcean</a></li>
<li><a href="https://medium.com/byte-sized-ai/llm-inference-optimization-accelerating-long-context-generation-with-kv-cache-offloading-to-cpu-12d3bea407d8">LLM Inference: Accelerating Long Context Generation with KV Cache ...</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#Deep Learning Optimization`, `#GPU Acceleration`, `#DeepSeek V4`, `#System Software`

---

<a id="item-2"></a>
## [I turned a $80 RK3562 Android tablet into a Debian Linux workstation](https://github.com/tech4bot/rk3562deb) ⭐️ 8.0/10

一个项目成功地将一台价值 80 美元的 RK3562 安卓平板电脑改造成了 Debian Linux 工作站，展示了实用的硬件再利用。

hackernews · tech4bot · May 17, 13:16

**标签**: `#Linux`, `#硬件改造`, `#DIY计算`, `#Debian`, `#平板电脑再利用`

---

<a id="item-3"></a>
## [GDS weighs in on the NHS's decision to retreat from Open Source](https://simonwillison.net/2026/May/17/gds-weighs-in/#atom-everything) ⭐️ 8.0/10

The Government Digital Service (GDS) has published guidance reaffirming 'open by default' for public sector code, directly countering the NHS's recent decision to close open-source repositories due to reported vulnerabilities.

rss · Simon Willison · May 17, 15:59

**标签**: `#Open Source Policy`, `#Public Sector IT`, `#Software Security`, `#Government Digital Service`, `#UK Government`

---

<a id="item-4"></a>
## [欧盟 DMA 推动 Firefox 在欧洲新增逾 600 万用户](http://news.zol.com.cn/1182/11821187.html) ⭐️ 8.0/10

欧盟的《数字市场法案》要求手机开放默认浏览器选择后，Firefox 在欧洲新增了逾 600 万用户，Mozilla 呼吁将此规则扩展到个人电脑。

telegram · zaihuapd · May 18, 02:32

**标签**: `#欧盟 DMA`, `#浏览器竞争`, `#Firefox`, `#科技监管`, `#市场份额`

---

<a id="item-5"></a>
## [Quoting Julia Evans](https://simonwillison.net/2026/May/16/julia-evans/#atom-everything) ⭐️ 7.0/10

Julia Evans shares her journey of learning to love and respect CSS as a serious technology that solves hard problems, realizing many frustrations stem from a lack of understanding rather than inherent flaws.

rss · Simon Willison · May 16, 16:45

**标签**: `#CSS`, `#Web Development`, `#Developer Mindset`, `#Front-end`

---

<a id="item-6"></a>
## [Amazon 强制员工达成 AI 使用配额，员工却用它来做无关工作的事](https://futurism.com/artificial-intelligence/amazon-quotas-ai-use) ⭐️ 7.0/10

亚马逊为强制员工使用 AI 而设定配额，却导致员工为达标而将内部 AI 工具用于个人事务，揭示了企业 AI 推广中激励机制与实际效果的脱节。

telegram · zaihuapd · May 17, 01:34

**标签**: `#AI采用`, `#企业文化`, `#员工生产力`, `#AI伦理`, `#工作场所技术`

---

<a id="item-7"></a>
## [无锡将建“Token 工厂”，首批部署 4 台华为昇腾 384 超节点集群](https://wap.eastmoney.com/a/202605173739675157.html) ⭐️ 7.0/10

无锡将与弘信电子合作建设省内首个华为昇腾 384 超节点算力集群，部署 1536 张 AI 卡，以此为基础打造大规模“Token 工厂”。

telegram · zaihuapd · May 17, 06:21

**标签**: `#AI Infrastructure`, `#Huawei Ascend`, `#High-Performance Computing`, `#AI/ML`, `#China Tech`

---