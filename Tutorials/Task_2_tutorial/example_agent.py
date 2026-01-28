"""
Task 2 Example Agent - Reliable Agentic FinSearch

IMPORTANT: This is just a TEMPLATE to help you understand the expected interface.
You should NOT use this script directly for your submission.
You need to design and implement your own agent with:
- Your own search/retrieval strategy (e.g., web search APIs, RAG, knowledge bases)
- Your own reasoning/inference pipeline
- Your own LLM integration

The key interface is the `predict(question)` method which should return:
- answer (str): The extracted answer
- evidence (str): The supporting evidence/sources
"""

import os

class ExampleAgent:
    """
    A template agent class demonstrating the expected interface.
    
    DO NOT USE THIS DIRECTLY - Implement your own agent!
    """
    
    def __init__(self):
        """
        Initialize your agent here.
        
        TODO: Add your own initialization:
        - Load your LLM (local or API-based)
        - Set up your search/retrieval tools
        - Initialize any other resources
        """
        print("ExampleAgent initialized (template only).")
        print("NOTE: You must implement your own agent for the competition!")

    def search(self, query, max_results=3):
        """
        Search for relevant information.
        
        TODO: Implement your own search strategy:
        - Web search APIs (Tavily, Brave, SerpAPI, etc.)
        - RAG with vector databases
        - Custom knowledge bases
        - Multiple sources combination
        
        Args:
            query (str): The search query
            max_results (int): Maximum number of results
            
        Returns:
            List[Dict]: List of results with 'title', 'body', 'href' keys
        """
        # Placeholder - returns empty results
        # Replace with your own implementation!
        return []

    def predict(self, question):
        """
        Predict the answer for a given question.
        
        This is the MAIN interface your agent must implement.
        
        Args:
            question (str): The financial question to answer
            
        Returns:
            tuple: (answer, evidence)
                - answer (str): The extracted answer (e.g., "6.5%", "1.2 billion")
                - evidence (str): Supporting evidence or reasoning trace
        """
        # 1. Search for relevant information
        search_results = self.search(question)
        
        # 2. Build context from search results
        if search_results:
            context = "\n".join([
                f"Source: {r['title']}\nContent: {r['body']}\nURL: {r['href']}"
                for r in search_results
            ])
            evidence = context
        else:
            context = "No search results available."
            evidence = "No external sources retrieved."
        
        # 3. Generate answer using LLM
        # TODO: Replace with your LLM call
        answer = "NOT IMPLEMENTED - Please implement your own agent!"
        
        return answer, evidence


if __name__ == "__main__":
    # Demo usage
    agent = ExampleAgent()
    
    q = "What is the inflation rate in the US in 2023?"
    ans, ev = agent.predict(q)
    
    print(f"\nQuestion: {q}")
    print(f"Answer: {ans}")
    print(f"Evidence: {ev}")
    print("\n" + "="*50)
    print("This is just a template - implement your own agent!")
    print("="*50)
