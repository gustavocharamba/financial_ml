import yfinance as yf
import pandas as pd
import numpy as np


def get_data_download(ticker):

    df_5m = yf.download(ticker, period="30d", interval="5m", auto_adjust=True)
    df_15m = yf.download(ticker, period="59d", interval="15m", auto_adjust=True)
    df_1h = yf.download(ticker, period="720d", interval="1h", auto_adjust=True)

    data_map = {
        "5m": df_5m,
        "15m": df_15m,
        "1h": df_1h
    }

    for interval in data_map:
        df = data_map[interval].copy()

        if isinstance(df.columns, pd.MultiIndex):
            try:
                df.columns = df.columns.droplevel('Ticker')
            except KeyError:
                df.columns = df.columns.droplevel(1)

        df = df[~df.index.duplicated(keep='first')]
        df = df.sort_index()

        df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

        df.loc[df['Volume'] == 0, 'Volume'] = np.nan

        df['Volume'] = df['Volume'].interpolate(method='linear')

        df['Volume'] = df['Volume'].bfill()

        df = df.ffill()
        df = df.dropna()

        data_map[interval] = df

    name = ticker.replace("-", "").lower()

    path_5m = f"{name}_5m.csv"
    path_15m = f"{name}_15m.csv"
    path_1h = f"{name}_1h.csv"

    data_map["5m"].to_csv(path_5m)
    data_map["15m"].to_csv(path_15m)
    data_map["1h"].to_csv(path_1h)

get_data_download("BTC-USD")