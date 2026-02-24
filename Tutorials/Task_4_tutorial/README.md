# Task 4 Starter Kit: AI for Venture Capital

This starter kit provides a template for the **AI for Venture Capital** task, enabling participants to quickly set up, run baseline inference, and develop their own models.


## 📂 Directory Structure

```
Task_4_tutorial/
├── README.md               # This file
├── Task_4_Description.md   # Task description and dataset information
├── requirements.txt        # Python dependencies
├── start.bash              # Script to launch main.py
├── VCbench_dev.csv         # Development (test) set
├── VCbench_train.csv       # Training and validation set
├── data_loader.py          # Utilities for loading VCBench data
├── example_model.py        # Template model implementation
├── evaluate.py             # F1-score evaluation script
└── main.py                 # Main script for running inference
```

## 🚀 Setup

```bash
cd Tutorials/Task_4_tutorial
pip install -r requirements.txt
```

## ▶️ Running

```bash
bash start.bash
```
This will execute main.py and generate prediction outputs using the example model.
## 🛠 Developing Your Model

The provided example demonstrates a simple pipeline where an LLM predicts startup success using the VCBench dataset.

### Key Notes

- The output file format must match the format of VCbench_dev.csv.
- You are free to implement your own modeling approach, including:
- Prompt engineering
- Output parsing strategies
- Fine-tuning
- Hybrid or non-LLM methods


