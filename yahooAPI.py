import urllib.request as request

data = request.urlopen("http://table.finance.yahoo.com/table.csv?s=600000.ss")
data = data.read().decode()

print(data)