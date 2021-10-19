import yfinance as yf
import mplfinance as mpf
# https://github.com/matplotlib/mplfinance
from datetime import datetime, timedelta, date


#get previous days chart
today = date.today()
time_delta = timedelta(days = 1)
if today == 0:
	interval_end = str(today-time_delta*2)
	interval_start  = str(today-time_delta*3)

else:
	interval_end = str(today)
	interval_start  = str(today-time_delta)


# Need to make it so it only does previous trading day




tsla = yf.Ticker("TSLA")
#print(tsla.history(period='5d', actions=False))
data =tsla.history(start=interval_start,end=interval_end, interval='5m', actions = False)
data.index.name = 'Date'
data.shape
data.head(3)
data.tail(3)


mpf.plot(data, type='candle', mav = (3,8,12), volume=True)









