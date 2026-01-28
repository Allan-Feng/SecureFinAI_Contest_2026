# Task V: Agentic Trading

**Description**
This task focuses on developing models for real-time financial decision making under uncertain conditions. It formulates trading as a reasoning-to-action problem, where agents must integrate time-varying signals such as prices, newsflow, and asset-specific fundamentals, make a discrete trading decision, and justify that decision with evidence-grounded rationales. Evaluation emphasizes both profitability and risk, and is conducted under a leakage-resistant, time-ordered protocol.

**Objective & Constraints**
*   **Action**: Models must output a discrete trading action (Buy, Hold, or Sell) based on the daily market context.
*   **Rationale**: Models must provide a concise textual rationale (maximum 50 words) that justifies the decision using evidence from the available inputs.
*   **Evaluation Protocol**: Evaluation follows a live, time-ordered setup with fixed daily submission deadlines.

**Datasets**

*   **ETH (Crypto)**: Daily snapshots starting from 2025-08-01, updated daily.
    - Price data (OHLCV)
    - Synthesized newsflow
    - Momentum annotations
    - **Data Source**: Provided by organizers (TBA)
    
*   **MSFT (Equity)**: Daily snapshots starting from 2025-08-01, updated daily.
    - Price data (OHLCV)
    - Newsflow
    - Momentum labels
    - Relevant financial filings
    - **Data Source**: Provided by organizers (TBA)

**Publicly Available Data Sources (for reference)**
- **Yahoo Finance API**: Historical price data via `yfinance` Python package
- **CoinGecko API**: Crypto price data (free tier available)
- **Alpha Vantage**: Stock and crypto data (free API key required)
- **News APIs**: NewsAPI, Finnhub, Alpha Vantage News Sentiment

**Metrics**
*   **Primary**: Cumulative Return (CR) over the evaluation horizon.
*   **Secondary**: Sharpe Ratio (SR), Maximum Drawdown (MD), Daily Volatility (DV), and Annualized Volatility (AV).

**Submission Requirements**

Participants must submit:
1. **GitHub Repository**: Public or private repo containing your agent code
2. **HuggingFace Model Link** (if applicable): Any fine-tuned models uploaded to HuggingFace Hub
3. **Run Script**: A script (e.g., `run.py`) that we can execute to generate daily trading decisions
4. **Requirements File**: `requirements.txt` with all dependencies

**Output Format**:
Daily submissions with:
- `date`: Trading date
- `asset`: ETH or MSFT
- `action`: Buy, Hold, or Sell
- `rationale`: Text justification (max 50 words)

We will evaluate your submission by running your agent on the evaluation data.
