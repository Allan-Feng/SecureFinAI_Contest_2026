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
This task benchmarks the reliability of financial search agents, specifically focusing on eliminating hallucinations and ensuring numerical precision. Participants are expected to finetune models and design agent pipelines that will be evaluated on their ability to retrieve and process financial data without errors.

**Datasets:**
*   **The FinSearchComp benchmark** consists of 635 financial questions (e.g., “What was the annual inflation rate in Australia in 2022?”) paired with their ground-truth answers (e.g., “6.6%,” allowing for minor rounding errors). These questions are designed to evaluate an agent’s proficiency of searching and reasoning in terms of numerical and temporal accuracy. The benchmark covers three types of tasks: (1) real-time retrieval of numerical data (Task 1), (2) simple lookup of historical data (Task 2), and (3) complex computation over historical data (Task 3). The dataset includes 244 questions for Task 1, 219 for Task 2, and 172 for Task 3.
*   The link of benchmark: https://huggingface.co/datasets/ByteSeedXpert/FinSearchComp


### Task III: Prediction Market Arbitrage
This task focuses on developing trading agents that identify and execute arbitrage opportunities across two prediction markets, Kalshi and Polymarket, for a series of sports events with binary options. Models may incorporate sentiment signals in addition to market data to anticipate market moves when new information changes expectations during a game. Evaluation will be conducted via paper trading, where agents are tested on historical or simulated market data without real capital.

**Datasets:**
*   **Kalshi Real-Time Sports Market Feed**: Market metadata and public market snapshots combined with WebSocket streams for real-time updates on the order book, public trades, and price or ticker changes.
*   **Polymarket Real-Time Sports Market Feed**: Market metadata from the public Gamma API with market and outcome identifiers, paired with real-time updates from the CLOB WebSocket market feed to track live pricing and liquidity.
*   **Sports Sentiment Signal Feed**: APIs for sports news and social media discussion, including headlines and alerts, injury and lineup updates, and player performance as sentiment inputs.

### Task IV: AI for [Venture Capital](https://www.vcbench.com/) - Prediction of Startup Success 
This task tests the ability of Large Language Models to act as Venture Capitalists by predicting the potential success of early-stage startups. Using the **VCBench** dataset, which consists of anonymized founder profiles, participants must predict whether a startup will achieve a significant liquidity event (IPO, M&A >$500M, or high-tier funding).

**Goal & Constraints:**
*   **Objective:** Predict the binary "Success" label for given founder profiles.
*   **Optimization:** Participants are encouraged to optimize input templates and output extraction methods alongside model fine-tuning.
*   **Metric:** F1-Score.

### Task V: Agentic Trading
This task focuses on developing models for real-time financial decision making under uncertain conditions. It formulates trading as a reasoning-to-action problem, where agents must integrate time-varying signals such as prices, newsflow, and asset-specific fundamentals, make a discrete trading decision, and justify that decision with evidence-grounded rationales. Evaluation emphasizes both profitability and risk, and is conducted under a leakage-resistant, time-ordered protocol.

**Datasets:**

*   **ETH (Crypto)**: A dataset with daily snapshots starting from 2025-08-01 and updated daily. It includes price data, synthesized newsflow, and momentum annotations, as well as fundamental information where applicable.
*   **MSFT (Equity)**: A dataset with daily snapshots starting from 2025-08-01 and updated daily. It includes price data, newsflow, momentum labels, and relevant financial filings for equity assets.

**Objective & Constraints:**
* Action: Models must output a discrete trading action (Buy, Hold, or Sell) based on the daily market context.
* Rationale: Models must provide a concise textual rationale (maximum 50 words) that justifies the decision using evidence from the available inputs.
* Evaluation Protocol: Evaluation follows a live, time-ordered setup with fixed daily submission deadlines. Teams may submit either daily decisions with verifiable timestamps or reproducible code that deterministically generates decisions from the provided inputs.

**Metric:**
* Primary: Cumulative Return (CR) over the evaluation horizon.
* Secondary: Sharpe Ratio (SR), Maximum Drawdown (MD), Daily Volatility (DV), and Annualized Volatility (AV), capturing profitability, stability, and risk control.

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




