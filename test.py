import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt
# from pandas_datareader import data as pdr
# Can be used for collecting other data. 

tickers = ["SPY"]

EndDate = dt.datetime.now()
StartDate = dt.datetime(2024, 1, 1)

df = yf.download(tickers, start = StartDate, end = EndDate, use_threads=False)
print(df.head())

# Det funker ikke bedre nå.