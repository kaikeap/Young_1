import requests as r

from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/start/esport/'
page = r.get(url)
print(page.content)