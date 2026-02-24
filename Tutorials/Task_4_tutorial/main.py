"""
Task 4 Main Script - AI for Venture Capital

This script runs inference on the VCBench dataset.
"""

from datetime import datetime

from data_loader import read_train_data, read_test_data, read_dev_data
from evaluate import get_F_score
import json
from example_model import LLMForVC
import pandas as pd

def testModel():
    # Run inference on both train and test sets
    train_data = read_train_data()
    train_data = train_data  # Use a subset for quick testing
    agent = LLMForVC() 
    
    inputs = [item["input"] for item in train_data]
    outputs = agent.batch_predict(inputs)
    
    results = []
    for output, profile in zip(outputs, train_data):

        results.append({
            "founder_uuid": profile.get("uuid"),
            "input": profile.get("input"),
            "prediction": output
        })
    
    labels = [item["output"] for item in train_data]
    F_score, acc = get_F_score(outputs, labels)
    print(f"F-score: {F_score}, Accuracy: {acc}")
    
    
    

def dev_prediction():
    dev_data = read_dev_data()
    inputs = [item["input"] for item in dev_data]
    agent = LLMForVC() 
    
    outputs = agent.batch_predict(inputs)
    
    results = []
    for output, profile in zip(outputs, dev_data):

        results.append({
            "founder_uuid": profile.get("uuid"),
            "input": profile.get("input"),
            "prediction": output
        })
    
    df = pd.DataFrame(results)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    out_file = f"results/dev_predictions_{timestamp}.csv"
    df.to_csv(out_file, index=False)
    print(f"\n✅ Saved dev predictions to {out_file}")
    

def main():
    dev_prediction()
    
    
if __name__ == "__main__":
    main()
