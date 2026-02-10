import yfinance as yf


def download(ticker):
    data = yf.download(ticker, period="5y", interval="1d")

    name = ticker.replace("-", "").lower()

    data.to_csv(f"{name}_history.csv")

download("BTC-USD")