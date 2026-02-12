from indicators.statistical.zscore import get_zscore
from indicators.statistical.volatility import get_volatility
from indicators.statistical.skewness import get_skewness
from indicators.statistical.kurtosis import get_kurtosis
from indicators.statistical.klass import get_klass
from indicators.statistical.parkinson import get_parkinson


def get_statistical_indicators(df):

    df = get_zscore(df)
    df = get_volatility(df)
    df = get_skewness(df)
    df = get_kurtosis(df)
    df = get_klass(df)
    df = get_parkinson(df)

    return df