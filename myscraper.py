import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.pichau.com.br/hardware/ssd"

site = requests.get(url)

if response.status_code == 200:

 soup = BeautifulSoup(site.content, "html.parser")
 placas = soup. find_all('div', class_="MuiCardContent-root jss131")
 ultimaPagina