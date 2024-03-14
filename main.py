import requests
from bs4 import BeautifulSoup

# Url pra scrappar
url = ('')
# Classe pra filtrar na URL
classe_alvo = ''

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elementos = soup.find_all(class_=classe_alvo)

for elemento in elementos:
    print(elemento.text)