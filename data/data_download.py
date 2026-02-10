import yfinance as yf
import pandas as pd

def download(ticker):
    data = yf.download(ticker, period="5y", interval="1d", auto_adjust=True)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel('Ticker')

    name = ticker.replace("-", "").lower()

    data.to_csv(f"{name}_history.csv")

download("BTC-USD")