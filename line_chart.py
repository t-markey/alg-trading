import yfinance as yf
import plotly.express as px


shak =yf.Ticker('SHAK')
historic = shak.history(start = "2021-07-01" , end= "2021-10-02" )
historic = historic.reset_index()
for i in ['Open', 'High', 'Close', 'Low']: 
      historic[i]  =  historic[i].astype('float64')







line= px.line(historic, x="Date", y="Open", title= "Shake Shak Past 3 months")
line.show()





















