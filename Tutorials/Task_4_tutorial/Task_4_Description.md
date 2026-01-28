# Task IV: AI for Venture Capital - Prediction of Startup Success

**Description**
This task tests the ability of Large Language Models to act as Venture Capitalists by predicting the potential success of early-stage startups. Using the **VCBench** dataset, which consists of anonymized founder profiles, participants must predict whether a startup will achieve a significant liquidity event (IPO, M&A >$500M, or high-tier funding).

**Goal & Constraints**
*   **Objective:** Predict the binary "Success" label for given founder profiles.
*   **Optimization:** Participants are encouraged to optimize input templates and output extraction methods alongside model fine-tuning.
*   **Metric:** F1-Score.

**Datasets**

*   **VCBench**: A benchmark for predicting founder success in venture capital with 9,000 anonymized founder profiles.
    - **HuggingFace**: [cloudcatcher2/VCBench](https://huggingface.co/datasets/cloudcatcher2/VCBench)
    - **Paper**: [VCBench: Benchmarking LLMs in Venture Capital](https://arxiv.org/abs/2501.xxxxx)
    - **Website**: [https://www.vcbench.com/](https://www.vcbench.com/)

**Dataset Details**
- 9,000 anonymized founder profiles
- 9% success rate (810 successful founders)
- Success = company achieved acquisition or IPO above threshold
- Features include founder background, education, experience, etc.

**Submission Requirements**

Participants must submit:
1. **GitHub Repository**: Public or private repo containing your model code
2. **HuggingFace Model Link**: Your fine-tuned model uploaded to HuggingFace Hub
3. **Run Script**: A script (e.g., `run.py`) that we can execute to generate predictions
4. **Requirements File**: `requirements.txt` with all dependencies

**Output Format**:
- Predict binary "Success" label (0 or 1) for each founder profile
- Include confidence score (optional)

We will evaluate your submission by running your model on the test set.
