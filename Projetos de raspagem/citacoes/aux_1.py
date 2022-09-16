import requests
from bs4 import BeautifulSoup

def raspar_texto(url):
    '''-Função que raspa o texto de uma pagina web
       -Recebe como parametro a URL da pagina'''
    pagina = requests.get(url)
    obj = BeautifulSoup(pagina.text,'html.parser')
    lista_citacoes = obj.find_all('p',class_= "frase fr")
    for tag in lista_citacoes:
        print(tag.text.strip())
    # return lista_citacoes.text()
    
a = "charles chaplin"
a.replace(" ","_")