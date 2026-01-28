# Task III: Prediction Market Arbitrage

**Description**
This task focuses on developing trading agents that identify and execute arbitrage opportunities across two prediction markets, Kalshi and Polymarket, for a series of sports events with binary options. Models may incorporate sentiment signals in addition to market data to anticipate market moves when new information changes expectations during a game. Evaluation will be conducted via paper trading, where agents are tested on historical or simulated market data without real capital.

**Datasets**

*   **Kalshi Real-Time Sports Market Feed**: Market metadata and public market snapshots combined with WebSocket streams for real-time updates on the order book, public trades, and price or ticker changes.
    - **API Documentation**: [https://trading-api.readme.io/docs](https://trading-api.readme.io/docs)
    - **REST API + WebSocket** for real-time market data
    - Requires Kalshi account for API key

*   **Polymarket Real-Time Sports Market Feed**: Market metadata from the public Gamma API with market and outcome identifiers, paired with real-time updates from the CLOB WebSocket market feed to track live pricing and liquidity.
    - **API Documentation**: [https://docs.polymarket.com](https://docs.polymarket.com)
    - **CLOB API**: Central Limit Order Book for trading
    - **Gamma API**: Market discovery and metadata
    - **Python SDK**: [py-clob-client](https://github.com/Polymarket/py-clob-client)

*   **Sports Sentiment Signal Feed**: APIs for sports news and social media discussion, including headlines and alerts, injury and lineup updates, and player performance as sentiment inputs.
    - Participants may use any sports news API or social media API of their choice
    - Examples: ESPN API, Twitter/X API, Reddit API, sports news RSS feeds

**Key Capabilities Required**
- Real-time market data processing
- Arbitrage opportunity detection
- Order execution logic
- Risk management
- Sentiment signal integration (optional)

**Evaluation**
Paper trading simulation with historical market data. Metrics include:
- Total profit/loss
- Sharpe ratio
- Maximum drawdown
- Number of successful arbitrage trades

**Submission Requirements**

Participants must submit:
1. **GitHub Repository**: Public or private repo containing your trading agent code
2. **HuggingFace Model Link** (if applicable): Any fine-tuned models uploaded to HuggingFace Hub
3. **Run Script**: A script (e.g., `run.py`) that we can execute to run your agent in paper trading simulation
4. **Requirements File**: `requirements.txt` with all dependencies

We will evaluate your submission by running your agent on historical market data.
