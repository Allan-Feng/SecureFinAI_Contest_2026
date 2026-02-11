---
layout: page
title: Overview
permalink: /
weight: 1
---

<div style="text-align: center; display: flex; width: 100%; justify-content: space-evenly; align-items: center; gap: 1em; padding: 2em">
  <img style="width: 40%;" src="https://github.com/Open-Finance-Lab/SecureFinAI_Contest_2026/blob/main/docs/assets/logos/ieee-logo.png?raw=true" alt="IEEE Logo">
  <img style="width: 30%;" src="https://github.com/Open-Finance-Lab/SecureFinAI_Contest_2026/blob/main/docs/assets/logos/securefinai_cu.png?raw=true" alt="SecureFinAI Lab Logo">
</div>
<div style="text-align: center; display: flex; width: 100%; justify-content: space-evenly; align-items: center; gap: 1em; padding: 2em">
  <img style="width: 30%;" src="https://github.com/Open-Finance-Lab/SecureFinAI_Contest_2026/blob/main/docs/assets/logos/trismik.png?raw=true" alt="Trismik Logo">
  <img style="width: 30%;" src="https://github.com/Open-Finance-Lab/SecureFinAI_Contest_2026/blob/main/docs/assets/logos/vela.png?raw=true" alt="Vela Logo">
</div>

### Thanks to the AI4Finance Foundation open source community for their support.



## Introduction

As AI continues to advance at a fast pace, more FinAI agents are being developed for the finance sector, such as FinRL trading agents [1,2,3], FinGPT agents [4,5] with multimodal capabilities [6], and regulatory reporting agents [7]. The **Secure FinAI Contest 2026** encourages the development of FinAI agents based on the frameworks FinRL [2,3] and FinGPT [4].


We design four tasks. These challenges allow contestants to participate in various financial tasks and contribute to secure finance using state-of-the-art technologies with privacy-preserving and verifiable computation frameworks. We welcome students, researchers, and engineers who are passionate about finance, machine learning, and security to partake in the contest.

## Tasks
Each team can choose to participate in one or more tasks. The prizes will be awarded for each task.

### Task I: Adaptive Evaluation and Benchmarking Suite for Financial LLMs and Agents
This task focuses on benchmarking Financial Large Language Models (FinLLMs) and agents using an **adaptive testing pipeline**. Unlike traditional benchmarks, the adaptive pipeline partitions the test set into difficulty levels and dynamically selects test items based on model performance. This enables more efficient evaluation while preserving rigour. Participants are expected to submit models that can handle a diverse range of financial reasoning and comprehension tasks, optimised for both accuracy and inference efficiency.

**Datasets:** We utilize the standard evaluation suite referenced in BloombergGPT, integrated into the adaptive framework. This includes **FPB** (sentiment analysis), **FiQA-SA** (aspect-based sentiment), **Headlines** (market news classification), **NER** (entity recognition), and **ConvFinQA** (conversational financial Q&A).

### Task II: Reliable Agentic FinSearch
**Task Description:**
Numerical accuracy is critical for financial tasks. On a small curated question set, we manually compared [Agentic FinSearch](https://chromewebstore.google.com/detail/agentic-finsearch/aehnlpneoncdfioafiigiljmbghccami?hl=en&authuser=0) (a google chrome extension) with [Perplexity](https://www.perplexity.ai/) (with financial support, [Link](https://www.perplexity.ai/finance)). Our Agentic FinSearch outperforms Perplexity substantially! 

This task invites teams to try our [Agentic FinSearch](https://chromewebstore.google.com/detail/agentic-finsearch/aehnlpneoncdfioafiigiljmbghccami?hl=en&authuser=0) demo and test your LLMs or agents on a large question set. Accurate retrieval of real-time financial data is a core infrastructure for building FinAgents. Higher numerical accuracy, lower hallucination & misinformation, and air-gapped deployment are three features. We encourage you to build powerful Agentic FinSearch agents. 

<div style="text-align: center;">
  <img src="https://github.com/Open-Finance-Lab/SecureFinAI_Contest_2026/blob/main/docs/assets/pictures/task_2.png?raw=true" alt="Fig. 1. Agentic FinSearch on Yahoo Finance" style="width: 80%;">
  <p>Fig. 1. Agentic FinSearch on Yahoo Finance.</p>
</div>

**Question sets for benchmarking:**
* Real-time retrieval of market data
* Simple lookup of historical data
* Complex computations over historical data
* Hallucinations and misinformation


### Task III: Prediction Market Arbitrage
This task focuses on developing trading agents that identify and execute arbitrage opportunities across two prediction markets, Kalshi and Polymarket, for a series of sports events with binary options. Models may incorporate sentiment signals in addition to market data to anticipate market moves when new information changes expectations during a game. Evaluation will be conducted via paper trading, where agents perform simulated trading on real market data without real capital.

**Datasets:**
*   **Kalshi Data**: Market metadata and public market snapshots collected via the Kalshi API, with optional WebSocket streams for real-time updates including order book changes, public trades, and price/ticker movements. 

Kalshi API Docs — https://docs.kalshi.com/

*   **Polymarket Data**: Market metadata from Polymarket’s public Gamma API (series, events, markets, and outcome identifiers), paired with real-time updates from the CLOB WebSocket market feed to track live pricing and liquidity. 

Polymarket Developer Docs — https://docs.polymarket.com/quickstart/overview

*   **Sentiment Data**: Sports news collected from RSS feeds across multiple sources, including 
breaking headlines and alerts, injury and lineup updates, and other game-related developments 
that can be used as sentiment inputs. 

### Task IV: AI for [Venture Capital](https://www.vcbench.com/) - Prediction of Startup Success 
This task tests the ability of Large Language Models to act as Venture Capitalists by predicting the potential success of early-stage startups. Using the **VCBench** dataset, which consists of anonymized founder profiles, participants must predict whether a startup will achieve a significant liquidity event (IPO, M&A >$500M, or high-tier funding).

**Goal & Constraints:**
*   **Objective:** Predict the binary "Success" label for given founder profiles.
*   **Optimization:** Participants are encouraged to optimize input templates and output extraction methods alongside model fine-tuning.
*   **Metric:** F1-Score.

### Task V: Agentic Trading
**Task Overview**
This task focuses on developing LLM agents for quantitative trading in a real-time paper trading setting. It formulates trading as a **reasoning-to-action** problem, where agents integrate real-time signals such as **prices, newsflow, and asset-specific fundamentals** and make trading actions. Evaluation will be conducted via paper trading on an Alpaca paper trading account, with metrics emphasizing profitability and risk.

**Datasets**
Participants may fetch historical market data from Alpaca Market Data API:
* **Stock**: [https://alpaca.markets/sdks/python/api_reference/data/stock.html](https://alpaca.markets/sdks/python/api_reference/data/stock.html)
* **Crypto**: [https://alpaca.markets/sdks/python/api_reference/data/crypto.html](https://alpaca.markets/sdks/python/api_reference/data/crypto.html)

**Evaluation**
Participants will create an Alpaca paper trading account, run their agent to trade during the evaluation period, and submit required files at the end of the evaluation period.
* **Time Period:** **April 20 – May 1**.
* **Initial Capital:** Each account starts with a fixed capital of **$100,000**.

**What to Submit**
* an **orders JSONL** file (time-ordered trading actions),
* a **daily equity CSV** file,
* a **snapshot of the Alpaca portfolio value** at the end of the evaluation period.

**Metrics**
* **Primary:** Cumulative Return (**CR**)
* **Secondary:** Sharpe Ratio (**SR**), Maximum Drawdown (**MD**), Daily Volatility (**DV**), Annualized Volatility (**AV**)

> *A single paper trading account trade asset from **only one market type: stock/crypto**. Create two accounts if you are participating in both the stock and crypto tracks. Stock and crypto tracks are evaluated separately.*

**Why this matters**
AI agents have seen rapid development and have been applied to financial trading tasks. Recent work such as Agent Market Arena (AMA) by FinAI and Alpha Arena by NoF1 introduces arena-style benchmarks that demonstrate the capability of AI agents to trade in market environments under standardized settings. While these benchmarks focus on comparing agent performance within fixed interfaces, this task emphasizes flexibility and agent design. Participants are encouraged to build their own trading agents, including data, agent architecture, and trading strategy, and evaluate them through live paper trading on Alpaca for stock or cryptocurrency markets.


<p style="font-size: 14px;">
[1] Wang, Keyi, et al. "FinRL Contests: Data‐Driven Financial Reinforcement Learning Agents for Stock and Crypto Trading." <em>Artificial Intelligence for Engineering</em> (2025). [<a href="https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/aie2.12004">IET</a>] [<a href="https://arxiv.org/abs/2504.02281">arXiv</a>]
</p>
<p style="font-size: 14px;">
[2] Liu, Xiao-Yang, et al. "Finrl-meta: Market environments and benchmarks for data-driven financial reinforcement learning." <em>Advances in Neural Information Processing Systems</em> 35 (2022): 1835-1849. [<a href="https://papers.neurips.cc/paper_files/paper/2022/file/0bf54b80686d2c4dc0808c2e98d430f7-Paper-Datasets_and_Benchmarks.pdf">NeurIPS</a>]
</p>
<p style="font-size: 14px;">
[3] Liu, Xiao-Yang, et al. "Fingpt: Democratizing internet-scale data for financial large language models." <em>arXiv preprint</em> arXiv:2307.10485 (2023). [<a href="https://arxiv.org/abs/2307.10485">arXiv</a>]
</p>
<p style="font-size: 14px;">
[4] Lin, Shengyuan, et al. "Evaluation and Benchmarking Suite for Financial Large Language Models and Agents." NeurIPS 2025 Workshop on Evaluating the Evolving LLM Lifecycle: Benchmarks, Emergent Abilities, and Scaling. [<a href="https://openreview.net/pdf?id=sSY4h3MFUB">NeurIPS 2025 Workshop</a>]
</p>
<p style="font-size: 14px;">
[5] Yan Wang, Keyi Wang, Shanshan Yang, Jaisal Patel, Jeff Zhao, Fengran Mo, Xueqing Peng, Lingfei Qian, Jimin Huang, Guojun Xiong, Xiao-Yang Liu, Jian-Yun Nie. "FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs." <em>arXiv preprint</em> arXiv:2510.08886 (2025). [<a href="https://arxiv.org/abs/2510.08886">arXiv</a>]
</p>
<p style="font-size: 14px;">
[6] Yan Wang, Lingfei Qian, Xueqing Peng, Yang Ren, Keyi Wang, Yi Han, Dongji Feng, Fengran Mo, Shengyuan Lin, Qinchuan Zhang, Kaiwen He, Chenri Luo, Jianxing Chen, Junwei Wu, Chen Xu, Ziyang Xu, Jimin Huang, Guojun Xiong, Xiao-Yang Liu, Qianqian Xie, Jian-Yun Nie. "FinTagging: Benchmarking LLMs for Extracting and Structuring Financial Information." <em>arXiv preprint</em> arXiv:2505.20650 (2025). [<a href="https://arxiv.org/abs/2505.20650">arXiv</a>]

## Contact
Contact email: [finrlcontest@gmail.com](mailto:finrlcontest@gmail.com)

Contestants can communicate any questions on 
* [Discord](https://discord.gg/dJY5cKzmkv).




