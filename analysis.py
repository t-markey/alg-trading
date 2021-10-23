import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# Comparing EV Automakers
stock = ["NIO", "TSLA","XPEV"]



# Fetching Data
yf.download(stock, start= "2020-01-01", end = "2021-01-01")
data = stock.loc[:, "Close"].copy()







