import requests
from bs4 import BeautifulSoup

url = 'https://psxbrasil.com.br/capcom-revela-melhorias-em-street-fighter-6-com-o-patch-de-elena/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lista =['elena']

for paragrafo in soup.find_all('body'):
    for palavra in lista:
        for paragrafo_str in paragrafo.stripped_strings:
            if palavra.upper() in str(paragrafo_str).upper():
                print('NOTÍCIA SOBRE: ', palavra.upper(), '\n', paragrafo_str, '\n')
                break