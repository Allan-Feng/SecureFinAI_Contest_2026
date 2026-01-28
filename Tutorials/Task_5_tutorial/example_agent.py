"""
Task 5 Example Agent - Agentic Trading

IMPORTANT: This is only an example. You should design and implement your own agent.

Your agent should:
- Process market data (price, news, fundamentals)
- Generate trading signals
- Output discrete action: Buy, Hold, or Sell
- Provide rationale for the decision (max 50 words)

The key interface is the `decide(market_data)` method.
"""

class ExampleAgent:
    """
    A template trading agent demonstrating the expected interface.
    
    DO NOT USE THIS DIRECTLY - Implement your own agent!
    """
    
    def __init__(self):
        """
        Initialize your agent here.
        
        TODO: Add your own initialization:
        - Load your LLM or ML model
        - Set up technical indicators
        - Configure risk parameters
        """
        print("ExampleAgent initialized (template only).")
        print("NOTE: You must implement your own agent for the competition!")

    def decide(self, market_data, news=None):
        """
        Make a trading decision based on market context.
        
        This is the MAIN interface your agent must implement.
        
        Args:
            market_data (DataFrame): Recent OHLCV data
            news (list): Optional list of recent news items
            
        Returns:
            dict: {
                "action": "Buy", "Hold", or "Sell",
                "rationale": str (max 50 words)
            }
        """
        # Placeholder - returns Hold with no logic
        # Replace with your own implementation!
        return {
            "action": "Hold",
            "rationale": "NOT IMPLEMENTED - Please implement your own trading logic."
        }


if __name__ == "__main__":
    import pandas as pd
    
    agent = ExampleAgent()
    
    # Mock market data for testing
    mock_data = pd.DataFrame({
        "Open": [100, 101, 102],
        "High": [102, 103, 104],
        "Low": [99, 100, 101],
        "Close": [101, 102, 103],
        "Volume": [1000, 1100, 1200]
    })
    
    result = agent.decide(mock_data)
    print(f"\nMarket Data:\n{mock_data}")
    print(f"\nDecision: {result['action']}")
    print(f"Rationale: {result['rationale']}")
    
    print("\n" + "="*50)
    print("This is only an example.")
    print("You should design and implement your own agent!")
    print("="*50)
