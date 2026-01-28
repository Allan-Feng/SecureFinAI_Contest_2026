"""
Task 3 Main Script - Prediction Market Arbitrage

This script runs the paper trading simulation.
"""

from example_agent import ExampleAgent

def main():
    # Initialize agent
    agent = ExampleAgent()
    
    # Run paper trading simulation
    # Adjust duration as needed for your testing
    agent.run(duration_seconds=10)

if __name__ == "__main__":
    main()
