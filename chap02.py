import numpy as np
import pandas as pd


def main():
    sp500 = pd.read_csv("data/sp500.csv", index_col="Symbol", usecols=[0, 2, 3, 7])
    print(sp500.info())
    print(sp500.head())
    print(sp500["Price"].head())
    print(sp500.loc["ABT"])
    print(sp500.at["MMM", "Price"])
    print(sp500.iat[0, 1])
    print(sp500[sp500.Price < 100])
    print(sp500[(sp500.Price < 10) & (sp500.Price > 0)][["Price", "Book Value"]])

    np.random.seed(100)
    df = pd.DataFrame(np.random.randn(5, 4), columns=["a", "b", "c", "d"])
    print(df - df.iloc[0])
    print(df[1:4][["b", "c"]])


if __name__ == "__main__":
    main()
