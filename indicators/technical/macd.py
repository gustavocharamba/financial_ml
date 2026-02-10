import pandas as pd

def get_macd(df):

    ema12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema26 = df['Close'].ewm(span=26, adjust=False).mean()

    line = ema12 - ema26
    signal = line.ewm(span=9, adjust=False).mean()
    hist = line - signal

    df['MACD_Line'] = line
    df['MACD_Signal'] = signal
    df['MACD_Hist'] = hist

    return df