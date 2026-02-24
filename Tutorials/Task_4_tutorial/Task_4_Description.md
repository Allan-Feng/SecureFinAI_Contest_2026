# Task IV: AI for Venture Capital - Prediction of Startup Success

**Description**
This task evaluates the ability of Large Language Models (LLMs) to function as venture capital analysts by predicting the potential success of early-stage startups. Using the **VCBench** dataset—comprising anonymized founder profiles—participants must determine whether a startup will achieve a significant liquidity event, such as an IPO, an acquisition exceeding \$500M, or top-tier funding.
---

**Goal & Constraints**
- **Objective:** Predict the binary **Success** label for each founder profile.
- **Optimization Scope:** Participants are encouraged to improve performance through prompt design, input formatting, output extraction, and optional model fine-tuning.
- **Evaluation Metric:** **F1-score**
---

**Datasets**

*   **VCBench**: A benchmark for predicting founder success in venture capital with 9,000 anonymized founder profiles.

    - 📄 Paper: [VCBench: Benchmarking LLMs in Venture Capital](https://arxiv.org/abs/2509.14448)  
    - 🌐 Website: https://www.vcbench.com/

---

**Dataset Details**
- **Total profiles:** 9,000 anonymized founder profiles  
- **Features include:**  
  - Founder background  
  - Education  
  - Professional experience  
  - Other relevant signals  

- **Success rate:** 9% (810 successful founders)  
- **Definition of Success:** Company achieved a qualifying acquisition, IPO, or comparable major outcome above the specified threshold.

### Data Splits

- **Public Labeled Data (4,500 samples)** — provided in `VCbench_train.csv`
  - Recommended usage:
    - First **3,000** samples → Training set  
    - Remaining **1,500** samples → Validation / local evaluation  

- **Private Evaluation Data (4,500 samples)**  
  - Labels are withheld.
  - Participants must generate predictions for these samples and submit a result file.
  - This split will be used for final scoring.

---

**Submission Requirements**

Participants must submit the following:

1. **GitHub Repository**  
   - Public or private repository containing the full pipeline used to generate predictions.

2. **Hugging Face Model Link (Optional)**  
   - Provide a link if you fine-tuned and uploaded a model to the Hugging Face Hub.

3. **Run Script**  
   - A reproducible script (e.g., `run.py`) that generates predictions end-to-end.

4. **Prediction Output File**  
   - Include your final predictions in the repository.
   - The file format must match the provided example.
   - You may change the prediction output file name, as long as it remains in **CSV** format (`.csv`) and contains the **same columns** as the provided example.

