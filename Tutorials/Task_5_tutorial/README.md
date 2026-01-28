# Task 5 Starter Kit: Agentic Trading

This starter kit provides a template for the **Agentic Trading** task.

> **IMPORTANT**: This is only an example. You should design and implement your own trading agent for submission.

## 📂 Directory Structure

```
Task_5_tutorial/
├── README.md               # This file
├── Task_5_Description.md   # Task description and dataset info
├── requirements.txt        # Python dependencies (add your own)
├── data_loader.py          # Script to load market data
├── example_agent.py        # Template agent (implement your own)
└── main.py                 # Main script to run trading simulation
```

## 🚀 Setup

```bash
cd Tutorials/Task_5_tutorial
pip install -r requirements.txt
```

## ▶️ Running

```bash
python main.py
```

## 🛠 Developing Your Agent

This is only an example. You should design and implement your own agent with:
- Your own market data processing
- Your own signal generation (technical, fundamental, sentiment)
- Your own decision-making logic (LLM-based or rule-based)
- Your own risk management

## 📚 Data Sources

Competition data will be provided by organizers. For development, you may use:
- **yfinance**: `pip install yfinance` for historical stock/crypto data
- **CoinGecko API**: Free crypto price data
- **Alpha Vantage**: Free tier with API key
