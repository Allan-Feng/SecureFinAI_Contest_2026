# Task III: Prediction Market Arbitrage 
This task focuses on developing trading agents that identify and execute arbitrage opportunities 
across two prediction markets, Kalshi and Polymarket, for a series of sports events with binary 
options. Models may incorporate sentiment signals in addition to market data to anticipate 
market moves when new information changes expectations during a game. Evaluation will be 
conducted via paper trading, where agents perform simulated trading on real market data 
without real capital. 
Datasets:  
Kalshi Data: Market metadata and public market snapshots collected via the Kalshi API, with 
optional WebSocket streams for real-time updates including order book changes, public trades, 
and price or ticker movements. 
Kalshi API Docs — https://docs.kalshi.com/ 
Polymarket Data: Market metadata from Polymarket’s public Gamma API (series, events, 
markets, and outcome identifiers), paired with real-time updates from the CLOB WebSocket 
market feed to track live pricing and liquidity. 
Polymarket Developer Docs — https://docs.polymarket.com/quickstart/overview 
Sentiment Data: Sports news collected from RSS feeds across multiple sources, including 
breaking headlines and alerts, injury and lineup updates, and other game-related developments 
that can be used as sentiment inputs.

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
