"""
Task 4 Data Loader - VCBench Dataset

Loads the VCBench dataset from HuggingFace.
"""

import os
import pandas as pd
from datetime import datetime
from typing import Optional
import json
def read_train_data():
    

    founders_data = pd.read_csv("VCbench_train.csv")
    data_list = [row.to_dict() for _, row in founders_data.iterrows()]

    processed_data = [{"uuid": item["founder_uuid"], "input": item["anonymised_prose"], "output": str(item["success"])} for item in data_list[:3000]]

    print(f"Total data size: {len(processed_data)}")
    print(f"Sample data: {processed_data[-1]}")
    print(f"positive data: {sum([1 for item in processed_data if item['output']=='1'])}")
    print(f"negative data: {sum([1 for item in processed_data if item['output']=='0'])}")
    
    return processed_data


def read_test_data():
    

    founders_data = pd.read_csv("VCbench_train.csv")
    data_list = [row.to_dict() for _, row in founders_data.iterrows()]

    processed_data = [{"input": item["anonymised_prose"], "output": str(item["success"])} for item in data_list[3000:]]

    print(f"Total data size: {len(processed_data)}")
    print(f"Sample data: {processed_data[-1]}")
    print(f"positive data: {sum([1 for item in processed_data if item['output']=='1'])}")
    print(f"negative data: {sum([1 for item in processed_data if item['output']=='0'])}")
    
    return processed_data

def read_dev_data():
    

    founders_data = pd.read_csv("VCbench_dev.csv")
    data_list = [row.to_dict() for _, row in founders_data.iterrows()]

    processed_data = [{"uuid": item["founder_uuid"], "input": item["anonymised_prose"]} for item in data_list]

    return processed_data
