from datasets import load_dataset
import pandas as pd
import json
import os

def load_finsearch_data(split='test'):
    """
    Load the FinSearchComp dataset from HuggingFace.
    
    Args:
        split (str): 'test', 'validation', or 'train'. Note: The challenge typically uses 'test' without labels.
                     If 'validation' is available with labels, it can be used for dev.
    
    Returns:
        List[Dict]: A list of dictionary items containing questions.
    """
    print(f"Loading FinSearchComp dataset (split={split})...")
    try:
        # Load from HuggingFace
        dataset = load_dataset("ByteSeedXpert/FinSearchComp", split=split)
        
        # Convert to list of dicts for easier handling
        data_list = []
        for item in dataset:
            # Normalize keys if necessary, assuming HF dataset structure
            entry = {
                "question_id": item.get("id", str(item.get("index", ""))),
                "question": item.get("question", ""),
                # Ground truth might not be present in test set
                "answer": item.get("answer", None), 
                "task_type": item.get("task_type", "unknown") 
            }
            data_list.append(entry)
            
        print(f"Successfully loaded {len(data_list)} items.")
        return data_list

    except Exception as e:
        print(f"Error loading dataset: {e}")
        # Fallback to local mock data for demonstration if HF download fails
        print("Falling back to mock data for demonstration.")
        return [
            {"question_id": "mock_1", "question": "What was the revenue of Apple Inc. in 2022?", "task_type": "historical"},
            {"question_id": "mock_2", "question": "Current price of Bitcoin in USD?", "task_type": "real-time"}
        ]

if __name__ == "__main__":
    # Test the loader
    data = load_finsearch_data()
    print("Sample item:", data[0] if data else "No data")
    
    # Save a sample for inspection
    with open("sample_data.json", "w") as f:
        json.dump(data[:5], f, indent=2)
    print("Saved sample_data.json")
