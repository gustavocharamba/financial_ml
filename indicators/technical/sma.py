import pandas as pd

def get_sma(df):

    windows = [7, 9, 11, 21, 50, 77, 200]

    for w in windows:
        sma_abs = df['Close'].rolling(window=w).mean()

        df[f'SMA_{w}_pct'] = (df['Close'] - sma_abs) / sma_abs


    return df