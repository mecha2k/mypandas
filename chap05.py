import datetime
import pandas_datareader.data as web
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getTickers(tickers, start, end):
    def getdata(ticker):
        return web.DataReader(ticker, "yahoo", start, end)

    datas = map(getdata, tickers)
    return pd.concat(datas, keys=tickers, names=["Ticker", "Date"])


def savedatafile(start, end):
    tickers = ["AAPL", "MSFT", "GE", "IBM", "AA", "DAL", "UAL", "PEP", "KO"]
    alldata = getTickers(tickers, start, end)
    alldata.to_csv("data/alldata.csv")


def main():
    start = datetime.date(2012, 1, 1)
    end = datetime.date(2014, 12, 31)

    data = pd.read_csv("data/alldata.csv")
    data = data.set_index(["Ticker", "Date"])
    print(data.head())

    sp_500 = web.DataReader("^GSPC", "yahoo", start, end)
    print(sp_500[:5])

    just_closing_prices = data[["Adj Close"]].reset_index()
    print(just_closing_prices[:5])

    daily_close_px = just_closing_prices.pivot("Date", "Ticker", "Adj Close")
    print(daily_close_px[:5])

    # _ = daily_close_px["AAPL"].plot(figsize=(12, 8))
    # plt.savefig("results/5104OS_05_01.png", bbox_inches="tight", dpi=300)
    #
    # _ = daily_close_px.plot(figsize=(12, 8))
    # plt.savefig("results/5104OS_05_02.png", bbox_inches="tight", dpi=300)

    # msftV = data.Volume.loc["MSFT"]
    # print(msftV.head())
    # plt.bar(msftV.index, msftV)
    # plt.gcf().set_size_inches(12, 6)
    # plt.savefig("results/5104OS_05_03.png", bbox_inches="tight", dpi=300)
    #
    # top = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
    # top.plot(daily_close_px.index, daily_close_px["MSFT"], label="Adjusted Close")
    # plt.title("MSFT Adjusted Close Price from 2011 - 2014")
    # plt.legend(loc=2)
    # bottom = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
    # bottom.bar(msftV.index, msftV)
    # plt.title("Microsoft Daily Trading Volume")
    # plt.gcf().set_size_inches(12, 8)
    # plt.subplots_adjust(hspace=0.75)
    # plt.savefig("results/5104OS_05_04.png", bbox_inches="tight", dpi=300)

    AA_p_t0 = daily_close_px.iloc[0]["AA"]
    AA_p_t1 = daily_close_px.iloc[1]["AA"]
    r_t1 = AA_p_t1 / AA_p_t0 - 1
    print(AA_p_t0, AA_p_t1, r_t1)

    price_matrix_minus_day1 = daily_close_px.iloc[1:]
    print(price_matrix_minus_day1[:5])


if __name__ == "__main__":
    main()
