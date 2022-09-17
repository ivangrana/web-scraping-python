import requests
from bs4 import BeautifulSoup

#arquivo auxiliar de funções

def raspar_texto(url):
    '''-Função que raspa o texto de uma pagina web
       -Recebe como parametro a URL da pagina'''
    pagina = requests.get(url) #Request GET para a pagina que será raspada
    soup = BeautifulSoup(pagina.text,'html.parser') #Objeto BeautifulSoup
    lista_citacoes = soup.find_all('p',class_= "frase fr") #Acha todas as frases que estão na tag '<p>
    for tag in lista_citacoes: #Loop FOR para retornar todas as citações da página
        print(tag.text.strip(),"|")