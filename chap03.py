import numpy as np
import pandas as pd


def main():
    msft = pd.read_csv("data/msft.csv", index_col=0, parse_dates=True)
    aapl = pd.read_csv("data/aapl.csv", index_col=0, parse_dates=True)
    print(msft.info())
    print(aapl.info())
    print(msft[:3])
    print(aapl[:3])

    msftA01 = msft["2012-01"][["Adj Close"]]
    msftA02 = msft["2012-02"][["Adj Close"]]
    print(msftA01[:3])
    print(pd.concat([msftA01.head(3), msftA02.head(3)]))
    print(msft["2012"][["Adj Close"]].head(5))

    msftA01R = msftA01.reset_index()
    print(msftA01.head(3))
    print(msftA01R.head(3))


if __name__ == "__main__":
    main()
