import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://webscraper.io/test-sites/e-commerce/allinone') #pagina que será raspada
soup_objeto = BeautifulSoup(pagina.text,'html.parser') #Criação de um objeto 
texts = soup_objeto.find('body')
texts = texts.get_text()
print(texts)

#Criação de um arquivo .txt para armazenar o texto raspado

