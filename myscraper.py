import requests
from bs4 import BeautifulSoup

url = "https://www.pichau.com.br/hardware/ssd"

site = requests.get(url)

soup = BeautifulSoup(site.content, "html.parser")
placas = soup.find_all('div', class_="MuiCardContent-root jss131")
ultimaPagina = soup.find('button', class_='text-page last')
marca = placas[0].find('a', class_='list_product')

print(marca)
