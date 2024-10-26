import yfinance as yf

def get_stock_data(symbol = 'AAPL' , period = '1mo'):
    """
    Get stock data from Yahoo Finance
    """
    stock = yf.Ticker(symbol)
    history = stock.history(period = period)
    return history

if __name__ == '__main__':
    # Test the function
    data = get_stock_data()
    print("Successfully download stock data:")
    print(data.head())