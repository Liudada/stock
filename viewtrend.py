import sqlite3
import sys
from matplotlib import pyplot as plt
from matplotlib import dates
from dateutil.parser import *

conn = sqlite3.connect('stock.db')
c = conn.cursor()

print(c.execute('SELECT sql FROM sqlite_master WHERE type="table"').fetchall())

stocks_num = c.execute('SELECT DISTINCT number FROM stocks')
stocks = []
for stock_num in stocks_num:
	stocks.append(stock_num[0])

if len(sys.argv) > 1:
	stock_search = sys.argv[1]
else:
	stock_search = stocks[0]
stock = c.execute("SELECT number, date, open, high, low, close, volume, adj close FROM stocks WHERE number='"+stocks[0]+"'")
dateaxis = []
opens = []
highs = []
lows = []
closes = []
volumes = []
adjcloses = []
for row in stock:
	dateaxis.append(parse(row[1]))
	opens.append(float(row[2]))
	highs.append(float(row[3]))
	lows.append(float(row[4]))
	closes.append(float(row[5]))
	volumes.append(float(row[6]))
	adjcloses.append(float(row[7]))
plt.figure()
plt.plot(dateaxis, opens, label='open')
plt.plot(dateaxis, highs, label='high')
plt.plot(dateaxis, lows, label='low')
plt.plot(dateaxis, closes, label='close')
plt.plot(dateaxis, adjcloses, label='adj close')
plt.legend()
plt.figure()
plt.plot(dateaxis, volumes, label='volume')
plt.show()