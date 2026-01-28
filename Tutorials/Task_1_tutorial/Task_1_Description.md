# Task I: Adaptive Evaluation and Benchmarking Suite for Financial LLMs and Agents

**Description**
This task focuses on benchmarking Financial Large Language Models (FinLLMs) and agents using an **adaptive testing pipeline**. Unlike traditional benchmarks, the adaptive pipeline partitions the test set into difficulty levels and dynamically selects test items based on model performance. This enables more efficient evaluation while preserving rigour. Participants are expected to submit models that can handle a diverse range of financial reasoning and comprehension tasks, optimised for both accuracy and inference efficiency.

**Datasets**
We utilize the standard evaluation suite referenced in BloombergGPT, integrated into the adaptive framework. This includes:
*   **FPB (Financial PhraseBank)**: Evaluates the model’s ability to categorize financial news sentences by sentiment (positive, negative, neutral). [Dataset Link](https://huggingface.co/datasets/ChanceFocus/en-fpb)
*   **FiQA-SA**: A more granular aspect-based sentiment analysis task, testing understanding of financial opinions in social media and microblogs. [Dataset Link](https://huggingface.co/datasets/ChanceFocus/flare-fiqasa)
*   **Headlines**: Tests the classification of news headlines in specific contexts (e.g., impact on gold prices), assessing market awareness. [Dataset Link](https://huggingface.co/datasets/ChanceFocus/flare-headlines)
*   **NER (Named Entity Recognition)**: Challenges the model to precisely identify and classify financial entities such as organizations, people, and locations within complex financial texts. [Dataset Link](https://huggingface.co/datasets/ChanceFocus/flare-ner)
*   **ConvFinQA**: A high-complexity task requiring the model to answer conversational questions by reasoning over both text and numerical tables found in financial reports. [Dataset Link](https://huggingface.co/datasets/ChanceFocus/flare-convfinqa)

**Submission Requirements**

Participants must submit:
1. **GitHub Repository**: Public or private repo containing your code
2. **HuggingFace Model Link**: Your fine-tuned model uploaded to HuggingFace Hub
3. **Run Script**: A script (e.g., `run.py` or `inference.py`) that we can execute to reproduce your results
4. **Requirements File**: `requirements.txt` with all dependencies

We will evaluate your submission by running your inference script on the test set.
