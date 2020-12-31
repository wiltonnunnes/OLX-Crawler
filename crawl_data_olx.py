import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = 1

while True:
  r = requests.get('https://rn.olx.com.br/?o={page}'.format(page=page), headers=headers)
  soup = BeautifulSoup(r.text, 'html.parser')

  for link in soup.find('ul', id='ad-list').find_all('a'):
    print(link['title'])

  if len(soup(string='Última pagina')) == 0:
    break

  page += 1