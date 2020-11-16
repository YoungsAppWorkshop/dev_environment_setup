#!/usr/bin/env python3
"""     p. 97 ~
"""
from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt

ticker = ['MSFT']
begdate = '2016-11-10'
enddate = '2016-12-31'

data_source = 'google'
mydata = data.DataReader(ticker, data_source, begdate, enddate)
price = mydata.ix['Close']
all_weekdays = pd.date_range(start=begdate, end=enddate, freq='B')
price = price.reindex(all_weekdays)
price = price.fillna(fethod='ffill')
stock = price.ix[:, ticker]

moving_average = stock.rolling(window=10).mean()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(stock.index, stock, label=ticker)
ax.plot(moving_average.index, moving_average, label='10-day moving average')
ax.set_xlabel('Date')
ax.set_ylabel('Closing Price')
ax.legend()
fig.autofmt_xdate()
plt.show()
