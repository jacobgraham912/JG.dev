# stock_bot/alpaca_client.py

import os
from alpaca_trade_api.rest import REST

# Load API keys from environment variables for security
API_KEY = 'PK3MFSNPTUMHNUG1WMX8'
API_SECRET = 'CW1oebMbabVNa8ahRcu4VcG1s3eQkvzINMWBdmS'
BASE_URL = 'https://paper-api.alpaca.markets'  # Change to live URL if needed

if not API_KEY or not API_SECRET:
    raise ValueError("Alpaca API keys not found in environment variables.")

# Initialize the Alpaca REST API client
api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')
