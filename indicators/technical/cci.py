import pandas as pd
import numpy as np

def get_cci(df, period=20):

    tp = (df['High'] + df['Low'] + df['Close']) / 3
    ma = tp.rolling(period).mean()
    md = (tp - ma).abs().rolling(period).mean()
    df[f'CCI_{period}'] = (tp - ma) / (0.015 * md)

    return df
