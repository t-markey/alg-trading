import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import csv



def ticker_check(tttt):
	
	# Check Nasdaq for ticker symbol
	with open ('nasdaq-listed_csv.csv', 'r') as csvfile:
		listings = csv.reader(csvfile, delimiter=',')
		for row in listings:
			if tttt in row:
				return row
		
	
	# Check Nyse for ticker symbol
	with open ('nyse-listed_csv.csv', 'r') as csvfile:
		listings = csv.reader(csvfile, delimiter=',')
		for row in listings:
			if tttt in row:
				return row

	return False
	

def year_check(yyyy , date_begin , date_end):
	try:
		aapl= yf.download(ticker,date_begin, date_end)
		year_valid= True
		return True
	except Exception as ex:
		print(ex)
		print('-No Data Available-')






# User input Equity to compare
ticker_valid = False
print('Enter Ticker to show Correlation to S&P 500 : ')
while ticker_valid == False:
	ticker =input()
	ticker_valid = ticker_check(ticker)
	if ticker_valid is not False:
		ticker_company= ticker_valid[1]
		break
	else:
		print('%s is not a valid stock ticker, Enter another :'% ticker)


# User input year to examine
print('Enter Year : ' )
year_valid =False
while year_valid == False:
	year = input()
	year_end = int(year) + 1
	date_start  = str( year) + "-01-01"
	date_finish  = str(year_end) + "-01-01"
	year_valid = year_check(ticker, date_start , date_finish)




# add error checking for year (old ass years outside of scope, or current year))
# add error yaer must be a year
# add multiple tickers
# add time period



# Get data from yahoo finance
aapl= yf.download(ticker,date_start, date_finish)
spx = yf.download('^GSPC',date_start, date_finish)
aapl['daily_percent_change'] = aapl['Adj Close'].pct_change()
spx['daily_percent_change'] = spx['Adj Close'].pct_change()


# Compute spearman correlation
# Will return values -1 to 1
# .7 to  1.0 highly positive correlation
# -.7 to -1.0 very negatively correlated, one goes up, the other down 
correlation, _ = spearmanr(aapl.daily_percent_change.dropna(),spx.daily_percent_change.dropna())
print('Spearmans correlation is %.2f' % correlation)




# Scatter plot Comparing Equity percent change to SPX
plt.figure(figsize=(10,7))
plt.scatter(aapl.daily_percent_change,spx.daily_percent_change)
plt.xlabel('%s Daily Returns'%ticker )
plt.ylabel('SPY Daily Returns')
plt.grid()
plt.title('%s Vs. SPY \n Correlation between %s and the S&P500 is %s '%(ticker, ticker_company, correlation))
plt.show()



