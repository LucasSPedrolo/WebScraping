from bs4 import BeautifulSoup
import html5lib
from requests import get

pagina = get('https://pt.wikipedia.org/wiki/Persistência_(ciência_da_computação)')
soup = BeautifulSoup(pagina.text,'html5lib')

print(f"Página principal : {soup.find('title').text}")

#busca links nos textos principais
subtitulosP1 = soup.find_all('a',attrs = {'class':'mw-redirect'})

#busca links em textos secundarios
subtitulosP2 = soup.find_all('a',attrs = {'class':'extiw'})

#pega apenas o conteudo em 'href'
link = [link.get('href') for link in subtitulosP1 + subtitulosP2]

#adiciona o resto do link ao /wiki/,assim o link funciona

links = []
for item in link:
  if 'https://en.wikipedia.org' in item:
    idlink = item
    links.append(idlink)
  elif not 'wikipedia.org/wiki/' or 'htpps' or 'http' or 'www' in item:
    idlink = 'https://pt.wikipedia.org' + item
    links.append(idlink)
  else:
    links.append(item)

#remove links duplicados
links = set(links)

paraVisitar = []
for item in links:
  rd = item
  item = get(rd)
  soup = BeautifulSoup(item.text,'html5lib')
  nomesSites = soup.find('title').text
  paraVisitar.append(nomesSites)

['Pagina Secundaria : ' + item for item in paraVisitar]
