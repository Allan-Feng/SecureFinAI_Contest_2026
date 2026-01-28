# Task II: Reliable Agentic FinSearch

**Description**
This task benchmarks the reliability of financial search agents, specifically focusing on eliminating hallucinations and ensuring numerical precision. Participants are expected to finetune models and design agent pipelines that will be evaluated on their ability to retrieve and process financial data without errors.

**Datasets**
*   **The FinSearchComp benchmark** consists of 635 financial questions (e.g., “What was the annual inflation rate in Australia in 2022?”) paired with their ground-truth answers (e.g., “6.6%,” allowing for minor rounding errors). These questions are designed to evaluate an agent’s proficiency of searching and reasoning in terms of numerical and temporal accuracy. The benchmark covers three types of tasks: (1) real-time retrieval of numerical data (Task 1), (2) simple lookup of historical data (Task 2), and (3) complex computation over historical data (Task 3). The dataset includes 244 questions for Task 1, 219 for Task 2, and 172 for Task 3.
*   **Dataset Link**: [HuggingFace - FinSearchComp](https://huggingface.co/datasets/ByteSeedXpert/FinSearchComp)

**Submission Requirements**

Participants must submit:
1. **GitHub Repository**: Public or private repo containing your agent code
2. **HuggingFace Model Link** (if applicable): Your fine-tuned model uploaded to HuggingFace Hub
3. **Run Script**: A script (e.g., `run.py`) that we can execute to generate predictions
4. **Requirements File**: `requirements.txt` with all dependencies

We will evaluate your submission by running your agent on the test set.
