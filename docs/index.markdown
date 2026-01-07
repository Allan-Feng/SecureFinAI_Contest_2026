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

### Thanks to the AI4Finance Foundation open source community for their support.



## Introduction

As AI continues to advance at a fast pace, more FinAI agents are being developed for the finance sector, such as FinRL trading agents [1,2,3], FinGPT agents [4,5] with multimodal capabilities [6], and regulatory reporting agents [7]. The **Secure FinAI Contest 2026** encourages the development of FinAI agents based on the frameworks FinRL [2,3] and FinGPT [4].


We design four tasks. These challenges allow contestants to participate in various financial tasks and contribute to secure finance using state-of-the-art technologies with privacy-preserving and verifiable computation frameworks. We welcome students, researchers, and engineers who are passionate about finance, machine learning, and security to partake in the contest.

## Tasks
Each team can choose to participate in one or more tasks. The prizes will be awarded for each task.

### Task I: Adaptive Evaluation and Benchmarking Suite for Financial LLMs
This task focuses on benchmarking Financial Large Language Models (FinLLMs) using **Trismik’s adaptive testing pipeline**. Unlike traditional benchmarks, Trismik pipeline split the testing set into different difficulty levels, and can dynamically select test items based on the model's performance. Therefore evaluation is efficient. Participants are expected to submit models that can handle a diverse range of financial reasoning and understanding tasks, optimized for both accuracy and inference efficiency.

**Datasets:** We utilize the standard evaluation suite referenced in BloombergGPT, integrated into the adaptive framework. This includes **FPB** (sentiment analysis), **FiQA-SA** (aspect-based sentiment), **Headlines** (market news classification), **NER** (entity recognition), and **ConvFinQA** (conversational financial Q&A).

### Task II: Reliable Agentic FinSearch
This task benchmarks the reliability of financial search agents, specifically focusing on eliminating hallucinations and ensuring numerical precision. Participants are expected to finetune models and design agent pipelines that will be evaluated on their ability to retrieve and process financial data without errors.

**Datasets:**
*   **Hallucination Evaluation**: A 35-question set spanning real-time data, company fundamentals, and trading calculations. Ground truth is validated against Yahoo Finance.
*   **Numerical & Temporal Accuracy**: A 24-question set derived from the **FinSearchComp** benchmark, testing real-time retrieval, historical lookup, and complex computation capabilities. Models are scored on exact match accuracy against expert-verified answers.

### Task III: FinRL-DeepSeek for Stock Trading
This task is about developing automated stock trading agents trained on stock prices and financial news data by combining reinforcement learning and large language models (LLMs). Participants can build upon the [FinRL-DeepSeek project](https://github.com/benstaf/FinRL_DeepSeek) (e.g., with new prompts, new ways to inject LLM-processed news signals into the RL agent, new RL algorithms like GRPO) or explore more computationally intensive directions, such as adapting variants of the DeepSeek R1 training method to this stock trading task

**Datasets:**
The [Financial News and Stock Price Integration Dataset (FNSPID)](https://huggingface.co/datasets/Zihan1004/FNSPID) [6] comprises stock prices and 15 million time-aligned financial news records for Nasdaq companies, covering the period from 1999 to 2023. The processed training dataset based on the FNSPID will be provided. Participants are also encouraged to utilize publicly available data, such as Twitter, or develop scraping/API AI agents for this purpose. Some teams can choose to focus their submission on improving the dataset, others on improving trading agents.



### Task IV: AI for Venture Capital - Prediction of Startup Success 
This task tests the ability of Large Language Models to act as Venture Capitalists by predicting the potential success of early-stage startups. Using the **VCBench** dataset, which consists of anonymized founder profiles, participants must predict whether a startup will achieve a significant liquidity event (IPO, M&A >$500M, or high-tier funding).

**Goal & Constraints:**
*   **Objective:** Predict the binary "Success" label for given founder profiles.
*   **Model Limits:** Participants must use and fine-tune models with **<14B parameters**.
*   **Optimization:** Participants are encouraged to optimize input templates and output extraction methods alongside model fine-tuning.
*   **Metric:** F1-Score.


<p style="font-size: 14px;">
[1] Wang, Keyi, et al. "FinRL Contests: Data‐Driven Financial Reinforcement Learning Agents for Stock and Crypto Trading." <em>Artificial Intelligence for Engineering</em> (2025). [<a href="https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/aie2.12004">IET</a>] [<a href="https://arxiv.org/abs/2504.02281">arXiv</a>]
</p>
<p style="font-size: 14px;">
[2] Liu, Xiao-Yang, et al. "Finrl-meta: Market environments and benchmarks for data-driven financial reinforcement learning." <em>Advances in Neural Information Processing Systems</em> 35 (2022): 1835-1849. [<a href="https://papers.neurips.cc/paper_files/paper/2022/file/0bf54b80686d2c4dc0808c2e98d430f7-Paper-Datasets_and_Benchmarks.pdf">NeurIPS</a>]
</p>
<p style="font-size: 14px;">
[3] Liu, Xiao-Yang, et al. "FinRL: A deep reinforcement learning library for automated stock trading in quantitative finance." <em>arXiv preprint</em> arXiv:2011.09607 (2020). [<a href="https://arxiv.org/abs/2011.09607">arXiv</a>] [<a href="https://neurips.cc/virtual/2020/19841">NeurIPS 2020</a>]
</p>
<p style="font-size: 14px;">
[4] Liu, Xiao-Yang, et al. "Fingpt: Democratizing internet-scale data for financial large language models." <em>arXiv preprint</em> arXiv:2307.10485 (2023). [<a href="https://arxiv.org/abs/2307.10485">arXiv</a>]
</p>
<p style="font-size: 14px;">
[5] Tian, Felix, et al. "Customized fingpt search agents using foundation models." <em>Proceedings of the 5th ACM International Conference on AI in Finance</em>. 2024. [<a href="https://dl.acm.org/doi/10.1145/3677052.3698637">ACM</a>]
</p>
<p style="font-size: 14px;">
[6] Yanglet, Xiao-Yang Liu, Yupeng Cao, and Li Deng. "Multimodal financial foundation models (mffms): Progress, prospects, and challenges." <em>arXiv preprint</em> arXiv:2506.01973 (2025). [<a href="https://www.arxiv.org/abs/2506.01973">arXiv</a>]
</p>
<p style="font-size: 14px;">
[7] Han, Shijie, et al. "Xbrl agent: Leveraging large language models for financial report analysis." <em>Proceedings of the 5th ACM International Conference on AI in Finance</em>. 2024. [<a href="https://dl.acm.org/doi/abs/10.1145/3677052.3698614">ACM</a>]
</p>
<p style="font-size: 14px;">
[8] Peng, Xueqing, et al. "MultiFinBen: A Multilingual, Multimodal, and Difficulty-Aware Benchmark for Financial LLM Evaluation." <em>arXiv preprint</em> arXiv:2506.14028 (2025). [<a href="https://arxiv.org/abs/2506.14028">arXiv</a>]
</p>


## Contact
Contact email: [finrlcontest@gmail.com](mailto:finrlcontest@gmail.com)

Contestants can communicate any questions on 
* [Discord](https://discord.gg/dJY5cKzmkv).




