import pandas as pd

def get_zscore(df, window=30):

    z_mean = df['Close'].rolling(window=window).mean()
    z_std = df['Close'].rolling(window=window).std()

    df['ZScore'] = (df['Close'] - z_mean) / z_std

    return df