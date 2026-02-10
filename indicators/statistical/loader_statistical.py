from indicators.statistical.zscore import get_zscore
from indicators.statistical.volatility import get_volatility
from indicators.statistical.skewness import get_skewness
from indicators.statistical.kurtosis import get_kurtosis


def get_statistical_features(df):

    df = get_zscore(df)
    df = get_volatility(df)
    df = get_skewness(df)
    df = get_kurtosis(df)

    return df