"""
Task 4 Data Loader - VCBench Dataset

Loads the VCBench dataset from HuggingFace.
"""

from datasets import load_dataset

def load_vcbench(split='test'):
    """
    Load the VCBench dataset from HuggingFace.
    
    Args:
        split (str): 'train', 'test', or 'validation'
    
    Returns:
        Dataset: HuggingFace dataset object
    """
    print(f"Loading VCBench dataset (split={split})...")
    dataset = load_dataset("cloudcatcher2/VCBench", split=split)
    print(f"Loaded {len(dataset)} samples.")
    return dataset


if __name__ == "__main__":
    # Test the loader
    data = load_vcbench()
    print("Sample item:", data[0] if len(data) > 0 else "No data")
