import pandas as pd
import numpy as np

def get_obv(df):

    df['OBV'] = (np.sign(df['Close'].diff()) * df['Volume']).fillna(0).cumsum()

    df['OBV_Slope'] = df['OBV'].diff(5)

    return df