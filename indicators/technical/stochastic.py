import pandas as pd

def get_stoch(df):
    low_14 = df['Low'].rolling(window=14).min()
    high_14 = df['High'].rolling(window=14).max()

    k = 100 * ((df['Close'] - low_14) / (high_14 - low_14))
    d = k.rolling(window=3).mean()

    return pd.DataFrame({
        "Stoch_K": k,
        "Stoch_D": d
    }, index=df.index)