"""
Task 5 Main Script - Agentic Trading

This script runs the trading simulation.
"""

from data_loader import load_market_data
from example_agent import ExampleAgent
import json
from datetime import datetime

def main():
    # 1. Load market data
    print("Loading market data...")
    eth_data = load_market_data("ETH", "2024-01-01")
    msft_data = load_market_data("MSFT", "2024-01-01")
    
    # 2. Initialize agent
    agent = ExampleAgent()
    
    # 3. Generate decisions for last 5 days (demo)
    results = []
    
    for asset, data in [("ETH", eth_data), ("MSFT", msft_data)]:
        if len(data) < 5:
            continue
        recent_data = data.tail(5)
        decision = agent.decide(recent_data)
        
        results.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "asset": asset,
            "action": decision["action"],
            "rationale": decision["rationale"]
        })
    
    # 4. Save results
    with open("submission.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    
    print(f"\nSaved {len(results)} decisions to submission.jsonl")
    for r in results:
        print(f"  {r['asset']}: {r['action']}")

if __name__ == "__main__":
    main()
