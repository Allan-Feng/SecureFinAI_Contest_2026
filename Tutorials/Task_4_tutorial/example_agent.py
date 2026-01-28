"""
Task 4 Example Agent - AI for Venture Capital

IMPORTANT: This is only an example. You should design and implement your own model.

Your model should:
- Process founder profile information
- Predict success probability
- Optimize for F1-Score

The key interface is the `predict(profile)` method.
"""

class ExampleAgent:
    """
    A template model class demonstrating the expected interface.
    
    DO NOT USE THIS DIRECTLY - Implement your own model!
    """
    
    def __init__(self):
        """
        Initialize your model here.
        
        TODO: Add your own initialization:
        - Load your LLM or ML model
        - Set up prompts or feature extractors
        """
        print("ExampleAgent initialized (template only).")
        print("NOTE: You must implement your own model for the competition!")

    def predict(self, profile):
        """
        Predict success for a founder profile.
        
        This is the MAIN interface your model must implement.
        
        Args:
            profile (dict): Founder profile data from VCBench
            
        Returns:
            dict: {
                "prediction": 0 or 1 (binary success label),
                "confidence": float between 0 and 1
            }
        """
        # Placeholder - returns random/default prediction
        # Replace with your own implementation!
        return {
            "prediction": 0,
            "confidence": 0.5
        }


if __name__ == "__main__":
    agent = ExampleAgent()
    
    # Mock profile for testing
    mock_profile = {
        "founder_id": "test_001",
        "education": "Stanford CS PhD",
        "experience": "10 years in tech",
    }
    
    result = agent.predict(mock_profile)
    print(f"\nProfile: {mock_profile}")
    print(f"Prediction: {result}")
    
    print("\n" + "="*50)
    print("This is only an example.")
    print("You should design and implement your own model!")
    print("="*50)
