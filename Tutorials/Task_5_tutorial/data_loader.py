"""
Task 5 Data Loader - Market Data

Loads market data for ETH and MSFT.
For development, uses yfinance. Competition data will be provided separately.
"""

def load_market_data(asset="ETH", start_date="2024-01-01", end_date=None):
    """
    Load market data for the specified asset.
    
    Args:
        asset (str): 'ETH' or 'MSFT'
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date (None = today)
    
    Returns:
        DataFrame: OHLCV data
    """
    try:
        import yfinance as yf
        
        ticker = "ETH-USD" if asset == "ETH" else "MSFT"
        print(f"Loading {ticker} data from Yahoo Finance...")
        
        data = yf.download(ticker, start=start_date, end=end_date)
        print(f"Loaded {len(data)} rows.")
        return data
        
    except ImportError:
        print("yfinance not installed. Install with: pip install yfinance")
        print("Returning empty DataFrame.")
        import pandas as pd
        return pd.DataFrame()


if __name__ == "__main__":
    # Test the loader
    data = load_market_data("ETH", "2024-01-01")
    print(data.head() if len(data) > 0 else "No data")
