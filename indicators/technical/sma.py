import pandas as pd

def get_sma(df):

    sma_7 = df['Close'].rolling(7).mean()
    sma_9 = df['Close'].rolling(9).mean()
    sma_11 = df['Close'].rolling(11).mean()
    sma_21 = df['Close'].rolling(21).mean()
    sma_50 = df['Close'].rolling(50).mean()
    sma_77 = df['Close'].rolling(77).mean()
    sma_200 = df['Close'].rolling(200).mean()

    return df.DataFrame({
        "SMA_7": sma_7,
        "SMA_9": sma_9,
        "SMA_11": sma_11,
        "SMA_21": sma_21,
        "SMA_50": sma_50,
        "SMA_77": sma_77,
        "SMA_200": sma_200
    }, index=df.index)