import requests
from bs4 import BeautifulSoup
import sqlite3 as sqlt
#arquivo auxiliar de funções

def criar_bd():
    conn = sqlt.connect("frases.bd")
    cur = sqlt.Cursor(conn)

def raspar_texto(url):
    lista_final = []
    '''-Função que raspa o texto de uma pagina web
       -Recebe como parametro a URL da pagina'''
    pagina = requests.get(url) #Request GET para a pagina que será raspada
    soup = BeautifulSoup(pagina.text,'html.parser') #Objeto BeautifulSoup
    lista_citacoes = soup.find_all('p',class_= "frase fr") #Acha todas as frases que estão na tag '<p>
    for tag in lista_citacoes: #Loop FOR para retornar todas as citações da página
        lista_final.append(tag.text.strip())
    return lista_final
