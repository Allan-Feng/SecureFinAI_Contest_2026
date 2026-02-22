"""
Task 4 Example Agent - AI for Venture Capital

IMPORTANT: This is only an example. You should design and implement your own model.

Your model can include:
- Process founder profile information
- Predict success probability
- Optimize for F1-Score

"""
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
class LLMForVC:
    """
    A template model class demonstrating the expected interface.
    
    """
    
    def __init__(self, model_name="Qwen/Qwen3-8B"):
        self.model_name = model_name
        self.llm = LLM(
        model=model_name,
        dtype="auto",
        trust_remote_code=True,  
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            padding_side="left",
            trust_remote_code=True
        )
        self.sampling_params = SamplingParams(
            max_tokens=512,
            temperature=1,  
            top_p=1.0,
        )
        if self.tokenizer.pad_token is None:
            if self.tokenizer.eos_token is not None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            else:
                self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
                
        self.system_prompt = """You are an expert venture capitalist.
            Your task is to PREDICT whether this founder is likely to become a 'successful founder' in the future, based on an early-stage profile.

            Important context:
            - The descriptions are from early-stage founders whose companies have only raised $100K–$4M so far.
            - Therefore the text will NOT contain evidence of $500M funding or a $500M exit yet.
            - You must infer potential from signals such as team quality, traction indicators, market size, business model, timing, and founder experience.

            Definition for evaluation:
            A 'successful founder' means that in the future their company will eventually achieve either:
            (1) total funding > $500M, OR
            (2) an exit/IPO valuation > $500M.

            Predict Yes/No for FUTURE success likelihood, not whether they already achieved it.
            """
        self.user_prompt_template = """Given the following founder description:
            {founder_description},
            please output a json string with two keys; 
            1. prediction: 'Yes' or 'No' corresponding to whether or not the founder will be successful.
            2. reasoning: a short explanation for your prediction (at most 100 words).
                DO NOT return anything else
        """
        
        
    def get_model_input(self, founder_description):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt_template.format(founder_description=founder_description)}
        ]
        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        return prompt
        
        

    def batch_predict(self, profile_list):
        """
        Batch prediction method. Takes a list of founder profiles and returns predictions.
        """
        results = []
        prompts = [self.get_model_input(item) for item in profile_list]
        outputs = self.llm.generate(prompts, self.sampling_params)
        
        decoded = [out.outputs[0].text for out in outputs]
        
        for pred in decoded:
            pred = pred.strip()
            try:
                prediction_text = pred.split("<think>")[1].split("</think>")[0].strip().lower()
            except IndexError:
                prediction_text = pred.lower()

            if "yes" in prediction_text:
                label = 1
            elif "no" in prediction_text:
                label = 0
            results.append(label)

        return results



if __name__ == "__main__":
    agent = LLMForVC()
    
