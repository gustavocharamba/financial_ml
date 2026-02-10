import pandas as pd
import numpy as np


def get_bollinger(df, period=20, std_dev=2):

    df['BB_Middle'] = df['Close'].rolling(window=period).mean()

    std = df['Close'].rolling(window=period).std()

    df['BB_Upper'] = df['BB_Middle'] + (std * std_dev)
    df['BB_Lower'] = df['BB_Middle'] - (std * std_dev)


    df['BB_Percent_B'] = (df['Close'] - df['BB_Lower']) / (df['BB_Upper'] - df['BB_Lower'])

    df['BB_Width'] = (df['BB_Upper'] - df['BB_Lower']) / df['BB_Middle']

    return df