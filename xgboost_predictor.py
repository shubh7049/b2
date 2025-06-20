from data_fetcher import fetch_stock_data
from technical_indicators import add_technical_indicators



def get_stock_predictions():
    stocks = ['TCS.NS', 'INFY.NS', 'RELIANCE.NS']
    results = []

    for stock in stocks:
        df = fetch_stock_data(stock)
        df = add_technical_indicators(df)
        
        # ✅ Check for empty DataFrame
        if df.empty:
            continue
        
        last_row = df.iloc[-1]

       if last_row['RSI'] < 30 and last_row['Close'] > last_row['upper_bb']:
    results.append({
        "stock": stock,
        "direction": "UP",
        "target_price": round(last_row['Close'] * 1.05)
    })
elif last_row['RSI'] > 70 and last_row['Close'] < last_row['lower_bb']:
    results.append({
        "stock": stock,
        "direction": "DOWN",
        "target_price": round(last_row['Close'] * 0.95)
    })

           

    return results
