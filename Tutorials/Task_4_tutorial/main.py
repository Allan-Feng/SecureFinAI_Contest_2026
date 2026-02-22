"""
Task 4 Main Script - AI for Venture Capital

This script runs inference on the VCBench dataset.
"""

from data_loader import read_train_data, read_test_data, read_dev_data
from evaluate import get_F_score
import json
from example_model import LLMForVC
def testModel():
    # Run inference on both train and test sets
    train_data = read_train_data()
    test_data = read_test_data()
    
    agent = LLMForVC()  # Initialize your model/agent here
    
    outputs = agent.batch_predict(train_data["input"])
    
    results = []
    for output, profile in zip(outputs, train_data):

        results.append({
            "founder_uuid": profile.get("uuid"),
            "input": profile.get("input"),
            "prediction": output
        })
    
    
    F_score, acc = get_F_score(outputs, train_data["output"])
    print(f"F-score: {F_score}, Accuracy: {acc}")
    
    
    
    
    with open("train_submission.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    
    

def main():
    testModel()
    
    
if __name__ == "__main__":
    main()
