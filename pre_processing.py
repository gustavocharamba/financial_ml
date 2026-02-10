import pandas as pd

def get_preprocessing(df):

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    df['Volume'] = df['Volume'].fillna(0).astype(int)

    return df