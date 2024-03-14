import requests
from bs4 import BeautifulSoup

# Url pra scrappar
url = ('https://www.google.com/localservices/prolist?g2lbs'
       '=AIQllVxtJ9GN10B4mq4xEqV1h2KpitQYIg2xgOToc1Chiz9e88rXZyx6HssH5Lv4sTzHjsw3Hvuoi8IXiyWR'
       '-sYmBsm8Mfs1lQPUO1bLWD6kif7JJWMewW4%3D&hl=pt-BR&gl=br&cs=1&ssta=1&q=advogados%20ub%C3%A1&oq=advogados%20ub%C3'
       '%A1&slp'
       '=MgA6HENoTUlnNGZMbE8zeWhBTVZCS21EQngzZU5nX0NSAggCYACSAbcCCg0vZy8xMWptN24yM3FoCg0vZy8xMWpfcWR5dm0xCg0vZy8xMW12NGhjcnNrCg0vZy8xMWo2MDBfdzJuCg0vZy8xMXE4OTVtYjBmCg0vZy8xMXZqNjZ4bnQ5Cg0vZy8xMXN3enFkel92Cg0vZy8xMXBjZjM2NDJoCg0vZy8xMWI2cDY4c3cyCgwvZy8xaGMxZzNwczIKDS9nLzExZzBtc2w1cTYKDS9nLzExbXRuMjIyNmoKDS9nLzExZmtyMXo4cXEKDS9nLzExbXh6ZzdfX2oKDS9nLzExcHY2N2w2dGMKDS9nLzExc3czNzg5MXEKDS9nLzExc3R5bnFyYmwKDS9nLzExa3JfMWs5Z2MKDS9nLzExZ2dzazg0MHgKDS9nLzExcTk1YmdjMzgSBBICCAESBAoCCAGaAQYKAhcZEAA%3D&src=2&serdesk=1&sa=X&ved=2ahUKEwjLy8WU7fKEAxXL9wIHHd_ZDWgQjGp6BAgiEAE&scp=ChpnY2lkOmNyaW1pbmFsX2xhd19hdHRvcm5leRJGEhIJ0dkPI1oZowARMdqbTYsZmzEaEglZZ3Z5gxujABH5V61vKAinjSIEVWLDoSoUDS_MZfMVdDFi5h05_m3zJT4Xb-YwABoJYWR2b2dhZG9zIg5hZHZvZ2Fkb3MgdWLDoSoRQWR2b2dhZG8gY3JpbWluYWw%3D&lci=120')

classe_alvo = 'deyx8d'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elementos = soup.find_all(class_=classe_alvo)

for elemento in elementos:
    print(elemento.text)