import pandas as pd

def get_sma(df):

    df['SMA_7'] = df['Close'].rolling(window=7).mean()
    df['SMA_9'] = df['Close'].rolling(window=9).mean()
    df['SMA_11'] = df['Close'].rolling(window=11).mean()
    df['SMA_21'] = df['Close'].rolling(window=21).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_77'] = df['Close'].rolling(window=77).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()

    return df