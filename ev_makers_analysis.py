import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

# Comparing EV Automakers
tickers  = ["NIO", "TSLA","JCI"]
#tickers  = ["XPEV", "KARS","IDRV","MP","LI","JCI"]
#tickers  = ["XPEV", "KARS","IDRV","MP","LI","JCI","ARVL","F","FSK","CPS","LEA","MGA","FREY","NRG","NVVE","NKLA","QS","IPWR","FSR","BEEM","AVAV","LEV","ABM","HYLN","ELMS"]



# Fetching Data
stocks = yf.download(tickers, start= "2020-01-01", end = "2021-01-01")
data = stocks.loc[:, "Close"].copy()

'''
#Plotting data
data.plot(figsize =( 12, 8 ), fontsize = 20)
print(type(data))
plt.style.use("seaborn")
plt.show()

#Normalizing Data
data.head()
#Select first row
data.iloc[0]
# Divide values
display(data.div(data.iloc[0]).mul(100))
'''




#Plot Normalized-ish data first value
norm_data = data.div(data.iloc[0]).mul(100)
norm_data.plot(figsize= (8,6), fontsize = 12)
plt.style.use("seaborn")
plt.show()

#Frequency of Percentage change
tsla = norm_data.TSLA.copy().to_frame()
ret = tsla.pct_change().dropna()

ret.plot(kind = "hist",figsize =(12,8), bins = 100)
plt.show()




 
