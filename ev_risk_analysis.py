import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn
import numpy as np


# Comparing EV Automakers
tickers  = ["NIO", "TSLA","JCI"]
#tickers  = ["XPEV", "KARS","IDRV","MP","LI","JCI"]
#tickers  = ["XPEV", "KARS","IDRV","MP","LI","JCI","ARVL","F","FSK","CPS","LEA","MGA","FREY","NRG","NVVE","NKLA","QS","IPWR","FSR","BEEM","AVAV","LEV","ABM","HYLN","ELMS"]



# Fetching Data
stocks = yf.download(tickers, start= "2018-01-01", end = "2021-01-01")
data = stocks.loc[:, "Close"].copy()


# Percentage change
print(data.head())
print(data.pct_change())


# Drop null value, get statistics
compare = data.pct_change().dropna()
print(compare.describe())



# Isolate stddev and mean
sum  = compare.describe().T.loc[:,['mean','std']]
print(sum)

# Convert to whole trading year
sum['mean']= sum['mean']*252
sum['std']= sum["std"]*np.sqrt(252)
print("Yearly :\n ", sum)


# Plotting 
sum.plot.scatter(x = "std", y = "mean", figsize = (12,8), s = 50 , fontsize = 14)
'''
for i in sum.index:
	plt.annotate(i, xy=(sum.loc[i,"std"]+0.002, sum.loc[i, "mean"]+0.002),size= 14)

'''
