# Task 3 Starter Kit: Prediction Market Arbitrage

This starter kit provides a template for the **Prediction Market Arbitrage** task. It demonstrates the expected agent interface for trading across Kalshi and Polymarket.

> **IMPORTANT**: This is only an example. You should design and implement your own agent for submission.

## 📂 Directory Structure

```
Task_3_tutorial/
├── README.md               # This file
├── Task_3_Description.md   # Task description and dataset info
├── requirements.txt        # Python dependencies (add your own)
├── example_agent.py        # Template agent (implement your own logic)
└── main.py                 # Main script to run paper trading simulation
```

## 🚀 Setup

```bash
cd Tutorials/Task_3_tutorial
pip install -r requirements.txt
```

## ▶️ Running

```bash
python main.py
```

## 🛠 Developing Your Agent

This is only an example. You should design and implement your own agent with:
- Your own market data fetching strategy (Kalshi API, Polymarket CLOB API)
- Your own arbitrage detection algorithm
- Your own order execution logic
- Your own risk management

## 📚 API Resources

- **Kalshi API**: https://trading-api.readme.io/docs
- **Polymarket CLOB API**: https://docs.polymarket.com
- **Polymarket Python SDK**: https://github.com/Polymarket/py-clob-client
