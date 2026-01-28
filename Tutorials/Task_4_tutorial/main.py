"""
Task 4 Main Script - AI for Venture Capital

This script runs inference on the VCBench dataset.
"""

from data_loader import load_vcbench
from example_agent import ExampleAgent
import json

def main():
    # 1. Load data
    data = load_vcbench()
    
    # 2. Initialize model
    agent = ExampleAgent()
    
    # 3. Run inference
    results = []
    for i, profile in enumerate(data):
        if i >= 5:  # Limit for demo
            break
        prediction = agent.predict(profile)
        results.append({
            "founder_id": profile.get("founder_id", str(i)),
            "prediction": prediction["prediction"],
            "confidence": prediction["confidence"]
        })
    
    # 4. Save results
    with open("submission.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    
    print(f"\nSaved {len(results)} predictions to submission.jsonl")

if __name__ == "__main__":
    main()
