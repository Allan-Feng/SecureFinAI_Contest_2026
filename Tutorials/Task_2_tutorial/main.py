from data_loader import load_finsearch_data
from example_agent import ExampleAgent
import json
import tqdm
import os

def main():
    # 1. Load Data
    # For starter kit, we default to a small sample or 'test' split
    # Since 'test' might not have labels, we don't evaluate here, just generate submission.
    data = load_finsearch_data(split='test') 
    
    # 2. Initialize Agent
    agent = ExampleAgent()
    
    # 3. Predict Loop
    results = []
    print("Running inference...")
    for item in tqdm.tqdm(data):
        qid = item['question_id']
        question = item['question']
        
        try:
            answer, evidence = agent.predict(question)
        except Exception as e:
            print(f"Error processing {qid}: {e}")
            answer = "Error"
            evidence = ""
            
        result_item = {
            "question_id": qid,
            "answer": answer,
            "evidence": evidence
        }
        results.append(result_item)
        
    # 4. Save Submission
    output_file = "submission.jsonl"
    with open(output_file, "w") as f:
        for res in results:
            f.write(json.dumps(res) + "\n")
            
    print(f"Submission saved to {output_file}")

if __name__ == "__main__":
    main()
