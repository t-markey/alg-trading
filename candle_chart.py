import yfinance as yf
import plotly.graph_objects as go




tesla = yf.Ticker('TSLA')
historic  = tesla.history(start = '2020-10-13', end = '2021-10-13')


#tesla. sustainability
#tesla.calendar
#tesla.isin
#print(tesla.info)






# Reset index of data and convert columns to float
historic = historic.reset_index()
for i in ['Open', 'High', 'Close', 'Low']: 
      historic[i]  =  historic[i].astype('float64')

# Change candlestick to Ohlc
fig = go.Figure(data=[go.Candlestick(x=historic['Date'],open=historic['Open'],high=historic['High'],low=historic['Low'],close=historic['Close'])])

fig.show()





























