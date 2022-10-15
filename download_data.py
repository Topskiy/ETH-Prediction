"""download data from binance"""
import os
import pandas as pd
from binance.client import Client

# client configuration
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET_KEY')
client = Client(api_key, api_secret)

#ETHBTC ETHUSDT
SYMBOL = "ETHEUR"
# 1m 5m 15m
INTERVAL='1m'

klines = client.get_historical_klines(SYMBOL, INTERVAL, "1 Jan,2021")
data = pd.DataFrame(klines)
 # create colums name
data.columns = ['open_time','open', 'high', 'low', 'close', 'volume','close_time',
                'qav','num_trades','taker_base_vol','taker_quote_vol', 'ignore']

data.to_csv(SYMBOL + '-' + INTERVAL +'.csv', index = None, header=True)
