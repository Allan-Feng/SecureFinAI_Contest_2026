# Task V: Agentic Trading

**Why this matters:** AI agents have seen rapid development and have been applied to financial trading tasks. Recent work such as Agent Market Arena (AMA) by FinAI and Alpha Arena by NoF1 introduces arena-style benchmarks that demonstrate the capability of AI agents to trade in market environments under standardized settings. While these benchmarks focus on comparing agent performance within fixed interfaces, this task emphasizes flexibility and agent design. Participants are encouraged to build their own trading agents, including data, agent architecture, and trading strategy, and evaluate them through live paper trading on Alpaca for stock or cryptocurrency markets.

This task focuses on developing LLM agents using OpenClaw for quantitative trading in a real-time paper trading setting. It formulates trading as a **reasoning-to-action** problem, where OpenClaw agents integrate real-time signals such as **prices, newsflow, and asset-specific fundamentals** and make trading actions. Evaluation will be conducted via paper trading on an Alpaca paper trading account, with metrics emphasizing profitability and risk.

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
