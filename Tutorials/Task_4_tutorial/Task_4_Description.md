# Task IV: VC Bench - Startup Success Prediction

**Description**
Venture Capital involves high uncertainty, sparse signals, and extremely low success rates. **VCBench** is a pioneering benchmark designed to evaluate whether AI agents can identify "unicorn" potential better than human intuition.

In this task, participants will work with a dataset of **9,000 anonymized founder profiles** provided by Vela. The dataset has a realistic, imbalanced distribution with a ~9% success rate. "Success" is rigorously defined as achieving a $500M+ exit (via IPO or M&A) or securing significant funding rounds.

**The Challenge**
Participants must develop a prediction pipeline that takes a structured or natural-language founder profile as input and outputs a binary success prediction. This is not just a standard classification task; it requires the model to synthesize subtle signals from background, experience, and team composition often found in VC due diligence.

**Rules & Requirements**
*   **Model Constraint:** To ensure accessibility and focus on efficiency, all competing models must have **fewer than 14 billion parameters** (e.g., Llama-3-8B, Qwen-14B, etc.).
*   **Optimization Scope:** Participants are allowed and encouraged to:
    *   Fine-tune their chosen base models on the provided public dataset.
    *   Design custom prompt templates (Input Engineering).
    *   Develop robust answer extraction logic (Output Engineering).
*   **Evaluation:**
    *   Models will be tested on a held-out set of profiles.
    *   The primary evaluation metric is **F1-Score**, balancing precision and recall to account for the class imbalance inherent in VC data.

**Resources**
*   **Dataset**: Derived from Vela’s database, processed through a multi-stage anonymization pipeline to prevent identity leakage while preserving predictive signals.
*   **Reference Paper**: [VCBench: Evaluating LLMs for Venture Capital](https://arxiv.org/abs/2509.14448)
