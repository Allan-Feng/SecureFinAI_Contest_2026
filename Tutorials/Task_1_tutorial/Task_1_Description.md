# Task I: Adaptive Evaluation for Financial LLMs (Powered by Trismik)

**Description**
This task introduces a next-generation evaluation methodology for the financial domain. We invite participants to submit FinLLMs to be evaluated using **Trismik’s Adaptive Testing Pipeline**, a system designed to overcome the inefficiencies of traditional static benchmarks.

The core innovation of this task is its **adaptive mechanism**. Instead of evaluating models on a fixed, exhaustive set of questions, the pipeline stratifies the underlying datasets into granular difficulty levels. During evaluation, the system acts like a computerized adaptive test (CAT) for humans: it dynamically selects a small, representative sample of items to probe the model's capabilities. By analyzing responses to these high-signal items, the pipeline can accurately determine the model's "skill ceiling" and proficiency curve. This allows for a robust, comprehensive score while requiring significantly fewer inference steps than standard methods.

**Datasets**
The evaluation covers the five core datasets defined in the **BloombergGPT** benchmark, ensuring industry-standard relevance:

*   **FPB (Financial PhraseBank)**: Evaluates the model’s ability to categorize financial news sentences by sentiment (positive, negative, neutral).
*   **FiQA-SA**: A more granular aspect-based sentiment analysis task, testing understanding of financial opinions in social media and microblogs.
*   **Headlines**: Tests the classification of news headlines in specific contexts (e.g., impact on gold prices), assessing market awareness.
*   **NER (Named Entity Recognition)**: Challenges the model to precisely identify and classify financial entities such as organizations, people, and locations within complex financial texts.
*   **ConvFinQA**: A high-complexity task requiring the model to answer conversational questions by reasoning over both text and numerical tables found in financial reports.
