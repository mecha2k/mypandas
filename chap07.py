import datetime
import pandas_datareader.data as web
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    msft = web.DataReader("MSFT", "yahoo", datetime.date(2000, 1, 1), datetime.date(2014, 12, 31))
    print(msft[:5])

    msft["MA7"] = msft["Adj Close"].rolling(7).mean()
    msft["MA30"] = msft["Adj Close"].rolling(30).mean()
    msft["MA90"] = msft["Adj Close"].rolling(90).mean()
    msft["MA120"] = msft["Adj Close"].rolling(120).mean()

    msft["2014"][["Adj Close", "MA7", "MA30", "MA120"]].plot(figsize=(12, 8))
    plt.savefig("results/5104OS_07_01.png", bbox_inches="tight", dpi=300)

    msft["2002"][["Adj Close", "MA7", "MA30", "MA120"]].plot(figsize=(12, 8))
    plt.savefig("results/5104OS_07_02.png", bbox_inches="tight", dpi=300)

    periods = 10
    alpha = 2.0 / (periods + 1)
    factors = (1 - alpha) ** np.arange(1, 11)
    sum_factors = factors.sum()
    weights = factors / sum_factors

    span = 90
    msft_ewma = msft[["Adj Close"]].copy()
    msft_ewma["MA90"] = msft_ewma.rolling(span).mean()
    msft_ewma["EWMA90"] = msft_ewma["Adj Close"].ewm(span=span).mean()
    msft_ewma["2014"].plot(figsize=(12, 8))
    plt.savefig("results/5104OS_07_11.png", bbox_inches="tight", dpi=300)

    msft["2002-1":"2002-9"][["Adj Close", "MA30"]].plot(figsize=(12, 8))
    plt.savefig("results/5104OS_07_12.png", bbox_inches="tight", dpi=300)


if __name__ == "__main__":
    main()
