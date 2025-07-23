import pandas as pd

def calculate_sma(data, period):
    """Simple Moving Average"""
    return data['close'].rolling(window=period).mean()

def calculate_rsi(data, period=14):
    """Relative Strength Index"""
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
