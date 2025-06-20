import pandas as pd

def add_technical_indicators(df):
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['stddev'] = df['Close'].rolling(window=20).std()
    df['upper_bb'] = df['MA20'] + (df['stddev'] * 2)
    df['lower_bb'] = df['MA20'] - (df['stddev'] * 2)
    df['RSI'] = compute_rsi(df['Close'])
    return df

def compute_rsi(series, period=14):
    delta = series.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi