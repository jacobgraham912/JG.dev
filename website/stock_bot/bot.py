# stock_bot/bot.py
# Alpaca emergency code: 3b952555-d160-44be-a62d-716fce22ee41
import pandas as pd
import requests
from utils import calculate_sma, calculate_rsi

API_KEY = 'PK3MFSNPTUMHNUG1WMX8'
API_SECRET = 'CW1oebMbabVNda8ahRcu4VcG1s3eQkvzINMWBdmS'
BASE_URL = 'https://paper-api.alpaca.markets'

HEADERS = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET
}

def get_historical_data(symbol, limit=50):
    url = f"{BASE_URL}/v2/stocks/{symbol}/bars"
    params = {
        'timeframe': '1Day',
        'limit': limit
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch data for {symbol}")
        return None
    data = response.json()
    # Convert to DataFrame
    bars = data.get('bars', [])
    if not bars:
        return None
    df = pd.DataFrame(bars)
    df['t'] = pd.to_datetime(df['t'])
    df.set_index('t', inplace=True)
    return df

def scan_stocks(tickers):
    signals = {}
    for symbol in tickers:
        print(f"Scanning {symbol}...")
        df = get_historical_data(symbol)
        if df is None or df.empty:
            continue
        df['SMA5'] = calculate_sma(df, 5)
        df['SMA20'] = calculate_sma(df, 20)
        df['RSI'] = calculate_rsi(df)

        # Check latest crossover and RSI
        if len(df) < 21:
            continue  # Need at least 20 days of data

        latest = df.iloc[-1]
        prev = df.iloc[-2]

        # SMA crossover: 5-day crosses above 20-day
        crossover = prev['SMA5'] < prev['SMA20'] and latest['SMA5'] > latest['SMA20']
        rsi_oversold = latest['RSI'] < 30

        if crossover and rsi_oversold:
            signals[symbol] = "BUY signal"

    return signals

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'TSLA', 'AMZN']
    results = scan_stocks(tickers)
    for sym, signal in results.items():
        print(f"{sym}: {signal}")

