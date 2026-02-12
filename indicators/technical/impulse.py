def get_impulse(df):

    df['ROC_10'] = df['Close'].pct_change(10)

    std = df['Close'].rolling(window=20).std()
    middle = df['Close'].rolling(window=20).mean()
    upper = middle + (std * 2)
    lower = middle - (std * 2)
    df['BB_Width'] = (upper - lower) / middle

    v_mean = df['Volume'].rolling(window=20).mean()
    v_std = df['Volume'].rolling(window=20).std()
    df['Volume_Z'] = (df['Volume'] - v_mean) / v_std

    return df