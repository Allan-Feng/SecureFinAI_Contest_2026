"""
Task 3 Example Agent - Prediction Market Arbitrage

IMPORTANT: This is only an example. You should design and implement your own agent.

Your agent should:
- Connect to Kalshi and Polymarket APIs
- Monitor market prices in real-time
- Detect arbitrage opportunities (price discrepancies)
- Execute trades to capture spread
- Manage risk and position sizing

The key interface is the `run()` method which implements your trading loop.
"""

class ExampleAgent:
    """
    A template agent class demonstrating the expected interface.
    
    DO NOT USE THIS DIRECTLY - Implement your own agent!
    """
    
    def __init__(self):
        """
        Initialize your agent here.
        
        TODO: Add your own initialization:
        - API clients for Kalshi and Polymarket
        - WebSocket connections for real-time data
        - Trading parameters (position limits, spread thresholds, etc.)
        """
        print("ExampleAgent initialized (template only).")
        print("NOTE: You must implement your own agent for the competition!")
        
        # Example: placeholder for API clients
        self.kalshi_client = None
        self.polymarket_client = None
        
        # Example: trading parameters
        self.min_spread_threshold = 0.02  # 2% minimum spread to trade
        self.max_position_size = 100  # Maximum position per market

    def get_kalshi_markets(self):
        """
        Fetch available markets from Kalshi.
        
        TODO: Implement using Kalshi REST API
        https://trading-api.readme.io/docs
        
        Returns:
            List[Dict]: List of markets with prices
        """
        # Placeholder - returns empty
        return []

    def get_polymarket_markets(self):
        """
        Fetch available markets from Polymarket.
        
        TODO: Implement using Polymarket Gamma API and CLOB API
        https://docs.polymarket.com
        
        Returns:
            List[Dict]: List of markets with prices
        """
        # Placeholder - returns empty
        return []

    def find_arbitrage_opportunities(self, kalshi_markets, polymarket_markets):
        """
        Identify arbitrage opportunities between the two markets.
        
        An arbitrage opportunity exists when:
        - Same event is priced differently on both platforms
        - The spread exceeds transaction costs
        
        TODO: Implement your matching and detection logic
        
        Args:
            kalshi_markets: Markets from Kalshi
            polymarket_markets: Markets from Polymarket
            
        Returns:
            List[Dict]: List of arbitrage opportunities
        """
        # Placeholder - returns empty
        return []

    def execute_trade(self, opportunity):
        """
        Execute a trade to capture the arbitrage opportunity.
        
        TODO: Implement order placement on both platforms
        
        Args:
            opportunity: The arbitrage opportunity to execute
            
        Returns:
            Dict: Trade execution result
        """
        # Placeholder
        return {"status": "NOT IMPLEMENTED"}

    def run(self, duration_seconds=60):
        """
        Main trading loop.
        
        This is the MAIN interface your agent must implement.
        
        Args:
            duration_seconds: How long to run the paper trading simulation
        """
        print(f"\nRunning paper trading simulation for {duration_seconds} seconds...")
        print("NOTE: This is a template - implement your own trading logic!")
        
        # Placeholder trading loop
        import time
        start_time = time.time()
        
        while time.time() - start_time < duration_seconds:
            # 1. Fetch market data
            kalshi_markets = self.get_kalshi_markets()
            polymarket_markets = self.get_polymarket_markets()
            
            # 2. Find opportunities
            opportunities = self.find_arbitrage_opportunities(
                kalshi_markets, polymarket_markets
            )
            
            # 3. Execute trades
            for opp in opportunities:
                result = self.execute_trade(opp)
                print(f"Trade result: {result}")
            
            # Wait before next iteration
            time.sleep(1)
        
        print("\nPaper trading simulation complete.")
        print("Total P&L: NOT IMPLEMENTED")


if __name__ == "__main__":
    agent = ExampleAgent()
    agent.run(duration_seconds=5)
    
    print("\n" + "="*50)
    print("This is only an example.")
    print("You should design and implement your own agent!")
    print("="*50)
