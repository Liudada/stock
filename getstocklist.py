from bs4 import BeautifulSoup
import urllib.request as request
import urllib
import sqlite3

conn = sqlite3.connect('stock.db')
c = conn.cursor()
# c.execute('''CREATE TABLE stocks
#	(name, number, date, open, high, low, close, volume, adj close)''')

data = request.urlopen('http://bbs.10jqka.com.cn/codelist.html#sh')
page = data.read().decode('gbk')

soup = BeautifulSoup(page)
for li in soup.find_all('li'):
	if li.a:
		href = li.a.get('href')
		if href and ('sz' in href or 'sh' in href) and li.a.get('target'):
			stock = li.a.get_text().split()
			if len(stock) > 2:
				name = ' '.join(stock[:-1])
				number = stock[-1]
			else:
				name = stock[0]
				number = stock[1]
			print(number)
			if 'sz' in href:
				sufix = '.sz'
			else:
				sufix = '.ss'
			try:
				stockdata = request.urlopen("http://table.finance.yahoo.com/table.csv?s="+number+sufix)
				stockdata = stockdata.read().decode().split("\n")[1:-1]
				stockdata = [tuple([name,number]+[l.split(',')[0]]+[float(i) for i in l.split(',')[1:]]) for l in stockdata]
				c.executemany("INSERT INTO stocks VALUES (?,?,?,?,?,?,?,?,?)",stockdata)
			except urllib.error.HTTPError:
				print('Not found')
				pass

conn.commit()
conn.close()