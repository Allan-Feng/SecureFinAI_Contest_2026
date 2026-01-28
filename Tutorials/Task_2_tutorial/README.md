# Task 2 Starter Kit: Reliable Agentic FinSearch

This starter kit provides a template for the **Reliable Agentic FinSearch** task.

> **IMPORTANT**: This is only an example. You should design and implement your own agent for submission.

## 📂 Directory Structure

```
Task_2_tutorial/
├── Task_2_Description.md  # Taxonomy and task details
├── requirements.txt       # Python dependencies
├── data_loader.py         # Script to download/load FinSearchComp dataset
├── example_agent.py       # A simple example agent (replace with your logic)
├── main.py                # Main script to run inference and generate submission
```

## 🚀 Setup

1. **Install Dependencies**
   It is recommended to use a virtual environment (Conda or venv).
   ```bash
   pip install -r requirements.txt
   ```

2. **Data Preparation**
   The datasets are hosted on HuggingFace: [ByteSeedXpert/FinSearchComp](https://huggingface.co/datasets/ByteSeedXpert/FinSearchComp).
   The `data_loader.py` script handles downloading automatically using the `datasets` library.

## 🏃 Running the Example Agent

The `example_agent.py` contains a `random` or simple search-based agent. You can run it to generate a sample submission file.

```bash
python main.py
```

## 🛠 Developing Your Agent

This is only a example agent. You should design and implement your own agent for submission.


