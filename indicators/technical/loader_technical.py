import pandas as pd

from indicators.technical.macd import get_macd
from indicators.technical.rsi import get_rsi
from indicators.technical.sma import get_sma
from indicators.technical.stochastic import get_stoch
from indicators.technical.adx import get_adx
from indicators.technical.atr import get_atr
from indicators.technical.bollinger import get_bollinger
from indicators.technical.obv import get_obv

def get_technical_indicators(df):

    df = get_macd(df)
    df = get_rsi(df)
    df = get_sma(df)
    df = get_stoch(df)
    df = get_adx(df)
    df = get_atr(df)
    df = get_bollinger(df)
    df = get_obv(df)

    return df