import pandas as pd
import numpy as np

def get_williams(df, period=14):

    high_max = df['High'].rolling(period).max()
    low_min = df['Low'].rolling(period).min()
    df[f'WilliamsR_{period}'] = -100 * (high_max - df['Close']) / (high_max - low_min)

    return df

