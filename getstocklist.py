from bs4 import BeautifulSoup
import urllib.request as request

data = request.urlopen('http://bbs.10jqka.com.cn/codelist.html#sh')
page = data.read().decode('gbk')

soup = BeautifulSoup(page)
for li in soup.find_all('li'):
	if li.a:
		#print(li.a)
		href = li.a.get('href')
		if href and ('sz' in href or 'sh' in href) and li.a.get('target'):
			print(li.a.get_text())