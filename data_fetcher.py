import yfinance as yf

def fetch_stock_data(ticker):
    df = yf.download(ticker, period="3mo", interval="1d")
    return df